!! Static içerisine result ve uploads klasörleri oluşturulmalı

Upload - remove background kullanıldığında asıl fotoğrafın kaydedildiği yer

Result - küçük fotoğrafların kaydedildiği yer , daha sonra buradaki fotoğraflara embedding uygulanarak database2.db ye kaydediliyor

----------------------------------------------------------------

Dataset - veritabanına kaydedilecek fotoğrafların bulunduğu kısım

Burada bulunmuyor ancak Dataset'teki fotoğrafları Result'a küçük resim olarak kaydetmek istiyorsak app.py'nin en üstünde de bulunan  alg = "haarcascade_frontalface_default.xml" yani bir haarcascade_frontalface_default.xml bizim proje dosyamızda bulunması lazım.

Onu da buradan indirebilirsiniz : https://github.com/kipr/opencv/blob/master/data/haarcascades/haarcascade_frontalface_default.xml

----------------------------------------------------------------

input_folder = "dataset"   # İşlenecek resim dosyalarının bulunduğu klasörün yolu

output_folder = "result"   # Çıktıların kaydedileceği klasörün yolu

----------------------------------------------------------------

Kodu çalıştırmaya başlamadan önce Database klasörünün içerisindeki "create_table.py" ve "createdb2.py" dosyaları çalıştırılmalı.Bunlar "Database.db" ve "Database2.db" isimli iki SQLite veritabanı oluşturacaktır.!! Veritabanlarını VSC'de görüntüleyebilmek için "SQLite Viewer" Extensionunu kurmanız gerek.Database klasörünün içindeki "delete_table.py" ve "deletetable2.py" dosyaları veritabanlarındaki table'ları silmek içindir."Database.db"deki table verilerini isterseniz dinamik olarak silebilirsiniz,bunu yapmak için öncelikle Web sitesine resim yükleyip "Remove Background" butonuna basmanız gerek.Bu işlemler sizi arkaplanı silinmiş dosyaların bulunduğu bir alt siteye yönlendirecek,burada "Database.db"de yer alan verileri istediğiniz gibi silebilirsiniz.

----------------------------------------------------------------





