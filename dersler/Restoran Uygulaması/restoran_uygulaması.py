masalar = dict()
for a in range(20):
    masalar[a] = 0


def hesap_ekle():
    masa_no = int(input("Masa numarası : "))
    bakiye = masalar[masa_no]
    eklenecek_ücret = float(input("Eklenecek ücret : "))
    güncel_bakiye = bakiye + eklenecek_ücret
    masalar[masa_no] = güncel_bakiye
    print("İşleminiz tamamlandı.")


def hesap_ödeme():
    masa_no = int(input("Masa numarası : "))
    bakiye = masalar[masa_no]
    print("Masa {}'in hesabı : {} TL".format(masa_no, bakiye))
    masalar[masa_no] = 0
    print("Hesap ödendi.")


def dosya_kontrolu(dosya_adi):
    try:
        dosya = open(dosya_adi, "r", encoding="utf-8")
        veri = dosya.read()
        veri = veri.split("\n")
        veri.pop()
        dosya.close()
        for a in enumerate(veri):
            masalar[a[0]] = float(a[1])
    except FileNotFoundError:
        dosya = open(dosya_adi, "w", encoding="utf-8")
        dosya.close()
        print("Kayıt dosyası oluşturuldu.")


def dosya_guncelle(dosya_adi):
    dosya = open(dosya_adi, "w", encoding="utf-8")
    for a in range(20):
        bakiye = masalar[a]
        bakiye = str(bakiye)
        dosya.write(bakiye + "\n")
    dosya.close()


def ana_islemler():
    dosya_kontrolu("bakiye.txt")
    while True:
        print("""
            Battal KOÇ Restaurant Uygulaması

        1) Masaları Görüntüle
        2) Hesap Ekle
        3) Hesap Ödeme
        Q) Çıkış

        """)
        secim = input("Yapılacak işlemi giriniz : ")
        if secim == "1":
            for a in range(20):
                print("Masa {} için hesap : {} TL".format(a, masalar[a]))
        elif secim == "2":
            hesap_ekle()
        elif secim == "3":
            hesap_ödeme()
        elif secim == "q" or secim == "Q":
            print("Çıkış yapılıyor. İyi günler.")
            quit()
        else:
            print("Hatalı seçim yaptınız.")
        dosya_guncelle("bakiye.txt")
        input("Ana menüye dönmek için enter'a basınız.")


ana_islemler()