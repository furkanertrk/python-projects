# Foto Compressor

Görüntü dosyalarını sıkıştırmak için kullanılan script.

Dosya
- `main.py` — fotoğraf sıkıştırma işlemini yapan ana script.

Gereksinimler
- Python 3.x
- Görüntü işleme kütüphaneleri (`Pillow`, `opencv-python` vb.) — script başındaki importlara bakın.

Kullanım (genel)
- `python main.py <girdi_dosyası> <çıktı_dosyası> [--quality 75]`
- Script içindeki komut satırı argümanlarını kontrol edin; burada örnek amaçlı genel gösterim verilmiştir.

İpuçları
- Orijinal dosyayı kaybetmemek için önce yedeğini alın.
- Farklı kalite ayarlarını test ederek görsel kalite ve dosya boyutu arasında denge bulun.