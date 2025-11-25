import os
import subprocess
import sys
import re
import concurrent.futures
from tqdm import tqdm  # pip install tqdm

# Desteklenen uzantılar
VIDEO_EXTENSIONS = {'.mp4', '.mkv', '.mov', '.avi', '.flv', '.wmv'}

def get_ffmpeg_path():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    local_ffmpeg = os.path.join(script_dir, "ffmpeg.exe")
    if os.path.exists(local_ffmpeg):
        return local_ffmpeg
    return "ffmpeg"

def get_video_duration(input_file, ffmpeg_path):
    """Videonun toplam süresini saniye cinsinden bulur."""
    command = [ffmpeg_path, '-i', input_file]
    try:
        # ffmpeg -i komutu hata çıktısında bilgi verir, o yüzden stderr okuyoruz
        result = subprocess.run(command, stderr=subprocess.PIPE, stdout=subprocess.PIPE, text=True)
        
        # Regex ile "Duration: 00:00:10.50" formatını arıyoruz
        match = re.search(r"Duration: (\d{2}):(\d{2}):(\d{2})\.(\d{2})", result.stderr)
        if match:
            hours, minutes, seconds, centis = map(int, match.groups())
            return hours * 3600 + minutes * 60 + seconds + (centis / 100)
    except:
        pass
    return 0

def compress_worker(args):
    """
    İşçi fonksiyonu. tqdm progress bar ile entegre çalışır.
    args: (input_file, ffmpeg_path, position_index)
    """
    input_file, ffmpeg_path, position = args
    file_name, ext = os.path.splitext(input_file)
    output_file = "{}_gpu_compressed{}".format(file_name, ext)

    if "_gpu_compressed" in file_name or os.path.exists(output_file):
        return

    # Toplam süreyi al
    total_duration = get_video_duration(input_file, ffmpeg_path)
    
    command = [
        ffmpeg_path, '-y', # -y: dosya varsa sormadan üzerine yaz (kontrolü zaten yaptık)
        '-i', input_file,
        '-c:v', 'h264_nvenc', '-rc', 'vbr', '-cq', '23', '-preset', 'p4',
        '-c:a', 'aac',
        '-progress', 'pipe:1', # İlerlemeyi stdout'a bas
        '-nostats',            # Gereksiz istatistikleri kapat
        output_file
    ]

    # Progress Bar Ayarları
    short_name = os.path.basename(input_file)
    if len(short_name) > 20: short_name = short_name[:17] + "..."
    
    pbar = tqdm(
        total=total_duration, 
        position=position, 
        desc=short_name, 
        leave=True, 
        unit="sn",
        ncols=100
    )

    # İşlemi başlat ve satır satır çıktı oku
    process = subprocess.Popen(
        command, 
        stdout=subprocess.PIPE, 
        stderr=subprocess.STDOUT, 
        text=True,
        bufsize=1 # Satır satır buffer
    )

    # out_time_ms= veya out_time= parametresini takip et
    last_time = 0
    
    for line in process.stdout:
        # FFmpeg progress çıktısı "out_time_us=12345678" şeklinde mikrosaniye verir
        if "out_time_us=" in line:
            try:
                time_us = int(line.split("=")[1])
                current_time = time_us / 1000000.0 # Saniyeye çevir
                
                # İlerleme çubuğunu güncelle (fark kadar artır)
                update_val = current_time - last_time
                if update_val > 0:
                    pbar.update(update_val)
                    last_time = current_time
            except:
                pass

    process.wait()
    pbar.close()

def main():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    ffmpeg_path = get_ffmpeg_path()
    
    print("\nMod: RTX 4060 Multi-Thread + Progress Bar")
    print("-" * 50)

    tasks = []
    files = [f for f in os.listdir(current_dir) if os.path.isfile(os.path.join(current_dir, f))]
    
    index = 0
    for file in files:
        full_path = os.path.join(current_dir, file)
        _, ext = os.path.splitext(file)
        
        if ext.lower() in VIDEO_EXTENSIONS and "_gpu_compressed" not in file:
             # (dosya_yolu, ffmpeg, görsel_sıra_no)
            tasks.append((full_path, ffmpeg_path, index))
            index += 1

    if not tasks:
        print("İşlenecek video bulunamadı.")
        input()
        return

    print("{} video işleniyor...\n".format(len(tasks)))

    # max_workers=3 ideal. position argümanı barların üst üste binmemesini sağlar.
    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
        executor.map(compress_worker, tasks)

    print("\n" * (len(tasks) + 1)) # Barların altında temiz bir boşluk bırak
    print("--- Tüm işlemler tamamlandı ---")
    input("Çıkmak için Enter...")

if __name__ == "__main__":
    main()