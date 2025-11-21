# 🪄 AI Arka Plan Temizleyici (High Performance)

Bu proje Python ve **rembg (u2net)** kullanarak bir klasördeki resimlerin arka planlarını toplu ve yüksek performanslı şekilde temizler. Özellikle **NVIDIA GPU (CUDA)** hızlandırması için gerekli `.dll` dosyalarını yerel olarak kullanarak, RTX 40-serisi gibi kartlarda çoklu iş parçacığı (multi-threading) ile maksimum verim sağlar.

---

## 📂 Proje Yapısı

```
AI Arka Plan Temizleyici/
├── bg_remover.py           # Ana Python betiği
├── dll_files/              # GPU hızlandırma için gerekli kütüphaneler (opsiyonel)
├── orijinaller/            # İşlenecek fotoğrafları buraya koyun
└── temizlenmis_resimler/   # Arka planı silinen dosyalar buraya çıkar
```

> Çalıştırmadan önce `orijinaller/` klasörüne fotoğraflarınızı koymanız yeterlidir.

---

## 🚀 Özellikler

* **GPU Hızlandırma**: `dll_files` klasöründeki uygun `.dll` dosyaları tespit edildiğinde ONNX/onnxruntime-gpu ile GPU üzerinden çalışır.
* **Multi-Threading**: Aynı anda birden fazla resmi işleyerek toplam süreyi kısaltır (varsayılan: `workers = 8`).
* **Akıllı Atlatma**: Hâlihazırda `temizlenmis_resimler/` içinde temizlenmiş bir dosya varsa tekrar işleme yapmaz.
* **Otomatik Klasör Oluşturma**: Çıktı klasörü yoksa script çalıştırılınca otomatik oluşturur.

---

## 🛠️ Gereksinimler

* Python 3.8+ yüklü olmalı.
* Gerekli Python paketleri:

```bash
pip install rembg pillow tqdm
```

> Not: `dll_files` klasörü sayesinde sistem genelinde CUDA kurulumu yapmanıza gerek yoktur; script doğru `.dll` dosyalarını tespit ederse GPU moduna geçer.

---

## 💻 Kullanım

1. `orijinaller/` klasörüne arka planını temizlemek istediğiniz resimleri koyun (`.jpg`, `.png`, `.jpeg`, `.webp` desteklenir).
2. Terminalde proje klasörüne gidin ve çalıştırın:

```bash
python bg_remover.py
```

3. İşlem tamamlandığında temizlenmiş PNG dosyalarını `temizlenmis_resimler/` içinde bulacaksınız.

---

## ⚙️ GPU Hızlandırma için DLL Talimatları

Eğer NVIDIA GPU (ör. RTX 4060) ile hızlandırmadan faydalanmak istiyorsanız aşağıdaki adımları izleyin.

1. Proje kökünde `dll_files` adında bir klasör oluşturun (boş olması yeterli).
2. **NVIDIA CUDA Toolkit 12.x** ve **cuDNN 9.x** kurulumundan aşağıdaki `.dll` dosyalarını bulun ve `dll_files/` klasörüne kopyalayın.

**Gereken örnek dosyalar (tam liste olmayabilir, sisteminize göre ek dosyalar gerekebilir):**

* `cublas64_12.dll`, `cublasLt64_12.dll`
* `cudart64_12.dll`
* `cudnn64_9.dll`
* `cudnn_adv64_9.dll`, `cudnn_cnn64_9.dll`, `cudnn_graph64_9.dll`
* `cudnn_ops64_9.dll`, `cudnn_heuristic64_9.dll`
* `cudnn_engines_precompiled64_9.dll`
* `cudnn_engines_runtime_compiled64_9.dll`
* `cufft64_11.dll`
* `curand64_10.dll`

> **Önemli:** Bu `.dll` dosyalarını buraya eklemeyin (boyutları büyük olabilir). Projenin telif/güvenlik kuralları gereğince bu dosyalar depo içine konmamalıdır.

Script, `dll_files/` içinde uygun dosyaları tespit ederse otomatik olarak GPU moduna geçecektir. Eğer dosyalar yoksa veya uygun bir NVIDIA kartı bulunamazsa çalışma CPU modunda devam eder (daha yavaş).

---

## ⚡ Performans Notları

* `workers = 8` varsayılanı RTX 4060 ve benzeri güçlü kombinasyonlar için optimize edilmiştir. Daha zayıf donanımlarda bu sayıyı düşürün (ör. 2–4).
* Büyük boyutlu resimlerde bellek kullanımı artar; GPU bellek sınırlarına dikkat edin.

---

## ✨ Örnek Komutlar ve İpuçları

* Tek seferde sadece birkaç dosya test etmek isterseniz `orijinaller/` içine küçük örnekler koyun.
* Hatalarla karşılaşırsanız terminal çıktısını kontrol edin; script kullanıcıya hangi modda çalıştığını (GPU/CPU) bildirir.

---

## 🔒 Güvenlik & Lisans

* Bu depo `.dll` dosyalarını içermez. Kullanıcılar kendi CUDA/cuDNN kurulumlarından gerekli dosyaları sağlamalıdır.

---

## 🤝 Katkıda Bulunma

Katkılar hoş gelir! Hata bildirimi, performans iyileştirmeleri veya dökümantasyon düzeltmeleri için pull request açabilirsiniz.

---

## İletişim

Sorularınız veya özel istekleriniz için README üzerinden veya proje issue tracker üzerinden bana ulaşabilirsiniz.

---

*Hazır — hızlı, pratik ve GPU destekli arka plan temizleme çözümünüz.*
