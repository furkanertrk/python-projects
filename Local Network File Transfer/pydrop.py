import socket
import os
import sys
import tqdm  # İlerleme çubuğu için

# Ayarlar
SEPARATOR = "<SEPARATOR>"
BUFFER_SIZE = 4096 * 4  # 16KB'lık paketler halinde gönder (Hız için artırılabilir)
PORT = 5001             # Transferin yapılacağı kapı numarası

def get_local_ip():
    """Bilgisayarın yerel ağdaki (Wi-Fi/Ethernet) IP adresini bulur"""
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(('8.8.8.8', 80))
        IP = s.getsockname()[0]
    except Exception:
        IP = '127.0.0.1'
    finally:
        s.close()
    return IP

def send_file():
    """GÖNDERİCİ MODU (Client)"""
    # 1. Dosya Seçimi
    filename = input("Gönderilecek dosyanın tam yolunu yapıştır (veya sürükle bırak): ").replace('"', '')
    
    if not os.path.exists(filename):
        print("❌ Dosya bulunamadı!")
        return

    filesize = os.path.getsize(filename)
    
    # 2. Hedef Belirleme
    target_ip = input("Alıcı bilgisayarın IP adresi nedir? (Örn: 192.168.1.x): ")

    print(f"\n🚀 {target_ip} adresine bağlanılıyor...")
    
    try:
        # 3. Bağlantı Kurma (TCP Socket)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target_ip, PORT))
        print("✅ Bağlantı başarılı!")

        # 4. Metadata Gönderme (Dosya Adı ve Boyutu)
        # os.path.basename ile sadece dosya adını al (C:\Users\...\foto.jpg -> foto.jpg)
        file_name_only = os.path.basename(filename)
        
        # Bilgiyi şu formatta gönderiyoruz: "dosya.jpg<SEPARATOR>102450"
        s.send(f"{file_name_only}{SEPARATOR}{filesize}".encode('utf-8'))

        # 5. Dosya Transferi
        progress = tqdm.tqdm(range(filesize), f"Gönderiliyor: {file_name_only}", unit="B", unit_scale=True, unit_divisor=1024)

        with open(filename, "rb") as f:
            while True:
                # Dosyadan bir parça oku
                bytes_read = f.read(BUFFER_SIZE)
                if not bytes_read:
                    break # Dosya bitti
                
                s.sendall(bytes_read)
                progress.update(len(bytes_read))

        s.close()
        print("\n🎉 Dosya başarıyla gönderildi!")

    except Exception as e:
        print(f"\n❌ Hata oluştu: {e}")

def receive_file():
    """ALICI MODU (Server)"""
    # 1. Sunucuyu Başlat
    my_ip = get_local_ip()
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Portu dinlemeye başla
    s.bind(('0.0.0.0', PORT))
    s.listen(5)
    
    print(f"\n📡 ALICI MODU AKTİF")
    print(f"🔗 Senin IP Adresin: {my_ip}")
    print(f"👂 {PORT} portundan dosya bekleniyor... (Göndericiye bu IP'yi ver)\n")

    # 2. Bağlantı Kabul Et
    client_socket, address = s.accept()
    print(f"✅ {address} cihazı bağlandı!")

    # 3. Metadata Al (Dosya adı ve boyutu)
    received = client_socket.recv(BUFFER_SIZE).decode('utf-8')
    filename, filesize = received.split(SEPARATOR)
    
    # Dosya adını temizle (sadece ismini al)
    filename = os.path.basename(filename)
    filesize = int(filesize)

    # 4. Dosyayı Yazmaya Başla
    # Çakışmayı önlemek için başına 'gelen_' ekleyelim
    output_name = f"gelen_{filename}"
    
    progress = tqdm.tqdm(range(filesize), f"Alınıyor: {filename}", unit="B", unit_scale=True, unit_divisor=1024)

    with open(output_name, "wb") as f:
        while True:
            # Soketten veri oku
            bytes_read = client_socket.recv(BUFFER_SIZE)
            
            if not bytes_read:    
                break # Veri akışı bitti

            f.write(bytes_read)
            progress.update(len(bytes_read))

    # 5. Kapat
    client_socket.close()
    s.close()
    print(f"\n🎉 Dosya başarıyla alındı ve kaydedildi: {output_name}")

def main():
    print("--- PYDROP: Local File Transfer ---")
    print("[1] Dosya Gönder (Sender)")
    print("[2] Dosya Al (Receiver)")
    
    choice = input("Seçiminiz (1/2): ")
    
    if choice == '1':
        send_file()
    elif choice == '2':
        receive_file()
    else:
        print("Geçersiz seçim.")

if __name__ == "__main__":
    main()