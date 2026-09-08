

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
