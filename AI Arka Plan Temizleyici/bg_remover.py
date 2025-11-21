import os
import sys
import time
from concurrent.futures import ThreadPoolExecutor
from tqdm import tqdm

# --- 1. DLL AYARLAMALARI ---
script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)
dll_path = os.path.join(script_dir, "dll_files")

if os.path.exists(dll_path):
    if hasattr(os, 'add_dll_directory'):
        os.add_dll_directory(dll_path)
    os.environ['PATH'] = dll_path + os.pathsep + os.environ['PATH']

# --- 2. KÜTÜPHANELER ---
try:
    from rembg import remove, new_session
    from PIL import Image
except ImportError:
    print("Kütüphaneler eksik.")
    sys.exit()

# Global Session
session = new_session("u2net")

def process_image(file_info):
    """Sadece işler ve kaydeder (Taşıma yapmaz)"""
    input_path, output_dir = file_info
    file_name = os.path.basename(input_path)
    
    try:
        # Çıktı dosya adı
        name_no_ext = os.path.splitext(file_name)[0]
        output_path = os.path.join(output_dir, f"{name_no_ext}.png")
        
        # Eğer çıktı zaten varsa işlemi atla (Hız kazandırır)
        if os.path.exists(output_path):
            return "skipped"

        # İşleme
        with Image.open(input_path) as img:
            result = remove(img, session=session)
            result.save(output_path)
        
        return "success"

    except Exception as e:
        return f"error: {e} - Dosya: {file_name}"

def main():
    # --- KLASÖR YAPILANDIRMASI ---
    # ARTIK KAYNAK OLARAK 'orijinaller' KLASÖRÜNE BAKIYORUZ
    input_folder = os.path.join(script_dir, "orijinaller") 
    output_folder = os.path.join(script_dir, "temizlenmis_resimler")
    
    # Klasör kontrolü
    if not os.path.exists(input_folder):
        print(f"❌ Hata: '{input_folder}' klasörü bulunamadı!")
        print("Lütfen fotoğrafları 'orijinaller' klasörünün içine attığından emin ol.")
        return

    if not os.path.exists(output_folder):
        os.mkdir(output_folder)

    # Dosyaları bul
    valid_exts = ('.jpg', '.jpeg', '.png', '.webp', '.bmp')
    files = [f for f in os.listdir(input_folder) 
             if os.path.isfile(os.path.join(input_folder, f)) 
             and f.lower().endswith(valid_exts)]

    total_files = len(files)
    if total_files == 0:
        print(f"⚠️ '{input_folder}' klasörü boş. İşlenecek resim yok.")
        return

    print(f"🚀 İŞLEM BAŞLIYOR: {total_files} resim")
    print(f"📂 Kaynak: /orijinaller")
    print(f"📂 Hedef:  /temizlenmis_resimler")
    print("-" * 50)
    
    # Görev paketi: (Dosyanın Tam Yolu, Çıktı Klasörü)
    tasks = [(os.path.join(input_folder, f), output_folder) for f in files]
    
    start_time = time.time()
    
    # RTX 4060 için worker ayarı
    workers = 8 
    
    with ThreadPoolExecutor(max_workers=workers) as executor:
        results = list(tqdm(executor.map(process_image, tasks), total=total_files, unit="img"))

    end_time = time.time()
    duration = end_time - start_time
    
    success = results.count("success")
    skipped = results.count("skipped")
    errors = total_files - success - skipped
    
    print("\n" + "="*50)
    print(f"🎉 İŞLEM TAMAMLANDI!")
    print(f"⏱️  Süre: {duration:.2f} saniye")
    print(f"⚡ Ortalama Hız: {total_files/duration:.2f} resim/saniye")
    print(f"✅ Başarılı: {success}")
    print(f"⏭️  Atlanan (Zaten var): {skipped}")
    print(f"❌ Hatalı: {errors}")
    print("="*50)
    
    if errors > 0:
        print("Hatalar:")
        for res in results:
            if "error" in res:
                print(res)
    print("="*50)

if __name__ == "__main__":
    main()