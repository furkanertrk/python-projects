# MySQL Veritabanı için Otomatik Veri Doldurucu (Seeder)

Bu script, bir MySQL veritabanına test amaçlı olarak hızlıca binlerce sahte kullanıcı verisi (isim, adres, telefon, e-posta) eklemek için kullanılır.

## Ne İşe Yarar?
- Geliştirme aşamasındaki uygulamaların veritabanını test verileriyle doldurur.
- Belirtilen veritabanında `users` adında bir tablo olup olmadığını kontrol eder, eğer yoksa otomatik olarak oluşturur.
- Türkçe'ye uygun, gerçekçi sahte veriler üretir (`tr_TR` yerelleştirmesi ile).
- Etkileşimli olarak kullanıcıdan veritabanı bağlantı bilgilerini (host, kullanıcı, şifre, veritabanı adı) ister.

## Gereksinimler
- Python 3.x
- Çalışan bir MySQL veritabanı sunucusu.
- Gerekli kütüphaneler. Hepsini tek komutla yüklemek için:
  ```bash
  pip install mysql-connector-python Faker
  ```

## Kullanım
1.  **Terminali Açın:** Script'in bulunduğu `src` klasörünün **bir üst dizininde** (proje kök dizininde) bir terminal açın.
2.  **Script'i Çalıştırın:**
    ```bash
    python src/database_seeder.py
    ```
3.  **Veritabanı Bilgilerini Girin:** Program sizden adım adım MySQL sunucunuza ait bağlantı bilgilerini isteyecektir:
    - **Host:** Genellikle `localhost` veya `127.0.0.1`
    - **Veritabanı Kullanıcı Adı:** MySQL kullanıcı adınız (örn: `root`)
    - **Veritabanı Şifresi:** İlgili kullanıcının şifresi (yazarken görünmez)
    - **Veritabanı Adı:** Verilerin ekleneceği veritabanının ismi.
4.  **İşlemin Bitmesini Bekleyin:** Bağlantı başarılı olduğunda, script önce `users` tablosunu kontrol edecek, ardından 1000 adet sahte kullanıcı verisini bu tabloya ekleyecektir.

    ```
    Host (genellikle 'localhost'): localhost
    Veritabanı Kullanıcı Adı: root
    Veritabanı Şifresi:
    Veritabanı Adı: test_db
    Veritabanı bağlantısı başarılı!
    'users' tablosu hazır.
    1000 adet kullanıcı verisi üretiliyor ve veritabanına ekleniyor...
    1000 adet kullanıcı başarıyla eklendi!
    Veritabanı bağlantısı kapatıldı.
    ```

## Ayarlar
- **Eklenecek Veri Sayısı:** Script içerisindeki `seed_database(connection)` satırını `seed_database(connection, count=5000)` şeklinde değiştirerek eklenecek kullanıcı sayısını artırıp azaltabilirsiniz.