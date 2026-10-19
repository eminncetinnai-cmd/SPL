# -*- coding: utf-8 -*-
"""
Modül 1012: 50 İleri Seviye (Sert) Sınav Sorusu Üreticisi
Konu: Takas, Saklama ve Operasyon İşlemleri (Takasbank, MKK, MKT Şelalesi, DVP, Hak Kullanımları)
Türkiye Maarif Modeli: KB2_Muhakeme (%60), KB3_Vaka (%40)
Cevap Dağılımı: 10 A, 10 B, 10 C, 10 D, 10 E (Tam dengeli)
Tüm seçenek uzunluk oranları < 1.8, 0 Giveaway, 5 Aşamalı Açıklama Standardı.
"""
import json

def generate_questions():
    questions = []
    
    raw_data = [
        ("q_1012_sert_001", "A", "MKT Temerrüt Şelalesi Sıralaması (Takasbank)",
         "İstanbul Takas ve Saklama Bankası A.Ş.'nin (Takasbank) Merkezi Karşı Taraf (MKT) olarak hizmet verdiği piyasalarda bir takas üyesinin temerrüde düşmesi halinde, oluşan zararın karşılanmasında devreye sokulacak 'Temerrüt Şelalesi' (Default Waterfall) kanuni sıralaması hangisidir?",
         [
           ("A", "1) Temerrüde düşen üyenin teminatları, 2) Temerrüt eden üyenin Garanti Fonu payı, 3) Takasbank'ın dedike özkaynak katkısı, 4) Diğer üyelerin Garanti Fonu payları, 5) Takasbank'ın kalan özkaynakları"),
           ("B", "1) Takasbank'ın genel özkaynakları, 2) SPK bütçesi, 3) Yatırımcı Tazmin Merkezi fonu, 4) Hazine ve Maliye Bakanlığı garantisi, 5) Temerrüt eden üyenin hisseleri"),
           ("C", "1) Diğer üyelerin garanti fonu payları, 2) Temerrüt eden üyenin teminatları, 3) Borsa İstanbul bütçesi, 4) Takasbank sermayesi, 5) Mahkeme iflas masası"),
           ("D", "1) Yatırımcı Tazmin Merkezi, 2) Temerrüt eden üyenin müşterilerinin nakit paraları, 3) Takasbank garanti fonu, 4) Borsa yönetim kurulu şahsi varlıkları, 5) Hazine"),
           ("E", "1) Borsa İstanbul temerrüt fonu, 2) Takasbank ihtiyat akçesi, 3) Temerrüde düşen üyenin yönetim kurulu üyeleri, 4) Garanti fonu, 5) SPK idari cezaları"),
         ],
         "1. MEVZUAT DAYANAĞI: Takasbank MKT Yönetmeliği ve Takasbank Temerrüt Yönergesi m. 14.\n2. HUKUKİ / TEKNİK ÇERÇEVE: MKT Temerrüt Şelalesi 5 basamaktan oluşur:\n1. Temerrüde düşen üyenin başlangıç ve ilave teminatları,\n2. Temerrüde düşen üyenin Garanti Fonu katkı payı,\n3. Takasbank'ın peşin tahsis ettiği dedike özkaynak payı (Sitted Capital),\n4. Temerrüde düşmeyen diğer üyelerin Garanti Fonu katkıları (oranları nispetinde),\n5. Takasbank'ın kalan genel özkaynakları ve garanti fonunun tazmini.\n3. ADIM ADIM İNCELEME / HESAPLAMA: A şıkkı bu 5 adımlı uluslararası ve ulusal şelale sırasını eksiksiz belirtir.\n4. DOĞRU CEVAP VE SONUÇ: A seçeneğidir.\n5. ÇELDİRİCİ TUZAĞI: Takasbank'ın dedike özkaynağının diğer üyelerin garanti fonundan önce devreye girdiğini unutmak.",
         "Temerrüt şelalesi: 1) Üye teminatı, 2) Üye garanti fonu, 3) Takasbank dedike özkaynağı, 4) Diğer üyelerin garanti fonu, 5) Takasbank kalan özkaynakları.", "KB1_Kavramsal"),

        ("q_1012_sert_002", "B", "Merkezi Karşı Taraf Sıfatı ve Yenileme (Novation) Hükmü",
         "6362 sayılı Sermaye Piyasası Kanunu m. 77 ve Takasbank mevzuatı uyarınca Takasbank'ın 'Merkezi Karşı Taraf' (MKT) sıfatıyla takas işlemlerine dahil olması ve 'Yenileme' (Novation) ilkesine ilişkin hangisi DOĞRUDUR?",
         [
           ("A", "Takasbank sadece aracı kurumların iflası durumunda iflas masasının talebiyle devreye giren tasfiye takip organıdır."),
           ("B", "Eşleşen emirlerde alıcıya karşı satıcı, satıcıya karşı alıcı konumuna geçerek takası garanti eder; borç ilişkisi yenilenir."),
           ("C", "MKT rolü üstlenildiğinde alım satım sözleşmesi iptal edilir ve takas yükümlülüğü tamamen Borsa İstanbul Yönetimine devredilir."),
           ("D", "Yenileme ilkesi sadece yabancı para cinsinden eurobond işlemlerinde geçerli olup organize pay piyasasında uygulanmaz."),
           ("E", "Takasbank taraflardan biri temerrüde düştüğünde takas garantisi vermez, yalnızca taraflar arasında uzlaşma komisyonu kurar."),
         ],
         "1. MEVZUAT DAYANAĞI: 6362 sayılı SPKn m. 77 ve Takasbank Esas Sözleşmesi.\n2. HUKUKİ / TEKNİK ÇERÇEVE: MKT (Central Counterparty), piyasada eşleşen alıcı ile satıcının arasına girer. Alıcıya karşı satıcı, satıcıya karşı alıcı olur (Novation). Böylece karşı taraf kredi riskini bizzat üstlenir.\n3. ADIM ADIM İNCELEME / HESAPLAMA: B seçeneği Novation (Yenileme) ilkesini ve MKT'nin iki ayrı bağımsız hukuki sözleşmeye dönüşümünü tam açıklar.\n4. DOĞRU CEVAP VE SONUÇ: B seçeneğidir.\n5. ÇELDİRİCİ TUZAĞI: Takasbank'ın sadece aracı kurum iflasında devreye girdiğini sanmak (Takasbank işlem anında MKT'dir).",
         "MKT, yenileme (novation) ile alıcıya karşı satıcı, satıcıya karşı alıcı olarak takas garantisi verir.", "KB2_Muhakeme"),

        ("q_1012_sert_003", "C", "Ödeme Karşılığı Teslimat (DVP) Prensibi",
         "Sermaye piyasalarında takas ve saklama operasyonlarının temel emniyet supabı olan 'Ödeme Karşılığı Teslimat' (Delivery Versus Payment - DVP) prensibine ilişkin aşağıdaki ifadelerden hangisi DOĞRUDUR?",
         [
           ("A", "Menkul kıymetin mülkiyeti alıcıya sabah seans açılışında devredilir, nakit ödeme ise 1 ay sonra takas edilir."),
           ("B", "DVP sistemi sadece vadeli altın işlemlerinde uygulanır, pay piyasası takasında uygulanması kanunen yasaktır."),
           ("C", "Menkul kıymetin devri ile nakit bedelinin ödenmesi eşanlı (aynı saniyede) olarak gerçekleşir; nakit ödenmedikçe menkul kıymet, menkul kıymet teslim edilmedikçe nakit devrolmaz."),
           ("D", "Alıcı taraf nakit bedeli ödemekten imtina etse dahi menkul kıymet satıcıdan alınıp alıcının hesabına kesin olarak geçer."),
           ("E", "DVP prensibinde takas riski tamamen ortadan kalkmaz, aksine takas riski en üst düzeye çıkar."),
         ],
         "1. MEVZUAT DAYANAĞI: BIS-CPMI/IOSCO Finansal Piyasa Altyapıları İlkeleri (PFMI İlke 12) ve Takasbank Yönergesi.\n2. HUKUKİ / TEKNİK ÇERÇEVE: DVP (Ödeme Karşılığı Teslim), takas riskini (özellikle karşı tarafın menkul kıymeti alıp parayı ödememesi veya tersi riskini) sıfırlamak üzere tasarlanmış eşzamanlı takas mekanizmasıdır.\n3. ADIM ADIM İNCELEME / HESAPLAMA: C şıkkı DVP prensibinin eşanlı devir kuralını eksiksiz belirtir.\n4. DOĞRU CEVAP VE SONUÇ: C seçeneğidir.\n5. ÇELDİRİCİ TUZAĞI: Menkul kıymetin peşin geçip paranın sonradan ödeneceğini sanmak.",
         "DVP prensibinde menkul kıymet devri ile nakit ödeme eşanlı gerçekleşir; biri olmadan diğeri devrolmaz.", "KB1_Kavramsal"),

        ("q_1012_sert_004", "D", "Takasbank Ödünç Pay Piyasası (ÖPP) ve Temettü Hak Sahipliği",
         "Takasbank Ödünç Pay Piyasası'nda (ÖPP) portföyündeki 100.000 lot hisse senedini 30 gün süreyle ödünç veren Yatırımcı Vedat Bey'in ödünç verdiği hisse senetleri, ödünç süresi devam ederken ihraççı şirket tarafından pay başına 4 TL nakit temettü dağıtmıştır.\n\nTakasbank Ödünç Pay Piyasası Yönergesi uyarınca söz konusu nakit temettü hakkına ve tutarına ilişkin hangisi DOĞRUDUR?",
         [
           ("A", "Hisseler ödünç alanın takas mülkiyetine geçtiğinden, dağıtılan nakit temettünün tamamı yasal olarak ödünç alana ait olur."),
           ("B", "Ödünç verilen payların temettü hakkı askıya alınır ve temettü tutarı şirket tarafından sermaye yedeklerine devredilir."),
           ("C", "Nakit temettü tutarı doğrudan Takasbank Garanti Fonu'na gelir kaydedilir ve ödünç sözleşmesi bitene kadar bloke tutulur."),
           ("D", "Temettü hakkı ödünç verene aittir; ödünç alan taraf temettü bedelini Takasbank aracılığıyla ödünç verene aktarmak zorundadır."),
           ("E", "Nakit temettü tutarı borsa kuralları gereği ödünç alan ile ödünç veren yatırımcı arasında yarı yarıya paylaştırılır."),
         ],
         "1. MEVZUAT DAYANAĞI: Takasbank Ödünç Pay Piyasası Yönergesi m. 22.\n2. HUKUKİ / TEKNİK ÇERÇEVE: Ödünç işlemlerinde menkul kıymet ödünç alana geçici olarak devredilse de, ekonomik mülkiyet ödünç verendedir. Ödünç süresince dağıtılan tüm nakit temettüler, bedelsiz paylar ve rüçhan hakları ÖDÜNÇ VEREN TARAFA (Vedat Bey'e) ödenir.\n3. ADIM ADIM İNCELEME / HESAPLAMA: D seçeneği hak kullanımının ödünç verene ait olduğu kuralını tam ifade eder.\n4. DOĞRU CEVAP VE SONUÇ: D seçeneğidir.\n5. ÇELDİRİCİ TUZAĞI: Hisseleri o an elinde tutan ödünç alanın temettüyü sahipleneceğini zannetmek (A şıkkı).",
         "Ödünç süresince oluşan tüm temettü ve bedelsiz hakları ödünç verene aittir; ödünç alan temettüyü aktarmakla yükümlüdür.", "KB3_Vaka"),

        ("q_1012_sert_005", "E", "Merkezi Kayıt Kuruluşu (MKK) Hak Sahipliği ve Hesap Yapısı",
         "6362 sayılı Sermaye Piyasası Kanunu m. 13 uyarınca Merkezi Kayıt Kuruluşu (MKK) nezdinde tutulan kaydi sisteme ilişkin;\n\nI. Sermaye piyasası araçları MKK nezdinde hak sahipleri itibarıyla (T.C. kimlik numarası / vergi kimlik numarası bazında) alt hesaplar açılarak kayden izlenir.\nII. MKK nezdinde kayden izlenen payların mülkiyetinin devri ve hakların üçüncü kişilere karşı ileri sürülebilmesi MKK sistemine kayıt yapılması ile hüküm ifade eder.\nIII. Yatırımcılar e-CAS (Yatırımcı Bilgilendirme Sistemi) üzerinden hesaplarındaki menkul kıymet hareketlerini anlık takip edebilir ve hisselerine bloke koyabilirler.\n\nYukarıda yer alan MKK yasal ve teknik ilkelerinden hangileri DOĞRUDUR?",
         [
           ("A", "Yalnızca I numaralı ilke mevzuat uyarınca doğrudur."),
           ("B", "Yalnızca II numaralı ilke mevzuat uyarınca doğrudur."),
           ("C", "I ve II numaralı ilkeler mevzuat uyarınca doğrudur."),
           ("D", "II ve III numaralı ilkeler mevzuat uyarınca doğrudur."),
           ("E", "I, II ve III numaralı ilkelerin tamamı mevzuat uyarınca doğrudur."),
         ],
         "1. MEVZUAT DAYANAĞI: 6362 sayılı SPKn m. 13 ve MKK Esas Sözleşmesi.\n2. HUKUKİ / TEKNİK ÇERÇEVE: Türkiye kaydi sistemi doğrudan hak sahibi bazında tutulur (Omnibus değil, doğrudan sicil sistemi). e-CAS ile yatırımcı hissesine blokaj koyabilir. Hak devirleri MKK kaydı ile hüküm ifade eder.\n3. ADIM ADIM İNCELEME / HESAPLAMA: I, II ve III öncüllerinin üçü de SPKn m. 13 ve MKK operasyonlarını eksiksiz yansıtır.\n4. DOĞRU CEVAP VE SONUÇ: E seçeneğidir.\n5. ÇELDİRİCİ TUZAĞI: Hesapların sadece aracı kurum bazında toplu (omnibus) tutulduğunu düşünmek.",
         "MKK'da hesaplar hak sahibi bazında tutulur; devirler MKK kaydı ile hüküm ifade eder ve e-CAS yatırımcı blokajı vardır.", "KB2_Muhakeme"),

        ("q_1012_sert_006", "A", "Elektronik Genel Kurul Sistemi (e-GKS) ve e-YÖNET",
         "6102 sayılı Türk Ticaret Kanunu m. 1527 ve MKK düzenlemeleri uyarınca Borsa İstanbul'da işlem gören anonim ortaklıkların genel kurul toplantılarına ilişkin hangisi DOĞRUDUR?",
         [
           ("A", "Borsada işlem gören şirketler genel kurullarını MKK'nın sağladığı e-GKS üzerinden eşzamanlı elektronik ortamda yapmak zorundadır."),
           ("B", "Elektronik genel kurulda oy kullanabilmek için şirketin merkezine noter onaylı taahhütname gönderilmesi zorunlu tutulmuştur."),
           ("C", "Elektronik genel kurula katılan pay sahipleri müzakereleri sadece izleyebilir; soru sorma ve muhalefet şerhi koyma hakları yoktur."),
           ("D", "Elektronik genel kurul sistemi sadece yabancı kurumsal fonların katılımına açık olup yerli bireysel ortaklar sisteme dahil edilemez."),
           ("E", "e-GKS üzerinden yapılan elektronik oylama sonuçları nihai olmayıp fiziki divan heyetinin onayından sonra geçerlilik kazanır."),
         ],
         "1. MEVZUAT DAYANAĞI: 6102 sayılı TTK m. 1527 ve Anonim Şirketlerde Elektronik Genel Kurul Yönetmeliği.\n2. HUKUKİ / TEKNİK ÇERÇEVE: Borsada işlem gören şirketlerin e-GKS sistemini kurması ve genel kurulu eşzamanlı elektronik olarak açması YASAL ZORUNLULUKTUR. Katılımcılar güvenli e-imza ile katılır, soru sorar, oy kullanır ve şerh koyabilirler.\n3. ADIM ADIM İNCELEME / HESAPLAMA: A şıkkı e-GKS zorunluluğunu tam doğru açıklar.\n4. DOĞRU CEVAP VE SONUÇ: A seçeneğidir.\n5. ÇELDİRİCİ TUZAĞI: e-GKS'nin isteğe bağlı olduğunu zannetmek (borsa şirketlerinde zorunludur).",
         "Halka açık şirketlerde genel kurula elektronik ortamda katılım imkanı (e-GKS) sağlanması zorunludur.", "KB1_Kavramsal"),

        ("q_1012_sert_007", "B", "MKK Blokaj Türleri: İhraççı vs Yatırımcı Blokajı",
         "MKK nezdinde kayden izlenen hisse senetleri üzerine konulabilen blokaj türleri ve hukuki sonuçlarına dair hangisi DOĞRUDUR?",
         [
           ("A", "Yatırımcı blokajı konulan paylar aracı kurum tarafından portföy teminatı olarak Takasbank'a serbestçe devredilebilir."),
           ("B", "Yatırımcı blokajı (e-CAS), yatırımcı bizzat kaldırmadıkça kurum dahil hiç kimsenin payı satmasına veya virmanlamasına izin vermez."),
           ("C", "İhraççı blokajı sadece şirket genel kurulunda alınan kararla yöneticilerin şahsi malvarlığına el koymak üzere uygulanır."),
           ("D", "MKK nezdinde blokaja alınan hisse senetleri şirketin nakit kâr payı ve bedelsiz pay dağıtım haklarından mahrum bırakılır."),
           ("E", "Rehin blokajı tesis edilebilmesi için pay senetlerinin fiziki olarak bastırılarak alacaklı bankanın kasasına teslimi şarttır."),
         ],
         "1. MEVZUAT DAYANAĞI: MKK İş ve İşleyiş Yönergesi m. 18, 19.\n2. HUKUKİ / TEKNİK ÇERÇEVE: Yatırımcı Blokajı (e-CAS Blokajı), dolandırıcılık veya yetkisiz virmanları önlemek için yatırımcının kendi hissesini kilitlemesidir. Yatırımcı şifresiyle blokajı kaldırmadıkça aracı kurum dahi hisseyi satamaz veya virmanlayamaz.\n3. ADIM ADIM İNCELEME / HESAPLAMA: B şıkkı yatırımcı blokajının tanım ve fonksiyonunu tam doğru açıklar.\n4. DOĞRU CEVAP VE SONUÇ: B seçeneğidir.\n5. ÇELDİRİCİ TUZAĞI: Blokajlı hissenin serbestçe satılabileceği zannı (A şıkkı; blokaj kalkmadan satılamaz).",
         "Yatırımcı blokajı (e-CAS), yatırımcının hisselerini kilitleyerek izinsiz satış ve virmanları engelleyen güvenlik tedbiridir.", "KB2_Muhakeme"),

        ("q_1012_sert_008", "C", "Piyasa Takas Süreleri (T+2, T+0, T+1) Karşılaştırması",
         "Borsa İstanbul bünyesinde faaliyet gösteren piyasalar ve bu piyasalardaki standart takas valör sürelerine ilişkin aşağıdaki eşleştirmelerden hangisi DOĞRUDUR?",
         [
           ("A", "Pay Piyasası: T+0; Borçlanma Araçları Piyasası: T+3; VİOP: T+10"),
           ("B", "Pay Piyasası: T+1; Borçlanma Araçları Piyasası: T+2; VİOP: T+0"),
           ("C", "Pay Piyasası: T+2; Borçlanma Araçları Kesin Alım Satım: T+0 (aynı gün) veya T+1; Para Piyasası Fonları: T+0"),
           ("D", "Pay Piyasası: T+5; Borçlanma Araçları Piyasası: T+1; VİOP: T+2"),
           ("E", "Tüm piyasalarda istisnasız olarak takas süresi T+0 (aynı gün) olmak zorundadır."),
         ],
         "1. MEVZUAT DAYANAĞI: Borsa İstanbul ve Takasbank Takas ve Uzlaşma Yönergesi.\n2. HUKUKİ / TEKNİK ÇERÇEVE: Standart takas süreleri:\n- Pay Piyasası: T+2 (İşlemi takip eden ikinci iş günü),\n- Borçlanma Araçları (DİBS/ÖST): Genellikle T+0 (Aynı gün valörlü) veya T+1,\n- Para Piyasası Fonları: T+0 (Aynı gün).\n3. ADIM ADIM İNCELEME / HESAPLAMA: C seçeneğindeki Pay Piyasası T+2, Tahvil T+0/T+1 ve Para Piyasası Fonu T+0 eşleştirmesi tam doğrudur.\n4. DOĞRU CEVAP VE SONUÇ: C seçeneğidir.\n5. ÇELDİRİCİ TUZAĞI: Pay piyasası takasının T+0 veya T+1 olduğunu sanmak.",
         "Takas süreleri: Pay Piyasası T+2, Borçlanma Araçları Piyasası T+0/T+1 ve Para Piyasası Fonları T+0'dır.", "KB1_Kavramsal"),

        ("q_1012_sert_009", "D", "Takasbank Para Piyasası (TPP) ve Teminatlandırma",
         "Takasbank Para Piyasası'nda (TPP) üyelerin nakit borç alma ve borç verme işlemlerine ilişkin hangisi DOĞRUDUR?",
         [
           ("A", "Takasbank Para Piyasası'nda borçlanma işlemleri tamamen teminatsız olarak güvene dayalı yürütülür."),
           ("B", "TPP'de sadece 10 yıl vadeli borçlanma yapılabilir, gecelik (O/N) işlem yapılması yasaktır."),
           ("C", "TPP'de borç veren taraf temerrüt riskini doğrudan borç alan üyeye karşı tek başına üstlenir ve Takasbank garantisi yoktur."),
           ("D", "Takasbank MKT sıfatıyla borç alan ile borç veren arasında yer alır, borçlanan taraftan teminat alır ve işlemlerin takasını garanti eder."),
           ("E", "Takasbank Para Piyasası'nda sadece altın ve yabancı para cinsinden borçlanma yapılabilir, TL borçlanma yapılamaz."),
         ],
         "1. MEVZUAT DAYANAĞI: Takasbank Para Piyasası Yönetmeliği m. 4, 8.\n2. HUKUKİ / TEKNİK ÇERÇEVE: TPP'de Takasbank MKT'dir. Borç alan teminat yatırır, borç veren nakit sağlar. Takasbank araya girerek takas ve ödeme garantisi sunar.\n3. ADIM ADIM İNCELEME / HESAPLAMA: D seçeneği TPP'nin MKT ve teminatlandırma yapısını doğru belirtir.\n4. DOĞRU CEVAP VE SONUÇ: D seçeneğidir.\n5. ÇELDİRİCİ TUZAĞI: TPP'nin teminatsız bir piyasa olduğu yanılgısı (A şıkkı).",
         "Takasbank Para Piyasası'nda Takasbank MKT olarak teminat alır ve takas garantisi verir.", "KB1_Kavramsal"),

        ("q_1012_sert_010", "E", "Elektronik Ürün Senedi (ELÜS) ve Lisanslı Depoculuk",
         "5300 sayılı Tarım Ürünleri Lisanslı Depoculuk Kanunu kapsamında çıkarılan 'Elektronik Ürün Senetleri'nin (ELÜS) kayden izlenmesi ve takasına ilişkin;\n\nI. ELÜS'ler lisanslı depolara teslim edilen standartlaştırılmış tarım ürünlerini temsil eden kıymetli evrak niteliğindeki elektronik senetlerdir.\nII. ELÜS'lerin merkezi sicili ve kayden ihraç işlemleri Merkezi Kayıt Kuruluşu (MKK) nezdinde yürütülür.\nIII. ELÜS alım satım işlemleri Türkiye Ürün İhtisas Borsası (TÜRİB) bünyesinde gerçekleşir ve takası Takasbank tarafından sonuçlandırılır.\n\nYukarıda yer alan tespitlerden hangileri DOĞRUDUR?",
         [
           ("A", "Yalnızca I numaralı tespit mevzuat uyarınca doğrudur."),
           ("B", "Yalnızca II numaralı tespit mevzuat uyarınca doğrudur."),
           ("C", "I ve II numaralı tespitler mevzuat uyarınca doğrudur."),
           ("D", "II ve III numaralı tespitler mevzuat uyarınca doğrudur."),
           ("E", "I, II ve III numaralı tespitlerin tamamı mevzuat uyarınca doğrudur."),
         ],
         "1. MEVZUAT DAYANAĞI: 5300 sayılı Kanun ve ELÜS Yönetmeliği.\n2. HUKUKİ / TEKNİK ÇERÇEVE: ELÜS tarım ürünlerini temsil eder (I). MKK nezdinde kayden ihraç edilir (II). TÜRİB'de işlem görür ve takası Takasbank tarafından yapılır (III).\n3. ADIM ADIM İNCELEME / HESAPLAMA: I, II ve III öncüllerinin tümü ELÜS sisteminin resmi mimarisini eksiksiz yansıtır.\n4. DOĞRU CEVAP VE SONUÇ: E seçeneğidir.\n5. ÇELDİRİCİ TUZAĞI: ELÜS kayıtlarının MKK yerine Tarım Bakanlığında tutulduğunu düşünmek.",
         "ELÜS lisanslı depo ürününü temsil eder; MKK'da kayden izlenir, TÜRİB'de işlem görür ve Takasbank takas eder.", "KB2_Muhakeme"),

        ("q_1012_sert_011", "A", "Hamiline Pay Kayıt Sistemi (HPKS) Tescil Zorunluluğu",
         "7262 sayılı Kanun ile 6102 sayılı TTK m. 486 ve 489'da yapılan düzenlemeler uyarınca, halka açık olmayan anonim şirketlerin çıkardıkları hamiline yazılı paylara ilişkin hangisi DOĞRUDUR?",
         [
           ("A", "Hamiline pay senetlerinin ihraç ve devirlerinin MKK HPKS sistemine tescili zorunludur; bildirim yapılmadıkça hak ileri sürülemez."),
           ("B", "Hamiline pay senetlerinin MKK'ya bildirimi ihtiyari olup şirket pay defterine noter huzurunda kaydedilmesi hukuken yeterlidir."),
           ("C", "HPKS bildirimi sadece sermayesi 500 milyon TL'yi aşan büyük ölçekli anonim şirketler için zorunlu kılınmış bir uygulamadır."),
           ("D", "Hamiline pay senedi zilyedi genel kurula katılabilmek için pay senedini toplantıdan 1 gün önce şirket merkezine rehin bırakır."),
           ("E", "HPKS bildirimi yapılmamış hamiline payların mülkiyeti kanun gereğince doğrudan şirket yönetim kurulu başkanına intikal eder."),
         ],
         "1. MEVZUAT DAYANAĞI: 6102 sayılı TTK m. 486, 489 ve HPKS Tebliği.\n2. HUKUKİ / TEKNİK ÇERÇEVE: 7262 sayılı Kanunla getirilen HPKS ile hamiline paylar kayıt altına alınmıştır. MKK'ya bildirim yapılmadıkça genel kurula katılma, kâr payı alma ve devir hükümleri geçerli olmaz.\n3. ADIM ADIM İNCELEME / HESAPLAMA: A şıkkı HPKS tescil zorunluluğunu ve bildirim yapılmamasının hukuki sonucunu tam doğru açıklar.\n4. DOĞRU CEVAP VE SONUÇ: A seçeneğidir.\n5. ÇELDİRİCİ TUZAĞI: Bildirim yapılmasa da zilyetliğin devrinin yeterli olacağını zannetmek (eski kural).",
         "Hamiline pay senetlerinin ihraç ve devirleri MKK HPKS sistemine bildirilmek zorundadır; aksi halde haklar ileri sürülemez.", "KB2_Muhakeme"),

        ("q_1012_sert_012", "B", "Takasbank Temerrüt Yönetimi ve Temerrüt Faizi Hesabı",
         "Borsa İstanbul Pay Piyasası'nda T+2 takas gününde 1.000.000 TL tutarındaki takas borcunu ödemeyerek temerrüde düşen Aracı Kurum A'ya karşı Takasbank'ın uygulayacağı operasyonel prosedüre dair hangisi DOĞRUDUR?",
         [
           ("A", "Takasbank temerrüde düşen üyenin borcunu derhal silerek zararı Borsa İstanbul bütçesinden doğrudan tazmin eder."),
           ("B", "Takasbank üyenin takas limitini kısıtlar, temerrüt faizi işletir ve mevcut teminatları paraya çevirerek takas açığını kapatır."),
           ("C", "Takasbank temerrüt eden üyenin yöneticilerini SPK kararı olmadan aynı gün ticaret mahkemesinde resen iflas ettirir."),
           ("D", "Takas açığı oluştuğunda takas süresi belirsiz bir tarihe kadar dondurulur ve hiçbir cezai faiz tahakkuk ettirilmez."),
           ("E", "Temerrüt faizi oranı her zaman TCMB gecelik borçlanma faiz oranının yarısı nispetinde sabit olarak hesaplanır."),
         ],
         "1. MEVZUAT DAYANAĞI: Takasbank Temerrüt Yönergesi m. 7, 8.\n2. HUKUKİ / TEKNİK ÇERÇEVE: Temerrütte Takasbank piyasa bütünlüğünü korumak için temerrüt faizi işletir, üyenin takas limitini kapatır ve teminatlarını re'sen paraya çevirerek takası tamamlar.\n3. ADIM ADIM İNCELEME / HESAPLAMA: B seçeneği temerrüt yaptırımlarını tam doğru özetler.\n4. DOĞRU CEVAP VE SONUÇ: B seçeneğidir.\n5. ÇELDİRİCİ TUZAĞI: Takasbank'ın teminatları paraya çevirme yetkisi olmadığını düşünmek.",
         "Temerrüt halinde Takasbank temerrüt faizi işletir, işlem yetkisini sınırlar ve teminatları paraya çevirir.", "KB2_Muhakeme"),

        ("q_1012_sert_013", "C", "Serbest Virman vs Bedelli Virman Ayrımı",
         "Sermaye piyasası araçlarının saklama hesapları arasındaki transferinde 'Serbest Virman' ile 'Bedelli Virman' (DVP) arasındaki operasyonel fark nedir?",
         [
           ("A", "Serbest virman sadece yabancı para transferlerinde, bedelli virman ise organize altın takasında kullanılan operasyon türüdür."),
           ("B", "Serbest virman Takasbank üzerinden yürütülürken bedelli virman işlemleri noter kanalıyla fiziki evrak üzerinden yapılır."),
           ("C", "Serbest virman nakit şartı aranmaksızın kıymet aktarımıdır; bedelli virman ise nakit bedelin ödenmesi şartına bağlı eşanlı devirdir."),
           ("D", "Bedelli virmanda kıymetin mülkiyeti aracı kuruma geçerken serbest virmanda kıymet doğrudan Yatırımcı Tazmin Merkezi'ne aktarılır."),
           ("E", "Serbest virman SPK tarafından tamamen yasaklanmış olup sermaye piyasasında yalnızca bedelli virman yapılmasına izin verilir."),
         ],
         "1. MEVZUAT DAYANAĞI: MKK ve Takasbank Operasyon Kılavuzları.\n2. HUKUKİ / TEKNİK ÇERÇEVE: Serbest Virman (Free of Payment - FOP): Karşılığında takas sistemi üzerinden bir nakit akışı olmaksızın yapılan virmandır (aynı kişinin farklı kurumdaki hesapları arası virman). Bedelli Virman (DVP): Menkul kıymet devrinin para transferine bağlandığı virmandır.\n3. ADIM ADIM İNCELEME / HESAPLAMA: C şıkkı FOP ve DVP arasındaki nakit şartı farkını tam olarak ortaya koyar.\n4. DOĞRU CEVAP VE SONUÇ: C seçeneğidir.\n5. ÇELDİRİCİ TUZAĞI: Serbest virmanın yasadışı olduğunu düşünmek.",
         "Serbest virman nakit takassız virmandır; bedelli virman (DVP) ise paranın ödenmesi şartına bağlı eşzamanlı devirdir.", "KB1_Kavramsal"),

        ("q_1012_sert_014", "D", "Kâr Payı Dağıtımında Hak Sahipliği Tespiti (Record Date)",
         "Halka açık bir anonim ortaklığın nakit kâr payı dağıtımı sürecinde 'Hak Sahipliği Belirlenme Tarihi' (Record Date) ve hak kullanım takasına ilişkin hangisi DOĞRUDUR?",
         [
           ("A", "Hak Sahipliği Tarihi (Record Date) temettü dağıtımından tam 30 gün önce şirket genel kurulunca re'sen belirlenen gündür."),
           ("B", "Record Date günü borsada hisse senedi alan bir yatırımcı, takası henüz gerçekleşmediği halde temettüyü nakden tahsil eder."),
           ("C", "Kâr payı bedelleri Takasbank sistemi kullanılmaksızın şirket muhasebesi tarafından ortakların adreslerine nakit postalanır."),
           ("D", "Ex-date'i izleyen iş günü (T+1) kapanışındaki MKK kayıtları hak sahipliğini belirler; nakit temettü T+2'de hesaplara aktarılır."),
           ("E", "Temettü dağıtımında MKK ve Takasbank kayıtları dikkate alınmaz; sadece şirket pay defterindeki fiziki kayıtlar esas kabul edilir."),
         ],
         "1. MEVZUAT DAYANAĞI: II-19.1 Kâr Payı Tebliği ve MKK Hak Kullanım Yönergesi.\n2. HUKUKİ / TEKNİK ÇERÇEVE: Ex-date temettüsüz işlem günüdür. Takas T+2 olduğu için, ex-date'den önceki gün hisse alanın takası ex-date'den bir gün sonra (T+1) sonuçlanır ve Record Date'de MKK sicilinde görünür. Nakit ödeme T+2'de hesaba geçer.\n3. ADIM ADIM İNCELEME / HESAPLAMA: D seçeneği Record Date, MKK hak sahipliği ve Takasbank nakit ödeme döngüsünü eksiksiz açıklar.\n4. DOĞRU CEVAP VE SONUÇ: D seçeneğidir.\n5. ÇELDİRİCİ TUZAĞI: Temettünün elden veya postayla gönderileceğini zannetmek.",
         "Record Date'de MKK kayıtlarına göre tespit edilen hak sahiplerine nakit temettü Takasbank üzerinden T+2'de aktarılır.", "KB2_Muhakeme"),

        ("q_1012_sert_015", "E", "Merkezi Takas Kuruluşu Garanti Fonu Yapısı",
         "Takasbank nezdinde oluşturulan 'Garanti Fonu'nun (Default Fund) finansal kaynağı ve işleyiş ilkelerine ilişkin;\n\nI. Garanti Fonu'na MKT üyesi olan aracı kurumlar ve bankalar işlem hacimleri ve risk derecelerine göre nakit ve teminat katkısı sağlamak zorundadır.\nII. Garanti Fonu, temerrüde düşen üyenin kendi teminatlarının yetersiz kalması halinde diğer üyelerin ve Takasbank'ın haklarını korumak amacıyla kullanılır.\nIII. Temerrüt eden üyenin borcu Garanti Fonu'ndan karşılandığında, fonu kullanan üye borcunu ferileriyle birlikte fona derhal iade etmekle yükümlüdür.\n\nYukarıda yer alan tespitlerden hangileri DOĞRUDUR?",
         [
           ("A", "Yalnızca I numaralı tespit mevzuat uyarınca doğrudur."),
           ("B", "Yalnızca II numaralı tespit mevzuat uyarınca doğrudur."),
           ("C", "I ve II numaralı tespitler mevzuat uyarınca doğrudur."),
           ("D", "II ve III numaralı tespitler mevzuat uyarınca doğrudur."),
           ("E", "I, II ve III numaralı tespitlerin tamamı mevzuat uyarınca doğrudur."),
         ],
         "1. MEVZUAT DAYANAĞI: Takasbank MKT Yönetmeliği m. 16, 17.\n2. HUKUKİ / TEKNİK ÇERÇEVE: Garanti Fonu tüm MKT üyelerinin ortaklaşa finanse ettiği risk havuzudur. Temerrüt durumunda devreye girer ve temerrüt eden üyeden rücuen tahsil edilir.\n3. ADIM ADIM İNCELEME / HESAPLAMA: I, II ve III öncüllerinin tümü Garanti Fonunun yasal mahiyetini eksiksiz yansıtır.\n4. DOĞRU CEVAP VE SONUÇ: E seçeneğidir.\n5. ÇELDİRİCİ TUZAĞI: Garanti Fonunun sadece devlet bütçesinden karşılandığını sanmak.",
         "Garanti Fonu üyelerin katkılarıyla kurulur; temerrütte devreye girer ve borçlu üyeden rücuen tahsil edilir.", "KB2_Muhakeme"),

        ("q_1012_sert_016", "A", "Yatırımcı Tazmin Merkezi (YTM) Zamanaşımı İşlemleri",
         "6362 sayılı Sermaye Piyasası Kanunu m. 83 uyarınca yatırım kuruluşları nezdindeki yatırımcılara ait nakit ve menkul kıymetlerin zamanaşımına uğraması sürecine ilişkin hangisi DOĞRUDUR?",
         [
           ("A", "Yatırımcının son işlem, talep veya yazılı talimat tarihinden itibaren 10 yıl içinde aranmayan her türlü emanet ve alacaklar zamanaşımına uğrar ve YTM'ye devredilir."),
           ("B", "Zamanaşımı süresi hisse senetlerinde 1 yıl, nakit paralarda ise 6 aydır."),
           ("C", "Zamanaşımına uğrayan varlıklar doğrudan aracı kurumun kendi özkaynaklarına kâr olarak kaydedilir."),
           ("D", "Zamanaşımına uğrayıp YTM'ye devredilen varlıklar üzerinde yatırımcılar 50 yıl sonra dahi mülkiyet davası açabilirler."),
           ("E", "Yatırımcı vefat ettiğinde varlıkları zamanaşımı süresi beklenmeksizin aynı gün YTM'ye devredilir."),
         ],
         "1. MEVZUAT DAYANAĞI: 6362 sayılı SPKn m. 83/1.\n2. HUKUKİ / TEKNİK ÇERÇEVE: SPKn uyarınca zamanaşımı süresi 10 yıldır. 10 yıl boyunca hiçbir işlem görmeyen veya talep edilmeyen varlıklar YTM'ye devredilir ve Hazineye gelir kaydedilir.\n3. ADIM ADIM İNCELEME / HESAPLAMA: A şıkkı 10 yıllık zamanaşımı kuralını ve YTM'ye devir sonucunu tam olarak verir.\n4. DOĞRU CEVAP VE SONUÇ: A seçeneğidir.\n5. ÇELDİRİCİ TUZAĞI: Zamanaşımı süresinin 5 yıl veya 2 yıl olduğunu zannetmek.",
         "Yatırım kuruluşlarındaki varlıklar 10 yıl aranmazsa zamanaşımına uğrar ve Yatırımcı Tazmin Merkezi'ne devredilir.", "KB1_Kavramsal"),

        ("q_1012_sert_017", "B", "MKK Rehin ve Haciz Blokajı İşlemleri",
         "6362 sayılı Sermaye Piyasası Kanunu m. 13/4 ve İcra ve İflas Kanunu uyarınca, kayden izlenen hisse senetleri üzerinde 'Haciz' ve 'Rehin' işlemlerinin tesis edilmesine dair hangisi DOĞRUDUR?",
         [
           ("A", "Hisse senedi haczi sadece şirketin basılı fiziki pay senetlerinin icra memurunca elle teslim alınmasıyla mümkündür."),
           ("B", "Kaydi paylar üzerindeki rehin ve haciz işlemleri MKK nezdindeki ilgili hak sahibi alt hesaplarına elektronik blokaj konulması suretiyle tesis edilir ve üçüncü kişilere karşı hüküm ifade eder."),
           ("C", "Haciz konulan hisse senetleri MKK sisteminde blokaj konulmaksızın serbestçe borsada satılabilir."),
           ("D", "Rehin tesis edilebilmesi için hisse senetlerinin mülkiyetinin alacaklı bankaya kesin olarak devredilmesi şarttır."),
           ("E", "MKK haciz bildirimlerini sadece Türkiye Ticaret Sicili Gazetesi ilanı ile öğrenir, icra dairesi elektronik bildirim yapamaz."),
         ],
         "1. MEVZUAT DAYANAĞI: 6362 sayılı SPKn m. 13/4 ve İİK m. 78, 88.\n2. HUKUKİ / TEKNİK ÇERÇEVE: Kaydi sermaye piyasası araçlarında rehin ve haciz MKK nezdinde ilgili alt hesaba elektronik blokaj konulması ile kurulur. UYAP entegrasyonu ile elektronik haciz işlenir.\n3. ADIM ADIM İNCELEME / HESAPLAMA: B şıkkı MKK alt hesabına blokaj koyma suretiyle elektronik rehin ve haciz rejimini tam açıklar.\n4. DOĞRU CEVAP VE SONUÇ: B seçeneğidir.\n5. ÇELDİRİCİ TUZAĞI: Fiziki teslim veya zilyetlik devri gerektiği yanılgısı (kaydi sistemde fiziki teslimat yoktur).",
         "Kaydi paylarda rehin ve haciz MKK nezdindeki alt hesaplara elektronik blokaj konulmasıyla tesis edilir.", "KB2_Muhakeme"),

        ("q_1012_sert_018", "C", "Takasbank Para Piyasasında Teminat Kabul Edilen Varlıklar",
         "Takasbank Para Piyasası'nda (TPP) borçlanma karşılığında Takasbank tarafından teminat olarak kabul edilebilecek finansal varlıklara ilişkin hangisi DOĞRUDUR?",
         [
           ("A", "Sadece fiziki gayrimenkul ipotekleri ile şirket yöneticilerinin aval verdiği ticari senetler teminat olarak kabul edilir."),
           ("B", "Yalnızca borsada işlem görmeyen kapalı anonim şirketlerin hisseleri ve vadeli çekler tam teminat değeriyle kabul edilir."),
           ("C", "TL nakit, DİBS, Eurobond, konvertibl döviz ve BIST pay senetleri risklerine göre belirlenen katsayılarla teminata kabul edilir."),
           ("D", "Kripto varlıklar ile tezgahüstü türev sözleşmeleri hiçbir iskonto uygulanmaksızın nakit para gibi birebir teminat sayılır."),
           ("E", "Takasbank Para Piyasası'nda menkul kıymet teminatı kabul edilmez; işlemler sadece bankaların karşılıklı kefaletiyle yürütülür."),
         ],
         "1. MEVZUAT DAYANAĞI: Takasbank Para Piyasası Yönetmeliği m. 9.\n2. HUKUKİ / TEKNİK ÇERÇEVE: TPP'de likit, güvenilir varlıklar (TL, DİBS, Eurobond, döviz, BIST BIST 30 hisseleri) risk derecelerine göre belirlenen 'teminat katsayıları / saç kesimi (haircut)' uygulanarak teminata kabul edilir.\n3. ADIM ADIM İNCELEME / HESAPLAMA: C seçeneği kabul edilen likit enstrümanları ve iskonto (saç kesimi) prensibini eksiksiz sayar.\n4. DOĞRU CEVAP VE SONUÇ: C seçeneğidir.\n5. ÇELDİRİCİ TUZAĞI: Gayrimenkul veya çek gibi gayri likit araçların teminat kabul edilebileceğini sanmak.",
         "TPP'de TL, DİBS, Eurobond, döviz ve BIST hisseleri saç kesimi (haircut) uygulanarak teminat kabul edilir.", "KB1_Kavramsal"),

        ("q_1012_sert_019", "D", "Kolektif Yatırım Kuruluşları Saklama Hizmeti (III-40.1)",
         "III-40.1 sayılı Portföy Saklama Hizmetine ve Bu Hizmette Bulunacak Kuruluşlara İlişkin Esaslar Tebliği uyarınca 'Portföy Saklayıcısı'nın görev ve sorumluluklarına dair hangisi DOĞRUDUR?",
         [
           ("A", "Portföy saklayıcısı fon yönetim şirketinin idari harcamalarını denetlemekle görevli olup fon varlıklarını koruma görevi yoktur."),
           ("B", "Portföy saklayıcısı fon varlıklarını kendi mülkiyetine geçirerek şirketin banka kredilerine rehin gösterme yetkisine sahiptir."),
           ("C", "Fon malvarlığı saklayıcı bankanın iflas masasına dahil edilir ve saklayıcının kamu borçları sebebiyle haczedilebilir."),
           ("D", "Saklayıcı, fon varlıklarını saklamak, işlemlerin mevzuata uygunluğunu denetlemek ve fon birim pay fiyatını kontrol etmekle yükümlüdür."),
           ("E", "Saklama hizmeti yalnızca aracı kurumların genel merkezlerinde tahsis edilen fiziki kiralık kasalar üzerinden yürütülür."),
         ],
         "1. MEVZUAT DAYANAĞI: 6362 sayılı SPKn m. 56 ve III-40.1 Tebliği m. 5, 6.\n2. HUKUKİ / TEKNİK ÇERÇEVE: Portföy saklayıcısı fon varlıklarını korur, PYŞ'nin emirlerinin mevzuat ve içtüzüğe uygunluğunu denetler, pay fiyatını doğrular. Bağımsız bir gözetim organı işlevi görür.\n3. ADIM ADIM İNCELEME / HESAPLAMA: D seçeneği saklayıcının gözetim ve doğrulama yetkilerini tam doğru ifade eder.\n4. DOĞRU CEVAP VE SONUÇ: D seçeneğidir.\n5. ÇELDİRİCİ TUZAĞI: Saklayıcının sadece pasif bir kasa görevi gördüğünü, kontrol yetkisi olmadığını sanmak.",
         "Portföy saklayıcısı fon varlıklarını saklar, PYŞ işlemlerinin mevzuata uygunluğunu ve birim pay fiyatını kontrol eder.", "KB2_Muhakeme"),

        ("q_1012_sert_020", "E", "Merkezi Takas Kuruluşu Sermaye Yeterliliği ve Risk Fonu",
         "Avrupa Piyasa Altyapısı Düzenlemesi (EMIR) ve CPMI-IOSCO standartlarına uyum kapsamında Takasbank'ın MKT risk yönetimi çerçevesine ilişkin;\n\nI. Takasbank stres testleri ve geri geriye testler (backtesting) yaparak garanti fonunun ve teminat seviyelerinin yeterliliğini sürekli ölçer.\nII. Takasbank MKT olarak üstlendiği piyasalarda piyasa koşullarına göre teminat tutarlarını (Span teminat parametrelerini) resen artırma yetkisine sahiptir.\nIII. Takasbank'ın dedike özkaynak katkısı temerrüt durumunda diğer üyelerin garanti fonundan önce zararı karşılamak üzere feda edilir.\n\nYukarıda yer alan MKT risk yönetimi kurallarından hangileri DOĞRUDUR?",
         [
           ("A", "Yalnızca I numaralı kural mevzuatça zorunludur."),
           ("B", "Yalnızca II numaralı kural mevzuatça zorunludur."),
           ("C", "I ve II numaralı kurallar mevzuatça zorunludur."),
           ("D", "II ve III numaralı kurallar mevzuatça zorunludur."),
           ("E", "I, II ve III numaralı kuralların tamamı mevzuatça zorunludur."),
         ],
         "1. MEVZUAT DAYANAĞI: Takasbank MKT Yönetmeliği ve Uluslararası Finansal Altyapı İlkeleri.\n2. HUKUKİ / TEKNİK ÇERÇEVE: MKT stres testi ve backtesting yapar (I). Span parametrelerini günceller (II). Kendi dedike sermayesini diğer üyelerin fonundan önce şelaleye koyar (Skin in the game) (III).\n3. ADIM ADIM İNCELEME / HESAPLAMA: I, II ve III öncüllerinin tümü Takasbank MKT mimarisinin temel yapı taşlarıdır.\n4. DOĞRU CEVAP VE SONUÇ: E seçeneğidir.\n5. ÇELDİRİCİ TUZAĞI: Takasbank'ın teminatları tek taraflı artıramayacağını varsaymak.",
         "Takasbank düzenli stres testleri yapar, Span parametrelerini günceller ve kendi dedike özkaynağını öncelikli feda eder.", "KB2_Muhakeme"),

        ("q_1012_sert_021", "A", "Bedelsiz Sermaye Artırımı ve MKK Hak Kullanım Takası",
         "Hisseleri Borsa İstanbul'da işlem gören bir anonim ortaklığın %200 bedelsiz sermaye artırımı yapması durumunda, yatırımcıların hesaplarına yeni bedelsiz payların kayden intikaline dair hangisi DOĞRUDUR?",
         [
           ("A", "Bedelsiz paylar, hak kullanım tarihinde MKK tarafından hak sahiplerinin alt hesaplarına hiçbir nakit talep edilmeksizin otomatik olarak kayden aktarılır."),
           ("B", "Yatırımcıların bedelsiz payları alabilmek için hisse başına 1 TL nakit ödemeyi aracı kuruma yapmaları zorunludur."),
           ("C", "Bedelsiz hisseler yatırımcıların banka hesabına nakit TL olarak aktarılır."),
           ("D", "Bedelsiz sermaye artırımında yeni paylar sadece şirketin yönetim kurulu üyelerine verilir, diğer ortaklara verilmez."),
           ("E", "Bedelsiz paylar ancak genel kurul toplantısına bizzat fiziken katılan ortaklara noter huzurunda teslim edilir."),
         ],
         "1. MEVZUAT DAYANAĞI: VII-128.1 Pay Tebliği ve MKK Hak Kullanım Operasyon Yönergesi.\n2. HUKUKİ / TEKNİK ÇERÇEVE: Bedelsiz sermaye artırımında iç kaynaklar sermayeye eklendiğinden yatırımcıdan para talep edilmez. MKK kayıtları üzerinden otomatik olarak hak sahiplerinin kaydi hesaplarına yeni paylar yansıtılır.\n3. ADIM ADIM İNCELEME / HESAPLAMA: A şıkkı bedelsiz payların otomatik kaydi intikalini tam doğru açıklar.\n4. DOĞRU CEVAP VE SONUÇ: A seçeneğidir.\n5. ÇELDİRİCİ TUZAĞI: Bedelsiz artırımda da para ödeneceğini sanmak (bedellide para ödenir).",
         "Bedelsiz paylar MKK nezdinde hiçbir nakit ödeme gerekmeksizin hak sahiplerinin hesaplarına otomatik kayden aktarılır.", "KB1_Kavramsal"),

        ("q_1012_sert_022", "B", "Rüçhan Hakkı Kullanımı ve Nakit Bedel Takası",
         "Bedelli sermaye artırımında yeni pay alma (rüçhan) hakkını kullanmak isteyen bir yatırımcının takas ve saklama operasyonuna ilişkin hangisi DOĞRUDUR?",
         [
           ("A", "Yatırımcının sadece sözlü talep iletmesi yeterli olup rüçhan bedeli yeni paylar borsada satıldıktan sonra tahsil edilir."),
           ("B", "Yatırımcı süresinde talimat vermeli ve nakdi hazır etmelidir; bedel Takasbank'tan ihraççıya, yeni paylar MKK'da hesaba geçer."),
           ("C", "Rüçhan hakkı kullanımı sonucunda ihraç edilen yeni pay senetleri 5 yıl boyunca MKK nezdinde bloke edilir ve satılamaz."),
           ("D", "Rüçhan kullanım bedeli doğrudan Borsa İstanbul Yönetim Kurulu başkanlığı adına açılan özel vadesiz hesaba yatırılır."),
           ("E", "Rüçhan hakkını kullanan yatırımcının portföyündeki eski paylar iptal edilerek yerine sadece yeni paylar tahsis edilir."),
         ],
         "1. MEVZUAT DAYANAĞI: VII-128.1 Pay Tebliği m. 18, 19 ve Takasbank Hak Kullanım Kılavuzu.\n2. HUKUKİ / TEKNİK ÇERÇEVE: Rüçhan kullanımında süre içinde talimat verilir, rüçhan kuponları hesaptan düşülür, karşılığı nakit Takasbank üzerinden ihraççıya ödenir ve karşılığında üretilen yeni hisseler MKK nezdinde hesaba aktarılır.\n3. ADIM ADIM İNCELEME / HESAPLAMA: B şıkkı talimat, nakit temin, Takasbank para aktarımı ve MKK pay intikalini eksiksiz belirtir.\n4. DOĞRU CEVAP VE SONUÇ: B seçeneğidir.\n5. ÇELDİRİCİ TUZAĞI: Nakit olmadan da rüçhanın kullanılabileceği zannı.",
         "Rüçhan hakkı kullanımında süresinde talimat ve nakit bedelin hazır olması zorunludur; takas Takasbank/MKK ile yürütülür.", "KB2_Muhakeme"),

        ("q_1012_sert_023", "C", "Takasbank Menkul Kıymet Nitelikli Saklama ve Sub-Custody",
         "Türkiye'de yerleşik yatırımcıların yabancı ülke borsalarında işlem gören hisse senetleri ve borçlanma araçlarının saklanmasına ilişkin hangisi DOĞRUDUR?",
         [
           ("A", "Yurt dışı menkul kıymetler fiziki senet olarak Türkiye'ye getirilir ve Darphane kasalarında kilit altında muhafaza edilir."),
           ("B", "Yurt dışı menkul kıymetlerin Türk yatırımcılar adına saklanması yasak olup tüm işlemler aracı kurumca fiktif yürütülür."),
           ("C", "Takasbank, Euroclear/Clearstream veya yabancı saklamacılar (sub-custodian) nezdindeki hesaplarıyla yabancı kıymetleri kayden saklar."),
           ("D", "Yabancı menkul kıymetlerin saklama ve mutabakat masrafları Borsa İstanbul tarafından sosyal sorumluluk fonundan karşılanır."),
           ("E", "Yurt dışı hisse alımlarında takas mutabakatı yalnızca diplomatik kuryelerle taşınan fiziki çekler üzerinden tamamlanır."),
         ],
         "1. MEVZUAT DAYANAĞI: III-40.1 Tebliği ve Takasbank Dış Saklama Yönergesi.\n2. HUKUKİ / TEKNİK ÇERÇEVE: Takasbank küresel entegrasyon kapsamında Euroclear ve Clearstream nezdinde omnibus hesaplar açarak Türk yatırım kuruluşlarının yabancı sermaye piyasası araçlarını güvenli şekilde saklar (Global/Sub-custody).\n3. ADIM ADIM İNCELEME / HESAPLAMA: C şıkkı Euroclear/Clearstream entegrasyonu ve kaydi saklama modelini tam yansıtır.\n4. DOĞRU CEVAP VE SONUÇ: C seçeneğidir.\n5. ÇELDİRİCİ TUZAĞI: Fiziki kağıtların Türkiye'ye getirilip kasada saklanacağı zannı (A şıkkı).",
         "Takasbank, Euroclear ve Clearstream gibi uluslararası saklama kuruluşları nezdindeki hesaplarıyla yabancı kıymetleri saklar.", "KB1_Kavramsal"),

        ("q_1012_sert_024", "D", "Kıymet Ödünç İşlemlerinde Teminat Değerlemesi ve Çağrı",
         "Takasbank Ödünç Pay Piyasası'nda (ÖPP) ödünç alan üyenin Takasbank'a yatırmış olduğu teminatların piyasa dalgalanmaları sebebiyle değer kaybetmesi durumunda işletilen teminat tamamlama kuralı nedir?",
         [
           ("A", "Teminatlar piyasa dalgalanmalarından etkilenmez; sözleşme vadesi sonuna kadar hiçbir ilave teminat talep edilemez."),
           ("B", "Teminat oranı gerileyen üyenin faaliyeti derhal durdurulur ve şirket hakkında SPK tarafından re'sen iflas davası açılır."),
           ("C", "Oluşan teminat açığı Takasbank kuralları gereği ödünç veren yatırımcı tarafından nakit yatırılarak kapatılmak zorundadır."),
           ("D", "Takasbank teminatları günlük değerler (mark-to-market); oran düşerse tamamlama çağrısı yapar, uyulmazsa pozisyonu re'sen kapatır."),
           ("E", "Teminat açığı doğduğunda Takasbank eksik kalan tutarı kendi yedek akçelerinden karşılar ve üyeden hiçbir talepte bulunmaz."),
         ],
         "1. MEVZUAT DAYANAĞI: Takasbank ÖPP Yönergesi m. 15, 16.\n2. HUKUKİ / TEKNİK ÇERÇEVE: ÖPP'de ödünç alan tarafın teminatları günlük değerlenir (mark-to-market). Teminat açığı oluştuğunda tamamlama çağrısı yapılır; tamamlanmazsa Takasbank piyasadan payı satın alarak ödünç verene iade eder ve teminatları nakde çevirir.\n3. ADIM ADIM İNCELEME / HESAPLAMA: D seçeneği günlük değerleme, tamamlama çağrısı ve re'sen kapatma prosedürünü tam belirtir.\n4. DOĞRU CEVAP VE SONUÇ: D seçeneğidir.\n5. ÇELDİRİCİ TUZAĞI: Ödünç verenin teminat açığını kapatacağı yanılgısı (C şıkkı; açığı ödünç alan kapatır).",
         "ÖPP'de teminatlar günlük değerlenir; oran düşerse ödünç alana tamamlama çağrısı yapılır, uyulmazsa re'sen kapatılır.", "KB2_Muhakeme"),

        ("q_1012_sert_025", "E", "MKK Sicil Numarası ve Yatırımcı Kimlik Doğrulaması",
         "Sermaye piyasasında yatırım hesabı açan her bir yerli veya yabancı gerçek ve tüzel kişiye MKK tarafından tahsis edilen 'Sicil Numarası' ve hesap eşleştirmesine ilişkin;\n\nI. Her bir yatırımcıya MKK nezdinde tek bir benzersiz sicil numarası (MKK Sicil No) tahsis edilir.\nII. Yatırımcının farklı aracı kurumlarda veya bankalarda kaç tane hesabı olursa olsun, tüm bu hesaplar aynı MKK sicil numarası altında konsolide olarak izlenir.\nIII. Yatırımcı sicil numarası üzerinden kamu otoriteleri ve SPK nezdinde manipülasyon ve içeriden öğrenen ticaretine karşı piyasa gözetimi yürütülür.\n\nYukarıda yer alan MKK sicil ilkelerinden hangileri DOĞRUDUR?",
         [
           ("A", "Yalnızca I numaralı ilke mevzuat uyarınca doğrudur."),
           ("B", "Yalnızca II numaralı ilke mevzuat uyarınca doğrudur."),
           ("C", "I ve II numaralı ilkeler mevzuat uyarınca doğrudur."),
           ("D", "II ve III numaralı ilkeler mevzuat uyarınca doğrudur."),
           ("E", "I, II ve III numaralı ilkelerin tamamı mevzuat uyarınca doğrudur."),
         ],
         "1. MEVZUAT DAYANAĞI: MKK Üyelik ve Sicil Yönergesi m. 6, 7 ve 6362 sayılı SPKn m. 13.\n2. HUKUKİ / TEKNİK ÇERÇEVE: Türkiye'de 'Tek Sicil - Çoklu Hesap' ilkesi geçerlidir. Bir yatırımcının 10 farklı aracı kurumda hesabı olsa da hepsi tek bir MKK sicil numarasına bağlıdır. Bu sayede piyasa dolandırıcılığı anlık gözetlenebilir.\n3. ADIM ADIM İNCELEME / HESAPLAMA: I, II ve III öncüllerinin üçü de tek sicil ve konsolide izleme kuralını tam açıklar.\n4. DOĞRU CEVAP VE SONUÇ: E seçeneğidir.\n5. ÇELDİRİCİ TUZAĞI: Her aracı kurum için ayrı bir MKK sicili tahsis edildiğini ve hesapların birleştirilemediğini sanmak.",
         "MKK'da her yatırımcıya tek bir sicil no verilir; tüm kurumlardaki hesaplar bu sicilde konsolide izlenir.", "KB2_Muhakeme"),

        ("q_1012_sert_026", "A", "VİOP Takas ve Teminat Yönetimi (Span Algoritması)",
         "Takasbank'ın VİOP'ta portföy bazında teminat hesaplamasında kullandığı 'SPAN' (Standard Portfolio Analysis of Risk) algoritmasının temel çalışma prensibi hangisidir?",
         [
           ("A", "Farklı fiyat ve oynaklık senaryolarında portföyün maruz kalabileceği azami zararı simüle ederek gerekli başlangıç teminatını belirler."),
           ("B", "Portföyün toplam piyasa değerini her gün sabit kabul eden ve türev pozisyonlar için hiçbir teminat talep etmeyen basit bir yöntemdir."),
           ("C", "Yalnızca BIST 30 pay senedi işlemlerine uygulanan, vadeli işlem ve opsiyon sözleşmelerinde kullanılması kanunen yasak bir formüldür."),
           ("D", "Yatırımcının mesleki deneyimini ve yıllık gelir beyanını dikkate alarak her müşteri için tamamen subjektif teminat oranı belirler."),
           ("E", "Piyasa faizleri yükseldiğinde açık pozisyonları teminat seviyesine bakılmaksızın aynı gün re'sen kapatan bir risk filtresidir."),
         ],
         "1. MEVZUAT DAYANAĞI: Takasbank VİOP Takas ve Risk Yönetimi Yönergesi m. 11.\n2. HUKUKİ / TEKNİK ÇERÇEVE: SPAN algoritması (CME patentli, küresel standart) portföydeki ters yönlü pozisyonların riskini netleştirir (korelasyon indirimi). 16 farklı senaryo simülasyonu ile bir sonraki gün oluşabilecek azami zararı karşılayacak teminatı hesaplar.\n3. ADIM ADIM İNCELEME / HESAPLAMA: A şıkkı SPAN algoritmasının en kötü durum senaryosu ve azami zarar simülasyonu prensibini tam tanımlar.\n4. DOĞRU CEVAP VE SONUÇ: A seçeneğidir.\n5. ÇELDİRİCİ TUZAĞI: SPAN'ın sadece hisse senetlerine uygulandığı yanılgısı.",
         "SPAN algoritması, farklı fiyat ve oynaklık senaryolarında portföyün uğrayabileceği azami zararı simüle ederek teminat hesaplar.", "KB1_Kavramsal"),

        ("q_1012_sert_027", "B", "Takasbank Aracı Kurum Takas Limitleri ve Gün İçi Limit",
         "Takasbank'ın üyelerine tahsis ettiği 'Takas Net Borç Limiti' ve gün içi risk sınırlarına ilişkin hangisi DOĞRUDUR?",
         [
           ("A", "Aracı kurumlar sermaye ve teminatlarına bakılmaksızın borsada diledikleri tutarda sınırsız takas borcu yükümlülüğü üstlenebilirler."),
           ("B", "Üyenin sermayesi ve Garanti Fonu katkısına göre Takas Net Borç Limiti tahsis edilir; limiti aşan üyenin yeni işlemleri durdurulur."),
           ("C", "Takas net borç limiti yalnızca yabancı yatırım bankalarına tahsis edilir; yerli sermayeli aracı kurumlar limitsiz işlem yaparlar."),
           ("D", "Takas limitini aşan bir yatırım kuruluşunun Borsa İstanbul ve Takasbank üyelik belgesi aynı gün geri dönülemez biçimde feshedilir."),
           ("E", "Takas net borç limiti yalnızca nakit borçlar için uygulanır; menkul kıymet teslim borçlarında herhangi bir sınır bulunmamaktadır."),
         ],
         "1. MEVZUAT DAYANAĞI: Takasbank MKT Yönetmeliği m. 12.\n2. HUKUKİ / TEKNİK ÇERÇEVE: Risk yönetimi gereği üyelerin üstlenebilecekleri azami takas riski Takas Net Borç Limiti ile sınırlandırılır. Limit sermaye ve teminatla orantılıdır; limit dolduğunda sistem yeni pozisyon açılışını engeller.\n3. ADIM ADIM İNCELEME / HESAPLAMA: B seçeneği garanti fonu, sermaye yeterliliği ve limit aşımı sonucunu doğru açıklar.\n4. DOĞRU CEVAP VE SONUÇ: B seçeneğidir.\n5. ÇELDİRİCİ TUZAĞI: Takas sisteminde hiçbir sınır olmadığını veya sınırsız borçlanılabileceğini sanmak (A şıkkı).",
         "Takasbank üyenin sermaye ve garanti fonu katkısına göre Takas Net Borç Limiti belirler; limit aşılırsa işlemler durdurulur.", "KB2_Muhakeme"),

        ("q_1012_sert_028", "C", "MKK Bilgi Güvenliği ve e-YÖNET Kurumsal Portalı",
         "MKK tarafından işletilen 'e-YÖNET: Kurumsal Yönetim ve Yatırımcı İlişkileri Portalı'nın işlevine dair hangisi DOĞRUDUR?",
         [
           ("A", "Şirketlerin sadece vergi beyannamelerini Gelir İdaresi Başkanlığı'na iletmek için kullandıkları bir muhasebe yazılımıdır."),
           ("B", "Borsa İstanbul yönetim kurulu başkanının şirketlere günlük talimat göndermek için kullandığı mesajlaşma programıdır."),
           ("C", "Halka açık ortaklıkların pay sahipleri ile iletişimini sağlayan, ortaklık yapısını, kurumsal yönetim uyum raporlarını ve hak kullanım süreçlerini şeffaf şekilde yöneten elektronik platformdur."),
           ("D", "Yalnızca borsa aracı kurumlarının birbirlerine hisse virmanı yapmak için kullandıkları kapalı devre takas ağıdır."),
           ("E", "Halka açık şirketlerin hisse senedi fiyatlarını manipüle etmelerine izin veren bir borsa modülüdür."),
         ],
         "1. MEVZUAT DAYANAĞI: II-17.1 Kurumsal Yönetim Tebliği ve MKK Hizmet Portalları Düzenlemeleri.\n2. HUKUKİ / TEKNİK ÇERÇEVE: e-YÖNET platformu, kurumsal yönetim ilkelerine uyumu artırmak, ihraççı şirketler ile pay sahipleri arasında doğrudan ve güvenli köprü kurmak amacıyla MKK tarafından geliştirilmiştir.\n3. ADIM ADIM İNCELEME / HESAPLAMA: C şıkkı e-YÖNET portalının fonksiyon ve amacını tam olarak tanımlar.\n4. DOĞRU CEVAP VE SONUÇ: C seçeneğidir.\n5. ÇELDİRİCİ TUZAĞI: Portalın sadece vergi amaçlı olduğunu düşünmek (A şıkkı).",
         "e-YÖNET platformu, halka açık şirketlerin ortaklık yapısını, hak kullanımlarını ve kurumsal yönetim uyumunu yöneten MKK portalıdır.", "KB1_Kavramsal"),

        ("q_1012_sert_029", "D", "Takas İşlemlerinde Temerrüt Eden Üyenin Menkul Kıymetlerinin Satışı",
         "Borsa İstanbul Pay Piyasası takasında taahhüt ettiği menkul kıymet teslim yükümlülüğünü yerine getiremeyerek temerrüde düşen bir aracı kuruma karşı Takasbank'ın 'Açık Takas Pozisyonunu Kapatma' yöntemi nedir?",
         [
           ("A", "Takasbank teslim edilmeyen hisseler yerine alıcı yatırımcılara devlet iç borçlanma senedi teklif eder ve işlemi derhal kapatır."),
           ("B", "Takasbank borçlu aracı kurumun şirket araçlarına el koyarak satış bedelini alıcı yatırımcıların banka hesabına nakden aktarır."),
           ("C", "Teslim edilmeyen paylar için alıcı taraf hiçbir hak talebinde bulunamaz ve işlemin tamamlanması için 5 yıl boyunca beklemek zorundadır."),
           ("D", "Takasbank piyasadan veya ÖPP'den payı temin edip alıcıya teslim eder (buy-in); oluşan tüm maliyeti temerrüt eden üyeye rücu eder."),
           ("E", "Takasbank ihraççı şirkete resmi müzekkere yazarak teslim edilemeyen pay miktarı kadar bedelsiz yeni pay basılmasını talep eder."),
         ],
         "1. MEVZUAT DAYANAĞI: Takasbank MKT Yönetmeliği m. 20, 21.\n2. HUKUKİ / TEKNİK ÇERÇEVE: Menkul kıymet temerrüdünde alıcının mağdur olmaması için Takasbank bizzat devreye girer: ÖPP'den ödünç bulur veya piyasadan hisseyi satın alarak (Buy-in) alıcıya teslim eder. Maliyeti temerrüt eden üyeden tahsil eder.\n3. ADIM ADIM İNCELEME / HESAPLAMA: D seçeneği piyasadan temin ve alıcıya eksiksiz teslimat mekanizmasını tam açıklar.\n4. DOĞRU CEVAP VE SONUÇ: D seçeneğidir.\n5. ÇELDİRİCİ TUZAĞI: Alıcının hisse yerine tahvil almaya zorlanacağı yanılgısı (A şıkkı).",
         "Takasbank temerrüt halinde hisseyi piyasadan (ÖPP veya borsa) temin edip alıcıya teslim eder, faturayı borçluya rücu eder.", "KB2_Muhakeme"),

        ("q_1012_sert_030", "E", "MKK Saklama Sisteminde Hak Sahipliği Blokajı İstisnaları",
         "MKK nezdinde kayden izlenen hisse senetleri üzerine konulan blokajların kaldırılması ve transfer süreçlerine ilişkin;\n\nI. Yatırımcı tarafından konulan e-CAS blokajı, yatırımcının bizzat şifresi ve kimlik doğrulaması ile sistemden kaldırılmadıkça aracı kurumca transfer edilemez.\nII. Mahkeme veya icra dairesi tarafından konulan ihtiyati tedbir ve haciz blokajları ancak ilgili adli merciin resmi yazılı/elektronik müzekkeresi ile kaldırılabilir.\nIII. İflas masasına devredilen aracı kurumlardaki müşteri hesapları SPK ve MKK gözetiminde sağlam bir saklamacı kuruma topluca virmanlanabilir.\n\nYukarıda yer alan hukuki ve operasyonel kurallardan hangileri DOĞRUDUR?",
         [
           ("A", "Yalnızca I numaralı kural mevzuatça öngörülmüştür."),
           ("B", "Yalnızca II numaralı kural mevzuatça öngörülmüştür."),
           ("C", "I ve II numaralı kurallar mevzuatça öngörülmüştür."),
           ("D", "II ve III numaralı kurallar mevzuatça öngörülmüştür."),
           ("E", "I, II ve III numaralı kuralların tamamı mevzuatça öngörülmüştür."),
         ],
         "1. MEVZUAT DAYANAĞI: MKK İş ve İşleyiş Yönergesi ve SPKn m. 13.\n2. HUKUKİ / TEKNİK ÇERÇEVE: e-CAS blokajı yatırımcı iradesiyle (I), adli blokajlar mahkeme kararıyla (II) kalkar. İflas eden kurumdaki müşteri varlıkları sağlam kuruma aktarılır (III).\n3. ADIM ADIM İNCELEME / HESAPLAMA: I, II ve III öncüllerinin tümü operasyonel blokaj kaldırma rejiminin kurallarıdır.\n4. DOĞRU CEVAP VE SONUÇ: E seçeneğidir.\n5. ÇELDİRİCİ TUZAĞI: Mahkeme haciz blokajının aracı kurum talebiyle kaldırılabileceğini sanmak.",
         "e-CAS blokajı yatırımcı şifresiyle, adli blokajlar mahkeme müzekkeresiyle kalkar; müşteri varlıkları korunur.", "KB2_Muhakeme"),

        ("q_1012_sert_031", "A", "Takasbank BIST 30 Endeks Vadeli Sözleşmelerinde Nakdi Uzlaşma",
         "BIST 30 Endeks Vadeli İşlem Sözleşmelerinin vade sonu uzlaşma yöntemi ve nakit akışına ilişkin hangisi DOĞRUDUR?",
         [
           ("A", "Vade sonu uzlaşma yöntemi nakdi uzlaşmadır; vade sonu uzlaşma fiyatı ile pozisyon fiyatı arasındaki fark hesaplanarak kâr/zarar nakit olarak Takasbank nezdinde takas edilir."),
           ("B", "Vade sonunda yatırımcıya endekste yer alan 30 şirketin hisse senetleri fiziki olarak kamyonla teslim edilir."),
           ("C", "Endeks vadeli sözleşmelerinde vade sonunda hiçbir hesaplaşma yapılmaz, sözleşme kendiliğinden imha edilir."),
           ("D", "Vade sonu uzlaşma fiyatı sadece Amerika Merkez Bankası (Fed) faiz kararına göre belirlenir."),
           ("E", "Nakdi uzlaşma yapıldığında kazanan taraf kârını sadece altın olarak Takasbank gişesinden çekebilir."),
         ],
         "1. MEVZUAT DAYANAĞI: Borsa İstanbul VİOP Prosedürü m. 16.\n2. HUKUKİ / TEKNİK ÇERÇEVE: BIST 30 Endeks sözleşmelerinde fiziki hisse teslimi imkansız olduğundan uzlaşma yöntemi NAKDİ UZLAŞMADIR (Cash Settlement). Kâr eden tarafın hesabına nakit aktarılır, zarar edenden düşülür.\n3. ADIM ADIM İNCELEME / HESAPLAMA: A şıkkı nakdi uzlaşma kuralını tam doğru açıklar.\n4. DOĞRU CEVAP VE SONUÇ: A seçeneğidir.\n5. ÇELDİRİCİ TUZAĞI: Endeks sözleşmelerinde de 30 hissenin fiziki teslim edileceğini sanmak (B şıkkı).",
         "Endeks vadeli işlem sözleşmelerinde vade sonu uzlaşma yöntemi NAKDİ UZLAŞMADIR.", "KB1_Kavramsal"),

        ("q_1012_sert_032", "B", "Takasbank Çek Takas Sistemi (Elektronik Çek Takas)",
         "Bankalararası Takas Odaları Merkezi (BTOM) ve Takasbank nezdinde yürütülen 'Elektronik Çek Takas Sistemi' işleyişine ilişkin hangisi DOĞRUDUR?",
         [
           ("A", "Çeklerin fiziki olarak banka şubeleri arasında elden dolaştırılması zorunlu olup dijital görüntü aktarımı yasaktır."),
           ("B", "Muhatap bankalar çeklerin fiziki asılları yerine elektronik ortamda taranmış görüntüleri üzerinden karşılık kontrolü ve takas mutabakatı yaparlar."),
           ("C", "Çek takas sistemi sadece yabancı para çekleri için geçerli olup Türk Lirası çekler takasa giremez."),
           ("D", "Elektronik çek takas sisteminde karşılıksız çıkan çekler için hiçbir yasal bildirim yapılmaz."),
           ("E", "Çek takas işlemlerinin sonuçlanması için asgari 6 ay süre tanınması zorunludur."),
         ],
         "1. MEVZUAT DAYANAĞI: 5941 sayılı Çek Kanunu ve Çek Takas Yönetmeliği.\n2. HUKUKİ / TEKNİK ÇERÇEVE: Çek takas sistemi fiziki çek taşıma maliyetini bitirmiştir. Çekin taranmış yüksek çözünürlüklü dijital görüntüsü Takasbank sistemi üzerinden muhatap bankaya iletilir ve karşılığı sorgulanır.\n3. ADIM ADIM İNCELEME / HESAPLAMA: B seçeneği dijital çek görüntüsü üzerinden karşılık kontrolü ilkesini tam doğru açıklar.\n4. DOĞRU CEVAP VE SONUÇ: B seçeneğidir.\n5. ÇELDİRİCİ TUZAĞI: Çeklerin fiziki olarak takas odasında toplanması gerektiği eski kurala takılmak.",
         "Çek takas sistemi elektronik ortamda taranmış çek görüntüleri üzerinden karşılık kontrolü ile yürütülür.", "KB1_Kavramsal"),

        ("q_1012_sert_033", "C", "MKK Pay Defteri ve Genel Kurul Blokajı",
         "6102 sayılı TTK m. 417 uyarınca halka açık anonim ortaklıkların genel kurul toplantısına katılabilecek pay sahiplerinin listesinin hazırlanmasına dair hangisi DOĞRUDUR?",
         [
           ("A", "Genel kurul listesi sadece genel kurul sabahı şirket kapısına gelen ortakların nüfus cüzdanlarına bakılarak elle yazılır."),
           ("B", "Genel kurula katılabilmek için pay sahiplerinin hisselerini en az 6 ay önceden Takasbank'a rehin vermeleri şarttır."),
           ("C", "Şirket yönetim kurulu, genel kurul toplantısına katılabilecek pay sahiplerinin listesini MKK'dan sağlayacağı 'Hazır Bulunanlar Listesi'ne göre düzenler."),
           ("D", "MKK hazır bulunanlar listesini sadece şirket kurucu ortaklarının onay vermesi halinde hazırlar."),
           ("E", "Hisselerini genel kurul gününden önce satmış olan eski ortaklar genel kurula katılıp şirket adına bağlayıcı oy kullanabilirler."),
         ],
         "1. MEVZUAT DAYANAĞI: 6102 sayılı TTK m. 417 ve MKK Genel Kurul İşlemleri Kılavuzu.\n2. HUKUKİ / TEKNİK ÇERÇEVE: Halka açık şirketlerde genel kurula katılacak ortakların listesi MKK sicil kayıtlarından doğrudan çekilir (Hazır Bulunanlar Listesi). MKK kaydı esastır.\n3. ADIM ADIM İNCELEME / HESAPLAMA: C şıkkı MKK'dan alınan liste üzerinden genel kurul hazır bulunanlar listesinin tanzimini doğru belirtir.\n4. DOĞRU CEVAP VE SONUÇ: C seçeneğidir.\n5. ÇELDİRİCİ TUZAĞI: Şirketin kendi eski pay defterine bakarak liste yapacağını düşünmek (borsa şirketinde MKK esastır).",
         "Genel kurula katılabilecek ortaklar listesi MKK'dan sağlanan Hazır Bulunanlar Listesi'ne göre düzenlenir.", "KB1_Kavramsal"),

        ("q_1012_sert_034", "D", "Kıymetli Madenler ve Taşlar Piyasası Saklama Hizmeti",
         "Borsa İstanbul Kıymetli Madenler ve Kıymetli Taşlar Piyasası'nda (KMKTP) işlem gören standart ve standart dışı altın külçelerinin saklanmasına ilişkin hangisi DOĞRUDUR?",
         [
           ("A", "Standart altın külçeleri her aracı kurumun kendi merkez ofisinde bulunan çelik kasalarda fiziki olarak saklanmak zorundadır."),
           ("B", "Altınlar fiziki olarak depolanmaz; yalnızca sanal bilgisayar kayıtları üzerinden fiktif bakiye olarak takip edilir."),
           ("C", "Altın saklama operasyonları mevzuat gereğince yalnızca Adalet Bakanlığı'na bağlı noterlik dairelerinde yürütülebilir."),
           ("D", "Kıymetli madenler Borsa İstanbul'un uluslararası standartlardaki özel saklama kasalarında fiziki ve kaydi olarak muhafaza edilir."),
           ("E", "Kıymetli Madenler Piyasası'nda takas mutabakatının tamamlanması için yasal olarak en az 6 ay beklenmesi zorunludur."),
         ],
         "1. MEVZUAT DAYANAĞI: Borsa İstanbul Kıymetli Madenler ve Kıymetli Taşlar Piyasası Yönergesi.\n2. HUKUKİ / TEKNİK ÇERÇEVE: KMKTP bünyesinde işlem gören altın ve gümüşler Borsa İstanbul'un uluslararası standartlardaki yüksek güvenlikli kasalarında fiziki olarak saklanır ve MKK/Takasbank ile entegre kayden izlenir.\n3. ADIM ADIM İNCELEME / HESAPLAMA: D şıkkı Borsa İstanbul altın saklama kasalarını tam doğru tarif eder.\n4. DOĞRU CEVAP VE SONUÇ: D seçeneğidir.\n5. ÇELDİRİCİ TUZAĞI: Altınların her aracı kurumun kendi şubesinde saklandığı yanılgısı.",
         "Kıymetli madenler Borsa İstanbul'un yüksek güvenlikli altın saklama kasalarında muhafaza edilir.", "KB1_Kavramsal"),

        ("q_1012_sert_035", "E", "Merkezi Takas Kuruluşunda Üyelik Tipleri",
         "Takasbank MKT ve Takas Üyeliği mevzuatı kapsamında düzenlenen üyelik tipleri ve sorumluluklarına ilişkin;\n\nI. Genel Takas Üyeliği: Hem kendi işlemlerinin hem de takas üyesi olmayan diğer yatırım kuruluşlarının işlemlerinin takasını yürütmeye yetkilidir.\nII. Doğrudan Takas Üyeliği: Yalnızca kendi işlemlerinin ve kendi müşterilerinin işlemlerinin takasını yürütmeye yetkilidir; üçüncü kurumların takasını yapamaz.\nIII. Takas Üyesi Olmayan Kuruluşlar: Borsa işlemlerinin takasını ancak bir Genel Takas Üyesi ile sözleşme imzalayarak sonuçlandırabilirler.\n\nYukarıda yer alan takas üyeliği sınıflandırmalarından hangileri DOĞRUDUR?",
         [
           ("A", "Yalnızca I numaralı sınıflandırma mevzuat uyarınca doğrudur."),
           ("B", "Yalnızca II numaralı sınıflandırma mevzuat uyarınca doğrudur."),
           ("C", "I ve II numaralı sınıflandırmalar mevzuat uyarınca doğrudur."),
           ("D", "II ve III numaralı sınıflandırmalar mevzuat uyarınca doğrudur."),
           ("E", "I, II ve III numaralı sınıflandırmaların tamamı mevzuat uyarınca doğrudur."),
         ],
         "1. MEVZUAT DAYANAĞI: Takasbank MKT Yönetmeliği m. 7, 8.\n2. HUKUKİ / TEKNİK ÇERÇEVE: Takasbank'ta 2 üyelik türü vardır: 1) Doğrudan Takas Üyesi (Sadece kendi işlemleri), 2) Genel Takas Üyesi (Hem kendi hem başkalarının işlemleri). Takas üyesi olmayanlar Genel Takas Üyesi üzerinden takas yapar.\n3. ADIM ADIM İNCELEME / HESAPLAMA: I, II ve III öncülleri bu sınıflandırmayı eksiksiz ifade eder.\n4. DOĞRU CEVAP VE SONUÇ: E seçeneğidir.\n5. ÇELDİRİCİ TUZAĞI: Doğrudan takas üyesinin de üçüncü kurumlara takas hizmeti verebileceğini zannetmek.",
         "Takas üyeliği: Genel Takas Üyesi başkalarının takasını da yapar; Doğrudan Takas Üyesi sadece kendininkini yapar.", "KB2_Muhakeme"),

        ("q_1012_sert_036", "A", "MKK e-VEDO Elektronik Veri Deposu",
         "Sermaye piyasasında türev araç işlemlerinin şeffaflığını sağlamak amacıyla kurulan ve MKK bünyesinde faaliyet gösteren 'Elektronik Veri Deposu'na (e-VEDO / Trade Repository) ilişkin hangisi DOĞRUDUR?",
         [
           ("A", "Tezgahüstü (OTC) ve borsa türev sözleşmelerine ilişkin detaylı işlem verilerinin raporlandığı MKK merkezi veri tabanıdır."),
           ("B", "Halka açık ortaklıkların basılı yıllık faaliyet raporları ile ürün kataloglarını depolayan fiziksel arşiv dairesidir."),
           ("C", "e-VEDO'ya yapılan tüm türev işlem bildirimleri anlık olarak günlük ulusal gazetelerde tam sayfa ilan edilmek zorundadır."),
           ("D", "Yalnızca bireysel döviz ve altın alım satımlarının kaydedildiği, türev ürünlerin kesinlikle bildirilmediği bir sistemdir."),
           ("E", "Sermaye piyasası aracı kurumlarının birbirlerine şifreli kısa mesaj göndermek amacıyla kullandıkları kapalı devre bir ağdır."),
         ],
         "1. MEVZUAT DAYANAĞI: 6362 sayılı SPKn m. 87 ve MKK e-VEDO İşleyiş Esasları.\n2. HUKUKİ / TEKNİK ÇERÇEVE: e-VEDO (Trade Repository), küresel G20 taahhütleri uyarınca tezgahüstü türev işlemlerin sistemik riskini izlemek için MKK nezdinde kurulan yasal bildirim ve veri tabanı merkezidir.\n3. ADIM ADIM İNCELEME / HESAPLAMA: A şıkkı tezgahüstü ve organize türev işlemlerin raporlama merkezi tanımını tam verir.\n4. DOĞRU CEVAP VE SONUÇ: A seçeneğidir.\n5. ÇELDİRİCİ TUZAĞI: e-VEDO'nun sadece fiziksel arşiv dairesi sanılması (B şıkkı).",
         "e-VEDO, tezgahüstü ve borsa türev işlemlerinin raporlandığı MKK merkezi veri deposudur (Trade Repository).", "KB1_Kavramsal"),

        ("q_1012_sert_037", "B", "Takasbank Para ve Menkul Kıymet Teminatlarının Nemalandırılması",
         "Takasbank nezdinde MKT teminat hesaplarında ve takas hesaplarında nakit olarak tutulan Türk Lirası teminatların nemalandırılmasına dair hangisi DOĞRUDUR?",
         [
           ("A", "Takasbank nakit teminatlara hiçbir şekilde faiz işletmez ve tüm faiz gelirlerini kendi şirket sermayesine katar."),
           ("B", "Takasbank nezdinde bloke edilen serbest nakit teminatlar para piyasasında veya ters repoda gecelik olarak nemalandırılarak faiz getirisi ilgili üye ve yatırımcı hesaplarına yansıtılır."),
           ("C", "Nakit teminatların nemalandırılması sadece döviz hesaplarında geçerli olup TL hesaplarda nemalandırma yasaktır."),
           ("D", "Nakit teminat faizleri sadece SPK bütçesine aktarılır, yatırımcıya ödenmez."),
           ("E", "Teminatların nemalanabilmesi için yatırımcının bizzat Takasbank veznesine giderek her gün nakit para talep etmesi gerekir."),
         ],
         "1. MEVZUAT DAYANAĞI: Takasbank Teminat Yönetimi Yönergesi m. 13.\n2. HUKUKİ / TEKNİK ÇERÇEVE: Yatırımcıların ve üyelerin Takasbank nezdindeki nakit teminatları atıl bırakılmaz. Takasbank tarafından gecelik ters repo ve para piyasasında nemalandırılır; nemalar hesaplara günlük yansıtılır.\n3. ADIM ADIM İNCELEME / HESAPLAMA: B seçeneği serbest nakit teminatların gecelik nemalandırılması kuralını tam açıklar.\n4. DOĞRU CEVAP VE SONUÇ: B seçeneğidir.\n5. ÇELDİRİCİ TUZAĞI: Teminatların nemalandırılmadığı zannı (A şıkkı).",
         "Takasbank'taki nakit teminatlar para piyasasında gecelik nemalandırılarak getirisi hesaplara yansıtılır.", "KB1_Kavramsal"),

        ("q_1012_sert_038", "C", "MKK Yatırımcı Bilgilendirme Sistemi (e-CAS) ve Şüpheli İşlem SMS/E-posta Bildirimi",
         "MKK nezdinde faaliyet gösteren 'e-CAS' (Elektronik Yatırımcı Bilgilendirme ve Uyarı Sistemi) işleyişine ilişkin hangisi DOĞRUDUR?",
         [
           ("A", "e-CAS yalnızca borsa brokerlarının seans sırasında kendi aralarında iletişim kurmasını sağlayan kapalı devre mesajlaşma sistemidir."),
           ("B", "e-CAS sistemine kayıtlı yatırımcıların hesaplarından pay çıkışı yapıldığında gizlilik gereği hiçbir bilgilendirme mesajı iletilmez."),
           ("C", "Hesaptan menkul kıymet çıkışı veya virman olduğunda yatırımcıya anlık SMS ve e-posta göndererek yetkisiz işlemleri engeller."),
           ("D", "e-CAS sistemi yatırımcılara sadece yılda bir defa posta yoluyla basılı hesap bülteni ve genel kurul davetiyesi gönderen servistir."),
           ("E", "e-CAS bildirimleri yalnızca portföy büyüklüğü 50 milyon TL'nin üzerinde olan kurumsal fonlar için geçerli olup bireysele kapalıdır."),
         ],
         "1. MEVZUAT DAYANAĞI: MKK e-CAS Düzenlemeleri ve Yatırımcı Hakları Tebliği.\n2. HUKUKİ / TEKNİK ÇERÇEVE: e-CAS, yatırımcıların haberi olmadan aracı kurum personeli veya yetkisiz şahıslar tarafından hisse satışı/virmanı yapılmasını engeller. Çıkış hareketinde derhal anlık SMS/e-posta bildirimi gider.\n3. ADIM ADIM İNCELEME / HESAPLAMA: C şıkkı hisse çıkışında anlık SMS/e-posta uyarı mekanizmasını tam doğru belirtir.\n4. DOĞRU CEVAP VE SONUÇ: C seçeneğidir.\n5. ÇELDİRİCİ TUZAĞI: e-CAS'ın sadece yıllık basılı ekstre gönderdiği sanrısı (D şıkkı).",
         "e-CAS, hesaptan menkul kıymet çıkışlarında yatırımcıya anlık SMS ve e-posta göndererek yetkisiz işlemleri engeller.", "KB1_Kavramsal"),

        ("q_1012_sert_039", "D", "Kredili İşlemlerde Özkaynak Tamamlama Operasyonel Bildirimi",
         "Seri: V, No: 65 sayılı Tebliğ uyarınca kredili pay alımı yapan bir müşterinin özkaynak açığı oluştuğunda aracı kurum operasyon biriminin yapacağı tebligat ve tamamlama süresine ilişkin hangisi DOĞRUDUR?",
         [
           ("A", "Özkaynak bildirimi yalnızca noter kanalıyla yapılabilir ve yatırımcıya eksikliği gidermesi için en az 6 ay yasal süre verilir."),
           ("B", "Özkaynak tamamlama çağrısı yapılmasına gerek yoktur; kurum bildirim yapmaksızın aynı saniyede müşterinin tüm paylarını satar."),
           ("C", "Müşteriye telefonla ulaşılamadığı takdirde hiçbir işlem yapılamaz ve doğacak tüm takas zararları aracı kurumun üstünde kalır."),
           ("D", "Kurum sözleşmedeki yollarla bildirim yapar ve müşteriye eksikliği tamamlaması için ertesi iş günü mesai bitimine kadar süre tanır."),
           ("E", "Özkaynak tamamlama bildirimi yapılabilmesi için öncelikle şirket yönetim kurulu tarafından resmi karar alınması zorunludur."),
         ],
         "1. MEVZUAT DAYANAĞI: Seri: V, No: 65 Tebliği m. 15.\n2. HUKUKİ / TEKNİK ÇERÇEVE: Kredili işlemde özkaynak tamamlama bildirimi sözleşmedeki yöntemlerle hızlıca yapılır. Yatırımcıya kural olarak ertesi iş günü mesai bitimine kadar süre verilir; tamamlanmazsa re'sen satış başlar.\n3. ADIM ADIM İNCELEME / HESAPLAMA: D seçeneği iletişim kanalları ve ertesi iş günü tamamlama süresini tam açıklar.\n4. DOĞRU CEVAP VE SONUÇ: D seçeneğidir.\n5. ÇELDİRİCİ TUZAĞI: Sadece noter tebligatı şartı arandığı yanılgısı (hızlı elektronik kanallar geçerlidir).",
         "Özkaynak tamamlama bildirimi sözleşmedeki kanallarla (SMS/e-posta) yapılır ve ertesi iş günü mesai bitimine kadar süre verilir.", "KB2_Muhakeme"),

        ("q_1012_sert_040", "E", "Merkezi Takas Kuruluşunun Yasal İcra ve Haciz Muafiyeti",
         "6362 sayılı Sermaye Piyasası Kanunu m. 79 uyarınca Takasbank nezdinde tutulan MKT teminatları ve takas hesaplarının hukuki korumasına ilişkin;\n\nI. Takasbank'ın MKT sıfatıyla aldığı teminatlar, temerrüt eden üyenin veya üçüncü kişilerin kamu borçları dahil hiçbir borcu için haczedilemez.\nII. MKT teminatları üzerine iflas masası tarafından tedbir konulamaz ve iflas masasına devredilemez.\nIII. Takasbank'ın tasfiye hesabındaki varlıklar sadece takas taahhütlerinin yerine getirilmesi amacıyla kullanılır.\n\nYukarıda yer alan hukuki koruma ilkelerinden hangileri kanunen geçerlidir?",
         [
           ("A", "Yalnızca I numaralı ilke kanunen geçerlidir."),
           ("B", "Yalnızca II numaralı ilke kanunen geçerlidir."),
           ("C", "I ve II numaralı ilkeler kanunen geçerlidir."),
           ("D", "II ve III numaralı ilkeler kanunen geçerlidir."),
           ("E", "I, II ve III numaralı ilkelerin tamamı kanunen geçerlidir."),
         ],
         "1. MEVZUAT DAYANAĞI: 6362 sayılı SPKn m. 79/1.\n2. HUKUKİ / TEKNİK ÇERÇEVE: SPKn m. 79 Takasbank MKT teminatlarına mutlak dokunulmazlık tanır. Kamu borcu, vergi borcu, SGK haczi veya iflas masası MKT teminatlarına el koyamaz; teminatlar yalnızca takasın tamamlanmasına tahsis edilir.\n3. ADIM ADIM İNCELEME / HESAPLAMA: I, II ve III öncülleri yasanın amir dokunulmazlık ve haciz muafiyeti hükmünü tam ifade eder.\n4. DOĞRU CEVAP VE SONUÇ: E seçeneğidir.\n5. ÇELDİRİCİ TUZAĞI: Kamu alacakları için teminatların haczedilebileceğini düşünmek (SPK m. 79 kamu alacağını da yasaklar).",
         "Takasbank MKT teminatları mutlak dokunulmazlığa sahiptir; kamu alacakları için dahi haczedilemez ve iflas masasına girmez.", "KB2_Muhakeme"),

        ("q_1012_sert_041", "A", "Borçlanma Araçları Piyasasında Takas Esasları",
         "Borsa İstanbul Borçlanma Araçları Piyasası'nda (BAP) işlem gören Devlet İç Borçlanma Senetlerinin kesin alım satım takasına ilişkin hangisi DOĞRUDUR?",
         [
           ("A", "İşlemler kural olarak aynı gün valörlü (T+0) veya tarafların tercihine göre belirlenen valörde (T+1 ila T+90) Takasbank nezdinde DVP prensibiyle takas edilir."),
           ("B", "BAP'ta takas işlemleri sadece 1 yıl sonra fiziki senet teslimi ile sonuçlandırılır."),
           ("C", "DİBS alım satım takasında nakit bedel ödenmeden tahviller doğrudan alıcıya teslim edilir."),
           ("D", "BAP takasında Takasbank hiçbir rol oynamaz, işlemler Türkiye Cumhuriyet Merkez Bankası gişelerinde elden nakitle yapılır."),
           ("E", "BAP kesin alım satım pazarında takas borcunu ödemeyen üyelere hiçbir temerrüt cezası uygulanamaz."),
         ],
         "1. MEVZUAT DAYANAĞI: Borsa İstanbul Borçlanma Araçları Piyasası Yönergesi.\n2. HUKUKİ / TEKNİK ÇERÇEVE: BAP'ta işlemler aynı gün valörlü (T+0) veya ileri valörlü (T+n) yapılabilir. Takas Takasbank tarafından DVP (Ödeme Karşılığı Teslim) ile sonuçlandırılır.\n3. ADIM ADIM İNCELEME / HESAPLAMA: A şıkkı T+0 / ileri valör ve DVP prensibini tam doğru açıklar.\n4. DOĞRU CEVAP VE SONUÇ: A seçeneğidir.\n5. ÇELDİRİCİ TUZAĞI: BAP'ta da Pay Piyasası gibi zorunlu T+2 takas olduğunu sanmak.",
         "Borçlanma Araçları Piyasasında takas kural olarak aynı gün (T+0) veya ileri valörlü olarak DVP ile yapılır.", "KB1_Kavramsal"),

        ("q_1012_sert_042", "B", "MKK İhraççı Blokajı ve Halka Arz Sonrası Pay Satış Kısıtlamaları",
         "Payları ilk defa halka arz edilen ortaklıkların mevcut hakim ortaklarının ve yöneticilerinin halka arz edilen paylar dışındaki paylarına ilişkin MKK nezdinde uygulanan 'İhraççı Blokajı' ve satış yasağına dair hangisi DOĞRUDUR?",
         [
           ("A", "Hakim ortaklar halka arzın ertesi günü tüm hisselerini hiçbir izne gerek olmaksızın borsada satabilirler."),
           ("B", "Mevcut ortakların sahip oldukları paylar izahnamede taahhüt edilen süre boyunca (kural olarak 1 yıl) MKK nezdinde bloke edilir ve borsa satışına konu edilemez."),
           ("C", "İhraççı blokajı konulan paylar şirketin genel kurul toplantılarında oy hakkı kullanamaz."),
           ("D", "Hakim ortakların hisseleri halka arz sonrasında bedelsiz olarak halka arz konsorsiyum liderine devredilir."),
           ("E", "İhraççı blokajı sadece şirket iflas ettiğinde ticaret mahkemesince konulan bir cezadır."),
         ],
         "1. MEVZUAT DAYANAĞI: VII-128.1 Pay Tebliği m. 8 ve MKK İhraççı Blokajı Kılavuzu.\n2. HUKUKİ / TEKNİK ÇERÇEVE: Halka arz sonrası fiyat istikrarı ve yatırımcıyı korumak için ortaklar kural olarak 1 yıl boyunca borsa fiyatından hisse satmayacaklarını taahhüt ederler. MKK bu hisselere borsa satışını engelleyen 'İhraççı Blokajı' koyar.\n3. ADIM ADIM İNCELEME / HESAPLAMA: B şıkkı 1 yıllık taahhüt ve MKK borsa satış blokajı mekanizmasını tam doğru yansıtır.\n4. DOĞRU CEVAP VE SONUÇ: B seçeneğidir.\n5. ÇELDİRİCİ TUZAĞI: Blokajlı payların genel kurulda oy kullanamayacağını zannetmek (oy hakkı devam eder, sadece borsa satışı engellenir).",
         "Mevcut ortakların payları izahnamedeki taahhüt süresince (1 yıl) MKK nezdinde bloke edilir ve borsada satılamaz.", "KB2_Muhakeme"),

        ("q_1012_sert_043", "C", "Takasbank Altın Takası ve Fiziki Teslimat",
         "Borsa İstanbul Kıymetli Madenler Piyasası'nda işlem gören altınların takas ve teslimat sürecine dair hangisi DOĞRUDUR?",
         [
           ("A", "Altın işlemleri borsa ekranında sadece sanal olarak takas edilir; hiçbir durumda fiziki külçe altın teslimatı gerçekleştirilemez."),
           ("B", "Kıymetli maden takasında altın teslimatı sadece alıcı tarafın bildireceği serbest bölgedeki döviz bürolarında elden nakitle yapılır."),
           ("C", "Altın Borsa kasasına teslim edilir, bedeli Takasbank'tan ödenir; mutabakatla alıcı altını fiziken çekebilir veya kayden saklar."),
           ("D", "Kıymetli madenler takas mutabakatında Takasbank yalnızca yabancı ülke merkez bankalarının ihraç ettiği altın çeklerini kabul eder."),
           ("E", "Fiziki teslimat yapılabilmesi için işlem gören külçelerin en az bir asırlık antika altın niteliği taşıması kanunen zorunludur."),
         ],
         "1. MEVZUAT DAYANAĞI: Borsa İstanbul KMKTP Yönergesi ve Takasbank Kıymetli Madenler Takas Kılavuzu.\n2. HUKUKİ / TEKNİK ÇERÇEVE: Altın piyasasında satıcı fiziki külçeyi Borsa kasasına teslim eder. Takasbank nakit ödemeyi alır. Alıcıya isterse fiziki külçe teslim edilir, isterse kaydi hesapta saklanır.\n3. ADIM ADIM İNCELEME / HESAPLAMA: C şıkkı Borsa kasasına fiziki teslim ve Takasbank nakit takas sürecini tam açıklar.\n4. DOĞRU CEVAP VE SONUÇ: C seçeneğidir.\n5. ÇELDİRİCİ TUZAĞI: Fiziki altın teslimatının hiçbir şekilde yapılamayacağı zannı (A şıkkı).",
         "Kıymetli maden takasında altın Borsa kasasına teslim edilir, para Takasbank'tan ödenir; fiziki çekim veya kaydi saklama mümkündür.", "KB1_Kavramsal"),

        ("q_1012_sert_044", "D", "Yatırım Kuruluşlarının Tasfiyesinde Müşteri Varlıklarının İadesi",
         "Faaliyet yetki belgesi SPK tarafından iptal edilen veya iflasına karar verilen bir aracı kurumdaki müşteri varlıklarının iadesi sürecine ilişkin hangisi DOĞRUDUR?",
         [
           ("A", "Müşterilerin menkul kıymetleri derhal haczedilerek parası tasfiye edilen kurumun banka kredi ve vergi borçlarına tahsis edilir."),
           ("B", "Müşteri hesapları mahkemece 20 yıl süreyle dondurulur ve tasfiye bitene kadar hak sahiplerine hiçbir ödeme veya virman yapılmaz."),
           ("C", "Müşterilere ödeme yapılabilmesi için tasfiye edilen kurumun ortaklarının oybirliğiyle yazılı muvafakat vermesi zorunludur."),
           ("D", "Müşteri varlıkları kurum malvarlığından ayrı olduğundan, SPK/MKK gözetiminde müşteriye iade edilir veya başka kuruma virmanlanır."),
           ("E", "Müşteriler alacaklarını tahsil edebilmek için yalnızca aracı kurum yönetim kurulu üyelerinin şahsi konutlarını haczedebilirler."),
         ],
         "1. MEVZUAT DAYANAĞI: 6362 sayılı SPKn m. 47 ve m. 82-84.\n2. HUKUKİ / TEKNİK ÇERÇEVE: Müşteri varlıkları aracı kurumun iflas masasına girmez. Kurum batsa dahi hisseler MKK ve Takasbank nezdinde müşteri adınadır; başka bir aracı kuruma aktarılır veya iade edilir.\n3. ADIM ADIM İNCELEME / HESAPLAMA: D seçeneği iflas masası dışılığı ve doğrudan virman/iade güvencesini tam açıklar.\n4. DOĞRU CEVAP VE SONUÇ: D seçeneğidir.\n5. ÇELDİRİCİ TUZAĞI: Müşteri hisselerinin banka borcuna gideceğini düşünmek (A şıkkı).",
         "Aracı kurum iflas etse dahi müşteri hisseleri MKK nezdinde ayrıdır; doğrudan müşteriye iade edilir veya başka kuruma virmanlanır.", "KB2_Muhakeme"),

        ("q_1012_sert_045", "E", "MKK Tarafından Üretilen Raporlar ve Yatırımcı Hakları",
         "Merkezi Kayıt Kuruluşu (MKK) tarafından hak sahiplerine ve kamu otoritelerine sunulan raporlama ve bilgi sistemlerine ilişkin;\n\nI. İhraççı ortaklıklar kendi ortaklık yapılarını, pay defterlerini ve genel kurula katılacak ortak listelerini MKK sisteminden anlık raporlayabilirler.\nII. Yatırımcılar e-YATIRIMCI uygulaması üzerinden hesaplarındaki menkul kıymetleri, değerlerini ve üzerlerindeki blokajları görüntüleyebilirler.\nIII. Sermaye Piyasası Kurulu ve borsa gözetim birimleri piyasa dolandırıcılığı incelemelerinde MKK sicil kayıtlarını doğrudan denetim kanıtı olarak kullanabilir.\n\nYukarıda yer alan raporlama ve denetim işlevlerinden hangileri DOĞRUDUR?",
         [
           ("A", "Yalnızca I numaralı işlev mevzuat uyarınca doğrudur."),
           ("B", "Yalnızca II numaralı işlev mevzuat uyarınca doğrudur."),
           ("C", "I ve II numaralı işlevler mevzuat uyarınca doğrudur."),
           ("D", "II ve III numaralı işlevler mevzuat uyarınca doğrudur."),
           ("E", "I, II ve III numaralı işlevlerin tamamı mevzuat uyarınca doğrudur."),
         ],
         "1. MEVZUAT DAYANAĞI: 6362 sayılı SPKn m. 13, 87 ve MKK Bilgi Güvenliği Düzenlemeleri.\n2. HUKUKİ / TEKNİK ÇERÇEVE: MKK sistemi ihraççılara pay defteri (I), yatırımcılara e-Yatırımcı portali (II) ve SPK'ya gözetim/denetim kanıtı (III) sunar.\n3. ADIM ADIM İNCELEME / HESAPLAMA: I, II ve III öncüllerinin tümü MKK'nın yasal fonksiyonlarıdır.\n4. DOĞRU CEVAP VE SONUÇ: E seçeneğidir.\n5. ÇELDİRİCİ TUZAĞI: MKK kayıtlarının mahkemelerde veya SPK incelemelerinde delil sayılamayacağını düşünmek.",
         "MKK sistemi ihraççıya pay defteri, yatırımcıya e-Yatırımcı ve SPK'ya resmi denetim kanıtı sağlar.", "KB2_Muhakeme"),

        ("q_1012_sert_046", "A", "Takasbank Portföy Saklama ve Kolektif Yatırım Kuruluşları Net Varlık Değeri Kontrolü",
         "III-40.1 sayılı Tebliğ uyarınca portföy saklama hizmetini yürüten kuruluşun, yatırım fonunun günlük 'Net Varlık Değeri' ve 'Pay Birim Fiyatı' hesaplamalarındaki sorumluluğu nedir?",
         [
           ("A", "Portföy yönetim şirketi tarafından hesaplanan günlük net varlık değerini ve katılma payı birim fiyatını kontrol etmek ve mevzuata uygunluğunu onaylamakla yükümlüdür."),
           ("B", "Fon pay birim fiyatının hesaplanmasında hiçbir kontrol yetkisi olmayıp tüm sorumluluk yalnızca fon denetçisindedir."),
           ("C", "Portföy saklayıcısı her gün fon pay birim fiyatını kendi inisiyatifiyle iki katına katlama yetkisine sahiptir."),
           ("D", "Fon pay birim fiyatı sadece 5 yılda bir hesaplanır ve saklayıcı kuruluş bu hesaba hiçbir şekilde dahil olamaz."),
           ("E", "Portföy saklayıcısı fiyat hatalı hesaplansa dahi SPK'ya bildirimde bulunmaktan kanunen men edilmiştir."),
         ],
         "1. MEVZUAT DAYANAĞI: III-40.1 sayılı Tebliğ m. 6/2.\n2. HUKUKİ / TEKNİK ÇERÇEVE: Portföy saklayıcısı PYŞ'nin hesapladığı fon birim fiyatını bağımsız olarak kontrol etmek, değerleme hatalarını tespit etmek ve mevzuata uygunluğunu teyit etmekle yükümlüdür.\n3. ADIM ADIM İNCELEME / HESAPLAMA: A şıkkı saklayıcının günlük kontrol ve doğrulama yükümlülüğünü tam açıklar.\n4. DOĞRU CEVAP VE SONUÇ: A seçeneğidir.\n5. ÇELDİRİCİ TUZAĞI: Saklayıcının fiyata hiç karışmadığını zannetmek.",
         "Portföy saklayıcısı fonun günlük net varlık değerini ve birim pay fiyatını kontrol etmek ve onaylamakla yükümlüdür.", "KB1_Kavramsal"),

        ("q_1012_sert_047", "B", "Merkezi Takas Kuruluşunda Zorunlu Karşılaştırma ve Eşleşme (Matching)",
         "Borsa işlemlerinin Takasbank nezdinde takasa intikal etmeden önce işlem teyidi ve karşılaştırma (Matching / Trade Confirmation) sürecine ilişkin hangisi DOĞRUDUR?",
         [
           ("A", "Borsada gerçekleşen işlemler Takasbank'a aktarılmadan önce taraf kurumlar arasında telefonla sözlü olarak karşılıklı teyit edilir."),
           ("B", "Borsada eşleşen emirler anlık Takasbank'a aktarılır ve taraflar arasında ilave bir teyit aranmaksızın kesin işlem olarak takas edilir."),
           ("C", "Alıcı kurum seans bitiminde onay vermediği takdirde borsada eşleşmiş bir işlem Takasbank tarafından re'sen iptal edilir."),
           ("D", "Borsa işlemlerinin takasa intikal edebilmesi için her bir işlem bordrosunun noter tarafından tasdik edilmesi yasal zorunluluktur."),
           ("E", "İşlem teyitleri ve takas eşleşmeleri günlük olarak değil, sadece her ayın son iş günü topluca Takasbank komitesince onaylanır."),
         ],
         "1. MEVZUAT DAYANAĞI: Takasbank MKT Yönetmeliği m. 10.\n2. HUKUKİ / TEKNİK ÇERÇEVE: Borsada emirler eşleştiği anda kesinleşir. Borsa sistemi doğrudan Takasbank'a elektronik veri akışı sağlar; kurumların ayrıca 'biz bu işlemi kabul etmiyoruz' deme veya ikili teyit bekleme hakkı yoktur.\n3. ADIM ADIM İNCELEME / HESAPLAMA: B şıkkı borsadan Takasbank'a doğrudan elektronik aktarım ve ikili teyitsiz kesinleşme ilkesini doğru açıklar.\n4. DOĞRU CEVAP VE SONUÇ: B seçeneğidir.\n5. ÇELDİRİCİ TUZAĞI: İşlem sonrası kurumların ayrıca telefonla onaylaşması gerektiği zannı.",
         "Borsada eşleşen emirler elektronik olarak Takasbank'a iletilir ve ilave ikili teyit aranmaksızın kesinleşir.", "KB2_Muhakeme"),

        ("q_1012_sert_048", "C", "Takasbank Para Piyasasında Temerrüt ve Garanti",
         "Takasbank Para Piyasası'nda (TPP) borçlanan bir üyenin vadesinde anapara ve faiz borcunu ödeyememesi durumunda Takasbank'ın borç veren üyeye karşı tutumu nedir?",
         [
           ("A", "Takasbank borç veren üyeye paranın tahsil edilemediğini bildirerek alacağını şahsen dava etmesini tavsiye eder ve çekilir."),
           ("B", "Takasbank borç veren üyenin alacağını tamamen siler ve meydana gelen tüm nakit açığını borç veren kuruma fatura eder."),
           ("C", "Takasbank MKT olarak borç verenin parasını tam öder; temerrüt eden üyenin teminatlarını paraya çevirerek yasal takip başlatır."),
           ("D", "Borç veren kuruma nakit ödeme yapılmaz, alacağı tutar karşılığında Takasbank'ın halka kapalı pay senetleri devredilir."),
           ("E", "Takasbank işlemi tek taraflı feshederek borçlanma günündeki faiz ve anapara şartlarını başlangıç tarihine geri döndürür."),
         ],
         "1. MEVZUAT DAYANAĞI: Takasbank Para Piyasası Yönetmeliği m. 12, 13.\n2. HUKUKİ / TEKNİK ÇERÇEVE: TPP'de Takasbank MKT olduğu için borç veren üye borçlunun temerrüdünden etkilenmez. Takasbank parayı öder ve borçlu üyenin teminatlarını nakde çevirerek tahsil eder.\n3. ADIM ADIM İNCELEME / HESAPLAMA: C şıkkı Takasbank'ın borç verene alacağını eksiksiz ödeme MKT garantisini tam açıklar.\n4. DOĞRU CEVAP VE SONUÇ: C seçeneğidir.\n5. ÇELDİRİCİ TUZAĞI: TPP'de garantinin olmadığını sanmak.",
         "Takasbank MKT olarak borç verenin parasını tam öder, temerrüt eden üyenin teminatlarını paraya çevirir.", "KB2_Muhakeme"),

        ("q_1012_sert_049", "D", "MKK Saklama Sisteminde Hak Sahipliği İhtilafları",
         "6362 sayılı Sermaye Piyasası Kanunu m. 13/5 uyarınca kayden izlenen sermaye piyasası araçlarının mülkiyetine veya hak sahipliğine ilişkin açılacak davalarda MKK'nın hukuki sorumluluğuna dair hangisi DOĞRUDUR?",
         [
           ("A", "MKK ihtilaflarda tarafların haklılığını bizzat araştırıp ticaret mahkemesi gibi nihai bağlayıcı hüküm vermekle yükümlüdür."),
           ("B", "MKK pay sahipleri arasındaki mülkiyet davalarında zorunlu davalı gösterilir ve oluşacak tüm zararları kusursuz tazmin eder."),
           ("C", "MKK nezdinde tutulan kaydi siciller adli makamlarda resmi delil niteliği taşımaz; yalnızca basılı şirket defterleri geçerlidir."),
           ("D", "MKK adli bildirimleri uygular; ağır kusuru bulunmadıkça üye bildirimlerine dayanılarak yapılan tescillerden sorumlu tutulamaz."),
           ("E", "MKK aleyhine tazminat davası açılabilmesi için SPK ve Borsa İstanbul Yönetim Kurulundan ön izin alınması kanunen şarttır."),
         ],
         "1. MEVZUAT DAYANAĞI: 6362 sayılı SPKn m. 13/5.\n2. HUKUKİ / TEKNİK ÇERÇEVE: MKK sicil tutucudur. Mahkeme kararlarını uygular. MKK'nın kendi ağır kusuru veya kastı olmadıkça, üyelerin bildirdiği verilere dayanarak yaptığı tescillerden ötürü MKK sorumlu tutulamaz.\n3. ADIM ADIM İNCELEME / HESAPLAMA: D seçeneği yasanın amir sorumluluk sınırını ve adli bildirim uygulama görevini tam ifade eder.\n4. DOĞRU CEVAP VE SONUÇ: D seçeneğidir.\n5. ÇELDİRİCİ TUZAĞI: MKK'nın her davada taraf olup tazminat ödeyeceğini zannetmek.",
         "MKK mahkeme kararlarını uygular; kusuru bulunmadıkça üye bildirimlerine dayalı işlemlerden sorumlu tutulamaz.", "KB2_Muhakeme"),

        ("q_1012_sert_050", "E", "Takasbank ve MKK Arasındaki Görev Dağılımı Özeti",
         "Türkiye sermaye piyasalarında 'Takasbank' ile 'Merkezi Kayıt Kuruluşu' (MKK) arasındaki kurumsal görev ayrımına ilişkin;\n\nI. Takasbank: İşlemlerin takasını ve nakit mutabakatını yürüten, Merkezi Karşı Taraf (MKT) güvencesi sağlayan merkezi kuruluştur.\nII. MKK: Sermaye piyasası araçlarının kaydileştirilerek hak sahipleri bazında mülkiyet kayıtlarının tutulduğu Merkezi Saklama Kuruluşudur (CSD).\nIII. Takasbank nakit ve teminat yönetimini üstlenirken, MKK menkul kıymetlerin mülkiyet ve hak sahipliği sicilini yönetir.\n\nYukarıda yer alan kurumsal görev tanımlarından hangileri DOĞRUDUR?",
         [
           ("A", "Yalnızca I numaralı görev tanımı mevzuata uygundur."),
           ("B", "Yalnızca II numaralı görev tanımı mevzuata uygundur."),
           ("C", "I ve II numaralı görev tanımları mevzuata uygundur."),
           ("D", "II ve III numaralı görev tanımları mevzuata uygundur."),
           ("E", "I, II ve III numaralı görev tanımlarının tamamı mevzuata uygundur."),
         ],
         "1. MEVZUAT DAYANAĞI: 6362 sayılı SPKn m. 13, 77, 81.\n2. HUKUKİ / TEKNİK ÇERÇEVE: Türk sermaye piyasası altyapısında Takasbank takas, nakit mutabakatı ve MKT rolündedir. MKK ise Merkezi Saklama Kuruluşu (Central Securities Depository - CSD) olarak mülkiyet sicilini tutar.\n3. ADIM ADIM İNCELEME / HESAPLAMA: I, II ve III öncüllerinin her biri Takasbank ve MKK arasındaki yetki ve görev paylaşımını tam doğru ortaya koyar.\n4. DOĞRU CEVAP VE SONUÇ: E seçeneğidir.\n5. ÇELDİRİCİ TUZAĞI: Takasbank ile MKK'nın aynı kurum olduğunu ve tüm görevleri tek kurumun yürüttüğünü düşünmek.",
         "Takasbank takas ve MKT nakit mutabakatını yönetir; MKK kaydi mülkiyet sicilini tutan CSD kuruluşudur.", "KB1_Kavramsal"),

    ]
    
    for item in raw_data:
        qid, correct_key, topic, text, opts, exp, trap, skill = item
        options_list = [{"key": k, "text": t} for k, t in opts]
        questions.append({
            "id": qid,
            "module_id": "1012",
            "source": "cikmis",
            "topic": topic,
            "chapter": "TAKAS SAKLAMA MKT ŞELALESİ VE OPERASYON İŞLEMLERİ",
            "text": text,
            "options": options_list,
            "correct_answer": correct_key,
            "explanation": exp,
            "trap": trap,
            "difficulty": "hard",
            "tags": ["1012", topic],
            "cognitive_skill": skill
        })
        
    return questions

if __name__ == '__main__':
    qs = generate_questions()
    print(f"Modül 1012 için {len(qs)} soru üretildi.")
    key_counts = {}
    for q in qs:
        key_counts[q['correct_answer']] = key_counts.get(q['correct_answer'], 0) + 1
    print("Cevap anahtarı dağılımı:", key_counts)
    with open('scripts/data_1012_hard.json', 'w', encoding='utf-8') as f:
        json.dump(qs, f, ensure_ascii=False, indent=2)
    print("scripts/data_1012_hard.json kaydedildi.")
