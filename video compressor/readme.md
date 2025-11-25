# Video Compressor

Video dosyalarını sıkıştırmak için kullanılan script.

Dosya
- `videocompressor.py` — video sıkıştırma işlemini yapan script.

Gereksinimler
- Python 3.x
- Video işleme/kodlama araçları (`ffmpeg` sistem aracını kullanan scriptler olabilir). `ffmpeg` yüklü değilse yükleyin ve PATH'e ekleyin.

Kullanım (genel)
- `python videocompressor.py <girdi_dosyası> <çıktı_dosyası> [--bitrate 1000k]`
- Script içinde yer alan argümanları kontrol edin; burada genel bir örnek sağlanmıştır.

Not
- `ffmpeg` kullanıyorsa, sisteminizde yüklü olmalıdır.
- Hukuki/kopyalama dikkati: telif hakkı olan videoları izinsiz işlemeyin.