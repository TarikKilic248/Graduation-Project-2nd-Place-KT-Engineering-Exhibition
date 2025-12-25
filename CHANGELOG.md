# Değişiklik Geçmişi

Projedeki tüm önemli değişiklikler bu dosyada belgelenecektir.

Format [Keep a Changelog](https://keepachangelog.com/en/1.0.0/) standardını takip eder.

## [1.0.0] - 2024-12-25

### Eklenenler

- ✨ YOLO v8 tabanlı faz tespit sistemi
- 📊 5 faz türü desteği (Ferrit, Perlit, Austenit, Martenzit, Bainit)
- 🚀 Ana analiz modülü (`phase_analysis.py`)
- 🎓 Model eğitim scripti (`train_model.py`)
- 📓 İnteraktif demo Jupyter notebook
- 📄 Detaylı PDF sunumu (10 sayfa)
- 📚 Kapsamlı dokümantasyon
  - Metodoloji açıklaması
  - Sonuçlar ve bulgular
  - Hızlı başlangıç rehberi
- 🎨 Sonuç görselleştirme fonksiyonları
- 📈 Batch işleme desteği
- 💾 Otomatik rapor oluşturma
- 🔧 Model konfigürasyon dosyaları
- 📦 Gereksinim listesi (requirements.txt)
- 🗂️ Proje klasör yapısı
- 📝 README.md (Türkçe)
- 🤝 Katkı rehberi
- ⚖️ MIT Lisansı

### Performans

- %94.5 doğruluk oranı
- %93.2 precision
- %95.1 recall
- %94.1 F1-score
- 6.4 ms işlem süresi (GPU)
- 156 FPS (teorik maksimum)

### Başarılar

- 🏆 KT Mühendislik Sergisi - 2. Ödül

### Teknik Detaylar

- Python 3.8+ desteği
- CUDA GPU desteği
- CPU fallback
- YOLO v8 Small model (11.2M parametre)
- Transfer learning (COCO pretrained)
- 100 epoch eğitim
- 1000 görüntü veri seti (70/20/10 split)

## [Gelecek Versiyonlar]

### Planlanıyor

- [ ] Instance segmentation desteği
- [ ] Web arayüzü
- [ ] REST API
- [ ] 3D analiz desteği
- [ ] Mobil uygulama
- [ ] Real-time analiz
- [ ] Daha fazla faz türü
- [ ] Multi-language support (İngilizce)
- [ ] Docker container
- [ ] Cloud deployment desteği

---

## Sürüm Notasyonu

Proje [Semantic Versioning](https://semver.org/) kullanır:

- **MAJOR**: Geriye uyumsuz değişiklikler
- **MINOR**: Geriye uyumlu yeni özellikler
- **PATCH**: Geriye uyumlu hata düzeltmeleri

## İletişim

Değişiklikler hakkında sorularınız için:
- GitHub Issues
- Pull Requests
- Discussions

---

**Son Güncelleme**: 25 Aralık 2024
