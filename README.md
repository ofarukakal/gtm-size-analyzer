# GTM Size Analyzer

Google Tag Manager (GTM) konteyner dosyalarınızı analiz ederek etiketler, tetikleyiciler ve değişkenlerin boyutlarını ve detaylarını gösteren Python aracı.

## 🚀 Özellikler

- GTM konteyner JSON dosyasının detaylı analizi
- Etiketler (Tags), tetikleyiciler (Triggers) ve değişkenlerin (Variables) boyut analizi
- Büyükten küçüğe sıralanmış listeleme
- CSV formatında rapor çıktıları
- En büyük 10 öğenin özet listesi
- Terminal ekranında detaylı görüntüleme

## 📋 Gereksinimler

- Python 3.6 veya üzeri
- `json` modülü (Python ile birlikte gelir)
- `csv` modülü (Python ile birlikte gelir)

## 🔧 Kurulum

1. Bu dosyaları bilgisayarınıza indirin
2. GTM konteyner JSON dosyanızı `gtm-workspace.json` adıyla aynı klasöre koyun

## 📖 Kullanım

### 1. GTM JSON Dosyasını Hazırlama

- Google Tag Manager'da konteynerinizi açın
- **Admin** > **Export Container** seçeneğine gidin
- JSON dosyasını indirin
- Dosya adını `gtm-workspace.json` olarak değiştirin

### 2. Analizi Çalıştırma

```bash
python gtm-size-analyzer.py
```

## 📊 Çıktılar

### Terminal Çıktısı
- Konteyner bilgileri (ad, ID, hesap)
- Tüm etiketlerin detaylı listesi
- Tüm tetikleyicilerin detaylı listesi  
- Tüm değişkenlerin detaylı listesi
- En büyük 10 öğenin özet listesi

### CSV Dosyaları
Script çalıştırıldıktan sonra aşağıdaki CSV dosyaları oluşturulur:

1. **`gtm_tags_analysis.csv`** - Etiketler analizi
   - Sıra, ad, tip, boyut (byte), parametre sayısı, tetikleyici sayısı, tag ID

2. **`gtm_triggers_analysis.csv`** - Tetikleyiciler analizi
   - Sıra, ad, tip, boyut (byte), koşul sayısı, trigger ID

3. **`gtm_variables_analysis.csv`** - Değişkenler analizi
   - Sıra, ad, tip, boyut (byte), parametre sayısı, variable ID

## 📈 Örnek Çıktı

```
==========================================
GTM KONTEYNER DETAYLI ANALİZİ
Konteyner Adı: My Website
Konteyner ID: GTM-XXXXXXX
Account ID: 123456789
==========================================

📋 TÜM ETİKETLER (TAGS) - Toplam: 25
#    Etiket Adı                               Tip            Boyut    Param  Tetik
1    Google Analytics - Universal Analytics   ua             2,341    15     3
2    Facebook Pixel                          sp             1,892    8      2
...

🏆 EN BÜYÜK 10 ETİKET
1. Google Analytics - Universal Analytics (2,341 byte)
2. Facebook Pixel (1,892 byte)
...
```

## 🎯 Ne İçin Kullanılır?

- GTM konteynerinizin performans optimizasyonu
- En büyük etiketleri tespit etme
- Gereksiz veya optimize edilebilir bileşenleri bulma
- Konteyner boyutunu küçültme stratejileri geliştirme
- GTM konteyner içeriğini anlama ve dokümantasyon

## 🔍 Dosya Formatı

Script, GTM'den export edilen JSON dosyasını bekler. Dosya şu yapıda olmalıdır:
```json
{
  "containerVersion": {
    "tag": [...],
    "trigger": [...], 
    "variable": [...],
    "container": {...}
  }
}
```

## ⚠️ Notlar

- JSON dosya adının `gtm-workspace.json` olması gerekiyor
- Script UTF-8 kodlamasını kullanır
- Boyutlar byte cinsinden hesaplanır
- Tüm listeler boyuta göre büyükten küçüğe sıralanır

## 🐛 Hata Çözümü

**"Dosya bulunamadı" hatası:**
- `gtm-workspace.json` dosyasının script ile aynı klasörde olduğundan emin olun

**"JSON geçersiz" hatası:**
- GTM'den doğru şekilde export edilmiş JSON dosyası kullandığınızdan emin olun

**"Beklenmeyen hata" hatası:**
- JSON dosyasının GTM konteyner formatında olduğunu kontrol edin 