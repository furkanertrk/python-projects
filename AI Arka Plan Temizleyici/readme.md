🪄 AI Arka Plan Temizleyici (High Performance)
Bu proje, Python ve Rembg (u2net) yapay zeka modelini kullanarak klasördeki resimlerin arka planlarını toplu halde ve yüksek hızda temizler.

Özellikle NVIDIA GPU (CUDA) desteği için gerekli .dll dosyalarıyla entegre edilmiştir ve RTX 4060 gibi kartlarda maksimum performans verecek şekilde çoklu iş parçacığı (multi-threading) ile çalışır.

📂 Proje Yapısı
Dosya ve klasör düzeni aşağıdaki gibidir. Çalıştırmadan önce fotoğraflarınızı orijinaller klasörüne atmanız yeterlidir.

Plaintext
AI Arka Plan Temizleyici/
├── bg_remover.py           # Ana Python betiği
├── dll_files/              # GPU hızlandırma için gerekli kütüphaneler
├── orijinaller/            # İşlenecek fotoğrafları buraya koyun
└── temizlenmis_resimler/   # Arka planı silinenler buraya çıkar

🚀 Özellikler
GPU Hızlandırma: Proje klasörü içerisindeki dll_files sayesinde sistem genelinde CUDA kurulumuyla uğraşmadan GPU gücünü kullanır.

Multi-Threading: Aynı anda birden fazla fotoğrafı işleyerek (Varsayılan: 8 worker) süreyi minimuma indirir.

Akıllı Atlatma: Eğer bir fotoğrafın temizlenmiş hali zaten temizlenmis_resimler klasöründe varsa, o fotoğrafı tekrar işlemez (zaman kazandırır).

Otomatik Klasör Yapısı: Çıktı klasörü yoksa kendi oluşturur.

🛠️ Kurulum ve Gereksinimler
Bilgisayarınızda Python kurulu olmalıdır.

Gerekli kütüphaneleri kurmak için terminalde şu komutu çalıştırın:

Bash

pip install rembg pillow tqdm
(Not: dll_files klasörü sayesinde ekstra bir CUDA kurulumu yapmanıza gerek yoktur, script bu dosyaları otomatik tanır.)

💻 Nasıl Kullanılır?
Arka planını silmek istediğiniz resimleri (.jpg, .png, .jpeg, .webp) orijinaller klasörünün içine atın.

Scripti çalıştırın:

Bash

python bg_remover.py
İşlem bittiğinde temizlenmiş PNG dosyalarınızı temizlenmis_resimler klasöründe bulabilirsiniz.

⚙️ Teknik Detaylar (DLL & GPU)
Bu proje, onnxruntime-gpu kütüphanesinin NVIDIA kartlarda sorunsuz çalışması için gerekli olan CUDA 12.x ve cuDNN 9.x kütüphanelerini yerel olarak barındırır.

dll_files içeriği: Script çalıştırıldığında otomatik olarak PATH değişkenine eklenen dosyalar: (Bu .dll dosyalarını eklemeyeceğim.Boyutu çok büyük (1.92GB))

**Eğer GPU hızlandırmasını (RTX/GTX kartlarda) kullanmak istiyorsanız:**

1.  Proje klasöründe `dll_files` adında boş bir klasör oluşturun.
2.  **NVIDIA CUDA Toolkit 12.x** ve **cuDNN 9.x** kütüphanelerinden aşağıdaki dosyaları bulup bu klasörün içine kopyalayın:

* 'cublas64_12.dll' & 'cublasLt64_12.dll'
* 'cudart64_12.dll'
* 'cudnn64_9.dll'
* 'cudnn_adv64_9.dll', 'cudnn_cnn64_9.dll', 'cudnn_graph64_9.dll'
* 'cudnn_ops64_9.dll', 'cudnn_heuristic64_9.dll'
* cudnn_engines_precompiled64_9.dll
* 'cudnn_engines_runtime_compiled64_9.dll'
* 'cufft64_11.dll'
* 'curand64_10.dll'

3.  Scripti çalıştırdığınızda otomatik olarak bu klasörü algılayıp GPU moduna geçecektir.
*Not: Eğer bu adımı yapmazsanız veya NVIDIA kartınız yoksa, script otomatik olarak CPU üzerinden çalışmaya devam eder (çok daha yavaş olacaktır).*

📊 Performans Notu

Kod içerisindeki workers = 8 ayarı RTX 4060 ve muadili güçlü işlemci/ekran kartı kombinasyonları için optimize edilmiştir. Daha düşük donanımlarda bu sayıyı düşürebilirsiniz.
