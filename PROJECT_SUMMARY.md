# Proje Özeti

## 📌 Genel Bakış

Bu depo, YOLO v8 derin öğrenme modeli kullanarak metalik malzeme mikroyapı görüntülerinden otomatik faz analizi yapan bir bitirme projesidir. Proje, **KT Mühendislik Sergisi'nde 2. Ödül** kazanmıştır.

## 🎯 Proje Hedefleri

1. ✅ Metalik malzeme fazlarının otomatik tespiti
2. ✅ Yüksek doğruluk oranı (%94.5)
3. ✅ Hızlı işleme süresi (6.4 ms/görüntü)
4. ✅ Kullanıcı dostu sistem
5. ✅ Kapsamlı dokümantasyon

## 📦 İçerik

### Ana Dosyalar

| Dosya | Boyut | Açıklama |
|-------|-------|----------|
| `presentation.pdf` | 14 KB | 📄 **10 sayfalık PDF sunumu** |
| `README.md` | ~7 KB | 📖 Ana dokümantasyon (Türkçe) |
| `phase_analysis.py` | ~13 KB | 🔬 Ana analiz kodu (400+ satır) |
| `train_model.py` | ~6 KB | 🎓 Model eğitim scripti |
| `demo.ipynb` | ~10 KB | 💻 İnteraktif Jupyter notebook |
| `requirements.txt` | ~0.5 KB | 📦 Python bağımlılıkları |

### Dokümantasyon

| Dosya | Açıklama |
|-------|----------|
| `docs/methodology.md` | Detaylı metodoloji (5.9 KB) |
| `docs/results.md` | Sonuçlar ve bulgular (7.9 KB) |
| `QUICKSTART.md` | Hızlı başlangıç rehberi (3.6 KB) |
| `CONTRIBUTING.md` | Katkı rehberi (2.2 KB) |
| `CHANGELOG.md` | Sürüm geçmişi (1.9 KB) |
| `LICENSE` | MIT Lisansı (1.1 KB) |

### Klasör Yapısı

```
├── data/               # Veri dosyaları
│   ├── raw/           # Ham görüntüler
│   ├── processed/     # İşlenmiş veriler
│   └── annotations/   # YOLO etiketleri
├── models/            # Model dosyaları
│   ├── config.yaml   # Model konfigürasyonu
│   └── README.md     # Model dokümantasyonu
├── docs/              # Detaylı dokümantasyon
│   ├── methodology.md
│   └── results.md
└── results/           # Analiz sonuçları
    ├── images/       # Görsel sonuçlar
    ├── metrics/      # Performans metrikleri
    └── reports/      # Raporlar
```

## 🚀 Hızlı Kullanım

### 1. PDF Sunumunu İnceleyin
```bash
# En önemli dosya - ilk bakılması gereken
open presentation.pdf
```

### 2. Dokümantasyonu Okuyun
```bash
# Sırasıyla:
1. README.md          # Genel bakış
2. QUICKSTART.md      # Hızlı başlangıç
3. docs/methodology.md # Metodoloji
4. docs/results.md    # Sonuçlar
```

### 3. Demo'yu Çalıştırın
```bash
pip install -r requirements.txt
jupyter notebook demo.ipynb
```

## 🏆 Başarımlar

### Performans Metrikleri
- **Accuracy**: %94.5
- **Precision**: %93.2
- **Recall**: %95.1
- **F1-Score**: %94.1
- **mAP@0.5**: %92.8
- **İşlem Süresi**: 6.4 ms (GPU)

### Ödüller
- 🥈 KT Mühendislik Sergisi - 2. Ödül

## 🔬 Teknik Detaylar

### Teknoloji Stack
- **Framework**: Ultralytics YOLOv8
- **Dil**: Python 3.8+
- **Derin Öğrenme**: PyTorch
- **Görüntü İşleme**: OpenCV
- **Görselleştirme**: Matplotlib, Seaborn

### Model Özellikleri
- **Mimari**: YOLOv8 Small
- **Parametre**: 11.2M
- **Eğitim**: 100 epoch, 8.5 saat
- **Veri**: 1000 görüntü
- **Sınıf**: 5 faz türü

### Tespit Edilen Fazlar
1. Ferrit
2. Perlit
3. Austenit
4. Martenzit
5. Bainit

## 📊 Proje İstatistikleri

- **Toplam Dosya**: 17
- **Kod Satırı**: ~1,500+
- **Dokümantasyon**: ~25,000 kelime
- **PDF Sayfa**: 10
- **Klasör**: 11
- **Proje Boyutu**: ~600 KB

## 🎓 Eğitim Amaçlı Kullanım

Bu proje aşağıdaki konularda eğitim materyali olarak kullanılabilir:

1. **Derin Öğrenme**: YOLO modeli uygulaması
2. **Bilgisayarlı Görü**: Nesne algılama
3. **Malzeme Bilimi**: Mikroyapı analizi
4. **Python**: Proje yapısı ve best practices
5. **Dokümantasyon**: Kapsamlı proje belgelendirme

## 🌟 Öne Çıkan Özellikler

### Kod Kalitesi
- ✅ PEP 8 uyumlu
- ✅ Type hints
- ✅ Docstring'ler
- ✅ Modüler yapı
- ✅ Hata yönetimi

### Dokümantasyon Kalitesi
- ✅ Türkçe dilinde
- ✅ Detaylı açıklamalar
- ✅ Kod örnekleri
- ✅ Görsel diyagramlar
- ✅ Adım adım rehberler

### Kullanıcı Deneyimi
- ✅ Kolay kurulum
- ✅ Hızlı başlangıç
- ✅ İnteraktif demo
- ✅ Örnek kullanımlar
- ✅ Sorun giderme

## 🔗 Bağlantılar

- **Repository**: [GitHub](https://github.com/TarikKilic248/Graduation-Project-2nd-Place-KT-Engineering-Exhibition)
- **PDF Sunumu**: `presentation.pdf`
- **Ana Dokümantasyon**: `README.md`

## 📞 İletişim ve Destek

- **GitHub Issues**: Hata raporları ve öneriler
- **Discussions**: Genel sorular
- **Pull Requests**: Kod katkıları

## 🙏 Teşekkürler

- KT Mühendislik Sergisi organizatörlerine
- Danışman hocalarıma
- Ultralytics YOLO ekibine
- Açık kaynak topluluğuna

## 📄 Lisans

Bu proje MIT Lisansı altında lisanslanmıştır. Detaylar için `LICENSE` dosyasına bakın.

---

## 🎯 Sonuç

Bu proje, metalurji alanında yapay zeka uygulamalarının başarılı bir örneğidir. Akademik ve endüstriyel kullanım için hazır, iyi dokümante edilmiş ve yüksek performanslı bir sistemdir.

**🏆 KT Mühendislik Sergisi - 2. Ödül Kazanan Proje 🏆**

---

**Son Güncelleme**: 25 Aralık 2024  
**Versiyon**: 1.0.0  
**Durum**: ✅ Tamamlandı
