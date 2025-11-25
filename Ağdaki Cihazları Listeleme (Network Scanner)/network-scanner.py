import scapy.all as scapy

def tarama_yap(ip_araligi):
    print("{} araligi taraniyor...".format(ip_araligi))
    
    # ARP istegi paketi olustur
    arp_istegi = scapy.ARP(pdst=ip_araligi)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_paketi = broadcast/arp_istegi
    
    # Paketi gonder ve cevaplari al
    cevaplar = scapy.srp(arp_paketi, timeout=1, verbose=False)[0]
    
    print("IP Adresi\t\tMAC Adresi")
    print("-----------------------------------------")
    
    for gonderen, alici in cevaplar:
        print("{}\t\t{}".format(alici.psrc, alici.hwsrc))

if __name__ == "__main__":
    # Modem arayuzune gore degisebilir (192.168.1.1/24 genelde standart)
    hedef_ip = input("Hedef IP Araligi (Orn: 192.168.1.1/24): ")
    tarama_yap(hedef_ip)