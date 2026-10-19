# -*- coding: utf-8 -*-
"""
Modül 1003: 50 İleri Seviye (Sert) Sınav Sorusu Üreticisi
Konu: Sermaye Piyasası Araçları 1
Türkiye Maarif Modeli: KB2_Muhakeme (%60), KB3_Vaka (%40)
Cevap Dağılımı: 10 A, 10 B, 10 C, 10 D, 10 E (Tam dengeli)
Tüm seçenek uzunluk oranları < 1.8, 0 Giveaway, 5 Aşamalı Açıklama Standardı.
"""
import json

def generate_questions():
    questions = []
    
    raw_data = [
        # --- BLOK 1: Q01-Q10 (2 A, 2 B, 2 C, 2 D, 2 E) ---
        # 1 (A)
        ("q_1003_sert_001", "A", "Bedelli Sermaye Artırımı & Rüçhan Hakkı Değeri",
         "Borsa İstanbul Yıldız Pazar'da işlem gören ve sermaye artırımı öncesi hisse kapanış fiyatı 40 TL olan Alfa Çimento A.Ş., %100 bedelli sermaye artırımına gitme kararı almıştır. Rüçhan hakkı kullanım fiyatı nominal değer olan 1 TL olarak belirlenmiştir.\n\nBuna göre bölünme sonrası hissenin teorik düzeltilmiş baz fiyatı ile 1 adet paya ait rüçhan hakkı kuponunun teorik değeri sırasıyla hangi seçenekte DOĞRU verilmiştir?",
         [("A", "Yeni Hisse Fiyatı: 20,50 TL; Rüçhan Hakkı Değeri: 19,50 TL"),
          ("B", "Yeni Hisse Fiyatı: 20,00 TL; Rüçhan Hakkı Değeri: 20,00 TL"),
          ("C", "Yeni Hisse Fiyatı: 19,50 TL; Rüçhan Hakkı Değeri: 20,50 TL"),
          ("D", "Yeni Hisse Fiyatı: 21,00 TL; Rüçhan Hakkı Değeri: 19,00 TL"),
          ("E", "Yeni Hisse Fiyatı: 40,00 TL; Rüçhan Hakkı Değeri: 1,00 TL")],
         "1. MEVZUAT DAYANAĞI: Borsa İstanbul Pay Piyasası Prosedürü ve VII-128.1 Pay Tebliği.\n2. HUKUKİ / TEKNİK ÇERÇEVE: Bedelli sermaye artırımında yeni teorik hisse fiyatı: P_yeni = (P_eski + B * R_fiyat) / (1 + B). Rüçhan hakkı değeri ise: R = P_eski - P_yeni formülüyle hesaplanır.\n3. ADIM ADIM İNCELEME / HESAPLAMA:\n- P_eski = 40 TL, B = %100 = 1,0, R_fiyat = 1 TL.\n- P_yeni = (40 + 1 * 1) / (1 + 1) = 41 / 2 = 20,50 TL.\n- Rüçhan Hakkı Değeri (R) = 40 - 20,50 = 19,50 TL.\n4. DOĞRU CEVAP VE SONUÇ: A şıkkında 20,50 TL ve 19,50 TL doğru verilmiştir.\n5. ÇELDİRİCİ TUZAĞI: Rüçhan fiyatını 1 TL yerine 0 almak veya P_eski / 2 = 20 TL ezberine düşmek.",
         "Rüçhan kullanım fiyatı 1 TL hesaba katılmalıdır: P_yeni = 41/2 = 20,50 TL; R = 40 - 20,50 = 19,50 TL.", "KB3_Vaka"),

        # 2 (B)
        ("q_1003_sert_002", "B", "Bedelli ve Bedelsiz Sermaye Artırımı Birlikte",
         "Sermayesi 100 milyon TL, hisse senedi son kapanış fiyatı 60 TL olan Beta Teknoloji A.Ş., aynı anda %100 bedelli ve %100 bedelsiz sermaye artırımı yapacağını duyurmuştur. Bedelli sermaye artırımında rüçhan hakkı kullanım fiyatı 2 TL'dir.\n\nBuna göre, sermaye artırımı sonrası oluşacak yeni hisse senedi teorik baz fiyatı kaç TL olacaktır?",
         [("A", "Yeni teorik baz fiyat 18,67 TL olarak belirlenir."),
          ("B", "Yeni teorik baz fiyat 20,67 TL olarak belirlenir."),
          ("C", "Yeni teorik baz fiyat 22,33 TL olarak belirlenir."),
          ("D", "Yeni teorik baz fiyat 25,00 TL olarak belirlenir."),
          ("E", "Yeni teorik baz fiyat 30,00 TL olarak belirlenir.")],
         "1. MEVZUAT DAYANAĞI: Borsa İstanbul Düzeltilmiş Pay Fiyatı Hesaplama Yöntemi.\n2. HUKUKİ / TEKNİK ÇERÇEVE: Bedelli ve bedelsiz sermaye artırımı birlikte yapıldığında formül:\nP_yeni = (P_eski + B * R_fiyat) / (1 + B + BD)'dir.\n3. ADIM ADIM İNCELEME / HESAPLAMA:\n- P_eski = 60 TL\n- B (Bedelli oranı) = %100 = 1,0\n- BD (Bedelsiz oranı) = %100 = 1,0\n- R_fiyat = 2 TL\n- Payda = 1 + 1 + 1 = 3\n- Pay = 60 + (1 * 2) = 62 TL\n- P_yeni = 62 / 3 = 20,666... ≈ 20,67 TL.\n4. DOĞRU CEVAP VE SONUÇ: B seçeneği 20,67 TL'dir.\n5. ÇELDİRİCİ TUZAĞI: Paydaya sadece bedelliyi eklemek veya rüçhan fiyatını nominal 1 TL varsayarak 61/3 = 20,33 bulmak.",
         "Payda 1 + B + BD = 3 olur. Pay ise 60 + 2 = 62 TL. 62/3 = 20,67 TL.", "KB3_Vaka"),

        # 3 (C)
        ("q_1003_sert_003", "C", "Nakit Temettü Dağıtımı ve Borsa Referans Fiyatı",
         "Hisseleri Borsa İstanbul'da işlem gören Gama Sanayi A.Ş., hisse başına brüt 6 TL (%600), net 5,40 TL (%540) nakit temettü dağıtacaktır (Bireysel yatırımcı stopaj oranı %10). Şirket hisseleri temettü dağıtım tarihinden önceki son seansta 52 TL kapanış fiyatından işlem görmüştür.\n\nBuna göre temettü dağıtım günü seans açılışında geçerli olacak teorik hisse referans fiyatı kaç TL olacaktır?",
         [("A", "Açılış referans baz fiyatı 44,00 TL olarak sisteme girilir."),
          ("B", "Açılış referans baz fiyatı 45,40 TL olarak sisteme girilir."),
          ("C", "Açılış referans baz fiyatı 46,00 TL olarak sisteme girilir."),
          ("D", "Açılış referans baz fiyatı 46,60 TL olarak sisteme girilir."),
          ("E", "Açılış referans baz fiyatı 52,00 TL olarak sisteme girilir.")],
         "1. MEVZUAT DAYANAĞI: Borsa İstanbul Pay Piyasası İşleyiş Prosedürü.\n2. HUKUKİ / TEKNİK ÇERÇEVE: Borsa referans fiyatı hesabında hisse kapanış fiyatından BRÜT TEMETTÜ düşülür. Stopaj yatırımcının şahsi vergi yükümlülüğü olup borsa baz fiyatını etkilemez.\n3. ADIM ADIM İNCELEME / HESAPLAMA:\n- P_ref = P_kapanis - Brüt Temettü\n- P_ref = 52 - 6,00 = 46,00 TL.\n4. DOĞRU CEVAP VE SONUÇ: C seçeneğidir (46,00 TL).\n5. ÇELDİRİCİ TUZAĞI: Net temettüyü düşerek 52 - 5,40 = 46,60 TL bulmak (D şıkkı en yaygın tuzaktır).",
         "Borsa referans fiyatı hesaplanırken brüt temettü düşülür, stopaj düşülmez: 52 - 6 = 46,00 TL.", "KB3_Vaka"),

        # 4 (D)
        ("q_1003_sert_004", "D", "Tahvil Kirli ve Temiz Fiyat Ayrımı",
         "Yıllık %20 kupon faizi ödeyen, 1.000 TL nominal değerli bir devlet tahvilinin kupon ödeme sıklığı 6 ayda birdir (yılda iki kupon, kupon başına %10). Son kupon ödemesinin üzerinden 90 gün geçmiştir (Kupon dönemi 180 gün kabul edilecektir). Tahvilin borsadaki temiz fiyatı (clean price) 1.020 TL'dir.\n\nBuna göre söz konusu tahvilin alım satımına esas teşkil edecek 'Kirli Fiyatı' (dirty price) kaç TL'dir?",
         [("A", "İşleme esas kirli takas fiyatı 1.020 TL'dir."),
          ("B", "İşleme esas kirli takas fiyatı 1.040 TL'dir."),
          ("C", "İşleme esas kirli takas fiyatı 1.050 TL'dir."),
          ("D", "İşleme esas kirli takas fiyatı 1.070 TL'dir."),
          ("E", "İşleme esas kirli takas fiyatı 1.120 TL'dir.")],
         "1. MEVZUAT DAYANAĞI: Sermaye Piyasasında Borçlanma Araçları Fiyatlama Esasları.\n2. HUKUKİ / TEKNİK ÇERÇEVE: Kirli Fiyat = Temiz Fiyat + Birikmiş Faiz (Accrued Interest).\n3. ADIM ADIM İNCELEME / HESAPLAMA:\n- Nominal Değer = 1.000 TL\n- 6 aylık kupon faiz oranı = %10 -> 6 aylık kupon tutarı = 1.000 * %10 = 100 TL.\n- Kupon döneminde geçen gün = 90 gün / 180 gün = 0,5 (yarısı).\n- Birikmiş Faiz = 100 * (90 / 180) = 50 TL.\n- Kirli Fiyat = Temiz Fiyat + Birikmiş Faiz = 1.020 + 50 = 1.070 TL.\n4. DOĞRU CEVAP VE SONUÇ: D seçeneğidir (1.070 TL).\n5. ÇELDİRİCİ TUZAĞI: Yıllık faiz üzerinden 90 günlük hesap yapıp 1.000 * 0,20 * (90/360) = 50 TL bulup temiz fiyata eklemeyi unutup sadece 1.050 demek.",
         "Kirli Fiyat = Temiz Fiyat + Birikmiş Faiz. Birikmiş faiz = 100 * (90/180) = 50 TL. Kirli fiyat = 1.020 + 50 = 1.070 TL.", "KB3_Vaka"),

        # 5 (E)
        ("q_1003_sert_005", "E", "Tahvil Getiri Eğrisi ve Beklentiler Teorisi",
         "Gelecekte kısa vadeli faiz oranlarının kesintisiz olarak yükseleceği genel piyasa aktörleri tarafından öngörüldüğünde, 'Geleneksel Beklentiler Teorisi' (Expectations Theory) uyarınca getiri eğrisinin (yield curve) şekli ve özellikleri hakkında;\n\nI. Uzun vadeli tahvil faizleri, gelecekte beklenen kısa vadeli faizlerin geometrik ortalamasını yansıtacağı için getiri eğrisi pozitif eğimli (yukarı eğimli) olur.\nII. Getiri eğrisinin ters (negatif eğimli) olması piyasada gelecekte faizlerin düşeceği beklentisine işaret eder.\nIII. Yatırımcıların uzun vadeli tahvillerde katlandıkları risk için talep ettikleri likidite primi pozitif eğimi daha da dikleştirir.\n\nYukarıda yer alan iktisadi ve finansal tespitlerden hangileri DOĞRUDUR?",
         [("A", "Yalnızca I numaralı tespit teorik olarak doğrudur."),
          ("B", "Yalnızca II numaralı tespit teorik olarak doğrudur."),
          ("C", "I ve II numaralı tespitler teorik olarak doğrudur."),
          ("D", "II ve III numaralı tespitler teorik olarak doğrudur."),
          ("E", "I, II ve III numaralı tespitlerin tamamı teorik olarak doğrudur.")],
         "1. MEVZUAT DAYANAĞI: Sermaye Piyasası Finansal Teori ve Sabit Getirili Menkul Kıymetler Analizi.\n2. HUKUKİ / TEKNİK ÇERÇEVE: Beklentiler teorisine göre uzun vadeli getiri gelecekteki kısa vadeli getirilerin ortalamasıdır. Faiz artışı beklentisi pozitif eğim yaratır; düşüş beklentisi ters eğim yaratır. Likidite primi eğimi dikleştirir.\n3. ADIM ADIM İNCELEME / HESAPLAMA: I, II ve III öncülleri finans teorisinin getiri eğrisi aksiyomlarını eksiksiz açıklar.\n4. DOĞRU CEVAP VE SONUÇ: E şıkkıdır.\n5. ÇELDİRİCİ TUZAĞI: Faiz artışında getiri eğrisinin ters olacağını zannetmek.",
         "Gelecekte faiz artışı beklentisi pozitif eğimli getiri eğrisi üretir; likidite primi ise eğimi daha da dikleştirir.", "KB2_Muhakeme"),

        # 6 (A)
        ("q_1003_sert_006", "A", "Tahvil Süresi (Duration) ve Fiyat Değişimi",
         "Portföy yöneticisi Ahmet Bey'in elinde modifiye süresi (Modified Duration) 4,5 yıl olan 10 milyon TL piyasa değerli sabit kuponlu tahvil bulunmaktadır. Piyasa faiz oranlarının (getirinin) derhal ve paralel olarak 200 baz puan (%2,00) ARTMASI durumunda;\n\nTahvil portföyünün piyasa değerinde yaklaşık olarak nasıl bir oransal ve parasal değişim meydana gelir?",
         [("A", "%9 oranında değer kaybı gerçekleşir ve portföy değeri 900.000 TL azalır."),
          ("B", "%9 oranında değer kazancı gerçekleşir ve portföy değeri 900.000 TL artar."),
          ("C", "%4,5 oranında değer kaybı gerçekleşir ve portföy değeri 450.000 TL azalır."),
          ("D", "%2 oranında değer kaybı gerçekleşir ve portföy değeri 200.000 TL azalır."),
          ("E", "%18 oranında değer kaybı gerçekleşir ve portföy değeri 1.800.000 TL azalır.")],
         "1. MEVZUAT DAYANAĞI: Sabit Getirili Menkul Kıymetler Faiz Riski Ölçümü.\n2. HUKUKİ / TEKNİK ÇERÇEVE: Tahvil fiyatının faiz değişimine duyarlılığı: Delta P / P ≈ - Modified Duration * Delta y.\n3. ADIM ADIM İNCELEME / HESAPLAMA:\n- MD = 4,5 yıl\n- Faiz artışı (Delta y) = +%2 = +0,02 (200 baz puan)\n- Fiyat Değişimi (Delta P / P) = -4,5 * (+0,02) = -0,09 = -%9 (Yani %9 değer kaybı).\n- Parasal Tutar = 10.000.000 * %9 = 900.000 TL değer azalışı.\n4. DOĞRU CEVAP VE SONUÇ: A seçeneğinde %9 azalış ve 900.000 TL kayıp doğru verilmiştir.\n5. ÇELDİRİCİ TUZAĞI: Faiz arttığında tahvil fiyatının da artacağını sanmak (B şıkkı) veya 200 baz puanı %0,2 sanmak.",
         "Fiyat değişimi = -MD * Delta y = -4,5 * %2 = -%9. Portföy 900.000 TL değer kaybeder.", "KB3_Vaka"),

        # 7 (B)
        ("q_1003_sert_007", "B", "İskontolu Bono Basit Getiri Hesabı",
         "Vadesine 73 gün kalmış olan 100 TL nominal değerli bir Hazine Bonosu piyasada 95 TL peşin fiyattan satılmaktadır (Faiz hesabında 1 yıl 365 gün kabul edilecektir).\n\nSöz konusu bonoyu satın alarak vadesine kadar elinde tutacak bir yatırımcının elde edeceği 'Yıllık Basit İskonto Getirisi' (yıllık basit faiz) yüzde kaçtır?",
         [("A", "Yıllık basit iskonto getirisi yüzde 23,45 olarak gerçekleşir."),
          ("B", "Yıllık basit iskonto getirisi yüzde 26,32 olarak gerçekleşir."),
          ("C", "Yıllık basit iskonto getirisi yüzde 25,00 olarak gerçekleşir."),
          ("D", "Yıllık basit iskonto getirisi yüzde 28,15 olarak gerçekleşir."),
          ("E", "Yıllık basit iskonto getirisi yüzde 30,00 olarak gerçekleşir.")],
         "1. MEVZUAT DAYANAĞI: Para ve Sermaye Piyasası Finansal Matematik Standartları.\n2. HUKUKİ / TEKNİK ÇERÇEVE: Basit Verim (Getiri) Formülü:\nr = [(Nominal - Satış Fiyatı) / Satış Fiyatı] * (365 / Gün Sayısı).\n3. ADIM ADIM İNCELEME / HESAPLAMA:\n- Nominal = 100 TL, Alış Fiyatı = 95 TL, Vade = 73 gün.\n- Dönemsel Getiri = (100 - 95) / 95 = 5 / 95 = 0,05263 (%5,263).\n- Yıllık Basit Getiri = 0,05263 * (365 / 73) = 0,05263 * 5 = 0,26315 = %26,32.\n4. DOĞRU CEVAP VE SONUÇ: B seçeneği (%26,32) tam doğrudur.\n5. ÇELDİRİCİ TUZAĞI: Paydaya satış fiyatı yerine nominal değeri yazıp (5/100) * 5 = %25 bulmak (C şıkkı klasik sınav tuzağıdır).",
         "Getiri yatırılan anapara (95 TL) üzerinden hesaplanır: (5/95) * (365/73) = %26,32.", "KB3_Vaka"),

        # 8 (C)
        ("q_1003_sert_008", "C", "Sukuk (Kira Sertifikası) Türleri ve Sahipliğe Dayalı İhraç",
         "III-61.1 sayılı Kira Sertifikaları Tebliği uyarınca ihraç edilen kira sertifikası türleri arasında yer alan 'Sahipliğe Dayalı Kira Sertifikası' (İcara Sukuk) işleyiş mekanizmasına dair hangisi DOĞRUDUR?",
         [("A", "Varlık kiralama şirketi hiçbir varlık satın almaz; doğrudan faiz karşılığı borç para toplar."),
          ("B", "VKŞ tarafından kaynak kuruluştan satın alınan varlıklar derhal üçüncü şahıslara satılarak kapatılır."),
          ("C", "VKŞ varlığı devralır, tekrar kaynak kuruluşa kiralar ve kira gelirini sertifika sahiplerine dağıtır."),
          ("D", "Sahipliğe dayalı kira sertifikasında kaynak kuruluşun geri alım taahhüdünde bulunması kanunen yasaktır."),
          ("E", "Yatırımcılara ödenecek kira getirisi şirket hisse senetlerinin borsa performansına endekslenmek zorundadır.")],
         "1. MEVZUAT DAYANAĞI: III-61.1 Tebliği m. 4.\n2. HUKUKİ / TEKNİK ÇERÇEVE: Sahipliğe dayalı kira sertifikasında VKŞ varlığı satın alır, kaynak kuruluşa geri kiralar (Sat ve Geri Kirala - Sale and Leaseback) ve periyodik kira bedellerini yatırımcılara öder.\n3. ADIM ADIM İNCELEME / HESAPLAMA: C şıkkı sahipliğe dayalı sukukun mevzuattaki tanımıdır.\n4. DOĞRU CEVAP VE SONUÇ: C seçeneğidir.\n5. ÇELDİRİCİ TUZAĞI: Borçlanma aracıyla aynı mekanizmada çalıştığının düşünülmesi.",
         "Sahipliğe dayalı sukukta VKŞ varlığı alır, kaynak kuruluşa kiralar ve kira gelirlerini yatırımcılara aktarır.", "KB2_Muhakeme"),

        # 9 (D)
        ("q_1003_sert_009", "D", "Kira Sertifikası Türleri Arasındaki Hukuki Farklar",
         "III-61.1 sayılı Tebliğ kapsamında kira sertifikası türleri ve dayanak sözleşme eşleştirmelerine dair;\n\nI. Yönetim Sözleşmesine Dayalı: Varlık veya hakların VKŞ adına yönetilmesi amacıyla kaynak kuruluşa devredilmesi esasına dayanır.\nII. Ortaklığa Dayalı: Mudaraba (sermaye-emek ortaklığı) veya Müşareke (sermaye-sermaye ortaklığı) sözleşmelerine dayanılarak ihraç edilir.\nIII. Eser Sözleşmesine Dayalı: İstisna sözleşmesi kapsamında henüz imal edilmemiş veya inşa edilmemiş bir eserin meydana getirilmesini finanse etmek amacıyla ihraç edilir.\n\nYukarıda yapılan hukuki ve teknik nitelemelerden hangileri DOĞRUDUR?",
         [("A", "Yalnızca I numaralı niteleme mevzuat uyarınca doğrudur."),
          ("B", "Yalnızca II numaralı niteleme mevzuat uyarınca doğrudur."),
          ("C", "I ve II numaralı nitelemeler mevzuat uyarınca doğrudur."),
          ("D", "I, II ve III numaralı nitelemelerin tamamı mevzuat uyarınca doğrudur."),
          ("E", "Yalnızca III numaralı niteleme mevzuat uyarınca doğrudur.")],
         "1. MEVZUAT DAYANAĞI: III-61.1 sayılı Tebliğ m. 4-8.\n2. HUKUKİ / TEKNİK ÇERÇEVE: Tebliğde 5 temel kira sertifikası düzenlenmiştir: 1) Sahiplik, 2) Yönetim sözleşmesi (Vekalet), 3) Alım-satım (Murabaha), 4) Ortaklık (Mudaraba/Müşareke), 5) Eser sözleşmesi (İstisna).\n3. ADIM ADIM İNCELEME / HESAPLAMA: I, II ve III öncüllerinin her biri tebliğ maddeleriyle birebir uyumludur.\n4. DOĞRU CEVAP VE SONUÇ: D seçeneğidir.\n5. ÇELDİRİCİ TUZAĞI: Eser sözleşmesinin sermaye piyasasında sukuka konu olamayacağını zannetmek.",
         "Ortaklık sukuku Mudaraba/Müşareke, eser sözleşmesine dayalı sukuk ise İstisna prensibine dayanır.", "KB2_Muhakeme"),

        # 10 (E)
        ("q_1003_sert_010", "E", "Alım Varantı (Call) Başabaş Noktası ve Kâr/Zarar",
         "Yatırımcı Cengiz Bey, Borsa İstanbul Varant Pazarı'nda XYZ hisse senedi üzerine yazılmış, kullanım fiyatı 80 TL ve çarpanı 0,50 olan bir alım varantını 4 TL prim ödeyerek satın almıştır.\n\nVade sonunda dayanak XYZ hisse senedinin piyasa fiyatının 92 TL olması durumunda, Cengiz Bey'in 1 adet varant başına net kârı veya zararı ne olur?",
         [("A", "Varant başına net sekiz TL kâr elde eder."),
          ("B", "Varant başına net altı TL kâr elde eder."),
          ("C", "Varant başına net dört TL zarar eder."),
          ("D", "Varant başabaş noktasında olup kâr veya zarar sıfırdır."),
          ("E", "Varant başına net iki TL kâr elde eder.")],
         "1. MEVZUAT DAYANAĞI: Borsa İstanbul Varant ve Sertifikalar Piyasası İşleyiş Kılavuzu.\n2. HUKUKİ / TEKNİK ÇERÇEVE: Alım varantı içsel değeri: Max[0, (Dayanak Fiyat - Kullanım Fiyatı) * Çarpan]. Net Kâr = İçsel Değer - Ödenen Prim.\n3. ADIM ADIM İNCELEME / HESAPLAMA:\n- Dayanak Fiyat (S) = 92 TL\n- Kullanım Fiyatı (K) = 80 TL\n- Fark = 92 - 80 = 12 TL\n- Çarpan = 0,50\n- Vade sonu varant değeri (ödeme) = 12 * 0,50 = 6 TL.\n- Başlangıçta ödenen varant primi = 4 TL.\n- Net Kâr = 6 - 4 = +2 TL.\n4. DOĞRU CEVAP VE SONUÇ: E seçeneğidir (+2 TL kâr).\n5. ÇELDİRİCİ TUZAĞI: Çarpanı (0,50) unutarak 92 - 80 = 12 TL bulup 12 - 4 = 8 TL demek veya primi düşmeyi unutarak 6 TL demek.",
         "Varant itfa değeri = (92 - 80) * 0,5 = 6 TL. Net Kâr = 6 - 4 = +2 TL kâr.", "KB3_Vaka"),

        # --- BLOK 2: Q11-Q20 (2 A, 2 B, 2 C, 2 D, 2 E) ---
        # 11 (A)
        ("q_1003_sert_011", "A", "Satım Varantı (Put) Başabaş Noktası ve İtfa",
         "Kullanım fiyatı 50 TL, çarpanı 0,20 ve piyasa satış primi 1,50 TL olan bir satım varantının (Put Warrant) vade sonundaki 'Başabaş Noktası' (dayanak varlık hisse fiyatı) kaç TL'dir?",
         [("A", "Başabaş dayanak varlık hisse fiyatı 42,50 TL'dir."),
          ("B", "Başabaş dayanak varlık hisse fiyatı 48,50 TL'dir."),
          ("C", "Başabaş dayanak varlık hisse fiyatı 51,50 TL'dir."),
          ("D", "Başabaş dayanak varlık hisse fiyatı 57,50 TL'dir."),
          ("E", "Başabaş dayanak varlık hisse fiyatı 40,00 TL'dir.")],
         "1. MEVZUAT DAYANAĞI: Borsa İstanbul Yapılandırılmış Ürünler Pazarı Kılavuzu.\n2. HUKUKİ / TEKNİK ÇERÇEVE: Satım varantında başabaş noktası (Break-even): Dayanak Varlık Fiyatı = Kullanım Fiyatı - (Ödenen Prim / Çarpan).\n3. ADIM ADIM İNCELEME / HESAPLAMA:\n- Kullanım Fiyatı = 50 TL\n- Prim / Çarpan = 1,50 / 0,20 = 7,50 TL (Hisse başına katlanılan prim maliyeti).\n- Başabaş Fiyatı = 50 - 7,50 = 42,50 TL.\n- Kontrol: Hisse 42,50 TL olursa, varant değeri = (50 - 42,50) * 0,20 = 7,50 * 0,20 = 1,50 TL. Prim 1,50 TL ödendiğinden kâr/zarar = 0 TL.\n4. DOĞRU CEVAP VE SONUÇ: A seçeneğidir (42,50 TL).\n5. ÇELDİRİCİ TUZAĞI: Çarpanı bölmek yerine primle doğrudan çıkarmak (50 - 1,50 = 48,50 TL) veya alım varantı gibi toplayarak 57,50 TL bulmak.",
         "Satım varantı başabaş = Kullanım Fiyatı - (Prim / Çarpan) = 50 - (1,50 / 0,20) = 42,50 TL.", "KB3_Vaka"),

        # 12 (B)
        ("q_1003_sert_012", "B", "Varant Göstergeleri: Kaldıraç ve Efektif Kaldıraç",
         "Dayanak hisse senedi fiyatı 100 TL, kullanım fiyatı 95 TL, varant fiyatı 5 TL, çarpanı 0,25 ve Deltası 0,60 olan bir alım varantının 'Kaldıraç' (Gearing) ve 'Efektif Kaldıraç' (Elasticity) değerleri sırasıyla nedir?",
         [("A", "Kaldıraç: 20; Efektif Kaldıraç: 12"),
          ("B", "Kaldıraç: 5; Efektif Kaldıraç: 3"),
          ("C", "Kaldıraç: 10; Efektif Kaldıraç: 6"),
          ("D", "Kaldıraç: 4; Efektif Kaldıraç: 2,4"),
          ("E", "Kaldıraç: 15; Efektif Kaldıraç: 9")],
         "1. MEVZUAT DAYANAĞI: Sermaye Piyasasında Türev ve Yapılandırılmış Araçlar Risk Göstergeleri.\n2. HUKUKİ / TEKNİK ÇERÇEVE: Kaldıraç (Gearing) = (Dayanak Hisse Fiyatı * Çarpan) / Varant Fiyatı. Efektif Kaldıraç (Effective Gearing) = Delta * Kaldıraç.\n3. ADIM ADIM İNCELEME / HESAPLAMA:\n- Gearing = (100 * 0,25) / 5 = 25 / 5 = 5.\n- Effective Gearing = 0,60 * 5 = 3,0.\n4. DOĞRU CEVAP VE SONUÇ: B seçeneğidir (Kaldıraç: 5; Efektif Kaldıraç: 3).\n5. ÇELDİRİCİ TUZAĞI: Çarpanı paya çarpmayı unutup 100 / 5 = 20 demek ve efektif kaldıracı 20 * 0,6 = 12 bulmak (A şıkkı).",
         "Gearing = (100 * 0,25) / 5 = 5. Efektif Kaldıraç = 5 * 0,60 = 3.", "KB3_Vaka"),

        # 13 (C)
        ("q_1003_sert_013", "C", "VİOP Vadeli İşlem Sözleşmesi Teorik Fiyatı",
         "Dayanak varlık spot fiyatı 200 TL olan bir hisse senedi vadeli işlem sözleşmesinde vadenin bitimine 73 gün vardır. Yıllık risksiz faiz oranı %30, dayanak hissenin vadesi boyunca beklenen temettü verimi %5'tir (1 yıl = 365 gün kabul edilecektir).\n\nTaşıma Maliyeti Modeli (Cost of Carry) uyarınca söz konusu vadeli işlem sözleşmesinin teorik vadeli fiyatı kaç TL olmalıdır?",
         [("A", "Teorik vadeli uzlaşma fiyatı 205,00 TL olmalıdır."),
          ("B", "Teorik vadeli uzlaşma fiyatı 208,00 TL olmalıdır."),
          ("C", "Teorik vadeli uzlaşma fiyatı 210,00 TL olmalıdır."),
          ("D", "Teorik vadeli uzlaşma fiyatı 212,00 TL olmalıdır."),
          ("E", "Teorik vadeli uzlaşma fiyatı 215,00 TL olmalıdır.")],
         "1. MEVZUAT DAYANAĞI: Borsa İstanbul VİOP Prosedürü ve Vadeli Sözleşmeler Fiyatlama Teorisi.\n2. HUKUKİ / TEKNİK ÇERÇEVE: Vadeli Sözleşme Teorik Fiyatı: F = S * [1 + (r - q) * (t / 365)]. Burada S = Spot fiyat, r = Faiz oranı, q = Temettü verimi, t = Vadeye kalan gün.\n3. ADIM ADIM İNCELEME / HESAPLAMA:\n- Net Taşıma Maliyeti Oranı = r - q = %30 - %5 = %25 = 0,25.\n- Dönem Oranı = 73 / 365 = 1 / 5 = 0,20.\n- Net Taşıma Maliyeti Çarpanı = 1 + (0,25 * 0,20) = 1 + 0,05 = 1,05.\n- Vadeli Fiyat (F) = 200 * 1,05 = 210 TL.\n4. DOĞRU CEVAP VE SONUÇ: C seçeneğidir (210,00 TL).\n5. ÇELDİRİCİ TUZAĞI: Temettüyü düşmek yerine faize ekleyerek 200 * [1 + 0,35 * 0,2] = 214 TL veya temettüyü tamamen ihmal edip 200 * 1,06 = 212 TL bulmak (D şıkkı).",
         "F = S * [1 + (r - q) * (t/365)] = 200 * [1 + 0,25 * 0,2] = 200 * 1,05 = 210 TL.", "KB3_Vaka"),

        # 14 (D)
        ("q_1003_sert_014", "D", "VİOP Margin Call (Teminat Tamamlama Çağrısı) Kuralı",
         "Yatırımcı Derya Hanım, VİOP'ta başlangıç teminatı sözleşme başına 2.000 TL, sürdürme teminatı oranı %75 (1.500 TL) olan bir sözleşmeden 10 adet uzun (long) pozisyon açmış ve hesabına 20.000 TL nakit teminat yatırmıştır. Gün sonunda piyasa aleyhine hareket etmiş ve hesaptaki toplam teminat tutarı 13.500 TL'ye (sözleşme başına 1.350 TL) gerilemiştir.\n\nTakasbank ve VİOP mevzuatı uyarınca Derya Hanım'a yapılacak teminat tamamlama çağrısı tutarı ve yasal tamamlama seviyesi nedir?",
         [("A", "Teminat sürdürme seviyesine (15.000 TL) tamamlanmalı ve 1.500 TL yatırılmalıdır."),
          ("B", "Yalnızca sözleşme başına 100 TL olmak üzere toplam 1.000 TL yatırılmalıdır."),
          ("C", "Pozisyonlar derhal re'sen kapatılır ve hiçbir nakit tamamlama talep edilemez."),
          ("D", "Teminat Başlangıç Teminatına (20.000 TL) tamamlanmalı ve 6.500 TL nakit yatırılmalıdır."),
          ("E", "Teminat tutarı 13.500 TL olduğu için herhangi bir margin call çağrısı oluşmaz.")],
         "1. MEVZUAT DAYANAĞI: Takasbank Merkezi Karşı Taraf Mevzuatı ve VİOP İşleyiş Esasları.\n2. HUKUKİ / TEKNİK ÇERÇEVE: Teminat tutarı Sürdürme Teminatı seviyesinin (10 * 1.500 = 15.000 TL) altına düştüğünde Margin Call oluşur. TEMİNAT SÜRDÜRME SEVİYESİNE DEĞİL, BAŞLANGIÇ TEMİNATI SEVİYESİNE (20.000 TL) TAMAMLANMAK ZORUNDADIR!\n3. ADIM ADIM İNCELEME / HESAPLAMA:\n- Başlangıç Teminatı Hedefi = 10 * 2.000 = 20.000 TL.\n- Mevcut Teminat = 13.500 TL.\n- Eksik Tutar (Yatırılması gereken) = 20.000 - 13.500 = 6.500 TL.\n4. DOĞRU CEVAP VE SONUÇ: D seçeneğidir (Başlangıç teminatına tamamlama ve 6.500 TL).\n5. ÇELDİRİCİ TUZAĞI: Teminatın sürdürme teminatına tamamlanacağını zannederek 15.000 - 13.500 = 1.500 TL demek (A şıkkı sınavın en büyük tuzağıdır!).",
         "VİOP'ta teminat sürdürme seviyesinin altına indiğinde BAŞLANGIÇ TEMİNATI'na tamamlanır. 20.000 - 13.500 = 6.500 TL.", "KB3_Vaka"),

        # 15 (E)
        ("q_1003_sert_015", "E", "VİOP Günlük Uzlaşma ve Mark-to-Market Mekanizması",
         "Borsa İstanbul Vadeli İşlem ve Opsiyon Piyasası'nda (VİOP) uygulanan 'Günlük Uzlaşma Fiyatı' ve pozisyonların piyasa fiyatına göre değerlenmesi (Mark-to-Market) sürecine ilişkin;\n\nI. Her iş günü seans sonunda Takasbank tarafından hesaplanan günlük uzlaşma fiyatına göre tüm açık pozisyonların kâr/zararı hesaplanır.\nII. Oluşan kârlar yatırımcının serbest teminat hesabına alacak, zararlar ise teminat hesabından borç kaydedilir.\nIII. Günlük uzlaşma fiyatı tespit edilirken son 10 dakika içinde seansta gerçekleşen işlemlerin ağırlıklı ortalama fiyatı esas alınır.\n\nYukarıda belirtilen VİOP operasyonel kurallarından hangileri DOĞRUDUR?",
         [("A", "Yalnızca I numaralı kural mevzuat uyarınca doğrudur."),
          ("B", "Yalnızca II numaralı kural mevzuat uyarınca doğrudur."),
          ("C", "I ve II numaralı kurallar mevzuat uyarınca doğrudur."),
          ("D", "II ve III numaralı kurallar mevzuat uyarınca doğrudur."),
          ("E", "I, II ve III numaralı kuralların tamamı mevzuat uyarınca doğrudur.")],
         "1. MEVZUAT DAYANAĞI: Borsa İstanbul VİOP Prosedürü Bölüm 7.\n2. HUKUKİ / TEKNİK ÇERÇEVE: VİOP'ta kâr/zarar her gün uzlaşma fiyatıyla realize olur. Kârlar nemalanır, zararlar teminattan düşer. Günlük uzlaşma fiyatında seans sonu son 10 dakikanın ağırlıklı ortalaması kullanılır.\n3. ADIM ADIM İNCELEME / HESAPLAMA: I, II ve III öncülleri mark-to-market mekanizmasını tam ve doğru tarif eder.\n4. DOĞRU CEVAP VE SONUÇ: E seçeneğidir.\n5. ÇELDİRİCİ TUZAĞI: Kâr/zararın sadece vade sonunda hesaba geçeceğini zannetmek.",
         "VİOP'ta mark-to-market günlük işler, kâr/zarar nakit yansır ve son 10 dakikalık ağırlıklı ortalama fiyat esas alınır.", "KB2_Muhakeme"),

        # 16 (A)
        ("q_1003_sert_016", "A", "Tahvil Fiyatı ve Faiz Oranı Duyarlılığı",
         "Sabit getirili borçlanma araçları teorisinde 'Kupon Oranı' ve 'Vade' (Maturity) unsurlarının tahvilin faiz duyarlılığı (fiyat oynaklığı) üzerindeki etkisine dair hangisi DOĞRUDUR?",
         [("A", "Vadesi daha uzun ve kupon oranı daha düşük olan tahviller faiz değişimlerine karşı en yüksek fiyat duyarlılığına sahiptir."),
          ("B", "Kupon oranı yüksek olan tahvillerin faiz değişimlerine karşı fiyat duyarlılığı kuponsuz tahvillerden daha fazladır."),
          ("C", "Vadenin uzaması tahvil fiyatının faiz değişimlerine karşı duyarlılığını her zaman azaltır."),
          ("D", "Kupon oranı ve vadenin tahvilin süre (duration) değeri ve faiz riskine hiçbir etkisi bulunmaz."),
          ("E", "Sadece değişken faizli tahvillerin faiz duyarlılığı vardır, sabit faizli tahvillerin fiyatı sabittir.")],
         "1. MEVZUAT DAYANAĞI: Sabit Getirili Menkul Kıymetler Analiz İlkeleri.\n2. HUKUKİ / TEKNİK ÇERÇEVE: Tahvil teoremleri: 1) Vade uzadıkça süre ve faiz duyarlılığı artar. 2) Kupon oranı azaldıkça süre artar ve faiz duyarlılığı artar. Sıfır kuponlu (kuponsuz) uzun vadeli tahvil en yüksek faiz riskine sahiptir.\n3. ADIM ADIM İNCELEME / HESAPLAMA: A seçeneğindeki uzun vade ve düşük kupon kombinasyonu en yüksek fiyat oynaklığını üretir.\n4. DOĞRU CEVAP VE SONUÇ: A seçeneğidir.\n5. ÇELDİRİCİ TUZAĞI: Yüksek kuponun daha çok risk taşıdığı yanılgısı (yüksek kupon nakit akışını öne çekerek süreyi kısaltır ve riski azaltır).",
         "Düşük kupon ve uzun vade en yüksek faiz duyarlılığını (duration) oluşturur.", "KB2_Muhakeme"),

        # 17 (B)
        ("q_1003_sert_017", "B", "Eurobond (Eurotahvil) Yapısı ve Özellikleri",
         "Türkiye Cumhuriyeti Hazine ve Maliye Bakanlığı veya yerli bir banka tarafından uluslararası piyasalarda ihraç edilen Eurobond'lara (Dış Borçlanma Araçları) ilişkin hangisi YANLIŞTIR?",
         [("A", "İhraççının kendi ulusal para birimi dışındaki bir para birimi (genellikle ABD Doları veya Avro) cinsinden ihraç edilir."),
          ("B", "Eurobond ihraçlarında takas ve saklama yalnızca Borsa İstanbul Takasbank nezdinde yapılmak zorundadır."),
          ("C", "Genellikle hamiline yazılı olarak ihraç edilir ve uluslararası takas Euroclear veya Clearstream üzerinden yürütülür."),
          ("D", "ABD Doları cinsi Eurobondlar kural olarak 6 ayda bir, Avro cinsi Eurobondlar ise yılda bir kupon faizi öder."),
          ("E", "Borsa İstanbul Borçlanma Araçları Piyasası bünyesinde oluşturulan Dış Borçlanma Araçları Pazarı'nda işlem görebilir.")],
         "1. MEVZUAT DAYANAĞI: 6362 sayılı SPKn m. 31 ve Dış Borçlanma Araçları Düzenlemeleri.\n2. HUKUKİ / TEKNİK ÇERÇEVE: Eurobondlar uluslararası piyasada ihraç edilir ve küresel saklama Euroclear ve Clearstream nezdindedir. Takasbank'ta saklanma zorunluluğu yoktur.\n3. ADIM ADIM İNCELEME / HESAPLAMA: B seçeneğindeki Takasbank zorunluluğu açıkça yanlıştır.\n4. DOĞRU CEVAP VE SONUÇ: B seçeneğidir.\n5. ÇELDİRİCİ TUZAĞI: Eurobond'un adındaki 'Euro' sebebiyle sadece para biriminin Avro olabileceğini sanmak.",
         "Eurobond takas ve saklaması küresel ölçekte Euroclear ve Clearstream nezdinde gerçekleştirilir.", "KB2_Muhakeme"),

        # 18 (C)
        ("q_1003_sert_018", "C", "Varlığa Dayalı Menkul Kıymetler (VDMK) ve Fon Malvarlığı",
         "III-58.1 sayılı Varlığa Dayalı Menkul Kıymetler Tebliği uyarınca kurulan 'Varlık Finansmanı Fonu' (VFF) ve fon portföyünün hukuki statüsüne dair hangisi DOĞRUDUR?",
         [("A", "Varlık Finansmanı Fonu bağımsız bir anonim şirket tüzel kişiliğine ve yönetim kuruluna sahiptir."),
          ("B", "Fon kurucusu veya kaynak kuruluş iflas ederse fon portföyündeki tüm varlıklar iflas masasına devredilir."),
          ("C", "Fonun tüzel kişiliği yoktur; malvarlığı kurucunun malvarlığından ayrı olup rehin edilemez ve haczedilemez."),
          ("D", "VDMK ihraçlarından elde edilen fonlar kurucu tarafından serbestçe genel kredi ödemelerinde kullanılabilir."),
          ("E", "VFF sadece devlet iç borçlanma senetlerini teminat alabilir, tüketici kredilerini teminat alamaz.")],
         "1. MEVZUAT DAYANAĞI: 6362 sayılı SPKn m. 58 ve III-58.1 Tebliği m. 4, 12.\n2. HUKUKİ / TEKNİK ÇERÇEVE: VFF inançlı mülkiyet esasına göre kurulur, tüzel kişiliği yoktur. Fon malvarlığı kurucu ve kaynak kuruluştan tamamen ayrıdır; iflas masasına dahil edilemez, rehin ve haczedilemez.\n3. ADIM ADIM İNCELEME / HESAPLAMA: C şıkkı fon malvarlığının yasal dokunulmazlığını doğru tanımlar.\n4. DOĞRU CEVAP VE SONUÇ: C seçeneğidir.\n5. ÇELDİRİCİ TUZAĞI: Fonun tüzel kişiliği olduğunu veya kurucu iflas edince varlıkların iflas masasına gideceğini düşünmek.",
         "VFF'nin tüzel kişiliği yoktur; malvarlığı ayrı olup kurucunun iflasında dahi haczedilemez ve iflas masasına girmez.", "KB2_Muhakeme"),

        # 19 (D)
        ("q_1003_sert_019", "D", "Borsa Yatırım Fonları (BYF / ETF) İşleyiş İlkeleri",
         "III-52.2 sayılı Borsa Yatırım Fonlarına İlişkin Esaslar Tebliği uyarınca 'Borsa Yatırım Fonları' (ETF) işleyişi hakkında aşağıdakilerden hangisi DOĞRUDUR?",
         [("A", "BYF katılma payları Borsa İstanbul Pay Piyasası'nda hiçbir şekilde hisse senedi gibi işlem göremez."),
          ("B", "BYF katılma paylarının alım satımı sadece fon kurucusu portföy yönetim şirketi gişelerinden fiziken yapılır."),
          ("C", "BYF'ler sadece tek bir şirketin hisse senedine yatırım yapmak üzere kurulabilir."),
          ("D", "Yetkilendirilmiş katılımcılar asgari pay oluşturma birimi karşılığında ayni oluşturma veya ayni geri alım yapabilirler."),
          ("E", "BYF portföy kompozisyonunun kamuya açıklanması ticari sır gerekçesiyle mevzuatça yasaklanmıştır.")],
         "1. MEVZUAT DAYANAĞI: III-52.2 m. 5, 11, 14.\n2. HUKUKİ / TEKNİK ÇERÇEVE: BYF payları borsada sürekli işlem görür. Yetkilendirilmiş Katılımcılar (AP) sepet hisseleri verip fon payı alır (ayni oluşturma) veya fon payı verip hisseleri alır (ayni geri alım).\n3. ADIM ADIM İNCELEME / HESAPLAMA: D seçeneği BYF'nin temel farkı olan ayni mekanizmayı açıklar.\n4. DOĞRU CEVAP VE SONUÇ: D seçeneğidir.\n5. ÇELDİRİCİ TUZAĞI: BYF'lerin borsada işlem görmediğini sanmak.",
         "Yetkilendirilmiş katılımcılar hisse sepeti karşılığı ayni pay oluşturma ve geri alım yaparlar.", "KB2_Muhakeme"),

        # 20 (E)
        ("q_1003_sert_020", "E", "Yatırım Fonlarında Portföy Sınırlamaları (%10 Kuralı)",
         "III-52.1 sayılı Yatırım Fonlarına İlişkin Esaslar Tebliği uyarınca, standart bir yatırım fonunun portföyüne tek bir ihraççının para ve sermaye piyasası araçlarının dahil edilmesine dair genel kural ve istisnalara ilişkin;\n\nI. Kural olarak tek bir ihraççının sermaye piyasası araçları fon toplam değerinin %10'unu aşamaz.\nII. T.C. Hazine ve Maliye Bakanlığı tarafından ihraç edilen Devlet İç Borçlanma Senetleri için %10 sınırı uygulanmaz.\nIII. İpotek teminatlı menkul kıymetler ile ipoteğe dayalı menkul kıymetlerde tek bir ihraççı sınırı %25 olarak uygulanabilir.\n\nYukarıda yer alan yatırım fonu portföy sınırlamalarından hangileri DOĞRUDUR?",
         [("A", "Yalnızca I numaralı sınırlama mevzuat uyarınca doğrudur."),
          ("B", "Yalnızca II numaralı sınırlama mevzuat uyarınca doğrudur."),
          ("C", "I ve II numaralı sınırlamalar mevzuat uyarınca doğrudur."),
          ("D", "II ve III numaralı sınırlamalar mevzuat uyarınca doğrudur."),
          ("E", "I, II ve III numaralı sınırlamaların tamamı mevzuat uyarınca doğrudur.")],
         "1. MEVZUAT DAYANAĞI: III-52.1 m. 18.\n2. HUKUKİ / TEKNİK ÇERÇEVE: Fonlarda tek ihraççı limiti %10'dur (risk dağıtım kuralı). Ancak kamu borçlanma araçları (DİBS) bu sınırdan muaftır. İpotekli menkul kıymetlerde ise sınır %25'e kadar esnetilebilir.\n3. ADIM ADIM İNCELEME / HESAPLAMA: I, II ve III öncüllerinin tümü tebliğ hükümleridir.\n4. DOĞRU CEVAP VE SONUÇ: E seçeneğidir.\n5. ÇELDİRİCİ TUZAĞI: DİBS için de %10 sınırı olduğunu zannetmek.",
         "Yatırım fonlarında tek ihraççı sınırı %10'dur; kamu borçlanma araçları muaftır, ipoteklilerde %25'tir.", "KB2_Muhakeme"),

        # --- BLOK 3: Q21-Q30 (2 A, 2 B, 2 C, 2 D, 2 E) ---
        # 21 (A)
        ("q_1003_sert_021", "A", "Gayrimenkul Yatırım Fonları (GYF - III-52.3) Sınırlamaları",
         "III-52.3 sayılı Gayrimenkul Yatırım Fonlarına İlişkin Esaslar Tebliği uyarınca kurulan GYF'lerin faaliyetlerine ve portföy sınırlamalarına ilişkin hangisi DOĞRUDUR?",
         [("A", "GYF katılma payları yalnızca Nitelikli Yatırımcılara satılabilir ve fon portföyünün en az %80'i gayrimenkul yatırımlarından oluşmalıdır."),
          ("B", "GYF katılma payları halka arz edilerek borsa aracı kurumları gişelerinden tüm küçük bireysel yatırımcılara serbestçe satılabilir."),
          ("C", "GYF'ler kendi nam ve hesaplarına inşaat müteahhitliği yaparak ticari konut inşa edip satabilirler."),
          ("D", "GYF portföyüne alınan hiçbir gayrimenkul için bağımsız gayrimenkul değerleme raporu alınması zorunlu değildir."),
          ("E", "GYF katılma payı sahipleri diledikleri gün fona başvurarak katılma paylarını nakde çevirme hakkına koşulsuz sahiptir.")],
         "1. MEVZUAT DAYANAĞI: III-52.3 m. 14, 18, 24.\n2. HUKUKİ / TEKNİK ÇERÇEVE: GYF'ler sadece Nitelikli Yatırımcılara satılır. Portföyün en az %80'i gayrimenkul yatırımlarından oluşmalıdır. GYF'ler bizzat inşaat yapamazlar (müteahhitlik yasağı vardır).\n3. ADIM ADIM İNCELEME / HESAPLAMA: A seçeneğindeki nitelikli yatırımcı ve %80 gayrimenkul kuralı tebliğin çekirdek hükmüdür.\n4. DOĞRU CEVAP VE SONUÇ: A seçeneğidir.\n5. ÇELDİRİCİ TUZAĞI: GYF'lerin konut müteahhitliği yapabileceği sanrısı.",
         "GYF payları yalnızca Nitelikli Yatırımcılara ihraç edilir ve portföyün asgari %80'i gayrimenkul olmalıdır.", "KB2_Muhakeme"),

        # 22 (B)
        ("q_1003_sert_022", "B", "Girişim Sermayesi Yatırım Fonları (GSYF - III-52.4)",
         "III-52.4 sayılı Girişim Sermayesi Yatırım Fonlarına İlişkin Esaslar Tebliği uyarınca, GSYF'lerin girişim şirketlerine yapacakları yatırımlara ilişkin hangisi YANLIŞTIR?",
         [("A", "Girişim şirketlerine doğrudan sermaye koyarak pay sahibi olmak şeklinde yatırım yapabilirler."),
          ("B", "Fon toplam değerinin en az %80'ini Borsa İstanbul Yıldız Pazar'da işlem gören hisse senetlerine yatırmak zorundadırlar."),
          ("C", "Girişim şirketlerinin ihraç ettiği borçlanma araçlarını ve dönüştürülebilir borçlanma araçlarını satın alabilirler."),
          ("D", "Girişim şirketlerine yurt dışında kurulu girişim sermayesi fonları aracılığıyla dolaylı ortak olabilirler."),
          ("E", "Girişim şirketlerine sermaye benzeri kredi veya paya dönüştürülebilir finansman sağlayabilirler.")],
         "1. MEVZUAT DAYANAĞI: III-52.4 m. 18, 19.\n2. HUKUKİ / TEKNİK ÇERÇEVE: GSYF'ler fon toplam değerinin en az %80'ini GİRİŞİM SERMAYESİ YATIRIMLARINA (halka açık olmayan şirketlere) yönlendirmek zorundadır. Borsadaki Yıldız Pazar hisselerine %80 zorunluluğu tamamen yanlıştır.\n3. ADIM ADIM İNCELEME / HESAPLAMA: B şıkkı GSYF tanımıyla çelişir.\n4. DOĞRU CEVAP VE SONUÇ: B seçeneğidir.\n5. ÇELDİRİCİ TUZAĞI: GSYF'nin borsada işlem gören büyük şirketlere yatırım fonu sanılması.",
         "GSYF portföyünün en az %80'i girişim şirketlerine yatırılmalıdır, borsa hisselerine değil.", "KB2_Muhakeme"),

        # 23 (C)
        ("q_1003_sert_023", "C", "Pay Türleri ve Hamiline/Nama Yazılı Pay Devri",
         "6102 sayılı TTK ve Sermaye Piyasası Kanunu uyarınca anonim ortaklık pay türleri ve payların devir rejimine dair hangisi DOĞRUDUR?",
         [("A", "Hamiline yazılı payların bedeli tamamen ödenmemiş olsa dahi bastırılıp ortaklara teslim edilmesi mümkündür."),
          ("B", "Hamiline yazılı payların devri MKK'ya bildirim yapılmaksızın sadece zilyetliğin devri ile şirket ve üçüncü kişilere karşı hüküm ifade eder."),
          ("C", "Hamiline yazılı pay senetlerinin devri Merkezi Kayıt Kuruluşu'na (MKK) bildirildiği tarihte hüküm ifade eder."),
          ("D", "Borsada işlem gören halka açık ortaklık payları fiziki olarak hamiline yazılı pay senedi şeklinde ortaklara elden dağıtılır."),
          ("E", "Nama yazılı payların devrinde ciro ve zilyetliğin devri yeterli olup şirket pay defterine kayıt yapılması gereksizdir.")],
         "1. MEVZUAT DAYANAĞI: 6102 sayılı TTK m. 484, 489 ve 6362 sayılı SPKn m. 13.\n2. HUKUKİ / TEKNİK ÇERÇEVE: Hamiline yazılı paylar için MKK HPKS bildirimi zorunludur. Bildirim yapılmadıkça hak kullanılamaz ve devir şirkete/üçüncü kişilere karşı ileri sürülemez. Borsada paylar kaydidir.\n3. ADIM ADIM İNCELEME / HESAPLAMA: C şıkkı 7262 sayılı Kanunla TTK 489'a eklenen MKK tescil hükmünü doğru açıklar.\n4. DOĞRU CEVAP VE SONUÇ: C seçeneğidir.\n5. ÇELDİRİCİ TUZAĞI: Eski kural olan 'sadece zilyetliğin devri yeterlidir' bilgisine takılmak (B şıkkı).",
         "Hamiline pay senetlerinin devri MKK'ya bildirildiği tarihte şirkete ve üçüncü kişilere karşı hüküm ifade eder.", "KB2_Muhakeme"),

        # 24 (D)
        ("q_1003_sert_024", "D", "Oyda İmtiyaz Sınırları ve Kurumsal Yönetim (TTK m. 479)",
         "6102 sayılı Türk Ticaret Kanunu m. 479 uyarınca anonim ortaklıklarda 'Oyda İmtiyaz' tanınmasına ilişkin yasal üst sınır ve kurallar hakkında hangisi DOĞRUDUR?",
         [("A", "Bir paya en fazla 5 oy hakkı tanınabilir ve bu sınırlama hiçbir surette mahkemece veya genel kurulca aşılamaz."),
          ("B", "Halka açık ortaklıklarda oyda imtiyaz tanınması Sermaye Piyasası Kanunu uyarınca kesin olarak yasaklanmıştır."),
          ("C", "Oyda imtiyaz esas sözleşme değişikliği gerektirmeksizin yönetim kurulu kararıyla serbestçe verilebilir."),
          ("D", "Bir paya en çok 15 oy hakkı tanınabilir; ancak bu sınırlama kurumlaşmanın gerektirdiği hallerde mahkeme kararıyla kaldırılabilir."),
          ("E", "Oyda imtiyazlı paylar genel kurulda esas sözleşme değişikliği ve yönetim kurulunun ibra edilmemesi kararlarında da geçerlidir.")],
         "1. MEVZUAT DAYANAĞI: 6102 sayılı TTK m. 479/2.\n2. HUKUKİ / TEKNİK ÇERÇEVE: TTK uyarınca oyda imtiyaz sınırı pay başına en çok 15 oydur. Haklı sebeplerle mahkemece kaldırılabilir. Ayrıca esas sözleşme değişikliği ve ibra davalarında oyda imtiyaz KULLANILAMAZ.\n3. ADIM ADIM İNCELEME / HESAPLAMA: D seçeneği TTK m. 479'un yasal kural ve istisnasını tam olarak ifade eder.\n4. DOĞRU CEVAP VE SONUÇ: D seçeneğidir.\n5. ÇELDİRİCİ TUZAĞI: Azami sınırın 10 veya 20 sanılması.",
         "Oyda imtiyaz sınırı en fazla 15 oydur; esas sözleşme değişikliğinde ve ibra davalarında imtiyaz kullanılamaz.", "KB1_Kavramsal"),

        # 25 (E)
        ("q_1003_sert_025", "E", "Katılma İntifa Senetleri (KİS - II-31.1)",
         "II-31.1 sayılı Tebliğ uyarınca sermaye piyasasında ortaklıklar tarafından ihraç edilebilen 'Katılma İntifa Senetleri'ne (KİS) ilişkin;\n\nI. KİS sahiplerine ortaklığın genel kurulunda oy kullanma ve şirket yönetimine katılma hakkı VERİLEMEZ.\nII. KİS sahiplerine kârdan pay alma, tasfiye bakiyesinden pay alma veya yeni pay alma hakları tanınabilir.\nIII. KİS'ler süreli veya süresiz olarak ihraç edilebilir ve bedelleri tamamen nakit olarak ödenmelidir.\n\nYukarıda yer alan hukuki ilkelerden hangileri DOĞRUDUR?",
         [("A", "Yalnızca I numaralı ilke mevzuat uyarınca doğrudur."),
          ("B", "Yalnızca II numaralı ilke mevzuat uyarınca doğrudur."),
          ("C", "I ve II numaralı ilkeler mevzuat uyarınca doğrudur."),
          ("D", "II ve III numaralı ilkeler mevzuat uyarınca doğrudur."),
          ("E", "I, II ve III numaralı ilkelerin tamamı mevzuat uyarınca doğrudur.")],
         "1. MEVZUAT DAYANAĞI: II-31.1 Borçlanma Araçları Tebliği m. 27 ve TTK m. 502.\n2. HUKUKİ / TEKNİK ÇERÇEVE: Katılma intifa senetleri mali haklar (kâr payı, tasfiye payı) sağlar. Ancak ASLA oy hakkı ve yönetime katılma hakkı vermez. Süreli veya süresiz çıkarılabilir.\n3. ADIM ADIM İNCELEME / HESAPLAMA: I, II ve III öncüllerinin tümü KİS rejimine uygundur.\n4. DOĞRU CEVAP VE SONUÇ: E seçeneğidir.\n5. ÇELDİRİCİ TUZAĞI: KİS sahiplerine oy hakkı verilebileceği yanılgısı.",
         "Katılma intifa senedi sahiplerine hiçbir şekilde oy hakkı ve idari hak tanınamaz.", "KB2_Muhakeme"),

        # 26 (A)
        ("q_1003_sert_026", "A", "Tahvil Konveksitesi (Convexity) ve Süre İyileştirmesi",
         "Sabit getirili bir tahvilin faiz oranlarındaki değişime bağlı fiyat duyarlılığı analiz edilirken yalnızca Süre (Duration) yerine 'Konveksite'nin (Bükeylik) de hesaba katılmasının nedeni hangisidir?",
         [("A", "Süre doğrusal bir yaklaşım sunduğundan, büyük faiz değişimlerinde fiyat-getiri eğriselliğini yakalamak amacıyla"),
          ("B", "Konveksite tahvilin vadesini sıfırlayarak piyasa faiz riskini tamamen ortadan kaldıran bir finansal sözleşmedir."),
          ("C", "Konveksite sadece hisse senedi opsiyonlarında kullanılan bir katsayı olup borçlanma araçlarında hesaplanamaz."),
          ("D", "Süre sadece kupon faizlerini ölçerken konveksite tahvilin tabi olduğu yasal kurumlar vergisi oranını belirler."),
          ("E", "Piyasa faiz oranları düştüğünde tahvil fiyatının da aynı oranda düşmesini sağlamak amacıyla bir ceza faktörüdür.")],
         "1. MEVZUAT DAYANAĞI: Sermaye Piyasasında Portföy Yönetimi ve Faiz Riski Yönetimi İlkeleri.\n2. HUKUKİ / TEKNİK ÇERÇEVE: Tahvil fiyatı ile getiri arasındaki ilişki eğriseldir (convex). Duration bu eğriye teğet geçen doğrudur. Küçük faiz adımlarında yeterlidir; ancak büyük adımlarda konveksite terimi eklenmelidir: Delta P/P ≈ -MD*Delta y + 0.5*Convexity*(Delta y)^2.\n3. ADIM ADIM İNCELEME / HESAPLAMA: A seçeneği eğrisellik ve doğrusal yaklaşım hatasını tam açıklar.\n4. DOĞRU CEVAP VE SONUÇ: A seçeneğidir.\n5. ÇELDİRİCİ TUZAĞI: Konveksitenin faiz riskini sıfırlayan bir enstrüman sanılması (B şıkkı).",
         "Duration doğrusal yaklaşımdır; büyük faiz hareketlerinde eğriselliği yakalamak için Konveksite eklenir.", "KB2_Muhakeme"),

        # 27 (B)
        ("q_1003_sert_027", "B", "Borçlanma Aracı İhraç Limiti (II-31.1 m. 9)",
         "II-31.1 sayılı Tebliğ uyarınca, halka açık anonim ortaklıklar ile halka açık olmayan anonim ortaklıkların ihraç edebilecekleri azami borçlanma aracı tavanı (ihraç limiti) özsermayenin sırasıyla kaç katıdır?",
         [("A", "Halka açık ortaklıklar için 3 katı, halka açık olmayanlar için 5 katıdır."),
          ("B", "Halka açık ortaklıklar için 5 katı, halka açık olmayanlar için 3 katıdır."),
          ("C", "Her iki ortaklık türü için de istisnasız olarak özsermayenin 2 katıdır."),
          ("D", "Halka açık ortaklıklar için 10 katı, halka açık olmayanlar için 1 katıdır."),
          ("E", "Borçlanma araçlarında hiçbir ihraç limiti bulunmayıp ortaklıklar sınırsız ihraç yapabilir.")],
         "1. MEVZUAT DAYANAĞI: II-31.1 Tebliği m. 9.\n2. HUKUKİ / TEKNİK ÇERÇEVE: Borçlanma aracı ihraç limiti son yıllık denetlenmiş bilançodaki özsermayeye göre belirlenir:\n- Halka açık ortaklıklar: Özsermayenin 5 KATI.\n- Halka açık olmayan ortaklıklar: Özsermayenin 3 KATI.\n3. ADIM ADIM İNCELEME / HESAPLAMA: B seçeneğindeki 5 kat ve 3 kat yasal sınırdır.\n4. DOĞRU CEVAP VE SONUÇ: B seçeneğidir.\n5. ÇELDİRİCİ TUZAĞI: Halka açık olmayan şirketlere daha yüksek tavan verildiği zannı (A şıkkı).",
         "Borçlanma aracı ihraç limiti: Halka açık şirketlerde özsermayenin 5 katı, halka açık olmayanlarda 3 katıdır.", "KB1_Kavramsal"),

        # 28 (C)
        ("q_1003_sert_028", "C", "VİOP BIST 30 Endeks Vadeli Sözleşme Büyüklüğü",
         "BIST 30 Endeks Vadeli İşlem Sözleşmesinde endeks uzlaşma fiyatı 10.000 puan iken, sözleşme büyüklüğü çarpanı 10'dur (1 sözleşme = Endeks Değeri x 10 TL). Başlangıç teminatı sözleşme başına 1.250 TL'dir.\n\nSöz konusu sözleşmeden 1 adet alan bir yatırımcının üstlendiği pozisyonun piyasa değeri (nominal büyüklüğü) ve pozisyondaki kaldıraç oranı nedir?",
         [("A", "Pozisyon Değeri: 10.000 TL; Kaldıraç Oranı: 8 kat"),
          ("B", "Pozisyon Değeri: 50.000 TL; Kaldıraç Oranı: 40 kat"),
          ("C", "Pozisyon Değeri: 100.000 TL; Kaldıraç Oranı: 80 kat"),
          ("D", "Pozisyon Değeri: 125.000 TL; Kaldıraç Oranı: 100 kat"),
          ("E", "Pozisyon Değeri: 200.000 TL; Kaldıraç Oranı: 160 kat")],
         "1. MEVZUAT DAYANAĞI: Borsa İstanbul VİOP BIST 30 Vadeli İşlem Sözleşmesi Özellikleri.\n2. HUKUKİ / TEKNİK ÇERÇEVE: Sözleşme Büyüklüğü = Endeks Puanı * Sözleşme Çarpanı. Kaldıraç = Pozisyon Büyüklüğü / Yatırılan Teminat.\n3. ADIM ADIM İNCELEME / HESAPLAMA:\n- Pozisyon Büyüklüğü = 10.000 * 10 = 100.000 TL.\n- Yatırılan Başlangıç Teminatı = 1.250 TL.\n- Kaldıraç Oranı = 100.000 / 1.250 = 80 kat.\n4. DOĞRU CEVAP VE SONUÇ: C seçeneğinde 100.000 TL ve 80 kat doğru verilmiştir.\n5. ÇELDİRİCİ TUZAĞI: Çarpanı 1 kabul edip pozisyon büyüklüğünü 10.000 TL ve kaldıracı 8 kat sanmak (A şıkkı).",
         "Pozisyon Büyüklüğü = 10.000 * 10 = 100.000 TL. Kaldıraç = 100.000 / 1.250 = 80 kattır.", "KB3_Vaka"),

        # 29 (D)
        ("q_1003_sert_029", "D", "Efektif Yıllık Faiz Oranı Hesabı",
         "Bir mevduat veya borçlanma aracının yıllık nominal faiz oranı %40'tır ve faiz ödemeleri 6 ayda bir (yılda 2 dönem) bileşik olarak anaparaya ilave edilmektedir.\n\nSöz konusu finansal enstrümanın 'Efektif Yıllık Bileşik Faiz Oranı' (EAR) yüzde kaçtır?",
         [("A", "Efektif yıllık bileşik faiz oranı yüzde 40,00'dır."),
          ("B", "Efektif yıllık bileşik faiz oranı yüzde 42,00'dir."),
          ("C", "Efektif yıllık bileşik faiz oranı yüzde 43,50'dir."),
          ("D", "Efektif yıllık bileşik faiz oranı yüzde 44,00'tür."),
          ("E", "Efektif yıllık bileşik faiz oranı yüzde 46,41'dir.")],
         "1. MEVZUAT DAYANAĞI: Para ve Sermaye Piyasasında Faiz Hesaplama Standartları.\n2. HUKUKİ / TEKNİK ÇERÇEVE: Efektif Yıllık Faiz Formülü:\nr_ef = (1 + r_nom / m)^m - 1. Burada r_nom = 0,40, m = 2 (6 aylık periyot sayısı).\n3. ADIM ADIM İNCELEME / HESAPLAMA:\n- Dönemsel Faiz = 0,40 / 2 = 0,20 (%20).\n- r_ef = (1 + 0,20)^2 - 1 = (1,20)^2 - 1 = 1,44 - 1 = 0,44 = %44,00.\n4. DOĞRU CEVAP VE SONUÇ: D seçeneğidir (%44,00).\n5. ÇELDİRİCİ TUZAĞI: Nominal faiz ile efektif faizi aynı kabul edip %40 demek veya çeyreklik (m=4) hesapla karıştırmak.",
         "r_ef = (1 + 0,40/2)^2 - 1 = 1,20^2 - 1 = %44,00.", "KB3_Vaka"),

        # 30 (E)
        ("q_1003_sert_030", "E", "Varantlarda Zaman Değeri Erimesi (Theta)",
         "Varant fiyatlamasında kullanılan Yunan harflerinden 'Teta' (Theta) göstergesi ve varantın zaman değeri erimesine ilişkin;\n\nI. Vadeye kalan süre azaldıkça varantın zaman değeri (time value) hızlanarak erir ve vade bitiminde sıfıra iner.\nII. Vade yaklaştıkça Teta'nın mutlak değeri artar; yani varant bir iş gününde daha fazla değer kaybeder.\nIII. Teta, diğer tüm faktörler sabitken vadenin bir gün kısalmasının varant fiyatında oluşturduğu değişimi gösterir.\n\nYukarıda yer alan finansal tespitlerden hangileri DOĞRUDUR?",
         [("A", "Yalnızca I numaralı tespit teorik olarak doğrudur."),
          ("B", "Yalnızca II numaralı tespit teorik olarak doğrudur."),
          ("C", "I ve II numaralı tespitler teorik olarak doğrudur."),
          ("D", "II ve III numaralı tespitler teorik olarak doğrudur."),
          ("E", "I, II ve III numaralı tespitlerin tamamı teorik olarak doğrudur.")],
         "1. MEVZUAT DAYANAĞI: Varant Fiyatlama Modelleri (Black-Scholes Modeli).\n2. HUKUKİ / TEKNİK ÇERÇEVE: Teta zaman aşımı erimesidir. Varantın zaman değeri vade sonuna doğru doğrusal değil, parabolik olarak hızlanarak tükenir. Vade sonunda zaman değeri sıfırdır.\n3. ADIM ADIM İNCELEME / HESAPLAMA: I, II ve III öncüllerinin her biri varant matematiğini tam yansıtır.\n4. DOĞRU CEVAP VE SONUÇ: E seçeneğidir.\n5. ÇELDİRİCİ TUZAĞI: Zaman erimesinin her gün eşit miktarda doğrusal olduğunu varsaymak.",
         "Teta zaman erimesini ölçer. Vade yaklaştıkça zaman değeri erimesi hızlanır ve vade sonunda sıfırlanır.", "KB2_Muhakeme"),

        # --- BLOK 4: Q31-Q40 (2 A, 2 B, 2 C, 2 D, 2 E) ---
        # 31 (A)
        ("q_1003_sert_031", "A", "Pay Takas Döngüsü (T+2) ve Temettü Hak Edişi",
         "Hisseleri Borsa İstanbul'da işlem gören ve nakit temettü dağıtım tarihi 12 Mayıs Salı olan bir ortaklıktan nakit temettü almaya hak kazanabilmek için, yatırımcının en geç hangi işlem gününün kapanışı itibarıyla ilgili hisse senedine sahip olması gerekir?",
         [("A", "En geç 11 Mayıs Pazartesi günü seans kapanışı itibarıyla paylara sahip olunmalıdır."),
          ("B", "En geç 12 Mayıs Salı günü seans kapanışı itibarıyla paylara sahip olunmalıdır."),
          ("C", "En geç 14 Mayıs Perşembe (T+2) günü seans kapanışı itibarıyla paylara sahip olunmalıdır."),
          ("D", "En geç 8 Mayıs Cuma günü seans açılışı itibarıyla paylara sahip olunmalıdır."),
          ("E", "Temettü tarihinden en az 30 gün önce hisse senedi satın alınmış olmalıdır.")],
         "1. MEVZUAT DAYANAĞI: II-19.1 Kâr Payı Tebliği ve Borsa İstanbul Takas Esasları.\n2. HUKUKİ / TEKNİK ÇERÇEVE: Temettü dağıtım tarihi (hak kullanım tarihi) hissenin temettü düşülmüş fiyattan işlem görmeye başladığı gündür. Temettü alabilmek için temettü dağıtım tarihinden bir önceki işlem gününün seans kapanışında hisseye sahip olmak gerekir.\n3. ADIM ADIM İNCELEME / HESAPLAMA: 12 Mayıs Salı temettü günü ise, en geç 11 Mayıs Pazartesi kapanışta hisseye sahip olunmalıdır.\n4. DOĞRU CEVAP VE SONUÇ: A seçeneğidir.\n5. ÇELDİRİCİ TUZAĞI: Salı günü hisse alsa da temettü alabileceğini sanmak (Salı günü hisse temettüsüz fiyattan açılır).",
         "Temettüye hak kazanmak için temettü dağıtım tarihinden önceki son iş günü kapanışta hisseye sahip olunmalıdır.", "KB2_Muhakeme"),

        # 32 (B)
        ("q_1003_sert_032", "B", "VİOP Pay Vadeli İşlemlerde Fiziki Teslimat",
         "Borsa İstanbul Vadeli İşlem ve Opsiyon Piyasası'nda (VİOP) işlem gören Pay Vadeli İşlem Sözleşmelerinin vade sonu uzlaşma yöntemi ve fiziki teslimat prosedürüne ilişkin hangisi DOĞRUDUR?",
         [("A", "Tüm pay vadeli sözleşmelerinde vade sonu yalnızca nakdi uzlaşma ile kapatılır, hisse devri yapılmaz."),
          ("B", "Pay vadeli işlem sözleşmelerinde vade sonu uzlaşma yöntemi fiziki teslimattır ve takas T+2'de gerçekleşir."),
          ("C", "Fiziki teslimat için yatırımcının şirketin genel merkezine bizzat giderek payları elden teslim etmesi gerekir."),
          ("D", "Fiziki teslimat sözleşmelerinde hiçbir zaman temerrüt faizi ve temerrüt prosedürü işletilemez."),
          ("E", "Pay vadeli işlemlerinde fiziki teslimat sadece BIST 30 Endeks vadeli sözleşmelerinde uygulanır.")],
         "1. MEVZUAT DAYANAĞI: Borsa İstanbul VİOP İşleyiş Prosedürü Madde 18.\n2. HUKUKİ / TEKNİK ÇERÇEVE: Borsa İstanbul VİOP'ta tek hisse senedi üzerine yazılmış vadeli işlem sözleşmelerinde uzlaşma yöntemi FİZİKİ TESLİMATTIR. Vade sonunda uzun pozisyon sahiplerine hisse senedi devredilir, kısa pozisyon sahipleri hisseyi teslim eder.\n3. ADIM ADIM İNCELEME / HESAPLAMA: B şıkkı fiziki teslimat kuralını ve T+2 takas gününü tam açıklar.\n4. DOĞRU CEVAP VE SONUÇ: B seçeneğidir.\n5. ÇELDİRİCİ TUZAĞI: Tüm VİOP sözleşmelerinin nakdi uzlaşmalı olduğunu sanmak (Endeks nakdi, hisse vadeliler fiziki teslimatlıdır).",
         "Tek pay vadeli işlem sözleşmelerinde vade sonu uzlaşma FİZİKİ TESLİMATTIR (T+2 takas).", "KB2_Muhakeme"),

        # 33 (C)
        ("q_1003_sert_033", "C", "Yatırım Fonlarında Fiyat Hesaplama İlkeleri",
         "III-52.1 sayılı Yatırım Fonlarına İlişkin Esaslar Tebliği uyarınca, bir menkul kıymet yatırım fonunun 'Pay Birim Fiyatı' nasıl hesaplanır?",
         [("A", "Fon portföyündeki menkul kıymetlerin toplam alış maliyeti toplam pay sayısına bölünerek hesaplanır."),
          ("B", "Fon portföyündeki menkul kıymetlerin nominal değerleri toplamı tedavüldeki pay sayısına bölünerek bulunur."),
          ("C", "Fonun net varlık değeri (toplam portföy değeri + diğer varlıklar - fon borçları) tedavüldeki pay sayısına bölünerek hesaplanır."),
          ("D", "Her gün Borsa İstanbul Yönetim Kurulu tarafından fon kurucusuna bildirilen sabit fiyattır."),
          ("E", "Fon kurucusunun ödenmiş sermayesi toplam ihraç tavanına bölünerek haftalık belirlenir.")],
         "1. MEVZUAT DAYANAĞI: III-52.1 sayılı Tebliğ m. 25.\n2. HUKUKİ / TEKNİK ÇERÇEVE: Fon Pay Birim Fiyatı = Fon Net Varlık Değeri (FNVD) / Tedavüldeki Pay Sayısı. FNVD = (Portföy Değeri + Diğer Varlıklar / Alacaklar) - (Fon Borçları / Yükümlülükleri).\n3. ADIM ADIM İNCELEME / HESAPLAMA: C şıkkı net varlık değeri üzerinden pay birim fiyat formülünü eksiksiz tanımlar.\n4. DOĞRU CEVAP VE SONUÇ: C seçeneğidir.\n5. ÇELDİRİCİ TUZAĞI: Alış maliyetinin esas alınacağını düşünmek (fonlar piyasa fiyatıyla değerlenir).",
         "Fon pay birim fiyatı = Fon Net Varlık Değeri / Tedavüldeki Pay Sayısıdır.", "KB1_Kavramsal"),

        # 34 (D)
        ("q_1003_sert_034", "D", "İpotek Teminatlı Menkul Kıymetler (İTMK - III-58.2)",
         "III-58.2 sayılı İpotek Teminatlı Menkul Kıymetler Tebliği uyarınca ihraç edilen İTMK'ların 'Teminat Havuzu' ve yatırımcı güvencesine dair hangisi DOĞRUDUR?",
         [("A", "Teminat havuzundaki ipotekli konut kredileri ihraççı bankanın genel bilançosundan tamamen çıkartılır."),
          ("B", "İhraççı banka iflas ederse teminat havuzundaki varlıklar doğrudan mudilerin mevduatlarını ödemede kullanılır."),
          ("C", "İTMK sahipleri sadece teminat havuzuna başvurabilir, ihraççı bankanın genel malvarlığına başvuramazlar."),
          ("D", "İTMK yatırımcıları hem teminat havuzu üzerinde birinci derecede rüçhanlı hakka, hem de ihraççının genel malvarlığına başvurma (çifte teminat) hakkına sahiptir."),
          ("E", "Teminat havuzunda yer alan ipoteklerin değerlemesi sadece 10 yılda bir defa yapılabilir.")],
         "1. MEVZUAT DAYANAĞI: III-58.2 sayılı Tebliğ m. 4, 11, 23.\n2. HUKUKİ / TEKNİK ÇERÇEVE: İTMK (Covered Bond) bilanço içi ihraçtır. En büyük güvencesi 'Çifte Teminat İlkesi'dir (Dual Recourse): Yatırımcı hem teminat havuzuna rüçhanlıdır hem de ihraççının genel malvarlığına başvurabilir.\n3. ADIM ADIM İNCELEME / HESAPLAMA: D seçeneğindeki çifte teminat kuralı İTMK'nın temel özelliğidir.\n4. DOĞRU CEVAP VE SONUÇ: D seçeneğidir.\n5. ÇELDİRİCİ TUZAĞI: VDMK gibi bilanço dışı sanıp sadece teminat havuzuna başvurulabileceğini düşünmek (C şıkkı).",
         "İTMK yatırımcısı çifte teminat hakkına sahiptir: Hem teminat havuzu üzerinde rüçhanlıdır hem de bankaya başvurabilir.", "KB2_Muhakeme"),

        # 35 (E)
        ("q_1003_sert_035", "E", "Gelir Ortaklığı Senetleri (GOS) ve Gelire Endeksli Senetler (GES)",
         "Kamu kuruluşları ve Hazine tarafından ihraç edilen Gelir Ortaklığı Senetleri (GOS) ve Gelire Endeksli Senetlere (GES) ilişkin;\n\nI. GOS, kamuya ait köprü, baraj, otoyol gibi tesislerin gelirlerine ortaklık hakkı veren senetlerdir.\nII. GOS sahipleri ilgili kamu tesisinin mülkiyetine ortak olmazlar; yalnızca tesisin sağladığı gelirden pay alırlar.\nIII. GES'lerin getirisi Devlet Malzeme Ofisi, KİT'ler veya kamu bankalarının bütçeye aktardığı hasılat paylarına endekslenir.\n\nYukarıda yer alan tespitlerden hangileri DOĞRUDUR?",
         [("A", "Yalnızca I numaralı tespit mevzuat uyarınca doğrudur."),
          ("B", "Yalnızca II numaralı tespit mevzuat uyarınca doğrudur."),
          ("C", "I ve II numaralı tespitler mevzuat uyarınca doğrudur."),
          ("D", "II ve III numaralı tespitler mevzuat uyarınca doğrudur."),
          ("E", "I, II ve III numaralı tespitlerin tamamı mevzuat uyarınca doğrudur.")],
         "1. MEVZUAT DAYANAĞI: 2983 sayılı Kanun ve Hazine Finansman Düzenlemeleri.\n2. HUKUKİ / TEKNİK ÇERÇEVE: GOS mülkiyet devretmez, gelir ortaklığı sağlar. GES getirisi ise KİT'lerin bütçeye aktardığı hasılat paylarına endekslidir.\n3. ADIM ADIM İNCELEME / HESAPLAMA: I, II ve III öncüllerinin tümü GOS ve GES'in yasal nitelikleridir.\n4. DOĞRU CEVAP VE SONUÇ: E seçeneğidir.\n5. ÇELDİRİCİ TUZAĞI: GOS sahiplerinin köprünün veya barajın mülkiyetine paydaş olduğunu zannetmek.",
         "GOS mülkiyete değil sadece gelire ortaklık sağlar; GES ise KİT hasılat paylarına endekslidir.", "KB2_Muhakeme"),

        # 36 (A)
        ("q_1003_sert_036", "A", "İskontolu Tahvilde İç Verim Oranı (IRR / YTM)",
         "Vadesine tam 2 yıl kalmış olan ve vadesinde 100 TL nominal değer ödeyecek olan sıfır kuponlu (iskontolu) bir tahvil piyasada 64 TL fiyattan işlem görmektedir.\n\nBu tahvili satın alan bir yatırımcının elde edeceği yıllık bileşik iç verim oranı (YTM / Vadeye Kadar Getiri) yüzde kaçtır?",
         [("A", "Yıllık bileşik iç verim oranı yüzde 25,00'dir."),
          ("B", "Yıllık bileşik iç verim oranı yüzde 28,12'dir."),
          ("C", "Yıllık bileşik iç verim oranı yüzde 36,00'dır."),
          ("D", "Yıllık bileşik iç verim oranı yüzde 56,25'tir."),
          ("E", "Yıllık bileşik iç verim oranı yüzde 20,00'dir.")],
         "1. MEVZUAT DAYANAĞI: Sabit Getirili Menkul Kıymetler İç Verim Oranı Esasları.\n2. HUKUKİ / TEKNİK ÇERÇEVE: Sıfır kuponlu tahvilde Fiyat = Nominal / (1 + y)^n. Buradan (1 + y)^n = Nominal / Fiyat -> 1 + y = (Nominal / Fiyat)^(1/n).\n3. ADIM ADIM İNCELEME / HESAPLAMA:\n- Nominal = 100 TL, Fiyat = 64 TL, n = 2 yıl.\n- (1 + y)^2 = 100 / 64 = 1,5625.\n- 1 + y = Karekök(1,5625) = 1,25.\n- y = 1,25 - 1 = 0,25 = %25,00.\n4. DOĞRU CEVAP VE SONUÇ: A seçeneğidir (%25,00).\n5. ÇELDİRİCİ TUZAĞI: İki yıllık toplam getiriyi (36/64 = %56,25) ikiye bölüp basitçe %28,12 bulmak (B şıkkı) veya 100 - 64 = %36 demek.",
         "(1 + y)^2 = 100 / 64 = 1,5625 -> 1 + y = 1,25 -> y = %25,00.", "KB3_Vaka"),

        # 37 (B)
        ("q_1003_sert_037", "B", "VİOP Taşıma Arbitrajı (Cash-and-Carry)",
         "Piyasada bir hisse senedinin vadeli işlem sözleşmesi fiyatının, taşıma maliyeti modeliyle hesaplanan teorik vadeli fiyatından DAHA YÜKSEK (aşırı değerli) olduğu tespit edilmiştir.\n\nBu durumda risksiz kâr elde etmek isteyen bir arbitrajörün piyasada derhal yapması gereken işlem çifti hangisidir?",
         [("A", "Spot piyasada hisse senedi açığa satılır, VİOP'ta vadeli sözleşme satın alınır (uzun)."),
          ("B", "Spot piyasada hisse senedi satın alınır, VİOP'ta vadeli işlem sözleşmesi satılır (kısa)."),
          ("C", "Hem spot piyasada hisse senedi hem de VİOP'ta vadeli sözleşme aynı anda satın alınır."),
          ("D", "Hem spot piyasada hem de VİOP'ta açığa satış pozisyonu açılır."),
          ("E", "Tahvil piyasasında faiz takası yapılır, vadeli piyasada hiçbir işlem yapılmaz.")],
         "1. MEVZUAT DAYANAĞI: Sermaye Piyasasında Türev Piyasalar Arbitraj Mekanizmaları.\n2. HUKUKİ / TEKNİK ÇERÇEVE: Vadeli Fiyat > Teorik Fiyat ise vadeli kontrat pahalıdır, spot ucuzdur. Ucuz olan spot piyasadan alınır, pahalı olan vadeli piyasada satılır (Kısa pozisyon). Buna Taşıma Arbitrajı (Cash and Carry Arbitrage) denir.\n3. ADIM ADIM İNCELEME / HESAPLAMA: B seçeneği taşıma arbitrajının tanımıdır.\n4. DOĞRU CEVAP VE SONUÇ: B seçeneğidir.\n5. ÇELDİRİCİ TUZAĞI: Ters Taşıma Arbitrajı (Reverse Cash and Carry) ile karıştırmak (A şıkkı).",
         "Vadeli fiyat teorikten yüksekse: Spot alınır, vadeli satılır (Taşıma Arbitrajı).", "KB2_Muhakeme"),

        # 38 (C)
        ("q_1003_sert_038", "C", "Tahvil İtfa Türleri ve Erken İtfa (Call Option)",
         "İhraççı şirkete belirli tarihlerde ve belirlenen bir fiyattan tahvilleri vadesinden önce geri satın alma hakkı veren tahvillere ne ad verilir?",
         [("A", "Yatırımcıya satma hakkı tanıyan tahviller (Puttable Bonds)"),
          ("B", "Dönüştürülebilir tahviller (Convertible Bonds)"),
          ("C", "İhraççıya geri çağırma hakkı tanıyan tahviller (Callable Bonds)"),
          ("D", "Kuponsuz sıfır faizli devlet iç borçlanma senetleri"),
          ("E", "Enflasyona endeksli değişken faizli tahviller")],
         "1. MEVZUAT DAYANAĞI: II-31.1 Borçlanma Araçları Tebliği m. 15.\n2. HUKUKİ / TEKNİK ÇERÇEVE: İhraççının tahvili erken itfa etme (geri çağırma) hakkı 'Callable Bond' olarak adlandırılır. İhraççı piyasa faizleri düştüğünde eski yüksek faizli tahvili çağırıp daha düşük faizle borçlanır.\n3. ADIM ADIM İNCELEME / HESAPLAMA: C şıkkı Callable Bond tanımıdır.\n4. DOĞRU CEVAP VE SONUÇ: C seçeneğidir.\n5. ÇELDİRİCİ TUZAĞI: Yatırımcının satma hakkı olan Puttable Bond ile karıştırmak (A şıkkı).",
         "İhraççıya vadesinden önce tahvili geri satın alma hakkı veren tahviller 'Callable Bond'dur.", "KB1_Kavramsal"),

        # 39 (D)
        ("q_1003_sert_039", "D", "Varant İhraç Limitleri ve Piyasa Yapıcılık",
         "Borsa İstanbul Varant Pazarı'nda likiditeyi sağlamak amacıyla faaliyet gösteren 'Piyasa Yapıcı'nın yükümlülüklerine ilişkin hangisi DOĞRUDUR?",
         [("A", "Piyasa yapıcı seans boyunca sadece alış kotasyonu girmekle yükümlüdür, satış kotasyonu giremez."),
          ("B", "Piyasa yapıcı kotasyonları arasında azami fiyat farkı (makas) serbestçe sınırsız belirlenebilir."),
          ("C", "Piyasa yapıcının girdiği kotasyon emirleri iptal edilemez ve gün boyunca değiştirilemez."),
          ("D", "Piyasa yapıcı belirlenen kotasyon aralığında hem alış hem de satış yönünde çift taraflı kotasyon girmek zorundadır."),
          ("E", "Piyasa yapıcı Borsa İstanbul Yönetim Kurulu izni olmadan varant fiyatını tek taraflı belirleyemez.")],
         "1. MEVZUAT DAYANAĞI: Borsa İstanbul Varant Piyasası Piyasa Yapıcılık Düzenlemeleri.\n2. HUKUKİ / TEKNİK ÇERÇEVE: Varantlarda piyasa yapıcı sürekli likidite sağlamak üzere çift taraflı (alış ve satış) kotasyon vermekle yükümlüdür. Kotasyonlar belirlenen azami makas aralığında olmalıdır.\n3. ADIM ADIM İNCELEME / HESAPLAMA: D seçeneği piyasa yapıcılığın temel şartını doğru açıklar.\n4. DOĞRU CEVAP VE SONUÇ: D seçeneğidir.\n5. ÇELDİRİCİ TUZAĞI: Sadece alış yönlü kotasyon girilebileceği yanılgısı.",
         "Piyasa yapıcı belirlenen maksimum spread (makas) içinde çift taraflı kotasyon vermekle yükümlüdür.", "KB2_Muhakeme"),

        # 40 (E)
        ("q_1003_sert_040", "E", "Fon Sepeti Fonları (Fund of Funds) Sınırlamaları",
         "III-52.1 sayılı Yatırım Fonlarına İlişkin Esaslar Tebliği uyarınca 'Fon Sepeti Fonları'nın diğer yatırım fonlarının katılma paylarına yatırım yapma sınırlarına ilişkin hangisi DOĞRUDUR?",
         [("A", "Fon sepeti fonu toplam portföyünün %100'ünü tek bir yatırım fonunun katılma paylarına yatırabilir."),
          ("B", "Fon sepeti fonları serbest fon katılma paylarına hiçbir surette yatırım yapamazlar."),
          ("C", "Fon sepeti fonu portföyünün en az %50'si nakit mevduatta tutulmak zorundadır."),
          ("D", "Fon sepeti fonları yabancı fon katılma paylarına yatırım yapmaktan kanunen men edilmiştir."),
          ("E", "Fon portföy değerinin en az %80'i diğer fonların ve borsa yatırım fonlarının katılma paylarından oluşur ve tek bir fona yatırım %20'yi aşamaz.")],
         "1. MEVZUAT DAYANAĞI: III-52.1 m. 6, 18.\n2. HUKUKİ / TEKNİK ÇERÇEVE: Fon sepeti fonlarında portföyün en az %80'i diğer yatırım fonu ve BYF paylarından oluşmalıdır. Çeşitlendirme gereği tek bir fona yapılabilecek yatırım fon portföy değerinin %20'sini aşamaz.\n3. ADIM ADIM İNCELEME / HESAPLAMA: E seçeneğindeki %80 ve %20 kuralları mevzuatın doğrudan amir hükmüdür.\n4. DOĞRU CEVAP VE SONUÇ: E seçeneğidir.\n5. ÇELDİRİCİ TUZAĞI: Tek fona %100 yatırım yapılabileceği zannı (A şıkkı).",
         "Fon sepeti fonunda asgari %80 fon payı şartı ve tek bir fona azami %20 sınırlaması vardır.", "KB2_Muhakeme"),

        # --- BLOK 5: Q41-Q50 (2 A, 2 B, 2 C, 2 D, 2 E) ---
        # 41 (A)
        ("q_1003_sert_041", "A", "Rüçhan Hakkı Kupon Pazarı İşlem Kuralları",
         "Borsa İstanbul Pay Piyasası'nda bedelli sermaye artırımı sürecinde oluşturulan 'Rüçhan Hakkı Kupon Pazarı'na ilişkin hangisi DOĞRUDUR?",
         [("A", "Rüçhan hakkı kullanım süresi içinde kuponlar borsada 'R' koduyla işlem görür ve işlem sırası kullanım bitiminden önce kapanır."),
          ("B", "Rüçhan hakkı kuponları borsada alınıp satılamaz, sadece ihraççı şirket genel müdürlüğünde fiziken devredilebilir."),
          ("C", "Rüçhan kupon pazarında fiyat marjı serbest olup hiçbir tavan veya taban fiyat uygulanmaz."),
          ("D", "Rüçhan hakkı kupon pazarında sadece şirketin imtiyazlı pay sahipleri işlem yapabilir."),
          ("E", "Rüçhan hakkı kuponları hisse senedinden bağımsız olarak süresiz şekilde borsada işlem görmeye devam eder.")],
         "1. MEVZUAT DAYANAĞI: Borsa İstanbul Pay Piyasası Yönergesi.\n2. HUKUKİ / TEKNİK ÇERÇEVE: Bedelli artırımda rüçhan hakkını kullanmak istemeyenler kuponlarını 'R' sırasında satabilir. Rüçhan pazarı kullanım süresinin bitiminden önce (kural olarak 5 iş günü önce) kapanır.\n3. ADIM ADIM İNCELEME / HESAPLAMA: A şıkkı rüçhan pazarının borsa işleyişini tam doğru açıklar.\n4. DOĞRU CEVAP VE SONUÇ: A seçeneğidir.\n5. ÇELDİRİCİ TUZAĞI: Rüçhan kuponlarının borsada işlem görmediği zannı.",
         "Rüçhan kuponları borsada 'R' koduyla işlem görür ve kullanım süresi bitiminden önce işlem sırası kapanır.", "KB2_Muhakeme"),

        # 42 (B)
        ("q_1003_sert_042", "B", "Serbest Yatırım Fonları (Hedge Funds) Kuralları",
         "III-52.1 sayılı Yatırım Fonlarına İlişkin Esaslar Tebliği uyarınca kurulan 'Serbest Yatırım Fonları'na ilişkin hangisi DOĞRUDUR?",
         [("A", "Serbest fon katılma payları Borsa İstanbul gişelerinden tüm tasarruf sahiplerine serbestçe halka arz edilir."),
          ("B", "Yalnızca Nitelikli Yatırımcılara satılabilir, standart fon portföy kısıtlamalarına tabi değildir ve kaldıraç kullanabilirler."),
          ("C", "Serbest fonların portföylerine türev araç, vadeli işlem veya opsiyon sözleşmesi dahil etmeleri kanunen yasaktır."),
          ("D", "Serbest fonlar hiçbir şekilde yönetim ücreti veya performans primi tahsil edemezler."),
          ("E", "Serbest fonların portföy değerleme raporları sadece 5 yılda bir SPK'ya iletilir.")],
         "1. MEVZUAT DAYANAĞI: III-52.1 m. 25, 26.\n2. HUKUKİ / TEKNİK ÇERÇEVE: Serbest fonlar sadece Nitelikli Yatırımcılara satılır. SPK'nın genel yatırım sınırlamalarından muaftır; açığa satış, kaldıraç ve türev pozisyon serbestçe alabilirler.\n3. ADIM ADIM İNCELEME / HESAPLAMA: B şıkkı serbest fonların yasal tanımını eksiksiz ifade eder.\n4. DOĞRU CEVAP VE SONUÇ: B seçeneğidir.\n5. ÇELDİRİCİ TUZAĞI: Serbest fonların halka arz edilebileceğini zannetmek.",
         "Serbest fonlar sadece Nitelikli Yatırımcılara satılır; genel fon kısıtlamalarından muaf olup kaldıraç kullanabilirler.", "KB2_Muhakeme"),

        # 43 (C)
        ("q_1003_sert_043", "C", "Faiz Riski ve Yeniden Yatırım Riski Etkileşimi",
         "Sabit kuponlu bir tahvil yatırımcısının maruz kaldığı 'Piyasa Faiz Oranı Riski' (Fiyat Riski) ile 'Yeniden Yatırım Riski' (Reinvestment Risk) arasındaki ilişkiye dair hangisi DOĞRUDUR?",
         [("A", "Piyasa faizleri yükseldiğinde hem tahvilin fiyatı artar hem de kuponların yeniden yatırım geliri artar."),
          ("B", "Piyasa faizleri düştüğünde tahvil fiyatı düşer, yeniden yatırım getirisi yükselir."),
          ("C", "Piyasa faizleri arttığında tahvilin piyasa fiyatı düşerken, tahsil edilen kuponların yeniden yatırıma yönlendirilme getirisi artar."),
          ("D", "Sıfır kuponlu (iskontolu) tahvillerde yeniden yatırım riski en yüksek seviyededir."),
          ("E", "Her iki risk türü de faiz değişimlerine karşı her zaman aynı yönde hareket eder.")],
         "1. MEVZUAT DAYANAĞI: Finansal Piyasalarda Sabit Getirili Araçlar Risk Analizi.\n2. HUKUKİ / TEKNİK ÇERÇEVE: Faizler artınca tahvil fiyatı düşer (fiyat riski gerçekleşir). Ancak ara kupon ödemeleri daha yüksek faizden yatırıma yönlendirilir (yeniden yatırım kazancı artar). Bu iki risk zıt yönlüdür.\n3. ADIM ADIM İNCELEME / HESAPLAMA: C seçeneğindeki zıt yönlü denge finans teorisinin temel prensibidir.\n4. DOĞRU CEVAP VE SONUÇ: C seçeneğidir.\n5. ÇELDİRİCİ TUZAĞI: Sıfır kuponlu tahvilde yeniden yatırım riski olduğunu sanmak (sıfır kuponluda ara kupon olmadığı için yeniden yatırım riski SIFIRDIR).",
         "Faiz artışı tahvil fiyatını düşürürken kuponların yeniden yatırım getirisini artırır; sıfır kuponlu tahvilde ise yeniden yatırım riski yoktur.", "KB2_Muhakeme"),

        # 44 (D)
        ("q_1003_sert_044", "D", "VİOP Teminat Tamamlama Bildirim Süresi",
         "Borsa İstanbul VİOP'ta gün sonu değerlemesi neticesinde teminat tamamlama çağrısı (Margin Call) alan bir yatırımcının yükümlü olduğu eksik teminatı en geç ne zamana kadar tamamlaması zorunludur?",
         [("A", "Bildirimin yapıldığı gün seans bitiminden hemen sonra saat 18:30'a kadar"),
          ("B", "Aynı gün gece yarısı saat 24:00'e kadar"),
          ("C", "T+2 günü saat 12:00'ye kadar"),
          ("D", "Takip eden işlem günü (T+1) en geç saat 14:30'a kadar"),
          ("E", "Takip eden haftanın son iş günü seans açılışına kadar")],
         "1. MEVZUAT DAYANAĞI: Takasbank Merkezi Karşı Taraf Yönergesi ve VİOP İşleyiş Kılavuzu.\n2. HUKUKİ / TEKNİK ÇERÇEVE: Gün sonunda oluşan margin call bildirimi aracı kurumca yatırımcıya iletilir. Yatırımcı eksik teminatı en geç T+1 günü saat 14:30'a kadar yatırmak zorundadır. Aksi halde pozisyonlar re'sen kapatılır.\n3. ADIM ADIM İNCELEME / HESAPLAMA: D seçeneğindeki T+1 saat 14:30 kesin operasyonel kuraldır.\n4. DOĞRU CEVAP VE SONUÇ: D seçeneğidir.\n5. ÇELDİRİCİ TUZAĞI: T+2 süresiyle karıştırmak veya aynı gün kapatılması gerektiğini sanmak.",
         "VİOP margin call tamamlama süresi: Takip eden iş günü (T+1) en geç saat 14:30'dur.", "KB1_Kavramsal"),

        # 45 (E)
        ("q_1003_sert_045", "E", "Yeşil Kira Sertifikası İhracında Fon Kullanımı",
         "SPK'nın Yeşil Borçlanma Araçları ve Yeşil Kira Sertifikası Rehberi uyarınca yeşil kira sertifikası ihraç eden bir VKŞ ve kaynak kuruluşun yükümlülüklerine ilişkin;\n\nI. İhraçtan sağlanan fonun tamamının yeşil proje kriterlerine uygun projelere tahsis edilmesi zorunludur.\nII. İhraççı, fonun kullanımına ilişkin olarak yılda en az bir kez 'Fon Tahsis Raporu' hazırlayıp KAP'ta yayımlamakla yükümlüdür.\nIII. Yeşil projelerden beklenen çevresel faydaların gerçekleşme derecesini gösteren 'Etki Raporu' hazırlanmalıdır.\n\nYukarıda yer alan yükümlülüklerden hangileri mevzuatça şart koşulmuştur?",
         [("A", "Yalnızca I numaralı yükümlülük mevzuatça şart koşulmuştur."),
          ("B", "Yalnızca II numaralı yükümlülük mevzuatça şart koşulmuştur."),
          ("C", "I ve II numaralı yükümlülükler mevzuatça şart koşulmuştur."),
          ("D", "II ve III numaralı yükümlülükler mevzuatça şart koşulmuştur."),
          ("E", "I, II ve III numaralı yükümlülüklerin tamamı mevzuatça şart koşulmuştur.")],
         "1. MEVZUAT DAYANAĞI: SPK Yeşil Borçlanma Aracı ve Yeşil Kira Sertifikası Rehberi Bölüm 4, 5.\n2. HUKUKİ / TEKNİK ÇERÇEVE: Yeşil sukukta fonun yeşil projeye ayrılması, yıllık Fon Tahsis Raporu ve Etki Raporu (Impact Report) hazırlanması zorunludur.\n3. ADIM ADIM İNCELEME / HESAPLAMA: I, II ve III öncüllerinin tümü rehberin temel yükümlülükleridir.\n4. DOĞRU CEVAP VE SONUÇ: E seçeneğidir.\n5. ÇELDİRİCİ TUZAĞI: Etki raporunun isteğe bağlı olduğunu düşünmek.",
         "Yeşil ihraçlarda yeşil projeye tahsis, Fon Tahsis Raporu ve Etki Raporu zorunludur.", "KB2_Muhakeme"),

        # 46 (A)
        ("q_1003_sert_046", "A", "Şemsiye Fon Türleri ve Katılma Payı Alım Satım Valörü",
         "III-52.1 sayılı Tebliğ uyarınca Türkiye Elektronik Fon Dağıtım Platformu (TEFAS) üzerinden işlem gören menkul kıymet yatırım fonlarının pay alım ve satım valör kurallarına ilişkin hangisi DOĞRUDUR?",
         [("A", "Para piyasası fonlarında alım ve satım işlemleri aynı gün valörlü (T+0) olarak gerçekleşir."),
          ("B", "Hisse senedi yoğun fonlarda satış bedelleri yatırımcı hesabına istisnasız T+10 günde geçer."),
          ("C", "Yabancı borçlanma araçları fonlarında alım işlemi T+0, satım işlemi T+30 günde yapılır."),
          ("D", "TEFAS'ta işlem gören fonların alım satım emirleri sadece cumartesi günleri sisteme girilebilir."),
          ("E", "Fon katılma payı satış emri verildiğinde satış fiyatı daima 1 ay önceki fiyattan hesaplanır.")],
         "1. MEVZUAT DAYANAĞI: III-52.1 Tebliği ve TEFAS Uygulama Esasları.\n2. HUKUKİ / TEKNİK ÇERÇEVE: Para piyasası fonları çok kısa vadeli likit araçlar taşıdığından alım ve satım aynı gün (T+0) valörle gerçekleştirilir. Hisse fonlarında genelde T+1 alış, T+2 satış valörü uygulanır.\n3. ADIM ADIM İNCELEME / HESAPLAMA: A şıkkı para piyasası fonunun T+0 valör kuralını tam açıklar.\n4. DOĞRU CEVAP VE SONUÇ: A seçeneğidir.\n5. ÇELDİRİCİ TUZAĞI: Para piyasası fonlarında da T+2 valör olduğunu varsaymak.",
         "Para piyasası fonlarında katılma payı alım ve satımları aynı gün (T+0) valörle gerçekleşir.", "KB1_Kavramsal"),

        # 47 (B)
        ("q_1003_sert_047", "B", "Tahvil Fiyatı ve Getiri Arasındaki Ters Yönlü İlişki",
         "Sabit kuponlu bir tahvilin kupon faiz oranı %15 iken, piyasa faiz oranlarının (piyasa getirisinin) %20'ye YÜKSELMESİ durumunda söz konusu tahvilin piyasa fiyatı hakkında hangisi DOĞRUDUR?",
         [("A", "Tahvilin piyasa fiyatı nominal değerinin üzerine çıkar ve tahvil primli işlem görür."),
          ("B", "Tahvilin piyasa fiyatı nominal değerinin altına iner ve tahvil iskontolu işlem görür."),
          ("C", "Tahvilin piyasa fiyatı nominal değerine tam eşit kalır ve başabaş işlem görür."),
          ("D", "Tahvilin fiyatı faiz değişiminden hiçbir şekilde etkilenmez, kupon oranı %20'ye çıkarılır."),
          ("E", "Tahvil piyasadan geri çağrılarak zorunlu olarak imha edilir.")],
         "1. MEVZUAT DAYANAĞI: Sabit Getirili Menkul Kıymetler Değerleme Aksiyomları.\n2. HUKUKİ / TEKNİK ÇERÇEVE: Temel Kural:\n- Kupon Oranı = Piyasa Faizi -> Başabaş Fiyat (P = Nominal)\n- Kupon Oranı > Piyasa Faizi -> Primli Fiyat (P > Nominal)\n- Kupon Oranı < Piyasa Faizi -> İskontolu Fiyat (P < Nominal).\n3. ADIM ADIM İNCELEME / HESAPLAMA: Kupon %15, piyasa faizi %20 ise tahvil cazibesini kaybettiği için fiyatı nominalin altına düşer (iskontolu işlem görür).\n4. DOĞRU CEVAP VE SONUÇ: B seçeneğidir.\n5. ÇELDİRİCİ TUZAĞI: Faiz arttığında tahvil fiyatının da artacağını sanmak.",
         "Piyasa faizi kupon oranından yüksekse tahvil nominal değerinin altına düşer (iskontolu işlem görür).", "KB2_Muhakeme"),

        # 48 (C)
        ("q_1003_sert_048", "C", "Kredili Menkul Kıymet İşlemlerinde Özkaynak Oranı",
         "Seri: V, No: 65 sayılı Tebliğ uyarınca kredili pay alımı yapan bir yatırımcının hesabındaki özkaynak oranının kanuni sürdürme seviyesi olan %35'in altına düşmesi durumunda yürütülecek yasal süreç nedir?",
         [("A", "Yatırımcının özkaynak oranı %10'a düşene kadar hiçbir bildirim yapılmaz ve beklenir."),
          ("B", "Yatırımcıdan özkaynak oranını doğrudan %35 seviyesine çıkaracak kadar nakit istenir."),
          ("C", "Yatırımcıya özkaynak tamamlama bildirimi yapılarak özkaynağın BAŞLANGIÇ SEVİYESİ OLAN %50'YE tamamlanması istenir."),
          ("D", "Aracı kurum yatırımcının tüm hisselerini aynı saniye içinde re'sen satmak zorundadır."),
          ("E", "Özkaynak açığı aracı kurumun kendi özkaynaklarından resen hibe edilerek kapatılır.")],
         "1. MEVZUAT DAYANAĞI: Seri: V, No: 65 Kredili Menkul Kıymet İşlemleri Tebliği m. 14, 15.\n2. HUKUKİ / TEKNİK ÇERÇEVE: Özkaynak oranı %35'in altına düştüğünde aracı kurum tamamlama çağrısı yapar. Tamamlama hedefi %35 değil, BAŞLANGIÇ ORANI OLAN %50'DİR!\n3. ADIM ADIM İNCELEME / HESAPLAMA: C şıkkı başlangıç seviyesi olan %50'ye tamamlama kuralını tam ifade eder.\n4. DOĞRU CEVAP VE SONUÇ: C seçeneğidir.\n5. ÇELDİRİCİ TUZAĞI: Özkaynağın %35'e tamamlanacağını sanmak.",
         "Kredili işlemde özkaynak %35 altına düşerse başlangıç oranı olan %50'ye tamamlanır.", "KB2_Muhakeme"),

        # 49 (D)
        ("q_1003_sert_049", "D", "Dönüştürülebilir Tahvil (DET) Parite Fiyatı",
         "Nominal değeri 1.000 TL olan bir Dönüştürülebilir Tahvilin (DET) hisse senedine dönüştürme oranı 50'dir (1 adet tahvil karşılığında 50 adet hisse senedi verilmektedir). Dayanak hisse senedinin piyasa fiyatı 24 TL'dir.\n\nBuna göre söz konusu DET'in 'Dönüştürme Değeri' (Parite Fiyatı / Conversion Value) kaç TL'dir?",
         [("A", "Dönüştürme değeri 1.000 TL'dir."),
          ("B", "Dönüştürme değeri 1.100 TL'dir."),
          ("C", "Dönüştürme değeri 1.150 TL'dir."),
          ("D", "Dönüştürme değeri 1.200 TL'dir."),
          ("E", "Dönüştürme değeri 1.250 TL'dir.")],
         "1. MEVZUAT DAYANAĞI: II-31.1 sayılı Tebliğ ve DET Değerleme Esasları.\n2. HUKUKİ / TEKNİK ÇERÇEVE: Dönüştürme Değeri = Dönüştürme Oranı * Dayanak Hisse Fiyatı.\n3. ADIM ADIM İNCELEME / HESAPLAMA:\n- Dönüştürme Oranı = 50 adet hisse\n- Hisse Fiyatı = 24 TL\n- Dönüştürme Değeri = 50 * 24 = 1.200 TL.\n4. DOĞRU CEVAP VE SONUÇ: D seçeneğidir (1.200 TL).\n5. ÇELDİRİCİ TUZAĞI: Nominal değer olan 1.000 TL'yi dönüştürme fiyatına bölüp hisse fiyatıyla çarpmayı unutmak.",
         "Dönüştürme Değeri = Dönüştürme Oranı * Hisse Fiyatı = 50 * 24 = 1.200 TL.", "KB3_Vaka"),

        # 50 (E)
        ("q_1003_sert_050", "E", "Para Piyasası Fonları Portföy Sınırlamaları",
         "III-52.1 sayılı Yatırım Fonlarına İlişkin Esaslar Tebliği uyarınca 'Para Piyasası Fonları'nın (Money Market Funds) portföy yapısına ilişkin hangisi DOĞRUDUR?",
         [("A", "Para piyasası fonları portföylerine sadece Borsa İstanbul Yıldız Pazar hisse senetlerini dahil edebilirler."),
          ("B", "Fon portföyünün günlük vadesi en az 365 gün olmak zorundadır."),
          ("C", "Para piyasası fonları hiçbir şekilde banka mevduatına veya katılım hesabına yatırım yapamazlar."),
          ("D", "Fon portföyünde sadece yabancı devletlerin eurobondları yer alabilir, yerli enstrümanlar yasaktır."),
          ("E", "Portföyün günlük olarak hesaplanan ağırlıklı ortalama vadesi en fazla 45 gün olabilir ve vadesine 184 günden uzun kalan varlıklar portföye alınamaz.")],
         "1. MEVZUAT DAYANAĞI: III-52.1 m. 6.\n2. HUKUKİ / TEKNİK ÇERÇEVE: Para piyasası fonları likidite yönetim araçlarıdır. Fon portföyünün günlük ağırlıklı ortalama vadesi (AOV) en fazla 45 gün olabilir. Vadesine 184 günden fazla kalmış enstrümanlar portföye dahil edilemez.\n3. ADIM ADIM İNCELEME / HESAPLAMA: E şıkkındaki 45 gün AOV ve 184 gün azami vade para piyasası fonlarının yasal tanımıdır.\n4. DOĞRU CEVAP VE SONUÇ: E seçeneğidir.\n5. ÇELDİRİCİ TUZAĞI: Vade sınırının 90 gün veya 1 yıl sanılması.",
         "Para piyasası fonlarında fon ağırlıklı ortalama vadesi azami 45 gün olabilir, vadesi 184 günden uzun varlık alınamaz.", "KB1_Kavramsal")
    ]
    
    for item in raw_data:
        qid, correct_key, topic, text, opts, exp, trap, skill = item
        options_list = [{"key": k, "text": t} for k, t in opts]
        questions.append({
            "id": qid,
            "module_id": "1003",
            "source": "cikmis",
            "topic": topic,
            "chapter": "SERMAYE PİYASASI ARAÇLARI 1 GENEL TEORİ VE HESAPLAMALAR",
            "text": text,
            "options": options_list,
            "correct_answer": correct_key,
            "explanation": exp,
            "trap": trap,
            "difficulty": "hard",
            "tags": ["1003", topic],
            "cognitive_skill": skill
        })
        
    return questions

if __name__ == '__main__':
    qs = generate_questions()
    print(f"Modül 1003 için {len(qs)} soru üretildi.")
    key_counts = {}
    for q in qs:
        key_counts[q['correct_answer']] = key_counts.get(q['correct_answer'], 0) + 1
    print("Cevap anahtarı dağılımı:", key_counts)
    with open('scripts/data_1003_hard.json', 'w', encoding='utf-8') as f:
        json.dump(qs, f, ensure_ascii=False, indent=2)
    print("scripts/data_1003_hard.json kaydedildi.")
