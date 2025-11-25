# TCMB Güncel Kur Çevirici

Bu script, Türkiye Cumhuriyet Merkez Bankası (TCMB) tarafından yayınlanan güncel döviz kurlarını kullanarak anlık olarak Dolar, Euro ve Sterlin'in Türk Lirası karşılığını gösterir.

## Ne İşe Yarar?
- TCMB'nin resmi "today.xml" dosyasından canlı olarak kur verilerini çeker.
- Kullanıcıya Dolar (USD), Euro (EUR) ve Sterlin (GBP) arasında seçim yapma imkanı sunar.
- Seçilen döviz biriminin güncel TL karşılığını ekrana yazdırır.

## Gereksinimler
- Python 3.x
- Herhangi bir ek kütüphane gerektirmez, Python'un standart kütüphaneleri ile çalışır.
- Kur verilerini çekebilmek için aktif bir internet bağlantısı gereklidir.

## Kullanım
1.  **Terminali açın:** Script'in bulunduğu klasöre gidin.
2.  **Script'i çalıştırın:**
    ```bash
    python kur_cevirici.py
    ```
3.  **Döviz Cinsini Seçin:** Program sizden bir seçim yapmanızı isteyecektir.
    ```
    Lütfen bir döviz cinsi seçiniz:
    1- Amerikan Doları (USD)
    2- Euro (EUR)
    3- İngiliz Sterlini (GBP)
    Seçiminiz: 2
    ```
4.  **Sonucu Görüntüleyin:** Seçiminize göre, o anki güncel kur bilgisi ekrana yazdırılacaktır.
    ```
    Güncel Kur: 1 EUR = 35.50 TL
    ```
    *(Not: Yukarıdaki kur değeri temsilidir.)*