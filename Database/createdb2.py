import sqlite3

conn = sqlite3.connect('database2.db')
cur = conn.cursor()

# Tabloyu oluşturma
cur.execute('''
CREATE TABLE IF NOT EXISTS pictures (
    picture TEXT,
    embedding TEXT
)
''')

conn.commit()
cur.close()