import os
from PIL import Image

def compress_image(input_path, output_path, quality=60):
    try:
        img = Image.open(input_path)
        
        # Eğer PNG ise ve şeffaflık içeriyorsa arka planı beyaz yapıp JPG'e çevirelim
        # (Daha iyi sıkıştırma için)
        if img.mode in ("RGBA", "P"):
            img = img.convert("RGB")
            
        # Sıkıştırarak kaydet
        img.save(output_path, "JPEG", optimize=True, quality=quality)
        
        print(f"✅ Dönüştürüldü: {input_path} -> {output_path}")
        
    except Exception as e:
        print(f"❌ {input_path} işlenirken hata oluştu: {e}")

def main():
    # Desteklenen formatlar
    valid_formats = ('.jpg', '.jpeg', '.png', '.bmp')
    
    # Şu anki dizindeki dosyaları listele
    files = os.listdir('.')
    
    print("--- Sıkıştırma İşlemi Başlıyor ---\n")
    
    count = 0
    for filename in files:
        # Dosya uzantısını küçük harfe çevirip kontrol et
        if filename.lower().endswith(valid_formats):
            
            # Zaten sıkıştırılmış dosyaları tekrar işleme alma
            if "_sikistirilmis" in filename:
                continue
            
            # Dosya adını ve uzantısını ayır
            name, ext = os.path.splitext(filename)
            
            # Yeni dosya adını oluştur (örn: tatil.jpg -> tatil_sikistirilmis.jpg)
            # Çıktıyı her zaman .jpg yapıyoruz çünkü sıkıştırma oranı en iyi onda.
            output_filename = f"{name}_sikistirilmis.jpg"
            
            compress_image(filename, output_filename, quality=50)
            count += 1

    if count == 0:
        print("⚠️ Klasörde hiç resim dosyası bulunamadı.")
    else:
        print(f"\n🎉 Toplam {count} fotoğraf başarıyla sıkıştırıldı.")

if __name__ == "__main__":
    main()