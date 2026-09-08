---
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
   - Toplam soru sayısının konu ağırlıklarına göre dengeli olup olmadığını kontrol et.
   - Resmi notta yer alan ancak havuzda sorusu bulunmayan veya yetersiz olan "garanti sınav konularını" saptayarak hedef soru sayısını belirle (Platform standardı: Modül başına 210 – 230 soru, toplam 860 soru).

---

## Aşama 2: Psikometrik ve Hukuki Kalite Denetimi

Mevcut soru havuzunu adayın ezbere ya da şık kusurlarından doğru cevabı tahmin etmesini önlemek amacıyla 4 temel filtreyle tara:

1. **Aşırı Uzun Şık Sapması (Length Outlier Bias):**
   - Kural: Doğru cevap, yanlış şıkların ortalama uzunluğundan **1.8 kattan daha uzun olmamalıdır**.
   - Doğru şıkkın tek başına uzun bir paragraf olduğu sorular tespit edilmeli; yanlış seçenekler de eşit uzunlukta, ikna edici ve güçlü alternatiflerle genişletilmelidir.
   - Doğru cevabın strictly en uzun olduğu soru oranı havuz genelinde **%40 - %55 bandını aşmamalıdır**.
2. **Parantez İçi İpuçları (Giveaway Parentheticals):**
   - Kural: Yalnızca doğru şıkta parantez içinde terim tanımı, Türkçe karşılığı veya ipucu bulunması kesinlikle yasaktır.
   - Tüm seçenekler simetrik formatta yapılandırılmalıdır.
3. **Mülga / Hatalı Mevzuat Hükümleri:**
   - Yürürlükten kalkmış eski tebliğ hükümleri ve parasal tutarlar derhal güncellenmelidir.
4. **Zayıf ve Gayriciddi Çeldiricilerin Güçlendirilmesi:**
   - Sınav ciddiyetiyle bağdaşmayan seçenekler yerine mevzuata uygun profesyonel finansal alternatifler yazılmalıdır.

---

## Aşama 3: Soru Havuzu Genişletme ve Dengeleme Standartları

Yeni eklenecek sorular aşağıdaki standartlara harfiyen uymalıdır:

1. **Dengeli Cevap Anahtarı:**
   - Eklenen soru paketinin cevap anahtarı A, B, C, D, E arasında tam olarak eşit dağıtılmalıdır (Örn: 50 soru için 10 A, 10 B, 10 C, 10 D, 10 E).
2. **Rastgele Karıştırma (Random Shuffle) Uyumu:**
   - Şıklarda asla "Yukarıdakilerin hepsi", "Hiçbiri", "A ve B", "C ve D" gibi konumsal referanslar bulunmamalıdır.
   - Çözüm açıklamaları "A şıkkı doğrudur" diye başlamamalı; yasal gerekçeyi ve doğru kuralı doğrudan açıklamalıdır.
3. **Senkronizasyon:**
   - Yapılan her soru eklemesi ve güncellemesi `src/data/all_questions.json` ve `src/data/questions_master.json` dosyalarına aynı anda ve birebir eşit yazılmalıdır.

---

## Aşama 4: Kritik Hap Bilgiler (`CheatSheetPage.tsx`) Genişletmesi

Modüle özgü sınav öncesi 10 dakikalık hızlı tekrar havuzu 4 temel kategoride genişletilmeli ve modül başına en az **35-42 hap bilgi** sağlanmalıdır:

1. **Süreler (`DURATIONS`):** Bildirim, itiraz, dava, tescil, saklama ve işlem süreleri.
2. **Oranlar ve Eşikler (`RATIOS`):** Yasal nisaplar, parasal yeniden değerleme eşikleri, özkaynak katsayıları ve limitler.
3. **Kavram Karşılaştırmaları (`COMPARISONS`):** Sınavda birbirine karıştırılan ikili müesseseler (Örn: MKT Açık Teklif vs Yenileme, Segregated vs Omnibus Saklama).
4. **Sınav Tuzakları (`TRAPS`):** Adayların en çok yanıldığı "doğru bilinen yanlışlar" (Myth vs Reality formatı).

---

## Aşama 5: Bütünlük Testleri ve Versiyonlama

Her modül tamamlandığında aşağıdaki adımlar eksiksiz uygulanır:

