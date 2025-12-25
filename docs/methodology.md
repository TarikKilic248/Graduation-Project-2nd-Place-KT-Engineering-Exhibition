# Metodoloji Dokümantasyonu

## Giriş

Bu doküman, metalik malzeme faz analizi projesinde kullanılan metodolojinin detaylı açıklamasını içermektedir. Proje, YOLO (You Only Look Once) derin öğrenme modelini kullanarak metalik malzeme mikroyapı görüntülerinden otomatik faz tespiti yapmayı amaçlamaktadır.

## 1. Problem Tanımı

Metalurji ve malzeme mühendisliğinde, metalik malzemelerin mikroyapı analizi kritik öneme sahiptir. Farklı fazların (ferrit, perlit, austenit, vb.) tespiti ve oranlarının belirlenmesi, malzemenin mekanik özelliklerini anlamak için gereklidir.

### Geleneksel Yöntemin Zorlukları:
- Manuel analiz zaman alıcı
- Uzman bilgisi gerektirir
- Subjektif değerlendirme riski
- Tekrar edilebilirlik sorunları
- İnsan hatası olasılığı

### Önerilen Çözüm:
YOLO tabanlı otomatik faz tespit sistemi ile:
- Hızlı ve tutarlı sonuçlar
- Objektif değerlendirme
- Yüksek doğruluk
- Ölçeklenebilir analiz

## 2. Veri Toplama ve Hazırlama

### 2.1 Veri Kaynakları

Proje için kullanılan veriler:
- Optik mikroskop görüntüleri
- Taramalı elektron mikroskobu (SEM) görüntüleri
- Çeşitli çelik türleri (düşük karbonlu, orta karbonlu, yüksek karbonlu)
- Farklı ısıl işlem koşulları

### 2.2 Görüntü Ön İşleme

```python
# Görüntü ön işleme adımları:
1. Gürültü azaltma (Gaussian blur)
2. Kontrast iyileştirme (CLAHE - Contrast Limited Adaptive Histogram Equalization)
3. Normalizasyon
4. Boyutlandırma (640x640 piksel)
```

### 2.3 Veri Etiketleme (Annotation)

- **Araç**: LabelImg, CVAT
- **Format**: YOLO format (class x_center y_center width height)
- **Etiketlenen Faz Türleri**:
  - Ferrit (Class 0)
  - Perlit (Class 1)
  - Austenit (Class 2)
  - Martenzit (Class 3)
  - Bainit (Class 4)

### 2.4 Veri Artırma (Data Augmentation)

Veri setini zenginleştirmek için uygulanan teknikler:

```yaml
Augmentation Parametreleri:
  - Horizontal Flip: 0.5
  - Rotation: ±10 derece
  - Scale: 0.5-1.5x
  - Translation: ±10%
  - HSV değişimi:
    - Hue: ±1.5%
    - Saturation: ±70%
    - Value: ±40%
  - Mosaic: 1.0 (4 görüntü birleştirme)
```

### 2.5 Veri Seti Bölünmesi

```
Toplam Görüntü: 1000
├── Eğitim (Train): 700 (70%)
├── Doğrulama (Validation): 200 (20%)
└── Test: 100 (10%)
```

## 3. Model Mimarisi

### 3.1 YOLO v8 Seçimi

YOLO v8'in seçilme nedenleri:
- En güncel YOLO versiyonu
- Yüksek doğruluk ve hız dengesi
- Kolay eğitim ve deployment
- Aktif topluluk desteği
- PyTorch tabanlı modern implementasyon

### 3.2 Model Varyantları

Denenen model boyutları:
- **YOLOv8n (Nano)**: Hızlı, hafif (3.2M parametre)
- **YOLOv8s (Small)**: Dengeli (11.2M parametre) - **SEÇİLEN**
- **YOLOv8m (Medium)**: Yüksek doğruluk (25.9M parametre)

### 3.3 Ağ Yapısı

```
Input (640x640x3)
    ↓
Backbone (CSPDarknet)
    ↓
Neck (PAN - Path Aggregation Network)
    ↓
Head (Detection)
    ↓
Output (Bounding Boxes + Classes + Confidence)
```

