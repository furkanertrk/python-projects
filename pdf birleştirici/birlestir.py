import os
from PyPDF2 import PdfMerger # type: ignore

cikti_ismi = "birlestirilmis_dosya.pdf"

tum_dosyalar = os.listdir()

pdf_listesi = []
for dosya in tum_dosyalar:
    if dosya.endswith(".pdf") and dosya != cikti_ismi:
        pdf_listesi.append(dosya)

pdf_listesi.sort()

if len(pdf_listesi) == 0:
    print("Bu klasörde hic PDF dosyasi bulunamadi.")
    exit(0)

print("Bulunan PDF sayisi: {}".format(len(pdf_listesi)))

try:
    merger = PdfMerger()
    
    for pdf in pdf_listesi:
        print("- {} ekleniyor...".format(pdf))
        merger.append(pdf)
        
    merger.write(cikti_ismi)
    merger.close()
    
    print("-" * 30)
    print("Islem basarili! Dosya adi: {}".format(cikti_ismi))
    
except Exception as e:
    print("Bir hata olustu: {}".format(e))
