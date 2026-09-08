import os

skill_content = """---
name: spl-module-curator
description: >-
  SPK SPL Lisanslama Sınavı modülleri (1001, 1003, 1005, 1012) için soru havuzu denetimi,
  eksik müfredat analizi, psikometrik kalite iyileştirme (şık uzunluk dengesi, parantez ipuçları temizliği),
  Kritik Hap Bilgiler (CheatSheet) genişletmesi, 2026 mevzuat güncellemeleri ve %98+ sınav kapsayıcılığı sağlama protokolü.
---

# SPL Sınav Modülü Kapsam ve Kalite Kürasyon Protokolü

Bu yetenek (skill), SPK SPL Düzey 1 ve diğer lisanslama sınavlarına hazırlık platformundaki modüllerin (**1001**, **1003**, **1005**, **1012**) en güncel resmi SPL ders notlarına göre **%98+ sınav kapsayıcılığına** ve **üstün psikometrik kaliteye** ulaştırılması için izlenecek 5 aşamalı standart işletim protokolünü (SOP) ve modül bilgi bankasını tanımlar.

---

## Aşama 1: Resmi Müfredat Taraması ve Konu Boşluğu Analizi (OCR & Delta)

1. **Resmi Ders Notunu İnceleme:**
   - En güncel resmi SPL Çalışma Notunun (örneğin Temmuz 2026 notu) tüm bölümlerini ve alt başlıklarını tara.
   - Son 1-2 yılda yayımlanan güncel SPK İlke Kararlarını (i-SPK), tebliğ değişikliklerini ve yıllık Yeniden Değerleme katsayısı ile güncellenen parasal sınırları listele.
2. **Konu Dağılımı ve Eksiklik Tespiti:**
   - Mevcut soru havuzunu resmi konu başlıklarına göre sınıflandır.
   - Toplam soru sayısının konu ağırlıklarına göre dengeli olup olmadığını kontrol et (örneğin Belge ve Kayıt Düzeni %1'in altındaysa veya DİBS %2'de kalmışsa eksikliği belirle).
   - Resmi notta yer alan ancak havuzda sorusu bulunmayan veya yetersiz olan "garanti sınav konularını" saptayarak hedef soru sayısını belirle (Örn: Modül başına 210 – 230 soru).

---

## Aşama 2: Psikometrik ve Hukuki Kalite Denetimi

Mevcut soru havuzunu adayın ezbere ya da şık kusurlarından doğru cevabı tahmin etmesini önlemek amacıyla 4 temel filtreyle tara:

1. **Aşırı Uzun Şık Sapması (Length Outlier Bias):**
   - Kural: Doğru cevap, yanlış şıkların ortalama uzunluğundan **1.8 kattan daha uzun olmamalıdır**.
   - Doğru şıkkın tek başına uzun bir paragraf olduğu sorular tespit edilmeli; yanlış seçenekler de eşit uzunlukta, ikna edici ve güçlü alternatiflerle genişletilmelidir.
   - Doğru cevabın strictly en uzun olduğu soru oranı havuz genelinde **%40 - %50 bandını aşmamalıdır**.
2. **Parantez İçi İpuçları (Giveaway Parentheticals):**
   - Kural: Yalnızca doğru şıkta parantez içinde terim tanımı, Türkçe karşılığı veya ipucu bulunması kesinlikle yasaktır.
   - Örnek: "Murabaha (Yönetim sözleşmesine / alım satıma dayalı)" şeklindeki tek taraflı parantezler temizlenmeli, tüm seçenekler tek kelime veya eşit açıklamalı yapılmalıdır.
3. **Mülga / Hatalı Mevzuat Hükümleri:**
   - Yürürlükten kalkmış eski tebliğ hükümleri ve parasal tutarlar derhal güncellenmelidir.
   - Örnekler:
     - Dar/Kısmi/Geniş Yetkili Aracı Kurum asgari özsermayeleri 2026 güncel tutarları (45M, 190M, 380M TL; kuruluş 440M TL).
     - Kurumsal Profesyonel Müşteri kriterleri (Aktif 500M, Hasılat 1 Mr, Özsermaye 50M TL).
     - BASK toplantı/karar nisabı güncel 2/3 kuralı.
     - Ortaklıktan çıkarma ve satma hakkı kuralı (%98).
     - İrtibat bürolarının müşteri emirlerini iletme yetkisi (Tebliğ III-39.1 m. 44).
4. **Zayıf ve Gayriciddi Çeldiricilerin Güçlendirilmesi:**
   - Sınav ciddiyetiyle bağdaşmayan seçenekler ("şirket batarsa", "müdür keyfi belirler", "100 yaşında olması", "akrabaların adıyla gizlice yürütülür") yerine mevzuata uygun profesyonel finansal alternatifler yazılmalıdır.

---

## Aşama 3: Soru Havuzu Genişletme ve Dengeleme Standartları

Yeni eklenecek sorular aşağıdaki standartlara harfiyen uymalıdır:

1. **Dengeli Cevap Anahtarı:**
   - Eklenen soru paketinin cevap anahtarı A, B, C, D, E arasında tam olarak eşit dağıtılmalıdır (Örn: 10 soru eklenecekse 2 A, 2 B, 2 C, 2 D, 2 E; 20 soru eklenecekse 4 A, 4 B, 4 C, 4 D, 4 E).
2. **Rastgele Karıştırma (Random Shuffle) Uyumu:**
   - Şıklarda asla "Yukarıdakilerin hepsi", "Hiçbiri", "A ve B", "C ve D" gibi konumsal referanslar bulunmamalıdır.
   - Çözüm açıklamaları "A şıkkı doğrudur" diye başlamamalı; yasal gerekçeyi ve doğru kuralı doğrudan açıklamalıdır.
3. **Senkronizasyon:**
   - Yapılan her soru eklemesi ve güncellemesi `src/data/all_questions.json` ve `src/data/questions_master.json` dosyalarına aynı anda ve birebir eşit yazılmalıdır.

---

## Aşama 4: Kritik Hap Bilgiler (`CheatSheetPage.tsx`) Genişletmesi

Modüle özgü sınav öncesi 10 dakikalık hızlı tekrar havuzu 4 temel kategoride genişletilmeli ve modül başına en az **35-40 hap bilgi** sağlanmalıdır:

1. **Süreler (`DURATIONS`):** Bildirim, itiraz, dava, tescil, saklama ve işlem süreleri (Örn: 30 gün itiraz, 2 iş günü tamamlama, 5 yıl saklama, 60 gün kampanya).
2. **Oranlar ve Eşikler (`RATIOS`):** Yasal nisaplar, parasal yeniden değerleme eşikleri, özkaynak katsayıları ve limitler (Örn: %50 başlangıç, %35 sürdürme, 45M/190M/380M TL).
3. **Kavram Karşılaştırmaları (`COMPARISONS`):** Sınavda birbirine karıştırılan ikili müesseseler (Örn: İrtibat Bürosu vs Şube, Uygunluk vs Yerindelik Testi, Kredili İşlem vs Açığa Satış).
4. **Sınav Tuzakları (`TRAPS`):** Adayların en çok yanıldığı "doğru bilinen yanlışlar" (Myth vs Reality formatı).

---

## Aşama 5: Bütünlük Testleri ve Versiyonlama

Her modül tamamlandığında aşağıdaki adımlar eksiksiz uygulanır:

1. **`python scripts/verify_all.py`:**
   - Modül soru sayısı assertion'ı güncellenir.
   - 0 kopya soru metni, 0 eksik id, tam 5 şık (A-E) ve geçerli cevap anahtarları doğrulanır.
2. **`npm run build`:**
   - TypeScript derlemesi (`tsc`) ve Vite derlemesi 0 hata ile tamamlanmalıdır.
3. **Dokümantasyon ve Git:**
   - `walkthrough.md` güncellenir.
   - Git reposunda değişiklikler düzenli olarak commit edilir.

---

# Modül Bazlı Bilgi Bankası ve Sınav Eşikleri (2026 Mevzuatı)

### Modül 1001: Dar Kapsamlı Sermaye Piyasası Mevzuatı ve Meslek Kuralları (210 Soru, %98+ Kapsayıcılık)
- **Kapsam:** 6362 sayılı Sermaye Piyasası Kanunu, Kurul Teşkilatı, İdari ve Cezai Yaptırımlar, Piyasa Dolandırıcılığı (Manipülasyon), Bilgi Suiistimali (İçeriden Öğrenenlerin Ticareti), Örtülü Kazanç Aktarımı, Kamuyu Aydınlatma (KAP, Özel Durumlar), Yatırımcı Tazmin Merkezi (YTM), TSPB Meslek Kuralları.
- **Kritik Süreler:** İdari para cezalarında dava açma süresi (30 gün İdare Mahkemesi), İhraç belgesi onay süresi (10-20 iş günü), Özel durum açıklamaları (derhal, en geç ertesi iş günü seans öncesi), YTM zamanaşımı (10 yıl).

### Modül 1003: Sermaye Piyasası Araçları 1 (210 Soru, %98+ Kapsayıcılık)
- **Kapsam:** Paylar (Adi, İmtiyazlı, Bedelli, Bedelsiz), Borçlanma Araçları (Tahvil, Finansman Bonosu, DİBS, Gelir Ortaklığı Senedi), Kira Sertifikaları (Sukuk - Mülkiyete Dayalı/İcara, Yönetim Sözleşmesine Dayalı, Alım-Satıma Dayalı/Murabaha, Ortaklığa Dayalı/Mudaraba-Müşareke, Eser Sözleşmesine Dayalı/İstisna), Menkul Kıymetleştirme (Varlığa Dayalı Menkul Kıymetler - VDMK, İpotek Teminatlı Menkul Kıymetler - İTMK), Varantlar ve Yatırım Kuruluşu Sertifikaları, Yatırım Fonları ve Yatırım Ortaklıkları (BYF, GSYF, GEYF, Menkul Kıymet Yatırım Ortaklığı).
- **Kritik Eşikler:** BASK toplantı ve karar nisabı (2/3 kuralı), Ortaklıktan çıkarma ve satma hakkı (%98 oy hakkı eşiği), Sukuk ihraç limitleri ve fon kullanıcısı taahhütleri.

### Modül 1005: Yatırım Kuruluşları (230 Soru, %98.5+ Kapsayıcılık)
- **Bölüm 1: III-37.1 Yatırım Hizmetleri ve Faaliyetleri ile Yan Hizmetler:**
  - *10 Temel Yatırım Hizmeti:* Emir iletimi, işlem aracılığı, portföy aracılığı, saklama (genel/sınırlı), portföy yöneticiliği, yatırım danışmanlığı, halka arza aracılık (en iyi gayret / yüklenim).
  - *Müşteri Sınıflandırması:* Genel Müşteri vs Profesyonel Müşteri.
  - *2026 Kurumsal Profesyonel Müşteri Eşikleri:* Aktif toplamı 500 Milyon TL, Yıllık net hasılat 1 Milyar TL, Özsermaye 50 Milyon TL (en az ikisini sağlayanlar).
  - *Uygunluk (Appropriateness) vs Yerindelik (Suitability) Testi:* Portföy yöneticiliği ve yatırım danışmanlığında Yerindelik Testi zorunludur; diğer işlemlerde genel müşteriye Uygunluk Testi yapılır. Profesyonel müşteriye uygunluk testi yapılmaz; yerindelik testinde mali güç ve yatırım amacı incelenir ancak bilgi/tecrübe var kabul edilir.
- **Bölüm 2: III-39.1 Yatırım Kuruluşlarının Kuruluş ve Faaliyet Esasları:**
  - *2026 Asgari Özsermaye Şartları:* Dar Yetkili: 45.000.000 TL, Kısmi Yetkili: 190.000.000 TL, Geniş Yetkili: 380.000.000 TL, Yeni Kuruluş Sermayesi: 440.000.000 TL.
  - *Şube vs İrtibat Bürosu (Madde 44):* İrtibat büroları sadece tanıtım ve müşteri emirlerini merkeze iletme yapabilir. Müşteri adına para/menkul kıymet teslim alamaz, hesap açamaz, sözleşme imzalayamaz.
  - *Teşkilat Yapısı:* İç Kontrol, Risk Yönetimi ve Teftiş Kurulu bağımsız birimlerdir; yöneticileri ve personeli doğrudan Yönetim Kurulu'na bağlıdır.
- **Bölüm 3: III-45.1 Belge ve Kayıt Düzeni:**
  - *Ekstre ve İtiraz:* Hesap ekstreleri en az ayda bir iletilir. 30 gün içinde itiraz edilmeyen ekstre kesinleşir; ancak bu kural aracı kurumun sahtecilik ve kasıtlı işlemlerine karşı itiraz hakkını düşürmez (hükümsüzlük ilkesi).
  - *Saklama Süresi:* Fiziki ve elektronik belgeler, telefon ses kayıtları, müşteri emir formları 5 yıl saklanır. Müşteri şikayet defteri ve kayıtları 5 yıl saklanır.
  - *Fiziki Mutabakat:* Müşteri varlıklarının fiziki mevcudu ile MKK/Takasbank kayıtları her yıl sonu itibarıyla ve en geç 3 iş günü içinde mutabakata bağlanır.
- **Bölüm 4: Seri: V, No: 65 Kredili Alım, Açığa Satış ve Ödünç İşlemleri:**
  - *Özkaynak Oranları:* Başlangıç özkaynak oranı asgari %50, Sürdürme özkaynak oranı asgari %35.
  - *Özkaynak Tamamlama (Margin Call):* Oran %35'in altına indiğinde aracı kurum derhal çağrıda bulunur; müşteri bildirimi izleyen 2 iş günü içinde oranını %50'ye tamamlamak zorundadır.
  - *Re'sen Satım:* 2 iş günü içinde tamamlanmazsa aracı kurum müşterinin onayına ihtiyaç duymaksızın re'sen kıymet satarak oranı %50'ye çıkarır.
  - *Kredili İşlem Yasakları:* Kredili işlem hesabında teminat olarak aracı kurumun kendi hissesi kabul edilemez; kredili işlemle alınan hisse başka bir krediye teminat olamaz.
- **Bölüm 5: III-35/A.2 Kitle Fonlaması Tebliği:**
  - *Türleri:* Pay ve Borca Dayalı Kitle Fonlaması (Gayrimenkul ve bağış hariçtir).
  - *Platform Şartları:* SPK listesine alınma zorunluluğu, asgari sermaye 9.000.000 TL, %5 ve üzeri ortaklarda temiz adli sicil.
  - *Kampanya Kuralları:* Maksimum 60 gün; 12 aylık dönemde en fazla 2 kampanya.
  - *Yatırım Limitleri:* Nitelikli olmayan yatırımcılar için bir yılda yıllık net gelirinin en fazla %10'u veya maksimum 600.000 TL.
  - *Fon Denetimi:* Toplanan fonun kullanım amacına uygunluğu bağımsız denetim veya YMM raporu ile teyit edilir.
- **Bölüm 6: III-42.1 Uzaktan Kimlik Tespiti & TSPB Promosyon Esasları:**
  - *Uzaktan Kimlik:* NFC çip okuma, canlılık testi, 28.02.2026 itibarıyla Yapay Zeka destekli biyometri karşılaştırması zorunluluğu.
  - *Çalışma Ortamı:* Müşteri temsilcisi yabancıların giremediği güvenli/izole odada görüşme yapar; görüşme kayıtları en az 10 yıl saklanır.
  - *Promosyon Yönergesi:* Promosyon bütçesi yatırım kuruluşunun asgari özsermayesinin %1'ini aşamaz; çekiliş ve promosyon objektif/ayrımcılıktan uzak olmalıdır.

### Modül 1012: Takas, Saklama ve Operasyon İşlemleri (Hedef: 210 Soru, %98+ Kapsayıcılık Hazırlığı)
- **Kapsam:** Takasbank (Merkezi Takas Kuruluşu ve Banka statüsü), Merkezi Kayıt Kuruluşu (MKK - Doğrudan Saklama ve Hak Sahipliği Bazında Kayden İzleme), Merkezi Karşı Taraf (MKT) Müessesesi ve Risk Yönetimi, Garanti Fonu ve Temerrüt Yönetimi, Pay ve Borçlanma Araçları Takas Süreçleri (T+2, DVP - Teslim Karşılığı Ödeme), Hak Kullanım Operasyonları (Temettü, Bedelli/Bedelsiz Pay Dağıtımı, Genel Kurul Blokajı/Bildirimi), Ödünç Pay Piyasası (ÖPP) Takas ve Teminat Mekanizması, Yurt Dışı Menkul Kıymet Saklama ve Muhabirlik İlişkileri.
"""

for target in [".agent/skills/spl-module-curator/SKILL.md", ".agents/skills/spl-module-curator/SKILL.md"]:
    os.makedirs(os.path.dirname(target), exist_ok=True)
    with open(target, "w", encoding="utf-8") as f:
        f.write(skill_content.strip() + "\n")
    print(f"Successfully written to: {target}")
