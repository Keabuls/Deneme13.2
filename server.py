from flask import Flask, render_template, redirect, url_for,request, g, redirect, url_for
from werkzeug.utils import secure_filename
import sqlite3
import os
os.environ["TF_ENABLE_ONEDNN_OPTS"] = "0" # Hata mesajını engellemek için,genel kod çalışabilirliğine bir etkisi yok
from rembg import new_session, remove
from PIL import Image 
import io
import base64
import numpy as np
import json
from imgbeddings import imgbeddings
from sklearn.metrics.pairwise import cosine_similarity




app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = 'static/uploads/'
app.config['ALLOWED_EXTENSIONS'] = {'png', 'jpg', 'jpeg'}

DATABASE = 'database.db'

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

def query_db(query, args=(), one=False):
    cur = get_db().cursor()
    cur.execute(query, args)
    rv = cur.fetchall()
    cur.close()
    return (rv[0] if rv else None) if one else rv

def get_photo_by_id(photo_id):
    cur = get_db().cursor()
    cur.execute('SELECT file_path FROM photos WHERE id = ?', (photo_id,))
    photo_path = cur.fetchone()
    cur.close()
    return photo_path[0] if photo_path else None

@app.context_processor
def inject_functions():
    return dict(get_photo_by_id=get_photo_by_id)

""" ****************************************************** """

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'files[]' not in request.files:
        return redirect(url_for('index'))
    
    files = request.files.getlist('files[]')

    for file in files:
        if file.filename == '':
            return redirect(url_for('index'))
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename).replace("\\", "/")
            file.save(file_path)
            
            # Arka planı sil ve sonucu /uploads klasörüne kaydet
            model_name = "isnet-general-use"
            session = new_session(model_name)
            input_image = Image.open(file.stream)
            output_image = remove(input_image,session=session)

            output_file_path = os.path.join(app.config['UPLOAD_FOLDER'], 'removed_' + filename)
            output_image.save(output_file_path, format='PNG')

            # Göreceli dosya yolunu kaydet
            relative_file_path = os.path.join('uploads', 'removed_' + filename).replace("\\", "/")
            query_db('INSERT INTO photos (file_path) VALUES (?)', [relative_file_path])
            get_db().commit()

    return redirect(url_for('result'))


def find_top_n_similar_embeddings(conn, target_embedding, n=20): # burada n'e vereceğiniz değer search_result'ta göstereceği fotoğraf sayısını temsil ediyor
    cur = conn.cursor()
    cur.execute("SELECT picture, embedding FROM pictures")

    similarities = []

    for row in cur.fetchall():
        picture, embedding_json = row
        embedding = np.array(json.loads(embedding_json))
        embedding = np.squeeze(embedding)

        similarity = cosine_similarity([target_embedding.flatten()], [embedding])[0][0]
        scaled_similarity = similarity * 100
        rounded_similarity = round(scaled_similarity)

        similarities.append((picture, rounded_similarity))

    # Sort by similarity in descending order and get the top n
    similarities.sort(key=lambda x: x[1], reverse=True)
    top_n_similar_images = similarities[:n]

    cur.close()
    return top_n_similar_images


@app.route('/search_result', methods=['POST'])
def search_file():
    if 'files[]' not in request.files:
        return redirect(request.url)

    files = request.files.getlist('files[]')

    if not any(file.filename for file in files):
        return redirect(url_for('index'))

    conn = sqlite3.connect('database2.db')

    all_results = []

    for file in files:
        if file and file.filename:
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(file.filename))
            file.save(file_path)

            img = Image.open(file_path)
            ibed = imgbeddings()
            embedding = ibed.to_embeddings(img)

            top_images = find_top_n_similar_embeddings(conn, embedding)

            all_results.extend(top_images)

    conn.close()
    
    if all_results:
        return render_template('search.html', results=all_results)
    
    return 'No similar images found', 404



@app.route('/delete', methods=['POST'])
def delete_photo():
    photo_id = request.form['photo_id']
    db = get_db()
    cur = db.cursor()
    cur.execute('DELETE FROM photos WHERE id = ?', [photo_id])
    db.commit()
    cur.close()
    return redirect(url_for('result'))

""" ******************************************************** """

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/home')
def home():
    return redirect(url_for('index'))


@app.route('/result')
def result():
    photo_ids = query_db('SELECT id FROM photos')
    return render_template('result.html',photo_ids=photo_ids)

@app.route('/search')
def search():
    return render_template('search.html')


if __name__ == '__main__':
    app.run(debug=True,port ="5001")