1. **`python scripts/verify_all.py`:**
   - Modül soru sayısı assertion'ı doğrulanır (Toplam 860: 1001: 210, 1003: 210, 1005: 230, 1012: 210).
   - 0 kopya soru metni, 0 eksik id, tam 5 şık (A-E) ve geçerli cevap anahtarları teyit edilir.
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
  - *2026 Kurumsal Profesyonel Müşteri Eşikleri:* Aktif toplamı 500 Milyon TL, Yıllık net hasılat 1 Milyar TL, Özsermaye 50 Milyon TL (en az ikisini sağlayanlar).
  - *Uygunluk (Appropriateness) vs Yerindelik (Suitability) Testi:* Portföy yöneticiliği ve yatırım danışmanlığında Yerindelik Testi zorunludur.
- **Bölüm 2: III-39.1 Yatırım Kuruluşlarının Kuruluş ve Faaliyet Esasları:**
  - *2026 Asgari Özsermaye Şartları:* Dar Yetkili: 45.000.000 TL, Kısmi Yetkili: 190.000.000 TL, Geniş Yetkili: 380.000.000 TL, Yeni Kuruluş Sermayesi: 440.000.000 TL.
  - *Şube vs İrtibat Bürosu (Madde 44):* İrtibat büroları sadece tanıtım ve müşteri emirlerini iletme yapabilir. Müşteri adına para/menkul kıymet teslim alamaz, hesap açamaz, sözleşme imzalayamaz.
- **Bölüm 3: III-45.1 Belge ve Kayıt Düzeni:**
  - *Saklama Süresi:* Fiziki ve elektronik belgeler, telefon ses kayıtları, müşteri emir formları 5 yıl saklanır.
- **Bölüm 4: Seri: V, No: 65 Kredili Alım, Açığa Satış ve Ödünç İşlemleri:**
  - *Özkaynak Oranları:* Başlangıç özkaynak oranı asgari %50, Sürdürme özkaynak oranı asgari %35. Tamamlama süresi 2 iş günü.
- **Bölüm 5: III-35/A.2 Kitle Fonlaması Tebliği:**
  - *Türleri:* Pay ve Borca Dayalı Kitle Fonlaması. Sermaye: 9.000.000 TL. Kampanya süresi max 60 gün.

### Modül 1012: Takas, Saklama ve Operasyon İşlemleri (210 Soru, %98.5+ Kapsayıcılık - Tamamlandı)
- **Bölüm 1: Takasbank Hukuki Statüsü ve Merkezi Karşı Taraf (MKT) Müessesesi:**
  - *Hukuki Statü:* 6362 sayılı Kanun m. 77 kapsamında Merkezi Takas Kuruluşu ve 5411 sayılı Kanun kapsamında Özel Statülü Kalkınma ve Yatırım Bankası.
  - *MKT Hizmeti Verdiği Piyasalar:* Pay Piyasası, Borçlanma Araçları Piyasası (BAP), VİOP, Takasbank Para Piyasası (TPP), SWAP Piyasası.
  - *MKT Olmadığı Piyasalar:* Kıymetli Madenler ve Taşlar Piyasası (KMTP), Dış Borçlanma Araçları Piyasası.
  - *Takas Üyeliği:* Doğrudan Takas Üyesi (kendi ve müşterileri) vs Genel Takas Üyesi (kendi, müşterileri ve üye olmayan kuruluşlar).
  - *Sermaye Güncellemesi:* MKT özkaynak şartı her yılın 4. ayının ilk iş günü YDO oranında güncellenir; sermayesi eksilen üye 1 ay içinde tamamlar.
