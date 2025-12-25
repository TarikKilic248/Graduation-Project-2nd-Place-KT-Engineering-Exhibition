"""
Metalik Malzeme Faz Analizi - Ana Analiz Modülü

Bu modül YOLO modelini kullanarak metalik malzeme görüntülerinden
faz analizi yapmak için gerekli fonksiyonları içerir.
"""

import os
import cv2
import numpy as np
from pathlib import Path
from typing import Dict, List, Tuple, Optional
from ultralytics import YOLO
import matplotlib.pyplot as plt
from datetime import datetime


class PhaseAnalyzer:
    """Metalik malzeme faz analizi için ana sınıf"""
    
    def __init__(self, model_path: str = 'models/yolov8_phase_detection.pt', 
                 confidence_threshold: float = 0.5):
        """
        PhaseAnalyzer sınıfını başlatır
        
        Args:
            model_path: Eğitilmiş YOLO model dosyasının yolu
            confidence_threshold: Tespit için minimum güven eşiği
        """
        self.model_path = model_path
        self.confidence_threshold = confidence_threshold
        self.model = None
        self.phase_names = {
            0: 'Ferrit',
            1: 'Perlit',
            2: 'Austenit',
            3: 'Martenzit',
            4: 'Bainit'
        }
        
        if os.path.exists(model_path):
            self.load_model()
        else:
            print(f"Model dosyası bulunamadı: {model_path}")
            print("Model eğitimi için aşağıdaki komutu çalıştırın:")
            print("  python train_model.py --data data/annotations/ --epochs 100")
    
    def load_model(self):
        """YOLO modelini yükler"""
        try:
            self.model = YOLO(self.model_path)
            print(f"Model başarıyla yüklendi: {self.model_path}")
        except Exception as e:
            print(f"Model yükleme hatası: {e}")
            raise
    
    def analyze_image(self, image_path: str) -> Dict:
        """
        Tek bir görüntüyü analiz eder
        
        Args:
            image_path: Analiz edilecek görüntünün yolu
            
        Returns:
            Dict: Analiz sonuçlarını içeren dictionary
        """
        if self.model is None:
            raise ValueError("Model yüklenmemiş. Önce load_model() çağrılmalı.")
        
        # Görüntüyü oku
        image = cv2.imread(image_path)
        if image is None:
            raise ValueError(f"Görüntü okunamadı: {image_path}")
        
        # YOLO ile tahmin yap
        results = self.model(image, conf=self.confidence_threshold)
        
        # Sonuçları işle
        detections = self._process_results(results[0], image.shape)
        
        return {
            'image_path': image_path,
            'image_shape': image.shape,
            'detections': detections,
            'phase_statistics': self._calculate_statistics(detections),
            'timestamp': datetime.now().isoformat()
        }
    
    def _process_results(self, result, image_shape: Tuple) -> List[Dict]:
        """YOLO sonuçlarını işler"""
        detections = []
        
        if result.boxes is not None:
            boxes = result.boxes.xyxy.cpu().numpy()
            confidences = result.boxes.conf.cpu().numpy()
            class_ids = result.boxes.cls.cpu().numpy().astype(int)
            
            for box, conf, cls_id in zip(boxes, confidences, class_ids):
                detection = {
                    'bbox': box.tolist(),
                    'confidence': float(conf),
                    'class_id': int(cls_id),
                    'class_name': self.phase_names.get(cls_id, 'Unknown'),
                    'area': self._calculate_box_area(box)
                }
                detections.append(detection)
        
        return detections
    
    def _calculate_box_area(self, box: np.ndarray) -> float:
        """Bounding box alanını hesaplar"""
        x1, y1, x2, y2 = box
        return float((x2 - x1) * (y2 - y1))
    
    def _calculate_statistics(self, detections: List[Dict]) -> Dict:
        """Tespit edilen fazların istatistiklerini hesaplar"""
        stats = {
            'total_detections': len(detections),
            'phase_counts': {},
            'phase_areas': {},
            'average_confidence': 0.0
        }
        
        if not detections:
            return stats
        
        # Faz sayıları ve alanları
        for detection in detections:
            phase_name = detection['class_name']
            
            # Sayıları güncelle
            stats['phase_counts'][phase_name] = \
                stats['phase_counts'].get(phase_name, 0) + 1
            
            # Alanları güncelle
            stats['phase_areas'][phase_name] = \
                stats['phase_areas'].get(phase_name, 0.0) + detection['area']
        
        # Ortalama güven skoru
        confidences = [d['confidence'] for d in detections]
        stats['average_confidence'] = float(np.mean(confidences))
        
        return stats
    
    def visualize_results(self, results: Dict, save_path: Optional[str] = None,
                         show: bool = True) -> None:
        """
        Analiz sonuçlarını görselleştirir
        
        Args:
            results: analyze_image() çıktısı
            save_path: Görüntünün kaydedileceği yol
            show: Görüntüyü göster
        """
        # Görüntüyü oku
        image = cv2.imread(results['image_path'])
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        
        # Renk paleti
        colors = {
            'Ferrit': (255, 0, 0),      # Kırmızı
            'Perlit': (0, 255, 0),      # Yeşil
            'Austenit': (0, 0, 255),    # Mavi
            'Martenzit': (255, 255, 0), # Sarı
            'Bainit': (255, 0, 255)     # Magenta
        }
        
        # Tespit edilen fazları çiz
        for detection in results['detections']:
            x1, y1, x2, y2 = map(int, detection['bbox'])
            phase_name = detection['class_name']
            confidence = detection['confidence']
            
            color = colors.get(phase_name, (128, 128, 128))
            
            # Bounding box çiz
            cv2.rectangle(image, (x1, y1), (x2, y2), color, 2)
            
            # Etiket ekle
            label = f"{phase_name}: {confidence:.2f}"
            (label_width, label_height), _ = cv2.getTextSize(
                label, cv2.FONT_HERSHEY_SIMPLEX, 0.5, 1
            )
            cv2.rectangle(image, (x1, y1 - label_height - 5),
                         (x1 + label_width, y1), color, -1)
            cv2.putText(image, label, (x1, y1 - 5),
                       cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)
        
        # Görselleştir
        if show:
            plt.figure(figsize=(12, 8))
            plt.imshow(image)
            plt.title(f"Faz Analizi Sonuçları\n"
                     f"Toplam Tespit: {results['phase_statistics']['total_detections']}")
            plt.axis('off')
            
            if save_path:
                plt.savefig(save_path, bbox_inches='tight', dpi=300)
                print(f"Görüntü kaydedildi: {save_path}")
            
            plt.show()
        elif save_path:
            cv2.imwrite(save_path, cv2.cvtColor(image, cv2.COLOR_RGB2BGR))
            print(f"Görüntü kaydedildi: {save_path}")
    
    def batch_analyze(self, input_dir: str, output_dir: str = 'results/') -> List[Dict]:
        """
        Bir klasördeki tüm görüntüleri analiz eder
        
        Args:
            input_dir: Giriş görüntülerinin bulunduğu klasör
            output_dir: Çıktıların kaydedileceği klasör
            
        Returns:
            List[Dict]: Tüm analiz sonuçları
        """
        # Çıktı klasörünü oluştur
        output_path = Path(output_dir)
        output_path.mkdir(parents=True, exist_ok=True)
        (output_path / 'images').mkdir(parents=True, exist_ok=True)
        
        # Desteklenen görüntü formatları
        extensions = ['.jpg', '.jpeg', '.png', '.bmp', '.tiff']
        
        # Tüm görüntüleri bul
        image_files = []
        for ext in extensions:
            image_files.extend(Path(input_dir).glob(f'*{ext}'))
        
        print(f"Toplam {len(image_files)} görüntü bulundu.")
        
        # Tüm görüntüleri analiz et
        all_results = []
        for image_file in image_files:
            print(f"Analiz ediliyor: {image_file.name}")
            
            try:
                results = self.analyze_image(str(image_file))
                all_results.append(results)
                
                # Sonuçları görselleştir ve kaydet
                result_output_path = str(Path(output_dir) / 'images' / f"{image_file.stem}_result.jpg")
                self.visualize_results(results, save_path=result_output_path, show=False)
                
            except Exception as e:
                print(f"Hata ({image_file.name}): {e}")
        
        # Özet rapor oluştur
        self._generate_batch_summary(all_results, output_dir)
        
        return all_results
    
    def _generate_batch_summary(self, results_list: List[Dict], output_dir: str):
        """Batch işleme için özet rapor oluşturur"""
        summary_path = str(Path(output_dir) / 'batch_summary.txt')
        
        with open(summary_path, 'w', encoding='utf-8') as f:
            f.write("=" * 60 + "\n")
            f.write("Metalik Malzeme Faz Analizi - Batch İşleme Özeti\n")
            f.write("=" * 60 + "\n\n")
            f.write(f"Tarih: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write(f"Toplam İşlenen Görüntü: {len(results_list)}\n\n")
            
            # Genel istatistikler
            total_detections = sum(r['phase_statistics']['total_detections'] 
                                  for r in results_list)
            confidence_values = [r['phase_statistics']['average_confidence'] 
                               for r in results_list if r['phase_statistics']['average_confidence'] > 0]
            avg_confidence = np.mean(confidence_values) if confidence_values else 0.0
            
            f.write(f"Toplam Tespit: {total_detections}\n")
            f.write(f"Ortalama Güven Skoru: {avg_confidence:.2%}\n\n")
            
            # Görüntü bazında sonuçlar
            f.write("Görüntü Bazında Sonuçlar:\n")
            f.write("-" * 60 + "\n")
            
            for i, result in enumerate(results_list, 1):
                f.write(f"\n{i}. {Path(result['image_path']).name}\n")
                f.write(f"   Tespit Sayısı: {result['phase_statistics']['total_detections']}\n")
                
                if result['phase_statistics']['phase_counts']:
                    f.write("   Faz Dağılımı:\n")
                    for phase, count in result['phase_statistics']['phase_counts'].items():
                        f.write(f"      - {phase}: {count}\n")
        
        print(f"\nÖzet rapor kaydedildi: {summary_path}")
    
    def generate_report(self, results: Dict, output_path: str = 'report.txt'):
        """
        Analiz sonuçları için detaylı rapor oluşturur
        
        Args:
            results: analyze_image() çıktısı
            output_path: Raporun kaydedileceği yol
        """
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write("=" * 60 + "\n")
            f.write("Metalik Malzeme Faz Analizi Raporu\n")
            f.write("=" * 60 + "\n\n")
            
            f.write(f"Görüntü: {Path(results['image_path']).name}\n")
            f.write(f"Tarih: {results['timestamp']}\n")
            f.write(f"Görüntü Boyutu: {results['image_shape'][1]}x{results['image_shape'][0]}\n\n")
            
            stats = results['phase_statistics']
            f.write(f"Toplam Tespit: {stats['total_detections']}\n")
            f.write(f"Ortalama Güven Skoru: {stats['average_confidence']:.2%}\n\n")
            
            if stats['phase_counts']:
                f.write("Faz Dağılımı:\n")
                f.write("-" * 40 + "\n")
                for phase, count in stats['phase_counts'].items():
                    area = stats['phase_areas'].get(phase, 0)
                    f.write(f"{phase}:\n")
                    f.write(f"  Tespit Sayısı: {count}\n")
                    f.write(f"  Toplam Alan: {area:.2f} piksel²\n\n")
            
            f.write("\nDetaylı Tespit Listesi:\n")
            f.write("-" * 40 + "\n")
            for i, detection in enumerate(results['detections'], 1):
                f.write(f"{i}. {detection['class_name']}\n")
                f.write(f"   Güven Skoru: {detection['confidence']:.2%}\n")
                f.write(f"   Alan: {detection['area']:.2f} piksel²\n")
                f.write(f"   Konum: {detection['bbox']}\n\n")
        
        print(f"Rapor kaydedildi: {output_path}")


def main():
    """Ana fonksiyon - Örnek kullanım"""
    print("Metalik Malzeme Faz Analizi Sistemi")
    print("=" * 60)
    
    # Analyzer'ı başlat
    analyzer = PhaseAnalyzer(
        model_path='models/yolov8_phase_detection.pt',
        confidence_threshold=0.5
    )
    
    # Örnek kullanım
    # analyzer.batch_analyze('data/raw/', 'results/')


if __name__ == "__main__":
    main()
