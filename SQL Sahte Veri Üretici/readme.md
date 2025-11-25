# SQL Sahte Veri Üretici

Bu script, veritabanı tablolarınız için `INSERT INTO` formatında, test amaçlı kullanılabilecek, Türkçe'ye uygun sahte veriler üretir ve bunları bir `.sql` dosyasına kaydeder.

## Ne İşe Yarar?
- Belirttiğiniz sayıda kullanıcı kaydını (Ad, Soyad, Email, Telefon, Şehir, Yaş) otomatik olarak oluşturur.
- Çıktıyı doğrudan SQL veritabanı yönetim araçlarında (SSMS, phpMyAdmin, DBeaver vb.) çalıştırabileceğiniz `.sql` formatında verir.
- Gerçekçi ve Türkçe isimler, şehirler, telefon numaraları üretir.
- Oluşturulan `.sql` dosyası, `Kullanicilar` adında bir tabloya veri eklemek üzere yapılandırılmıştır.

## Gereksinimler
- Python 3.x
- `Faker` kütüphanesi. Yüklemek için:
  ```bash
  pip install Faker
  ```

## Kullanım
1.  **Terminali Açın:** Script'in bulunduğu klasöre gidin.
2.  **Script'i Çalıştırın:**
    ```bash
    python sql_generator.py
    ```
3.  **Üretilecek Veri Sayısını Girin:** Program, sizden kaç adet kullanıcı verisi üretmek istediğinizi soracaktır. Bir sayı girip `Enter`'a basın.
    ```
    Kaç adet kullanıcı üretilsin? (Örn: 100): 500
    ```
4.  **SQL Dosyasını Kullanın:** İşlem tamamlandığında, script'in bulunduğu klasörde `dummy_data.sql` adında bir dosya oluşacaktır. Bu dosyanın içeriğini kopyalayıp veritabanı yönetim aracınızda çalıştırarak sahte verileri tablonuza ekleyebilirsiniz.

    **Örnek `dummy_data.sql` İçeriği:**
    ```sql
    -- Kullanicilar tablosu için otomatik üretildi
    INSERT INTO Kullanicilar (Ad, Soyad, Email, Telefon, Sehir, Yas) VALUES
    ('Ahmet', 'Yılmaz', 'ahmet.yilmaz@example.com', '+90...', 'Ankara', 34),
    ('Ayşe', 'Kaya', 'ayse.kaya@example.org', '+90...', 'İstanbul', 28),
    ...;
    ```

## Ayarlar
- **Tablo Adı ve Kolonlar:** Script içerisindeki `table_name` değişkenini ve `INSERT INTO` sorgusundaki kolon adlarını (`Ad`, `Soyad` vb.) kendi tablonuza uyacak şekilde kolayca değiştirebilirsiniz.