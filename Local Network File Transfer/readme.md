# PyDrop - Yerel Ağda Dosya Transfer Aracı

PyDrop, aynı Wi-Fi veya kablolu ağa bağlı iki bilgisayar arasında kolayca dosya göndermenizi ve almanızı sağlayan bir komut satırı aracıdır.

## Ne İşe Yarar?
- Büyük dosyaları USB bellek veya internet kullanmadan hızlıca transfer etmenizi sağlar.
- Basit bir arayüz ile bir bilgisayarı "Alıcı" moduna, diğerini "Gönderici" moduna geçirerek çalışır.
- Dosya transferi sırasında hızı ve ilerlemeyi gösteren bir ilerleme çubuğu sunar.

## Gereksinimler
- Python 3.x
- `tqdm` kütüphanesi (ilerleme çubuğu için). Yüklemek için:
  ```bash
  pip install tqdm
  ```
- İki bilgisayarın da aynı yerel ağa (örneğin aynı modeme) bağlı olması.
- Güvenlik duvarınızın (Firewall) Python uygulamalarına veya belirtilen porta (varsayılan: 5001) izin verdiğinden emin olun.

## Kullanım

### Adım 1: Alıcı Bilgisayarı Hazırlama
1.  **Script'i çalıştırın:** Dosyayı alacak olan bilgisayarda bir terminal açın ve komutu girin:
    ```bash
    python pydrop.py
    ```
2.  **Modu Seçin:** Program size hangi modda çalışmak istediğinizi soracaktır. `2` yazarak "Alıcı" modunu seçin.
    ```
    --- PyDrop Dosya Transfer ---
    [1] Dosya Gönder (Gönderici)
    [2] Dosya Bekle (Alıcı)
    Seçiminiz: 2
    ```
3.  **IP Adresini Not Alın:** Program ekranınıza o bilgisayarın IP adresini yazdıracaktır. Bu adresi gönderici bilgisayarda kullanacaksınız.
    ```
    📡 ALICI MODU AKTİF
    🔗 Senin IP Adresin: 192.168.1.45
    👂 5001 portundan dosya bekleniyor... (Göndericiye bu IP'yi ver)
    ```
    *Alıcı bilgisayar artık dosya bekliyor.*

### Adım 2: Gönderici Bilgisayardan Dosyayı Yollama
1.  **Script'i çalıştırın:** Dosyayı gönderecek olan bilgisayarda da `pydrop.py`'ı çalıştırın.
2.  **Modu Seçin:** Bu kez `1` yazarak "Gönderici" modunu seçin.
3.  **Dosya Yolunu Girin:** Göndermek istediğiniz dosyanın tam yolunu terminale yapıştırın. (İpucu: Dosyayı terminal penceresine sürükleyip bırakabilirsiniz.)
    ```
    Gönderilecek dosyanın tam yolunu yapıştır (veya sürükle bırak): C:\Users\Kullanici\Belgeler\proje.zip
    ```
4.  **Hedef IP'yi Girin:** Alıcı bilgisayarın ekranında gördüğünüz IP adresini buraya girin.
    ```
    Alıcı bilgisayarın IP adresi nedir? (Örn: 192.168.1.x): 192.168.1.45
    ```
5.  **Transferi İzleyin:** Bağlantı kurulduğunda dosya transferi başlayacak ve bir ilerleme çubuğu ile durumu takip edebileceksiniz.

Transfer tamamlandığında, gönderilen dosya alıcı bilgisayardaki `pydrop.py`'ın bulunduğu klasörde `gelen_proje.zip` adıyla görünecektir.