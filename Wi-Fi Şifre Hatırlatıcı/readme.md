# Windows Wi-Fi Şifre Hatırlatıcı

Bu script, **sadece Windows işletim sistemlerinde**, daha önce bağlanılmış ve şifresi kaydedilmiş olan tüm kablosuz ağların (Wi-Fi) adlarını (SSID) ve şifrelerini listeler.

## Ne İşe Yarar?
- Unuttuğunuz Wi-Fi şifrelerini bilgisayarınızın kayıtlarından bularak size gösterir.
- Bir arkadaşınıza Wi-Fi şifresini vermeniz gerektiğinde, modemin altına bakmadan hızlıca öğrenmenizi sağlar.
- Yeni bir cihaza ağları kurarken kayıtlı şifreleri toplu olarak görmenize yardımcı olur.

## Gereksinimler
- **Windows İşletim Sistemi:** Script, Windows'un `netsh` komut setini kullandığı için sadece bu platformda çalışır.
- **Yönetici Hakları:** Bazı durumlarda, tüm kayıtlı profillere erişebilmek için terminali veya komut istemini "Yönetici olarak çalıştır" seçeneği ile başlatmanız gerekebilir.
- **Python 3.x:** Ek bir kütüphane kurulumu gerektirmez.

## Kullanım
1.  **Terminali Açın:** Script'in bulunduğu klasörde bir terminal (Komut İstemi veya PowerShell) açın. En iyi sonuçlar için terminale sağ tıklayıp "Yönetici olarak çalıştır" seçeneğini kullanın.
2.  **Script'i Çalıştırın:**
    ```bash
    python wifi_sifre_hatirlatici.py
    ```
3.  **Sonuçları Görüntüleyin:** Script, bilgisayarınızda kayıtlı olan tüm Wi-Fi ağlarını ve karşılığında şifrelerini listeleyecektir.

    **Örnek Çıktı:**
    ```
    🔍 Kayıtlı Wi-Fi ağları taranıyor...

    Wi-Fi Ağı (SSID)              | Şifre
    --------------------------------------------------
    EvdekiInternet                 | cokgizlisifre123
    MisafirAgı                     | misafirlericin
    Ofis-Wifi                      | calisiyoruz!
    Telefonumun İnterneti          | (Şifre Yok veya Okunamadı)

    Çıkmak için Enter'a bas...
    ```

> **⚠️ Uyarı:** Bu araç, yalnızca kendi bilgisayarınızdaki kayıtlı şifreleri görmek içindir. Başkasının bilgisayarında izinsiz olarak kullanmak yasa dışı olabilir ve kişisel gizliliği ihlal eder.