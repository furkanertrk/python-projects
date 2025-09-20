import random
import os

print("Savaş Oyunu PLUS")


class karakter:
    def __init__(self, isim):
        self.isim = isim
        can = random.randint(50, 150)
        self.can = can
        saldırı = random.randint(10, 150)
        self.saldırı = saldırı

    def vur(self,hedef):
        hedef.can -= self.saldırı
        print("{} {} hasar verdi!{} canı {} kaldı".format(self.isim,self.saldırı,hedef.isim,hedef.can))


karakter1 = karakter("Büyücü")
karakter2 = karakter("Savaşcı")
karakter3 = karakter("Kolpa K")
karakterler = [karakter1,karakter2,karakter3]
def karakterseçim():
    global karakterler
    for i in range(3):
        print(i+1,"- ",karakterler[i].isim)
    seçim = int(input("Seçim (1/2/3): "))
    if seçim > 0 and seçim < 4 :
        seç = karakterler[seçim-1]
        karakterler.pop(seçim-1)
        return seç
    else:
        print("hatalı seçim!")
        quit()
def bilgi_yazdır():
    for i in range(len(karakterler)):
        print("İsim:{} Can:{} Saldırı Gücü:{}".format(karakterler[i].isim,karakterler[i].can,karakterler[i].saldırı))
 #program başlıyor
sayac=0
bilgi_yazdır()
oyuncu = karakterseçim()
while True:
    os.system("cls")
    bilgi_yazdır()
    sayac+=1
    if sayac%2 == 0 :
        hedef = random.choice(karakterler)
        oyuncu.vur(hedef)
    else:
        hedef = random.choice(karakterler)
        saldıran_karakter = random.choice(karakterler)
        saldıran_karakter.vur(hedef)

    if hedef.can <= 0:
        print(f"{hedef.isim} yok oldu.")
        karakterler.remove(hedef)
        print("oyun bitti")
        quit()

    input("Devam etmek için bir tuşa basın...")


