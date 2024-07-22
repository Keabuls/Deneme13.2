import sqlite3

conn = sqlite3.connect('database.db')
c = conn.cursor()
c.execute('''
          CREATE TABLE Photos
          (id INTEGER PRIMARY KEY ASC, 
          file_path TEXT NOT NULL)
          ''')
conn.commit()
conn.close()
