import random
from faker import Faker

# Türkçe veri üretmesi için ayar
fake = Faker('tr_TR')

def generate_sql_data(record_count=50):
    table_name = "Kullanicilar"
    file_name = "dummy_data.sql"
    
    print(f"⏳ {record_count} adet sahte veri üretiliyor...")
    
    with open(file_name, 'w', encoding='utf-8') as f:
        # Tablo oluşturma kodunu da ekleyelim (İstersen silebilirsin)
        f.write(f"-- {table_name} tablosu için otomatik üretildi\n")
        f.write(f"INSERT INTO {table_name} (Ad, Soyad, Email, Telefon, Sehir, Yas) VALUES\n")
        
        values_list = []
        
        for i in range(record_count):
            # Rastgele veriler oluştur
            ad = fake.first_name()
            soyad = fake.last_name()
            # Email'i isme göre oluşturup tırnak işaretlerini temizleyelim
            email = f"{ad.lower()}.{soyad.lower()}@{fake.free_email_domain()}".replace("'", "")
            telefon = fake.phone_number()
            sehir = fake.city()
            yas = random.randint(18, 65)
            
            # SQL formatına uygun string oluştur
            # Tek tırnak (') içeren isimler SQL'i bozmasın diye kaçış karakteri ekliyoruz
            ad = ad.replace("'", "''")
            soyad = soyad.replace("'", "''")
            
            row = f"('{ad}', '{soyad}', '{email}', '{telefon}', '{sehir}', {yas})"
            values_list.append(row)
            
            # Yüzdelik gösterge
            if i % 10 == 0:
                print(f"İşleniyor... %{int((i/record_count)*100)}", end='\r')

        # Tüm verileri virgülle birleştirip dosyaya yaz
        f.write(",\n".join(values_list) + ";")
    
    print(f"\n✅ Başarılı! SQL kodları '{file_name}' dosyasına kaydedildi.")
    print("📌 İpucu: Bu dosyayı SSMS veya phpMyAdmin'de direkt çalıştırabilirsin.")

if __name__ == "__main__":
    try:
        sayi = int(input("Kaç adet kullanıcı üretilsin? (Örn: 100): "))
        generate_sql_data(sayi)
    except ValueError:
        print("Lütfen sayı giriniz.")