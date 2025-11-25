# Foto Compressor

Bu script, bir klasördeki tüm resim dosyalarını (`.jpg`, `.jpeg`, `.png`, `.bmp`) otomatik olarak algılayıp daha düşük dosya boyutuna sahip yeni versiyonlarını oluşturur.

## Ne İşe Yarar?
- Web siteleri veya e-postalar için resimlerin dosya boyutunu küçültür.
- PNG gibi formatlardaki resimleri daha verimli olan JPEG formatına dönüştürür.
- Orijinal dosyaları korur ve sıkıştırılmış kopyaları `_sikistirilmis.jpg` ekiyle kaydeder.

## Gereksinimler
- Python 3.x
- `Pillow` kütüphanesi. Yüklemek için:
  ```bash
  pip install Pillow
  ```

## Kullanım
1.  **Script'i ve Resimleri Aynı Klasöre Koyun:** `main.py` dosyasını, sıkıştırmak istediğiniz resimlerin bulunduğu klasörün içine kopyalayın.
2.  **Terminali Açın:** O klasörün içindeyken bir terminal veya komut istemi açın.
3.  **Script'i Çalıştırın:**
    ```bash
    python main.py
    ```
4.  **İşlemin Bitmesini Bekleyin:** Script, klasördeki tüm uygun resimleri işleyecek ve her birinin yanına sıkıştırılmış bir kopyasını oluşturacaktır.

    **Örnek Klasör Yapısı:**
    ```
    /Resimlerim
    |-- main.py              <-- Script
    |-- tatil.jpg            <-- Orijinal Resim 1
    |-- dugun.png            <-- Orijinal Resim 2
    |-- tatil_sikistirilmis.jpg  <-- Oluşturulan Sıkıştırılmış Kopya 1
    |-- dugun_sikistirilmis.jpg  <-- Oluşturulan Sıkıştırılmış Kopya 2
    ```

## Ayarlar
- **Kalite:** Script içerisindeki `compress_image` fonksiyonunda bulunan `quality=50` değerini değiştirerek sıkıştırma kalitesini ayarlayabilirsiniz. Değer ne kadar düşük olursa dosya boyutu o kadar küçülür ancak görüntü kalitesi de o kadar düşer. (Örneğin: `quality=75` daha yüksek kalite, `quality=40` daha düşük kalite).