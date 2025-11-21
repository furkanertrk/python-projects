import xml.etree.ElementTree as ET
from urllib.request import urlopen

TCMB_URL = "https://www.tcmb.gov.tr/kurlar/today.xml"

def kur_getir(doviz_kodu):
    with urlopen(TCMB_URL) as response:
        data = response.read()
    
    tree = ET.fromstring(data)
    
    # XML içinde ilgili dövizi ara
    for currency in tree.findall("Currency"):
        if currency.get("CurrencyCode") == doviz_kodu:
            kurlardaki_yazi = currency.find("BanknoteSelling").text
            return float(kurlardaki_yazi.replace(",", "."))
            
    return None

print("Lütfen bir döviz cinsi seçiniz:")
print("1- Amerikan Doları (USD)")
print("2- Euro (EUR)")
print("3- İngiliz Sterlini (GBP)")

secim = input("Seçiminiz: ")
doviz_kodu = ""

if secim == "1":
    doviz_kodu = "USD"
elif secim == "2":
    doviz_kodu = "EUR"
elif secim == "3":
    doviz_kodu = "GBP"
else:
    print("Hatalı bir seçim yaptınız.")
    exit()

miktar = 1  

try:
    kur = kur_getir(doviz_kodu)
    if kur is not None:
        sonuc = miktar * kur
        print("Güncel Kur: {} {} = {:.2f} TL".format(miktar, doviz_kodu, sonuc))
    else:
        print("{} için kur bilgisi bulunamadı.".format(doviz_kodu))
except Exception as e:
    print("Bir hata oluştu: {}".format(e))