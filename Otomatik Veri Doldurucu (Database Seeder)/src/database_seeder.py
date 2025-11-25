
import mysql.connector
from faker import Faker
import getpass

# Veritabanı bağlantı bilgilerini kullanıcıdan al
def get_db_config():
    """Kullanıcıdan veritabanı bağlantı bilgilerini alır."""
    config = {
        'host': input("Host (genellikle 'localhost'): "),
        'user': input("Veritabanı Kullanıcı Adı: "),
        'password': getpass.getpass("Veritabanı Şifresi: "),
        'database': input("Veritabanı Adı: ")
    }
    return config

# Veritabanı bağlantısı oluştur
def create_db_connection(config):
    """Verilen konfigürasyon ile MySQL veritabanına bağlanır."""
    try:
        connection = mysql.connector.connect(**config)
        print("Veritabanı bağlantısı başarılı!")
        return connection
    except mysql.connector.Error as err:
        print(f"Hata: {err}")
        return None

# Users tablosunu kontrol et ve gerekirse oluştur
def ensure_users_table_exists(connection):
    """'users' tablosunun varlığını kontrol eder, yoksa oluşturur."""
    cursor = connection.cursor()
    try:
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(255) NOT NULL,
                address TEXT,
                phone VARCHAR(255),
                email VARCHAR(255) UNIQUE NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        print("'users' tablosu hazır.")
    except mysql.connector.Error as err:
        print(f"Tablo oluşturulurken hata oluştu: {err}")
    finally:
        cursor.close()

# Sahte veri üret ve veritabanına ekle
def seed_database(connection, count=1000):
    """Belirtilen sayıda sahte kullanıcı verisi üretir ve veritabanına ekler."""
    fake = Faker('tr_TR')  # Türkçe veri üretimi için
    cursor = connection.cursor()
    
    insert_query = "INSERT INTO users (name, address, phone, email) VALUES (%s, %s, %s, %s)"
    
    print(f"{count} adet kullanıcı verisi üretiliyor ve veritabanına ekleniyor...")
    
    for _ in range(count):
        name = fake.name()
        address = fake.address()
        phone = fake.phone_number()
        email = fake.email()
        
        try:
            cursor.execute(insert_query, (name, address, phone, email))
        except mysql.connector.Error as err:
            print(f"Veri eklenirken hata: {err} - {email} zaten olabilir.")
            continue
            
    connection.commit()
    cursor.close()
    print(f"{count} adet kullanıcı başarıyla eklendi!")


def main():
    """Ana program akışını yönetir."""
    db_config = get_db_config()
    connection = create_db_connection(db_config)
    
    if connection and connection.is_connected():
        ensure_users_table_exists(connection)
        seed_database(connection)
        connection.close()
        print("Veritabanı bağlantısı kapatıldı.")

if __name__ == "__main__":
    main()
