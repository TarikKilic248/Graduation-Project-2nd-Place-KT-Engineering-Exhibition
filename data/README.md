# Veri Seti Bilgileri

Bu klasör, metalik malzeme mikroyapı görüntülerini içerir.

## Klasör Yapısı

```
data/
├── raw/                # Ham, işlenmemiş görüntüler
├── processed/          # Ön işlemden geçmiş görüntüler
└── annotations/        # YOLO formatında etiketlenmiş veriler
    ├── images/
    │   ├── train/     # Eğitim görüntüleri
    │   ├── val/       # Doğrulama görüntüleri
    │   └── test/      # Test görüntüleri
    └── labels/
        ├── train/     # Eğitim etiketleri
        ├── val/       # Doğrulama etiketleri
        └── test/      # Test etiketleri
```

## Görüntü Formatı

- **Desteklenen formatlar**: JPG, JPEG, PNG, BMP, TIFF
- **Önerilen boyut**: 640×640 piksel
- **Renk uzayı**: RGB
- **Bit derinliği**: 8-bit

## Etiketleme Formatı

YOLO formatı kullanılmaktadır:

```
<class_id> <x_center> <y_center> <width> <height>
```

Her değer 0-1 arasında normalize edilmiştir.

### Sınıf ID'leri:

- 0: Ferrit
- 1: Perlit
- 2: Austenit
- 3: Martenzit
- 4: Bainit

## Örnek Veri

Örnek görüntüler ve etiketler projeye dahil edilmemiştir. 
Kendi veri setinizi hazırlamak için:

1. Mikroskop görüntülerini `raw/` klasörüne yerleştirin
2. LabelImg veya CVAT kullanarak etiketleyin
3. Etiketleri `annotations/` yapısına göre düzenleyin

## Veri Toplama İpuçları

- Farklı büyütme oranlarında görüntüler alın
- Çeşitli ısıl işlem koşullarını kapsayın
- Aydınlatma ve kontrast kalitesine dikkat edin
- Her faz türünden dengeli örnekler toplayın

## Veri Artırma

Model eğitimi sırasında otomatik veri artırma uygulanmaktadır:
- Yatay çevirme (flip)
- Rotasyon
- Ölçekleme
- Renk uzayı değişimleri
