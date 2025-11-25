# Gelişmiş Sistem Monitörü Paneli (Dashboard)

Bu script, bilgisayarınızın anlık sistem kaynak kullanımını (CPU, RAM, GPU, Disk, Ağ) terminalinizde şık ve okunabilir bir panel (dashboard) formatında canlı olarak gösterir.

## Ne İşe Yarar?
- **CPU:** Genel ve çekirdek bazında anlık kullanımı, işlemci frekansını ve işlem sayısını gösterir.
- **RAM:** Toplam, kullanılan ve boşta olan bellek miktarını görsel bir bar ile birlikte sunar.
- **GPU (NVIDIA):** NVIDIA ekran kartınız varsa; kullanım, bellek kullanımı, sıcaklık ve fan hızı gibi detaylı bilgileri gösterir.
- **Disk:** Tüm disk sürücülerinizin toplam boyutunu, kullanılan ve boş alanı listeler.
- **Ağ:** Anlık indirme (download) ve yükleme (upload) hızlarınızı gösterir.
- **İşlemler (Processes):** En çok CPU ve RAM tüketen ilk 10 işlemi listeler.

## Gereksinimler
- Python 3.x
- **(İsteğe Bağlı) NVIDIA Ekran Kartı:** GPU bilgilerinin gösterilebilmesi için gereklidir.
- Gerekli kütüphaneler. Hepsini tek komutla yüklemek için:
  ```bash
  pip install psutil pynvml rich
  ```
  *(Eğer NVIDIA kartınız yoksa `pynvml` kurmanıza gerek yoktur, script yine de çalışacaktır.)*

## Kullanım
1.  **Terminali Açın:** Script'in bulunduğu klasöre gidin.
2.  **Script'i Çalıştırın:**
    ```bash
    python system_monitor.py
    ```
3.  **Canlı Paneli İzleyin:** Terminal ekranınız temizlenecek ve sistem bilgileri her saniye güncellenerek canlı bir şekilde size sunulacaktır.
4.  **Çıkmak için:** `CTRL + C` tuş kombinasyonuna basın.

## Ekran Görüntüsü (Temsili)
```
+---------------------------------------------------------------------------------+
| 💻 Sistem Paneli - 2025-11-25 14:30:00                                           |
+---------------------------------------------------------------------------------+
| ⚡ CPU (İşlemci)         | 💾 RAM (Bellek)               | 🎮 GPU (NVIDIA)           |
|-------------------------|-------------------------------|---------------------------|
| Genel Kullanım: %25.4   | RAM Kullanımı: █████░░░░░ %50 | GPU Kullanımı: %15        |
| Frekans: 3400 MHz       | Toplam: 15.6 GB               | Bellek: 2.1 / 8.0 GB      |
| Çekirdek 1: %30 ███░░    | Kullanılan: 7.8 GB            | Sıcaklık: 45°C            |
| Çekirdek 2: %20 ██░░░    | Boşta: 7.8 GB                 | Fan Hızı: %30             |
+---------------------------------------------------------------------------------+
| 💿 Disk Kullanımı                                                               |
+---------------------------------------------------------------------------------+
| C:\    Total: 465 GB   Used: 120 GB    Free: 345 GB                             |
| D:\    Total: 931 GB   Used: 500 GB    Free: 431 GB                             |
+---------------------------------------------------------------------------------+
```