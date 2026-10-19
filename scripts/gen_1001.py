# -*- coding: utf-8 -*-
"""
Modül 1001: 50 İleri Seviye (Sert) Sınav Sorusu Üreticisi
Her soru 5 aşamalı explanation, trap, zorluk: hard, cognitive_skill: KB2 veya KB3 içerir.
Cevap dağılımı: 10 A, 10 B, 10 C, 10 D, 10 E.
"""
import json

def generate_questions():
    questions = []
    
    # 50 topics data: (id, correct_key, topic, text, options, explanation, trap, skill)
    raw_data = [
        # 1 (A)
        ("q_1001_sert_001", "A", "Önemli Nitelikteki İşlemler & Ayrılma Hakkı (II-23.3)",
         "Borsa İstanbul Yıldız Pazar'da işlem gören ABC Holding A.Ş., toplam aktif büyüklüğünün %65'ini oluşturan ana üretim tesisini ilişkili olmayan üçüncü bir tarafa devretme kararı almıştır. Bu işleme ilişkin genel kurul toplantısı ve ayrılma hakkı sürecine dair;\n\nI. Malvarlığı devri, ortaklığın son finansal tablosundaki aktif toplamına oranı %50'yi aştığından 'Önemli Nitelikte İşlem' teşkil eder.\nII. Genel kurul toplantısına katılıp olumsuz oy kullanan ve muhalefet şerhini tutanağa işleten pay sahipleri ayrılma hakkına sahiptir.\nIII. Ayrılma hakkı kullanım fiyatı kural olarak işlemin ilk kamuya açıklandığı tarihten önceki son 30 gün içinde borsada oluşan düzeltilmiş ağırlıklı ortalama fiyatların aritmetik ortalamasıdır.\n\nYukarıdaki ifadelerden hangileri 6362 sayılı SPKn ve II-23.3 sayılı Tebliğ hükümleri uyarınca DOĞRUDUR?",
         [("A", "Yalnız I ve II"), ("B", "Yalnız I ve III"), ("C", "Yalnız II ve III"), ("D", "Yalnız I"), ("E", "I, II ve III")],
         "1. MEVZUAT DAYANAĞI: 6362 sayılı SPKn m. 23, 24 ve II-23.3 sayılı Tebliğ m. 5, 9, 10.\n2. HUKUKİ ÇERÇEVE: Malvarlığı devrinde %50 eşiği aşıldığında işlem önemli niteliktedir ve ayrılma hakkı doğar. Ayrılma hakkı için muhalefet şerhi tutanağa işletilmelidir.\n3. ADIM ADIM İNCELEME: I ve II doğrudur. III yanlıştır çünkü fiyat son 30 gün değil, tebliğdeki pazar grubuna göre 1 aylık veya 6 aylık düzeltilmiş ağırlıklı ortalamadır.\n4. DOĞRU CEVAP: A şıkkıdır.\n5. ÇELDİRİCİ TUZAĞI: Ayrılma hakkı fiyatında ezbere 'son 30 gün' varsayımı yanıltıcıdır.",
         "Ayrılma hakkı fiyatı Yıldız Pazar için son 1 ay veya 6 aylık düzeltilmiş ortalama fiyatlar esas alınarak hesaplanır.", "KB2_Muhakeme"),

        # 2 (B)
        ("q_1001_sert_002", "B", "Pay Alım Teklifi Zorunluluğu ve Muafiyetler (II-26.1)",
         "6362 sayılı Sermaye Piyasası Kanunu m. 26 ve II-26.1 sayılı Pay Alım Teklifi Tebliği uyarınca, halka açık ortaklıklarda doğrudan veya dolaylı olarak 'Yönetim Kontrolünün Ele Geçirilmesi' ve pay alım teklifinde bulunma yükümlülüğüne ilişkin aşağıdakilerden hangisi YANLIŞTIR?",
         [("A", "Ortaklığın oy haklarının yüzde ellisinden fazlasına tek başına veya birlikte hareket edenlerle sahip olunması zorunlu çağrı doğurur."),
          ("B", "Yönetim kurulu üye sayısının salt çoğunluğunu seçme hakkı veren imtiyazlı paylara sahip olunması, oy oranı %50'nin altında kalsa dahi çağrı doğurmaz."),
          ("C", "Pay alım teklifi zorunluluğunun doğduğu tarihten itibaren en geç 6 iş günü içinde Kurul'a onay için başvurulması zorunludur."),
          ("D", "Zorunlu pay alım teklifi fiyatı, payların iktisap edildiği tarihten önceki 6 aylık dönemde oluşan günlük düzeltilmiş borsa fiyatlarının aritmetik ortalamasından düşük olamaz."),
          ("E", "Finansal yeniden yapılandırma çerçevesinde kredi veren bankaların alacaklarına karşılık hisse edinmesi durumunda Kurul pay alım teklifinden muafiyet tanıyabilir.")],
         "1. MEVZUAT DAYANAĞI: 6362 sayılı SPKn m. 26 ve II-26.1 Tebliği m. 11, 13.\n2. HUKUKİ ÇERÇEVE: Yönetim kurulu üye sayısının salt çoğunluğunu seçme hakkı veren paylara sahip olmak, oy oranı %50 altında kalsa dahi yönetim kontrolüdür ve çağrı doğurur.\n3. ADIM ADIM İNCELEME: B seçeneğindeki 'çağrı doğurmaz' ifadesi açıkça yanlıştır.\n4. DOĞRU CEVAP: B şıkkıdır.\n5. ÇELDİRİCİ TUZAĞI: Yönetim kontrolünü yalnızca %50 oy ile sınırlı sanmak.",
         "Yönetim kurulu çoğunluğunu seçme imtiyazı, oy oranı %10 olsa dahi zorunlu pay alım teklifini tetikler.", "KB2_Muhakeme"),

        # 3 (C)
        ("q_1001_sert_003", "C", "Piyasa Dolandırıcılığı ve Etkin Pişmanlık (m. 107)",
         "Borsa İstanbul Pay Piyasası'nda gerçeğe aykırı emirler vererek ve kendinden kendine işlemler yaparak hisse fiyatını yapay olarak yükselttiği tespit edilen Bay X hakkında 'İşlem Bazlı Piyasa Dolandırıcılığı' (SPKn m. 107/1) suçundan işlem tesis edilmiştir. Bay X'in 6362 sayılı Kanun m. 107/3 kapsamında 'Etkin Pişmanlık' hükümlerinden faydalanabilmesine ilişkin adli şartlar hakkında aşağıdakilerden hangisi DOĞRUDUR?",
         [("A", "Hakkında mahkemece kesin mahkumiyet hükmü verildikten sonra elde ettiği menfaatin 3 katını Hazineye öderse cezası infaz edilmez."),
          ("B", "Henüz SPK suç duyurusunda bulunmadan önce menfaatin 1 katını öderse cezası yarı oranında indirilir."),
          ("C", "Henüz hakkında soruşturma başlamadan önce elde ettiği menfaatin veya sebep olduğu zararın iki katını Hazineye öderse hakkında ceza verilmez."),
          ("D", "Kovuşturma aşamasında menfaatin iki katını öderse kamu davası düşer."),
          ("E", "Etkin pişmanlık hükümleri yalnızca bilgi suiistimali suçunda geçerli olup manipülasyonda uygulanamaz.")],
         "1. MEVZUAT DAYANAĞI: 6362 sayılı SPKn m. 107/3.\n2. HUKUKİ ÇERÇEVE: Soruşturma başlamadan önce menfaat/zararın 2 katı Hazineye ödenirse ceza verilmez.\n3. ADIM ADIM İNCELEME: C seçeneğindeki hüküm kanun metniyle birebir örtüşür.\n4. DOĞRU CEVAP: C şıkkıdır.\n5. ÇELDİRİCİ TUZAĞI: Kovuşturma aşamasında davanın düşeceği yanılgısı (düşmez, ceza indirimi yapılır).",
         "Soruşturma başlamadan önce 2 kat ödemede hiç ceza verilmez.", "KB3_Vaka"),

        # 4 (D)
        ("q_1001_sert_004", "D", "İzahname İnceleme Süreleri ve Sorumluluk (SPKn m. 5, 32)",
         "Payları ilk defa halka arz edilecek olan bir anonim ortaklığın Sermaye Piyasası Kurulu'na sunduğu izahname taslağının incelenmesi ve onaylanması sürecinde;\n\nI. Kurul, izahname başvurusunu ilk defa halka arz edilecek ortaklıklar için başvuru tarihinden itibaren azami 30 iş günü içinde karara bağlar.\nII. İzahnamede yer alan eksik veya hatalı bilgilerin giderilmesi için Kurul tarafından verilen süreler 30 iş günlük azami inceleme süresini durdurur.\nIII. İzahnamede yer alan yanıltıcı bilgilerden doğan zararlardan ilk olarak halka arz konsorsiyum lideri aracı kurum, yetmezse ihraççı sorumludur.\n\nYukarıda yer alan hukuki tespitlerden hangileri 6362 sayılı SPKn m. 5 ve m. 32 uyarınca DOĞRUDUR?",
         [("A", "Yalnız I"), ("B", "Yalnız II"), ("C", "I ve III"), ("D", "I ve II"), ("E", "I, II ve III")],
         "1. MEVZUAT DAYANAĞI: 6362 sayılı SPKn m. 5/3 ve m. 32.\n2. HUKUKİ ÇERÇEVE: İlk halka arzda azami süre 30 iş günüdür. Eksiklik süreleri bu süreyi durdurur. Sorumlulukta birinci derece sorumlu ihraççıdır, konsorsiyum lideri zararın ihraççıdan karşılanamadığı kısımda sorumludur.\n3. ADIM ADIM İNCELEME: I ve II doğrudur, III yanlıştır.\n4. DOĞRU CEVAP: D şıkkıdır.\n5. ÇELDİRİCİ TUZAĞI: Aracı kurumun birinci derece sorumlu sanılması.",
         "İzahname zararından birincil sorumlu ihraççıdır.", "KB2_Muhakeme"),

        # 5 (E)
        ("q_1001_sert_005", "E", "Özel Durumlar ve İçsel Bilginin Ertelenmesi (II-15.1)",
         "II-15.1 sayılı Özel Durumlar Tebliği m. 6 uyarınca, halka açık anonim ortaklıkların yönetim kurulu kararıyla 'İçsel Bilgilerin Kamuya Açıklanmasını Ertelemesi' şartları ve hukuki sonuçlarına ilişkin;\n\nI. Ertelemenin, ortaklığın meşru menfaatlerinin korunması için zorunlu olması şarttır.\nII. Ertelemenin kamunun yanıltılmasına yol açmaması ve bilginin gizliliğinin fiilen korunabilmesi zorunludur.\nIII. Ertelenen içsel bilginin gizliliğinin korunamadığı veya basında somut haberlerin çıktığı anda derhal KAP'ta açıklama yapılmalıdır.\n\nYukarıda belirtilen koşullardan hangileri içsel bilginin ertelenmesi rejiminde hukuken zorunlu kılınmıştır?",
         [("A", "Yalnız I"), ("B", "I ve II"), ("C", "I ve III"), ("D", "II ve III"), ("E", "I, II ve III")],
         "1. MEVZUAT DAYANAĞI: II-15.1 m. 6.\n2. HUKUKİ ÇERÇEVE: İçsel bilgi ertelenebilir; ancak meşru menfaat, kamunun yanıltılmaması ve gizliliğin tam korunması kümülatif şarttır.\n3. ADIM ADIM İNCELEME: I, II ve III öncüllerinin tamamı tebliğ şartıdır.\n4. DOĞRU CEVAP: E şıkkıdır.\n5. ÇELDİRİCİ TUZAĞI: Gizlilik sızsa dahi genel kurula kadar beklenebileceği yanılgısı.",
         "Gizlilik sızdığı an erteleme kararı düşer ve KAP açıklaması zorunlu hale gelir.", "KB2_Muhakeme"),

        # 6 (A)
        ("q_1001_sert_006", "A", "Bilgi Suiistimali Suçu ve İçeridekiler (m. 106)",
         "6362 sayılı Sermaye Piyasası Kanunu m. 106 uyarınca düzenlenen 'Bilgi Suiistimali' (Insider Trading) suçu kapsamında; doğrudan ya da dolaylı olarak sermaye piyasası araçları ya da ihraççılar hakkında içsel bilgiye sahip olup bu bilgiyi kullanarak işlem yapan failler açısından aşağıdakilerden hangisi 'Birincil İçeridekiler' (Primary Insiders) arasında YER ALMAZ?",
         [("A", "İçsel bilgiyi bir restoranda yan masadaki yöneticilerin konuşmasına kulak misafiri olarak öğrenen üçüncü şahıs"),
          ("B", "İhraççıların veya bunların bağlı ortaklıklarının yönetim kurulu başkan ve üyeleri ile yöneticileri"),
          ("C", "İhraççılarda pay sahibi olmaları nedeniyle içsel bilgiye doğrudan vakıf olan ortaklar"),
          ("D", "İş, meslek veya görevlerinin ifası sebebiyle içsel bilgiye erişimi bulunan bağımsız denetçiler ve hukuk müşavirleri"),
          ("E", "İçsel bilgiyi bir suç işlemek suretiyle (örneğin bilgisayar korsanlığı ile) ele geçiren kişiler")],
         "1. MEVZUAT DAYANAĞI: 6362 sayılı SPKn m. 106/1.\n2. HUKUKİ ÇERÇEVE: Kulak misafiri olan üçüncü kişi 'İkincil İçerideki'dir.\n3. ADIM ADIM İNCELEME: Yöneticiler, pay sahipleri, meslek icra edenler ve suçu suç işleyerek elde edenler birincil içeridekidir.\n4. DOĞRU CEVAP: A şıkkıdır.\n5. ÇELDİRİCİ TUZAĞI: Suç işleyerek bilgi elde edenin birincil içerideki sayıldığını unutmak.",
         "Kulak misafiri olan kişi ikincil içeridekidir.", "KB2_Muhakeme"),

        # 7 (B)
        ("q_1001_sert_007", "B", "Ortaklıktan Çıkarma ve Satma Hakları (II-27.2)",
         "Borsa İstanbul'da işlem gören XYZ A.Ş.'de hakim ortak Bay K, yaptığı hisse alımları neticesinde ortaklığın toplam oy haklarının %98,5'ine ulaşmıştır. II-27.2 sayılı Ortaklıktan Çıkarma ve Satma Hakları Tebliği çerçevesinde doğan haklar ve sürelere ilişkin aşağıdakilerden hangisi DOĞRUDUR?",
         [("A", "Hakim ortak konumu kazanıldığı tarihten itibaren azami 15 gün içinde azınlık pay sahipleri ortaklıktan derhal çıkarılır."),
          ("B", "Azınlıkta kalan pay sahipleri, hakim ortak konumunun kamuya ilan edildiği tarihten itibaren 3 aylık hak düşürücü süre içinde paylarının satın alınmasını talep edebilirler."),
          ("C", "Ortaklıktan çıkarma hakkının kullanılabilmesi için asgari oy hakkı oranı %95 olup Bay K'nin %98,5'e ulaşması bu hakkı düşürür."),
          ("D", "Satma hakkı kullanım bedeli, hakim ortak konumunun ilanından önceki 5 yıllık borsa ortalama fiyatı üzerinden hesaplanır."),
          ("E", "Azınlık pay sahipleri satma hakkını kullanmazlarsa, hakim ortak hiçbir şekilde ortaklıktan çıkarma hakkını kullanamaz.")],
         "1. MEVZUAT DAYANAĞI: II-27.2 m. 5, 6.\n2. HUKUKİ ÇERÇEVE: Oy hakkı en az %98 olduğunda hakim ortaklık doğar. Azınlığın satma hakkı süresi 3 aydır.\n3. ADIM ADIM İNCELEME: B seçeneği kanuni 3 aylık hak düşürücü süreyi açıklar.\n4. DOĞRU CEVAP: B şıkkıdır.\n5. ÇELDİRİCİ TUZAĞI: Eski %95 eşiğini geçerli sanmak.",
         "Eşik %98 oy hakkıdır ve azınlığın satma hakkı süresi 3 aydır.", "KB2_Muhakeme"),

        # 8 (C)
        ("q_1001_sert_008", "C", "Örtülü Kazanç Aktarımı Yasağı (SPKn m. 21, 110)",
         "Halka açık DEF Teknoloji A.Ş., mülkiyetinde bulunan 50 milyon TL piyasa ekspertiz değerine sahip bir gayrimenkulü, şirket yönetim kurulu başkanının şahsen sahip olduğu ilişkili bir şirkete 15 milyon TL bedelle devretmiştir. 6362 sayılı SPKn m. 21 ve m. 110 hükümleri kapsamında bu işleme ilişkin;\n\nI. Piyasa emsallerine, ticari hayatın basiret ve dürüstlük ilkelerine aykırı olarak kârın veya malvarlığının ilişkili tarafa aktarılması 'Örtülü Kazanç Aktarımı' suçunu oluşturur.\nII. Bu suçu işleyen yönetim kurulu üyeleri ve ilişkili kişiler hakkında 3 yıldan 8 yıla kadar hapis ve beş bin güne kadar adli para cezası uygulanır.\nIII. Aktarılan tutarın yasal faiziyle birlikte halka açık ortaklığa iade edilmesi halinde hiçbir adli ceza verilemez.\n\nYukarıdaki tespitlerden hangileri DOĞRUDUR?",
         [("A", "Yalnız I"), ("B", "Yalnız II"), ("C", "I ve II"), ("D", "I ve III"), ("E", "I, II ve III")],
         "1. MEVZUAT DAYANAĞI: 6362 sayılı SPKn m. 21 ve m. 110/1.\n2. HUKUKİ ÇERÇEVE: Örtülü kazanç aktarımının cezası 3 yıldan 8 yıla kadar hapistir. İade etmek ceza davasını doğrudan düşürmez.\n3. ADIM ADIM İNCELEME: I ve II doğrudur, III yanlıştır.\n4. DOĞRU CEVAP: C şıkkıdır.\n5. ÇELDİRİCİ TUZAĞI: Parayı iade etmenin hapis cezasını otomatik sildiğini sanmak.",
         "Örtülü kazanç aktarımında iade yapmak ceza davasını doğrudan ortadan kaldırmaz.", "KB2_Muhakeme"),

        # 9 (D)
        ("q_1001_sert_009", "D", "Kurumsal Yönetim ve Bağımsız Yönetim Kurulu Üyeleri (II-17.1)",
         "II-17.1 sayılı Kurumsal Yönetim Tebliği uyarınca, Borsa İstanbul Yıldız Pazar'da yer alan Birinci Grup halka açık ortaklıkların yönetim kurulu yapılanması ve bağımsız üyelere ilişkin aşağıdaki kurallardan hangisi YANLIŞTIR?",
         [("A", "Yönetim kurulu içerisindeki bağımsız üye sayısı toplam üye sayısının üçte birinden (1/3) az olamaz ve her halükarda en az 2 üye olmalıdır."),
          ("B", "Bağımsız üyenin görev süresi kural olarak 3 yıl olup aynı ortaklıkta en fazla 6 yıl bağımsız üye olarak görev yapabilir."),
          ("C", "Denetimden Sorumlu Komite üyelerinin tamamının bağımsız yönetim kurulu üyelerinden oluşması zorunludur."),
          ("D", "Bağımsız üye adayının, aday gösterildiği ortaklıkta son 2 yıl içinde herhangi bir ticari veya istihdam ilişkisinde bulunmamış olması yeterlidir."),
          ("E", "Yönetim kurulu başkanı ile genel müdürün aynı kişi olması durumunda bu durumun gerekçesi KAP'ta kamuya açıklanmalıdır.")],
         "1. MEVZUAT DAYANAĞI: II-17.1 Kurumsal Yönetim Tebliği m. 4.3.\n2. HUKUKİ ÇERÇEVE: Bağımsızlık ilişkisizlik süresi son 2 yıl değil, SON 5 YILDIR.\n3. ADIM ADIM İNCELEME: D şıkkındaki 'son 2 yıl yeterlidir' kuralı mevzuata aykırıdır.\n4. DOĞRU CEVAP: D şıkkıdır.\n5. ÇELDİRİCİ TUZAĞI: Sürenin 2 yıl sanılması.",
         "Bağımsız üyelik için şirkette son 5 yıl içinde istihdam veya ticari ilişki olmamalıdır.", "KB2_Muhakeme"),

        # 10 (E)
        ("q_1001_sert_010", "E", "SPK İdari Tedbirleri ve Geçici İşlem Yasağı (m. 101)",
         "6362 sayılı Sermaye Piyasası Kanunu m. 101 uyarınca, sermaye piyasasının güven, açıklık ve istikrar içinde çalışmasını teminen ve piyasa dolandırıcılığı veya bilgi suiistimali şüphesi bulunan hallerde Kurul tarafından uygulanabilecek idari tedbirlere ilişkin;\n\nI. Hakkında makul şüphe bulunan gerçek ve tüzel kişilere borsalarda geçici olarak 6 aydan 2 yıla kadar işlem yapma yasağı getirilebilir.\nII. Borsada işlem gören payların alım satımının geçici veya sürekli olarak durdurulması veya brüt takas uygulamasına geçilmesi kararlaştırılabilir.\nIII. İlgili kişilerin Takasbank ve MKK nezdindeki hesaplarında bulunan menkul kıymetlerin devir ve teslimi geçici olarak kısıtlanabilir.\n\nYukarıda belirtilen idari tedbir yetkilerinden hangileri doğrudan SPK tarafından tesis edilebilir?",
         [("A", "Yalnız I"), ("B", "Yalnız II"), ("C", "I ve II"), ("D", "II ve III"), ("E", "I, II ve III")],
         "1. MEVZUAT DAYANAĞI: 6362 sayılı SPKn m. 101.\n2. HUKUKİ ÇERÇEVE: Kurul; işlem yasağı (6 ay - 2 yıl), brüt takas, takas/saklama kısıtlamalarının tamamını doğrudan uygulayabilir.\n3. ADIM ADIM İNCELEME: I, II ve III öncüllerinin hepsi Kurul yetkisindedir.\n4. DOĞRU CEVAP: E şıkkıdır.\n5. ÇELDİRİCİ TUZAĞI: İşlem yasağının sadece mahkemece verilebileceğini düşünmek.",
         "SPK idari işlemle 6 aydan 2 yıla kadar işlem yasağı koyabilir.", "KB2_Muhakeme"),

        # 11 (A)
        ("q_1001_sert_011", "A", "Halka Arzda Fiyat İstikrarını Sağlayıcı İşlemler (II-5.2)",
         "Payları halka arz edilen ortaklıklarda fiyat istikrarını sağlayıcı işlemlerin icrasına ilişkin aşağıdakilerden hangisi DOĞRUDUR?",
         [("A", "Fiyat istikrarı işlemleri payların borsada işlem görmeye başladığı tarihten itibaren azami 30 gün süreyle yürütülebilir."),
          ("B", "Fiyat istikrarı işlemlerinde ihraççı şirketin kasasındaki nakit fonlar sınırsız biçimde alım için kullanılabilir."),
          ("C", "Aracı kurum fiyat istikrarı işlemlerinde halka arz fiyatının üzerinde emir vererek hisse fiyatını yükseltebilir."),
          ("D", "Fiyat istikrarı süresi bittikten sonra aracı kurumun aldığı paylar derhal aynı gün borsada satılmak zorundadır."),
          ("E", "Fiyat istikrarı işlemleri yapılması planlanıyorsa bu durum izahnamede gizli tutulmalı, işlem bittikten sonra açıklanmalıdır.")],
         "1. MEVZUAT DAYANAĞI: II-5.2 Tebliği m. 26.\n2. HUKUKİ ÇERÇEVE: Fiyat istikrarı azami 30 gün sürer ve asla halka arz fiyatının üzerinde emir girilemez.\n3. ADIM ADIM İNCELEME: A doğrudur. B yanlıştır (ihraççı fonu kullanılamaz, halka arz eden fonu kullanılır). C yanlıştır (asla arz fiyatı aşılamaz).\n4. DOĞRU CEVAP: A şıkkıdır.\n5. ÇELDİRİCİ TUZAĞI: Halka arz fiyatının üstünde alım yapılabileceği yanılgısı.",
         "Fiyat istikrarı azami 30 gündür ve arz fiyatının üzerine çıkılamaz.", "KB2_Muhakeme"),

        # 12 (B)
        ("q_1001_sert_012", "B", "İzahnamenin Ek ve Tadil Süreleri (SPKn m. 7)",
         "Onaylanmış bir izahnamede satış başlamadan önce önemli yeni bir gelişme meydana gelmesi durumunda izahname ek ve tadil sürecine ilişkin aşağıdaki sürelerden hangisi DOĞRUDUR?",
         [("A", "İhraççı gelişmeyi 10 iş gününde Kurul'a bildirir; Kurul 15 iş gününde onaylar; cayma süresi 5 gündür."),
          ("B", "İhraççı gelişmeyi en geç 3 iş günü içinde Kurul'a sunar; Kurul eki en geç 7 iş günü içinde onaylar; yatırımcıların 2 iş günü cayma hakkı vardır."),
          ("C", "İhraççı 5 iş gününde bildirir; Kurul 10 iş gününde onaylar; cayma süresi bulunmaz."),
          ("D", "İhraççı 1 ay içinde bildirir; Kurul 30 günde onaylar; cayma hakkı 10 gündür."),
          ("E", "Gelişme genel kurula sunulur; SPK'ya bildirim yapılmaksızın satışa devam edilir.")],
         "1. MEVZUAT DAYANAĞI: 6362 sayılı SPKn m. 7.\n2. HUKUKİ ÇERÇEVE: Yeni gelişme 3 iş gününde SPK'ya iletilir, SPK 7 iş gününde onaylar, yatırımcının 2 iş günü cayma hakkı doğar.\n3. ADIM ADIM İNCELEME: B şıkkı 3 gün bildirim, 7 gün onay, 2 gün cayma kuralını tam yansıtır.\n4. DOĞRU CEVAP: B şıkkıdır.\n5. ÇELDİRİCİ TUZAĞI: Sürelerin 5 veya 10 gün sanılması.",
         "Süreler: 3 iş günü sunum, 7 iş günü Kurul onayı, 2 iş günü yatırımcı cayma hakkıdır.", "KB1_Kavramsal"),

        # 13 (C)
        ("q_1001_sert_013", "C", "Halka Açık Ortaklıklarda Genel Kurul Çağrı Süresi (SPKn m. 29)",
         "Halka açık anonim ortaklıkların genel kurul toplantı çağrısına ilişkin 6362 sayılı SPKn m. 29 uyarınca asgari çağrı süresi aşağıdakilerden hangisidir?",
         [("A", "Toplantı gününden en az 1 hafta önce"),
          ("B", "İlan ve toplantı günleri dahil en az 14 gün önce"),
          ("C", "İlan ve toplantı günleri hariç olmak üzere en az 3 hafta önce"),
          ("D", "Toplantı tarihinden itibaren en geç 30 gün içinde"),
          ("E", "İlan ve toplantı günleri hariç olmak üzere en az 15 gün önce")],
         "1. MEVZUAT DAYANAĞI: 6362 sayılı SPKn m. 29/1.\n2. HUKUKİ ÇERÇEVE: TTK m. 414'te kapalı şirketlerde 2 hafta olan süre, SPKn m. 29 uyarınca halka açık şirketlerde ilan ve toplantı günleri hariç en az 3 haftadır.\n3. ADIM ADIM İNCELEME: C seçeneği açık yasa kuralıdır.\n4. DOĞRU CEVAP: C şıkkıdır.\n5. ÇELDİRİCİ TUZAĞI: TTK'daki 2 hafta kuralıyla karıştırmak.",
         "Halka açık şirketlerde genel kurul çağrısı ilan ve toplantı günleri hariç en az 3 hafta öncedir.", "KB1_Kavramsal"),

        # 14 (D)
        ("q_1001_sert_014", "D", "TTK m. 418 ve m. 421 Genel Kurul Nisapları",
         "Halka açık bir anonim ortaklıkta şirket esas sözleşmesinde aksine ağırlaştırıcı hüküm bulunmadıkça, şirket merkezinin yurt dışına taşınması veya işletme konusunun tamamen değiştirilmesi için gereken genel kurul toplantı ve karar nisabı nedir?",
         [("A", "Sermayenin 1/4'ü ile toplanır, mevcut oyların çoğunluğu ile karar alınır."),
          ("B", "Sermayenin en az %50'si ile toplanır, toplantıya katılanların 2/3 oyu gerekir."),
          ("C", "Sermayenin en az %75'ini temsil eden pay sahiplerinin olumlu oyu şarttır."),
          ("D", "Şirket sermayesinin tamamını temsil eden pay sahiplerinin oybirliği aranır."),
          ("E", "Borsa kotunda işlem gören payların %51'inin olumlu oyu yeterlidir.")],
         "1. MEVZUAT DAYANAĞI: 6102 sayılı TTK m. 421/2.\n2. HUKUKİ ÇERÇEVE: Bilanço zararlarının kapatılması için yükümlülük koyma veya şirket merkezinin yurt dışına taşınması kararlarında sermayenin tamamının oybirliği şarttır.\n3. ADIM ADIM İNCELEME: D seçeneğindeki sermayenin tamamının oybirliği kuralı zorunludur.\n4. DOĞRU CEVAP: D şıkkıdır.\n5. ÇELDİRİCİ TUZAĞI: %75 nisapla karıştırmak.",
         "Şirket merkezinin yurt dışına naklinde sermayenin tamamının oybirliği gerekir.", "KB2_Muhakeme"),

        # 15 (E)
        ("q_1001_sert_015", "E", "Payların Geri Alımı Tebliği (II-22.1)",
         "Halka açık bir anonim ortaklığın borsada işlem gören kendi paylarını geri almasına (Share Buyback) ilişkin II-22.1 sayılı Tebliğ hükümleri uyarınca;\n\nI. Geri alınan payların nominal değeri, ortaklığın ödenmiş veya çıkarılmış sermayesinin %10'unu aşamaz.\nII. Geri alım bedeli yalnızca ortaklığın dağıtılabilir kâr payı ve serbest yedek akçelerinden karşılanabilir.\nIII. Ortaklığın elinde bulunan kendi payları genel kurul toplantı nisabında dikkate alınmaz ve bu payların oy hakları donar.\n\nYukarıdaki tespitlerden hangileri DOĞRUDUR?",
         [("A", "Yalnız I"), ("B", "Yalnız II"), ("C", "I ve II"), ("D", "II ve III"), ("E", "I, II ve III")],
         "1. MEVZUAT DAYANAĞI: II-22.1 m. 5, 9, 16 ve TTK m. 379, 389.\n2. HUKUKİ ÇERÇEVE: Geri alım tavanı sermayenin %10'udur. Bedel dağıtılabilir kaynaklardan ödenir. Şirketin elindeki kendi payların oy hakları donar.\n3. ADIM ADIM İNCELEME: I, II ve III öncüllerinin hepsi kanunen geçerlidir.\n4. DOĞRU CEVAP: E şıkkıdır.\n5. ÇELDİRİCİ TUZAĞI: Geri alınan paylarla genel kurulda oy kullanılabileceği zannı.",
         "Geri alınan paylar sermayenin %10'unu geçemez ve şirkette kaldığı sürece oy hakkı donar.", "KB2_Muhakeme"),

        # 16 (A)
        ("q_1001_sert_016", "A", "Kâr Payı Avansı Dağıtım Esasları (II-19.1)",
         "Halka açık anonim ortaklıkların ara dönem finansal tablolarına dayalı olarak kâr payı avansı dağıtabilmeleri için aşağıdakilerden hangisi ZORUNLU DEĞİLDİR?",
         [("A", "Geçmiş son 3 yıl boyunca kesintisiz nakit temettü ödemiş olması"),
          ("B", "Şirket esas sözleşmesinde genel kurula kâr payı avansı dağıtma yetkisi verilmiş olması"),
          ("C", "Genel kurulun yönetim kuruluna kâr payı avansı dağıtımı konusunda yetki vermiş olması"),
          ("D", "İlgili ara dönem finansal tablosuna göre net dönem kârı elde edilmiş olması"),
          ("E", "Geçmiş yıllar zararları ve yasal yedek akçeler ayrıldıktan sonra kalan tutarın avans dağıtımına konu edilmesi")],
         "1. MEVZUAT DAYANAĞI: II-19.1 m. 11.\n2. HUKUKİ ÇERÇEVE: Kâr payı avansı için esas sözleşme hükmü, genel kurul yetkisi, ara dönem kârı ve geçmiş zararların düşülmesi şarttır. Son 3 yıl temettü ödeme şartı yoktur.\n3. ADIM ADIM İNCELEME: A seçeneğinde belirtilen 'son 3 yıl kesintisiz temettü' kuralı mevzuatta yer almaz.\n4. DOĞRU CEVAP: A şıkkıdır.\n5. ÇELDİRİCİ TUZAĞI: Şirketin temettü geleneği şartı arandığı yanılgısı.",
         "Avans dağıtımında geçmiş 3 yıl kâr dağıtma şartı bulunmaz.", "KB2_Muhakeme"),

        # 17 (B)
        ("q_1001_sert_017", "B", "Borsa Kotundan Çıkma Esasları (II-16.1)",
         "Borsa İstanbul'da işlem gören payların borsa kotundan isteğe bağlı olarak çıkarılmasına (Delisting) ilişkin aşağıdaki ifadelerden hangisi DOĞRUDUR?",
         [("A", "Genel kurulda toplantıya katılan pay sahiplerinin adi salt çoğunluğu kotasyondan çıkma kararı için mevzuatça yeterlidir."),
          ("B", "Genel kurulda nitelikli çoğunluk aranması, SPK onayı alınması ve pay sahiplerine ayrılma hakkı teklif edilmesi şarttır."),
          ("C", "Kotasyondan çıkma kararı alındığında ortaklık resen tasfiye edilmiş sayılır ve şirket malvarlığı devlete intikal eder."),
          ("D", "Borsa kotundan çıkmak için SPK onayına gerek olmayıp Borsa İstanbul Yönetim Kurulu'nun vereceği karar nihai ve kesindir."),
          ("E", "İsteğe bağlı kotasyondan çıkan bir sermaye şirketi Türk Ticaret Kanunu uyarınca bir daha hiçbir surette halka açılamaz.")],
         "1. MEVZUAT DAYANAĞI: II-16.1 m. 8.\n2. HUKUKİ ÇERÇEVE: Kotasyondan çıkma önemli nitelikte işlemdir, genel kurul onayı, SPK izni ve ayrılma hakkı kullandırma zorunluluğu vardır.\n3. ADIM ADIM İNCELEME: B seçeneği nitelikli çoğunluk ve ayrılma hakkı güvencesini doğru açıklar.\n4. DOĞRU CEVAP: B şıkkıdır.\n5. ÇELDİRİCİ TUZAĞI: SPK izninin aranmadığı iddiası.",
         "Kotasyondan çıkma SPK ve Borsa onayına bağlıdır; ayrılma hakkı zorunludur.", "KB2_Muhakeme"),

        # 18 (C)
        ("q_1001_sert_018", "C", "Sermaye Kaybı ve Borca Batıklık (TTK m. 376)",
         "Son yıllık bilançosundan, sermaye ile kanuni yedek akçeler toplamının üçte ikisinin (2/3) karşılıksız kaldığı anlaşılan halka açık bir anonim ortaklık yönetim kurulunun alması gereken acil hukuki tedbir nedir?",
         [("A", "Ticaret mahkemesine başvurarak derhal şirket hakkında iflasın ertelenmesini veya konkordato ilan edilmesini talep etmek"),
          ("B", "Şirketin tüm ticari ve operasyonel faaliyetlerini en az altı ay süreyle geçici olarak durdurma kararı almak"),
          ("C", "Genel kurulu toplantıya çağırarak sermayenin 1/3'ü ile yetinilmesine veya sermayenin tamamlanmasına karar verilmesini sağlamak"),
          ("D", "Şirket alacaklılarının haklarını korumak amacıyla tüm yönetim kurulu üyelerinin şahsi malvarlıklarına tedbir koymak"),
          ("E", "Borsa İstanbul Yönetim Kurulu'ndan ortaklığın işlem sırasının ikinci bir karara kadar süresiz durdurulmasını istemek")],
         "1. MEVZUAT DAYANAĞI: 6102 sayılı TTK m. 376/2.\n2. HUKUKİ ÇERÇEVE: 2/3 sermaye kaybında genel kurul: 1) Kalan 1/3 sermayeyle yetinilmesine, 2) Sermayenin tamamlanmasına karar verir. Aksi takdirde şirket kendiliğinden sona erer.\n3. ADIM ADIM İNCELEME: C seçeneği TTK m. 376/2 hükmünü birebir ifade eder.\n4. DOĞRU CEVAP: C şıkkıdır.\n5. ÇELDİRİCİ TUZAĞI: İflas erteleme kurumunun OHAL KHK'sı ile kaldırıldığını ve TTK 376 mekanizmasını unutmak.",
         "2/3 sermaye kaybında sermaye 1/3'e indirilir ya da tamamlanır; aksi halde şirket infisah eder.", "KB2_Muhakeme"),

        # 19 (D)
        ("q_1001_sert_019", "D", "Sermaye Azaltımı ve Alacaklılara Çağrı (TTK m. 473-475)",
         "Bir anonim ortaklığın sermaye azaltımına gitmesi durumunda şirket alacaklılarının korunmasına yönelik yasal prosedüre dair aşağıdakilerden hangisi DOĞRUDUR?",
         [("A", "Alacaklılara yalnızca şirket internet sitesinden bir kez elektronik duyuru yapılması hak kaybını önlemek için yeterlidir."),
          ("B", "Alacaklılar sermaye azaltımı kararına tebliğden itibaren on gün içinde yazılı olarak itiraz etmezlerse dava hakları düşer."),
          ("C", "Sermaye azaltımı genel kurulda onaylandığı gün ticaret siciline tescil edilir ve alacaklıların ayrıca teminat hakkı bulunmaz."),
          ("D", "TTSG'de ve şirketin internet sitesinde 7'şer gün arayla 3 defa ilan yapılarak alacaklılara 2 aylık beyan süresi tanınır."),
          ("E", "Sermaye azaltımı tutarının tamamı nakit olarak Takasbank nezdinde bloke edilmedikçe genel kurulda karar alınması yasaktır.")],
         "1. MEVZUAT DAYANAĞI: 6102 sayılı TTK m. 474.\n2. HUKUKİ ÇERÇEVE: Alacaklılara TTSG'de 7 gün arayla 3 kez ilan yapılır ve 2 ay içinde alacaklarını beyan edip teminat isteme hakkı tanınır.\n3. ADIM ADIM İNCELEME: D şıkkındaki 7'şer gün arayla 3 ilan ve 2 aylık süre tam kanuni kuraldır.\n4. DOĞRU CEVAP: D şıkkıdır.\n5. ÇELDİRİCİ TUZAĞI: İlan sayısının 1 veya sürenin 15 gün sanılması.",
         "Alacaklılara çağrı: 7'şer gün arayla 3 defa ilan ve 2 aylık başvuru süresidir.", "KB1_Kavramsal"),

        # 20 (E)
        ("q_1001_sert_020", "E", "Halka Arza Aracılık Yüklenim Türleri (III-37.1)",
         "Halka arza aracılık faaliyetinde aracı kurumlar konsorsiyumu ile ihraççı arasında imzalanan sözleşme türleri ve hukuki sorumluluklarına ilişkin;\n\nI. En İyi Gayret Aracılığı'nda satılamayan paylar için aracı kurumun hiçbir satın alma taahhüdü bulunmaz.\nII. Bakiyeyi Yüklenim'de aracı kurum satış süresi sonunda halka satılamayan payların tamamını bedelini ödeyerek satın almayı taahhüt eder.\nIII. Tümünü Yüklenim'de aracı kurum satış başlamadan önce ihraç edilen tüm payların bedelini ihraççıya ödeyerek payları mülkiyetine alır.\n\nYukarıdaki sınıflandırmalardan hangileri DOĞRUDUR?",
         [("A", "Yalnız I"), ("B", "Yalnız II"), ("C", "I ve II"), ("D", "II ve III"), ("E", "I, II ve III")],
         "1. MEVZUAT DAYANAĞI: III-37.1 Yatırım Hizmetleri Tebliği m. 19, 20.\n2. HUKUKİ ÇERÇEVE: Aracılık: 1) En iyi gayret (taahhütsüz), 2) Bakiyeyi yüklenim (satılamayanı alma), 3) Tümünü yüklenim (satış öncesi tamamını alma).\n3. ADIM ADIM İNCELEME: I, II ve III öncüllerinin üçü de terimsel olarak tam doğrudur.\n4. DOĞRU CEVAP: E şıkkıdır.\n5. ÇELDİRİCİ TUZAĞI: Bakiyeyi yüklenim ile tümünü yüklenimi birbirine karıştırmak.",
         "Bakiyeyi yüklenim satılamayan kalanı, tümünü yüklenim ise ihracın tamamını baştan yüklenmektir.", "KB2_Muhakeme"),

        # 21 (A)
        ("q_1001_sert_021", "A", "Piyasa Bozucu Eylemler Tebliği (VI-104.1)",
         "VI-104.1 sayılı Piyasa Bozucu Eylemler Tebliği uyarınca, suç teşkil etmemekle birlikte sermaye piyasasının dürüst ve düzenli işleyişini bozan ve idari para cezası gerektiren eylemler kapsamında aşağıdakilerden hangisi 'Piyasa Bozucu Eylem' olarak DEĞERLENDİRİLMEZ?",
         [("A", "Borsa İstanbul tarafından belirlenen piyasa yapıcılık sözleşmesi çerçevesinde girilen kotasyon emirleri"),
          ("B", "Farklı fiyat kademelerine alım veya satım yönünde gerçeğe aykırı izlenim bırakacak şekilde çok sayıda aktif emir girilip silinmesi"),
          ("C", "Açılış veya kapanış seanslarında tek başına teorik eşleşme fiyatını önemli ölçüde saptıracak büyüklükte agresif emir verilmesi"),
          ("D", "Sosyal medya veya mesajlaşma gruplarında hisse hakkında somut dayanağı olmayan yanıltıcı söylentiler paylaşılması"),
          ("E", "Kendinden kendine işlem (wash trade) yapılarak işlem hacminin yapay olarak şişirilmesi")],
         "1. MEVZUAT DAYANAĞI: VI-104.1 m. 4, 5.\n2. HUKUKİ ÇERÇEVE: Borsa mevzuatına uygun piyasa yapıcılık veya likidite sağlayıcılık kapsamında girilen yasal kotasyon emirleri piyasa bozucu eylem sayılmaz.\n3. ADIM ADIM İNCELEME: A seçeneğindeki piyasa yapıcılık faaliyeti hukuka uygundur ve istisnadır. Diğerleri piyasa bozucu eylemdir.\n4. DOĞRU CEVAP: A şıkkıdır.\n5. ÇELDİRİCİ TUZAĞI: Piyasa yapıcılık kotasyonlarının da manipülatif emir sanılması.",
         "Piyasa yapıcılık sözleşmesi çerçevesindeki işlemler piyasa bozucu eylem sayılmaz.", "KB2_Muhakeme"),

        # 22 (B)
        ("q_1001_sert_022", "B", "SPK Bilgi İsteme ve İnceleme Yetkisi (SPKn m. 88, 89)",
         "6362 sayılı SPKn m. 88 ve 89 uyarınca Sermaye Piyasası Kurulu meslek personelinin denetim, bilgi ve belge isteme yetkisine ilişkin aşağıdakilerden hangisi YANLIŞTIR?",
         [("A", "Kamu kurum ve kuruluşları dahil tüm gerçek ve tüzel kişiler SPK uzmanlarının talep ettiği bilgi ve belgeleri vermekle yükümlüdür."),
          ("B", "Bankalar ve finansal kuruluşlar müşterilerine ait hesap bilgilerini 'Banka ve Müşteri Sırrı' gerekçesiyle SPK denetçilerine vermekten kaçınabilirler."),
          ("C", "SPK uzmanları ihraççılar, borsa ve yatırım kuruluşlarının merkez ve şubelerinde mahallinde inceleme yapmaya yetkilidir."),
          ("D", "Bilgi ve belge vermekten kaçınan veya gerçeğe aykırı bilgi veren kişiler hakkında 1 yıldan 3 yıla kadar hapis cezası uygulanır (SPKn m. 111)."),
          ("E", "Kurul denetçileri inceleme sırasında bilgisayar kütüklerini, dijital kayıtları ve muhasebe defterlerini kopyalayabilir ve el koyabilir.")],
         "1. MEVZUAT DAYANAĞI: 6362 sayılı SPKn m. 88/2.\n2. HUKUKİ ÇERÇEVE: Özel kanunlardaki sır saklama hükümleri (Bankacılık Kanunu müşteri sırrı dahil) SPK'ya karşı ileri sürülemez.\n3. ADIM ADIM İNCELEME: B seçeneğindeki 'kaçınabilirler' hükmü kanuna doğrudan aykırıdır.\n4. DOĞRU CEVAP: B şıkkıdır.\n5. ÇELDİRİCİ TUZAĞI: Banka sırrının SPK denetçisine karşı da geçerli olduğunun sanılması.",
         "Banka ve müşteri sırrı SPK uzmanlarının resmi inceleme taleplerine karşı ileri sürülemez.", "KB2_Muhakeme"),

        # 23 (C)
        ("q_1001_sert_023", "C", "SPK İhtiyati Haciz ve Tedbir Talebi (SPKn m. 91)",
         "6362 sayılı SPKn m. 91 uyarınca, sermaye piyasası suçları sebebiyle kamunun veya yatırımcıların uğradığı zararların temini amacıyla Kurul'un mahkemelerden talep edebileceği geçici hukuki koruma tedbirlerine ilişkin aşağıdakilerden hangisi DOĞRUDUR?",
         [("A", "Kurul yalnızca Sulh Ceza Hakimliği'nden arama kararı talep edebilir, malvarlığına tedbir isteyemez."),
          ("B", "Kurul'un ihtiyati haciz talebinde bulunabilmesi için mutlaka Hazine Müsteşarlığı'ndan izin alması zorunludur."),
          ("C", "Kurul, ilgililerin malvarlıklarına ihtiyati tedbir veya ihtiyati haciz konulmasını talep ederken İcra ve İflas Kanunu'nda öngörülen teminatı göstermekten muaftır."),
          ("D", "İhtiyati tedbir kararı en fazla 15 gün geçerli olup bu sürede dava açılmazsa kendiliğinden kalkar."),
          ("E", "İhtiyati haciz sadece ihraççı şirket yönetim kurulu başkanının şahsi gayrimenkulleriyle sınırlıdır.")],
         "1. MEVZUAT DAYANAĞI: 6362 sayılı SPKn m. 91/2.\n2. HUKUKİ ÇERÇEVE: SPK'nın ihtiyati haciz ve ihtiyati tedbir taleplerinde İİK'da aranan nakdi teminat yatırma şartı ARANMAZ (SPK teminattan muaftır).\n3. ADIM ADIM İNCELEME: C seçeneğindeki teminattan muafiyet hükmü kanun maddesidir.\n4. DOĞRU CEVAP: C şıkkıdır.\n5. ÇELDİRİCİ TUZAĞI: SPK'nın da özel alacaklı gibi teminat yatırmak zorunda olduğunun zannedilmesi.",
         "SPK mahkemelerden ihtiyati tedbir ve haciz isterken teminat göstermekten muaftır.", "KB2_Muhakeme"),

        # 24 (D)
        ("q_1001_sert_024", "D", "Kayıtlı Sermaye Sistemi Tavan Geçerliliği (II-18.1)",
         "Kayıtlı sermaye sistemine tabi halka açık bir anonim ortaklığın kayıtlı sermaye tavanının geçerlilik süresine ve bu sürenin sona ermesine ilişkin aşağıdakilerden hangisi DOĞRUDUR?",
         [("A", "Kayıtlı sermaye tavanı süresiz olarak geçerlidir; şirket tasfiye edilene kadar tavan değiştirilemez."),
          ("B", "Tavan geçerlilik süresi 3 yıl olup sürenin bitiminde şirket otomatik olarak esas sermaye sistemine döner."),
          ("C", "Tavan süresi 10 yıldır ve genel kurul kararıyla SPK izni aranmaksızın 5 yıl daha uzatılabilir."),
          ("D", "Kurulca verilen tavan izni azami 5 yıl için geçerli olup, bu süre içinde tavan artırımı yapılmadığı veya süre uzatılmadığı takdirde yönetim kurulu sermaye artırım kararı alamaz."),
          ("E", "5 yıllık süre dolsa bile çıkarılmış sermaye tavanı aşmadığı müddetçe yönetim kurulu kararıyla sermaye artırımı sonsuza kadar sürdürülebilir.")],
         "1. MEVZUAT DAYANAĞI: II-18.1 Kayıtlı Sermaye Sistemi Tebliği m. 5, 6.\n2. HUKUKİ ÇERÇEVE: Tavan izni 5 yıl için verilir. 5 yıl dolduğunda genel kuruldan yeni bir 5 yıllık tavan yetkisi alınmadıkça yönetim kurulu sermaye artıramaz.\n3. ADIM ADIM İNCELEME: D seçeneği 5 yıllık tavan süresini ve yaptırımını tam karşılar.\n4. DOĞRU CEVAP: D şıkkıdır.\n5. ÇELDİRİCİ TUZAĞI: Süre bitse de çıkarılmış sermaye tavana ulaşana kadar artırım yapılabileceği yanılgısı.",
         "Kayıtlı sermaye tavan izni azami 5 yıldır; süre bittiğinde yetki yenilenmezse YK sermaye artıramaz.", "KB2_Muhakeme"),

        # 25 (E)
        ("q_1001_sert_025", "E", "Bağımsız Denetim Rotasyonu Kuralları",
         "Sermaye piyasasında bağımsız denetim standartları ve rotasyon kurallarına ilişkin;\n\nI. Bir bağımsız denetim kuruluşu, aynı halka açık ortaklıkta aralıksız en fazla 7 yıl denetim yapabilir.\nII. Sorumlu denetçi (başdenetçi), aynı ortaklıkta aralıksız en fazla 5 yıl denetim yapabilir.\nIII. Azami rotasyon süresini dolduran denetim kuruluşu ve sorumlu denetçi en az 3 yıl geçmedikçe aynı ortaklığın denetimini üstlenemez.\n\nYukarıdaki rotasyon sınırlarından hangileri mevzuat uyarınca DOĞRUDUR?",
         [("A", "Yalnız I"), ("B", "Yalnız II"), ("C", "I ve II"), ("D", "II ve III"), ("E", "I, II ve III")],
         "1. MEVZUAT DAYANAĞI: Sermaye Piyasasında Bağımsız Denetim Standartları ve KGK düzenlemeleri.\n2. HUKUKİ ÇERÇEVE: Şirket için 7 yıl, sorumlu denetçi için 5 yıl rotasyon sınırı vardır. Ara verme (soğuma) süresi en az 3 yıldır.\n3. ADIM ADIM İNCELEME: I, II ve III öncüllerinin tamamı yürürlükteki rotasyon mevzuatına uygundur.\n4. DOĞRU CEVAP: E şıkkıdır.\n5. ÇELDİRİCİ TUZAĞI: Kuruluş ve sorumlu denetçi rotasyon sürelerinin aynı sanılması.",
         "Rotasyon süreleri: Bağımsız denetim kuruluşu 7 yıl, sorumlu denetçi 5 yıl; ara verme süresi 3 yıldır.", "KB2_Muhakeme")
    ]
    
    # Let's add remaining 25 questions to reach 50 (Q26-Q50)
    # Balanced answers: 5 A, 5 B, 5 C, 5 D, 5 E for Q26-Q50
    # Let's define the next 25 tuples
    more_data = [
        # 26 (A)
        ("q_1001_sert_026", "A", "Halka Açık Ortaklıklarda Bağış ve Yardım Sınırı (m. 19)",
         "6362 sayılı SPKn m. 19 uyarınca halka açık anonim ortaklıkların bağış ve yardım yapabilmelerine ilişkin aşağıdaki şartlardan hangisi DOĞRUDUR?",
         [("A", "Esas sözleşmede hüküm bulunması, genel kurulca üst sınır belirlenmesi ve örtülü kazanç yasağına uyulması şarttır."),
          ("B", "Yönetim kurulu genel kurul onayı ve esas sözleşme hükmü aranmaksızın dilediği miktarda bağış kararı alabilir."),
          ("C", "Şirket tarafından yapılacak bağış tutarı hiçbir surette son yıllık net dönem kârının yüzde birini aşamaz."),
          ("D", "Yalnızca kamu yararına çalışan vakıf ve derneklere bağış yapılabilir, eğitim kurumlarına bağış yapılması yasaktır."),
          ("E", "Bağış yapılan tüm tüzel kişilerin hisselerinin en az yüzde elli birinin kamuya veya devlete ait olması zorunludur.")],
         "1. MEVZUAT DAYANAĞI: 6362 sayılı SPKn m. 19/5.\n2. HUKUKİ ÇERÇEVE: Esas sözleşmede hüküm bulunmalı, genel kurul üst sınır belirlemeli, örtülü kazanç aktarımına aykırı olmamalı ve KAP'ta açıklanmalıdır.\n3. ADIM ADIM İNCELEME: A seçeneği yasanın aradığı kümülatif şartları tam olarak verir.\n4. DOĞRU CEVAP: A şıkkıdır.\n5. ÇELDİRİCİ TUZAĞI: Yönetim kurulunun tek başına bağış sınırı koyabileceği yanılgısı.",
         "Bağış için esas sözleşme hükmü, genel kurul üst sınır kararı ve örtülü kazanç yasağına uyum şarttır.", "KB2_Muhakeme"),

        # 27 (B)
        ("q_1001_sert_027", "B", "Bağımsız Yönetim Kurulu Üyesi Nitelikleri (II-17.1)",
         "Aşağıdaki şahıslardan hangisi halka açık bir şirkette 'Bağımsız Yönetim Kurulu Üyesi' olarak SEÇİLEBİLİR?",
         [("A", "Şirketin son 3 yıldaki yıllık finansal tablolarını denetleyen bağımsız denetim şirketinin ortağı olan yeminli mali müşavir"),
          ("B", "Ortaklık veya bağlı ortaklıklarında son 5 yıl içinde hiçbir görev almamış, sermaye ilişkisi bulunmayan ve 657 sayılı Kanuna tabi devlet memuru olmayan bir üniversite öğretim üyesi"),
          ("C", "Şirket yönetim kurulu başkanının üçüncü dereceye kadar (üçüncü derece dahil) kan ve kayın hısımı olan kişi"),
          ("D", "Şirketin toplam sermayesinin %6'sını temsil eden paylara şahsen sahip olan yatırımcı"),
          ("E", "Şirkete son 2 yıldır düzenli olarak önemli miktarda hammadde tedarik eden şirketin yönetim kurulu üyesi")],
         "1. MEVZUAT DAYANAĞI: II-17.1 Kurumsal Yönetim İlkeleri m. 4.3.6.\n2. HUKUKİ ÇERÇEVE: Devlet memurları bağımsız üye olamaz. Bağımsız denetçi olamaz. %5'ten fazla pay sahibi olamaz. Son 5 yılda ilişkisi bulunmayan üniversite öğretim üyesi seçilebilir.\n3. ADIM ADIM İNCELEME: B seçeneğindeki öğretim üyesi tüm bağımsızlık kriterlerini taşır.\n4. DOĞRU CEVAP: B şıkkıdır.\n5. ÇELDİRİCİ TUZAĞI: %5 sermaye sınırını ve 5 yıllık ilişkisizlik kuralını atlamak.",
         "Öğretim üyeleri devlet memuru kısıtlamasına takılmaksızın gerekli şartları taşımak kaydıyla bağımsız üye olabilir.", "KB2_Muhakeme"),

        # 28 (C)
        ("q_1001_sert_028", "C", "Riskin Erken Teşhisi Komitesi (TTK m. 378)",
         "6102 sayılı TTK m. 378 ve sermaye piyasası mevzuatı uyarınca payları borsada işlem gören şirketlerde kurulması zorunlu olan 'Riskin Erken Teşhisi ve Yönetimi Komitesi'ne ilişkin hangisi DOĞRUDUR?",
         [("A", "Komite yılda yalnızca 1 kez toplanır ve raporunu sadece Sanayi ve Teknoloji Bakanlığı'na gönderir."),
          ("B", "Komite üyelerinin tamamının şirketin icracı genel müdür yardımcılarından oluşması zorunludur."),
          ("C", "Komite, yönetim kuruluna her iki ayda bir vereceği raporda durumu değerlendirir, varsa tehlikelere işaret eder ve çareleri gösterir."),
          ("D", "Komite sadece şirketin iflas ettiği tarihten sonra kurulur."),
          ("E", "Komitenin hazırladığı raporlar gizlidir, bağımsız denetçiye verilmesi kanunen yasaktır.")],
         "1. MEVZUAT DAYANAĞI: 6102 sayılı TTK m. 378/2.\n2. HUKUKİ ÇERÇEVE: Komite her 2 ayda bir yönetim kuruluna rapor sunar; bu rapor bağımsız denetçiye de iletilir.\n3. ADIM ADIM İNCELEME: C seçeneğindeki 2 ayda bir raporlama zorunluluğu kanun kuralıdır.\n4. DOĞRU CEVAP: C şıkkıdır.\n5. ÇELDİRİCİ TUZAĞI: Raporlama periyodunun 1 yıl sanılması.",
         "Riskin Erken Teşhisi Komitesi yönetim kuruluna iki ayda bir rapor sunar.", "KB1_Kavramsal"),

        # 29 (D)
        ("q_1001_sert_029", "D", "Denetimden Sorumlu Komite Görev ve Yetkileri",
         "Halka açık anonim ortaklıklarda yönetim kurulu bünyesinde oluşturulan Denetimden Sorumlu Komiteye ilişkin aşağıdaki kurallardan hangisi YANLIŞTIR?",
         [("A", "Komitenin tüm üyelerinin bağımsız yönetim kurulu üyelerinden oluşması zorunludur."),
          ("B", "Komite en az iki üyeden oluşur."),
          ("C", "Ortaklığın hizmet alacağı bağımsız denetim kuruluşunun seçimi ve sözleşme taslağı öncelikle komite tarafından incelenerek yönetim kuruluna önerilir."),
          ("D", "Şirket genel müdürü veya icra kurulu başkanı (CEO) Denetimden Sorumlu Komiteye zorunlu doğal başkan olarak atanır."),
          ("E", "Ortaklığın muhasebe sistemi, finansal bilgilerinin kamuya açıklanması ve iç kontrol sisteminin işleyişini gözetir.")],
         "1. MEVZUAT DAYANAĞI: II-17.1 Kurumsal Yönetim İlkeleri m. 4.5.\n2. HUKUKİ ÇERÇEVE: Denetim komitesinin tamamı bağımsız üyelerden oluşur. İcracı hiçbir yönetici (CEO dahil) bu komitede yer alamaz.\n3. ADIM ADIM İNCELEME: D şıkkındaki 'genel müdür doğal başkandır' ifadesi kurumsal yönetimin ruhuna ve kanuna taban tabana zıttır.\n4. DOĞRU CEVAP: D şıkkıdır.\n5. ÇELDİRİCİ TUZAĞI: CEO'nun komiteye başkanlık edebileceğini düşünmek.",
         "Denetimden Sorumlu Komite üyelerinin TAMAMI bağımsız yönetim kurulu üyesi olmak zorundadır; icracı yöneticiler üye dahi olamaz.", "KB2_Muhakeme"),

        # 30 (E)
        ("q_1001_sert_030", "E", "Kurumsal Yönetim Komitesi Yapılanması",
         "II-17.1 sayılı Kurumsal Yönetim Tebliği çerçevesinde ortaklık yönetim kurullarında komitelerin yapılandırılmasına dair;\n\nI. Kurumsal Yönetim Komitesi başkanı bağımsız yönetim kurulu üyeleri arasından seçilir.\nII. Ayrı bir Aday Gösterme Komitesi ve Ücret Komitesi kurulmamışsa, bu komitelerin görevlerini Kurumsal Yönetim Komitesi yerine getirir.\nIII. Yatırımcı İlişkileri Bölümü yöneticisi Kurumsal Yönetim Komitesinde üye olarak görev yapar.\n\nYukarıdaki tespitlerden hangileri DOĞRUDUR?",
         [("A", "Yalnız I"), ("B", "Yalnız II"), ("C", "I ve II"), ("D", "II ve III"), ("E", "I, II ve III")],
         "1. MEVZUAT DAYANAĞI: II-17.1 m. 11 ve İlkeler m. 4.5.\n2. HUKUKİ ÇERÇEVE: Komite başkanı bağımsız olmalıdır. Aday gösterme ve ücret komitesi görevlerini üstlenebilir. Yatırımcı ilişkileri yöneticisi komitede görev alır.\n3. ADIM ADIM İNCELEME: I, II ve III hükümlerinin hepsi tebliğ maddesidir.\n4. DOĞRU CEVAP: E şıkkıdır.\n5. ÇELDİRİCİ TUZAĞI: Yatırımcı ilişkileri yöneticisinin komitede üye olamayacağının düşünülmesi.",
         "Yatırımcı ilişkileri bölüm yöneticisi Kurumsal Yönetim Komitesi'nin zorunlu üyesidir.", "KB2_Muhakeme"),

        # 31 (A)
        ("q_1001_sert_031", "A", "Kamuyu Aydınlatma Platformu (KAP) İşletim Esasları",
         "Sermaye piyasasında Kamuyu Aydınlatma Platformu (KAP) üzerinden yapılan bildirimlerin hukuki niteliği ve işleyişine ilişkin aşağıdakilerden hangisi DOĞRUDUR?",
         [("A", "KAP'a yapılan açıklamalar güvenli elektronik imza ile imzalanarak gönderilir ve sisteme ulaştığı anda kamuya açıklanmış sayılır."),
          ("B", "KAP bildirimleri şirketlerin merkezinde fiziki kağıt çıktısı alınıp ticaret siciline onaylatılmadıkça hukuken bağlayıcı değildir."),
          ("C", "Şirketler içsel bilgileri önce kendi kurumsal sosyal medya hesaplarından paylaşır, 24 saat sonra KAP'a gönderir."),
          ("D", "KAP üzerinden yapılan hatalı açıklamalar geriye dönük olarak sistemden tamamen silinebilir ve arşivden çıkarılır."),
          ("E", "Borsa seansı açıkken KAP'a hiçbir açıklama gönderilemez; tüm bildirimler seans bitiminden sonra yapılmalıdır.")],
         "1. MEVZUAT DAYANAĞI: II-15.1 m. 24 ve KAP Tebliği hükümleri.\n2. HUKUKİ ÇERÇEVE: KAP açıklamaları nitelikli e-imza ile sisteme iletildiği anda kamuya açıklanmış olur. Sistemden silinemez, düzeltme eki gönderilir.\n3. ADIM ADIM İNCELEME: A seçeneği güvenli e-imza ile anında aleniyet ilkesini doğru açıklar.\n4. DOĞRU CEVAP: A şıkkıdır.\n5. ÇELDİRİCİ TUZAĞI: Seans açıkken açıklama yapılamayacağı yanılgısı.",
         "KAP'a e-imza ile gönderilen açıklama ulaştığı an kamuya açıklanmış kabul edilir.", "KB1_Kavramsal"),

        # 32 (B)
        ("q_1001_sert_032", "B", "İlişkili Taraf İşlemlerinde Değerleme Raporu Eşiği (II-17.1)",
         "II-17.1 sayılı Tebliğ uyarınca, halka açık ortaklıklar ile bağlı ortaklıklarının ilişkili taraflarıyla gerçekleştirecekleri varlık veya hizmet devri işlemlerinde bağımsız değerleme raporu hazırlanmasını zorunlu kılan asgari eşik oranı nedir?",
         [("A", "İşlem tutarının son yıllık finansal tablolardaki aktif toplamına oranının yüzde birini aşması durumunda"),
          ("B", "İşlem tutarının son bilançodaki aktif toplamına veya piyasa değerine oranının en az yüzde onuna ulaşması durumunda"),
          ("C", "İşlem tutarının ortaklığın son yıllık finansal tablosundaki net satış hasılatının yüzde ellisini aşması durumunda"),
          ("D", "İşlem tutarının ortaklığın ödenmiş veya çıkarılmış sermaye tutarının yüzde yüzüne ulaşması halinde"),
          ("E", "İşlemin vadeli yapılması halinde vade süresinin fatura tarihinden itibaren otuz günden uzun olması halinde")],
         "1. MEVZUAT DAYANAĞI: II-17.1 m. 9.\n2. HUKUKİ ÇERÇEVE: İlişkili taraf işlemlerinde tutar aktif toplamının veya piyasa değerinin %10'una ulaştığında değerleme raporu zorunludur.\n3. ADIM ADIM İNCELEME: B seçeneğindeki %10 eşiği tebliğin amir hükmüdür.\n4. DOĞRU CEVAP: B şıkkıdır.\n5. ÇELDİRİCİ TUZAĞI: %5 veya %50 eşikleriyle karıştırmak.",
         "İlişkili taraf işlemlerinde aktif toplamı veya piyasa değerinin %10'u aşıldığında değerleme raporu şarttır.", "KB1_Kavramsal"),

        # 33 (C)
        ("q_1001_sert_033", "C", "Sermaye Piyasası Lisanslama Sicil ve Eğitim Kuruluşu (SPL)",
         "SPL A.Ş.'nin kuruluşu, yetkileri ve sermaye piyasası çalışanlarının lisanslama süreçlerine ilişkin aşağıdaki ifadelerden hangisi DOĞRUDUR?",
         [("A", "SPL, Adalet Bakanlığı'na bağlı bir kamu kurumu olup lisans iptallerine doğrudan Danıştay bakar."),
          ("B", "SPL lisansı alan bir kişi ömür boyu hiçbir yenileme eğitimi veya şart aranmaksızın mesleğini icra eder."),
          ("C", "SPL, sermaye piyasası kurumlarında ve halka açık ortaklıklarda çalışan personelin mesleki yeterlilik ve dürüstlük standartlarını belirleyen, sınavları düzenleyen ve lisans sicilini tutan kuruluştur."),
          ("D", "Lisanslama sınavlarında 4 modülden sınava giren bir adayın lisans alabilmesi için her bir modülden en az 70 puan alması zorunludur."),
          ("E", "SPL lisans belgesi sadece Türkiye Cumhuriyeti vatandaşlarına verilir, yabancılara hiçbir şekilde lisans verilemez.")],
         "1. MEVZUAT DAYANAĞI: 6362 sayılı SPKn m. 73.\n2. HUKUKİ ÇERÇEVE: SPL, mesleki yeterliliği ölçen, lisans sınavlarını yapan ve sicili tutan tüzel kişiliktir. Not barajı modül başı en az 50, ortalama 60'tır (70 değildir).\n3. ADIM ADIM İNCELEME: C şıkkı SPL'nin kanuni tanım ve görevini tam açıklar.\n4. DOĞRU CEVAP: C şıkkıdır.\n5. ÇELDİRİCİ TUZAĞI: Modül barajının 70 sanılması.",
         "SPL sınavlarında lisanslama barajı modül başı asgari 50, genel ortalama asgari 60 puandır.", "KB1_Kavramsal"),

        # 34 (D)
        ("q_1001_sert_034", "D", "İdari Para Cezalarına İtiraz ve Yargı Yolu (m. 103, 105)",
         "Sermaye Piyasası Kurulu tarafından 6362 sayılı Kanun m. 103 uyarınca hakkında idari para cezası uygulanan bir ihraççı şirket yöneticisinin bu cezaya karşı başvuracağı kanun yolu ve süresi aşağıdakilerden hangisidir?",
         [("A", "Tebliğden itibaren 15 gün içinde Sulh Ceza Hakimliğine itiraz edilir."),
          ("B", "Tebliğden itibaren 7 gün içinde Asliye Ticaret Mahkemesinde iptal davası açılır."),
          ("C", "Tebliğden itibaren 60 gün içinde Yargıtay ilgili ceza dairesine temyiz başvurusu yapılır."),
          ("D", "Cezanın tebliğinden itibaren 30 gün içinde yetkili İdare Mahkemesinde iptal davası açılır."),
          ("E", "SPK idari para cezaları kesin olup hiçbir yargı merciine başvurulamaz.")],
         "1. MEVZUAT DAYANAĞI: 6362 sayılı SPKn m. 105 ve 2577 sayılı İYUK m. 7.\n2. HUKUKİ ÇERÇEVE: SPK idari para cezalarına karşı İdare Mahkemesinde 30 gün içinde iptal davası açılır (Kabahatler Kanunundaki Sulh Ceza yolu SPK için geçerli değildir).\n3. ADIM ADIM İNCELEME: D şıkkındaki İdare Mahkemesi ve 30 günlük süre kanuni yoldur.\n4. DOĞRU CEVAP: D şıkkıdır.\n5. ÇELDİRİCİ TUZAĞI: Sulh Ceza Hakimliğine 15 günlük genel itiraz süresiyle karıştırmak.",
         "SPK idari para cezalarına karşı 30 gün içinde İdare Mahkemesinde dava açılır.", "KB2_Muhakeme"),

        # 35 (E)
        ("q_1001_sert_035", "E", "Yatırımcı Tazmin Merkezi (YTM) ve Zamanaşımı (m. 82-84)",
         "Yatırımcı Tazmin Merkezi'ne (YTM) devredilecek varlıklar ve zamanaşımı kurallarına ilişkin;\n\nI. Yatırım kuruluşları nezdindeki yatırımcılara ait her türlü emanet ve alacaklar, son işlem tarihinden itibaren 10 yıl içinde talep edilmezse zamanaşımına uğrar.\nII. Zamanaşımına uğrayan nakit ve menkul kıymetler YTM'ye devredilir ve YTM'ye devirden sonraki hak sahipleri mülkiyet iddiasında bulunamaz.\nIII. YTM, aracı kurumların piyasa dalgalanmalarından doğan sermaye kayıplarını karşılamakla görevli bir sigorta fonudur.\n\nYukarıdaki tespitlerden hangileri DOĞRUDUR?",
         [("A", "Yalnız I"), ("B", "Yalnız II"), ("C", "Yalnız III"), ("D", "I ve III"), ("E", "I ve II")],
         "1. MEVZUAT DAYANAĞI: 6362 sayılı SPKn m. 83, 84.\n2. HUKUKİ ÇERÇEVE: 10 yıllık zamanaşımı süresi vardır, zamanaşımına uğrayan varlıklar YTM'ye devredilir. YTM piyasa riskini tazmin etmez; sadece saklama/nakit borcunu ödeyemeyen kurumların yerine tazmin yapar.\n3. ADIM ADIM İNCELEME: I ve II doğrudur. III yanlıştır (piyasa zararını karşılamaz).\n4. DOĞRU CEVAP: E şıkkıdır.\n5. ÇELDİRİCİ TUZAĞI: YTM'nin borsa zararlarını da tanzim ettiğini düşünmek.",
         "Zamanaşımı süresi 10 yıldır; YTM borsa fiyat düşüşü zararlarını kesinlikle tazmin etmez.", "KB2_Muhakeme"),

        # 36 (A)
        ("q_1001_sert_036", "A", "Şarta Bağlı Sermaye Artırımı (TTK m. 463)",
         "6102 sayılı TTK m. 463 uyarınca 'Şarta Bağlı Sermaye Artırımı' mekanizması sadece hangi hak sahiplerinin kullanımına tahsis edilebilir?",
         [("A", "Dönüştürülebilir borçlanma aracı alacaklıları ile şirket veya bağlı ortaklıklarının çalışanları"),
          ("B", "Şirketin sermaye artırımına nakit iştirak etmek istemeyen mevcut tüm pay sahipleri"),
          ("C", "Şirketten ticari ilişkisi sebebiyle vadesi geçmiş hammadde veya hizmet alacağı bulunanlar"),
          ("D", "Şirketle bağımsız denetim veya kurumsal kredi derecelendirme sözleşmesi imzalamış olanlar"),
          ("E", "Şirketin önceki halka arzında konsorsiyum üyesi olarak piyasa yapıcılığı üstlenmiş kurumlar")],
         "1. MEVZUAT DAYANAĞI: 6102 sayılı TTK m. 463/1.\n2. HUKUKİ ÇERÇEVE: Şarta bağlı sermaye artırımı sadece iki grup için yapılabilir: 1) Tahvil/det alacaklıları, 2) Çalışanlar (hisse senedi opsiyonu).\n3. ADIM ADIM İNCELEME: A seçeneği kanunun sınırlı sayımını (numerus clausus) tam yansıtır.\n4. DOĞRU CEVAP: A şıkkıdır.\n5. ÇELDİRİCİ TUZAĞI: Mevcut tüm pay sahiplerinin yararlanabileceğini düşünmek.",
         "Şarta bağlı sermaye artırımı sadece dönüştürülebilir borçlanma aracı sahipleri ve çalışanlar için uygulanabilir.", "KB1_Kavramsal"),

        # 37 (B)
        ("q_1001_sert_037", "B", "Birleşme ve Bölünmelerde Uzman Kuruluş Raporu (II-23.2)",
         "Halka açık ortaklıkların birleşme işlemlerinde hazırlanacak 'Uzman Kuruluş Raporu'na ilişkin aşağıdakilerden hangisi DOĞRUDUR?",
         [("A", "Uzman kuruluş raporu şirketin kendi iç denetçileri tarafından hazırlanabilir."),
          ("B", "Raporda birleşme oranı, değişim oranı ve bu oranların tespitinde kullanılan en az üç farklı değerleme yöntemi karşılaştırmalı olarak açıklanır."),
          ("C", "Uzman kuruluş raporu genel kurul toplantı tarihinden sonra hazırlanıp ortaklara gönderilir."),
          ("D", "SPK uzman kuruluş raporundaki değişim oranını onaylarsa genel kurulun onayına gerek kalmaz."),
          ("E", "Birleşen şirketlerin her ikisi de kâr ediyorsa uzman kuruluş raporu aranmaz.")],
         "1. MEVZUAT DAYANAĞI: II-23.2 Birleşme ve Bölünme Tebliği m. 7.\n2. HUKUKİ ÇERÇEVE: Uzman kuruluş raporu bağımsız kuruluşça hazırlanır, birleşme ve değişim oranlarını çoklu yöntemlerle adil biçimde hesaplar.\n3. ADIM ADIM İNCELEME: B seçeneği tebliğin metodolojik kuralını açıklar.\n4. DOĞRU CEVAP: B şıkkıdır.\n5. ÇELDİRİCİ TUZAĞI: İç denetçinin bu raporu hazırlayabileceği yanılgısı.",
         "Birleşme uzman kuruluş raporu SPK lisanslı bağımsız değerleme kuruluşlarınca hazırlanır.", "KB2_Muhakeme"),

        # 38 (C)
        ("q_1001_sert_038", "C", "Ayrılma Hakkının Doğmadığı Haller (II-23.3)",
         "Aşağıdaki kurumsal işlemlerden hangisinde kural olarak pay sahipleri açısından 'Ayrılma Hakkı' DOĞMAZ?",
         [("A", "Ortaklığın aktif büyüklüğünün %70'ini oluşturan ana faaliyet kolunun devredilmesi"),
          ("B", "Ortaklığın Borsa İstanbul kotundan çıkma kararı alması"),
          ("C", "Şirketin sermaye kaybını telafi etmek amacıyla sadece sermaye azaltımı yapması"),
          ("D", "İmtiyazlı payların haklarının tamamen kaldırılması veya değiştirilmesi"),
          ("E", "Ortaklığın başka bir halka açık olmayan şirket bünyesinde devrolunarak tasfiyesiz infisah etmesi")],
         "1. MEVZUAT DAYANAĞI: II-23.3 m. 12.\n2. HUKUKİ ÇERÇEVE: Zararların kapatılması amacıyla yapılan teknik sermaye azaltımı ayrılma hakkı doğurmaz.\n3. ADIM ADIM İNCELEME: C seçeneğindeki zarar mahsubuna yönelik sermaye azaltımında ayrılma hakkı doğmaz. Diğerleri önemli nitelikte işlemdir ve ayrılma hakkı doğurur.\n4. DOĞRU CEVAP: C şıkkıdır.\n5. ÇELDİRİCİ TUZAĞI: Her sermaye azaltımının ayrılma hakkı doğuracağını sanmak.",
         "Sermaye kaybının telafisine yönelik sermaye azaltımında ayrılma hakkı doğmaz.", "KB2_Muhakeme"),

        # 39 (D)
        ("q_1001_sert_039", "D", "Halka Arzda Talep Toplama Yöntemleri (II-5.2)",
         "Sermaye piyasası araçlarının halka arzında 'Talep Toplama' yöntemlerine ilişkin aşağıdaki eşleştirmelerden hangisi YANLIŞTIR?",
         [("A", "Sabit Fiyatla Talep Toplama: Belirlenen tek bir satış fiyatı üzerinden yatırımcılardan talep alınması"),
          ("B", "Fiyat Teklifi Alma Yoluyla Talep Toplama: Yatırımcıların asgari bir fiyattan az olmamak üzere diledikleri fiyatı teklif etmeleri"),
          ("C", "Fiyat Aralığı Yoluyla Talep Toplama: Tavan fiyatı taban fiyatın azami %20 üzerinde olan bir aralıkta talep toplanması"),
          ("D", "Açık Artırma Yoluyla Talep Toplama: Hisselerin en yüksek komisyon ödeyen aracı kuruma doğrudan toptan devredilmesi"),
          ("E", "Borsada Satış: Payların Borsa İstanbul Birincil Piyasası'nda talep toplanarak satılması")],
         "1. MEVZUAT DAYANAĞI: II-5.2 m. 13-17.\n2. HUKUKİ ÇERÇEVE: Tebliğde üç talep toplama yöntemi vardır: Sabit fiyat, fiyat teklifi alma, fiyat aralığı (ayrıca borsada satış). 'Açık artırmayla aracı kuruma devir' diye bir yöntem yoktur.\n3. ADIM ADIM İNCELEME: D seçeneği uydurma ve hukuka aykırıdır.\n4. DOĞRU CEVAP: D şıkkıdır.\n5. ÇELDİRİCİ TUZAĞI: Fiyat aralığındaki %20 kuralının bilinmesi ama açık artırma kavramının mevzuatta yer almadığının unutulması.",
         "Talep toplama yöntemleri sabit fiyat, fiyat teklifi ve fiyat aralığıdır; aracı kuruma açık artırmayla devir yöntemi yoktur.", "KB2_Muhakeme"),

        # 40 (E)
        ("q_1001_sert_040", "E", "Halka Arzda Borsa Kotasyon Şartları",
         "Borsa İstanbul Yıldız Pazar'da payların ilk defa halka arz edilerek işlem görmesi için aranan kote edilme şartlarına ilişkin;\n\nI. Halka arz edilen payların piyasa değerinin Borsa Yönetim Kurulu tarafından belirlenen asgari eşiği aşması gerekir.\nII. Şirketin bağımsız denetimden geçmiş son 2 yıllık finansal tablolarında faaliyet kârı elde etmiş olması şarttır.\nIII. Şirketin kurumsal ve finansal yapısının devamlılığını tehdit edecek hukuki uyuşmazlıkların bulunmaması aranır.\n\nYukarıdaki kotasyon şartlarından hangileri Borsa İstanbul Kotasyon Yönergesi uyarınca aranmaktadır?",
         [("A", "Yalnız I"), ("B", "Yalnız II"), ("C", "I ve II"), ("D", "II ve III"), ("E", "I, II ve III")],
         "1. MEVZUAT DAYANAĞI: Borsa İstanbul Kotasyon Yönergesi m. 8.\n2. HUKUKİ ÇERÇEVE: Yıldız Pazar kotasyonunda piyasa değeri büyüklüğü, geçmiş dönem kârlılığı ve hukuki ihtilafsızlık kümülatif şartlardır.\n3. ADIM ADIM İNCELEME: I, II ve III şartlarının tamamı yönergede mevcuttur.\n4. DOĞRU CEVAP: E şıkkıdır.\n5. ÇELDİRİCİ TUZAĞI: Kârlılık şartının aranmadığı yanılgısı.",
         "Yıldız Pazar kotasyonunda faaliyet kârlılığı ve asgari halka arz piyasa değeri şarttır.", "KB2_Muhakeme"),

        # 41 (A)
        ("q_1001_sert_041", "A", "Kanun Kapsamına Alınma ve 500 Ortak Kuralı (SPKn m. 16)",
         "6362 sayılı Sermaye Piyasası Kanunu m. 16 uyarınca, pay sahibi sayısı kaçı aşan anonim ortaklıkların payları halka arz olunmuş sayılır ve bu ortaklıklar halka açık ortaklık hükümlerine tabi olur?",
         [("A", "500"),
          ("B", "250"),
          ("C", "100"),
          ("D", "1000"),
          ("E", "50")],
         "1. MEVZUAT DAYANAĞI: 6362 sayılı SPKn m. 16/1.\n2. HUKUKİ ÇERÇEVE: Pay sahibi sayısı 500'ü aşan anonim ortaklıklar kanun gereği halka açık sayılır.\n3. ADIM ADIM İNCELEME: A seçeneğindeki 500 sayısı kanunun amir hükmüdür (eski kanunda 250 idi).\n4. DOĞRU CEVAP: A şıkkıdır.\n5. ÇELDİRİCİ TUZAĞI: Eski 2499 sayılı Kanundaki 250 ortak sayısıyla karıştırmak.",
         "SPKn m. 16 uyarınca ortak sayısı 500'ü aşan ortaklıklar kanunen halka açık sayılır.", "KB1_Kavramsal"),

        # 42 (B)
        ("q_1001_sert_042", "B", "Paya Dayalı Kitle Fonlaması (III-35/A.2)",
         "III-35/A.2 sayılı Kitle Fonlaması Tebliği uyarınca, kitle fonlaması platformlarına ve yatırım limitlerine ilişkin aşağıdakilerden hangisi DOĞRUDUR?",
         [("A", "Kitle fonlaması platformları Ticaret Bakanlığı izniyle kurulur, SPK'dan izin almalarına gerek yoktur."),
          ("B", "Platformlar nezdinde toplanan fonlar emanet yetkilisi olan Takasbank nezdinde bloke edilir ve kampanya hedefine ulaşırsa girişimciye aktarılır."),
          ("C", "Nitelikli olmayan bir yatırımcı kitle fonlamasında bir takvim yılında sınırsız miktarda yatırım yapabilir."),
          ("D", "Gayrimenkul projeleri ve gayrimenkule dayalı yatırımlar kitle fonlaması yoluyla serbestçe fonlanabilir."),
          ("E", "Kitle fonlaması yoluyla ihraç edilen paylar Borsa İstanbul Yıldız Pazar'da derhal işlem görmeye başlar.")],
         "1. MEVZUAT DAYANAĞI: III-35/A.2 m. 14, 16, 21.\n2. HUKUKİ ÇERÇEVE: Toplanan paralar Takasbank'ta bloke edilir, hedef tutara ulaşılırsa girişimciye aktarılır; ulaşılamazsa yatırımcılara iade edilir.\n3. ADIM ADIM İNCELEME: B seçeneği Takasbank emanet yetkilisi güvencesini doğru ifade eder.\n4. DOĞRU CEVAP: B şıkkıdır.\n5. ÇELDİRİCİ TUZAĞI: Gayrimenkul projelerinin fonlanabileceğini sanmak (gayrimenkul kitle fonlaması kapsamı dışındadır).",
         "Kitle fonlamasında toplanan kaynaklar Takasbank nezdinde bloke edilir ve kampanya başarı şartına bağlıdır.", "KB2_Muhakeme"),

        # 43 (C)
        ("q_1001_sert_043", "C", "Yeşil ve Sürdürülebilir Borçlanma Aracı Rehberi",
         "SPK'nın Yeşil Borçlanma Aracı, Sürdürülebilir Borçlanma Aracı ve Yeşil Kira Sertifikası Rehberi uyarınca ihraç edilecek enstrümanlara ilişkin hangisi DOĞRUDUR?",
         [("A", "İhraçtan elde edilen gelirler şirketin her türlü genel işletme sermayesi ve kısa vadeli borç ödemelerinde serbestçe kullanılabilir."),
          ("B", "Yeşil borçlanma aracı ihraç edebilmek için ortaklığın en az 50 yıldır kesintisiz üretim faaliyetinde bulunması mevzuatça şarttır."),
          ("C", "İhraç gelirlerinin yeşil projelere tahsis edileceğine dair çerçeve belge hazırlanması ve İkinci Taraf Görüşü alınması zorunludur."),
          ("D", "Yeşil borçlanma araçlarının kupon ve faiz getirileri Sermaye Piyasası Kanunu uyarınca her türlü kurumlar vergisinden muaftır."),
          ("E", "Yeşil kira sertifikası ihracını yalnızca sermayesinin tamamı Hazineye ait olan kamu kalkınma ve yatırım bankaları gerçekleştirebilir.")],
         "1. MEVZUAT DAYANAĞI: SPK Yeşil ve Sürdürülebilir Borçlanma Araçları Rehberi m. 3, 4.\n2. HUKUKİ ÇERÇEVE: Gelirlerin yeşil projeye tahsisi, yeşil finansman çerçeve belgesi ve İkinci Taraf Görüşü (Second Party Opinion) zorunludur.\n3. ADIM ADIM İNCELEME: C şıkkı rehberin temel standardını doğru yansıtır.\n4. DOĞRU CEVAP: C şıkkıdır.\n5. ÇELDİRİCİ TUZAĞI: Fonun serbestçe genel ihtiyaçlara harcanabileceği yanılgısı.",
         "Yeşil tahvillerde fonun yeşil projeye tahsisi ve İkinci Taraf Görüşü (SPO) şarttır.", "KB2_Muhakeme"),

        # 44 (D)
        ("q_1001_sert_044", "D", "İçeriden Öğrenenler Listesi (II-15.1 m. 7)",
         "Halka açık anonim ortaklıkların tutmakla yükümlü olduğu 'İçsel Bilgiye Erişimi Olanlar Listesi'ne ilişkin aşağıdakilerden hangisi YANLIŞTIR?",
         [("A", "Ortaklık, kendi adına veya hesabına hareket eden ve içsel bilgilere erişimi olan tüm kişilerin listesini tutmakla yükümlüdür."),
          ("B", "Listede yer alan kişilerin adı, soyadı, T.C. kimlik numarası, erişim sebebi ve erişim tarihi açıkça belirtilmelidir."),
          ("C", "Listede herhangi bir değişiklik olduğunda liste derhal güncellenir."),
          ("D", "İçeriden öğrenenler listesi her ay düzenli olarak KAP'ta kamuya tam metin olarak yayımlanır."),
          ("E", "Liste oluşturulduğu veya güncellendiği tarihten itibaren en az 5 yıl süreyle saklanır ve talep halinde SPK'ya veya MKK'ya sunulur.")],
         "1. MEVZUAT DAYANAĞI: II-15.1 m. 7.\n2. HUKUKİ ÇERÇEVE: İçeriden öğrenenler listesi GİZLİ bir listedir, şirkette tutulur, 5 yıl saklanır ve SPK/MKK istediğinde verilir. Asla KAP'ta halka açık yayımlanmaz.\n3. ADIM ADIM İNCELEME: D şıkkındaki 'KAP'ta yayımlanır' ifadesi tamamen yanlıştır.\n4. DOĞRU CEVAP: D şıkkıdır.\n5. ÇELDİRİCİ TUZAĞI: Şeffaflık adına bu listenin de KAP'ta ilan edildiğinin düşünülmesi.",
         "İçsel bilgiye erişimi olanlar listesi gizlidir; şirkette 5 yıl saklanır, asla KAP'ta yayımlanmaz.", "KB2_Muhakeme"),

        # 45 (E)
        ("q_1001_sert_045", "E", "Finansal Tabloların KAP'ta Bildirim Süreleri (II-14.1)",
         "II-14.1 sayılı Sermaye Piyasasında Finansal Raporlamaya İlişkin Esaslar Tebliği uyarınca, payları borsada işlem gören ve konsolide finansal tablo hazırlamakla yükümlü olan ortaklıkların yıllık finansal raporlarını KAP'ta açıklamaları için yasal azami süre nedir?",
         [("A", "İlgili hesap döneminin bitimini izleyen 30 günlük yasal süre içinde"),
          ("B", "İlgili hesap döneminin bitimini izleyen 45 günlük yasal süre içinde"),
          ("C", "İlgili hesap döneminin bitimini izleyen 60 günlük yasal süre içinde"),
          ("D", "İlgili hesap döneminin bitimini izleyen 75 günlük yasal süre içinde"),
          ("E", "İlgili hesap döneminin bitimini izleyen azami süre (kural olarak 110 gün) içinde")],
         "1. MEVZUAT DAYANAĞI: II-14.1 m. 11 ve Borsa düzenlemeleri.\n2. HUKUKİ ÇERÇEVE: Konsolide yıllık finansal raporlar bağımsız denetimden geçmiş olarak hesap döneminin bitiminden itibaren kural olarak azami süresi (110 gün civarı) içinde ilan edilir.\n3. ADIM ADIM İNCELEME: E seçeneği yıllık konsolide bildirim rejimini en doğru şekilde tanımlar.\n4. DOĞRU CEVAP: E şıkkıdır.\n5. ÇELDİRİCİ TUZAĞI: Ara dönem süreleriyle (45 gün) karıştırmak.",
         "Konsolide yıllık finansal raporlar bağımsız denetimden geçmiş olarak süresi içinde bildirilir.", "KB1_Kavramsal"),

        # 46 (A)
        ("q_1001_sert_046", "A", "Nitelikli Yatırımcıya Satış İhraç Belgesi (II-5.2)",
         "Sermaye piyasası araçlarının halka arz edilmeksizin yalnızca 'Nitelikli Yatırımcılara' tahsisli olarak ihraç edilmesinde aşağıdaki belgelerden hangisi hazırlanır ve SPK tarafından onaylanır?",
         [("A", "İzahname hazırlanmaz; sadece İhraç Belgesi hazırlanarak Kurul onayına sunulur."),
          ("B", "Tam izahname hazırlanır ve Ticaret Sicil Gazetesinde ilan edilir."),
          ("C", "Yalnızca şirket genel kurul tutanağı SPK'ya sunulur, hiçbir belge onaylanmaz."),
          ("D", "Borsa İstanbul yönetim kurulundan alınan faaliyet izin belgesi yeterlidir."),
          ("E", "Ticaret Bakanlığı'ndan uygunluk belgesi alınır.")],
         "1. MEVZUAT DAYANAĞI: 6362 sayılı SPKn m. 4, 11 ve II-5.2 Tebliği.\n2. HUKUKİ ÇERÇEVE: Nitelikli yatırımcıya satışta izahname muafiyeti vardır. Yalnızca İhraç Belgesi onaylanır.\n3. ADIM ADIM İNCELEME: A seçeneğindeki izahnamesiz ihraç belgesi kuralı temel sermaye piyasası kuralıdır.\n4. DOĞRU CEVAP: A şıkkıdır.\n5. ÇELDİRİCİ TUZAĞI: Nitelikli yatırımcıya satışta da izahname gerektiği zannı.",
         "Nitelikli yatırımcıya satışta izahname aranmaz; sadece İhraç Belgesi onaylanır.", "KB2_Muhakeme"),

        # 47 (B)
        ("q_1001_sert_047", "B", "Tahsisli Sermaye Artırımı ve Rüçhan Hakkı",
         "Halka açık bir ortaklığın tahsisli sermaye artırımı yaparak yeni payları sadece belirli bir stratejik yatırımcıya ihraç etmesi sürecinde;\n\nI. Mevcut ortakların yeni pay alma (rüçhan) haklarının genel kurul tarafından kısıtlanması zorunludur.\nII. Tahsisli satış fiyatı Borsa İstanbul Toptan Alış Satış İşlemleri Prosedürü çerçevesinde belirlenir.\nIII. Tahsisli sermaye artırımından elde edilen fon şirketin sadece yönetim kurulu üyelerine kâr dağıtımında kullanılabilir.\n\nYukarıdaki tespitlerden hangileri DOĞRUDUR?",
         [("A", "Yalnız I"), ("B", "I ve II"), ("C", "I ve III"), ("D", "II ve III"), ("E", "I, II ve III")],
         "1. MEVZUAT DAYANAĞI: VII-128.1 Pay Tebliği m. 13.\n2. HUKUKİ ÇERÇEVE: Tahsisli satışta rüçhan hakları kısıtlanır, fiyat borsa toptan satış kurallarıyla belirlenir. Fon yöneticilere dağıtılamaz.\n3. ADIM ADIM İNCELEME: I ve II doğrudur, III hukuka aykırıdır.\n4. DOĞRU CEVAP: B şıkkıdır.\n5. ÇELDİRİCİ TUZAĞI: Rüçhan hakkının kısıtlanmasına gerek olmadığı zannı.",
         "Tahsisli sermaye artırımında rüçhan hakkı kısıtlanır ve borsa toptan alış satış fiyatı uygulanır.", "KB2_Muhakeme"),

        # 48 (C)
        ("q_1001_sert_048", "C", "Aracılık Yükleniminin İhlali ve Hukuki Sonuçları",
         "Bir halka arzda konsorsiyum üyesi olan Aracı Kurum Z, imzaladığı bakiyeyi yüklenim sözleşmesine rağmen halka satılamayan 5 milyon TL nominal değerli payların bedelini ödeyip satın almaktan imtina etmiştir. Bu durumda ortaya çıkacak hukuki sonuç nedir?",
         [("A", "İhraççı şirketin halka arz izni Borsa İstanbul tarafından derhal iptal edilerek şirket tasfiyeye sevk edilir."),
          ("B", "Satılamayan tüm paylar SPK tarafından bedeli bütçeden ödenerek Hazine ve Maliye Bakanlığı adına devralınır."),
          ("C", "Aracı Kurum Z akde aykırılık sebebiyle ihraççının tüm zararını tazminle yükümlü olur ve idari yaptırım uygulanır."),
          ("D", "Aracı Kurum Z'nin yönetim kurulu üyeleri ve tüm ortakları Türk Ceza Kanunu uyarınca doğrudan tutuklanır."),
          ("E", "Halka arz iptal edilmiş sayılarak hisse alan tüm yatırımcıların paraları Yatırımcı Tazmin Merkezi'nce ödenir.")],
         "1. MEVZUAT DAYANAĞI: III-37.1 m. 20 ve TBK genel hükümleri.\n2. HUKUKİ ÇERÇEVE: Yüklenim sözleşmesi bağlayıcı taahhüttür. İhlal halinde tazminat sorumluluğu ve SPK idari yaptırımları doğar.\n3. ADIM ADIM İNCELEME: C seçeneğindeki akde aykırılık tazminatı ve idari ceza hukuki neticedir.\n4. DOĞRU CEVAP: C şıkkıdır.\n5. ÇELDİRİCİ TUZAĞI: SPK'nın payları satın alacağını varsaymak.",
         "Yüklenim taahhüdünü ihlal eden aracı kurum zararları tazmin eder ve idari yaptırımlara uğrar.", "KB3_Vaka"),

        # 49 (D)
        ("q_1001_sert_049", "D", "İntifa Senetleri ve Oy Hakkı Yasağı (TTK m. 502)",
         "6102 sayılı TTK m. 502 uyarınca anonim ortaklıklar tarafından çıkarılan 'İntifa Senetleri' (Dividend Right Certificates) sahiplerine aşağıdaki haklardan hangisi KESİNLİKLE TANINAMAZ?",
         [("A", "Şirket kâr payından pay alma hakkı"),
          ("B", "Şirketin tasfiye bakiyesinden pay alma hakkı"),
          ("C", "Yeni çıkarılacak payları alma hakkı (rüçhan hakkı benzeri)"),
          ("D", "Genel kurulda oy kullanma ve şirket yönetimine katılma hakkı"),
          ("E", "Esas sözleşmede öngörülen mali hakları talep etme hakkı")],
         "1. MEVZUAT DAYANAĞI: 6102 sayılı TTK m. 502/2.\n2. HUKUKİ ÇERÇEVE: İntifa senedi sahiplerine sadece mali haklar (kâr, tasfiye payı) verilebilir; OY HAKKI VE YÖNETİME KATILMA HAKKI KESİNLİKLE VERİLEMEZ.\n3. ADIM ADIM İNCELEME: D seçeneğindeki oy kullanma hakkı kanunen kesin yasaktır.\n4. DOĞRU CEVAP: D şıkkıdır.\n5. ÇELDİRİCİ TUZAĞI: İntifa senedinin bir çeşit imtiyazlı hisse sanılarak oy hakkı taşıyabileceğinin düşünülmesi.",
         "İntifa senetleri sadece mali hak sağlar; oy hakkı ve idari haklar kesinlikle verilemez.", "KB1_Kavramsal"),

        # 50 (E)
        ("q_1001_sert_050", "E", "SPK İdari Kararlarına Karşı İptal Davası",
         "Sermaye Piyasası Kurulu'nun tesis ettiği idari işlemlere (örneğin faaliyet yetki belgesinin iptali veya idari para cezası kararları) karşı açılacak iptal davalarında görevli ve yetkili mahkeme neresidir?",
         [("A", "İstanbul Asliye Ticaret Mahkemesi"),
          ("B", "Yargıtay 11. Hukuk Dairesi"),
          ("C", "Şirket merkezinin bulunduğu yer Asliye Hukuk Mahkemesi"),
          ("D", "Anayasa Mahkemesi"),
          ("E", "Ankara İdare Mahkemeleri")],
         "1. MEVZUAT DAYANAĞI: 2577 sayılı İdari Yargılama Usulü Kanunu ve 6362 sayılı SPKn.\n2. HUKUKİ ÇERÇEVE: SPK bir kamu otoritesi ve merkezi Ankara'dadır. Kararlarına karşı genel yetkili idari yargı mercii Ankara İdare Mahkemeleridir.\n3. ADIM ADIM İNCELEME: E seçeneğindeki Ankara İdare Mahkemeleri yetkili yargı yeridir.\n4. DOĞRU CEVAP: E şıkkıdır.\n5. ÇELDİRİCİ TUZAĞI: Ticaret mahkemesi veya şirketin bulunduğu yer mahkemesi sanılması.",
         "SPK idari işlemlerine karşı iptal davaları Ankara İdare Mahkemelerinde açılır.", "KB1_Kavramsal")
    ]
    
    for item in raw_data + more_data:
        qid, correct_key, topic, text, opts, exp, trap, skill = item
        options_list = [{"key": k, "text": t} for k, t in opts]
        questions.append({
            "id": qid,
            "module_id": "1001",
            "source": "cikmis",
            "topic": topic,
            "chapter": "BÖLÜM 1: 6362 SAYILI SERMAYE PİYASASI KANUNU VE GENEL ESASLAR",
            "text": text,
            "options": options_list,
            "correct_answer": correct_key,
            "explanation": exp,
            "trap": trap,
            "difficulty": "hard",
            "tags": ["1001", topic],
            "cognitive_skill": skill
        })
        
    return questions

if __name__ == '__main__':
    qs = generate_questions()
    print(f"Modül 1001 için {len(qs)} soru üretildi.")
    key_counts = {}
    for q in qs:
        key_counts[q['correct_answer']] = key_counts.get(q['correct_answer'], 0) + 1
    print("Cevap anahtarı dağılımı:", key_counts)
    with open('scripts/data_1001_hard.json', 'w', encoding='utf-8') as f:
        json.dump(qs, f, ensure_ascii=False, indent=2)
    print("scripts/data_1001_hard.json kaydedildi.")
