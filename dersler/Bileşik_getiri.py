import math
print("**Bileşik Getiri Hesaplama**")
def bileşik_hesap():
    ilk_para=float(input("İlk Para:"))
    yıl=int(input("Kaç Yıl Boyunca Yatırım Yapacaksın:"))
    temettü=float(input("Yıllık Ortalama Temettü Oranı (%):"))
    temettü=temettü/100
    artış=float(input("Yıllık Artış Oranı (%):"))
    artış=artış/100
    total=ilk_para*(pow(1+artış+temettü,yıl))
    return total

sonuc=bileşik_hesap()
sonuc=float(sonuc)
print("Sonuç:",format(sonuc ,".2f"))
print("Aylık Getiri:",format(sonuc/1200*5,".2f"))