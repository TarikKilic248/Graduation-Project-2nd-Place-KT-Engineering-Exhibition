# BİTİRME PROJESİ TEZİ

## 📄 Görüntü İşleme Yöntemleri ile Metalik Malzemelerin Mikroyapı Analizi - Tasarım Projesi
Bitirme projesi tezinin tam metnine aşağıdaki linkten ulaşabilirsiniz:

**[GÖRÜNTÜ_İŞLEME_YÖNTEMLERİ_İLE_METALİK_MALZEMELERİN_MİKROYAPI_ANALİZİ_Tasarım_Projesi.pdf](./GÖRÜNTÜ_İŞLEME_YÖNTEMLERİ_İLE_METALİK_MALZEMELERİN_MİKROYAPI_ANALİZİ_Tasarım_Projesi.pdf)**

<object data="./GÖRÜNTÜ_İŞLEME_YÖNTEMLERİ_İLE_METALİK_MALZEMELERİN_MİKROYAPI_ANALİZİ_Tasarım_Projesi.pdf" type="application/pdf" width="100%" height="800px">
  <embed src="./GÖRÜNTÜ_İŞLEME_YÖNTEMLERİ_İLE_METALİK_MALZEMELERİN_MİKROYAPI_ANALİZİ_Tasarım_Projesi.pdf" type="application/pdf" />
  <p>PDF dosyasını görüntüleyemiyor musunuz? <a href="./GÖRÜNTÜ_İŞLEME_YÖNTEMLERİ_İLE_METALİK_MALZEMELERİN_MİKROYAPI_ANALİZİ_Tasarım_Projesi.pdf">Buradan indirin</a>.</p>
</object>

---

# Metalik Malzeme Faz Analizi - YOLO Tabanlı Görüntü İşleme Projesi

## 🏆 KT Mühendislik Sergisi - 2. Ödül

Bu proje, metalik malzeme görüntülerinden YOLO (You Only Look Once) derin öğrenme modelleri kullanarak otomatik faz analizi yapan bir bitirme projesidir. Proje, KT Mühendislik Sergisi'nde 2. ödülü kazanmıştır.

## 📋 Proje Hakkında

Metalik malzemelerin mikroyapı analizi, malzeme bilimi ve mühendisliğinde kritik öneme sahiptir. Geleneksel yöntemler zaman alıcı ve uzman bilgisi gerektirmektedir. Bu proje, YOLO nesne algılama algoritması kullanarak bu süreci otomatikleştirmekte ve hızlandırmaktadır.

### Temel Özellikler

- ✅ YOLO v8 tabanlı nesne algılama
- ✅ Metalik malzeme fazlarının otomatik tespiti
- ✅ Yüksek doğruluk oranı
- ✅ Hızlı işleme süresi
- ✅ Kullanıcı dostu arayüz
- ✅ Detaylı raporlama ve görselleştirme

## 🎯 Kullanım Alanları

- Metalurji laboratuvarları
- Kalite kontrol süreçleri
- Malzeme araştırma ve geliştirme
- Eğitim ve öğretim

## 🚀 Kurulum

### Gereksinimler

```bash
Python 3.8+
CUDA 11.0+ (GPU kullanımı için)
```

### Bağımlılıkların Kurulumu

```bash
pip install -r requirements.txt
```

## 📊 Proje Yapısı

```
.
├── README.md                      # Proje dokümantasyonu
├── requirements.txt               # Python bağımlılıkları
├── phase_analysis.py              # Ana analiz scripti
├── train_model.py                 # Model eğitim scripti
├── demo.ipynb                     # Demo Jupyter notebook
├── presentation.pdf               # Proje sunumu (PDF)
├── GÖRÜNTÜ_İŞLEME_YÖNTEMLERİ_İLE_METALİK_MALZEMELERİN_MİKROYAPI_ANALİZİ_Tasarım_Projesi.pdf  # Bitirme projesi tezi
├── data/
│   ├── raw/                       # Ham görüntüler
│   ├── processed/                 # İşlenmiş görüntüler
│   └── annotations/               # Etiketlenmiş veriler
├── models/
│   ├── yolov8_phase_detection.pt  # Eğitilmiş model
│   └── config.yaml                # Model konfigürasyonu
├── results/
│   ├── images/                    # Sonuç görüntüleri
│   ├── metrics/                   # Performans metrikleri
│   └── reports/                   # Analiz raporları
└── docs/
    ├── methodology.md             # Metodoloji dokümantasyonu
    └── results.md                 # Sonuçlar ve bulgular
```

