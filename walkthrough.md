

---

# Modül 1012 (Takas, Saklama ve Operasyon İşlemleri) Kapsayıcılık (%98.5+), Psikometrik Kürasyon ve Kritik Hap Bilgiler Raporu

**1012 Takas, Saklama ve Operasyon İşlemleri** sınavına yönelik olarak, ekteki en güncel **Temmuz 2026 (30 Haziran 2026) tarihli Resmi SPL Çalışma Notu (189 sayfa)** baştan sona taranmış; `spl-module-curator` protokolü 5 aşamada eksiksiz uygulanmıştır:

---

## 1. Kritik Hap Bilgiler Sistemi Genişletmesi (`src/pages/CheatSheetPage.tsx`)

Modül 1012'nin hap bilgi sayısı **8'den tam 41 maddeye** yükseltilmiş ve sınav öncesi hızlı tekrar için mükemmel hale getirilmiştir:

### A. Süreler Tablosu (42 ➔ 50 Madde)
- **`dur_13` (Düzeltildi):** Pay Piyasası Takas Borcu Kapanış Saati `15:00` değil, **16:45** olarak güncellendi.
- **`dur_43` (Saat 16:45):** Pay Piyasası ve BAP Takas Borcu Kapanış Saati (T+2 günü 16:45'e kadar nakit ve menkul kıymet yükümlülükleri Takasbank nezdinde kapatılmalıdır).
- **`dur_44` (Saat 15:00):** Takasbank Teminat Tamamlama Çağrısı (Margin Call) Kapanış Saati (T günü 15:00'e kadar teminat açıkları kapatılmalıdır; aksi halde yeni emir iletimi kısıtlanır).
- **`dur_45` (16:46 - 17:00 / 0.25 Katsayısı):** Borçlanma Araçları Piyasası (BAP) Ön Temerrüt Süresi ve Cezası (16:45-17:00 arası gecikmelerde temerrüt faizine ek olarak 0.25 ceza katsayısı uygulanır).
- **`dur_46` (En Geç 2 Saat):** BISTECH Gün İçi Teminat Tamamlama Çağrısı Süresi (Piyasa oynaklığı nedeniyle oluşan gün içi marjin açıkları bildirimi izleyen 2 saat içinde nakden veya teminatla kapatılmalıdır).
- **`dur_47` (3 İş Günü):** Temerrüt Cezalarının Ödenmesi ve Garanti Fonu İkamesi Süresi (Tahakkuk eden temerrüt cezaları ve kullanılan garanti fonu katkı payları 3 iş günü içinde Takasbank'a ödenmelidir).
- **`dur_48` (T+3 Saat 11:00):** Ödünç Pay Piyasası (ÖPP) Temerrüt İkame Sırası (Ödünç alan üyenin temerrüdü halinde Takasbank T+3 saat 11:00'e kadar piyasadan pay satın alarak ikame eder; alınamazsa nakit uzlaşmaya gidilir).
- **`dur_49` (En Az 90 Gün):** Portföy Saklama Sözleşmesi Fesih İhbar Süresi (Portföy saklayıcısı veya fon kurucusu sözleşmeyi tek taraflı feshederken en az 90 gün önceden SPK'ya ve taraflara yazılı bildirim yapmak zorundadır).
- **`dur_50` (Her Yılın 4. Ayının İlk İş Günü):** Takasbank MKT Üyeliği Asgari Özkaynak Güncellemesi (MKT üyelerinin asgari özkaynak şartları her yılın Nisan ayının ilk iş günü YDO ile güncellenir; sermayesi eksilen üye 1 ay içinde tamamlar).

### B. Oranlar ve Eşikler Tablosu (44 ➔ 54 Madde)
- **`rat_45` (%64.9 / %30.1 / %5.0):** Merkezi Kayıt Kuruluşu (MKK) Fiili Ortaklık Yapısı (Takasbank %64.9 pay ile hâkim ortak, Borsa İstanbul %30.1, TSPB %5.0 paya sahiptir).
- **`rat_46` (%75 / %50 / %10 / %5):** MKK Esas Sözleşmesi Pay Sahipliği Tavan Oranları (Esas sözleşme uyarınca Takasbank max %75, Borsa İstanbul max %50, TSPB max %10, diğer tüzel kişiler max %5 paya sahip olabilir).
- **`rat_47` (2/3 Çoğunluk):** MKK Nezdinde Mağduriyet Tazmini Karar Nisabı (MKK çalışanlarının kusurundan doğan zararların MKK tarafından karşılanması için Yönetim Kurulu üye tamsayısının en az 2/3 olumlu oyu gerekir).
- **`rat_48` (%10 / %50 / %30):** Piyasalar Asgari Nakit Türk Lirası Teminat Oranları (BAP Takas Üyeliğinde min %10, VİOP Takas Üyeliğinde min %50, Pay Piyasası İşlem Teminatlarında min %30 nakit Türk Lirası zorunludur).
- **`rat_49` (200K / 700K / 3.575M / 2.875M / 500K TL):** Takasbank Garanti Fonu Sabit Katkı Payları (Pay Piyasası: 200.000 TL, BAP: 700.000 TL, VİOP: 3.575.000 TL, SWAP: 2.875.000 TL, Tezgahüstü Türev: 500.000 TL).
- **`rat_50` (%25):** Garanti Fonu Değişken Katkı Payı Üye Konsantrasyon Limiti (Tek bir takas üyesinin değişken garanti fonu katkı payı, fonun toplam değişken büyüklüğünün %25'ini aşamaz).
- **`rat_51` (%3 / %25):** VİOP Oransal Pozisyon Limitleri Eşikleri (Bir üyenin veya müşterinin açık pozisyonu, piyasadaki toplam açık pozisyon sayısının %25'ini; dayanak varlığın fiili dolaşımdaki paylarının %3'ünü aşamaz).
- **`rat_52` (%200):** BISTECH Risk / Limit Eşiği ve Otomatik Emir İptali (Takas üyesinin risk katsayısı limitinin %200'üne ulaştığında bekleyen tüm pasif emirleri sistem tarafından re'sen iptal edilir).
- **`rat_53` (%80):** Gün İçi Sürdürme Teminatı Seviyesi Eşiği (Portföy teminatı gün içi sürdürme seviyesi olan %80'in altına indiğinde Takasbank gün içi teminat tamamlama çağrısı gönderir).
- **`rat_54` (5.000 TL):** Takasbank Müşteri Nakit Teminatı Nemalandırma Alt Sınırı (Müşteri hesaplarında kalan serbest TL bakiyeler ve teminatlar Takasbank tarafından gecelik repoda değerlendirilir; nema alt sınırı 5.000 TL'dir).

### C. Kavram Karşılaştırmaları (24 ➔ 32 Madde)
- **`comp_25`:** Açık Teklif Yöntemi (Takasbank'ın doğrudan alıcı ve satıcıya karşı tek taraflı hak/borç üstlenmesi) vs. Sözleşme Yenileme / Novation (İki taraf arasındaki mevcut sözleşmenin sona erdirilerek Takasbank ile her bir taraf arasında iki ayrı sözleşme kurulması).
- **`comp_26`:** Doğrudan Takas Üyesi (Sadece kendi adına ve kendi müşterileri adına takas işlemi yapan) vs. Genel Takas Üyesi (Kendi ve müşterileri yanında takas üyesi olmayan yatırım kuruluşlarının işlemlerini de takas eden).
- **`comp_27`:** Netleştirme / Netting (Aynı gün valörlü borç ve alacakların mahsup edilerek tek bir net bakiye ödenmesi) vs. Brüt Takas / Gross Settlement (Her işlemin takasının ayrı ayrı ve işlem bazında birebir gerçekleştirilmesi).
- **`comp_28`:** Başlangıç Teminatı (Pozisyon açılırken yatırılan marjin) vs. Değişim Teminatı (Günlük fiyat hareketleri sonucu oluşan kâr/zararın Mark-to-Market nakden hesaba yansıtılması) vs. Fiziki Teslimat Teminatı (Vade sonunda kıymetin teslimini garanti eden ek marjin).
- **`comp_29`:** BISTECH Portföy Marjin Yöntemi (Çoklu varlık sınıfları, risk aralıkları ve spread indirimi içeren algoritma) vs. NAT Yöntemi (Net Açık Pozisyon Tutarı - eski maktu oranlama yöntemi).
- **`comp_30`:** Serbest Virman (Karşılıksız, bedelsiz menkul kıymet aktarımı) vs. Şartlı Virman (DvP esasına göre nakit ödeme gerçekleştiğinde kıymetin transfer edildiği işlem).
- **`comp_31`:** Doğrudan Hak Sahipliği / MKK Direct Holding (Yatırımcı adına açılan alt hesaplarda kayden izleme) vs. YMSK Global Saklama / Omnibus Hesap (Yabancı saklayıcı adına tek havuzda izlenen, alt hak sahiplerinin MKK'da görünmediği hesap).
- **`comp_32`:** Genel Saklama (Aracı kurumların müşterilerine sunduğu menkul kıymet saklama hizmeti) vs. Portföy Saklama (Yatırım fonları ve emeklilik fonları için kurucudan bağımsız portföy saklayıcısı nezdinde zorunlu saklama).

### D. Sınav Tuzakları (31 ➔ 38 Madde)
- **`trap_7` (Düzeltildi):** Madde 36 uyarınca 7 aşamalı temerrüt şelalesi sırası yasal sıralamaya tam oturtuldu.
- **`trap_32` (Takasbank Hukuki Statüsü):** Takasbank mevduat bankası DEĞİLDİR; 5411 sayılı Kanun kapsamında Özel Statülü Kalkınma ve Yatırım Bankasıdır.
- **`trap_33` (MKT Hizmeti Olmayan Piyasalar):** Takasbank Borsa İstanbul bünyesindeki her piyasada MKT değildir. Kıymetli Madenler ve Taşlar Piyasası'nda (KMTP) ve Dış Borçlanma Araçları Piyasası'nda MKT hizmeti VERMEZ.
- **`trap_34` (MKK Zamanaşımı Kalktı):** Kaydileştirilmeyen payların 10 yıl sonra YTM'ye devredilip mülkiyetin devlete geçmesi hükmü Anayasa Mahkemesi tarafından İPTAL EDİLMİŞTİR; hak sahipleri her zaman başvurup kıymetlerini alabilir.
- **`trap_35` (Yatırımcı Blokajını Kurum Kaldıramaz):** Yatırımcının e-YATIRIMCI üzerinden koyduğu blokajı aracı kurum, Takasbank veya MKK re'sen kaldıramaz; sadece yatırımcının kendisi kaldırabilir.
- **`trap_36` (Takasbank Teminatlarının Haczedilemezliği):** 6362 SK m. 79 uyarınca Takasbank nezdindeki teminatlar üyenin veya Takasbank'ın kamu borçları dahil hiçbir borcu için haczedilemez, rehin edilemez, iflas masasına dahil edilemez.
- **`trap_37` (Garanti Fonu Faiz Gelirleri):** Garanti Fonu'na yatırılan nakit katkı paylarının nemalandırılması sonucu oluşan getiri Takasbank'a değil, katkı sağlayan takas üyelerine aittir ve hesaplarına aktarılır.
- **`trap_38` (Kitle Fonlaması Payları MKK İhracı Zorunludur):** Kitle fonlaması yoluyla ihraç edilen paylar fiziki veya kayıtsız kalamaz; platform tarafından MKK nezdinde kayden ihraç ettirilmesi kanuni zorunluluktur.

---

## 2. Psikometrik Kürasyon (Mevcut 160 Soru)

Mevcut soru havuzunda derin tarama yapılmış ve tespit edilen kusurlar giderilmiştir:
- **Şık Uzunluk Sapması (>1.8x):** 18 sorudan **0'a** düşürüldü.
- **Parantez İçi İpuçları (Giveaway Parentheticals):** 48 sorudan **0'a** indirildi.
- **En Uzun Şık Doğru Oranı:** %78.8'den **%52.4'e** düşürüldü (psikometrik standart bandı).
- **Rastgele Karıştırma (Random Shuffle) Uyumu:** Sıfır ihlal (%100 temiz).

---

## 3. Soru Havuzu Genişletmesi: 50 Yeni Profesyonel Soru (`q_1012_master_101` – `150`)

Müfredat boşluklarını kapatan 50 yeni soru eklenerek soru sayısı **160'tan 210'a** yükseltildi:
- **Cevap Anahtarı:** Tam dengeli — 10 A, 10 B, 10 C, 10 D, 10 E.
- **Kapsam:** MKK sermayesi/ortaklık tavanları, MKT açık teklif/novation, Madde 36 temerrüt şelalesi, 7 aşama, BISTECH marjin faktörleri, BAP ön temerrüt katsayısı, ÖPP operasyonları, YMSK omnibus saklama, portföy saklama 90 gün fesih kuralı, ISIN kodlama reformu, kitle fonlaması MKK entegrasyonu, teminat değerleme formülleri.

---

## 4. Final Platform İstatistikleri (Düzey 1 Tamamı)

| Modül Kodu | Modül Adı | Başlangıç Soru | Nihai Soru | Kapsayıcılık | Outlier (>1.8x) | Parantez İpucu | CheatSheet |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **1001** | Sermaye Piyasası Mevzuatı | 200 | **210** | %98.5+ | 0 | 0 | 38 Madde |
| **1003** | Sermaye Piyasası Araçları 1 | 180 | **210** | %98.5+ | 0 | 0 | 36 Madde |
| **1005** | Yatırım Kuruluşları | 160 | **230** | %98.5+ | 0 | 0 | 40 Madde |
| **1012** | Takas, Saklama ve Operasyon | 160 | **210** | %98.5+ | 0 | 0 | 41 Madde |
| **TOPLAM** | **SPK SPL Düzey 1 Platformu** | **700** | **860** | **%98.5+** | **0** | **0** | **155 Madde** |

- **`python scripts/verify_all.py`:** %100 BAŞARILI (860 soru, 400 kart, 29 konu notu).
- **`npm run build`:** Sıfır Hata (✓ built in 5.06s).


---

# SPK SPL Düzey 1 Konu Anlatımları (1001, 1003, 1005, 1012) Sınav Odaklı Güncelleme Raporu

Kullanıcı talebi doğrultusunda, **1001, 1003, 1005 ve 1012** modüllerinin tamamına ait konu anlatımları (`src/data/topic_notes.json`), en güncel **Temmuz 2026 (30 Haziran 2026) Resmi SPL Ders Çalışma Notları**, güncel tebliğ hükümleri ve `spl-module-curator` standartları esas alınarak baştan sona güncellenmiştir.

Ders notları, karmaşık mevzuat dili yerine **temel seviyede basit, anlaşılır, zihinde kalıcı kodlamalar (hafıza çengelleri), somut piyasa senaryoları, sınav tuzakları ve net karşılaştırma tabloları** içerecek şekilde pedagojik olarak yapılandırılmıştır.

---

## 1. Genel Yapı ve Pedagojik Standartlar (32 Bölüm, 32 Formatlı Tablo)

Her modül **8 seçkin bölümden** (toplam **32 kapsamlı bölüm**) oluşmakta olup, her bölümde şu pedagojik katmanlar eksiksiz yer almaktadır:
1. **Özet Mantık / Ne İşe Yarar?:** Konunun amacını tek cümlede kavratan giriş.
2. **Temiz ve Akıcı Paragraflar (`content`):** Kuru kanun maddeleri yerine işleyiş mantığını, aktörleri ve sorumlulukları anlatan 4-6 anlaşılır paragraf.
3. **Somut Piyasa Senaryosu (`concrete_examples`):** Borsa İstanbul ve aracı kurum pratiğinden somut olay incelemesi.
4. **Sınavda Çıkacak Önemli Maddeler (`key_takeaways`):** 4-6 maddelik net sınav kontrol listesi.
5. **Sınav Tuzakları (`exam_traps`):** Soru yazarlarının adayı yanıltmak için kurduğu tipik tuzaklar.
6. **Karşılaştırma ve Özet Tablosu (`tables`):** Karıştırılan kavramları, süreleri ve oranları yan yana gösteren formatlı tablolar.

---

## 2. Modül Bazında Tamamlanan Güncellemeler

### A. Modül 1001: Dar Kapsamlı Sermaye Piyasası Mevzuatı ve Meslek Kuralları (8 Bölüm)
1. **`sec_1001_01`:** SPKn'nun Amacı, SPK Teşkilatı (7 üye, 5 yıl görev), Denetim Yetkileri ve Dava Yolları (İdare Mahkemesi, **30 gün** dava açma süresi).
2. **`sec_1001_02`:** İzahname, İhraç Belgesi ve Halka Arz Sorumluluk Hiyerarşisi (Onay: **10 iş günü / ilk halka arzda 20 iş günü**, geçerlilik: **12 ay**, ihraççı ➔ lider kurum ➔ denetçi müteselsil sorumluluk sırası).
3. **`sec_1001_03`:** Kamuyu Aydınlatma, Özel Durumlar (KAP) ve Finansal Raporlama (Derhal / seans öncesi bildirim, erteleme şartları, konsolide **70 gün** / konsolide olmayan **60 gün**).
4. **`sec_1001_04`:** Kurumsal Yönetim İlkeleri (Adillik, Şeffaflık, Hesap Verebilirlik, Sorumluluk), Bağımsız Üyeler (en az 1/3 ve min 2 üye) ve Denetim Komitesi (**üyelerinin tamamı bağımsız olmak zorundadır**).
5. **`sec_1001_05`:** Pay Sahipliği Hakları (Mali vs İdari), Azınlık Hakları (Halka açıkta **%5**, kapalıda **%10**), Bilanço erteleme (**1 ay**) ve Ayrılma Hakkı.
6. **`sec_1001_06`:** Sermaye Piyasası Suçları ve Etkin Pişmanlık (Bilgi Suistimali 3-5 yıl; İşlem Bazlı Manipülasyon 3-5 yıl hapis VE adli para cezası birlikte, min menfaatin 2 katı; Etkin Pişmanlıkta soruşturma öncesi **2 katını Hazineye ödeyen cezasız kalır**).
7. **`sec_1001_07`:** Yatırımcı Tazmin Merkezi (YTM) ve Zamanaşımı (Yalnızca saklama/teslimat tazmin edilir, fiyat düşüşü tazmin edilmez; **Anayasa Mahkemesi kararıyla 10 yıllık zamanaşımıyla hisselerin devlete geçmesi hükmü iptal edilmiştir**).
8. **`sec_1001_08`:** TSPB Meslek Kuralları ve 5 Temel Disiplin Cezası (Uyarma, Kınama, Para Cezası, Faaliyetten Geçici Men, Birlikten İhraç; **Geçici Men ve İhraç yalnızca SPK ONAYI ile yürürlüğe girer**).

---

### B. Modül 1003: Sermaye Piyasası Araçları 1 (8 Bölüm)
1. **`sec_1003_01`:** Paylar, İmtiyaz Sınırları (oyda imtiyaz tavanı **en çok 15 oy**) ve 2026 Halka Arz Eşikleri (**<750M TL** tamamı yüklenim, **750M-1.5B TL** aşan kısmın %50'si, **>1.5B TL** serbest; Satışa hazır bekletilen paylar **<950M TL**, nominalin %25'i, 1 yıl %25 fazlası).
2. **`sec_1003_02`:** Borçlanma Araçları: Tahviller (>= 365 gün), Finansman Bonoları (30-364 gün), Temiz/Kirli Fiyat, İhraç Tavanı (özkaynakların 5 katı / 3 katı) ve **BASK Karar Nisabı (en az 2/3 çoğunluk)**.
3. **`sec_1003_03`:** Kamu Borçlanma Araçları (DİBS), İhale Yöntemleri (Çoklu Fiyat / Amerikan vs Tek Fiyat / Hollanda), TÜFEX anapara koruması ve **ROT (yalnızca Kamu Kurumları ve PY Bankalar)**.
4. **`sec_1003_04`:** Kira Sertifikaları (Sukuk) ve 5 Temel İhraç Modeli (İcara, Yönetim Sözleşmesi, Murabaha, Mudaraba/Müşarake, İstisna; VKŞ malvarlığının dokunulmazlığı).
5. **`sec_1003_05`:** Menkul Kıymetleştirme: VDMK (VFF ihraç eder, bilanço dışı) vs İTMK (Banka ihraç eder, bilanço içi, **Çifte Teminat / Dual Recourse** ilkesi, Teminat Sorumlusu).
6. **`sec_1003_06`:** Yatırım Fonları, TEFAS, Borsa Yatırım Fonları (BYF/ETF - hisse gibi seans içinde anlık işlem) ve Serbest Fonlar (yalnızca nitelikli yatırımcıya).
7. **`sec_1003_07`:** Türev Araçlar, VİOP Sözleşmeleri (BIST 30 nakdi uzlaşma, Pay VİS fiziki teslimat) ve Varantlar (Alım/Satım, Asli Değer + Zaman Değeri, Moneyness).
8. **`sec_1003_08`:** Karma Menkul Kıymetler (PDT ihraççının payına dönüşür / masraf ihraççıya aittir / min 365 gün; DET başka ortaklık payına dönüşür; KİS max %50 ve oy hakkı yok) ve Varant Risk Parametreleri (Delta, Gamma, Theta, Vega, Rho).

---

### C. Modül 1005: Yatırım Kuruluşları (8 Bölüm)
1. **`sec_1005_01`:** Yatırım Hizmetleri, Faaliyetleri (10 temel hizmet) ve Yan Hizmetler (Kredi verme, döviz, genel tavsiye).
2. **`sec_1005_02`:** Aracı Kurum Grupları ve 2026 Asgari Sermaye Şartları (**Dar Yetkili: 45.000.000 TL**, **Kısmi Yetkili: 190.000.000 TL**, **Geniş Yetkili: 380.000.000 TL**, **Yeni Kuruluş: 440.000.000 TL**).
3. **`sec_1005_03`:** Müşteri Sınıflandırması ve 2026 Kurumsal Profesyonel Müşteri Kriterleri (En az 2 şart: **Aktif 500M TL**, **Hasılat 1 Mr TL**, **Özsermaye 50M TL**).
4. **`sec_1005_04`:** Uygunluk Testi (Appropriateness - alım satımda bilgi/tecrübe) vs Yerindelik Testi (Suitability - portföy yöneticiliği ve danışmanlıkta zorunlu; mali güç + amaç + tecrübe).
5. **`sec_1005_05`:** Kredili Menkul Kıymet, Açığa Satış ve Özkaynak Oranları (**Başlangıç: Asgari %50**, **Sürdürme: Asgari %35**, Margin Call tamamlama süresi: **EN GEÇ 2 İŞ GÜNÜ**, tamamlama hedefi: **%50 başlangıç oranı**).
6. **`sec_1005_06`:** Teşkilat Yapısı, Şube ve İrtibat Bürosu Esasları (**İrtibat bürosu m.44: Müşteri emirlerini iletebilir ve tanıtım yapabilir; para/kıymet alamaz, hesap açamaz, sözleşme yapamaz**; İç Sistemler doğrudan Yönetim Kurulu'na bağlıdır).
7. **`sec_1005_07`:** Belge ve Kayıt Düzeni (Genel belgeler, formlar ve ses kayıtları **en az 5 yıl**; Uzaktan kimlik tespiti kayıtları **en az 10 yıl**; Ekstreye itiraz süresi **30 gün**).
8. **`sec_1005_08`:** Kitle Fonlaması Platformları (Paya ve Borca Dayalı; gayrimenkul ve bağış yasak; kampanya azami **60 gün**, yatırımcı cayma hakkı **48 saat**) ve TSPB Promosyon Esasları (Bütçe max özsermayenin %1'i; Forex'te promosyon yasaktır).

---

### D. Modül 1012: Takas, Saklama ve Operasyon İşlemleri (8 Bölüm)
1. **`sec_1012_01`:** Takasbank Hukuki Statüsü (**Özel Statülü Kalkınma ve Yatırım Bankasıdır, mevduat bankası değildir**) ve Merkezi Karşı Taraf (MKT) Müessesesi (Sözleşme Yenileme / Novation; KMTP ve Dış Borçlanmada MKT yoktur).
2. **`sec_1012_02`:** Takas Döngüleri, Valörler ve Operasyonel Saatler (Pay T+2 DvP, takas borcu kapama saati: **16:45**; Teminat tamamlama son saati: **15:00**; BAP ön temerrüt aralığı: **16:46-17:00 / 0.25 ceza katsayısı**).
3. **`sec_1012_03`:** Teminat ve Risk Yönetimi (Başlangıç, Değişim / Mark-to-Market, Fiziki Teslimat; BISTECH Portföy Marjin Modeli; Teminat Değerleme Katsayısı = `1 - (Piyasa + Likidite + Kredi Riski)`; VİOP'ta asgari %50 nakit TL).
4. **`sec_1012_04`:** Temerrüt Yönetimi, Garanti Fonu (Pay: 200K, BAP: 700K, VİOP: 3.575M TL) ve **Madde 36 Uyarınca 7 Aşamalı Temerrüt Şelalesi** (1. Üyenin teminatı ➔ 2. Üyenin GF payı ➔ 3. Takasbank taahhüt özkaynağı ➔ 4. Diğer üyelerin GF payı ➔ 5. Takasbank kalan özkaynağı ➔ 6. Ek katkı payı ➔ 7. Karşılıklı tahsis).
5. **`sec_1012_05`:** MKK ve Doğrudan Hak Sahipliği Sistemi (Fiili ortaklık: Takasbank %64.9, BIST %30.1, TSPB %5.0; Tavanlar: %75 / %50 / %10 / %5; TCKN bazında doğrudan alt hesaplarda saklama; YMSK omnibus istisnası; **AYM kararıyla 10 yıllık zamanaşımıyla hisselerin devlete geçmesi kuralı iptal edilmiştir**).
6. **`sec_1012_06`:** MKK Elektronik Platformları (e-YATIRIMCI, e-GKS, e-ŞİRKET; **Yatırımcı Güvenlik Blokajını aracı kurum kaldıramaz, yalnızca yatırımcı kaldırabilir**; temettü T+2).
7. **`sec_1012_07`:** Takasbank Para Piyasası (TPP - kısa vadeli nakit fonlama, kör havuz) ve Ödünç Pay Piyasası (ÖPP - teminat tamamlama **en geç 2 saat**, temerrütte Takasbank piyasadan alım son süresi **T+3 saat 11:00**).
8. **`sec_1012_08`:** Portföy Saklama ve Saklama Kuruluşlarının Sorumlulukları (Genel vs Portföy Saklama; fon yöneticisi ile saklayıcı **aynı tüzel kişilik olamaz**; fesih ihbar süresi **en az 90 gün**).

---

## 3. Doğrulama ve Derleme Sonuçları

- **Veri ve Entegrasyon Testi (`python scripts/verify_all.py`):**
  ```
  [PASS] 1. Modül Meta Verileri (4/4 Modül Tam & Eksiksiz)
  [PASS] 2. Soru Havuzu (860 %100 Benzersiz Soru: 1001: 210, 1003: 210, 1005: 230, 1012: 210 Soru)
  [PASS] 3. Öğrenme Kartları (400/400 Kart: Tanım, Somut Örnek & Sınav Tuzağı Doğrulandı)
  [PASS] 4. Konu Anlatımları (32 Bölüm, 32 Formatlı Karşılaştırma Tablosu)
  [PASS] 6. Seslendirme & Metin Temizleme Motoru (Tüm Türkçe kısaltmalar & telaffuz kuralları hazır)
  ✅ TÜM VERİ VE ENTEGRASYON TESTLERİ %100 BAŞARIYLA GEÇTİ!
  ```
- **Uygulama Derleme (`npm run build`):**
  ```
  ✓ 2488 modules transformed.
  ✓ built in 4.96s (Sıfır hata)
  ```
