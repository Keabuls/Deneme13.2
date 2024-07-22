import sqlite3

# Veritabanı bağlantısı kur
conn = sqlite3.connect('database2.db')
c = conn.cursor()

# Tabloyu sil
c.execute('DROP TABLE IF EXISTS pictures')

# Değişiklikleri kaydet
conn.commit()

# Bağlantıyı kapat
conn.close()