## 🔬 Metodoloji

### 1. Veri Toplama ve Hazırlama
- Metalik malzeme mikroskop görüntülerinin toplanması
- Görüntülerin ön işleme (normalizasyon, boyutlandırma)
- Fazların manuel etiketlenmesi (annotation)

### 2. Model Eğitimi
- YOLO v8 mimarisinin kullanılması
- Transfer learning ile önceden eğitilmiş ağırlıkların kullanımı
- Augmentasyon teknikleri ile veri çoğaltma

### 3. Faz Tespiti
- Eğitilmiş model ile test görüntülerinde faz tespiti
- Bounding box ve güven skorları ile sonuçların görselleştirilmesi

### 4. Analiz ve Raporlama
- Tespit edilen fazların istatistiksel analizi
- Alan hesaplamaları ve faz oranları
- Detaylı raporların oluşturulması

## 💻 Kullanım

### Tek Görüntü Analizi

```python
from phase_analysis import PhaseAnalyzer

# Analyzer'ı başlat
analyzer = PhaseAnalyzer(model_path='models/yolov8_phase_detection.pt')

# Görüntüyü analiz et
results = analyzer.analyze_image('data/raw/sample.jpg')

# Sonuçları görselleştir
analyzer.visualize_results(results, save_path='results/images/output.jpg')

# Rapor oluştur
analyzer.generate_report(results, output_path='results/reports/analysis.pdf')
```

### Batch İşleme

```python
from phase_analysis import PhaseAnalyzer

analyzer = PhaseAnalyzer(model_path='models/yolov8_phase_detection.pt')

# Klasördeki tüm görüntüleri analiz et
results = analyzer.batch_analyze('data/raw/', output_dir='results/')
```

### Model Eğitimi

```bash
python train_model.py --data data/annotations/ --epochs 100 --batch-size 16
```

## 📈 Sonuçlar

### Performans Metrikleri

- **Doğruluk (Accuracy)**: 94.5%
- **Precision**: 93.2%
- **Recall**: 95.1%
- **F1-Score**: 94.1%
- **mAP@0.5**: 92.8%

### Tespit Edilen Faz Türleri

1. Ferrit fazı
2. Perlit fazı
3. Austenit fazı
4. Martenzit fazı
5. Bainit fazı

## 📄 Dökümanlar

Proje hakkında detaylı bilgi için aşağıdaki dökümanları inceleyebilirsiniz:

- [Bitirme Projesi Tezi (PDF)](GÖRÜNTÜ_İŞLEME_YÖNTEMLERİ_İLE_METALİK_MALZEMELERİN_MİKROYAPI_ANALİZİ_Tasarım_Projesi.pdf) - Tam tez metni
- [Proje Sunumu (PDF)](presentation.pdf) - Projenin genel sunumu
- [Metodoloji Dokümantasyonu](docs/methodology.md) - Detaylı metodoloji açıklaması
- [Sonuçlar ve Bulgular](docs/results.md) - Detaylı sonuçlar ve analizler
- [Demo Notebook](demo.ipynb) - Interaktif demo ve örnekler

## 🤝 Katkıda Bulunma

Bu proje KT Mühendislik Sergisi için hazırlanmış bir bitirme projesidir. Önerileriniz ve geri bildirimleriniz için issue açabilirsiniz.

## 📧 İletişim

Proje hakkında sorularınız için:
- GitHub Issues kullanabilirsiniz
- Repository sahibi ile iletişime geçebilirsiniz

## 🙏 Teşekkürler

- KT Mühendislik Sergisi organizatörlerine
- Danışman hocalarıma
- Ultralytics YOLO ekibine

## 📝 Lisans

Bu proje eğitim amaçlı hazırlanmıştır.

---

**Not**: Bu proje, metalik malzeme analizi alanında yapay zeka ve görüntü işleme tekniklerinin kullanımını göstermektedir. Akademik ve araştırma amaçlı kullanım için uygundur.
