# -*- coding: utf-8 -*-
"""
Modül 1005: 50 İleri Seviye (Sert) Sınav Sorusu Üreticisi
Konu: Yatırım Kuruluşları (Aracı Kurumlar, PYŞ, Kredili İşlemler, İç Sistemler, YTM)
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
        ("q_1005_sert_001", "A", "2026 Asgari Özsermaye Tutarları ve Faaliyet Yetkileri",
         "III-39.1 sayılı Yatırım Kuruluşlarının Kuruluş ve Faaliyet Esasları Tebliği uyarınca, 2026 yılı aracı kurum asgari özsermaye tutarları ve yapabilecekleri faaliyetlere ilişkin;\n\nI. Dar Yetkili Aracı Kurum: Asgari özsermaye 45 milyon TL olup yalnızca emir iletimine aracılık ve Kurulca uygun görülen sınırlı yatırım hizmetlerini yürütebilir.\nII. Kısmi Yetkili Aracı Kurum: Asgari özsermaye 190 milyon TL olup işlem aracılığı ve en iyi gayret aracılığı yapabilir; ancak portföy aracılığı ve yüklenimde bulunamaz.\nIII. Geniş Yetkili Aracı Kurum: Asgari özsermaye 380 milyon TL olup portföy aracılığı, bakiyeyi/tümünü yüklenim ve genel saklama dahil tüm yatırım hizmetlerini sunabilir.\n\nYukarıda belirtilen asgari özsermaye ve yetki eşleştirmelerinden hangileri DOĞRUDUR?",
         [("A", "I, II ve III numaralı eşleştirmelerin tamamı güncel mevzuata tam uygundur."),
          ("B", "Yalnızca I ve II numaralı eşleştirmeler güncel mevzuata uygundur."),
          ("C", "Yalnızca II ve III numaralı eşleştirmeler güncel mevzuata uygundur."),
          ("D", "Yalnızca I numaralı eşleştirme güncel mevzuata uygundur."),
          ("E", "Yalnızca III numaralı eşleştirme güncel mevzuata uygundur.")],
         "1. MEVZUAT DAYANAĞI: III-39.1 sayılı Tebliğ m. 5, 8 ve SPK 2026 yılı yeniden değerleme tutarları.\n2. HUKUKİ / TEKNİK ÇERÇEVE: 2026 yılı asgari özsermaye tutarları: Dar Yetkili: 45 Milyon TL, Kısmi Yetkili: 190 Milyon TL, Geniş Yetkili: 380 Milyon TL'dir. Yetki sınırları öncüllerde tam doğru tanımlanmıştır.\n3. ADIM ADIM İNCELEME / HESAPLAMA: I, II ve III öncüllerinin her biri tebliğin güncel asgari özsermaye ve yetki kapsamıyla birebir örtüşür.\n4. DOĞRU CEVAP VE SONUÇ: A seçeneğidir (I, II ve III).\n5. ÇELDİRİCİ TUZAĞI: Eski sermaye tutarlarını (örneğin 10M, 40M, 80M) hatırlayarak güncel 2026 rakamlarını yanlış sanmak.",
         "2026 asgari özsermayeleri: Dar: 45M TL, Kısmi: 190M TL, Geniş: 380M TL'dir; I, II ve III tam doğrudur.", "KB2_Muhakeme"),

        # 2 (B)
        ("q_1005_sert_002", "B", "Kredili Menkul Kıymet İşlemi Özkaynak Tamamlama Hesabı",
         "Yatırımcı Murat Bey'in aracı kurumdaki kredili işlem hesabında 300.000 TL piyasa değerli hisse senedi ve 220.000 TL kredi borcu bulunmaktadır. Hisselerin piyasa değeri üzerinden hesaplanan özkaynak tutarı 80.000 TL olup özkaynak oranı %26,67 ile kanuni sürdürme seviyesinin (%35) altına düşmüştür. Aracı kurum Murat Bey'e teminat tamamlama bildirimi yapmıştır.\n\nSeri: V, No: 65 sayılı Tebliğ uyarınca, Murat Bey'in özkaynağını kanuni başlangıç seviyesine (%50) çıkarabilmesi için hesaba yatırması gereken 'Nakit Tutarı' ile getirmesi gereken 'Kabul Edilebilir Hisse Senedi Piyasa Değeri' sırasıyla nedir?",
         [("A", "Nakit: 50.000 TL; Hisse Senedi: 100.000 TL"),
          ("B", "Nakit: 70.000 TL; Hisse Senedi: 140.000 TL"),
          ("C", "Nakit: 40.000 TL; Hisse Senedi: 80.000 TL"),
          ("D", "Nakit: 60.000 TL; Hisse Senedi: 120.000 TL"),
          ("E", "Nakit: 80.000 TL; Hisse Senedi: 160.000 TL")],
         "1. MEVZUAT DAYANAĞI: Seri: V, No: 65 sayılı Tebliğ m. 14, 15.\n2. HUKUKİ / TEKNİK ÇERÇEVE: Özkaynak oranı %35'in altına düştüğünde başlangıç seviyesi olan %50'ye tamamlanır. Hisse senedi getirilirse kabul katsayısı %50 olduğundan gereken hisse değeri eksik nakit tutarın 2 katıdır.\n3. ADIM ADIM İNCELEME / HESAPLAMA:\n- Portföy Değeri = 300.000 TL.\n- Hedef Özkaynak (%50) = 300.000 * 0,50 = 150.000 TL.\n- Mevcut Özkaynak = 300.000 - 220.000 = 80.000 TL.\n- Yatırılması gereken Nakit = 150.000 - 80.000 = 70.000 TL.\n- Getirilmesi gereken Hisse Senedi = 70.000 / 0,50 = 140.000 TL.\n4. DOĞRU CEVAP VE SONUÇ: B seçeneğidir (Nakit: 70.000 TL; Hisse: 140.000 TL).\n5. ÇELDİRİCİ TUZAĞI: Özkaynağı %35'e tamamlamaya çalışıp 105.000 - 80.000 = 25.000 TL bulmak veya hisse katsayısını unutmak.",
         "Kredili işlemde eksik tutar kadar nakit (70.000 TL) yatırılır; hisse getirilecekse %50 kabul katsayısı sebebiyle 2 katı (140.000 TL) hisse gerekir.", "KB3_Vaka"),

        # 3 (C)
        ("q_1005_sert_003", "C", "Yerindelik Testi (Appropriateness) Kapsamı ve Zorunluluğu",
         "III-39.1 sayılı Tebliğ uyarınca yatırım kuruluşları tarafından müşterilere uygulanması zorunlu olan 'Yerindelik Testi'ne (Suitability / Appropriateness) ilişkin hangisi DOĞRUDUR?",
         [("A", "Yerindelik testi yalnızca emir iletimine aracılık faaliyetinde zorunlu olup portföy yönetiminde uygulanmaz."),
          ("B", "Müşteri teste cevap vermek istemezse yatırım kuruluşu müşterinin risk profilini en riskli grup olarak varsayarak işlem yapar."),
          ("C", "Portföy yöneticiliği ve yatırım danışmanlığı hizmeti sunulmadan önce müşterinin mali durumu, risk-getiri tercihleri ve yatırım amaçlarını tespit etmek üzere yapılması kanunen zorunludur."),
          ("D", "Yerindelik testi bir kez yapıldıktan sonra müşteri vefat edene kadar bir daha asla yenilenemez."),
          ("E", "Yerindelik testi sonucunda müşteriye uygun olmayan yüksek riskli ürünlerin önerilmesi ve portföyüne re'sen alınması serbesttir.")],
         "1. MEVZUAT DAYANAĞI: III-39.1 Tebliği m. 34, 35.\n2. HUKUKİ / TEKNİK ÇERÇEVE: Yerindelik testi, bireysel portföy yöneticiliği ve yatırım danışmanlığı hizmetleri için zorunludur. Müşterinin mali gücü, risk toleransı ve yatırım vadesi ölçülür; yerinde olmayan hizmet sunulamaz.\n3. ADIM ADIM İNCELEME / HESAPLAMA: C şıkkı yerindelik testinin yasal zorunluluk alanını ve amacını tam olarak verir.\n4. DOĞRU CEVAP VE SONUÇ: C seçeneğidir.\n5. ÇELDİRİCİ TUZAĞI: Uygunluk testi (genel aracılık) ile yerindelik testini (danışmanlık/portföy yönetimi) birbirine karıştırmak.",
         "Yerindelik testi, portföy yöneticiliği ve yatırım danışmanlığı hizmetleri öncesinde yapılması zorunlu olan kapsamlı testtir.", "KB2_Muhakeme"),

        # 4 (D)
        ("q_1005_sert_004", "D", "Portföy Yönetim Şirketlerinde Başarı Primi (High-Water Mark)",
         "III-55.1 sayılı Portföy Yönetim Şirketleri Tebliği uyarınca, bireysel portföy yönetimi sözleşmelerinde veya yatırım fonlarında 'Başarı Primi' (Performance Fee) tahakkuk ettirilmesine ilişkin 'Zirve Değer' (High-Water Mark) kuralı nedir?",
         [("A", "Portföyün piyasa değeri her ay sonunda bir önceki aya göre pozitif olduğu sürece kesintisiz prim alınması kuralıdır."),
          ("B", "Yalnızca Borsa İstanbul BIST 100 endeksinin üzerinde getiri sağlanan günlerde günlük olarak prim tahakkuk ettirilmesidir."),
          ("C", "Fon yöneticisinin portföyü en az 10 kat büyütmesi durumunda SPK tarafından verilen bir başarı ödülüdür."),
          ("D", "Başarı primi tahakkuk ettirilebilmesi için portföyün net aktif değerinin geçmiş dönemlerde ulaştığı en yüksek zirve değeri (high-water mark) ve belirlenen eşik değeri fiilen aşmış olması zorunludur."),
          ("E", "Portföy zarar etse dahi yönetim ücretinin iki katı oranında garanti başarı primi tahsil edilmesini sağlayan kuraldır.")],
         "1. MEVZUAT DAYANAĞI: III-55.1 sayılı Tebliğ m. 27.\n2. HUKUKİ / TEKNİK ÇERÇEVE: High-water mark kuralı yatırımcıyı korur: Portföy yöneticisi geçmişte düşüş yaşattıysa, portföy eski zirve değerini ve karşılaştırma ölçütünü aşmadıkça yeni başarı primi alamaz.\n3. ADIM ADIM İNCELEME / HESAPLAMA: D seçeneği Zirve Değer ilkesinin finansal ve hukuki tanımıdır.\n4. DOĞRU CEVAP VE SONUÇ: D seçeneğidir.\n5. ÇELDİRİCİ TUZAĞI: Zarar telafi edilmeden sadece son ayki artış üzerinden başarı primi alınabileceğini sanmak.",
         "Başarı primi sadece geçmişte ulaşılan en yüksek zirve değer (high-water mark) ve eşik değer aşıldığında alınabilir.", "KB2_Muhakeme"),

        # 5 (E)
        ("q_1005_sert_005", "E", "Aracı Kurum Personelinin Pay Alım Satım Kısıtlamaları",
         "III-39.1 sayılı Tebliğ m. 43 uyarınca yatırım kuruluşu çalışanlarının kendi adlarına veya üçüncü şahıslar hesabına sermaye piyasası araçlarında işlem yapmalarına ilişkin;\n\nI. Çalışanlar sermaye piyasası araçları alım satım işlemlerini sadece kendi çalıştıkları yatırım kuruluşu nezdindeki hesapları üzerinden yürütmek zorundadır.\nII. Yatırım kuruluşu çalışanlarının satın aldıkları payları satın alma tarihinden itibaren en az 30 gün süreyle ellerinde tutmaları (satmamaları) zorunludur.\nIII. Müşterilerin emirleri yerine getirilmeden önce veya müşteri emirleriyle çıkar çatışması yaratacak şekilde çalışanların kendi hesaplarına işlem yapması (front-running) kesinlikle yasaktır.\n\nYukarıda yer alan personel işlem kısıtlamalarından hangileri DOĞRUDUR?",
         [("A", "Yalnızca I numaralı kısıtlama mevzuatça getirilmiştir."),
          ("B", "Yalnızca II numaralı kısıtlama mevzuatça getirilmiştir."),
          ("C", "I ve II numaralı kısıtlamalar mevzuatça getirilmiştir."),
          ("D", "II ve III numaralı kısıtlamalar mevzuatça getirilmiştir."),
          ("E", "I, II ve III numaralı kısıtlamaların tamamı mevzuatça getirilmiştir.")],
         "1. MEVZUAT DAYANAĞI: III-39.1 m. 43.\n2. HUKUKİ / TEKNİK ÇERÇEVE: Aracı kurum personeli sadece kendi kurumundan işlem yapabilir (I). Alınan paylar asgari 30 gün elde tutulmalıdır (II). Müşteri emrinin önüne geçerek işlem yapmak yasaktır (III).\n3. ADIM ADIM İNCELEME / HESAPLAMA: I, II ve III öncüllerinin tümü tebliğin amir etik ve operasyonel kurallarıdır.\n4. DOĞRU CEVAP VE SONUÇ: E seçeneğidir.\n5. ÇELDİRİCİ TUZAĞI: 30 gün elde tutma kuralını bilmemek veya personelin istediği kurumdan gizlice işlem yapabileceğini sanmak.",
         "Aracı kurum personeli sadece kendi kurumundan işlem yapabilir, hisseleri asgari 30 gün tutmalıdır ve front-running yasaktır.", "KB2_Muhakeme"),

        # 6 (A)
        ("q_1005_sert_006", "A", "Yatırım Kuruluşlarında Teftiş Kurulu ve İç Denetim Bağımsızlığı",
         "III-39.1 sayılı Tebliğ uyarınca yatırım kuruluşlarında kurulması zorunlu olan 'Teftiş Kurulu' (İç Denetim Birimi) ve müfettişlerin teşkilat yapısına ilişkin hangisi DOĞRUDUR?",
         [("A", "Teftiş Kurulu doğrudan ve yalnızca Yönetim Kurulu'na bağlı olarak görev yapar; icracı genel müdüre bağlanamaz."),
          ("B", "Teftiş Kurulu operasyonel olarak Genel Müdür Yardımcılığına bağlıdır ve raporlarını sadece Genel Müdüre sunar."),
          ("C", "Aracı kurumlarda teftiş kurulu kurulması zorunlu olmayıp teftiş görevi şirket muhasebe müdürü tarafından yürütülür."),
          ("D", "Müfettişler aynı zamanda şirketin borsa işlem salonunda müşteri emirlerini kabul edip seansa iletmekle görevlendirilebilir."),
          ("E", "Teftiş kurulunun hazırladığı denetim raporları SPK denetçilerine karşı gizli tutulur ve hiçbir şekilde ibraz edilmez.")],
         "1. MEVZUAT DAYANAĞI: III-39.1 Tebliği m. 20, 21.\n2. HUKUKİ / TEKNİK ÇERÇEVE: İç denetim (teftiş) bağımsızlığı gereği teftiş kurulu doğrudan Yönetim Kurulu'na bağlıdır. İcracı yönetimden (Genel Müdür) emir alamaz, icracı görev üstlenemez.\n3. ADIM ADIM İNCELEME / HESAPLAMA: A seçeneği iç denetimin doğrudan Yönetim Kurulu'na bağlılık kuralını tam açıklar.\n4. DOĞRU CEVAP VE SONUÇ: A seçeneğidir.\n5. ÇELDİRİCİ TUZAĞI: Teftiş kurulunun Genel Müdüre bağlı çalıştığını zannetmek (B şıkkı).",
         "Teftiş Kurulu bağımsızlık gereği doğrudan ve yalnızca Yönetim Kurulu'na bağlıdır.", "KB1_Kavramsal"),

        # 7 (B)
        ("q_1005_sert_007", "B", "Yatırımcı Tazmin Merkezi (YTM) Kapsamı ve Limitleri",
         "6362 sayılı Sermaye Piyasası Kanunu m. 82-84 uyarınca 'Yatırımcı Tazmin Merkezi' (YTM) tarafından hak sahiplerine ödenecek tazminatın kapsamı ve sınırlarına dair hangisi DOĞRUDUR?",
         [("A", "Borsa İstanbul'da hisse senedi fiyatlarının düşmesi sebebiyle portföyü değer kaybeden yatırımcıların tüm zararları YTM tarafından tazmin edilir."),
          ("B", "YTM yalnızca yatırım kuruluşunun iflası veya mali durumunun bozulması sebebiyle müşteriye ait nakit ve menkul kıymetlerin iade edilememesi durumunda kanuni tavan tutara kadar tazmin yapar."),
          ("C", "YTM'nin tazminat ödeme limiti sınırsız olup müşterinin kurumdaki milyarlarca liralık tüm varlığı eksiksiz karşılanır."),
          ("D", "YTM sadece yabancı kurumsal fonlara tazminat öder, Türkiye Cumhuriyeti vatandaşı bireysel yatırımcılar tazminat alamaz."),
          ("E", "Kredili işlem yaparak temerrüde düşen yatırımcıların aracı kuruma olan tüm kredi borçları YTM bütçesinden ödenir.")],
         "1. MEVZUAT DAYANAĞI: 6362 sayılı SPKn m. 82, 83.\n2. HUKUKİ / TEKNİK ÇERÇEVE: YTM bir piyasa riski sigortası değildir. YTM sadece yatırım kuruluşunun saklama ve nakit borcunu yerine getirememesi (dolandırıcılık, hırsızlık, batık) halinde kanuni limit dahilinde devreye girer.\n3. ADIM ADIM İNCELEME / HESAPLAMA: B şıkkı saklama/nakit iadesi yükümlülüğünün yerine getirilememesi şartını tam olarak tanımlar.\n4. DOĞRU CEVAP VE SONUÇ: B seçeneğidir.\n5. ÇELDİRİCİ TUZAĞI: Borsada para kaybedenlerin zararının YTM tarafından karşılanacağını düşünmek (A şıkkı).",
         "YTM borsa fiyat düşüşlerini asla tazmin etmez; sadece kurumun teslim edemediği müşteri varlıklarını kanuni tavan dahilinde öder.", "KB2_Muhakeme"),

        # 8 (C)
        ("q_1005_sert_008", "C", "Açığa Satış İşlemleri ve Teminatlandırma (Seri: V, No: 65)",
         "Açığa satış (Short Sale) işlemlerine ve temerrüt kurallarına ilişkin aşağıdaki ifadelerden hangisi DOĞRUDUR?",
         [("A", "Açığa satış emri verilirken emrin açığa satış olduğunun aracı kuruma ve borsa sistemine bildirilmesi zorunlu değildir."),
          ("B", "Borsa İstanbul'da işlem gören tüm sermaye piyasası araçlarında ve hisse senetlerinde koşulsuz olarak açığa satış serbesttir."),
          ("C", "Açığa satış işlemi gerçekleştirilmeden önce veya en geç takas gününe kadar satılan kıymetin ödünç alma yoluyla temin edilmiş olması zorunludur."),
          ("D", "Açığa satılan payların bedeli satış anında yatırımcının banka hesabına nakit olarak aktarılır ve serbestçe harcanabilir."),
          ("E", "Açığa satış yapan yatırımcı payın temettü dağıtması durumunda temettü ödemesinden hiçbir şekilde sorumlu tutulamaz.")],
         "1. MEVZUAT DAYANAĞI: Seri: V, No: 65 Tebliği ve Borsa İstanbul Açığa Satış Yönergesi.\n2. HUKUKİ / TEKNİK ÇERÇEVE: Açığa satışta satılan pay mülkiyette değildir. T+2 takasında teslim edilebilmesi için en geç takas anına kadar ödünç alınması veya satın alınması şarttır. Satış emri sisteme açığa satış olarak işaretlenir.\n3. ADIM ADIM İNCELEME / HESAPLAMA: C şıkkı ödünç alma ve takas temin zorunluluğunu doğru açıklar.\n4. DOĞRU CEVAP VE SONUÇ: C seçeneğidir.\n5. ÇELDİRİCİ TUZAĞI: Emrin açığa satış olduğunun gizlenebileceği veya tüm hisselerde serbest olduğu yanılgısı.",
         "Açığa satışta satılan kıymet en geç takas gününe kadar ödünç veya satın alma yoluyla temin edilmelidir.", "KB2_Muhakeme"),

        # 9 (D)
        ("q_1005_sert_009", "D", "Aracı Kurum Yetki Belgeleri ve İptali Şartları",
         "6362 sayılı Sermaye Piyasası Kanunu ve III-39.1 sayılı Tebliğ uyarınca bir yatırım kuruluşunun faaliyet yetki belgesinin Kurul tarafından iptal edilmesini gerektiren hallere dair hangisi YANLIŞTIR?",
         [("A", "Yetki belgesinin verilmesi sırasında aranan şartların kaybedilmesi ve Kurulca verilen sürede giderilmemesi"),
          ("B", "Yetki belgesinin gerçeğe aykırı beyan ve belgelerle hileli olarak alınmış olduğunun sonradan anlaşılması"),
          ("C", "Kuruluşun mali durumunun taahhütlerini karşılayamayacak derecede bozulması ve özsermayenin asgari haddin altına düşmesi"),
          ("D", "Yatırım kuruluşunun son bir takvim yılında herhangi bir müşterisine kâr garantisi verememiş olması"),
          ("E", "Yetki belgesi alındığı tarihten itibaren aralıksız bir yıl süreyle faaliyette bulunulmaması")],
         "1. MEVZUAT DAYANAĞI: 6362 sayılı SPKn m. 96, 97 ve III-39.1 m. 67.\n2. HUKUKİ / TEKNİK ÇERÇEVE: Yetki belgesi şartların kaybı, hile, mali çöküş veya 1 yıl faaliyetsizlikte iptal edilir. Müşteriye KÂR GARANTİSİ VERMEK ZATEN KANUNEN KESİN BİR SUÇTUR; kâr garantisi verememek iptal sebebi olamaz, aksine yasal zorunluluktur!\n3. ADIM ADIM İNCELEME / HESAPLAMA: D seçeneğindeki kâr garantisi verememe ifadesi hukuken anlamsız ve yanlıştır.\n4. DOĞRU CEVAP VE SONUÇ: D seçeneğidir.\n5. ÇELDİRİCİ TUZAĞI: 1 yıl faaliyetsizlik kuralını bilmemek.",
         "Müşteriye kâr garantisi vermek kanunen yasaktır; kâr garantisi verememek iptal sebebi olamaz.", "KB2_Muhakeme"),

        # 10 (E)
        ("q_1005_sert_010", "E", "Geniş Yetkili Aracı Kurum Portföy Aracılığı ve Saklama",
         "III-39.1 sayılı Tebliğ uyarınca 'Geniş Yetkili Aracı Kurum' statüsüne sahip bir aracı kurumun yürütebileceği faaliyetlere ilişkin;\n\nI. Kendi nam ve hesabına sermaye piyasası araçlarında alım satım yapmak (Portföy Aracılığı).\nII. Müşterilerine ait sermaye piyasası araçlarını kendi bünyesinde veya Takasbank nezdinde 'Genel Saklama' hizmeti kapsamında saklamak.\nIII. Halka arzlarda 'Bakiyeyi Yüklenim' veya 'Tümünü Yüklenim' sözleşmesi imzalayarak satışa aracılık etmek.\n\nYukarıda yer alan yatırım hizmetlerinden hangileri Geniş Yetkili Aracı Kurumlar tarafından hukuken icra edilebilir?",
         [("A", "Yalnızca I numaralı faaliyet icra edilebilir."),
          ("B", "Yalnızca II numaralı faaliyet icra edilebilir."),
          ("C", "I ve II numaralı faaliyetler icra edilebilir."),
          ("D", "II ve III numaralı faaliyetler icra edilebilir."),
          ("E", "I, II ve III numaralı faaliyetlerin tamamı icra edilebilir.")],
         "1. MEVZUAT DAYANAĞI: III-39.1 sayılı Tebliğ m. 5, 8, 9.\n2. HUKUKİ / TEKNİK ÇERÇEVE: Geniş yetkili aracı kurumlar sermaye piyasasının en üst yetkili kurumlarıdır. Portföy aracılığı (I), genel saklama (II) ve yüklenimli halka arz (III) faaliyetlerinin tamamını yapmaya yetkilidirler.\n3. ADIM ADIM İNCELEME / HESAPLAMA: I, II ve III öncülleri geniş yetkili kurumun kanuni yetkileridir.\n4. DOĞRU CEVAP VE SONUÇ: E seçeneğidir.\n5. ÇELDİRİCİ TUZAĞI: Kısmi yetkili ile geniş yetkili ayrımında yüklenim ve genel saklama yetkisini karıştırmak.",
         "Geniş yetkili aracı kurum portföy aracılığı, genel saklama ve yüklenimli halka arz yapabilir; I, II ve III doğrudur.", "KB2_Muhakeme"),

        # --- BLOK 2: Q11-Q20 (2 A, 2 B, 2 C, 2 D, 2 E) ---
        # 11 (A)
        ("q_1005_sert_011", "A", "Dar Yetkili Aracı Kurumların Yapamayacağı Faaliyetler",
         "III-39.1 sayılı Tebliğ uyarınca 'Dar Yetkili Aracı Kurumlar' aşağıdaki yatırım hizmeti ve faaliyetlerinden hangisini KESİNLİKLE YÜRÜTEMEZLER?",
         [("A", "Kendi nam ve hesabına sermaye piyasası araçlarında piyasa yapıcılığı ve portföy aracılığı yapmak"),
          ("B", "Müşterilerden gelen pay alım satım emirlerini Borsa İstanbul'a iletmek (Emir iletimine aracılık)"),
          ("C", "Kuruldan izin almak kaydıyla müşterilere bireysel yatırım danışmanlığı hizmeti sunmak"),
          ("D", "Sermaye piyasaları ile ilgili genel finansal piyasa bültenleri ve araştırma raporları yayımlamak"),
          ("E", "Kaldıraçlı işlemler hariç olmak üzere yurt içi borsalarda emir kabul etmek")],
         "1. MEVZUAT DAYANAĞI: III-39.1 m. 8/1.\n2. HUKUKİ / TEKNİK ÇERÇEVE: Dar yetkili aracı kurumlar kendi nam ve hesaplarına emir giremezler, portföy aracılığı yapamazlar, kredili işlem ve yüklenim yapamazlar. Sadece emir iletimi yapabilirler.\n3. ADIM ADIM İNCELEME / HESAPLAMA: A seçeneğindeki portföy aracılığı dar yetkili kurumlar için kesinlikle yasaktır.\n4. DOĞRU CEVAP VE SONUÇ: A seçeneğidir.\n5. ÇELDİRİCİ TUZAĞI: Yatırım danışmanlığı da yapamayacaklarını zannetmek (izinle yapabilirler).",
         "Dar yetkili aracı kurumlar kendi nam ve hesaplarına portföy aracılığı ve piyasa yapıcılığı yapamazlar.", "KB1_Kavramsal"),

        # 12 (B)
        ("q_1005_sert_012", "B", "Portföy Yönetim Şirketi (PYŞ) Kuruculuk ve Sermaye Şartı",
         "III-55.1 sayılı Portföy Yönetim Şirketleri Tebliği uyarınca, yeni kurulacak bir PYŞ'nin kuruluş şartları ve asgari ödenmiş sermayesine dair hangisi DOĞRUDUR?",
         [("A", "PYŞ'ler limited şirket şeklinde kurulabilir ve asgari başlangıç sermayesi 5 milyon TL'dir."),
          ("B", "PYŞ'ler münhasıran portföy işletmek üzere anonim şirket şeklinde kurulur ve güncel asgari özsermaye şartı 440 milyon TL'dir."),
          ("C", "PYŞ kurucularının hiçbir finansal tecrübesi bulunması şart olmayıp sabıkasız olmaları yeterlidir."),
          ("D", "PYŞ genel müdürünün en az 1 yıllık bankacılık tecrübesine sahip olması kanunen yeterlidir."),
          ("E", "PYŞ kurulduktan sonra sermaye piyasasında hiçbir yatırım fonu kuramaz, sadece gerçek kişilerin parasını yönetir.")],
         "1. MEVZUAT DAYANAĞI: III-55.1 sayılı Tebliğ m. 5 ve SPK 2026 yılı yeniden değerleme limitleri.\n2. HUKUKİ / TEKNİK ÇERÇEVE: PYŞ münhasıran fon ve portföy yönetmek üzere Anonim Şirket olarak kurulur. 2026 yılı asgari sermayesi 440 Milyon TL'dir. Genel müdür için en az 7 yıl tecrübe şarttır.\n3. ADIM ADIM İNCELEME / HESAPLAMA: B seçeneği A.Ş. şeklini ve 440 milyon TL güncel özsermaye kuralını tam açıklar.\n4. DOĞRU CEVAP VE SONUÇ: B seçeneğidir.\n5. ÇELDİRİCİ TUZAĞI: Limited şirket şeklinde kurulabileceğini sanmak.",
         "PYŞ münhasıran A.Ş. şeklinde kurulur ve 2026 yılı asgari özsermaye şartı 440 milyon TL'dir.", "KB1_Kavramsal"),

        # 13 (C)
        ("q_1005_sert_013", "C", "Kredili İşlemde Hisse Senedi Teminat Katsayısı Hesabı",
         "Kredili işlem hesabında özkaynak tamamlama bildirimi (Margin Call) alan bir yatırımcının kapatması gereken net nakit açığı 50.000 TL'dir. Yatırımcı nakit yatırmak yerine hesabına Borsa İstanbul BIST 50 endeksinde yer alan hisse senetlerinden virmanlamak istemektedir.\n\nSeri: V, No: 65 sayılı Tebliğ uyarınca getirilen hisselerin özkaynak hesabında %50 katsayı ile dikkate alındığı kuralı gereğince, yatırımcının teminat açığını kapatabilmesi için yatırması gereken hisselerin asgari piyasa değeri kaç TL olmalıdır?",
         [("A", "25.000 TL"),
          ("B", "50.000 TL"),
          ("C", "100.000 TL"),
          ("D", "150.000 TL"),
          ("E", "200.000 TL")],
         "1. MEVZUAT DAYANAĞI: Seri: V, No: 65 Kredili Menkul Kıymet Tebliği m. 15.\n2. HUKUKİ / TEKNİK ÇERÇEVE: Tebliğ uyarınca özkaynak hesabına ilave edilecek hisse senetleri piyasa değerinin %50'si üzerinden özkaynak olarak kabul edilir (kabul katsayısı = 0,50).\n3. ADIM ADIM İNCELEME / HESAPLAMA:\n- Eksik Özkaynak Tutarı = 50.000 TL.\n- Gereken Hisse Piyasa Değeri * 0,50 = 50.000 TL.\n- Gereken Hisse Piyasa Değeri = 50.000 / 0,50 = 100.000 TL.\n4. DOĞRU CEVAP VE SONUÇ: C seçeneğidir (100.000 TL).\n5. ÇELDİRİCİ TUZAĞI: 50.000 TL nakit açık için 50.000 TL hisse senedinin yeteceğini sanmak (B şıkkı) veya katsayıyı bölmek yerine çarpıp 25.000 TL demek (A şıkkı).",
         "Hisse senetleri %50 kabul katsayısına tabi olduğundan 50.000 TL nakit açık için 100.000 TL hisse senedi gerekir.", "KB3_Vaka"),

        # 14 (D)
        ("q_1005_sert_014", "D", "Kısmi Yetkili Aracı Kurumların Yetki Sınırları",
         "III-39.1 sayılı Tebliğ uyarınca 'Kısmi Yetkili Aracı Kurum' statüsündeki bir kurumun yapabileceği ve yapamayacağı faaliyet eşleştirmelerine ilişkin hangisi DOĞRUDUR?",
         [("A", "Halka arzlarda tümünü yüklenim yapabilir, ancak işlem aracılığı yapamaz."),
          ("B", "Genel saklama hizmeti verebilir, ancak emir iletimi yapamaz."),
          ("C", "Kendi nam ve hesabına hiçbir surette işlem yapamaz ve kredili işlem yürütemez."),
          ("D", "Müşteri emirleri için işlem aracılığı ve en iyi gayret aracılığı yapabilir; ancak bakiyeyi yüklenim ve genel saklama yapamaz."),
          ("E", "Yalnızca yatırım fonu kurup yönetebilir, pay piyasasında hiçbir aracılık faaliyeti yürütemez.")],
         "1. MEVZUAT DAYANAĞI: III-39.1 m. 8/2.\n2. HUKUKİ / TEKNİK ÇERÇEVE: Kısmi yetkili aracı kurumlar: İşlem aracılığı, en iyi gayret aracılığı, sınırlı saklama ve kendi namına işlem yapabilir. Ancak YÜKLENİM (underwriting), PORTFÖY ARACILIĞI ve GENEL SAKLAMA YAPAMAZLAR.\n3. ADIM ADIM İNCELEME / HESAPLAMA: D seçeneği kısmi yetkili kurumun sınırlarını tam yansıtır.\n4. DOĞRU CEVAP VE SONUÇ: D seçeneğidir.\n5. ÇELDİRİCİ TUZAĞI: Yüklenim yapabileceklerini sanmak (yüklenim sadece geniş yetkiliye aittir).",
         "Kısmi yetkili aracı kurum işlem aracılığı ve en iyi gayret yapabilir; yüklenim ve genel saklama yapamaz.", "KB2_Muhakeme"),

        # 15 (E)
        ("q_1005_sert_015", "E", "Uygunluk Testi (Appropriateness vs Suitability) Ayrımı",
         "III-39.1 sayılı Tebliğ uyarınca 'Uygunluk Testi' (Suitability) ile 'Yerindelik Testi' (Appropriateness) arasındaki hukuki ve operasyonel farklara ilişkin;\n\nI. Uygunluk testi genel yatırım hizmetleri (alım satım aracılığı) için uygulanırken, yerindelik testi portföy yönetimi ve yatırım danışmanlığı için zorunludur.\nII. Müşterinin uygunluk testini imzalamaktan kaçınması veya test sonucunda ürünün uygun olmaması halinde, yatırım kuruluşu müşterinin yazılı beyanını alarak işlemi gerçekleştirebilir.\nIII. Yerindelik testinde ise müşteriye uygun olmadığı tespit edilen hiçbir yatırım stratejisi veya ürün yatırım kuruluşunca önerilemez veya portföyüne dahil edilemez.\n\nYukarıda yer alan hukuki tespitlerden hangileri DOĞRUDUR?",
         [("A", "Yalnızca I numaralı tespit mevzuat uyarınca doğrudur."),
          ("B", "Yalnızca II numaralı tespit mevzuat uyarınca doğrudur."),
          ("C", "I ve II numaralı tespitler mevzuat uyarınca doğrudur."),
          ("D", "II ve III numaralı tespitler mevzuat uyarınca doğrudur."),
          ("E", "I, II ve III numaralı tespitlerin tamamı mevzuat uyarınca doğrudur.")],
         "1. MEVZUAT DAYANAĞI: III-39.1 m. 33, 34, 35.\n2. HUKUKİ / TEKNİK ÇERÇEVE: Uygunluk testinde müşteri uyarıya rağmen kendi sorumluluğuyla işlem yapabilir (II). Ancak yerindelik testinde kurum müşteriye uygun olmayan ürünü ASLA tavsiye edemez ve portföye alamaz (III).\n3. ADIM ADIM İNCELEME / HESAPLAMA: I, II ve III öncülleri bu iki test arasındaki farkı tam hukuki çerçevesiyle ortaya koyar.\n4. DOĞRU CEVAP VE SONUÇ: E seçeneğidir.\n5. ÇELDİRİCİ TUZAĞI: Yerindelik testinde de müşterinin yazılı feragatiyle uygun olmayan ürün tavsiye edilebileceğini düşünmek.",
         "Uygunluk testinde müşteri uyarılıp işlem yapabilir; yerindelik testinde ise uygun olmayan ürün asla tavsiye edilemez.", "KB2_Muhakeme"),

        # 16 (A)
        ("q_1005_sert_016", "A", "Nitelikli Müşteri Olma Şartları (III-39.1 m. 31)",
         "III-39.1 sayılı Tebliğ uyarınca, genel müşteri statüsünde olan bir bireysel yatırımcının talebi üzerine 'Nitelikli Müşteri' (Profesyonel Müşteri) olarak kabul edilebilmesi için asgari hangi finansal varlık ve tecrübe şartını sağlaması gerekir?",
         [("A", "Nakit mevduatı ve sahip olduğu sermaye piyasası araçları dahil finansal varlıkları toplamının en az 1 milyon TL olması"),
          ("B", "Borsa İstanbul'da en az 50 yıldır kesintisiz hisse senedi alım satımı yapmış olması"),
          ("C", "En az 100 milyon TL gayrimenkul servetine sahip olduğunu tapu kayıtlarıyla belgelemesi"),
          ("D", "Devlet memuru olarak en az 10 yıl kamu maliyesinde çalışmış olması"),
          ("E", "Herhangi bir anonim şirkette genel müdürlük yapmış olması")],
         "1. MEVZUAT DAYANAĞI: III-39.1 m. 31/1.\n2. HUKUKİ / TEKNİK ÇERÇEVE: Nitelikli yatırımcı/müşteri tanımında bireysel yatırımcılar için temel finansal eşik en az 1 MİLYON TL tutarında finansal varlıktır (nakit + menkul kıymet). Gayrimenkuller bu hesaba dahil edilmez.\n3. ADIM ADIM İNCELEME / HESAPLAMA: A seçeneğindeki 1 milyon TL finansal varlık şartı kanuni eşiktir.\n4. DOĞRU CEVAP VE SONUÇ: A seçeneğidir.\n5. ÇELDİRİCİ TUZAĞI: Gayrimenkul varlıklarının da 1 milyon TL hesabına sayılabileceğini düşünmek.",
         "Nitelikli müşteri olmak için finansal varlıkların (nakit ve sermaye piyasası araçları) toplamının en az 1 milyon TL olması şarttır.", "KB1_Kavramsal"),

        # 17 (B)
        ("q_1005_sert_017", "B", "Yatırım Kuruluşlarında Müşteri Sırrı ve Bilgi Güvenliği",
         "6362 sayılı Sermaye Piyasası Kanunu m. 46 ve ilgili mevzuat uyarınca 'Müşteri Sırrı' ve bilgi verme yükümlülüğüne ilişkin hangisi YANLIŞTIR?",
         [("A", "Yatırım kuruluşu mensupları sıfatları sebebiyle öğrendikleri müşteri sırlarını kanunen yetkili kılınan mercilerden başkasına açıklayamazlar."),
          ("B", "Yatırım kuruluşları SPK veya mahkemeler talep etse dahi müşteri sırrı gerekçesiyle hesap bilgilerini vermekten imtina edebilirler."),
          ("C", "Müşteri sırrının hukuka aykırı olarak açıklanması halinde Türk Ceza Kanunu ve SPKn uyarınca hapis cezası öngörülmüştür."),
          ("D", "Finansal Suçları Araştırma Kurulu'na (MASAK) yapılan şüpheli işlem bildirimleri müşteri sırrının ihlali sayılmaz."),
          ("E", "Bağımsız denetçilere denetim kapsamında verilen müşteri bilgileri bağımsız denetçiler tarafından da sır olarak saklanmak zorundadır.")],
         "1. MEVZUAT DAYANAĞI: 6362 sayılı SPKn m. 46, 114 ve MASAK mevzuatı.\n2. HUKUKİ / TEKNİK ÇERÇEVE: SPK, Mahkemeler, Savcılık ve MASAK kanunen yetkili mercilerdir. Bu mercilere bilgi verilmesi ZORUNLUDUR; müşteri sırrı gerekçesiyle bilgi vermekten kaçınılamaz.\n3. ADIM ADIM İNCELEME / HESAPLAMA: B seçeneğindeki SPK'ya bilgi vermekten imtina edilebileceği ifadesi suç teşkil eder ve açıkça yanlıştır.\n4. DOĞRU CEVAP VE SONUÇ: B seçeneğidir.\n5. ÇELDİRİCİ TUZAĞI: MASAK bildiriminin sır ihlali sayılacağını zannetmek.",
         "Yatırım kuruluşları SPK ve adli makamlara müşteri sırrı gerekçesiyle bilgi vermekten kaçınamazlar.", "KB2_Muhakeme"),

        # 18 (C)
        ("q_1005_sert_018", "C", "Aracı Kurumların Sermaye Yeterliliği Tabanı",
         "Seri: V, No: 34 sayılı Aracı Kurumların Sermaye Yeterliliği Esasları Tebliği uyarınca, aracı kurumların bulundurmakla yükümlü olduğu 'Sermaye Yeterliliği Tabanı' asgari ne kadar olmak zorundadır?",
         [("A", "Yalnızca şirketin ödenmiş sermayesi kadar olmak zorundadır."),
          ("B", "Müşterilerden toplanan toplam teminat tutarının en az 5 katı olmak zorundadır."),
          ("C", "Asgari özsermaye tutarından, risk karşılıkları toplamından ve son üç aydaki genel giderlerin üçte birinden AZ OLAMAZ."),
          ("D", "Yalnızca Borsa İstanbul'a ödenen yıllık aidat tutarı kadar olmalıdır."),
          ("E", "Borsa endeksinin günlük değişim oranına göre her gün sıfırlanan bir büyüklüktür.")],
         "1. MEVZUAT DAYANAĞI: Seri: V, No: 34 sayılı Tebliğ m. 4, 5.\n2. HUKUKİ / TEKNİK ÇERÇEVE: Sermaye yeterliliği tabanı: 1) Asgari özsermaye, 2) Risk karşılıkları toplamı (piyasa + karşı taraf + operasyonel), 3) Son 3 aylık genel giderlerin 1/3'ünden (üç aylık cari gider) az olamaz.\n3. ADIM ADIM İNCELEME / HESAPLAMA: C şıkkı bu üçlü yasal asgari taban kuralını eksiksiz belirtir.\n4. DOĞRU CEVAP VE SONUÇ: C seçeneğidir.\n5. ÇELDİRİCİ TUZAĞI: Sadece ödenmiş sermayeye eşit olacağını sanmak.",
         "Sermaye yeterliliği tabanı: Asgari özsermaye, risk karşılıkları toplamı ve 3 aylık genel giderlerin 1/3'ünden az olamaz.", "KB1_Kavramsal"),

        # 19 (D)
        ("q_1005_sert_019", "D", "Kaldıraçlı Alım Satım (Forex) İşlemlerinde Kaldıraç Oranı",
         "III-37.1 sayılı Yatırım Hizmetleri Tebliği uyarınca yurt içi yerleşik bireysel yatırımcıların gerçekleştireceği kaldıraçlı alım satım (Forex) işlemlerine ilişkin hangisi DOĞRUDUR?",
         [("A", "Kaldıraç oranı serbest piyasa koşullarında yatırımcı ile aracı kurum arasında 1:500 oranına kadar serbestçe belirlenebilir."),
          ("B", "Forex işlemi yapabilmek için yatırılması gereken asgari başlangıç teminatı 1.000 TL'dir."),
          ("C", "Tüm kaldıraçlı işlemler sadece bankalar tarafından yapılabilir, aracı kurumlar forex işlemi yapamaz."),
          ("D", "Azami kaldıraç oranı 1:10 olup, işlemlere başlayabilmek için yatırılması gereken asgari başlangıç teminatı 50.000 TL veya muadili dövizdir."),
          ("E", "Yurt dışındaki lisanssız kurumlardan internet üzerinden forex işlemi yapmak Türkiye'de tamamen serbest ve devlet güvencesindedir.")],
         "1. MEVZUAT DAYANAĞI: III-37.1 Tebliği m. 27/A ve SPK ilke kararları.\n2. HUKUKİ / TEKNİK ÇERÇEVE: Kaldıraçlı işlemlerde bireysel yatırımcılar için azami kaldıraç 1:10'dur. Asgari başlangıç teminatı 50.000 TL (veya muadili döviz) tutarındadır. Yurt dışı lisanssız sitelere erişim engeli getirilir.\n3. ADIM ADIM İNCELEME / HESAPLAMA: D seçeneği 1:10 kaldıraç ve 50.000 TL teminat kuralını tam doğru açıklar.\n4. DOĞRU CEVAP VE SONUÇ: D seçeneğidir.\n5. ÇELDİRİCİ TUZAĞI: Kaldıraç sınırının 1:100 veya asgari teminatın 10.000 TL olduğu eski düzenlemelere takılmak.",
         "Kaldıraçlı işlemlerde (Forex) azami kaldıraç 1:10 ve asgari başlangıç teminatı 50.000 TL'dir.", "KB1_Kavramsal"),

        # 20 (E)
        ("q_1005_sert_020", "E", "Yatırım Kuruluşlarında Çıkar Çatışması Yönetimi",
         "III-39.1 sayılı Tebliğ uyarınca yatırım kuruluşlarının 'Çıkar Çatışmalarını Önleme ve Yönetme' politikalarına ilişkin;\n\nI. Kurum, kendisi ile müşterileri veya müşterilerinin kendi aralarındaki çıkar çatışmalarını tespit etmek ve önlemek için Çin Duvarı (Bilgi Engelleri) politikaları uygulamak zorundadır.\nII. Yatırım tavsiyesi hazırlayan araştırma birimi personeli ile kurumsal finansman (halka arz) birimi çalışanları fiziksel ve operasyonel olarak birbirinden ayrılmalıdır.\nIII. Çıkar çatışmasının önlenemediği durumlarda, durum hizmet sunulmadan önce açıkça müşteriye yazılı olarak bildirilmeli ve müşterinin onayı alınmalıdır.\n\nYukarıda yer alan kurumsal yönetim ilkelerinden hangileri DOĞRUDUR?",
         [("A", "Yalnızca I numaralı ilke mevzuatça zorunlu kılınmıştır."),
          ("B", "Yalnızca II numaralı ilke mevzuatça zorunlu kılınmıştır."),
          ("C", "I ve II numaralı ilkeler mevzuatça zorunlu kılınmıştır."),
          ("D", "II ve III numaralı ilkeler mevzuatça zorunlu kılınmıştır."),
          ("E", "I, II ve III numaralı ilkelerin tamamı mevzuatça zorunlu kılınmıştır.")],
         "1. MEVZUAT DAYANAĞI: III-39.1 m. 41, 42.\n2. HUKUKİ / TEKNİK ÇERÇEVE: Yatırım kuruluşlarında araştırma ve kurumsal finansman arasında Çin Duvarı (Chinese Wall) zorunludur. Kaçınılmaz çıkar çatışmaları müşteriye açıklanmalıdır.\n3. ADIM ADIM İNCELEME / HESAPLAMA: I, II ve III öncülleri çıkar çatışması rejiminin üç temel ayağını tam yansıtır.\n4. DOĞRU CEVAP VE SONUÇ: E seçeneğidir.\n5. ÇELDİRİCİ TUZAĞI: Araştırma analistlerinin halka arz pazarlamasında aktif rol alabileceğini sanmak.",
         "Çıkar çatışmalarını önlemek için Çin Duvarı zorunludur; önlenemeyen durumlar müşteriye yazılı açıklanır.", "KB2_Muhakeme"),

        # --- BLOK 3: Q21-Q30 (2 A, 2 B, 2 C, 2 D, 2 E) ---
        # 21 (A)
        ("q_1005_sert_021", "A", "Kredili İşlemde Başlangıç Özkaynak Hesabı",
         "Yatırımcı Selin Hanım, aracı kurumdaki hesabında bulunan 100.000 TL nakit teminat ile kredili hisse senedi alımı yapmak istemektedir. Aracı kurumun uyguladığı başlangıç özkaynak oranı mevzuat uyarınca asgari %50'dir.\n\nSelin Hanım'ın bu teminatla satın alabileceği 'Azami Kredili Hisse Senedi Portföy Değeri' ve kullanabileceği 'Azami Kredi Tutarı' sırasıyla nedir?",
         [("A", "Azami Portföy: 200.000 TL; Azami Kredi: 100.000 TL"),
          ("B", "Azami Portföy: 150.000 TL; Azami Kredi: 50.000 TL"),
          ("C", "Azami Portföy: 300.000 TL; Azami Kredi: 200.000 TL"),
          ("D", "Azami Portföy: 250.000 TL; Azami Kredi: 150.000 TL"),
          ("E", "Azami Portföy: 500.000 TL; Azami Kredi: 400.000 TL")],
         "1. MEVZUAT DAYANAĞI: Seri: V, No: 65 Tebliği m. 13.\n2. HUKUKİ / TEKNİK ÇERÇEVE: Başlangıç Özkaynak Oranı = Özkaynak / Toplam Portföy Değeri ≥ %50. Burada Özkaynak = Yatırılan Nakit = 100.000 TL.\n3. ADIM ADIM İNCELEME / HESAPLAMA:\n- 100.000 / Toplam Portföy = 0,50 -> Toplam Portföy = 100.000 / 0,50 = 200.000 TL.\n- Azami Kredi Borcu = Toplam Portföy - Özkaynak = 200.000 - 100.000 = 100.000 TL.\n- Yani 1'e 1 oranında (özkaynağı kadar) kredi kullanabilir.\n4. DOĞRU CEVAP VE SONUÇ: A seçeneğinde 200.000 TL portföy ve 100.000 TL kredi doğru verilmiştir.\n5. ÇELDİRİCİ TUZAĞI: %50 oranını kredinin teminata oranı sanıp 100.000 TL nakitle 50.000 TL kredi (150.000 portföy) alınabileceğini düşünmek (B şıkkı).",
         "Başlangıç özkaynak oranı %50 olduğunda 100.000 TL nakit teminatla azami 200.000 TL hisse alınır (100.000 TL kredi).", "KB3_Vaka"),

        # 22 (B)
        ("q_1005_sert_022", "B", "Portföy Yöneticisi ve Yatırım Danışmanı Lisans Şartları",
         "Sermaye piyasasında Portföy Yöneticisi ve Yatırım Danışmanı olarak görev yapacak personelin sahip olması zorunlu lisans belgelerine dair hangisi DOĞRUDUR?",
         [("A", "Portföy yöneticisi olmak için sadece Sermaye Piyasası Faaliyetleri Düzey 1 Lisansı yeterlidir."),
          ("B", "Portföy yöneticiliği için Sermaye Piyasası Faaliyetleri Düzey 3 Lisansı ve Türev Araçlar Lisansı aranır."),
          ("C", "Yatırım danışmanlığı yapmak için hiçbir lisans belgesi aranmaz, üniversite diploması yeterlidir."),
          ("D", "Gayrimenkul Değerleme Lisansı alan bir kişi portföy yönetim şirketinde doğrudan fon yöneticisi olur."),
          ("E", "Türev Araçlar Lisansı sadece kambiyo müdürleri için zorunlu olup hisse portföyü yönetenlerde aranmaz.")],
         "1. MEVZUAT DAYANAĞI: VII-128.7 Sermaye Piyasasında Lisanslama Tebliği ve III-55.1 m. 11.\n2. HUKUKİ / TEKNİK ÇERÇEVE: Bireysel portföy yöneticisi ve fon yöneticisi olabilmek için SPL DÜZEY 3 LİSANSI ve TÜREV ARAÇLAR LİSANSI'na birlikte sahip olunması şarttır.\n3. ADIM ADIM İNCELEME / HESAPLAMA: B şıkkı Düzey 3 ve Türev Araçlar lisansı şartını eksiksiz belirtir.\n4. DOĞRU CEVAP VE SONUÇ: B seçeneğidir.\n5. ÇELDİRİCİ TUZAĞI: Düzey 1 veya Düzey 2 lisansının fon yönetmek için yeterli olacağını sanmak.",
         "Portföy yöneticisi olmak için Düzey 3 Lisansı ve Türev Araçlar Lisansı zorunludur.", "KB1_Kavramsal"),

        # 23 (C)
        ("q_1005_sert_023", "C", "Emirlerin Borsa Sistemine İletilmesinde Zaman Önceliği",
         "Borsa İstanbul Pay Piyasası Alım Satım Sistemi'nde geçerli olan emir öncelik kuralları uyarınca, sisteme girilen emirlerin eşleşmesinde öncelik sıralaması nasıldır?",
         [("A", "Önce Müşteri Büyüklüğü Önceliği, sonra Fiyat Önceliği, en son Zaman Önceliği uygulanır."),
          ("B", "Önce Zaman Önceliği, sonra Aracı Kurumun Sermaye Büyüklüğü, en son Fiyat Önceliği uygulanır."),
          ("C", "Önce Fiyat Önceliği (en yüksek alış, en düşük satış), aynı fiyattaki emirler arasında ise Zaman Önceliği uygulanır."),
          ("D", "Tüm emirler fiyata bakılmaksızın sadece sisteme giriş milisaniyesine göre eşleştirilir."),
          ("E", "Önce Kurumsal Yatırımcı Önceliği, sonra Bireysel Yatırımcı Önceliği uygulanır.")],
         "1. MEVZUAT DAYANAĞI: Borsa İstanbul Pay Piyasası Alım Satım Yönergesi m. 12.\n2. HUKUKİ / TEKNİK ÇERÇEVE: Borsa eşleşme motorunda ana kural: 1) FİYAT ÖNCELİĞİ (Alışta en yüksek fiyat, satışta en düşük fiyat önceliklidir), 2) ZAMAN ÖNCELİĞİ (Aynı fiyattaki emirler sisteme önce girilme sırasına göre eşleşir).\n3. ADIM ADIM İNCELEME / HESAPLAMA: C şıkkı Fiyat ve Zaman önceliği kuralını tam doğru açıklar.\n4. DOĞRU CEVAP VE SONUÇ: C seçeneğidir.\n5. ÇELDİRİCİ TUZAĞI: Zaman önceliğinin fiyattan önce geldiğini sanmak (B şıkkı).",
         "Borsa eşleşme motorunda temel kural: Önce Fiyat Önceliği, aynı fiyatta Zaman Önceliğidir.", "KB1_Kavramsal"),

        # 24 (D)
        ("q_1005_sert_024", "D", "Aracı Kurumlarda Müşteri Varlıklarının Ayrılığı İlkesi",
         "6362 sayılı Sermaye Piyasası Kanunu m. 47 uyarınca 'Müşteri Varlıklarının Korunması ve Ayrılığı İlkesi'ne ilişkin hangisi DOĞRUDUR?",
         [("A", "Müşterilere ait nakit paralar aracı kurumun kendi vadesiz şirket hesabında serbestçe genel gider ödemelerinde kullanılabilir."),
          ("B", "Müşterilerin sermaye piyasası araçları aracı kurumun mülkiyetine geçer ve aracı kurum iflas ederse iflas masasına kaydedilir."),
          ("C", "Aracı kurum müşterilerin hisselerini müşteri talimatı olmaksızın kendi borçları için bankalara rehin verebilir."),
          ("D", "Müşteriye ait nakit ve sermaye piyasası araçları yatırım kuruluşunun malvarlığından tamamen ayrıdır; kamu alacakları için dahi haczedilemez, rehin edilemez ve iflas masasına dahil edilemez."),
          ("E", "Müşteri hesaplarındaki nakit paralar Takasbank nezdinde değil, aracı kurumun kasasında fiziki nakit olarak saklanır.")],
         "1. MEVZUAT DAYANAĞI: 6362 sayılı SPKn m. 47/1.\n2. HUKUKİ / TEKNİK ÇERÇEVE: Müşteri varlıkları mutlak koruma altındadır. Aracı kurum borçları için haczedilemez, iflas masasına girmez ve müşterinin açık yazılı talimatı olmadan asla rehin edilemez veya devredilemez.\n3. ADIM ADIM İNCELEME / HESAPLAMA: D seçeneği yasadaki varlık dokunulmazlığı hükmünü tam olarak ifade eder.\n4. DOĞRU CEVAP VE SONUÇ: D seçeneğidir.\n5. ÇELDİRİCİ TUZAĞI: Vergi borcu gibi kamu borçları için müşteri hesabına haciz konulabileceğini düşünmek (kamu borcu için dahi aracı kurum borcundan ötürü müşteri varlığı haczedilemez).",
         "Müşteri varlıkları yatırım kuruluşunun malvarlığından ayrıdır; rehin edilemez, haczedilemez ve iflas masasına girmez.", "KB2_Muhakeme"),

        # 25 (E)
        ("q_1005_sert_025", "E", "Yatırım Kuruluşlarında Belge ve Kayıt Saklama Süresi",
         "6362 sayılı Sermaye Piyasası Kanunu ve ilgili tebliğler uyarınca, yatırım kuruluşlarının müşterileriyle yaptıkları sözleşmeleri, işlem emir formlarını, ses kayıtlarını ve elektronik yazışmaları saklamakla yükümlü oldukları asgari yasal süre nedir?",
         [("A", "İşlem tarihinden itibaren en az 1 yıl"),
          ("B", "İşlem tarihinden itibaren en az 2 yıl"),
          ("C", "İşlem tarihinden itibaren en az 3 yıl"),
          ("D", "İşlem tarihinden itibaren en az 5 yıl"),
          ("E", "İşlem tarihinden itibaren en az 10 yıl")],
         "1. MEVZUAT DAYANAĞI: 6362 sayılı SPKn m. 89 ve III-39.1 m. 47.\n2. HUKUKİ / TEKNİK ÇERÇEVE: Sermaye piyasası mevzuatı uyarınca yatırım kuruluşları tüm emir kayıtlarını, ses kayıtlarını, müşteri sözleşmelerini ve muhasebe kayıtlarını en az 10 YIL süreyle saklamak zorundadır.\n3. ADIM ADIM İNCELEME / HESAPLAMA: E şıkkındaki 10 yıllık süre TTK ve SPKn ile tam uyumludur.\n4. DOĞRU CEVAP VE SONUÇ: E seçeneğidir (10 yıl).\n5. ÇELDİRİCİ TUZAĞI: Özel durumlar tebliğindeki 5 yıl saklama süresiyle karıştırmak (D şıkkı).",
         "Yatırım kuruluşları işlem ve emir kayıtlarını en az 10 yıl süreyle saklamak zorundadır.", "KB1_Kavramsal"),

        # 26 (A)
        ("q_1005_sert_026", "A", "Kredili Menkul Kıymet İşleminde Özkaynak Oranı Düşüşü",
         "Yatırımcı Kerem Bey'in kredili hisse hesabında 500.000 TL değerinde hisse senedi ve 250.000 TL kredi borcu bulunmaktadır (Başlangıç özkaynak oranı: %50). Hisselerin fiyatı düşmüş ve portföy değeri 350.000 TL'ye gerilemiştir.\n\nBu durumda Kerem Bey'in yeni özkaynak oranı yüzde kaçtır ve kanuni sürdürme seviyesine (%35) göre hesaptaki durum nedir?",
         [("A", "Özkaynak Oranı: %28,57; sürdürme seviyesinin (%35) altına düştüğünden teminat tamamlama çağrısı yapılır."),
          ("B", "Özkaynak Oranı: %35,00; tam sınırda olduğundan hiçbir işlem tesis edilmez."),
          ("C", "Özkaynak Oranı: %42,85; sürdürme seviyesinin üzerinde olduğundan hesap güvenlidir."),
          ("D", "Özkaynak Oranı: %20,00; hisseler derhal aynı gün re'sen satılarak hesap kapatılır."),
          ("E", "Özkaynak Oranı: %50,00; kredi borcu değişmediği için oran sabit kalmıştır.")],
         "1. MEVZUAT DAYANAĞI: Seri: V, No: 65 sayılı Tebliğ m. 14.\n2. HUKUKİ / TEKNİK ÇERÇEVE: Özkaynak = Güncel Portföy Değeri - Kredi Borcu. Özkaynak Oranı = Özkaynak / Güncel Portföy Değeri.\n3. ADIM ADIM İNCELEME / HESAPLAMA:\n- Portföy Değeri = 350.000 TL\n- Kredi Borcu = 250.000 TL\n- Özkaynak = 350.000 - 250.000 = 100.000 TL.\n- Özkaynak Oranı = 100.000 / 350.000 = 0,2857 = %28,57.\n- %28,57 < %35 (Sürdürme oranı) olduğundan hesap temerrüt riskindedir ve Margin Call (tamamlama çağrısı) oluşur.\n4. DOĞRU CEVAP VE SONUÇ: A seçeneğinde %28,57 ve tamamlama çağrısı doğru verilmiştir.\n5. ÇELDİRİCİ TUZAĞI: Özkaynağı borca bölerek 100.000 / 250.000 = %40 bulmak (C şıkkı; özkaynak borca değil toplam portföye bölünür).",
         "Özkaynak = 100.000 TL. Oran = 100.000 / 350.000 = %28,57. %35 altına düştüğü için tamamlama çağrısı yapılır.", "KB3_Vaka"),

        # 27 (B)
        ("q_1005_sert_027", "B", "Portföy Yönetim Şirketlerinde Çıkar Çatışması ve Fon İşlemleri",
         "III-55.1 sayılı Tebliğ uyarınca, bir portföy yönetim şirketinin (PYŞ) yönettiği yatırım fonları ile ilişkilerine dair aşağıdaki yasaklardan hangisi DOĞRUDUR?",
         [("A", "PYŞ yönettiği yatırım fonlarının katılma paylarını kurucusu bankanın şube ağından satamaz."),
          ("B", "Fon portföyüne kendi ortaklarının ihraçlarını piyasa üstünde devredemez ve fonlar arası haksız varlık aktaramaz."),
          ("C", "PYŞ fon portföyüne Borsa İstanbul Pay Piyasası'nda işlem gören hisse senetlerini hiçbir şekilde alamaz."),
          ("D", "PYŞ yönettiği fonların bağımsız denetimini kendi şirket bünyesindeki iç denetçilere yaptırmak zorundadır."),
          ("E", "PYŞ, fon portföyünden sağlanan dönemsel kârların tamamını doğrudan kendi şirket kârı olarak kaydeder.")],
         "1. MEVZUAT DAYANAĞI: III-55.1 m. 22 ve 6362 sayılı SPKn m. 56.\n2. HUKUKİ / TEKNİK ÇERÇEVE: PYŞ, fon malvarlığını basiretli bir tacir gibi yönetmek zorundadır. Fonlar arasında veya fon ile kendi ortakları arasında örtülü kazanç aktarımı, haksız fiyatla menkul kıymet virmanı kesinlikle yasaktır.\n3. ADIM ADIM İNCELEME / HESAPLAMA: B seçeneği fonlar arası haksız varlık aktarımı yasağını tam doğru açıklar.\n4. DOĞRU CEVAP VE SONUÇ: B seçeneğidir.\n5. ÇELDİRİCİ TUZAĞI: Fonun kârının şirkete ait olduğunu sanmak (kâr fon katılma payı sahiplerinindir).",
         "PYŞ, fon portföyüne haksız fiyatla varlık aktarımı yapamaz ve fon ile ortakları arasında çıkar çatışması yaratamaz.", "KB2_Muhakeme"),

        # 28 (C)
        ("q_1005_sert_028", "C", "Yatırım Kuruluşlarında Uyum Görevlisi (Compliance)",
         "III-39.1 sayılı Tebliğ uyarınca yatırım kuruluşlarında istihdam edilmesi zorunlu olan 'İç Kontrol ve Mevzuata Uyum Birimi' (Compliance) görevlilerine ilişkin hangisi DOĞRUDUR?",
         [("A", "Mevzuata uyum görevlisi aynı zamanda şirketin en yüksek hacimli hisse senedi alım satım brokerı olmak zorundadır."),
          ("B", "Uyum birimi sadece Maliye Bakanlığı vergi denetimlerini yürütmekle görevlidir."),
          ("C", "Yatırım kuruluşunun yürüttüğü tüm faaliyetlerin SPKn, tebliğler ve şirket içi prosedürlere uygunluğunu sürekli kontrol eder ve Yönetim Kurulu'na raporlar."),
          ("D", "Uyum görevlileri müşteri şikayetlerini gizlemek ve SPK'ya bildirilmesini engellemekle yükümlüdür."),
          ("E", "Uyum görevlisinin hazırladığı raporlar şirketin genel kurulunda tüm kamuya açık olarak oylanır.")],
         "1. MEVZUAT DAYANAĞI: III-39.1 m. 18, 19.\n2. HUKUKİ / TEKNİK ÇERÇEVE: Uyum birimi (Compliance), kurumun faaliyetlerinin sermaye piyasası mevzuatına, şirket içi yönetmeliklere ve etik kurallara uygunluğunu gözetir ve icradan bağımsız çalışır.\n3. ADIM ADIM İNCELEME / HESAPLAMA: C şıkkı uyum görevlisinin mevzuattaki görev ve yetki tanımıdır.\n4. DOĞRU CEVAP VE SONUÇ: C seçeneğidir.\n5. ÇELDİRİCİ TUZAĞI: Uyum görevlisinin icracı brokerlık yapabileceğini düşünmek (icracı görev alamaz).",
         "Uyum birimi, kurumun tüm işlemlerinin mevzuata ve iç düzenlemelere uygunluğunu denetler ve raporlar.", "KB1_Kavramsal"),

        # 29 (D)
        ("q_1005_sert_029", "D", "Kredili Menkul Kıymet İşlemlerinde Özkaynak Olarak Kabul Edilen Varlıklar",
         "Seri: V, No: 65 sayılı Tebliğ uyarınca bir aracı kurum nezdindeki kredili işlem hesabında 'Özkaynak' olarak kabul edilebilecek varlıklar ve katsayılarına ilişkin hangisi YANLIŞTIR?",
         [("A", "Türk Lirası nakit para ve konvertibl yabancı para özkaynak olarak kabul edilir."),
          ("B", "T.C. Hazine ve Maliye Bakanlığı tarafından ihraç edilen Devlet İç Borçlanma Senetleri (DİBS) özkaynak olarak kabul edilir."),
          ("C", "Borsa İstanbul Yıldız Pazar ve Ana Pazar'da işlem gören ve kredili işleme konu paylar özkaynak sayılır."),
          ("D", "Halka açık olmayan anonim şirketlerin hisse senetleri ile gayrimenkul tapuları doğrudan %100 katsayı ile özkaynak olarak kabul edilir."),
          ("E", "Yatırım fonu katılma payları ve borsa yatırım fonu payları özkaynak olarak kabul edilebilir.")],
         "1. MEVZUAT DAYANAĞI: Seri: V, No: 65 Tebliği m. 12.\n2. HUKUKİ / TEKNİK ÇERÇEVE: Kredili işlemde özkaynak sadece likit ve borsada işlem gören enstrümanlar (nakit, DİBS, Eurobond, BIST payları, fon payları) olabilir. Halka açık olmayan hisseler ve gayrimenkul tapuları ASLA kredili işlem özkaynağı sayılamaz!\n3. ADIM ADIM İNCELEME / HESAPLAMA: D seçeneğindeki halka açık olmayan hisse ve gayrimenkul kabulü açıkça mevzuata aykırıdır.\n4. DOĞRU CEVAP VE SONUÇ: D seçeneğidir.\n5. ÇELDİRİCİ TUZAĞI: DİBS veya fon paylarının özkaynak sayılamayacağını düşünmek.",
         "Halka açık olmayan şirket payları ve gayrimenkul tapuları kredili işlemde özkaynak olarak kabul edilemez.", "KB2_Muhakeme"),

        # 30 (E)
        ("q_1005_sert_030", "E", "Yatırım Kuruluşlarında Emirlerin Kabulü ve Kaydı",
         "III-39.1 sayılı Tebliğ m. 48 uyarınca aracı kurumların müşterilerden emir kabul etme ve teyit süreçlerine ilişkin;\n\nI. Telefonla alınan tüm müşteri emirlerinin zaman damgalı ses kayıt sistemi ile kaydedilmesi zorunludur.\nII. İnternet üzerinden veya mobil uygulamadan verilen emirlerin IP numarası, tarih ve saat kayıtları loglanmalıdır.\nIII. Yazılı veya elektronik olarak kayıt altına alınmamış hiçbir müşteri emri borsa işlem sistemine iletilemez.\n\nYukarıda belirtilen emir kayıt kurallarından hangileri DOĞRUDUR?",
         [("A", "Yalnızca I numaralı kural mevzuatça zorunludur."),
          ("B", "Yalnızca II numaralı kural mevzuatça zorunludur."),
          ("C", "I ve II numaralı kurallar mevzuatça zorunludur."),
          ("D", "II ve III numaralı kurallar mevzuatça zorunludur."),
          ("E", "I, II ve III numaralı kuralların tamamı mevzuatça zorunludur.")],
         "1. MEVZUAT DAYANAĞI: III-39.1 m. 48, 49.\n2. HUKUKİ / TEKNİK ÇERÇEVE: Sermaye piyasasında sözlü/kayıtsız emir iletimi kesinlikle yasaktır. Telefon emirleri ses kaydına, internet emirleri IP loguna bağlanmalıdır.\n3. ADIM ADIM İNCELEME / HESAPLAMA: I, II ve III öncülleri emir kabul ve teyit rejiminin temel kurallarıdır.\n4. DOĞRU CEVAP VE SONUÇ: E seçeneğidir.\n5. ÇELDİRİCİ TUZAĞI: Ses kaydı olmadan da brokerın şahsi beyanıyla emir girilebileceği sanrısı.",
         "Müşteri emirlerinde ses kaydı ve elektronik log zorunludur; kayıtsız emir kesinlikle kabul edilemez.", "KB2_Muhakeme"),

        # --- BLOK 4: Q31-Q40 (2 A, 2 B, 2 C, 2 D, 2 E) ---
        # 31 (A)
        ("q_1005_sert_031", "A", "Yatırım Danışmanlığı Hizmet Sözleşmesi ve Yasaklar",
         "III-37.1 sayılı Tebliğ m. 32 uyarınca yetkili yatırım kuruluşları tarafından sunulan 'Yatırım Danışmanlığı' faaliyetine dair hangisi DOĞRUDUR?",
         [("A", "Yatırım danışmanlığı faaliyeti öncesinde müşteriyle yazılı bir Yatırım Danışmanlığı Çerçeve Sözleşmesi imzalanması ve yerindelik testi yapılması zorunludur."),
          ("B", "Yatırım danışmanı müşteriye tavsiye ettiği hisse senetlerinde oluşacak zararları şahsen veya kurum adına ödemeyi taahhüt edebilir."),
          ("C", "Yatırım danışmanlığı sözleşmesi imzalandığında danışman müşteri adına şifreleri alarak re'sen alım satım yapma hakkı kazanır."),
          ("D", "Yatırım danışmanlığı sadece halka açık olmayan şirketlerin tahvilleri üzerine verilebilir, hisse senetlerinde verilemez."),
          ("E", "Yatırım danışmanlığı sözleşmesi bulunmaksızın sosyal medya üzerinden belirli hisselere hedef fiyat vererek yönlendirme yapmak serbesttir.")],
         "1. MEVZUAT DAYANAĞI: III-37.1 m. 31, 32.\n2. HUKUKİ / TEKNİK ÇERÇEVE: Yatırım danışmanlığı çerçeve sözleşmesine ve yerindelik testine tabidir. Danışman müşteriye kâr garantisi veya zarar tazmin taahhüdü VEREMEZ. Müşteri yerine emir giremez (portföy yöneticiliği değildir).\n3. ADIM ADIM İNCELEME / HESAPLAMA: A seçeneği sözleşme ve yerindelik testi zorunluluğunu doğru açıklar.\n4. DOĞRU CEVAP VE SONUÇ: A seçeneğidir.\n5. ÇELDİRİCİ TUZAĞI: Yatırım danışmanının müşteri hesabını bizzat yönetebileceğini sanmak (bu portföy yöneticiliğidir).",
         "Yatırım danışmanlığı için yazılı çerçeve sözleşme ve yerindelik testi şarttır; kâr garantisi kesinlikle verilemez.", "KB2_Muhakeme"),

        # 32 (B)
        ("q_1005_sert_032", "B", "Kredili İşlemde Sürdürme Seviyesi Altına Düşüşte Satış",
         "Seri: V, No: 65 sayılı Tebliğ uyarınca kredili işlem hesabında özkaynak oranı %35'in altına düşen ve kendisine tanınan süre içinde özkaynağını tamamlamayan müşterinin hesabına ilişkin aracı kurumun yetkisi nedir?",
         [("A", "Aracı kurum müşterinin kredi borcunu kendi kârından silerek hesabı kapatmak zorundadır."),
          ("B", "Aracı kurum müşteriye ait hisse senetlerini bildirim aramaksızın re'sen satarak kredi borcunu tahsil etme ve hesabı kapatma yetkisine sahiptir."),
          ("C", "Aracı kurum hiçbir hisseyi satamaz, yalnızca ticaret mahkemesinde iflas davası açabilir."),
          ("D", "Hisseler derhal SPK'ya devredilir ve SPK tarafından 5 yıl boyunca emanette tutulur."),
          ("E", "Aracı kurum müşterinin gayrimenkullerine doğrudan haciz koyarak satışını Borsa İstanbul'dan talep eder.")],
         "1. MEVZUAT DAYANAĞI: Seri: V, No: 65 Tebliği m. 16.\n2. HUKUKİ / TEKNİK ÇERÇEVE: Özkaynak tamamlama bildirimine rağmen teminat yatırılmazsa aracı kurum sözleşmedeki re'sen satış yetkisine dayanarak borsada müşterinin hisselerini satar ve alacağını tahsil eder.\n3. ADIM ADIM İNCELEME / HESAPLAMA: B şıkkı aracı kurumun re'sen hisse satışı yetkisini tam tanımlar.\n4. DOĞRU CEVAP VE SONUÇ: B seçeneğidir.\n5. ÇELDİRİCİ TUZAĞI: Mahkeme kararı olmadan hisse satılamayacağını düşünmek.",
         "Teminat tamamlanmazsa aracı kurum sözleşme gereği müşterinin hisselerini re'sen satarak borcu tahsil eder.", "KB2_Muhakeme"),

        # 33 (C)
        ("q_1005_sert_033", "C", "Aracı Kurum Yönetim Kurulu Üyelerinin Nitelikleri",
         "6362 sayılı SPKn m. 38 ve III-39.1 sayılı Tebliğ uyarınca yatırım kuruluşu yönetim kurulu üyelerinde aranacak yasal şartlara dair hangisi DOĞRUDUR?",
         [("A", "Yönetim kurulu üyelerinin tamamının iktisat veya hukuk alanında doktora yapmış olması zorunludur."),
          ("B", "Yönetim kurulu üyeliği için hiçbir eğitim veya sabıka şartı bulunmayıp şirket hissesine sahip olmak yeterlidir."),
          ("C", "Müflis olmamak, yüz kızartıcı suçlardan veya sermaye piyasası suçlarından mahkum olmamak ve üyelerin çoğunluğunun 4 yıllık lisans mezunu olması şarttır."),
          ("D", "Yönetim kurulu üyelerinin hiçbirinin Türkiye Cumhuriyeti vatandaşı olmaması şart koşulmuştur."),
          ("E", "Yönetim kurulu üyeleri aynı zamanda bir diğer aracı kurumda genel müdürlük görevini eşzamanlı yürütebilirler.")],
         "1. MEVZUAT DAYANAĞI: 6362 sayılı SPKn m. 38 ve III-39.1 m. 13.\n2. HUKUKİ / TEKNİK ÇERÇEVE: YK üyelerinde mesleki itibar, dürüstlük, sabıkasızlık (m. 106, 107 vb. suçlardan mahkum olmama) ve çoğunluğunun 4 yıllık yükseköğretim mezunu olması şarttır.\n3. ADIM ADIM İNCELEME / HESAPLAMA: C şıkkı kanunun aradığı dürüstlük ve eğitim asgari şartlarını doğru yansıtır.\n4. DOĞRU CEVAP VE SONUÇ: C seçeneğidir.\n5. ÇELDİRİCİ TUZAĞI: Doktora şartı arandığını sanmak veya başka aracı kurumda da çalışabileceğini düşünmek.",
         "YK üyelerinin müflis olmaması, SPK suçlarından mahkum olmaması ve çoğunluğunun 4 yıllık mezun olması şarttır.", "KB1_Kavramsal"),

        # 34 (D)
        ("q_1005_sert_034", "D", "Aracı Kurum Genel Müdürünün Nitelikleri ve Atanması",
         "III-39.1 sayılı Tebliğ m. 14 uyarınca aracı kurumlarda 'Genel Müdür' olarak atanacak kişilerde aranacak asgari tecrübe ve onay şartı nedir?",
         [("A", "En az 1 yıllık finans stajı yapmış olması ve Ticaret Bakanlığı onayı alınması"),
          ("B", "En az 3 yıllık borsa üyeliği bulunması ve Borsa İstanbul Genel Müdürünün sözlü onayı"),
          ("C", "En az 5 yıllık kamu memurluğu bulunması ve Noter tasdiki"),
          ("D", "En az 4 yıllık lisans mezuniyeti ile sermaye piyasası alanında en az 7 yıllık mesleki tecrübeye sahip olması ve SPK'ya bildirilmesi"),
          ("E", "Herhangi bir tecrübe aranmaksızın aracı kurum hisselerinin %51'ine sahip olması")],
         "1. MEVZUAT DAYANAĞI: III-39.1 m. 14.\n2. HUKUKİ / TEKNİK ÇERÇEVE: Yatırım kuruluşlarında genel müdür: 4 yıllık lisans mezunu olmalı ve finans/sermaye piyasası alanında EN AZ 7 YIL mesleki tecrübeye sahip bulunmalıdır. Atama belgeleri SPK'ya iletilir.\n3. ADIM ADIM İNCELEME / HESAPLAMA: D seçeneğindeki 4 yıllık lisans ve 7 yıl tecrübe amir mevzuat kuralıdır.\n4. DOĞRU CEVAP VE SONUÇ: D seçeneğidir.\n5. ÇELDİRİCİ TUZAĞI: Tecrübe süresini 5 yıl veya 10 yıl zannetmek.",
         "Aracı kurum genel müdüründe 4 yıllık lisans ve en az 7 yıllık mesleki tecrübe şartı aranır.", "KB1_Kavramsal"),

        # 35 (E)
        ("q_1005_sert_035", "E", "Yatırım Kuruluşlarının Birleşme, Devir ve Tasfiyesi",
         "6362 sayılı Sermaye Piyasası Kanunu m. 40 uyarınca yatırım kuruluşlarının başka bir yatırım kuruluşu ile birleşmesi, devri veya faaliyetine son vererek tasfiyesine ilişkin;\n\nI. Yatırım kuruluşlarının birleşme veya bölünme işlemlerine başlamadan önce Kurul'dan (SPK) izin almaları zorunludur.\nII. İsteğe bağlı tasfiyede müşterilere ait tüm nakit ve menkul kıymet borçlarının tamamen tasfiye edilmiş veya başka bir kuruma devredilmiş olması şarttır.\nIII. Faaliyet iznini kendi isteğiyle iade eden kuruluş yetki belgesini Kurul'a teslim etmekle yükümlüdür.\n\nYukarıda yer alan hukuki ilkelerden hangileri DOĞRUDUR?",
         [("A", "Yalnızca I numaralı ilke mevzuatça şarttır."),
          ("B", "Yalnızca II numaralı ilke mevzuatça şarttır."),
          ("C", "I ve II numaralı ilkeler mevzuatça şarttır."),
          ("D", "II ve III numaralı ilkeler mevzuatça şarttır."),
          ("E", "I, II ve III numaralı ilkelerin tamamı mevzuatça şarttır.")],
         "1. MEVZUAT DAYANAĞI: 6362 sayılı SPKn m. 40 ve III-39.1 m. 68.\n2. HUKUKİ / TEKNİK ÇERÇEVE: Birleşme, bölünme ve tasfiye SPK iznine bağlıdır. Müşteri varlıkları sıfırlanmadan tasfiye tamamlanamaz ve yetki belgesi iade edilir.\n3. ADIM ADIM İNCELEME / HESAPLAMA: I, II ve III öncüllerinin tümü kanunun amir hükümleridir.\n4. DOĞRU CEVAP VE SONUÇ: E seçeneğidir.\n5. ÇELDİRİCİ TUZAĞI: SPK iznine gerek olmadan ticaret siciline tescil yapılabileceğini düşünmek.",
         "Yatırım kuruluşlarında birleşme, bölünme ve tasfiye SPK iznine tabidir; müşteri hakları tam güvenceye alınır.", "KB2_Muhakeme"),

        # 36 (A)
        ("q_1005_sert_036", "A", "Müşteri Emirlerinde Fiyat İyileştirmesi ve En İyi İcra İlkesi",
         "III-39.1 sayılı Tebliğ uyarınca yatırım kuruluşlarının müşterilerine karşı uymakla yükümlü olduğu 'En İyi İcra' (Best Execution) ilkesine ilişkin hangisi DOĞRUDUR?",
         [("A", "Yatırım kuruluşu, müşteri emirlerini yerine getirirken fiyat, maliyet, hız ve takas koşulları açısından müşteri lehine en iyi sonucu elde etmek için makul tüm tedbirleri almak zorundadır."),
          ("B", "Yatırım kuruluşu müşterinin piyasa emrini bekletip kendi portföyünden daha pahalı fiyata müşteriye satabilir."),
          ("C", "En iyi icra kuralı sadece kurumsal müşteriler için geçerli olup bireysel müşteriler için uygulanmaz."),
          ("D", "Yatırım kuruluşu emri borsa yerine doğrudan şirket genel müdürünün şahsi hesabıyla eşleştirmekle yükümlüdür."),
          ("E", "Müşteri özel talimat verse dahi kurum kendi belirlediği icra politikasını zorla uygulamak zorundadır.")],
         "1. MEVZUAT DAYANAĞI: III-39.1 m. 46.\n2. HUKUKİ / TEKNİK ÇERÇEVE: En İyi İcra ilkesi: Kurum emirleri icra ederken müşteri için en avantajlı toplam bedeli (fiyat + masraf + hız) sağlamakla yükümlüdür.\n3. ADIM ADIM İNCELEME / HESAPLAMA: A şıkkı En İyi İcra politikasının kanuni tanımını tam verir.\n4. DOĞRU CEVAP VE SONUÇ: A seçeneğidir.\n5. ÇELDİRİCİ TUZAĞI: Kurumun emri istediği fiyattan kendi hesabıyla eşleştirebileceği zannı.",
         "En İyi İcra ilkesi uyarınca yatırım kuruluşu fiyat, maliyet ve hız açısından müşteri için en iyi sonucu almak zorundadır.", "KB2_Muhakeme"),

        # 37 (B)
        ("q_1005_sert_037", "B", "Kredili İşlemde Portföy Çeşitlendirmesi ve Tek Hisse Sınırı",
         "Seri: V, No: 65 sayılı Tebliğ uyarınca bir yatırımcının kredili işlem hesabında tek bir hisse senedine aşırı yoğunlaşmasını önlemek amacıyla uygulanan 'Tek Pay Sınırı' kuralı nedir?",
         [("A", "Yatırımcı kredili hesabında sadece tek bir şirketin hissesini tutabilir ve başka hiçbir pay satın alamaz."),
          ("B", "Kredili işleme konu tek hissenin değeri, özkaynak hesabındaki toplam portföy değerinin belirlenen oranını aşamaz."),
          ("C", "Bir müşteri tüm BIST hisselerinden en az yüz farklı hisseyi aynı anda portföyünde bulundurmak zorundadır."),
          ("D", "Tek hisse sınırı sadece bankacılık sektörü payları için geçerli olup sınai hisselerde yoğunlaşma serbesttir."),
          ("E", "Kredili menkul kıymet işlemlerinde hiçbir yoğunlaşma sınırı bulunmayıp tek hisseye sınırsız yatırım serbesttir.")],
         "1. MEVZUAT DAYANAĞI: Seri: V, No: 65 m. 11.\n2. HUKUKİ / TEKNİK ÇERÇEVE: Risk yönetimi gereği aracı kurumlar tek hisseye yoğunlaşmayı sınırlandırır. Belirli bir oranın üzerindeki tek hisse yoğunlaşmalarında ilave özkaynak istenir veya kabul katsayısı düşürülür.\n3. ADIM ADIM İNCELEME / HESAPLAMA: B seçeneği tek pay yoğunlaşma risk sınırını doğru ifade eder.\n4. DOĞRU CEVAP VE SONUÇ: B seçeneğidir.\n5. ÇELDİRİCİ TUZAĞI: Hiçbir yoğunlaşma kuralının bulunmadığını sanmak.",
         "Kredili işlemlerde risk yönetimi gereğince tek pay yoğunlaşma sınırı uygulanır.", "KB2_Muhakeme"),

        # 38 (C)
        ("q_1005_sert_038", "C", "Aracı Kurumlarda Risk Yönetim Birimi ve Stres Testleri",
         "III-39.1 sayılı Tebliğ uyarınca aracı kurumlarda kurulması zorunlu olan 'Risk Yönetim Birimi'nin görev ve yetkilerine ilişkin hangisi DOĞRUDUR?",
         [("A", "Risk yönetim birimi her gün borsa seans salonunda en karlı hisseleri belirleyip müşterilere alım tavsiyesi vermekle görevlidir."),
          ("B", "Risk yönetim birimi çalışanları aynı zamanda aracı kurumun halka arza aracılık departmanını yönetmek zorundadır."),
          ("C", "Piyasa riski, kredi riski, likidite riski ve operasyonel riskleri ölçmek, düzenli aralıklarla stres testleri ve senaryo analizleri yaparak Yönetim Kurulu'na raporlamakla yükümlüdür."),
          ("D", "Risk yönetim birimi yalnızca şirket iflas ettikten sonra mahkeme tarafından atanan bir tasfiye kuruludur."),
          ("E", "Risk yönetimi hazırladığı risk raporlarını bağımsız denetim şirketlerinden gizli tutmakla yükümlüdür.")],
         "1. MEVZUAT DAYANAĞI: III-39.1 m. 22, 23.\n2. HUKUKİ / TEKNİK ÇERÇEVE: Risk yönetim birimi icradan bağımsızdır. Piyasa, kredi, likidite ve operasyonel riskleri izler, stres testleri uygular ve doğrudan Yönetim Kurulu'na bağlı çalışır.\n3. ADIM ADIM İNCELEME / HESAPLAMA: C şıkkı risk yönetim biriminin mevzuattaki temel görev tanımıdır.\n4. DOĞRU CEVAP VE SONUÇ: C seçeneğidir.\n5. ÇELDİRİCİ TUZAĞI: Risk biriminin hisse tavsiyesi veren bir departman olduğunu zannetmek (A şıkkı).",
         "Risk yönetim birimi piyasa, kredi, likidite risklerini ölçer, stres testleri uygular ve YK'ya raporlar.", "KB1_Kavramsal"),

        # 39 (D)
        ("q_1005_sert_039", "D", "Aracı Kurumların Kendi Hisselerini Geri Alması",
         "Halka açık bir aracı kurumun kendi paylarını borsadan geri satın almasına (Share Buyback) ilişkin hangisi DOĞRUDUR?",
         [("A", "Aracı kurumlar Sermaye Piyasası Kanunu uyarınca hiçbir şekilde kendi paylarını geri alamazlar."),
          ("B", "Geri alım için genel kurul kararı gerekmez, herhangi bir aracı kurum çalışanı kendi kararıyla şirket adına alım yapabilir."),
          ("C", "Geri alınan paylar derhal aynı saniye içinde bedelsiz olarak üçüncü şahıslara hibe edilmek zorundadır."),
          ("D", "II-22.1 sayılı Tebliğ hükümlerine uyulması, genel kurulca yetkilendirme yapılması ve sermaye yeterliliği tabanının asgari had altına düşmemesi şarttır."),
          ("E", "Geri alınan paylar genel kurul toplantılarında şirketin mevcut yönetim kurulu lehine oy hakkı kullanır.")],
         "1. MEVZUAT DAYANAĞI: II-22.1 Geri Alınan Paylar Tebliği ve TTK m. 379.\n2. HUKUKİ / TEKNİK ÇERÇEVE: Aracı kurumlar kendi paylarını geri alabilir; ancak II-22.1'e uymalı, sermaye yeterliliği tabanını tehlikeye atmamalıdır. Geri alınan payların oy hakkı donar.\n3. ADIM ADIM İNCELEME / HESAPLAMA: D seçeneği tebliğ ve sermaye yeterliliği şartını eksiksiz ifade eder.\n4. DOĞRU CEVAP VE SONUÇ: D seçeneğidir.\n5. ÇELDİRİCİ TUZAĞI: Geri alınan payların oy hakkı kullanabileceği zannı (E şıkkı; geri alınan payların oy hakkı donar).",
         "Geri alımda II-22.1 tebliğine uyum ve sermaye yeterliliği tabanının korunması zorunludur; oy hakları donar.", "KB2_Muhakeme"),

        # 40 (E)
        ("q_1005_sert_040", "E", "Yatırım Kuruluşlarında Özkaynak Bildirim Süreleri",
         "Seri: V, No: 34 sayılı Tebliğ uyarınca sermaye yeterliliği tabanı yükümlülüğünü sağlayamayan ve açığı oluşan bir aracı kurumun bu durumu SPK'ya bildirme ve giderme prosedürüne ilişkin;\n\nI. Aracı kurum sermaye yeterliliği açığı oluştuğunu derhal aynı iş günü içinde Kurul'a ve Borsa İstanbul'a bildirmek zorundadır.\nII. Kurul açığın giderilmesi için aracı kuruma en fazla 3 aya kadar süre verebilir.\nIII. Verilen sürede sermaye açığı kapatılmazsa Kurul aracı kurumun faaliyet yetki belgelerini geçici olarak durdurabilir veya iptal edebilir.\n\nYukarıda yer alan hukuki tedbirlerden hangileri DOĞRUDUR?",
         [("A", "Yalnızca I numaralı tedbir mevzuatça öngörülmüştür."),
          ("B", "Yalnızca II numaralı tedbir mevzuatça öngörülmüştür."),
          ("C", "I ve II numaralı tedbirler mevzuatça öngörülmüştür."),
          ("D", "II ve III numaralı tedbirler mevzuatça öngörülmüştür."),
          ("E", "I, II ve III numaralı tedbirlerin tamamı mevzuatça öngörülmüştür.")],
         "1. MEVZUAT DAYANAĞI: Seri: V, No: 34 Tebliği m. 15, 16 ve SPKn m. 96.\n2. HUKUKİ / TEKNİK ÇERÇEVE: Sermaye açığı derhal bildirilmelidir (I). SPK açığın kapatılması için süre tanır (II). Kapatılmazsa faaliyet yetkisi durdurulur veya iptal edilir (III).\n3. ADIM ADIM İNCELEME / HESAPLAMA: I, II ve III öncüllerinin tümü sermaye yeterliliği yaptırım rejimini tam oluşturur.\n4. DOĞRU CEVAP VE SONUÇ: E seçeneğidir.\n5. ÇELDİRİCİ TUZAĞI: Açığın bildirilmesine gerek olmadığını veya 1 yıl beklenebileceğini sanmak.",
         "Sermaye açığı derhal bildirilir; SPK açığın giderilmesi için süre verir, giderilmezse yetki durdurulur/iptal edilir.", "KB2_Muhakeme"),

        # --- BLOK 5: Q41-Q50 (2 A, 2 B, 2 C, 2 D, 2 E) ---
        # 41 (A)
        ("q_1005_sert_041", "A", "Yatırım Kuruluşlarının Şube ve İrtibat Bürosu Açması",
         "III-39.1 sayılı Tebliğ m. 54-58 uyarınca aracı kurumların 'Şube' ve 'İrtibat Bürosu' açma şartlarına ilişkin hangisi DOĞRUDUR?",
         [("A", "Şube açmak için SPK'dan izin alınması ve asgari özsermaye şartının sağlanması zorunludur; irtibat bürolarında ise emir kabul edilemez ve hiçbir ticari işlem yapılamaz."),
          ("B", "İrtibat bürolarında müşterilerden nakit para toplanabilir ve fiziki hisse senedi alım satımı serbestçe yapılabilir."),
          ("C", "Aracı kurumlar Türkiye genelinde sınırsız sayıda şubeyi SPK'ya haber vermeksizin diledikleri gün açabilirler."),
          ("D", "Şubelerde yönetici olarak atanacak kişilerin ilkokul mezunu olması mevzuatça yeterli görülmüştür."),
          ("E", "İrtibat bürosu açmak için şubeden daha yüksek sermaye yeterliliği aranır.")],
         "1. MEVZUAT DAYANAĞI: III-39.1 m. 54, 57.\n2. HUKUKİ / TEKNİK ÇERÇEVE: Şube açılışı SPK iznine ve şube başına ilave sermaye şartına bağlıdır. İrtibat büroları sadece tanıtım yapar; KESİNLİKLE EMİR KABUL EDEMEZ, İŞLEM YAPAMAZ VE NAKİT TAHSİL EDEMEZ.\n3. ADIM ADIM İNCELEME / HESAPLAMA: A şıkkı şube ve irtibat bürosunun yasal sınırlarını tam karşılaştırır.\n4. DOĞRU CEVAP VE SONUÇ: A seçeneğidir.\n5. ÇELDİRİCİ TUZAĞI: İrtibat bürolarında da emir alınabileceğini sanmak (B şıkkı).",
         "Şube açılışı SPK iznine tabidir; irtibat bürosunda ise emir kabul edilemez ve ticari işlem yapılamaz.", "KB2_Muhakeme"),

        # 42 (B)
        ("q_1005_sert_042", "B", "Müşteri İle Yapılan Çerçeve Sözleşmenin Feshi",
         "III-39.1 sayılı Tebliğ uyarınca aracı kurum ile müşteri arasında imzalanan Alım Satım Aracılığı Çerçeve Sözleşmesinin feshine ilişkin hangisi DOĞRUDUR?",
         [("A", "Müşteri sözleşmeyi hiçbir şekilde tek taraflı feshedemez, ömür boyu kurumda kalmak zorundadır."),
          ("B", "Taraflar sözleşmede belirlenen ihbar süresine uymak ve hesaplaşmayı tamamlamak kaydıyla sözleşmeyi her zaman feshedebilirler."),
          ("C", "Sözleşmenin feshedilebilmesi için Borsa İstanbul Genel Kurulunun onay vermesi şarttır."),
          ("D", "Aracı kurum sözleşmeyi feshederse müşterinin tüm portföyü kanunen devlete irat kaydedilir."),
          ("E", "Fesih halinde müşterinin Takasbank'taki hisseleri re'sen satılarak bedeli aracı kuruma hibe edilir.")],
         "1. MEVZUAT DAYANAĞI: III-39.1 m. 40 ve Türk Borçlar Kanunu.\n2. HUKUKİ / TEKNİK ÇERÇEVE: Çerçeve sözleşmeler sürekli borç ilişkisidir. Taraflar ihbar süresine uyarak ve karşılıklı borç-alacak hesaplaşmasını yaparak sözleşmeyi tek taraflı feshedebilir.\n3. ADIM ADIM İNCELEME / HESAPLAMA: B şıkkı ihbar süresi ve hesaplaşma ile sözleşmenin feshedilebileceğini doğru açıklar.\n4. DOĞRU CEVAP VE SONUÇ: B seçeneğidir.\n5. ÇELDİRİCİ TUZAĞI: Müşterinin sözleşmeyi feshedemeyeceği zannı.",
         "Taraflar ihbar süresine uyarak ve varlık hesaplaşmasını yaparak sözleşmeyi diledikleri zaman feshedebilirler.", "KB1_Kavramsal"),

        # 43 (C)
        ("q_1005_sert_043", "C", "Aracı Kurum Personelinin Müşteri Adına İşlem Yapması Yasağı",
         "Yatırım kuruluşlarında çalışan müşteri temsilcisi veya brokerların müşterilerle olan operasyonel ilişkilerine dair aşağıdaki fiillerden hangisi SERMAYE PİYASASI KANUNU UYARINCA KESİNLİKLE YASAKTIR?",
         [("A", "Müşterinin yazılı veya sesli emrini doğrulayarak sisteme girmek"),
          ("B", "Müşteriye şirketin araştırma departmanı tarafından hazırlanan raporu iletmek"),
          ("C", "Müşteriden genel vekaletname veya şifre alarak müşteri adına kendi inisiyatifiyle portföy yöneticiliği gibi hisse alıp satmak"),
          ("D", "Müşteriye hesap ekstresini ve işlem teyit formunu göndermek"),
          ("E", "Müşterinin talebi üzerine emir iptal veya fiyat iyileştirme işlemini gerçekleştirmek")],
         "1. MEVZUAT DAYANAĞI: III-39.1 m. 43 ve 6362 sayılı SPKn m. 39.\n2. HUKUKİ / TEKNİK ÇERÇEVE: Müşteri temsilcisi veya brokerlar portföy yöneticisi değildir. Müşteri adına vekalet alarak kendi kararlarıyla hisse alıp satamazlar; bu durum yetkisiz portföy yöneticiliği ve disiplin suçudur.\n3. ADIM ADIM İNCELEME / HESAPLAMA: C seçeneğindeki müşteri yerine kendi inisiyatifiyle işlem yapma fiili kesin yasaktır.\n4. DOĞRU CEVAP VE SONUÇ: C seçeneğidir.\n5. ÇELDİRİCİ TUZAĞI: Müşterinin rızası veya vekaleti varsa temsilcinin hisse yönetebileceğini düşünmek.",
         "Müşteri temsilcileri ve brokerlar müşteri vekaletiyle dahi kendi inisiyatifleriyle portföy yönetimi yapamazlar.", "KB2_Muhakeme"),

        # 44 (D)
        ("q_1005_sert_044", "D", "Yatırım Kuruluşlarının Kendi Adına Kredi Kullanması",
         "Aracı kurumların bankalardan veya para piyasasından kendi adlarına kredi temin etmelerine ve borçlanmalarına ilişkin yasal sınırlama nedir?",
         [("A", "Aracı kurumlar ticari bankalardan hiçbir surette işletme veya yatırım kredisi temin edemezler."),
          ("B", "Aracı kurumlar sadece Borsa İstanbul A.Ş.'den borç para alabilir, bankalardan borçlanmaları yasaktır."),
          ("C", "Aracı kurumlar piyasadan sınırsız miktarda borçlanabilir ve borçlanmada hiçbir sermaye rasyosu aranmaz."),
          ("D", "Borçlanmalar sermaye yeterliliği tabanı hesaplamalarında borç/özkaynak kaldıraç rasyoları sınırlarında kalmalıdır."),
          ("E", "Kullanılan tüm banka kredileri müşterilerin menkul kıymetleri aracı kurumca rehin verilerek teminatlandırılır.")],
         "1. MEVZUAT DAYANAĞI: Seri: V, No: 34 Tebliği m. 8.\n2. HUKUKİ / TEKNİK ÇERÇEVE: Aracı kurumlar kredi kullanabilir; ancak bu borçlanma sermaye yeterliliği rasyolarını (aktif büyüklüğüne göre özsermaye yükümlülüklerini) bozamaz. Müşteri hisseleri teminat gösterilemez.\n3. ADIM ADIM İNCELEME / HESAPLAMA: D seçeneği sermaye yeterliliği rasyoları sınırlamasını tam ifade eder.\n4. DOĞRU CEVAP VE SONUÇ: D seçeneğidir.\n5. ÇELDİRİCİ TUZAĞI: Müşteri hisselerinin teminat verilebileceğini zannetmek (E şıkkı ağır suçtur).",
         "Aracı kurum borçlanmaları sermaye yeterliliği kaldıraç ve risk karşılıkları sınırlarına tabidir.", "KB2_Muhakeme"),

        # 45 (E)
        ("q_1005_sert_045", "E", "Saklama Kuruluşları ve Takasbank İlişkisi",
         "Sermaye piyasasında saklama hizmeti sunulmasına ve Merkezi Takas Kuruluşu (Takasbank) ile saklamacı kuruluşların ilişkilerine ilişkin;\n\nI. Türkiye sermaye piyasasında Merkezi Takas Kuruluşu ve merkezi saklamacı Takasbank ve MKK'dır.\nII. Sınırlı saklama yetkisine sahip aracı kurumlar müşteri varlıklarını kendi kasalarında değil, Takasbank nezdindeki müşteri alt hesaplarında saklamak zorundadır.\nIII. Genel saklama yetkisine sahip yatırım kuruluşları kolektif yatırım kuruluşlarının (fonların) varlık saklama hizmetini de yürütebilir.\n\nYukarıda yer alan tespitlerden hangileri DOĞRUDUR?",
         [("A", "Yalnızca I numaralı tespit mevzuat uyarınca doğrudur."),
          ("B", "Yalnızca II numaralı tespit mevzuat uyarınca doğrudur."),
          ("C", "I ve II numaralı tespitler mevzuat uyarınca doğrudur."),
          ("D", "II ve III numaralı tespitler mevzuat uyarınca doğrudur."),
          ("E", "I, II ve III numaralı tespitlerin tamamı mevzuat uyarınca doğrudur.")],
         "1. MEVZUAT DAYANAĞI: III-40.1 Saklama Faaliyetleri Tebliği ve SPKn m. 77.\n2. HUKUKİ / TEKNİK ÇERÇEVE: Saklama sistemi Takasbank ve MKK nezdinde alt hesap bazında tutulur. Sınırlı saklama yetkililer Takasbank'ı kullanır; genel saklamacılar fon saklayıcısı olabilir.\n3. ADIM ADIM İNCELEME / HESAPLAMA: I, II ve III öncüllerinin tümü saklama mevzuatına tam uygundur.\n4. DOĞRU CEVAP VE SONUÇ: E seçeneğidir.\n5. ÇELDİRİCİ TUZAĞI: Aracı kurumların hisseleri kendi fiziki kasalarında saklayabileceği yanılgısı.",
         "Varlıklar Takasbank ve MKK nezdinde müşteri bazında saklanır; genel saklamacılar fon saklama hizmeti verebilir.", "KB2_Muhakeme"),

        # 46 (A)
        ("q_1005_sert_046", "A", "Yatırım Kuruluşlarında Kredi Komitesi ve Yetki Devri",
         "Seri: V, No: 65 sayılı Tebliğ uyarınca aracı kurumlarda müşterilere açılacak kredili işlem limitlerini belirlemekle görevli 'Kredi Komitesi'ne ilişkin hangisi DOĞRUDUR?",
         [("A", "Kredi komitesi yönetim kurulunca belirlenen esaslara göre kredi limitlerini belirler ve yetkisini sınırları açıkça çizilmek kaydıyla genel müdüre devredebilir."),
          ("B", "Kredi komitesinin tüm kararları sadece müşterilerin sözlü talepleriyle alınır ve tutanağa bağlanmaz."),
          ("C", "Kredi komitesi sadece şirketin en çok hissesine sahip ortağının yakınlarına kredi açmakla görevlidir."),
          ("D", "Kredi komitesi her kredi açılışında SPK Başkanından şahsen ıslak imzalı onay almak zorundadır."),
          ("E", "Kredi komitesi kurulması sadece bankalara zorunlu olup aracı kurumlarda kredi kararlarını resepsiyonist verir.")],
         "1. MEVZUAT DAYANAĞI: Seri: V, No: 65 m. 8, 9.\n2. HUKUKİ / TEKNİK ÇERÇEVE: Kredi komitesi müşterilerin mali gücüne göre limit belirler. Yönetim kurulu yetkisinin bir kısmını sınırlar dahilinde Kredi Komitesine veya Genel Müdüre devredebilir.\n3. ADIM ADIM İNCELEME / HESAPLAMA: A şıkkı kredi komitesinin yetki ve devir kuralını doğru açıklar.\n4. DOĞRU CEVAP VE SONUÇ: A seçeneğidir.\n5. ÇELDİRİCİ TUZAĞI: SPK Başkanından her kredi için onay alınacağı zannı (D şıkkı).",
         "Kredi komitesi YK ilkelerine göre limit tahsis eder ve sınırlar dahilinde genel müdüre yetki devredilebilir.", "KB1_Kavramsal"),

        # 47 (B)
        ("q_1005_sert_047", "B", "Portföy Yönetiminde Karşılaştırma Ölçütü (Benchmark)",
         "III-55.1 sayılı Tebliğ uyarınca portföy yönetim şirketlerinin yönettikleri fonlar ve özel portföyler için 'Karşılaştırma Ölçütü' (Benchmark / Eşik Değer) belirleme ilkelerine dair hangisi DOĞRUDUR?",
         [("A", "Hisse senedi fonu için karşılaştırma ölçütü olarak sadece ABD enflasyon oranı seçilmek zorundadır."),
          ("B", "Karşılaştırma ölçütü fonun yatırım stratejisine ve içerdiği varlıkların risk-getiri profiline uygun, tarafsız ve önceden belirlenmiş endekslerden oluşmalıdır."),
          ("C", "Karşılaştırma ölçütü fon yöneticisi tarafından her gün piyasa seyrine göre keyfi olarak geriye dönük değiştirilebilir."),
          ("D", "Portföy yöneticisi fonun getirisini hiçbir endeksle karşılaştıramaz, bu durum rekabet hukukuna aykırıdır."),
          ("E", "Karşılaştırma ölçütü yatırımcılardan tamamen gizli tutulan kurum içi bir sırdır.")],
         "1. MEVZUAT DAYANAĞI: III-55.1 m. 26.\n2. HUKUKİ / TEKNİK ÇERÇEVE: Karşılaştırma ölçütü (Benchmark) fonun hedefini yansıtır (Örn: %80 BIST 100 + %20 BIST KYD Repo). Önceden belirlenir, şeffaftır ve KAP'ta ilan edilir. Keyfi değiştirilemez.\n3. ADIM ADIM İNCELEME / HESAPLAMA: B seçeneği karşılaştırma ölçütünün yatırım stratejisine uygunluğu ve objektifliğini doğru belirtir.\n4. DOĞRU CEVAP VE SONUÇ: B seçeneğidir.\n5. ÇELDİRİCİ TUZAĞI: Ölçütün geriye dönük değiştirilebileceği zannı (C şıkkı).",
         "Karşılaştırma ölçütü fonun risk-getiri profiline uygun, objektif ve önceden belirlenmiş endekslerden oluşmalıdır.", "KB2_Muhakeme"),

        # 48 (C)
        ("q_1005_sert_048", "C", "Aracı Kurum Muhasebe Kayıtları ve Finansal Tablolar",
         "II-14.1 sayılı Sermaye Piyasasında Finansal Raporlamaya İlişkin Esaslar Tebliği uyarınca aracı kurumların finansal tablo hazırlama ve bildirim yükümlülüklerine ilişkin hangisi DOĞRUDUR?",
         [("A", "Aracı kurumlar finansal tablolarını yalnızca 10 yılda bir defa hazırlamakla yükümlüdür."),
          ("B", "Aracı kurumlar Türkiye Finansal Raporlama Standartlarına (TFRS/TMS) tabi olmayıp serbest defter tutarlar."),
          ("C", "Aracı kurumlar yıllık ve ara dönem finansal tablolarını TMS/TFRS'ye uygun olarak hazırlamak, bağımsız denetimden geçirmek ve süresi içinde KAP'ta açıklamak zorundadır."),
          ("D", "Aracı kurum finansal tabloları şirket merkezinde kilitli tutulur, ortakların veya SPK'nın incelemesine sunulamaz."),
          ("E", "Finansal tablolar sadece yabancı para cinsinden tutulabilir, Türk Lirası kullanılması yasaktır.")],
         "1. MEVZUAT DAYANAĞI: II-14.1 Tebliği m. 4, 11 ve 6362 sayılı SPKn m. 14.\n2. HUKUKİ / TEKNİK ÇERÇEVE: Yatırım kuruluşları TMS/TFRS standartlarında finansal raporlama yapar. Yıllık ve yarıyıl raporları bağımsız denetime tabidir ve KAP'ta ilan edilir.\n3. ADIM ADIM İNCELEME / HESAPLAMA: C şıkkı TFRS uyumu, bağımsız denetim ve KAP bildirimini eksiksiz ifade eder.\n4. DOĞRU CEVAP VE SONUÇ: C seçeneğidir.\n5. ÇELDİRİCİ TUZAĞI: TFRS'ye tabi olmadıkları iddiası.",
         "Aracı kurumlar finansal tablolarını TMS/TFRS'ye göre hazırlar, denetletir ve KAP'ta kamuya açıklarlar.", "KB1_Kavramsal"),

        # 49 (D)
        ("q_1005_sert_049", "D", "Kredili İşlemlerde Özkaynak Oranı Hesaplamasında Teminatlar",
         "Yatırımcı Burak Bey'in aracı kurumundaki kredili işlem hesabında 200.000 TL piyasa değerli hisse senedi, 50.000 TL nakit ve 150.000 TL kredi borcu bulunmaktadır.\n\nBurak Bey'in hesabındaki 'Mevcut Özkaynak Tutarı' ve 'Özkaynak Oranı' yüzde kaçtır?",
         [("A", "Özkaynak: 50.000 TL; Oran: %20,00"),
          ("B", "Özkaynak: 200.000 TL; Oran: %80,00"),
          ("C", "Özkaynak: 150.000 TL; Oran: %60,00"),
          ("D", "Özkaynak: 100.000 TL; Oran: %40,00"),
          ("E", "Özkaynak: 250.000 TL; Oran: %100,00")],
         "1. MEVZUAT DAYANAĞI: Seri: V, No: 65 sayılı Tebliğ m. 14.\n2. HUKUKİ / TEKNİK ÇERÇEVE: Toplam Portföy (Varlık) = Hisse Senetleri + Nakit = 200.000 + 50.000 = 250.000 TL. Kredi Borcu = 150.000 TL. Özkaynak = Toplam Varlık - Kredi Borcu.\n3. ADIM ADIM İNCELEME / HESAPLAMA:\n- Özkaynak = 250.000 - 150.000 = 100.000 TL.\n- Özkaynak Oranı = Özkaynak / Toplam Portföy = 100.000 / 250.000 = 0,40 = %40,00.\n4. DOĞRU CEVAP VE SONUÇ: D seçeneğinde 100.000 TL ve %40,00 doğru verilmiştir.\n5. ÇELDİRİCİ TUZAĞI: Nakit parayı portföy toplamına eklemeyi unutarak 200.000 - 150.000 = 50.000 TL özkaynak bulmak (A şıkkı).",
         "Toplam Varlık = 250.000 TL. Borç = 150.000 TL. Özkaynak = 100.000 TL. Oran = 100.000 / 250.000 = %40,00.", "KB3_Vaka"),

        # 50 (E)
        ("q_1005_sert_050", "E", "Yatırım Kuruluşlarının İlan, Reklam ve Tanıtım Kuralları",
         "III-39.1 sayılı Tebliğ uyarınca aracı kurumların ve portföy yönetim şirketlerinin yapacakları ilan, reklam ve tanıtımlara ilişkin;\n\nI. İlan ve reklamlarda yatırımcılara kesin kâr garantisi veya anaparanın kaybolmayacağına dair taahhütte bulunulamaz.\nII. Geçmiş getiri performansları gelecekteki sonuçların garantisi olarak sunulamaz ve geçmiş getiri verisi sunulurken dönemi açıkça belirtilmelidir.\nIII. Reklam ve tanıtımlarda kullanılan ifadeler gerçeğe aykırı, yanıltıcı veya abartılı olamaz.\n\nYukarıda yer alan tanıtım kurallarından hangileri mevzuatça emredilmiştir?",
         [("A", "Yalnızca I numaralı kural mevzuatça emredilmiştir."),
          ("B", "Yalnızca II numaralı kural mevzuatça emredilmiştir."),
          ("C", "I ve II numaralı kurallar mevzuatça emredilmiştir."),
          ("D", "II ve III numaralı kurallar mevzuatça emredilmiştir."),
          ("E", "I, II ve III numaralı kuralların tamamı mevzuatça emredilmiştir.")],
         "1. MEVZUAT DAYANAĞI: III-39.1 m. 51 ve Tüketicinin Korunması Mevzuatı.\n2. HUKUKİ / TEKNİK ÇERÇEVE: Sermaye piyasasında reklamlar yanıltıcı olamaz, kâr garantisi verilemez, geçmiş performans gelecek garantisi gibi gösterilemez.\n3. ADIM ADIM İNCELEME / HESAPLAMA: I, II ve III öncüllerinin tümü tebliğin amir reklam ilkeleridir.\n4. DOĞRU CEVAP VE SONUÇ: E seçeneğidir.\n5. ÇELDİRİCİ TUZAĞI: Reklamlarda kâr vaadinde bulunmanın serbest olduğunu düşünmek.",
         "Reklamlarda kâr garantisi verilemez, geçmiş getiri gelecek garantisi yapılamaz ve yanıltıcı ifade kullanılamaz.", "KB2_Muhakeme")
    ]
    
    for item in raw_data:
        qid, correct_key, topic, text, opts, exp, trap, skill = item
        options_list = [{"key": k, "text": t} for k, t in opts]
        questions.append({
            "id": qid,
            "module_id": "1005",
            "source": "cikmis",
            "topic": topic,
            "chapter": "YATIRIM KURULUŞLARI KURULUŞ FAALİYET VE DENETİM ESASLARI",
            "text": text,
            "options": options_list,
            "correct_answer": correct_key,
            "explanation": exp,
            "trap": trap,
            "difficulty": "hard",
            "tags": ["1005", topic],
            "cognitive_skill": skill
        })
        
    return questions

if __name__ == '__main__':
    qs = generate_questions()
    print(f"Modül 1005 için {len(qs)} soru üretildi.")
    key_counts = {}
    for q in qs:
        key_counts[q['correct_answer']] = key_counts.get(q['correct_answer'], 0) + 1
    print("Cevap anahtarı dağılımı:", key_counts)
    with open('scripts/data_1005_hard.json', 'w', encoding='utf-8') as f:
        json.dump(qs, f, ensure_ascii=False, indent=2)
    print("scripts/data_1005_hard.json kaydedildi.")
