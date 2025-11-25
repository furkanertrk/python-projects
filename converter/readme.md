# Çok Yönlü Dosya Dönüştürücü

Bu script, aynı klasörde bulunan dosyaları farklı formatlara dönüştürmenizi sağlayan interaktif bir araçtır.

## Desteklenen Dönüşümler
- **PDF -> DOCX:** PDF dosyalarınızı düzenlenebilir Word belgesine çevirir.
- **DOCX -> PDF:** Word belgelerinizi PDF formatına dönüştürür. *(Bu işlem için bilgisayarınızda Microsoft Word'ün yüklü olması gerekmektedir.)*
- **Resimden Resime:** `jpg`, `png`, `webp`, `bmp`, `ico` gibi popüler resim formatları arasında karşılıklı dönüşüm yapar.

## Gereksinimler
- Python 3.x
- Gerekli kütüphaneler. Hepsini tek komutla yüklemek için:
  ```bash
  pip install pdf2docx docx2pdf Pillow
  ```

## Kullanım
1.  **Script'i ve Dosyaları Aynı Klasöre Koyun:** `converter.py` dosyasını, dönüştürmek istediğiniz dosyaların bulunduğu klasörün içine kopyalayın.
2.  **Terminali Açın:** O klasörün içindeyken bir terminal veya komut istemi açın.
3.  **Script'i Çalıştırın:**
    ```bash
    python converter.py
    ```
4.  **Dönüştürülecek Dosyayı Seçin:** Script, klasördeki tüm dosyaları listeleyecektir. Dönüştürmek istediğiniz dosyanın başındaki numarayı girip `Enter`'a basın.
    ```
    --- 📂 DÖNÜŞTÜRÜCÜ ASİSTAN ---
    Bulunan dosyalar:
    [1] rapor.docx
    [2] tatil_fotografi.png
    [3] sunum.pdf

    Çevirmek istediğin dosyanın numarasını gir: 3
    ```
5.  **Hedef Formatı Belirtin:** Dosyayı hangi formata dönüştürmek istediğinizi yazın (örneğin: `docx`, `pdf`, `jpg`).
    ```
    Seçilen dosya: sunum.pdf
    Hangi formata çevireyim? (örn: docx, pdf, png, jpg): docx
    ```
6.  **İşlemin Bitmesini Bekleyin:** Script, dönüşümü gerçekleştirecek ve aynı klasörün içine `_converted` ekiyle yeni bir dosya oluşturacaktır.

    **Örnek Çıktı:**
    `sunum_converted.docx`