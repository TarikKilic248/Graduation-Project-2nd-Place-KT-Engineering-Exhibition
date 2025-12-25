"""
YOLO Model Eğitim Scripti

Bu script metalik malzeme faz tespiti için YOLO modelini eğitir.
"""

import os
import argparse
from pathlib import Path
from ultralytics import YOLO
import yaml


def create_dataset_config(data_dir: str, output_file: str = 'dataset.yaml'):
    """
    Veri seti konfigürasyon dosyası oluşturur
    
    Args:
        data_dir: Veri seti dizini
        output_file: Çıktı YAML dosyası
    """
    config = {
        'path': os.path.abspath(data_dir),
        'train': 'images/train',
        'val': 'images/val',
        'test': 'images/test',
        'nc': 5,  # Sınıf sayısı
        'names': {
            0: 'Ferrit',
            1: 'Perlit',
            2: 'Austenit',
            3: 'Martenzit',
            4: 'Bainit'
        }
    }
    
    with open(output_file, 'w') as f:
        yaml.dump(config, f, default_flow_style=False)
    
    print(f"Veri seti konfigürasyonu oluşturuldu: {output_file}")
    return output_file


def train_model(data_config: str, epochs: int = 100, batch_size: int = 16,
                img_size: int = 640, model_name: str = 'yolov8n.pt',
                device: str = '0'):
    """
    YOLO modelini eğitir
    
    Args:
        data_config: Veri seti konfigürasyon dosyası
        epochs: Eğitim epoch sayısı
        batch_size: Batch boyutu
        img_size: Görüntü boyutu
        model_name: Başlangıç model adı (yolov8n.pt, yolov8s.pt, vb.)
        device: Cihaz (0 = GPU, cpu = CPU)
    """
    print("=" * 60)
    print("YOLO Model Eğitimi Başlıyor")
    print("=" * 60)
    print(f"Model: {model_name}")
    print(f"Epochs: {epochs}")
    print(f"Batch Size: {batch_size}")
    print(f"Image Size: {img_size}")
    print(f"Device: {device}")
    print("=" * 60)
    
    # Model yükle
    model = YOLO(model_name)
    
    # Eğitim parametreleri
    results = model.train(
        data=data_config,
        epochs=epochs,
        batch=batch_size,
        imgsz=img_size,
        device=device,
        patience=50,
        save=True,
        project='runs/train',
        name='phase_detection',
        exist_ok=True,
        pretrained=True,
        optimizer='AdamW',
        lr0=0.01,
        lrf=0.001,
        momentum=0.937,
        weight_decay=0.0005,
        warmup_epochs=3,
        warmup_momentum=0.8,
        box=7.5,
        cls=0.5,
        dfl=1.5,
        pose=12.0,
        kobj=2.0,
        label_smoothing=0.0,
        nbs=64,
        hsv_h=0.015,
        hsv_s=0.7,
        hsv_v=0.4,
        degrees=0.0,
        translate=0.1,
        scale=0.5,
        shear=0.0,
        perspective=0.0,
        flipud=0.0,
        fliplr=0.5,
        mosaic=1.0,
        mixup=0.0,
        copy_paste=0.0
    )
    
    print("\n" + "=" * 60)
    print("Eğitim Tamamlandı!")
    print("=" * 60)
    print(f"En iyi model: runs/train/phase_detection/weights/best.pt")
    
    return results


def validate_model(model_path: str, data_config: str):
    """
    Eğitilmiş modeli doğrular
    
    Args:
        model_path: Model dosyası yolu
        data_config: Veri seti konfigürasyonu
    """
    print("\n" + "=" * 60)
    print("Model Doğrulama")
    print("=" * 60)
    
    model = YOLO(model_path)
    metrics = model.val(data=data_config)
    
    print(f"\nDoğrulama Metrikleri:")
    print(f"mAP50: {metrics.box.map50:.4f}")
    print(f"mAP50-95: {metrics.box.map:.4f}")
    print(f"Precision: {metrics.box.mp:.4f}")
    print(f"Recall: {metrics.box.mr:.4f}")
    
    return metrics


def export_model(model_path: str, format: str = 'onnx'):
    """
    Modeli farklı formatlara dışa aktarır
    
    Args:
        model_path: Model dosyası yolu
        format: Dışa aktarma formatı (onnx, torchscript, tflite, vb.)
    """
    print(f"\nModel {format} formatına dışa aktarılıyor...")
    
    model = YOLO(model_path)
    model.export(format=format)
    
    print(f"Model başarıyla dışa aktarıldı!")


def main():
    parser = argparse.ArgumentParser(
        description='YOLO model eğitimi - Metalik malzeme faz analizi'
    )
    
    parser.add_argument(
        '--data',
        type=str,
        default='data/annotations',
        help='Veri seti dizini'
    )
    
    parser.add_argument(
        '--epochs',
        type=int,
        default=100,
        help='Eğitim epoch sayısı'
    )
    
    parser.add_argument(
        '--batch-size',
        type=int,
        default=16,
        help='Batch boyutu'
    )
    
    parser.add_argument(
        '--img-size',
        type=int,
        default=640,
        help='Görüntü boyutu'
    )
    
    parser.add_argument(
        '--model',
        type=str,
        default='yolov8n.pt',
        help='Başlangıç model (yolov8n.pt, yolov8s.pt, yolov8m.pt, vb.)'
    )
    
    parser.add_argument(
        '--device',
        type=str,
        default='0',
        help='Cihaz (0 = GPU, cpu = CPU)'
    )
    
    parser.add_argument(
        '--validate',
        action='store_true',
        help='Eğitim sonrası doğrulama yap'
    )
    
    parser.add_argument(
        '--export',
        type=str,
        choices=['onnx', 'torchscript', 'tflite'],
        help='Modeli belirtilen formata dışa aktar'
    )
    
    args = parser.parse_args()
    
    # Veri seti konfigürasyonu oluştur
    config_file = create_dataset_config(args.data)
    
    # Modeli eğit
    train_model(
        data_config=config_file,
        epochs=args.epochs,
        batch_size=args.batch_size,
        img_size=args.img_size,
        model_name=args.model,
        device=args.device
    )
    
    # En iyi model yolu
    best_model = 'runs/train/phase_detection/weights/best.pt'
    
    # Doğrulama
    if args.validate and os.path.exists(best_model):
        validate_model(best_model, config_file)
    
    # Dışa aktarma
    if args.export and os.path.exists(best_model):
        export_model(best_model, args.export)
    
    print("\n" + "=" * 60)
    print("İşlemler Tamamlandı!")
    print("=" * 60)
    print(f"\nSonraki adımlar:")
    print(f"1. En iyi modeli 'models/' dizinine kopyalayın:")
    print(f"   cp {best_model} models/yolov8_phase_detection.pt")
    print(f"2. Modeli test edin:")
    print(f"   python phase_analysis.py")


if __name__ == "__main__":
    main()
