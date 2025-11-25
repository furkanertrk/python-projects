# YouTube Playlist Video ve Ses İndirici

Bu script, bir YouTube oynatma listesindeki (playlist) tüm içeriği video veya sadece ses olarak toplu halde indirmenizi sağlar.

## Ne İşe Yarar?
- Müzik listelerini veya eğitim serilerini tek seferde bilgisayarınıza kaydeder.
- Videoları mevcut en yüksek çözünürlükte indirir.
- Sadece ses dosyalarını (`.mp4` formatında, M4A/AAC kodekli) indirerek müzik arşivi oluşturmanıza olanak tanır.
- İndirme sırasında her bir dosya için anlık ilerleme durumunu gösterir.

## Gereksinimler
- Python 3.x
- `pytubefix` kütüphanesi. Yüklemek için:
  ```bash
  pip install pytubefix
  ```

## Kullanım
1.  **Terminali Açın:** Script'in bulunduğu klasöre gidin.
2.  **Script'i Çalıştırın:**
    ```bash
    python "yt playlist indirici.py"
    ```
3.  **Playlist Linkini Yapıştırın:** İndirmek istediğiniz YouTube oynatma listesinin linkini kopyalayıp terminale yapıştırın ve `Enter`'a basın.
    ```
    Playlist Linkini yapistir: https://www.youtube.com/playlist?list=PLxxxxxxxxxxxxxxxx
    ```
4.  **İndirme Formatını Seçin:** Video olarak mı yoksa sadece ses olarak mı indirmek istediğinizi seçin.
    ```
    Playlist Adi: Müzik Listem
    Toplam Video Sayisi: 50
    ----------------------------------------
    1- Tum videolari indir (Izlenebilir En Yuksek Kalite)
    2- Tum sesleri indir (MP3/M4A)
    Seciminiz (1-2): 2
    ```
5.  **İşlemin Bitmesini Bekleyin:** Script, listedeki tüm videoları/sesleri sırayla indirmeye başlayacaktır. İndirilen dosyalar, script'in bulunduğu klasörün içine kaydedilir. Ses dosyalarının adının başına `ses_` ön eki eklenir.

> **⚠️ Telif Hakkı Uyarısı:** Bu aracı yalnızca telif hakkı yasalarına uygun şekilde kullanın. Telif hakkıyla korunan içerikleri sahibinin izni olmadan indirmek ve dağıtmak yasa dışı olabilir. YouTube'un hizmet şartlarına uymak kullanıcının sorumluluğundadır.