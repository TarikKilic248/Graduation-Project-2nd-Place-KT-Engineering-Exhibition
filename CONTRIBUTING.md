# Katkıda Bulunma Rehberi

Projeye katkıda bulunmak istediğiniz için teşekkür ederiz! 

## 🤝 Nasıl Katkıda Bulunabilirsiniz?

### Hata Bildirimi

Bir hata buldunuz mu? Lütfen bir issue açın ve şunları ekleyin:

- Hatanın açık bir tanımı
- Hatayı yeniden oluşturma adımları
- Beklenen davranış
- Ekran görüntüleri (varsa)
- Sistem bilgileri (OS, Python versiyonu, vb.)

### Özellik Önerisi

Yeni bir özellik mi öneriyorsunuz?

1. Önce mevcut issues'ları kontrol edin
2. Eğer yoksa, yeni bir issue açın
3. Özelliği detaylı açıklayın
4. Kullanım senaryoları ekleyin

### Kod Katkısı

1. Repository'yi fork edin
2. Yeni bir branch oluşturun (`git checkout -b feature/AmazingFeature`)
3. Değişikliklerinizi commit edin (`git commit -m 'Add some AmazingFeature'`)
4. Branch'inizi push edin (`git push origin feature/AmazingFeature`)
5. Pull Request açın

## 📝 Kod Standartları

### Python Kod Stili

- PEP 8 standartlarını takip edin
- Docstring'ler ekleyin (Google style)
- Type hints kullanın
- Anlamlı değişken isimleri kullanın

### Commit Mesajları

```
feat: yeni özellik ekle
fix: hata düzeltmesi
docs: dokümantasyon güncellemesi
style: kod formatı düzeltmesi
refactor: kod yeniden yapılandırma
test: test ekleme/güncelleme
chore: build/config güncellemeleri
```

## 🧪 Test

Kod değişikliklerinden önce:

```bash
# Kodunuzu test edin
python -m pytest tests/

# Linting yapın
flake8 phase_analysis.py
```

## 📚 Dokümantasyon

- Yeni özellikler için dokümantasyon ekleyin
- README.md'yi güncel tutun
- Kod içi yorumları güncelleyin

## 🔍 Pull Request Süreci

1. Kodunuzun PEP 8'e uygun olduğundan emin olun
2. Yeni özellikler için testler ekleyin
3. Dokümantasyonu güncelleyin
4. PR açıklamasında değişiklikleri detaylı açıklayın
5. Review sürecine katılın

## 💡 İyi Katkı Örnekleri

- Hata düzeltmeleri
- Performans iyileştirmeleri
- Yeni faz türleri desteği
- Dokümantasyon geliştirmeleri
- Test coverage artırma
- Örnek kullanımlar ekleme

## ❓ Sorular?

- GitHub Discussions kullanın
- Issue açın
- Proje sahipleriyle iletişime geçin

## 🙏 Teşekkürler

Her türlü katkı değerlidir. Küçük düzeltmelerden büyük özelliklere kadar her şey projeyi ilerletir!

---

**Happy Coding! 🚀**
