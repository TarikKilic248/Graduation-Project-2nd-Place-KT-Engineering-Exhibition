"""
PDF Sunum Oluşturucu

Bu script projenin PDF sunumunu oluşturur.
"""

from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm, inch
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_JUSTIFY
from reportlab.lib import colors
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, PageBreak,
    Table, TableStyle, Image as RLImage, Flowable
)
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from datetime import datetime
import os


class NumberedCanvas:
    """Sayfa numarası ekleyen canvas"""
    def __init__(self, canvas, doc):
        self.canvas = canvas
        self.doc = doc
        
    def __call__(self, canvas, doc):
        canvas.saveState()
        # Sayfa numarası
        page_num = canvas.getPageNumber()
        text = f"Sayfa {page_num}"
        canvas.setFont('Helvetica', 9)
        canvas.drawRightString(A4[0] - 2*cm, 1.5*cm, text)
        canvas.restoreState()


def create_presentation_pdf(output_file='presentation.pdf'):
    """
    Proje sunumu PDF'i oluşturur
    
    Args:
        output_file: Çıktı PDF dosyası
    """
    print("PDF sunumu oluşturuluyor...")
    
    # PDF dosyası oluştur
    doc = SimpleDocTemplate(
        output_file,
        pagesize=A4,
        rightMargin=2*cm,
        leftMargin=2*cm,
        topMargin=2*cm,
        bottomMargin=2*cm
    )
    
    # Stil tanımlamaları
    styles = getSampleStyleSheet()
    
    # Başlık stili
    title_style = ParagraphStyle(
        'CustomTitle',
        parent=styles['Heading1'],
        fontSize=24,
        textColor=colors.HexColor('#1a237e'),
        spaceAfter=30,
        alignment=TA_CENTER,
        fontName='Helvetica-Bold'
    )
    
    # Alt başlık stili
    subtitle_style = ParagraphStyle(
        'CustomSubtitle',
        parent=styles['Heading2'],
        fontSize=16,
        textColor=colors.HexColor('#283593'),
        spaceAfter=12,
        spaceBefore=12,
        alignment=TA_CENTER,
        fontName='Helvetica-Bold'
    )
    
    # Bölüm başlığı stili
    section_style = ParagraphStyle(
        'SectionTitle',
        parent=styles['Heading2'],
        fontSize=16,
        textColor=colors.HexColor('#0d47a1'),
        spaceAfter=12,
        spaceBefore=20,
        fontName='Helvetica-Bold'
    )
    
    # Normal metin stili
    normal_style = ParagraphStyle(
        'CustomNormal',
        parent=styles['Normal'],
        fontSize=11,
        alignment=TA_JUSTIFY,
        spaceAfter=10
    )
    
    # Madde işareti stili
    bullet_style = ParagraphStyle(
        'CustomBullet',
        parent=styles['Normal'],
        fontSize=11,
        leftIndent=20,
        spaceAfter=6
    )
    
    # İçerik listesi
    story = []
    
    # === KAPAK SAYFASI ===
    story.append(Spacer(1, 2*cm))
    
    # Başlık
    story.append(Paragraph(
        "Metalik Malzeme Faz Analizi",
        title_style
    ))
    
    story.append(Spacer(1, 0.5*cm))
    
    story.append(Paragraph(
        "YOLO Tabanlı Görüntü İşleme Projesi",
        subtitle_style
    ))
    
    story.append(Spacer(1, 1.5*cm))
    
    # Ödül bilgisi
    award_style = ParagraphStyle(
        'Award',
        parent=subtitle_style,
        fontSize=18,
        textColor=colors.HexColor('#d32f2f')
    )
    
    story.append(Paragraph(
        "🏆 KT Mühendislik Sergisi<br/>2. Ödül",
        award_style
    ))
    
    story.append(Spacer(1, 2*cm))
    
    # Tarih
    date_style = ParagraphStyle(
        'Date',
        parent=normal_style,
        alignment=TA_CENTER,
        fontSize=12
    )
    
    story.append(Paragraph(
        f"Sunum Tarihi: {datetime.now().strftime('%d.%m.%Y')}",
        date_style
    ))
    
    story.append(PageBreak())
    
    # === İÇİNDEKİLER ===
    story.append(Paragraph("İçindekiler", section_style))
    story.append(Spacer(1, 0.5*cm))
    
    toc_data = [
        ["1", "Proje Özeti"],
        ["2", "Problem Tanımı"],
        ["3", "Metodoloji"],
        ["4", "Sistem Mimarisi"],
        ["5", "Sonuçlar ve Performans"],
        ["6", "Kullanım ve Uygulama"],
        ["7", "Gelecek Çalışmalar"],
        ["8", "Sonuç"]
    ]
    
    toc_table = Table(toc_data, colWidths=[2*cm, 14*cm])
    toc_table.setStyle(TableStyle([
        ('FONT', (0, 0), (-1, -1), 'Helvetica', 11),
        ('TEXTCOLOR', (0, 0), (0, -1), colors.HexColor('#0d47a1')),
        ('FONTNAME', (0, 0), (0, -1), 'Helvetica-Bold'),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('LEFTPADDING', (0, 0), (-1, -1), 6),
        ('RIGHTPADDING', (0, 0), (-1, -1), 6),
        ('TOPPADDING', (0, 0), (-1, -1), 6),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
    ]))
    
    story.append(toc_table)
    story.append(PageBreak())
    
    # === 1. PROJE ÖZETİ ===
    story.append(Paragraph("1. Proje Özeti", section_style))
    
    story.append(Paragraph(
        "Bu proje, metalik malzeme mikroyapı görüntülerinden YOLO (You Only Look Once) "
        "derin öğrenme modeli kullanarak otomatik faz analizi yapan bir sistemdir. "
        "Geleneksel manuel analiz yöntemlerinin yerini alan bu sistem, hızlı, doğru "
        "ve objektif sonuçlar sunmaktadır.",
        normal_style
    ))
    
    story.append(Spacer(1, 0.3*cm))
    
    # Ana özellikler
    features = [
        "✓ YOLO v8 tabanlı nesne algılama teknolojisi",
        "✓ 5 farklı faz türünün otomatik tespiti (Ferrit, Perlit, Austenit, Martenzit, Bainit)",
        "✓ %94.5 doğruluk oranı ile uzman seviyesinde performans",
        "✓ Milisaniyeler içinde hızlı analiz (6.4 ms/görüntü)",
        "✓ Batch işleme ile yüzlerce görüntünün toplu analizi",
        "✓ Detaylı raporlama ve görselleştirme özellikleri"
    ]
    
    for feature in features:
        story.append(Paragraph(feature, bullet_style))
    
    story.append(PageBreak())
    
    # === 2. PROBLEM TANIMI ===
    story.append(Paragraph("2. Problem Tanımı", section_style))
    
    story.append(Paragraph(
        "<b>Geleneksel Yöntemin Zorlukları:</b>",
        normal_style
    ))
    
    problems = [
        "• Manuel analiz 30-60 dakika sürmekte",
        "• Uzman metalurg bilgisi gerektirmekte",
        "• Subjektif değerlendirme riski taşımakta",
        "• İnsan hatası olasılığı yüksek",
        "• Tekrar edilebilirlik düşük",
        "• Büyük veri setlerinde ölçeklenebilirlik sorunu"
    ]
    
    for problem in problems:
        story.append(Paragraph(problem, bullet_style))
    
    story.append(Spacer(1, 0.5*cm))
    
    story.append(Paragraph(
        "<b>Önerilen Çözüm:</b>",
        normal_style
    ))
    
    story.append(Paragraph(
        "YOLO derin öğrenme modeli ile otomatik faz tespit sistemi geliştirilmiştir. "
        "Bu sistem, görüntü işleme ve yapay zeka teknolojilerini birleştirerek, "
        "metalik malzeme analizini otomatikleştirmekte ve standartlaştırmaktadır.",
        normal_style
    ))
    
    story.append(PageBreak())
    
    # === 3. METODOLOJİ ===
    story.append(Paragraph("3. Metodoloji", section_style))
    
    methodology_steps = [
        ("Veri Toplama", 
         "1000 adet metalik malzeme mikroskop görüntüsü toplanmış, "
         "çeşitli çelik türleri ve ısıl işlem koşulları kapsanmıştır."),
        
        ("Veri Etiketleme",
         "Uzman metalurglar tarafından görüntülerdeki fazlar etiketlenmiş, "
         "YOLO formatında annotation dosyaları oluşturulmuştur."),
        
        ("Veri Artırma",
         "Rotation, flip, scale gibi tekniklerle veri seti zenginleştirilmiş, "
         "model genelleme kapasitesi artırılmıştır."),
        
        ("Model Eğitimi",
         "YOLO v8 Small modeli, transfer learning ile COCO ağırlıkları "
         "kullanılarak 100 epoch eğitilmiştir."),
        
        ("Değerlendirme",
         "Precision, Recall, mAP metrikleri ile model performansı "
         "ölçülmüş ve optimize edilmiştir.")
    ]
    
    for i, (title, desc) in enumerate(methodology_steps, 1):
        story.append(Paragraph(f"<b>{i}. {title}:</b> {desc}", normal_style))
    
    story.append(PageBreak())
    
    # === 4. SİSTEM MİMARİSİ ===
    story.append(Paragraph("4. Sistem Mimarisi", section_style))
    
    story.append(Paragraph(
        "<b>YOLO v8 Model Yapısı:</b>",
        normal_style
    ))
    
    architecture = [
        "• <b>Backbone:</b> CSPDarknet53 (özellik çıkarma)",
        "• <b>Neck:</b> PAN (Path Aggregation Network)",
        "• <b>Head:</b> Detection head (nesne tespiti)",
        "• <b>Parametre Sayısı:</b> 11.2 milyon",
        "• <b>Model Boyutu:</b> 22.5 MB"
    ]
    
    for item in architecture:
        story.append(Paragraph(item, bullet_style))
    
    story.append(Spacer(1, 0.5*cm))
    
    story.append(Paragraph(
        "<b>Eğitim Konfigürasyonu:</b>",
        normal_style
    ))
    
    config = [
        "• Epoch: 100",
        "• Batch Size: 16",
        "• Learning Rate: 0.01 → 0.001 (cosine annealing)",
        "• Optimizer: AdamW",
        "• Image Size: 640×640",
        "• GPU: NVIDIA RTX 3080",
        "• Eğitim Süresi: 8.5 saat"
    ]
    
    for item in config:
        story.append(Paragraph(item, bullet_style))
    
    story.append(PageBreak())
    
    # === 5. SONUÇLAR VE PERFORMANS ===
    story.append(Paragraph("5. Sonuçlar ve Performans", section_style))
    
    story.append(Paragraph("<b>Genel Performans Metrikleri:</b>", normal_style))
    story.append(Spacer(1, 0.3*cm))
    
    # Performans tablosu
    perf_data = [
        ['Metrik', 'Değer'],
        ['Accuracy (Doğruluk)', '94.5%'],
        ['Precision (Kesinlik)', '93.2%'],
        ['Recall (Duyarlılık)', '95.1%'],
        ['F1-Score', '94.1%'],
        ['mAP@0.5', '92.8%'],
        ['İşlem Süresi', '6.4 ms'],
        ['FPS (GPU)', '156']
    ]
    
    perf_table = Table(perf_data, colWidths=[8*cm, 6*cm])
    perf_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#0d47a1')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 11),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('LEFTPADDING', (0, 0), (-1, -1), 8),
        ('RIGHTPADDING', (0, 0), (-1, -1), 8),
    ]))
    
    story.append(perf_table)
    story.append(Spacer(1, 0.5*cm))
    
    story.append(Paragraph("<b>Faz Bazında Performans:</b>", normal_style))
    story.append(Spacer(1, 0.3*cm))
    
    phase_data = [
        ['Faz', 'Precision', 'Recall', 'F1-Score'],
        ['Ferrit', '95.3%', '96.1%', '95.7%'],
        ['Perlit', '92.8%', '94.5%', '93.6%'],
        ['Austenit', '91.5%', '93.8%', '92.6%'],
        ['Martenzit', '94.1%', '95.9%', '95.0%'],
        ['Bainit', '92.4%', '94.2%', '93.3%']
    ]
    
    phase_table = Table(phase_data, colWidths=[4*cm, 3.5*cm, 3.5*cm, 3.5*cm])
    phase_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#0d47a1')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 10),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
    ]))
    
    story.append(phase_table)
    story.append(PageBreak())
    
    # === 6. KULLANIM VE UYGULAMA ===
    story.append(Paragraph("6. Kullanım ve Uygulama", section_style))
    
    story.append(Paragraph(
        "<b>Sistem Gereksinimleri:</b>",
        normal_style
    ))
    
    requirements = [
        "• Python 3.8 veya üzeri",
        "• CUDA destekli GPU (önerilen, opsiyonel)",
        "• 4GB RAM (minimum), 8GB+ (önerilen)",
        "• 500MB disk alanı (model ve bağımlılıklar için)"
    ]
    
    for req in requirements:
        story.append(Paragraph(req, bullet_style))
    
    story.append(Spacer(1, 0.5*cm))
    
    story.append(Paragraph(
        "<b>Kurulum Adımları:</b>",
        normal_style
    ))
    
    story.append(Paragraph(
        "<font face='Courier'>1. git clone [repository-url]<br/>"
        "2. pip install -r requirements.txt<br/>"
        "3. python phase_analysis.py</font>",
        bullet_style
    ))
    
    story.append(Spacer(1, 0.5*cm))
    
    story.append(Paragraph(
        "<b>Kullanım Senaryoları:</b>",
        normal_style
    ))
    
    use_cases = [
        "• <b>Metalurji Laboratuvarları:</b> Rutin mikroyapı analizi ve kalite kontrol",
        "• <b>Ar-Ge Merkezleri:</b> Yeni malzeme geliştirme ve karakterizasyon",
        "• <b>Üretim Tesisleri:</b> Üretim hattı kalite kontrolü ve izleme",
        "• <b>Eğitim Kurumları:</b> Malzeme bilimi öğretimi ve öğrenci projeleri"
    ]
    
    for use_case in use_cases:
        story.append(Paragraph(use_case, bullet_style))
    
    story.append(PageBreak())
    
    # === 7. GELECEK ÇALIŞMALAR ===
    story.append(Paragraph("7. Gelecek Çalışmalar", section_style))
    
    future_work = [
        ("<b>Instance Segmentation:</b>", 
         "Daha hassas alan hesabı için Mask R-CNN veya YOLO-Seg modeline geçiş"),
        
        ("<b>3D Analiz:</b>",
         "Seri kesit görüntülerinden 3D mikroyapı rekonstrüksiyonu"),
        
        ("<b>Web Arayüzü:</b>",
         "Kullanıcı dostu web tabanlı analiz platformu geliştirme"),
        
        ("<b>Mobil Uygulama:</b>",
         "Sahada hızlı analiz için mobil aplikasyon"),
        
        ("<b>Veri Tabanı Entegrasyonu:</b>",
         "Geçmiş analizlerin saklanması ve karşılaştırılması"),
        
        ("<b>Gerçek Zamanlı Analiz:</b>",
         "Canlı mikroskop görüntülerinin anlık analizi")
    ]
    
    for title, desc in future_work:
        story.append(Paragraph(f"{title} {desc}", normal_style))
    
    story.append(PageBreak())
    
    # === 8. SONUÇ ===
    story.append(Paragraph("8. Sonuç", section_style))
    
    story.append(Paragraph(
        "Bu proje, metalik malzeme faz analizinde yapay zeka ve derin öğrenme "
        "tekniklerinin başarılı bir uygulamasını göstermektedir. YOLO v8 modeli "
        "ile elde edilen %94.5 doğruluk oranı, sistemin uzman seviyesinde "
        "performans sergilediğini kanıtlamaktadır.",
        normal_style
    ))
    
    story.append(Spacer(1, 0.3*cm))
    
    story.append(Paragraph(
        "<b>Ana Başarımlar:</b>",
        normal_style
    ))
    
    achievements = [
        "✓ Manuel analize göre 250x daha hızlı işleme",
        "✓ Objektif ve tekrarlanabilir sonuçlar",
        "✓ Sınırsız ölçeklenebilirlik",
        "✓ Açık kaynak ve erişilebilir teknoloji",
        "✓ Endüstriyel uygulamaya hazır sistem"
    ]
    
    for achievement in achievements:
        story.append(Paragraph(achievement, bullet_style))
    
    story.append(Spacer(1, 0.5*cm))
    
    story.append(Paragraph(
        "Proje, metalurji ve malzeme mühendisliği alanında dijital dönüşümün "
        "önemini vurgulamakta ve gelecek çalışmalar için sağlam bir temel "
        "oluşturmaktadır. KT Mühendislik Sergisi'nde 2. ödülü kazanması, "
        "projenin kalitesini ve özgünlüğünü teyit etmektedir.",
        normal_style
    ))
    
    story.append(Spacer(1, 1*cm))
    
    # Teşekkür
    thanks_style = ParagraphStyle(
        'Thanks',
        parent=normal_style,
        fontSize=10,
        textColor=colors.HexColor('#424242'),
        alignment=TA_CENTER
    )
    
    story.append(Paragraph(
        "─────────────────────────────────────",
        thanks_style
    ))
    
    story.append(Spacer(1, 0.3*cm))
    
    story.append(Paragraph(
        "<b>Teşekkürler</b><br/>"
        "KT Mühendislik Sergisi organizatörlerine, danışman hocalarıma<br/>"
        "ve bu projeye destek olan herkese teşekkür ederim.",
        thanks_style
    ))
    
    story.append(Spacer(1, 0.5*cm))
    
    story.append(Paragraph(
        "🏆 <b>KT Mühendislik Sergisi - 2. Ödül</b> 🏆",
        thanks_style
    ))
    
    # PDF'i oluştur
    doc.build(story, onFirstPage=NumberedCanvas(None, doc), 
              onLaterPages=NumberedCanvas(None, doc))
    
    print(f"✅ PDF sunumu başarıyla oluşturuldu: {output_file}")
    print(f"   Dosya boyutu: {os.path.getsize(output_file) / 1024:.2f} KB")


if __name__ == "__main__":
    create_presentation_pdf('presentation.pdf')
