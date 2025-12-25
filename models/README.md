# Model Konfigürasyonu

Bu dosya YOLO modeli için konfigürasyon ayarlarını içerir.

## Model Parametreleri

```yaml
model:
  name: yolov8s
  input_size: 640
  num_classes: 5
  
classes:
  0: Ferrit
  1: Perlit
  2: Austenit
  3: Martenzit
  4: Bainit

training:
  epochs: 100
  batch_size: 16
  learning_rate: 0.01
  optimizer: AdamW
  
augmentation:
  hsv_h: 0.015
  hsv_s: 0.7
  hsv_v: 0.4
  degrees: 0.0
  translate: 0.1
  scale: 0.5
  flipud: 0.0
  fliplr: 0.5
  mosaic: 1.0

inference:
  confidence_threshold: 0.5
  iou_threshold: 0.45
  max_detections: 100
```

## Model İndirme

Eğitilmiş model dosyası büyük olduğu için git'e dahil edilmemiştir. 
Model dosyasını aşağıdaki şekilde edinebilirsiniz:

1. Kendi modelinizi eğitin: `python train_model.py`
2. Veya önceden eğitilmiş modeli kullanın (sağlanmışsa)

## Dosya Yapısı

```
models/
├── yolov8_phase_detection.pt  # Ana eğitilmiş model
├── config.yaml                # Model konfigürasyonu
└── README.md                  # Bu dosya
```