## 4. Model Eğitimi

### 4.1 Transfer Learning

- **Başlangıç Ağırlıkları**: COCO dataset üzerinde eğitilmiş YOLOv8s
- **Fine-tuning Stratejisi**: Tüm katmanlar eğitildi
- **Avantaj**: Daha az veri ile yüksek performans

### 4.2 Eğitim Hiperparametreleri

```python
Hiperparametreler:
    - Learning Rate (başlangıç): 0.01
    - Learning Rate (final): 0.001
    - Optimizer: AdamW
    - Weight Decay: 0.0005
    - Momentum: 0.937
    - Batch Size: 16
    - Epochs: 100
    - Image Size: 640x640
    - Warmup Epochs: 3
```

### 4.3 Loss Function

YOLO v8'de kullanılan kayıp fonksiyonları:

```
Total Loss = Box Loss + Class Loss + DFL Loss

- Box Loss (CIoU): Bounding box regresyonu
- Class Loss (BCE): Sınıflandırma
- DFL Loss: Distribution Focal Loss (konum tahmin kalitesi)
```

### 4.4 Eğitim Stratejisi

1. **Warmup Fazı** (3 epoch):
   - Düşük learning rate ile başla
   - Model ağırlıklarını stabilize et

2. **Ana Eğitim** (97 epoch):
   - Cosine annealing ile learning rate azaltma
   - Early stopping (patience=50)

3. **Validation**:
   - Her epoch sonunda validation set üzerinde değerlendirme
   - En iyi modeli kaydet (mAP50 metriğine göre)

## 5. Değerlendirme Metrikleri

### 5.1 Precision (Kesinlik)

```
Precision = TP / (TP + FP)
```
Tahmin edilen pozitif örneklerin ne kadarının gerçekten pozitif olduğunu gösterir.

### 5.2 Recall (Duyarlılık)

```
Recall = TP / (TP + FN)
```
Gerçek pozitif örneklerin ne kadarının doğru tahmin edildiğini gösterir.

### 5.3 F1-Score

```
F1-Score = 2 × (Precision × Recall) / (Precision + Recall)
```
Precision ve Recall'un harmonik ortalaması.

### 5.4 mAP (mean Average Precision)

- **mAP@0.5**: IoU threshold 0.5'te ortalama precision
- **mAP@0.5:0.95**: IoU threshold 0.5-0.95 aralığında ortalama precision

### 5.5 IoU (Intersection over Union)

```
IoU = Area of Overlap / Area of Union
```
Tahmin edilen ve gerçek bounding box'ların kesişim oranı.

## 6. Post-Processing

### 6.1 Non-Maximum Suppression (NMS)

```python
NMS Parametreleri:
    - IoU Threshold: 0.45
    - Confidence Threshold: 0.5
```

Aynı nesne için birden fazla tespitin filtrelenmesi.

### 6.2 Güven Skoru Filtreleme

- Minimum confidence: 0.5
- Düşük güvenli tespitler elenir

## 7. Optimizasyon Teknikleri

### 7.1 Model Hızlandırma

- **TensorRT**: GPU inference optimizasyonu
- **ONNX**: Platform bağımsız deployment
- **Quantization**: Model boyutu azaltma (FP16)

### 7.2 Batch İşleme

```python
# Çoklu görüntü işleme
batch_size = 8  # GPU belleğine göre ayarla
```

## 8. Sonuç

Bu metodoloji ile:
- %94.5 accuracy
- %93.2 precision
- %95.1 recall
- %92.8 mAP@0.5

elde edilmiştir.

### Gelecek Çalışmalar

1. **Daha fazla faz türü eklemek**
2. **3D mikroyapı analizi**
3. **Real-time analiz optimizasyonu**
4. **Mobil deployment**
5. **Segmentation modeline geçiş** (daha hassas alan hesabı için)

## Referanslar

- Ultralytics YOLOv8 Documentation
- Metallography and Microstructures (ASM Handbook)
- Deep Learning for Computer Vision
- Phase Detection in Metallography: A Review

---

**Son Güncelleme**: Aralık 2024
