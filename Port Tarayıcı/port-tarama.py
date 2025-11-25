import socket

hedef_ip = input("Taranacak IP adresi: ")

# En sık kullanilan portlar listesi
portlar = [21, 22, 23, 80, 443, 3306, 8080]

print("{} uzerinde portlar kontrol ediliyor...".format(hedef_ip))

for port in portlar:
    soket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    soket.settimeout(0.5) # Cok beklememesi icin zaman asimi
    
    sonuc = soket.connect_ex((hedef_ip, port))
    
    if sonuc == 0:
        print("Port {}: ACIK".format(port))
    else:
        print("Port {}: KAPALI".format(port))
        
    soket.close()

print("Tarama bitti.")