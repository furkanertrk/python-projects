import os
from pdf2docx import Converter
from docx2pdf import convert as convert_docx
from PIL import Image

def pdf_to_docx(pdf_file, docx_file):
    print(f"⏳ {pdf_file} dosyası DOCX'e çevriliyor...")
    cv = Converter(pdf_file)
    cv.convert(docx_file, start=0, end=None)
    cv.close()
    print(f"✅ Başarılı: {docx_file}")

def docx_to_pdf(docx_file, pdf_file):
    print(f"⏳ {docx_file} dosyası PDF'e çevriliyor (Word kullanılıyor)...")
    try:
        convert_docx(docx_file, pdf_file)
        print(f"✅ Başarılı: {pdf_file}")
    except Exception as e:
        print(f"❌ Hata: {e}. (Microsoft Word yüklü olduğundan emin ol.)")

def convert_image(input_file, output_file):
    print(f"⏳ {input_file} görseli dönüştürülüyor...")
    try:
        img = Image.open(input_file)
        # Eğer JPG'e çevireceksek ve resim şeffafsa (RGBA), RGB yapmalıyız
        if output_file.lower().endswith(('.jpg', '.jpeg')) and img.mode in ('RGBA', 'P'):
            img = img.convert('RGB')
        
        img.save(output_file)
        print(f"✅ Başarılı: {output_file}")
    except Exception as e:
        print(f"❌ Hata: {e}")

def main():
    # 1. Mevcut dizindeki dosyaları listele
    files = [f for f in os.listdir('.') if os.path.isfile(f) and not f.endswith('.py')]
    
    if not files:
        print("⚠️ Bu klasörde dönüştürülecek dosya yok.")
        return

    print("\n--- 📂 DÖNÜŞTÜRÜCÜ ASİSTAN ---")
    print("Bulunan dosyalar:")
    for i, file in enumerate(files, 1):
        print(f"[{i}] {file}")

    # 2. Kullanıcıdan dosya seçmesini iste
    try:
        choice = int(input("\nÇevirmek istediğin dosyanın numarasını gir: "))
        selected_file = files[choice - 1]
    except (ValueError, IndexError):
        print("❌ Geçersiz seçim!")
        return

    file_name, file_ext = os.path.splitext(selected_file)
    
    # 3. Hedef formatı sor
    print(f"\nSeçilen dosya: {selected_file}")
    target_ext = input("Hangi formata çevireyim? (örn: docx, pdf, png, jpg): ").lower().strip()
    
    # Nokta (.) eklemediyse biz ekleyelim
    if not target_ext.startswith('.'):
        target_ext = '.' + target_ext

    output_file = f"{file_name}_converted{target_ext}"

    # 4. Dosya türüne göre doğru fonksiyonu çalıştır
    # --- PDF -> DOCX ---
    if file_ext.lower() == '.pdf' and target_ext == '.docx':
        pdf_to_docx(selected_file, output_file)

    # --- DOCX -> PDF ---
    elif file_ext.lower() == '.docx' and target_ext == '.pdf':
        docx_to_pdf(selected_file, output_file)

    # --- RESİM -> RESİM (JPG, PNG, WEBP, ICO vs) ---
    elif file_ext.lower() in ('.jpg', '.jpeg', '.png', '.webp', '.bmp') and \
         target_ext in ('.jpg', '.jpeg', '.png', '.webp', '.ico', '.bmp'):
        convert_image(selected_file, output_file)
        
    else:
        print("⚠️ Üzgünüm, bu iki format arasındaki dönüşümü henüz desteklemiyorum.")
        print(f"Desteklenenler: PDF->DOCX, DOCX->PDF ve Tüm Resim Dönüşümleri.")

if __name__ == "__main__":
    main()