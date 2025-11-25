# Basit Port Tarayıcı

Bu script, belirtilen bir IP adresi üzerinde en yaygın kullanılan portların (21, 22, 23, 80, 443, 3306, 8080) durumunu (Açık/Kapalı) kontrol eder.

## Ne İşe Yarar?
- Bir sunucunun veya ağ cihazının hangi servisleri (FTP, SSH, HTTP, HTTPS vb.) çalıştırdığını hızlıca anlamanızı sağlar.
- Ağ güvenliği denetimlerinde temel bir araç olarak kullanılabilir.
- Bir servise neden bağlanamadığınızı anlamak için ilgili portun açık olup olmadığını kontrol eder.

## Gereksinimler
- Python 3.x
- Herhangi bir ek kütüphane gerektirmez, Python'un standart `socket` kütüphanesi ile çalışır.

## Kullanım
1.  **Terminali açın:** Script'in bulunduğu klasöre gidin.
2.  **Script'i çalıştırın:**
    ```bash
    python port-tarama.py
    ```
3.  **Hedef IP Adresini Girin:** Program sizden taranacak hedef sistemin IP adresini veya alan adını (örn: `google.com`) girmenizi isteyecektir.
    ```
    Taranacak IP adresi: 192.168.1.1
    ```
4.  **Sonuçları İnceleyin:** Script, belirlediği portları tek tek kontrol ederek durumlarını ekrana yazdıracaktır.

    ```
    192.168.1.1 uzerinde portlar kontrol ediliyor...
    Port 21: KAPALI
    Port 22: KAPALI
    Port 23: KAPALI
    Port 80: ACIK
    Port 443: ACIK
    Port 3306: KAPALI
    Port 8080: KAPALI
    Tarama bitti.
    ```

## Ayarlar
- **Port Listesi:** Daha fazla veya farklı portları taramak isterseniz, script içerisindeki `portlar = [21, 22, ...]` listesini düzenleyebilirsiniz.

> **⚠️ Uyarı:** Bu aracı yalnızca sahibi olduğunuz veya tarama izniniz olan sistemler üzerinde kullanın. İzinsiz olarak başka sistemlerde port taraması yapmak yasa dışı olabilir ve ağ saldırısı olarak algılanabilir.