Static içerisine result ve upload klasörleri oluşturulmalı

Upload - remove background kullanıldığında asıl fotoğrafın kaydedildiği yer

Result - küçük fotoğrafların kaydedildiği yer , daha sonra buradaki fotoğraflara embedding uygulanarak database2.db ye kaydediliyor

!! Dataset - veritabanına kaydedilecek fotoğrafların bulunduğu kısım

!! Burada bulunmuyor ancak Dataset'teki fotoğrafları Result'a küçük resim olarak kaydetmek istiyorsak app.py'nin en üstünde de bulunan  alg = "haarcascade_frontalface_default.xml" yani bir haarcascade_frontalface_default.xml bizim proje dosyamızda bulunması lazım.


input_folder = "dataset"   # İşlenecek resim dosyalarının bulunduğu klasörün yolu

output_folder = "result"   # Çıktıların kaydedileceği klasörün yolu
