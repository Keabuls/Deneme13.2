import sqlite3

# Veritabanı bağlantısı kur
conn = sqlite3.connect('database.db')
c = conn.cursor()

# Tabloyu sil
c.execute('DROP TABLE IF EXISTS sqlite_sequence')

# Değişiklikleri kaydet
conn.commit()

# Bağlantıyı kapat
conn.close()
