import warnings
warnings.filterwarnings("ignore", category=FutureWarning)
import cv2
from imgbeddings import imgbeddings
from PIL import Image
import sqlite3
import os
os.environ["TF_ENABLE_ONEDNN_OPTS"] = "0" # Hata mesajını engellemek için,genel kod çalışabilirliğine bir etkisi yok
from IPython.display import display
import json
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
import matplotlib.pyplot as plt


""" def detect_and_crop_faces_in_folder(input_folder, output_folder):
    # loading the haar cascade algorithm file into alg variable
    alg = "haarcascade_frontalface_default.xml"
    # passing the algorithm to OpenCV
    haar_cascade = cv2.CascadeClassifier(alg)

    # create output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # iterate through all files in the input folder
    for filename in os.listdir(input_folder):
        if filename.endswith((".jpg", ".png", ".jpeg")): 
            # construct the full path to the image
            image_path = os.path.join(input_folder, filename)

            # reading the image
            img = cv2.imread(image_path)
            if img is None:
                print(f"Error: Image not loaded properly from {image_path}")
                continue

            # creating a black and white version of the image
            gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

            # detecting the faces
            faces = haar_cascade.detectMultiScale(gray_img, scaleFactor=1.05, minNeighbors=2, minSize=(100, 100))

            i = 1
            # for each face detected
            for x, y, w, h in faces:
                # crop the image to select only the face
                cropped_image = img[y:y + h, x:x + w]
                # loading the target image path into target_file_name variable
                target_file_name = os.path.join(output_folder, f"{os.path.splitext(filename)[0]}_face_{i}.jpg")
                cv2.imwrite(target_file_name, cropped_image)
                i += 1

# Örnek kullanım:
input_folder = "dataset"   # İşlenecek resim dosyalarının bulunduğu klasörün yolu
output_folder = "static/result"   # Çıktıların kaydedileceği klasörün yolu """

""" detect_and_crop_faces_in_folder(input_folder, output_folder) """

# connecting to SQLite database
conn = sqlite3.connect('database2.db')
cur = conn.cursor()

# inserting images and embeddings into the database
for picture in os.listdir("static/result"):
    img_path = os.path.join("static/result", picture)
    img = Image.open(img_path)
    ibed = imgbeddings()
    embedding = ibed.to_embeddings(img)
    embedding_json = json.dumps(embedding[0].tolist())
    cur.execute("INSERT INTO pictures (picture, embedding) VALUES (?, ?)", (picture, embedding_json))
    print(f"{picture} added to database")

conn.commit()


""" def find_most_similar_embedding(conn, target_embedding):
    cur = conn.cursor()
    cur.execute("SELECT picture, embedding FROM pictures")

    highest_similarity = -1
    most_similar_image = None
    most_similar_score = 0  # Benzerlik skorunu takip etmek için

    for row in cur.fetchall():
        picture, embedding_json = row
        embedding = np.array(json.loads(embedding_json))

        # Ensure embedding is 1-dimensional (flatten if necessary)
        embedding = np.squeeze(embedding)

        # Calculate cosine similarity
        similarity = cosine_similarity([target_embedding.flatten()], [embedding])[0][0]

        if similarity > highest_similarity:
            highest_similarity = similarity
            most_similar_image = picture
            most_similar_score = similarity  # En yüksek benzerlik skorunu güncelle

    cur.close()
    return most_similar_image, most_similar_score """


# Test operation: finding the most similar embedding
""" file_name = "benhur.jpg"
img = Image.open(file_name)
ibed = imgbeddings()
embedding = ibed.to_embeddings(img)

# finding the most similar embedding from database
conn = sqlite3.connect('database.db')
most_similar_image, similarity_score = find_most_similar_embedding(conn, embedding)

if most_similar_image:
    print(f"Most similar image found: {most_similar_image}")
    print(f"Similarity score: {(similarity_score + 0.10)*100:.2f}")

    img = Image.open("result/" + most_similar_image)
    plt.imshow(img)
    plt.show()
else:
    print("No similar image found")

conn.close() """
