# Hızlı Başlangıç Rehberi

Bu rehber, projeyi hızlıca başlatmanız için adım adım talimatlar içerir.

## 🚀 5 Dakikada Başlayın

### 1. Depoyu Klonlayın

```bash
git clone https://github.com/TarikKilic248/Graduation-Project-2nd-Place-KT-Engineering-Exhibition.git
cd Graduation-Project-2nd-Place-KT-Engineering-Exhibition
```

### 2. Bağımlılıkları Kurun

```bash
# Python sanal ortamı oluşturun (önerilen)
python -m venv venv
source venv/bin/activate  # Linux/Mac
# veya
venv\Scripts\activate  # Windows

# Gereksinimleri yükleyin
pip install -r requirements.txt
```

### 3. Projeyi İnceleyin

#### PDF Sunumunu İnceleyin

```bash
# PDF sunumu doğrudan açabilirsiniz
open presentation.pdf  # Mac
xdg-open presentation.pdf  # Linux
start presentation.pdf  # Windows
```

#### Jupyter Notebook'u Çalıştırın

```bash
jupyter notebook demo.ipynb
```

### 4. Örnek Analiz (Model Varsa)

Eğer eğitilmiş bir modeliniz varsa:

```python
from phase_analysis import PhaseAnalyzer

# Analyzer'ı başlat
analyzer = PhaseAnalyzer(
    model_path='models/yolov8_phase_detection.pt',
    confidence_threshold=0.5
)

# Görüntüyü analiz et
results = analyzer.analyze_image('data/raw/sample.jpg')

# Sonuçları görselleştir
analyzer.visualize_results(results, save_path='results/output.jpg')
```

## 📚 Önemli Dosyalar

| Dosya | Açıklama |
|-------|----------|
| `presentation.pdf` | 📄 **Proje sunumu (PDF)** - İlk bakılması gereken |
| `README.md` | 📖 Ana dokümantasyon |
| `demo.ipynb` | 💻 İnteraktif demo notebook |
| `phase_analysis.py` | 🔬 Ana analiz scripti |
| `train_model.py` | 🎓 Model eğitim scripti |
| `docs/methodology.md` | 📊 Detaylı metodoloji |
| `docs/results.md` | 📈 Sonuçlar ve bulgular |

## 🎯 Kullanım Senaryoları

### Senaryo 1: Projeyi İncelemek

```bash
1. presentation.pdf dosyasını açın
2. README.md dosyasını okuyun
3. docs/ klasöründeki detaylı dökümanları inceleyin
```

### Senaryo 2: Demo Yapmak

```bash
1. Jupyter notebook'u çalıştırın: jupyter notebook demo.ipynb
2. Hücreleri sırayla çalıştırın
3. Örnek çıktıları inceleyin
```

### Senaryo 3: Kendi Modelinizi Eğitmek

```bash
1. Veri setinizi data/annotations/ dizinine yerleştirin
2. python train_model.py --epochs 100 --batch-size 16
3. Eğitilen modeli models/ dizinine kopyalayın
```

### Senaryo 4: Analiz Yapmak

```bash
1. Görüntüleri data/raw/ dizinine ekleyin
2. python phase_analysis.py (veya Python script'te kullanın)
3. Sonuçları results/ dizininde kontrol edin
```

## ⚙️ Sistem Gereksinimleri

### Minimum
- Python 3.8+
- 4GB RAM
- 500MB disk alanı

### Önerilen
- Python 3.10+
- 8GB+ RAM
- NVIDIA GPU (CUDA desteği)
- 2GB disk alanı

## 🔧 Sorun Giderme

### Model bulunamadı hatası

```bash
# Model eğitimi yapın veya önceden eğitilmiş modeli indirin
python train_model.py
```

### GPU bulunamadı

```bash
# CPU modunda çalıştırın (yavaş olacaktır)
# phase_analysis.py içinde device='cpu' olarak ayarlayın
```

### Bağımlılık hatası

```bash
# Bağımlılıkları tekrar yükleyin
pip install -r requirements.txt --upgrade
```

## 📞 Yardım ve Destek

- **GitHub Issues**: Hata raporları ve öneriler için
- **Dökümanlar**: docs/ klasöründe detaylı bilgi
- **Demo**: demo.ipynb ile örnekler

## 🎓 Öğrenme Yolu

1. ✅ **Başlangıç**: presentation.pdf ve README.md
2. ✅ **Teori**: docs/methodology.md
3. ✅ **Uygulama**: demo.ipynb
4. ✅ **İleri Seviye**: Kendi modelinizi eğitin
5. ✅ **Sonuçlar**: docs/results.md

## 🏆 Proje Hakkında

Bu proje KT Mühendislik Sergisi'nde **2. Ödül** kazanmıştır.

- **Konu**: Metalik malzeme faz analizi
- **Teknoloji**: YOLO v8 derin öğrenme
- **Doğruluk**: %94.5
- **Hız**: 6.4 ms/görüntü

---

**İyi Çalışmalar! 🚀**