- **Bölüm 2: MKK (Merkezi Kayıt Kuruluşu) ve Doğrudan Hak Sahipliği:**
  - *Hukuki Nitelik ve Fiili Ortaklık:* Özel hukuk tüzel kişisi anonim şirket (100 Milyon TL sermaye). Fiili ortaklık: Takasbank %64.9, Borsa İstanbul %30.1, TSPB %5.0. Esas sözleşme tavanları: Takasbank max %75, Borsa max %50, TSPB max %10, diğerleri max %5.
  - *Doğrudan Hak Sahipliği (Direct Holding):* Kıymetler aracı kurum havuzunda değil, MKK nezdinde hak sahipleri (TCKN/VKN) bazında alt hesaplarda kayden izlenir.
  - *Kaydileştirilmeyen Paylar (Madde 13):* Re'sen kaydileşir; mali haklar YTM özel hesabında bloke edilir, yönetim hakları donar. 10 yıllık zamanaşımı AYM kararıyla kaldırılmıştır (hak sahipliği mülkiyet hakkı gereği korunur).
  - *Yatırımcı Blokajı:* Yatırımcı e-YATIRIMCI üzerinden kendi paylarına blokaj koyar; kurum kaldıramaz.
- **Bölüm 3: Teminat ve Risk Yönetimi (BISTECH Marjin & NAT):**
  - *Teminat Türleri:* Başlangıç Teminatı, Değişim Teminatı (Mark-to-Market günlük kar/zarar farkı), Fiziki Teslimat Teminatı, Olağanüstü/Ek Teminat.
  - *BISTECH Risk Algoritması:* Çoklu varlık portföy marjin yöntemi. Risk faktörleri: Fiyat değişim aralığı, volatilite aralığı, spread indirimi.
  - *Teminat Kabul Esasları:* Nakit TL, döviz (USD, EUR), BIST 30 payları, DİBS, Eurobond, Altın. Nakit dışı teminatlarda saç tıraşı (haircut / iskonto) uygulanır.
  - *Asgari Nakit TL Oranı:* BAP ve Pay Piyasasında nakit TL zorunluluğu (%10 - %30), VİOP'ta asgari %50 nakit TL kuralı.
  - *Teminat Değerleme Katsayısı:* Katsayı = 1 - (Piyasa Riski + Likidite Riski + Kredi Riski).
- **Bölüm 4: Temerrüt Yönetimi ve Garanti Fonu (Madde 36 Şelale Sırası):**
  - *Garanti Fonu Sabit Katkı Payları:* Pay Piyasası: 200.000 TL, BAP: 700.000 TL, VİOP: 3.575.000 TL, SWAP: 2.875.000 TL, OTC: 500.000 TL.
  - *Değişken Katkı:* En büyük 1. üyenin veya 2. ve 3. üyenin toplam temerrüt riskinden büyük olanı baz alınarak stres testleriyle hesaplanır.
  - *Temerrüt Şelalesi Sırası (Madde 36):*
    1. Temerrüde düşen üyenin işlem teminatları
    2. Temerrüde düşen üyenin Garanti Fonu katkı payı
    3. Takasbank'ın taahhüt ettiği MKT Özkaynak Payı (Sermaye Katkısı)
    4. Temerrüde düşmeyen diğer üyelerin Garanti Fonu katkı payları (müteselsil oranında)
    5. Takasbank MKT Kalan Özkaynak Payı
    6. Garanti Fonu Ek Katkı Payları (üyelerden 1 katına kadar)
    7. Karşılıklı Tahsis / Kalan Zararın Üyelere Dağıtımı (Kayıp Paylaşımı)
- **Bölüm 5: Piyasalar Operasyon Saatleri ve Takas Döngüleri:**
  - *Pay Piyasası:* T+2 DvP takası. Takas borcu kapama son saati: **16:45**. Teminat tamamlama çağrısı son saati: **15:00**.
  - *BAP (Borçlanma Araçları Piyasası):* T+0 (aynı gün) veya T+1/T+2. Takas borcu kapama: 16:45; Ön temerrüt aralığı: 16:46 - 17:00 (0.25 gecikme katsayısı).
  - *VİOP:* Nakit uzlaşma T+1; fiziki teslimat T+2.
  - *Ödünç Pay Piyasası (ÖPP):* Takasbank güvencesinde; teminat tamamlama 2 saat; temerrüt halinde T+3 saat 11:00'e kadar açık piyasadan ikame alımı.
- **Bölüm 6: Portföy Saklama ve Genel Saklama Esasları:**
  - *Portföy Saklama:* Yatırım fonu ve emeklilik fonu varlıkları bağımsız portföy saklayıcısı nezdinde saklanır; portföy yöneticisi ile saklayıcı aynı tüzel kişilik olamaz. Saklayıcı fesih ihbar süresi en az **90 gün**dür.
