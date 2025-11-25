# Video Compressor (GPU ile Hızlandırılmış)

Bu script, bir klasördeki tüm video dosyalarını (`.mp4`, `.mkv`, `.mov` vb.) NVIDIA ekran kartı (GPU) kullanarak hızlı bir şekilde sıkıştırmak için tasarlanmıştır.

## Ne İşe Yarar?
- Videoların dosya boyutunu önemli ölçüde küçültür, böylece depolama alanından tasarruf sağlar.
- Sıkıştırma işlemini CPU yerine NVIDIA GPU (NVENC) üzerinden yaparak çok daha hızlı tamamlar.
- İşlem ilerlemesini gösteren bir ilerleme çubuğu (`progress bar`) sunar.
- Orijinal dosyaları korur ve sıkıştırılmış kopyaları `_gpu_compressed` ekiyle kaydeder.

## Gereksinimler
1.  **NVIDIA Ekran Kartı:** Bu script, donanım hızlandırma için `h264_nvenc` kodeğini kullandığından bir NVIDIA GPU gerektirir.
2.  **FFmpeg:** Sisteminize FFmpeg yüklenmiş ve sistem yoluna (PATH) eklenmiş olmalıdır. Alternatif olarak, `ffmpeg.exe` dosyasını script ile aynı klasöre koyabilirsiniz.
    - [FFmpeg İndirme Sayfası](https://ffmpeg.org/download.html)
3.  **Python 3.x**
4.  **`tqdm` kütüphanesi:** İlerleme çubuğu için gereklidir.
    ```bash
    pip install tqdm
    ```

## Kullanım
1.  **Script'i ve Videoları Aynı Klasöre Koyun:** `videocompressor.py` dosyasını, sıkıştırmak istediğiniz videoların bulunduğu klasörün içine yerleştirin.
2.  **(İsteğe Bağlı) `ffmpeg.exe`'yi Ekleyin:** Eğer FFmpeg sistem genelinde kurulu değilse, `ffmpeg.exe`'yi de aynı klasöre koyun.
3.  **Terminali Açın:** Videoların bulunduğu klasörde bir terminal açın.
4.  **Script'i Çalıştırın:**
    ```bash
    python videocompressor.py
    ```
5.  **İşlemin Bitmesini Bekleyin:** Script, klasördeki tüm videoları bulacak ve her biri için GPU destekli sıkıştırma işlemini başlatacaktır. İşlem tamamlandığında, orijinal videoların yanında `_gpu_compressed` uzantılı kopyaları oluşacaktır.

    **Örnek Klasör Yapısı:**
    ```
    /Videolarim
    |-- videocompressor.py   <-- Script
    |-- ffmpeg.exe           <-- (İsteğe bağlı)
    |-- tatil.mp4            <-- Orijinal Video 1
    |-- gezi.mov             <-- Orijinal Video 2
    |-- tatil_gpu_compressed.mp4  <-- Oluşturulan Sıkıştırılmış Kopya 1
    |-- gezi_gpu_compressed.mov  <-- Oluşturulan Sıkıştırılmış Kopya 2
    ```

> **Not:** Eğer bir NVIDIA ekran kartınız yoksa, script içerisindeki `command` listesinde yer alan `-c:v h264_nvenc` kısmını `-c:v libx264` olarak değiştirerek işlemi CPU üzerinden (daha yavaş bir şekilde) yapabilirsiniz.