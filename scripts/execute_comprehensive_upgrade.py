# -*- coding: utf-8 -*-
import json
import sys
import os

sys.stdout.reconfigure(encoding='utf-8')

# The 39 overhauled questions + 1 fix for q_1012_ogretici_011
REPLACEMENTS = {
    # ----------------------------------------------------
    # MODUL 1001 OVERHAULS (22 questions)
    # ----------------------------------------------------
    "q_1001_master_009": {
        "text": "6362 sayılı SPKn m.106 uyarınca doğrudan veya dolaylı olarak içsel bilgiye dayalı işlem yaparak (bilgi suistimali) haksız menfaat temin eden failler hakkında uygulanacak yaptırım hükmü aşağıdakilerden hangisinde tam ve doğru olarak verilmiştir?",
        "options": [
            {"key": "A", "text": "3 yıldan 5 yıla kadar hapis ve elde edilen menfaatin iki katından az olmamak üzere adli para cezası"},
            {"key": "B", "text": "2 yıldan 5 yıla kadar hapis veya Kurul tarafından belirlenecek tutarda idari para cezası"},
            {"key": "C", "text": "1 yıldan 3 yıla kadar hapis ve zarara uğrayan yatırımcıların tazmini amacıyla güvenlik tedbiri"},
            {"key": "D", "text": "3 yıldan 5 yıla kadar hapis veya elde edilen menfaatin üç katı tutarında disiplin para cezası"},
            {"key": "E", "text": "Yalnızca borsada 5 yıl süreyle geçici işlem yapma yasağı ve elde edilen haksız kazancın müsaderesi"}
        ],
        "correct_answer": "A",
        "explanation": "6362 sayılı Sermaye Piyasası Kanunu m.106 gereğince Bilgi Suistimali (insider trading) suçunun yaptırımı '3 yıldan 5 yıla kadar hapis VE elde edilen menfaatin iki katından az olmamak üzere adli para cezası'dır. Seçeneklerdeki 'veya' tuzaklarına dikkat edilmelidir; hapis ve adli para cezası kümülatif (birlikte) uygulanır."
    },
    "q_1001_master_011": {
        "text": "6362 sayılı Sermaye Piyasası Kanunu m.107 kapsamında piyasa dolandırıcılığı (manipülasyon) suçu bakımından 'Etkin Pişmanlık' kurumuna ilişkin aşağıdaki ifadelerden hangisi DOĞRUDUR?",
        "options": [
            {"key": "A", "text": "Hakkında mahkemece kesinleşmiş hapis cezası verildikten sonra Hazineye ödeme yaparsa infaz tamamen durdurulur."},
            {"key": "B", "text": "Kurulca incelemeye başlanmadan önce durumu Kurula bildirip elde edilen menfaatin iki katını Hazineye öderse ceza verilmez."},
            {"key": "C", "text": "Etkin pişmanlık kurumu yalnızca bilgi suistimalinde geçerli olup piyasa dolandırıcılığı suçlarında hiçbir şekilde uygulanmaz."},
            {"key": "D", "text": "Soruşturma evresinde Kurul ile uzlaşmaya varılması halinde adli süreç sona erer ve yalnızca idari para cezası ödenir."},
            {"key": "E", "text": "İnceleme başlatıldıktan sonra yapılan bildirimlerde menfaatin iadesi yapılsa dahi kovuşturma aşamasında ceza indirimi yapılamaz."}
        ],
        "correct_answer": "B",
        "explanation": "SPKn m.107/3 uyarınca; SPK tarafından incelemeye başlanmadan önce SPK'ya ihbarda bulunarak elde ettiği menfaatin iki katı tutarındaki parayı Hazineye ödeyen kişi hakkında cezaya hükmolunmaz. İnceleme başladıktan sonra fakat kovuşturma başlamadan önce ödenirse cezada 1/2 indirim uygulanır."
    },
    "q_1001_master_013": {
        "text": "Sermaye Piyasası Kurulu'ndan gerekli izin ve yetki belgelerini almaksızın sermaye piyasasında izinsiz faaliyette bulunan gerçek ve tüzel kişiler hakkında öngörülen kanuni yaptırım aşağıdakilerden hangisidir?",
        "options": [
            {"key": "A", "text": "Yalnızca Kurul tarafından faaliyet durdurma ihtarı verilir ve işlemler borsa bülteninde ilan edilir."},
            {"key": "B", "text": "İlgili faaliyetten elde edilen toplam gelirin yarısı oranında idari para cezası ve 1 ay men cezası verilir."},
            {"key": "C", "text": "İki yıldan beş yıla kadar hapis ve beş bin günden on bin güne kadar adli para cezası uygulanır."},
            {"key": "D", "text": "Ticaret mahkemesi tarafından şirketin kayyuma devredilmesi ve kuruculara ticaretten men cezası verilir."},
            {"key": "E", "text": "Yalnızca internet sitelerine idari erişim engeli getirilerek ilgililer hakkında disiplin soruşturması açılır."}
        ],
        "correct_answer": "C",
        "explanation": "SPKn m.109/2 gereğince Kuruldan izin almaksızın sermaye piyasası faaliyetinde bulunanlar 2 yıldan 5 yıla kadar hapis ve beş bin günden on bin güne kadar adli para cezası ile cezalandırılırlar. Ayrıca izinsiz internet sitelerine erişim engeli ve derhal tedbirler uygulanır."
    },
    "q_1001_master_025": {
        "text": "Sermaye piyasası araçlarının halka arzında aracılık türlerinden biri olan 'Tümünü Yüklenim' (Underwriting) yöntemiyle ilgili aşağıdaki ifadelerden hangisi DOĞRUDUR?",
        "options": [
            {"key": "A", "text": "Halka arz edilecek payların tamamı satış başlamadan önce yetkili aracı kurum tarafından bedeli ödenerek devralınır."},
            {"key": "B", "text": "Satılamayan payların tamamı veya bir kısmı halka arz süresi sonunda ihraççı ortaklığa bedelsiz olarak iade edilir."},
            {"key": "C", "text": "Aracı kurum yalnızca en iyi gayreti göstermeyi taahhüt eder ve satılmayan paylar için hiçbir finansal risk üstlenmez."},
            {"key": "D", "text": "Payların mülkiyeti ihraççıda kalmaya devam eder ve aracı kurum sadece komisyon karşılığı talep toplama yürütür."},
            {"key": "E", "text": "Satış süresi sonunda satılamayan paylar Borsa İstanbul tarafından doğrudan satın alınarak piyasa yapıcısına devredilir."}
        ],
        "correct_answer": "A",
        "explanation": "Tümünü yüklenimde ihraç edilecek sermaye piyasası araçlarının tamamı satış süresi başlamadan önce aracı kuruluş veya konsorsiyum tarafından bedeli ödenerek peşinen satın alınır; ihraççı finansman riskinden tamamen kurtulur ve ardından araçlar halka arz edilir."
    },
    "q_1001_master_031": {
        "text": "Özel Durumlar Tebliği (II-15.1) çerçevesinde, sermaye piyasası aracının fiyatını veya değerini etkileyebilecek nitelikteki 'İçsel Bilgi' kavramının tanımı aşağıdakilerden hangisinde tam olarak verilmiştir?",
        "options": [
            {"key": "A", "text": "Kamuya henüz açıklanmamış, doğrudan veya dolaylı olarak ihraççıya ya da araca ilişkin, fiyatı etkileyebilecek somut bilgidir."},
            {"key": "B", "text": "Şirket hakkında basın organlarında ve sosyal medyada yer alan doğruluğu teyit edilmemiş her türlü piyasa söylentisidir."},
            {"key": "C", "text": "İhraççının periyodik olarak kamuya duyurmakla yükümlü olduğu geçmiş dönem bağımsız denetimden geçmiş finansal raporlarıdır."},
            {"key": "D", "text": "Şirket yönetim kurulunun rutin iç yazışmalarında yer alan ve personelin idari işleyişine dair genel kurumsal duyurulardır."},
            {"key": "E", "text": "Kamu otoriteleri tarafından resmi istatistik bültenlerinde ilan edilen makroekonomik büyüme ve genel enflasyon göstergeleridir."}
        ],
        "correct_answer": "A",
        "explanation": "İçsel bilgi; kamuya açıklanmamış olması, doğrudan/dolaylı olarak ihraççı veya araçla ilgili bulunması, belirli ve kesin bir olaya dayanması ve açıklandığında fiyat veya yatırım kararını etkileme potansiyeline (önemlilik testi) sahip olması unsurlarını birlikte barındırır."
    },
    "q_1001_master_037": {
        "text": "İdari sorumluluğu bulunan yöneticiler ve bunlarla yakından ilişkili kişilerin şirket paylarında yaptıkları işlemlerin kamuya açıklanmasıyla ilgili hangisi DOĞRUDUR?",
        "options": [
            {"key": "A", "text": "Tebliğde belirlenen parasal eşiği aşan tüm pay alım veya satım işlemleri işlemi yapan kişi tarafından KAP'ta açıklanır."},
            {"key": "B", "text": "İdari sorumluluğu bulunan kişilerin işlemleri hiçbir koşulda kamuya açıklanmaz ve sır kapsamında gizli tutulur."},
            {"key": "C", "text": "Yalnızca net zarar ile sonuçlanan ve şirket sermayesinin yüzde beşini aşan hisse senedi işlemleri açıklanır."},
            {"key": "D", "text": "Yalnızca şirketin genel müdürü işlem bildiriminde bulunabilir; yönetim kurulu üyeleri bu tebliğ kapsamı dışındadır."},
            {"key": "E", "text": "İşlem bildirimleri yalnızca şirketin yıllık olağan genel kurul toplantısında ortaklara sözlü olarak sunulur."}
        ],
        "correct_answer": "A",
        "explanation": "Özel Durumlar Tebliği uyarınca idari sorumluluğu bulunan kişiler ve bunlarla yakından ilişkili kişilerin ortaklık paylarındaki işlemleri, takvim yılı içindeki toplam işlem tutarı Kurulca belirlenen parasal limiti aştığında işlemi yapan kişilerce KAP'ta duyurulur."
    },
    "q_1001_master_044": {
        "text": "Halka açık anonim ortaklıkların ilişkili taraflarıyla gerçekleştirecekleri varlık, hizmet devri veya yükümlülük transferlerinde SPK lisanslı bir değerleme kuruluşuna değerleme yaptırma zorunluluğu hangi eşikte doğar?",
        "options": [
            {"key": "A", "text": "İşlem tutarının, kamuya açıklanan son finansal tablolardaki aktif toplamına veya hasılata oranının %5'ini aşması durumunda"},
            {"key": "B", "text": "İşlem tutarının şirketin çıkarılmış veya ödenmiş sermayesine olan oranının en az %20'sine ulaşması halinde"},
            {"key": "C", "text": "Yönetim kurulu üyelerinin tamamının oybirliğiyle onay vermesi durumunda işlem büyüklüğüne bakılmaksızın"},
            {"key": "D", "text": "İşlemin piyasa değerinin bağımsız denetimden geçmiş özkaynak toplamının %1'ini aştığı her türlü ticari ilişkide"},
            {"key": "E", "text": "Yalnızca ilişkili tarafın yurt dışında yerleşik yabancı bir iştirak veya bağlı ortaklık olması şartına bağlı olarak"}
        ],
        "correct_answer": "A",
        "explanation": "Kurumsal Yönetim Tebliği (II-17.1) uyarınca ilişkili taraf işlemlerinde, işlem tutarının son finansal tablolardaki aktif toplamına veya hasılata oranının %5'ini aşması halinde değerleme raporu hazırlanması zorunludur. Oranın %10'u aşması halinde ise genel kurul kararı ve bağımsız üyelerin onayı gibi ağırlaştırılmış şartlar devreye girer."
    },
    "q_1001_master_051": {
        "text": "Borsa Yatırım Fonlarını (BYF / ETF) geleneksel menkul kıymet yatırım fonlarından ayıran en belirgin yapısal fark aşağıdakilerden hangisidir?",
        "options": [
            {"key": "A", "text": "Fon paylarının Borsa İstanbul Pay Piyasası'nda seans süresince hisse senedi gibi anlık piyasa fiyatlarıyla alınıp satılabilmesi"},
            {"key": "B", "text": "Fon portföyünün yalnızca kamu borçlanma araçlarından ve ters repo işlemlerinden oluşmak zorunda bulunması"},
            {"key": "C", "text": "Tüzel kişiliğe sahip bir anonim ortaklık şeklinde kurulması ve genel kurulunda pay sahiplerine oy hakkı tanıması"},
            {"key": "D", "text": "Yatırımcılardan yönetim ücreti veya saklama komisyonu gibi herhangi bir yasal gider ve masraf kesintisi yapılmaması"},
            {"key": "E", "text": "Portföy değerinin ve katılma payı fiyatının yalnızca ayda bir kez hesaplanarak kamuoyuna ilan edilmesi zorunluluğu"}
        ],
        "correct_answer": "A",
        "explanation": "Borsa Yatırım Fonları (BYF), bir endeksi takip eden ve payları borsa seansı boyunca tıpkı bir hisse senedi gibi piyasa fiyatından alınıp satılabilen fonlardır. Geleneksel fonlar ise günde bir kez hesaplanan pay fiyatı üzerinden kurucu aracılığıyla alınıp satılır."
    },
    "q_1001_master_077": {
        "text": "Türkiye Sermaye Piyasaları Birliği (TSPB) Meslek Kuralları ve Etik İlkeleri'nin bağlayıcılığı ve kapsamı hakkında aşağıdakilerden hangisi DOĞRUDUR?",
        "options": [
            {"key": "A", "text": "Birlik üyesi tüm sermaye piyasası kurumları ile bu kurumlarda görev yapan tüm unvanlardaki personel için bağlayıcıdır."},
            {"key": "B", "text": "Yalnızca borsa kotunda payları işlem gören halka açık ortaklıkların yönetim kurulu üyeleri için bağlayıcıdır."},
            {"key": "C", "text": "Sadece sermaye piyasası lisansına sahip genel müdür ve yönetim kurulu başkanları açısından hukuki sonuç doğurur."},
            {"key": "D", "text": "İhtiyari tavsiye niteliğinde prensipler olup uyulmaması halinde herhangi bir disiplin cezası uygulanması mümkün değildir."},
            {"key": "E", "text": "Yalnızca Takasbank ve Merkezi Kayıt Kuruluşu bünyesinde çalışan daimi personelin mesleki faaliyetlerini kapsar."}
        ],
        "correct_answer": "A",
        "explanation": "TSPB Meslek Kuralları ve Etik İlkeleri, Birliğin tüm üyeleri (aracı kurumlar, bankalar, portföy yönetim şirketleri vb.) ile bu kurumlarda çalışan tüm idari ve mesleki personel için istisnasız bağlayıcıdır; ihlali disiplin cezası gerektirir."
    },
    "q_1001_master_079": {
        "text": "Sermaye piyasası kurum ve çalışanlarının 'Mesleki Özen ve Titizlik' ilkesi çerçevesinde müşterilerine karşı yükümlülükleri hakkında hangisi DOĞRUDUR?",
        "options": [
            {"key": "A", "text": "Müşteri emirlerini zamanında ve talimata uygun olarak yerine getirmek, eksik ve yanıltıcı bilgi vermekten kaçınmak"},
            {"key": "B", "text": "Müşterinin yatırım kararlarında her koşulda mutlak kâr garantisi vererek portföy değer kaybını üstlenmek"},
            {"key": "C", "text": "Müşteri emirlerini piyasaya iletmeden önce kendi kurumsal portföyünün kârlılık hedeflerine göre bekletmek"},
            {"key": "D", "text": "Müşterilere yalnızca kurumun yüksek komisyon geliri elde edeceği riskli kaldıraçlı ürünleri tavsiye etmek"},
            {"key": "E", "text": "Müşteri hesap ekstrelerini ve işlem sonuç bildirimlerini yalnızca yılda bir kez genel kurulda posta ile göndermek"}
        ],
        "correct_answer": "A",
        "explanation": "Mesleki özen ve titizlik ilkesi gereğince sermaye piyasası çalışanları; müşteri işlemlerini basiretli bir uzmanın göstereceği özenle, mevzuata ve müşteri talimatlarına tam uygun olarak yürütmek, gerçeğe aykırı ve yanıltıcı bilgilendirmeden kesinlikle kaçınmak zorundadır."
    },
    "q_1001_master_080": {
        "text": "Sermaye piyasası kurumlarının veya çalışanlarının kendi menfaatleri ile müşterilerinin menfaatleri arasında bir menfaat çatışması ortaya çıkması durumunda TSPB Meslek Kuralları uyarınca izlenmesi gereken temel ilke hangisidir?",
        "options": [
            {"key": "A", "text": "Müşterinin hak ve menfaatleri her koşulda kurumun ve kurum çalışanlarının menfaatinden üstün tutulur ve önceliklendirilir."},
            {"key": "B", "text": "Kurumun ticari kârlılığı önceliklendirilir ve müşteriye işlem sonrasında yazılı bilgilendirme yapılmasıyla yetinilir."},
            {"key": "C", "text": "Menfaat çatışması konusu işlem derhal tek taraflı olarak iptal edilir ve müşteriyle olan çerçeve sözleşme feshedilir."},
            {"key": "D", "text": "Uyuşmazlık konusu işlem mahkeme kararı alınıncaya kadar hiçbir gerekçe gösterilmeksizin askıya alınır."},
            {"key": "E", "text": "Çalışan kendi lehine olan pozisyonu tercih ederek aracı kurum yönetim kuruluna üç iş günü içinde bilgi verir."}
        ],
        "correct_answer": "A",
        "explanation": "TSPB Meslek Kuralları ve SPK mevzuatı uyarınca 'Müşteri Menfaatinin Önceliği' esastır. Kurum ile müşteri veya çalışan ile müşteri arasında menfaat çatışması doğduğunda müşterinin hak ve menfaatleri daima kurumun ve çalışanın menfaatinin önünde tutulur."
    },
    "q_1001_master_081": {
        "text": "Bir aracı kurum çalışanının, müşterinin piyasa fiyatını etkileyebilecek büyüklükteki alım emrini sisteme iletmeden önce kendi adına hisse alması (Front-running) hangi hukuki ve mesleki ihlali oluşturur?",
        "options": [
            {"key": "A", "text": "Müşteri emrine ve piyasa bilgisine sadakat ilkesinin ihlali ile haksız kazanç sağlayan ağır bir meslek suçu ve suç teşkil eder."},
            {"key": "B", "text": "Kurum yönetim kurulundan önceden izin alınmış olması koşuluyla mevzuatça uygun kabul edilen standart bir arbitraj işlemidir."},
            {"key": "C", "text": "Sadece piyasa yapıcılığı sözleşmesi imzalamış olan yetkili kurumlara tanınan likidite sağlama ve kotasyon ayrıcalığıdır."},
            {"key": "D", "text": "İşlem hacminin yüksek tutulması amacıyla borsada teşvik edilen ve idari para cezası gerektirmeyen meşru bir uygulamadır."},
            {"key": "E", "text": "Yalnızca sermaye piyasası lisansına sahip olmayan stajyer personel tarafından yapıldığında hukuki sorumluluk doğurur."}
        ],
        "correct_answer": "A",
        "explanation": "Front-running (müşteri emrinin önüne geçme), aracı kurum çalışanının müşterinin fiyatı etkileyebilecek emrini bildiği halde bu emri borsaya iletmeden önce kendi veya ilişkili kişilerin hesabına işlem yapmasıdır. Bu eylem hem TSPB meslek kurallarını ihlal eder hem de SPKn m.106 kapsamında cezai sorumluluk doğurur."
    },
    "q_1001_master_083": {
        "text": "Sermaye piyasası kurumları ve çalışanlarının tabi olduğu 'Sır Saklama' yükümlülüğü ve bu yükümlülüğün yasal sınırları ile ilgili aşağıdakilerden hangisi DOĞRUDUR?",
        "options": [
            {"key": "A", "text": "Kanunen yetkili adli merciler, SPK, MASAK ve vergi denetim elemanlarının mevzuattan doğan talepleri sır saklamanın istisnasıdır."},
            {"key": "B", "text": "Çalışanın kurumdan istifa etmesi veya sözleşmesinin sona ermesi halinde müşteri sırlarını saklama yükümlülüğü de derhal biter."},
            {"key": "C", "text": "Müşteri bilgileri çalışanlar tarafından üçüncü kişilere ticari veya akademik araştırma amaçlı olarak serbestçe paylaşılabilir."},
            {"key": "D", "text": "Müşterinin yazılı onayı olmaksızın dahi kamuoyu aydınlatma amacıyla tüm hesap hareketleri basın organlarına verilebilir."},
            {"key": "E", "text": "Sır saklama yükümlülüğü yalnızca kurum genel müdürü için geçerli olup operasyon ve emir kabul personeli bu kurala tabi değildir."}
        ],
        "correct_answer": "A",
        "explanation": "SPKn m.108 ve ilgili mevzuat gereğince müşteri sırları kesinlikle saklanmalıdır. Bu yükümlülük görevden ayrıldıktan sonra da devam eder. Kanunen açıkça yetkilendirilmiş adli makamlar, SPK, MASAK, TCMB ve vergi denetimi gibi kamu otoritelerinin bilgi talepleri ise sır saklama yükümlülüğünün yasal istisnasıdır."
    },
    "q_1001_master_085": {
        "text": "TSPB Meslek Kuralları uyarınca sermaye piyasası kurum çalışanlarının müşterilerden veya üçüncü taraflardan maddi menfaat ya da borç kabul etmelerine ilişkin kural aşağıdakilerden hangisidir?",
        "options": [
            {"key": "A", "text": "Tarafsızlığı ve mesleki kararları etkileyebilecek, olağan teamülleri aşan maddi menfaat veya borç kabul edilmesi kesinlikle yasaktır."},
            {"key": "B", "text": "Değeri ne olursa olsun nakit para dışındaki tüm menkul malların çalışanlarca kabul edilmesi mevzuat uyarınca tamamen serbesttir."},
            {"key": "C", "text": "Müşteriden kişisel borç veya borç karşılığı menkul kıymet talep edilmesi aracı kurum yönetim kurulu iznine bağlı bir haktır."},
            {"key": "D", "text": "Yalnızca yılbaşı ve resmi kutlamalarda verilen ikramlar tutarına bakılmaksızın personelin kişisel kazancı ve hakkı sayılır."},
            {"key": "E", "text": "Müşteriden menfaat veya ağırlama kabul edilmesi durumunda işlemlerde ilgili müşterinin emirlerine öncelik tanınması zorunludur."}
        ],
        "correct_answer": "A",
        "explanation": "TSPB Meslek Kuralları uyarınca çalışanlar; bağımsızlıklarını, tarafsızlıklarını ve mesleki kararlarını etkileyebilecek ya da dışarıdan bu izlenimi verebilecek hiçbir borç, komisyon, ağırlama veya maddi menfaati müşterilerden ya da iş ortaklarından kabul edemezler; olağan teamül sınırlarını aşan menfaatler yasaktır."
    },
    "q_1001_master_091": {
        "text": "Türkiye Sermaye Piyasaları Birliği (TSPB) Disiplin Yönetmeliği uyarınca meslek kurallarına ve Birlik kararlarına aykırı hareket eden üye kuruluşlara veya personeline verilebilecek disiplin cezaları hangi seçenekte eksiksiz sıralanmıştır?",
        "options": [
            {"key": "A", "text": "Uyarı, Kınama, Para Cezası, Geçici Olarak Faaliyetten Men, Sürekli Olarak Faaliyetten Men"},
            {"key": "B", "text": "Sözlü İhtar, İdari Para Cezası, Hapis Cezası ve Ticaretten Men"},
            {"key": "C", "text": "Kınama, Ruhsat İptali, Şirket Kapatma ve Mal Varlığına El Koyma"},
            {"key": "D", "text": "Yazılı Uyarı, Adli Para Cezası, Zorunlu Sermaye Artırımı ve Borsa Kotundan Çıkarma"},
            {"key": "E", "text": "Disiplin Para Cezası, Gözaltı Pazarına Alma, Borsa Seans Durdurma ve Kayyum Atama"}
        ],
        "correct_answer": "A",
        "explanation": "TSPB Disiplin Yönetmeliği'ne göre verilebilecek disiplin cezaları ağırlık sırasına göre şunlardır: 1. Uyarı, 2. Kınama, 3. Para Cezası, 4. Geçici Olarak Faaliyetten Men (veya Birlik üyeliğinden geçici çıkarma), 5. Sürekli Olarak Faaliyetten Men (veya Birlik üyeliğinden sürekli çıkarma)."
    },
    "q_1001_master_092": {
        "text": "TSPB Disiplin Yönetmeliği kapsamında 'Uyarı' cezasının yasal tanımı ve uygulanma amacı aşağıdakilerden hangisinde doğru olarak açıklanmıştır?",
        "options": [
            {"key": "A", "text": "İlgilinin mesleki faaliyetlerinde ve görevini yerine getirmesinde daha dikkatli ve özenli davranması gerektiğinin yazı ile bildirilmesidir."},
            {"key": "B", "text": "İlgilinin eyleminden dolayı kınandığının ve meslek onurunu zedelediğinin siciline işlenerek kamuoyuna bültende duyurulmasıdır."},
            {"key": "C", "text": "İlgilinin belirli bir parasal tutarı ceza olarak ödemekle yükümlü tutulduğunu belirten mali yaptırım kararıdır."},
            {"key": "D", "text": "İlgilinin borsa ve teşkilatlanmış piyasalarda işlem yapma yetkisinin belirli bir süreyle durdurulduğunun bildirilmesidir."},
            {"key": "E", "text": "İlgili sermaye piyasası kurumunun yetki belgelerinin iptali talebiyle SPK'ya sevk edildiğinin taraflara tebliğ edilmesidir."}
        ],
        "correct_answer": "A",
        "explanation": "Uyarı cezası; personelin veya üyenin mesleki faaliyetlerinde, görevlerinde ve Birliğe karşı yükümlülüklerinde daha dikkatli, itinalı ve özenli davranması gerektiğinin ilgiliye yazı ile bildirilmesidir (en hafif disiplin cezasıdır)."
    },
    "q_1001_master_094": {
        "text": "TSPB Disiplin Yönetmeliği uyarınca Birlik Disiplin Kurulu tarafından üyeler veya personel hakkında uygulanan disiplin para cezalarının hukuki niteliği ve akıbeti nasıldır?",
        "options": [
            {"key": "A", "text": "Tahsil edilen para cezaları Birliğe irat (gelir) kaydedilir ve Birliğin eğitim ile mesleki araştırma faaliyetlerinde kullanılır."},
            {"key": "B", "text": "Tahsil edilen tutarlar doğrudan Sermaye Piyasası Kurulu bütçesine veya Hazine ve Maliye Bakanlığı hesaplarına aktarılır."},
            {"key": "C", "text": "İlgili aracı kurumun işlem yaptığı müşteriler arasında zararları oranında paylaştırılmak üzere teminata bağlanır."},
            {"key": "D", "text": "Borsa İstanbul A.Ş. nezdinde oluşturulan borsa yatırımcı koruma ve tazmin fonu havuzuna devredilir."},
            {"key": "E", "text": "İhlali gerçekleştiren personelin çalıştığı sermaye piyasası kurumuna prim veya munzam karşılık olarak iade edilir."}
        ],
        "correct_answer": "A",
        "explanation": "TSPB tarafından tahsil edilen disiplin para cezaları Birlik bütçesine irat (gelir) olarak kaydedilir. Bu kaynaklar Birliğin sermaye piyasası eğitimleri, mesleki araştırmaları ve kurumsal giderleri için harcanır."
    },
    "q_1001_master_096": {
        "text": "TSPB Disiplin Yönetmeliği'ne göre bir personel veya üye hakkında 'Sürekli Olarak Faaliyetten Men' cezasının verilmesini gerektiren durum aşağıdakilerden hangisidir?",
        "options": [
            {"key": "A", "text": "Sermaye piyasası faaliyetlerinde zimmet, irtikap, dolandırıcılık veya hileli iflas gibi yüz kızartıcı bir suçtan kesin mahkumiyet alınması"},
            {"key": "B", "text": "Bir takvim yılı içerisinde genel kurula veya eğitim seminerlerine mazeretsiz olarak iki kez katılınmamış olması"},
            {"key": "C", "text": "Birlik aidatlarının vade tarihinden itibaren 15 gün gecikmeyle yatırılmış olması ve gecikme faizinin ödenmemesi"},
            {"key": "D", "text": "Müşterinin vermiş olduğu hisse senedi alım emrinin seans içinde sisteme 5 dakika gecikmeli olarak iletilmesi"},
            {"key": "E", "text": "Sermaye piyasası lisans yenileme eğitim sınavlarının ilk oturumundan geçerli not alınamamış olması"}
        ],
        "correct_answer": "A",
        "explanation": "Sürekli faaliyetten men cezası en ağır disiplin cezasıdır. SPKn kapsamındaki ağır suçlardan (bilgi suistimali, piyasa dolandırıcılığı, güveni kötüye kullanma, sahtecilik, hileli iflas vb.) mahkumiyet veya meslek kurallarının süreklilik arz edecek biçimde ağır ihlali durumlarında verilir."
    },
    "q_1001_master_099": {
        "text": "TSPB Disiplin Yönetmeliği'ne göre disiplin cezasını gerektiren fiilin işlenmesinden itibaren disiplin soruşturması açılması ve ceza tayini bakımından geçerli olan genel zamanaşımı süreleri hangisidir?",
        "options": [
            {"key": "A", "text": "Fiilin işlendiği tarihten itibaren 2 yıl ve her halükarda fiilin gerçekleşmesinden itibaren 5 yıl geçmekle ceza verme yetkisi düşer."},
            {"key": "B", "text": "Fiilin işlendiği tarihten itibaren 6 ay ve her halükarda 1 yıl geçmekle soruşturma açma hakkı zamanaşımına uğrar."},
            {"key": "C", "text": "Disiplin ihlallerinde zamanaşımı süresi uygulanmaz, fiil ne zaman öğrenilirse öğrenilsin süresiz olarak ceza verilebilir."},
            {"key": "D", "text": "Fiilin işlendiği tarihten itibaren 10 yıl ve her halükarda 20 yıl geçmekle disiplin cezası kabiliyeti sona erer."},
            {"key": "E", "text": "Yalnızca para cezalarında 1 yıl, geçici ve sürekli faaliyetten men cezalarında ise 3 yıllık zamanaşımı süresi geçerlidir."}
        ],
        "correct_answer": "A",
        "explanation": "TSPB Disiplin Yönetmeliği uyarınca disiplin cezasını gerektiren fiilin öğrenildiği tarihten itibaren 2 yıl ve her halde fiilin işlendiği tarihten itibaren 5 yıl içinde soruşturma başlatılıp ceza verilmediği takdirde ceza verme yetkisi zamanaşımına uğrar."
    },
    "q_1001_ogretici_013": {
        "text": "6362 sayılı Sermaye Piyasası Kanunu m.106'da düzenlenen 'Bilgi Suistimali' (İçsel Bilgiye Dayalı Ticaret) suçuyla ilgili olarak aşağıdakilerden hangisi YANLIŞTIR?",
        "options": [
            {"key": "A", "text": "İşlemin suç sayılabilmesi için içsel bilginin resmi makamlarca onaylanmış yazılı bir belgeye dayanması zorunludur."},
            {"key": "B", "text": "İhraççıların yöneticileri, denetçileri ve meslekleri gereği bu bilgiye vakıf olan kişiler suçun faili olabilirler."},
            {"key": "C", "text": "Bilginin henüz kamuya açıklanmamış ve fiyatı etkileyebilecek nitelikte somut bir bilgi olması zorunludur."},
            {"key": "D", "text": "Bilgi suistimali suçunda faillere hapis cezasının yanında adli para cezası da birlikte ve kümülatif olarak uygulanır."},
            {"key": "E", "text": "Elde edilen menfaatin iki katından az olmamak üzere adli para cezasına hükmedilmesi kanuni bir zorunluluktur."}
        ],
        "correct_answer": "A",
        "explanation": "İçsel bilginin resmi makam onaylı veya yazılı olması gibi bir şart kesinlikle yoktur; sözlü, yazılı veya elektronik ortamda olması fark etmeksizin henüz kamuya açıklanmamış, somut ve fiyatı etkileme potansiyeline sahip olması suçun oluşumu için yeterlidir."
    },
    "q_1001_ogretici_018": {
        "text": "Türkiye Sermaye Piyasaları Birliği (TSPB) organlarının görev dağılımında 'Disiplin Cezaları' verme yetkisi kural olarak hangi organa aittir?",
        "options": [
            {"key": "A", "text": "Disiplin soruşturmasını Disiplin Kurulu yürütür ve yaptırım kararları Yönetim Kurulu tarafından verilir."},
            {"key": "B", "text": "Tüm disiplin cezaları doğrudan Birlik Genel Kurulu tarafından olağan toplantılarda oy çokluğuyla karara bağlanır."},
            {"key": "C", "text": "Sadece Birlik Başkanı tek başına re'sen her türlü disiplin cezasını vermeye ve infaz ettirmeye tam yetkilidir."},
            {"key": "D", "text": "Disiplin cezaları yalnızca Sermaye Piyasası Kurulu tarafından onaylanmadıkça hiçbir hukuki hüküm ifade etmez."},
            {"key": "E", "text": "Üyeler arasındaki tüm disiplin yaptırımları Bağımsız Denetleme Kurulu kararıyla doğrudan icra edilir."}
        ],
        "correct_answer": "A",
        "explanation": "TSPB teşkilatında Disiplin Kurulu soruşturmayı yürütür ve önerisini sunar; disiplin cezalarının verilmesi yetkisi ise kural olarak Birlik Yönetim Kurulu'na aittir."
    },
    "q_1001_cikmis_019": {
        "text": "Pay Alım Teklifi Tebliği (II-26.1) uyarınca, halka açık bir ortaklıkta yönetim kontrolünün el değiştirmesine rağmen Kurulun zorunlu pay alım teklifinde bulunma yükümlülüğünden muafiyet tanıyabileceği hal hangisidir?",
        "options": [
            {"key": "A", "text": "Ortaklığın finansal güçlük içinde bulunması nedeniyle sermaye yapısının güçlendirilmesi amacıyla pay devrinin yapılması"},
            {"key": "B", "text": "Devralan gerçek kişinin şirketin geçmiş dönem faaliyetlerinde herhangi bir hisse senedi almamış olması"},
            {"key": "C", "text": "Pay devir bedelinin borsa nominal değerinden daha düşük bir fiyatla aracı kurum aracılığıyla ödenmesi"},
            {"key": "D", "text": "Ortaklığın toplam piyasa değerinin Borsa İstanbul BIST 100 endeksindeki medyan değerin altında kalması"},
            {"key": "E", "text": "Yönetim kontrolünü ele geçiren ortağın yurt dışı yerleşik yabancı kurumsal yatırımcı statüsü taşıması"}
        ],
        "correct_answer": "A",
        "explanation": "Pay Alım Teklifi Tebliği m.18 uyarınca; şirketin finansal sıkıntı içinde olması ve şirketin kurtarılması veya sermaye yapısının güçlendirilmesi amacıyla pay devri yapılması durumunda SPK zorunlu pay alım teklifinde bulunma yükümlülüğünden muafiyet verebilir."
    },
    "q_1001_cikmis_023": {
        "text": "6362 sayılı Kanun m.106 kapsamında Bilgi Suistimali suçu nedeniyle hükmedilecek adli para cezası miktarının belirlenmesinde kanunda öngörülen asgari alt sınır nedir?",
        "options": [
            {"key": "A", "text": "Suçun işlenmesi suretiyle elde edilen haksız menfaatin veya önlenen zararın iki katından az olamaz."},
            {"key": "B", "text": "Suç tarihi itibarıyla belirlenmiş olan asgari ücretin yıllık brüt tutarının beş katından az olamaz."},
            {"key": "C", "text": "Halka açık şirketin ödenmiş sermayesinin yüzde birinden ve aktif toplamının binde beşinden az olamaz."},
            {"key": "D", "text": "Suç konusu payların borsadaki işlem hacminin yarısı ve ihraç tavanının üç katı tutarından az olamaz."},
            {"key": "E", "text": "Aracı kurumun sermaye yeterliliği tablosunda yer alan özsermaye yükümlülüğünün onda birinden az olamaz."}
        ],
        "correct_answer": "A",
        "explanation": "SPKn m.106 gereğince bilgi suistimali suçundan dolayı verilecek adli para cezası, suçun işlenmesi suretiyle temin edilen menfaatin (veya önlenen zararın) 2 (iki) katından az olamaz."
    },
    "q_1001_cikmis_035": {
        "text": "Paya Dayalı Kitle Fonlaması Tebliği (III-35/A.2) uyarınca, kitle fonlama platformları aracılığıyla toplanan fonların kampanya süresince muhafaza edildiği ve bloke altında tutulduğu yer neresidir?",
        "options": [
            {"key": "A", "text": "Kurulca belirlenen ve emanet yetkilisi sıfatını haiz Takasbank nezdinde açılan özel bloke hesaplarda"},
            {"key": "B", "text": "Girişimcinin veya girişim şirketinin anlaşmalı olduğu herhangi bir özel ticari banka vadesiz mevduatında"},
            {"key": "C", "text": "Kitle fonlama platformunun kendi tüzel kişilik işletme hesabında ve günlük repoda değerlendirilerek"},
            {"key": "D", "text": "Merkezi Kayıt Kuruluşu'nun fiziki güvenlik kasalarında ve menkul kıymet havuz depolarında"},
            {"key": "E", "text": "Şirket kuruluş işlemlerini yürüten yetkili ticaret sicil müdürlüğünün yediemin banka hesaplarında"}
        ],
        "correct_answer": "A",
        "explanation": "Kitle Fonlaması mevzuatına göre toplanan fonlar, kampanya başarıyla tamamlanıp girişim şirketine devredilene veya başarısız olup yatırımcılara iade edilene kadar emanet yetkilisi olan Takasbank nezdindeki bloke hesaplarda güvence altında tutulur."
    },

    # ----------------------------------------------------
    # MODUL 1003 OVERHAULS (17 questions)
    # ----------------------------------------------------
    "q_1003_master_022": {
        "text": "6362 sayılı Sermaye Piyasası Kanunu m.19 uyarınca halka açık anonim ortaklıkların yapacağı bağış ve yardımlarla ilgili aşağıdakilerden hangisi DOĞRUDUR?",
        "options": [
            {"key": "A", "text": "Yapılacak bağışın sınırı genel kurulca belirlenir ve bağışlar şirket amacını ve kâr dağıtımını aksatamaz."},
            {"key": "B", "text": "Ortaklıklar genel kurul kararı aranmaksızın yönetim kurulu kararıyla diledikleri tutarda bağış yapabilirler."},
            {"key": "C", "text": "Halka açık ortaklıkların herhangi bir kamu veya sosyal kuruluşa bağış ve yardım yapması kanunen tamamen yasaktır."},
            {"key": "D", "text": "Yapılan tüm bağışlar SPK tarafından onaylanmadıkça mali tablolarda gider kalemi olarak muhasebeleştirilemez."},
            {"key": "E", "text": "Bağış ve yardım tutarı ortaklığın ödenmiş sermayesinin yüzde ellisini aşmadığı sürece genel kurula bilgi verilmez."}
        ],
        "correct_answer": "A",
        "explanation": "SPKn m.19 uyarınca halka açık ortaklıklar tarafından yapılacak bağış ve yardımın sınırının genel kurul tarafından belirlenmesi, esas sözleşmede hüküm bulunması, bağışın ortaklık amacını aksatmayacak nitelikte olması ve kâr payı dağıtımını engellememesi şarttır. Yapılan bağışlar genel kurulda ortakların bilgisine sunulur ve KAP'ta açıklanır."
    },
    "q_1003_master_024": {
        "text": "Bir anonim ortaklıkta 'Pay Bölünmesi' (Hisse Bölünmesi / Stock Split - örneğin 1'e 2 bölünme) gerçekleştiğinde şirketin finansal yapısı ve hisse performansı üzerinde aşağıdaki etkilerden hangisi meydana gelir?",
        "options": [
            {"key": "A", "text": "Pay sayısı artarken pay başına piyasa fiyatı aynı oranda düşer; şirketin toplam piyasa değeri ve özkaynakları değişmez."},
            {"key": "B", "text": "Şirketin çıkarılmış sermayesi iki katına çıkar ve şirketin kasasına yeni nakit sermaye girişi sağlanır."},
            {"key": "C", "text": "Pay sahiplerinin şirketteki ortaklık payı ve oy hakkı oranı yarı yarıya azalarak imtiyazlı paylara geçer."},
            {"key": "D", "text": "Şirketin piyasa değeri anında ikiye katlanır ve hisse senetleri BIST 30 endeksine otomatik olarak dahil edilir."},
            {"key": "E", "text": "Şirketin ödenmiş sermayesi azalır ve aradaki fark dağıtılmamış geçmiş yıl kârları hesabına aktarılır."}
        ],
        "correct_answer": "A",
        "explanation": "Hisse bölünmesinde toplam piyasa değeri, ortakların sermaye payı oranı ve şirketin özkaynakları değişmez. Sadece pay sayısı artar, pay fiyatı oransal olarak düşer. Bu işlem hissenin piyasadaki likiditesini ve küçük yatırımcılar için erişilebilirliğini artırır."
    },
    "q_1003_master_025": {
        "text": "Borsa uygulamasında 'Ters Pay Bölünmesi' (Hisse Birleştirme / Reverse Stock Split - örneğin 10 payın 1 paya dönüştürülmesi) işleminin temel finansal amacı aşağıdakilerden hangisidir?",
        "options": [
            {"key": "A", "text": "Payın birim fiyatını yükselterek aşırı düşük fiyatlı hisse görünümünden çıkmak ve piyasa likiditesini disipline etmek"},
            {"key": "B", "text": "Şirketin toplam piyasa değerini ve kayıtlı sermaye tavanını genel kurul kararı olmadan doğrudan artırmak"},
            {"key": "C", "text": "Şirkete yeni stratejik ortaklar alabilmek amacıyla azınlık ortakların pay sahipliği haklarını tasfiye etmek"},
            {"key": "D", "text": "Şirketin geçmiş yıl zararlarını tamamen kapatmak ve ortaklara nakit sermaye iadesi gerçekleştirmek"},
            {"key": "E", "text": "Şirket paylarının borsa işlem sırasının kapatılarak borsa kotundan tamamen çıkarılmasını sağlamak"}
        ],
        "correct_answer": "A",
        "explanation": "Ters hisse bölünmesinde (hisse birleştirme) pay sayısı azaltılırken hisse fiyatı oransal olarak artırılır. Şirketin piyasa değeri değişmez. Temel amaç hisse fiyatının çok düşük (kuruşlu) seviyelere inmesini önlemek, kurumsal yatırımcı ilgisini artırmak ve borsa asgari fiyat kotasyon kurallarını karşılamaktır."
    },
    "q_1003_master_032": {
        "text": "Paya Dönüştürülebilir Tahvil (PDT) ile Değiştirilebilir Tahvil (DET) arasındaki en temel ayırt edici fark aşağıdakilerden hangisidir?",
        "options": [
            {"key": "A", "text": "PDT ihraççı şirketin kendi paylarına dönüşürken; DET ihraççının portföyündeki başka bir şirketin paylarıyla değiştirilir."},
            {"key": "B", "text": "PDT yalnızca yabancı para cinsinden ihraç edilebilirken; DET sadece Türk Lirası cinsinden ve devlet garantili ihraç edilir."},
            {"key": "C", "text": "PDT sahibine genel kurulda oy hakkı sağlarken; DET sahibi hiçbir zaman temettü veya faiz getirisi elde edemez."},
            {"key": "D", "text": "PDT'de vade süresi en fazla 1 yıl olabilirken; DET'lerde vade süresinin asgari 10 yıl olması kanuni zorunluluktur."},
            {"key": "E", "text": "PDT yalnızca bankalar tarafından ihraç edilirken; DET sadece varlık kiralama şirketleri tarafından tedavüle çıkarılır."}
        ],
        "correct_answer": "A",
        "explanation": "Paya Dönüştürülebilir Tahvil (PDT), ihraççı şirketin sermaye artırımı yoluyla ihraç edeceği KENDİ paylarına dönüştürme hakkı verir. Değiştirilebilir Tahvil (DET) ise ihraççının portföyünde bulunan BAŞKA bir ortaklığın (örneğin iştirakinin veya borsa kotundaki başka bir şirketin) paylarıyla değiştirme hakkı verir."
    },
    "q_1003_master_037": {
        "text": "Hazine ve Maliye Bakanlığı tarafından ihraç edilen Enflasyona Endeksli Devlet Tahvillerinin (TÜFE'ye Endeksli Tahviller) getiri ve kupon yapısı hakkında aşağıdakilerden hangisi DOĞRUDUR?",
        "options": [
            {"key": "A", "text": "Anapara ve kupon ödemeleri tüketici fiyat endeksindeki (TÜFE) değişim oranında güncellenerek reel getiri korunur."},
            {"key": "B", "text": "Tahvilin anaparası sabit kalırken kupon ödemeleri yalnızca ABD Doları döviz kurundaki artışa göre hesaplanır."},
            {"key": "C", "text": "Enflasyon negatif çıktığında (deflasyon durumunda) yatırımcının anapara tutarı nominal değerinin altına indirilir."},
            {"key": "D", "text": "Kupon faiz oranı her altı ayda bir BIST 100 endeksinin getiri performansına endekslenerek belirlenir."},
            {"key": "E", "text": "Vade sonunda anapara geri ödemesi yapılmaz, sadece dönemsel sabit kupon getirisi ödenerek tahvil itfa edilir."}
        ],
        "correct_answer": "A",
        "explanation": "TÜFE'ye endeksli tahvillerde nominal anapara tutarı enflasyon (TÜFE) oranında dönemsel olarak endekslenir. Kupon ödemeleri ise enflasyonla güncellenmiş bu anapara üzerinden reel kupon oranı uygulanarak hesaplanır; böylece yatırımcı hem anaparasını enflasyona karşı korur hem de reel getiri elde eder."
    },
    "q_1003_master_039": {
        "text": "SPK'nın Yeşil Borçlanma Aracı Rehberi uyarınca ihraç edilen bir 'Yeşil Borçlanma Aracı'ndan (Green Bond) elde edilen fonların kullanımı ve denetimi ile ilgili hangisi DOĞRUDUR?",
        "options": [
            {"key": "A", "text": "Fonlar yalnızca rehberde tanımlanan yeşil/çevre dostu projelerde kullanılır ve bağımsız İkinci Taraf Görüşü alınır."},
            {"key": "B", "text": "İhraçtan sağlanan fonlar şirketin kısa vadeli işletme sermayesi veya genel yönetim giderleri için serbestçe harcanabilir."},
            {"key": "C", "text": "Yeşil tahvil ihraç eden şirketler Kurul kaydından ve Kamuyu Aydınlatma Platformu bildirimlerinden muaf tutulurlar."},
            {"key": "D", "text": "Elde edilen gelirin en az %90'ının fosil yakıt veya geleneksel enerji santrali yatırımlarına yönlendirilmesi zorunludur."},
            {"key": "E", "text": "Yeşil borçlanma araçları yalnızca kamu kurumları ve belediyeler tarafından ihraç edilebilir, özel şirketler ihraç edemez."}
        ],
        "correct_answer": "A",
        "explanation": "Yeşil Borçlanma Araçlarında (Green Bonds) ihraçtan elde edilecek fonların tamamı yeşil/sürdürülebilir çevre projelerinin finansmanında kullanılmak zorundadır. Şirket bir Yeşil Borçlanma Çerçeve Belgesi hazırlar ve bağımsız bir değerlendirme kuruluşundan 'İkinci Taraf Görüşü' (Second Party Opinion) alarak KAP'ta ilan eder."
    },
    "q_1003_master_041": {
        "text": "İpotek Teminatlı Menkul Kıymetler (İTMK) ile Varlık Teminatlı Menkul Kıymetler (VTMK) arasındaki teminat havuzu ve ihraççı sorumluluğu açısından temel kural aşağıdakilerden hangisidir?",
        "options": [
            {"key": "A", "text": "İTMK'da teminat havuzunu ipotekli konut ve ticari krediler oluşturur; her ikisinde de ihraççının genel sorumluluğu esastır."},
            {"key": "B", "text": "İTMK bilanço dışı bir fon yapısıyla ihraç edilirken; VTMK yalnızca bankaların kendi bilançosu üzerinden çıkarılır."},
            {"key": "C", "text": "İTMK'da yatırımcı temerrüt durumunda teminat havuzuna başvuramaz, sadece ihraççının tasfiye masasına dahil olur."},
            {"key": "D", "text": "VTMK sadece kamu bankalarınca çıkarılabilirken; İTMK'yı yalnızca Tasfiye Halindeki Emlak Bankası ihraç edebilir."},
            {"key": "E", "text": "İTMK ihraçlarında teminat uyum sorumlusu atanması ihtiyaridir, VTMK'da ise SPK uzmanı kayyum olarak atanır."}
        ],
        "correct_answer": "A",
        "explanation": "İTMK ve VTMK teminatlı borçlanma araçlarıdır (covered bonds). Teminat havuzu ihraççının bilançosunda ayrı bir teminat kaydıyla takip edilir. İhraççı tüm malvarlığıyla birinci derecede sorumludur; teminat havuzu ise ihraççı iflas etse dahi sadece İTMK/VTMK yatırımcılarının alacaklarına tahsis edilmiştir (kamusal koruma). İTMK havuzu gayrimenkul rehinli alacaklardan oluşur."
    },
    "q_1003_master_047": {
        "text": "Değişken faizli borçlanma araçlarında (tahvil ve bonolarda) yatırımcıya ödenecek dönemsel kupon faiz oranı hangi esasa göre belirlenir?",
        "options": [
            {"key": "A", "text": "Önceden belirlenmiş bir referans faiz oranına (TLREF, DİBS getirisi vb.) sabit bir ek getiri marjı eklenerek belirlenir."},
            {"key": "B", "text": "İhraççı şirketin ilgili dönemde elde ettiği net kârlılık oranının yönetim kurulunca onaylanan yüzdesi olarak ödenir."},
            {"key": "C", "text": "Borsa İstanbul BIST 100 endeksinin altı aylık nominal artış oranına eşit olacak şekilde otomatik olarak hesaplanır."},
            {"key": "D", "text": "Türkiye Cumhuriyet Merkez Bankası'nın yıl sonu resmi TÜFE hedefi ile cari politika faizinin aritmetik ortalamasıdır."},
            {"key": "E", "text": "İhraç anında belirlenen sabit bir faiz oranı olup vade sonuna kadar piyasa koşullarından etkilenmeksizin değişmez."}
        ],
        "correct_answer": "A",
        "explanation": "Değişken faizli borçlanma araçlarında kupon oranı, objektif ve piyasada şeffafça ilan edilen bir referans faize (örneğin TLREF - Türk Lirası Gecelik Referans Faiz Oranı veya Hazine gösterge faizi) ihraç anında belirlenen bir ek getiri (spread / prim) eklenmesi suretiyle periyodik kupon dönemlerinde yeniden hesaplanır."
    },
    "q_1003_master_050": {
        "text": "Yatırımcı Tazmin Merkezi'nin (YTM) sermaye piyasasında işlem gören özel sektör tahvillerine ilişkin tazmin kapsamı hakkında aşağıdakilerden hangisi DOĞRUDUR?",
        "options": [
            {"key": "A", "text": "YTM sadece saklamadaki hisse ve nakit teslim yükümlülüğünü tazmin eder; tahvil ihraççısının iflas ve temerrüt riskini tazmin etmez."},
            {"key": "B", "text": "İflas eden veya kupon ödemeyen özel sektör şirketlerinin tahvilleri YTM tarafından 2026 yılı yasal limitine kadar tamamen ödenir."},
            {"key": "C", "text": "Özel sektör tahvillerinin anapara ve faiz ödemeleri Hazine garantisi altında olup doğrudan YTM bütçesinden karşılanır."},
            {"key": "D", "text": "YTM yalnızca yabancı para cinsinden eurobond ihraçlarını tazmin eder, TL borçlanma araçlarını kapsam dışı bırakır."},
            {"key": "E", "text": "Aracı kurum batsa dahi müşterinin hesabındaki tahviller Merkezi Kayıt Kuruluşu tarafından piyasa fiyatından satın alınır."}
        ],
        "correct_answer": "A",
        "explanation": "Yatırımcı Tazmin Merkezi (YTM), yatırım kuruluşlarının yatırımcılara ait nakit ve sermaye piyasası araçlarını (hisse, tahvil vb.) tevdi ve teslim yükümlülüklerini yerine getirememesi (kurumun batması/sahteciliği) durumunda devreye girer. Bir şirketin ihraç ettiği tahvilin vadesinde ödenmemesi bir piyasa ve kredi riskidir; YTM bu tür borç ödememe / batık tahvil risklerini ASLA tazmin etmez."
    },
    "q_1003_master_066": {
        "text": "Sermaye Piyasası Kurulu'nun Varantlar Tebliği (VII-128.3) çerçevesinde 'Aracı Kuruluş Varantı'nın hukuki tanımı ve niteliği aşağıdakilerden hangisinde tam olarak verilmiştir?",
        "options": [
            {"key": "A", "text": "Sahibine belirli bir dayanak varlığı önceden belirlenen fiyattan alma ya da satma hakkı veren menkul kıymet niteliğinde sermaye piyasası aracıdır."},
            {"key": "B", "text": "İhraççı şirketin esas sermayesini temsil eden ve hamiline genel kurulda oy kullanma ile kâr payı talep etme yetkisi veren ortaklık payıdır."},
            {"key": "C", "text": "İki taraf arasında ileri bir tarihte fiziki mal teslimi yapılmasını kanunen zorunlu kılan tezgahüstü bir türev sözleşmedir."},
            {"key": "D", "text": "Yatırımcısına her halükarda anapara garantisi ve sabit dönemsel kupon faizi ödemeyi taahhüt eden bir borçlanma senedidir."},
            {"key": "E", "text": "Fon kurucusunun portföyündeki menkul kıymetleri temsil eden ve borsa dışında alınıp satılan katılma belgesidir."}
        ],
        "correct_answer": "A",
        "explanation": "Aracı kuruluş varantı; sahibine, önceden belirlenen bir vadede veya vadeye kadar, dayanak varlığı (pay, endeks, emtia vb.) önceden belirlenen fiyattan (kullanım fiyatı) alma veya satma HAKKI veren, kaydileştirilmiş menkul kıymet niteliğindeki sermaye piyasası aracıdır. Alıcı için bir hak, ihraççı için yükümlülüktür."
    },
    "q_1003_master_077": {
        "text": "Borsa İstanbul bünyesinde işlem gören aracı kuruluş varantlarında vade sonu kullanım ve uzlaşma yöntemi kural olarak nasıl gerçekleştirilir?",
        "options": [
            {"key": "A", "text": "Vade sonunda varant kârda ise kullanım otomatik olarak gerçekleşir ve aradaki fark nakdi uzlaşı ile hesaba aktarılır."},
            {"key": "B", "text": "Vade sonunda dayanak hisse senetleri veya emtialar yatırımcının adresine fiziki teslimat yoluyla ulaştırılır."},
            {"key": "C", "text": "Yatırımcı vade sonundan 30 gün önce ihraççıya taahhütlü yazılı başvuru yapmadıkça varant hükümsüz kalır."},
            {"key": "D", "text": "Vade dolduğunda kârda olan varantların yerine yatırımcıya otomatik olarak yeni vadeli varantlar tahsis edilir."},
            {"key": "E", "text": "Vade sonu uzlaşması sadece Borsa İstanbul Yönetim Kurulu kararıyla belirlenen hisse takas havuzuyla yapılır."}
        ],
        "correct_answer": "A",
        "explanation": "BIST'te işlem gören aracı kuruluş varantlarında uzlaşma 'Nakdi Uzlaşı' (Cash Settlement) esasına göre yapılır. Fiziki teslimat yapılmaz. Vade sonu gösterge fiyatı ile kullanım fiyatı arasındaki fark (asli değer), çarpan dikkate alınarak otomatik olarak hesaplanır ve Takasbank aracılığıyla yatırımcının hesabına nakit olarak ödenir."
    },
    "q_1003_master_083": {
        "text": "Yatırım Fonlarına İlişkin Esaslar Tebliği (III-52.1) uyarınca 'Para Piyasası Fonları'nın (PPF) portföy yapısı ve vade kısıtlamaları hakkında aşağıdakilerden hangisi DOĞRUDUR?",
        "options": [
            {"key": "A", "text": "Portföyün günlük olarak hesaplanan ağırlıklı ortalama vadesi en fazla 45 gün olup, vadesine 184 günden uzun kalan araç alınamaz."},
            {"key": "B", "text": "Portföyünün en az %80'i BIST 100 endeksine dahil ortaklık paylarından ve borsa yatırım fonlarından oluşmak zorundadır."},
            {"key": "C", "text": "Fon portföyünün ortalama vadesi serbestçe belirlenir ve en az 3 yıl vadeli özel sektör tahvillerine yatırım yapılır."},
            {"key": "D", "text": "Fon portföyüne yalnızca yabancı ülke hazinelerinin ihraç ettiği eurobondlar ve altın sertifikaları dahil edilebilir."},
            {"key": "E", "text": "Portföyündeki varlıkların tamamının vadesine en az 365 gün kalmış uzun vadeli ipotekli tahvillerden oluşması şarttır."}
        ],
        "correct_answer": "A",
        "explanation": "Para Piyasası Fonları; portföyünün tamamı devamlı olarak vadesine en fazla 184 gün kalmış likit para ve sermaye piyasası araçlarından oluşan ve portföyünün günlük hesaplanan ağırlıklı ortalama vadesi en fazla 45 gün olan fonlardır. Bu sayede faiz ve piyasa riski son derece düşüktür."
    },
    "q_1003_master_097": {
        "text": "T.C. Hazine ve Maliye Bakanlığı Darphane ve Damga Matbaası Genel Müdürlüğü tarafından ihraç edilen ve Borsa İstanbul'da işlem gören Darphane Altın Sertifikası (ALTIN.S1) ile ilgili hangisi DOĞRUDUR?",
        "options": [
            {"key": "A", "text": "Her bir sertifika 0,01 gram altını temsil eder; borsa seansında işlem görür ve şartları sağlayana fiziki altın dönüşüm hakkı tanır."},
            {"key": "B", "text": "Sertifikalar yalnızca kurumsal bankalara satılır ve hiçbir şekilde bireysel yatırımcılar tarafından alınıp satılamaz."},
            {"key": "C", "text": "Vade sonunda fiziki dönüşüm imkanı bulunmayıp yalnızca TCMB döviz alış kuru üzerinden nakit ödeme yapılır."},
            {"key": "D", "text": "Altın sertifikası sahiplerine her ay Darphane tarafından çeyrek altın cinsinden fiziki kâr payı dağıtılır."},
            {"key": "E", "text": "Sertifikaların alım-satımında kazanç üzerinden %20 oranında stopaj kesintisi uygulanması zorunludur."}
        ],
        "correct_answer": "A",
        "explanation": "Darphane Altın Sertifikası (ALTIN.S1), Borsa İstanbul Pay Piyasası Emtia Pazarı'nda işlem görür. Her pay 0,01 gram (saflığı 995/1000) altını temsil eder. Yatırımcılar borsa işlemlerinde stopajdan muaf olup, belirlenen asgari miktara (Darphane şartlarına) ulaştıklarında sertifikalarını Darphane'den fiziki altına dönüştürme hakkına sahiptirler."
    },
    "q_1003_master_098": {
        "text": "Yurt dışı pay piyasalarında işlem gören yabancı hisse senetlerine yatırım yapan yerli bir yatırımcının karşı karşıya olduğu temel risk türleri hangi seçenekte doğru olarak gruplandırılmıştır?",
        "options": [
            {"key": "A", "text": "Piyasa (Fiyat) Riski, Kur (Döviz) Riski, Ülke (Politik) Riski ve Transfer (Likidite) Riski"},
            {"key": "B", "text": "Yalnızca Vergi Harcı Riski ve Ticaret Sicil Tescil Ücreti Artış Riski"},
            {"key": "C", "text": "Sadece Borsa İstanbul Temerrüt Riski ve Yerel Enflasyon Endeksleme Riski"},
            {"key": "D", "text": "Yalnızca Şirket Kuruluş Sözleşmesi Fesih Riski ve Kıdem Tazminatı Riski"},
            {"key": "E", "text": "Yalnızca Takasbank Takas Havuzu Üyelik İptali ve Munzam Karşılık Riski"}
        ],
        "correct_answer": "A",
        "explanation": "Yurt dışı menkul kıymet yatırımlarında yatırımcı; şirketin hisse fiyat dalgalanması (piyasa riski), yabancı para biriminin değer kaybı (kur riski), yatırım yapılan ülkedeki mevzuat/hükümet değişiklikleri (ülke/politik risk) ve fonların transferinde yaşanabilecek engeller (transfer riski) ile karşı karşıyadır."
    },
    "q_1003_ogretici_011": {
        "text": "6362 sayılı Sermaye Piyasası Kanunu uyarınca, halka açık anonim ortaklıkların nama ve hamiline yazılı paylarının Merkezi Kayıt Kuruluşu (MKK) nezdinde devri ve hak sahipliğinin ispatı nasıl gerçekleşir?",
        "options": [
            {"key": "A", "text": "Paylar MKK nezdinde hak sahipleri adına kayden izlenir ve pay devirleri kaydi sistemde hesaplar arası aktarımla tamamlanır."},
            {"key": "B", "text": "Hisselerin geçerli olabilmesi için her pay devrinde şirket yönetim kurulunun onaylı karar alması şarttır."},
            {"key": "C", "text": "Hamiline yazılı paylar fiziki kupon şeklinde basılır ve elden teslim edilerek şirket pay defterine işlenir."},
            {"key": "D", "text": "Borsa İstanbul'da işlem gören paylar ticaret mahkemesinden tasdikli devir senedi düzenlenmedikçe devredilemez."},
            {"key": "E", "text": "Müşterinin payları aracı kurumun kendi mülkiyetine geçer ve yatırımcı sadece aracı kuruma karşı alacaklı sayılır."}
        ],
        "correct_answer": "A",
        "explanation": "SPKn m.13 uyarınca sermaye piyasası araçları MKK nezdinde elektronik ortamda ve hak sahipleri adına kayden ihraç edilir ve izlenir. Payların devri kaydi sistemde hesaplar arası virman/aktarım ile hukuki geçerlilik kazanır; fiziki senet basımı veya pay defterine tescil zorunluluğu yoktur."
    },
    "q_1003_cikmis_020": {
        "text": "Borsa Yatırım Fonları (BYF / ETF) ile Geleneksel Yatırım Fonlarının alım-satım mekanizması ve fiyat oluşumu arasındaki farklarla ilgili hangisi DOĞRUDUR?",
        "options": [
            {"key": "A", "text": "BYF payları borsa seansında arz-talebe göre anlık fiyatla işlem görürken, geleneksel fonlar günde bir kez hesaplanan pay fiyatından işlem görür."},
            {"key": "B", "text": "Geleneksel yatırım fonları borsa emir defterinde sürekli müzayede ile satılırken, BYF payları sadece kurucu bankadan temin edilir."},
            {"key": "C", "text": "BYF'lerde portföy yöneticisi aktif olarak piyasayı yenmeye çalışırken, geleneksel fonlar sadece bir borsa endeksini pasif izler."},
            {"key": "D", "text": "Geleneksel fonlarda alım-satım emirleri gün boyu anlık gerçekleşirken, BYF'lerde takas süresi en az 30 iş günüdür."},
            {"key": "E", "text": "BYF paylarını sadece kurumsal nitelikli yatırımcılar alabilirken, geleneksel fonları yalnızca yabancı uyruklu kişiler alabilir."}
        ],
        "correct_answer": "A",
        "explanation": "Borsa Yatırım Fonları (ETF), borsada hisse senedi gibi işlem görür; fiyatı seans içinde piyasadaki arz ve talebe göre anlık olarak belirlenir. Geleneksel fonlarda ise fon toplam değerinin pay sayısına bölünmesiyle günde bir kez pay fiyatı açıklanır ve işlemler TEFAS/kurucu aracılığıyla bu fiyattan gerçekleşir."
    },
    "q_1003_cikmis_025": {
        "text": "Sermaye Piyasası Araçları mevzuatı çerçevesinde, Varlığa Dayalı Menkul Kıymetler (VDMK) ile Varlık Teminatlı Menkul Kıymetler (VTMK) arasındaki bilançoda taşınma ve ihraç yapısı farkı nedir?",
        "options": [
            {"key": "A", "text": "VDMK'da varlıklar bilançodan çıkarılarak Fon portföyüne aktarılır (bilanço dışı); VTMK'da ise teminat havuzu ihraççının bilançosunda kalır."},
            {"key": "B", "text": "VDMK sadece ipotekli konut kredilerine dayanırken; VTMK her türlü altın ve döviz rezervine dayalı olarak ihraç edilir."},
            {"key": "C", "text": "VDMK ihraçlarında ihraççının tüm malvarlığı sorumlu tutulurken; VTMK ihraçlarında ihraççının hiçbir sorumluluğu bulunmaz."},
            {"key": "D", "text": "VDMK sadece kamu kurumları tarafından çıkarılırken; VTMK yalnızca portföy yönetim şirketlerince fon şeklinde kurulur."},
            {"key": "E", "text": "VDMK sahipleri şirketin genel kurulunda oy kullanabilirken; VTMK sahiplerine sadece sabit kâr payı hakkı tanınır."}
        ],
        "correct_answer": "A",
        "explanation": "VDMK ihraçlarında varlıklar, kaynak kuruluşun bilançosundan çıkarılarak (off-balance sheet) SPK onaylı Varlık Finansmanı Fonu'na (VFF) devredilir ve menkul kıymetleştirilir. VTMK'da ise varlıklar ihraççının kendi bilançosunda kalmaya devam eder (on-balance sheet); ancak kanun gereği bu varlıklar üzerinde yatırımcılar lehine ayrılmış imtiyazlı bir teminat havuzu oluşturulur."
    },

    # ----------------------------------------------------
    # FIX FOR q_1012_ogretici_011 (replace 'Her cuma akşamı')
    # ----------------------------------------------------
    "q_1012_ogretici_011": {
        "text": "Borsa İstanbul Pay Piyasası'nda gerçekleştirilen hisse senedi alım satım işlemlerinin takas ve mutabakat süresi kural olarak ne zamandır?",
        "options": [
            {"key": "A", "text": "İşlem gününü izleyen ikinci iş günü (T+2)"},
            {"key": "B", "text": "İşlem gününü izleyen ilk iş günü (T+1)"},
            {"key": "C", "text": "İşlemin yapıldığı gün anında (T+0)"},
            {"key": "D", "text": "İşlem gününü izleyen üçüncü iş günü (T+3)"},
            {"key": "E", "text": "Haftalık takas mutabakat periyotları sonunda topluca"}
        ],
        "correct_answer": "A",
        "explanation": "Borsa İstanbul Pay Piyasası'nda hisse senedi alım satım işlemlerinin nakit ve menkul kıymet takası kural olarak T+2'de (işlem gününü takip eden ikinci iş günü) Takasbank nezdinde çok taraflı netleştirme ile gerçekleştirilir."
    }
}

# ----------------------------------------------------
# 10 BRAND NEW HIGH-YIELD SUPPLEMENTAL EXAM QUESTIONS
# ----------------------------------------------------
NEW_QUESTIONS = [
    # Modül 1001: 5 Questions
    {
        "id": "q_1001_master_101",
        "module_id": "1001",
        "number": 101,
        "source": "master",
        "topic": "Halka Arz ve İzahname",
        "chapter": "Bölüm 2: Sermaye Piyasası Araçlarının Satışı ve Halka Arz",
        "text": "Sermaye Piyasası Araçlarının Satışı Tebliği (II-5.2) uyarınca, halka arz yoluyla pay satışında talep toplama yöntemleri ve talep toplama süresi ile ilgili aşağıdaki kurallardan hangisi DOĞRUDUR?",
        "options": [
            {"key": "A", "text": "Talep toplama süresi 2 iş gününden az, 30 iş gününden fazla olamaz ve belirlenen tarihler izahnamede ilan edilir."},
            {"key": "B", "text": "Talep toplama süresi kural olarak 1 gün olup Kurul izni olsa dahi hiçbir şekilde uzatılamaz veya kısaltılamaz."},
            {"key": "C", "text": "Borsada satış yönteminde talep toplama süresi en az 10 iş günü olmak zorunda olup fiyat serbest marjla belirlenir."},
            {"key": "D", "text": "Sabit fiyatla talep toplama yönteminde yatırımcılar talep formuna istedikleri farklı fiyat tekliflerini yazabilirler."},
            {"key": "E", "text": "Talep toplama süresi içerisinde toplanan talepler ihraç tutarını aşsa dahi ek satış hakkının kullanılması kanunen yasaktır."}
        ],
        "correct_answer": "A",
        "explanation": "II-5.2 Tebliği m.11 uyarınca payların halka arzında talep toplama süresi 2 iş gününden az ve 30 iş gününden fazla olamaz. Talep toplama yöntemleri: 1. Sabit fiyatla talep toplama, 2. Fiyat teklifi alma yoluyla talep toplama, 3. Fiyat aralığı yoluyla talep toplama ve 4. Borsada satış yöntemidir.",
        "trap": "Talep toplama süresinin alt sınırı 2 iş günü, üst sınırı 30 iş günüdür. Genellikle piyasada 2-3 gün uygulanması kanuni üst sınırın 30 iş günü olduğu gerçeğini değiştirmez.",
        "difficulty": "orta",
        "tags": ["halka arz", "talep toplama", "mevzuat"]
    },
    {
        "id": "q_1001_master_102",
        "module_id": "1001",
        "number": 102,
        "source": "master",
        "topic": "İdari Para Cezaları ve Zamanaşımı",
        "chapter": "Bölüm 5: İdari ve Cezai Sorumluluk",
        "text": "6362 sayılı Sermaye Piyasası Kanunu'nda düzenlenen İdari Para Cezaları (İPC) ve bu cezaların tabi olduğu zamanaşımı hükümleri hakkında aşağıdakilerden hangisi DOĞRUDUR?",
        "options": [
            {"key": "A", "text": "Kurulun idari para cezası verme yetkisi, ihlale yol açan fiilin işlendiği tarihten itibaren 5 yıl geçmekle zamanaşımına uğrar."},
            {"key": "B", "text": "İdari para cezası kararlarına karşı sadece Türkiye Sermaye Piyasaları Birliği Disiplin Kurulu'na itiraz edilebilir."},
            {"key": "C", "text": "İdari para cezalarında zamanaşımı süresi 20 yıl olup süre hiçbir tebligat veya işlemle kesilemez."},
            {"key": "D", "text": "Kurul tarafından verilen idari para cezaları kesin olup hiçbir idari yargı merciinde dava konusu yapılamaz."},
            {"key": "E", "text": "Tüzel kişiler hakkında idari para cezası uygulandığında şirket yöneticilerine ayrıca hiçbir idari yaptırım uygulanamaz."}
        ],
        "correct_answer": "A",
        "explanation": "SPKn m.105 uyarınca ve Kabahatler Kanunu genel ilkeleri çerçevesinde; Kurulun idari para cezası verme yetkisi, kabahatin işlendiği tarihten itibaren 5 yıllık zamanaşımı süresine tabidir. Süreklilik arz eden fiillerde zamanaşımı fiilin sona erdiği günden itibaren işlemeye başlar.",
        "trap": "SPK idari para cezalarında zamanaşımı süresi 5 yıldır. Dava açma süresi ise kararın tebliğinden itibaren 30 gündür (İdare Mahkemesi).",
        "difficulty": "zor",
        "tags": ["idari para cezası", "zamanaşımı", "kabahatler"]
    },
    {
        "id": "q_1001_master_103",
        "module_id": "1001",
        "number": 103,
        "source": "master",
        "topic": "Kitle Fonlaması",
        "chapter": "Bölüm 2: Halka Arz ve İhraçlar",
        "text": "Kitle Fonlaması Tebliği (III-35/A.2) uyarınca, nitelikli yatırımcı olmayan gerçek kişilerin paya veya borçlanmaya dayalı kitle fonlamasında yapabilecekleri azami yıllık yatırım sınırları hakkında hangisi DOĞRUDUR?",
        "options": [
            {"key": "A", "text": "Nitelikli olmayan yatırımcılar için yıllık sınır belirlenmiş olup beyan edilen net gelirin %10'unu aşamaz; nitelikli yatırımcılara sınır uygulanmaz."},
            {"key": "B", "text": "Gerçek kişilerin kitle fonlaması platformlarına yapabilecekleri toplam yatırım tutarı ömür boyu 50.000 TL ile sınırlıdır."},
            {"key": "C", "text": "Yalnızca şirket kurucuları ve birinci derece akrabaları kitle fonlama kampanyalarına fon sağlayıcı olarak katılabilir."},
            {"key": "D", "text": "Nitelikli yatırımcılar dahil hiçbir gerçek veya tüzel kişi bir takvim yılında birden fazla kitle fonlama projesine katılamaz."},
            {"key": "E", "text": "Kitle fonlaması yoluyla fon toplayan girişim şirketlerinin 1 yıl içinde borsaya kote olma zorunluluğu bulunmaktadır."}
        ],
        "correct_answer": "A",
        "explanation": "Kitle Fonlaması Tebliği uyarınca nitelikli yatırımcı olmayan gerçek kişiler, bir takvim yılı içinde Kurulca belirlenen parasal limite (veya gelir beyanında bulunurlarsa beyan edilen yıllık net gelirin azami %10'una) kadar yatırım yapabilirler. Nitelikli yatırımcılar için ise bu yatırım üst limitleri uygulanmaz.",
        "trap": "Nitelikli yatırımcılar için herhangi bir yatırım üst sınırı uygulanmaz. Nitelikli olmayan yatırımcılar için ise yıllık azami sınır gelir beyanının %10'u ile sınırlandırılabilir.",
        "difficulty": "orta",
        "tags": ["kitle fonlaması", "nitelikli yatırımcı", "yatırım limiti"]
    },
    {
        "id": "q_1001_master_104",
        "module_id": "1001",
        "number": 104,
        "source": "master",
        "topic": "Önemli Nitelikteki İşlemler",
        "chapter": "Bölüm 3: Ortaklık Hakları ve Kurumsal Yönetim",
        "text": "Önemli Nitelikteki İşlemler ve Ayrılma Hakkı Tebliği (II-23.3) çerçevesinde, halka açık ortaklıklarda ayrılma hakkı kullanım fiyatının belirlenmesi ile ilgili kural aşağıdakilerden hangisidir?",
        "options": [
            {"key": "A", "text": "İşlemin ilk kamuya açıklandığı tarihten önceki son 1 aylık veya 6 aylık borsa düzeltilmiş ağırlıklı ortalama fiyatı esas alınır."},
            {"key": "B", "text": "Şirket yönetim kurulunun kendi takdirine bağlı olarak belirlediği ve genel kurulun onayladığı defter değeri uygulanır."},
            {"key": "C", "text": "Hisselerin borsa nominal değeri olan 1 TL üzerinden hesaplanan sabit tutar yatırımcılara nakit olarak ödenir."},
            {"key": "D", "text": "Ayrılma hakkı kullanım fiyatı hiçbir şekilde bağımsız denetimden geçmiş hisse başına özkaynak değerinin altına inemez."},
            {"key": "E", "text": "Pay sahipleri ayrılma hakkını kullanırken son 5 yılın temettü verimi ortalamasını kullanım bedeline re'sen eklerler."}
        ],
        "correct_answer": "A",
        "explanation": "II-23.3 Tebliği uyarınca ayrılma hakkı kullanım fiyatı; işlemin ilk kez kamuya açıklandığı tarihten önceki, payları Yıldız Pazar'da işlem gören ortaklıklar için son 1 aylık; diğer pazarlarda işlem görenler için son 6 aylık dönemde borsada oluşan düzeltilmiş ağırlıklı ortalama fiyatların aritmetik ortalaması olarak hesaplanır.",
        "trap": "Ayrılma hakkı kullanım fiyatı nominal veya defter değeri değil, işlemin ilk kamuya duyurulduğu tarihten önceki borsa düzeltilmiş ağırlıklı ortalama fiyatıdır (Yıldız Pazar'da 1 ay, diğerlerinde 6 ay).",
        "difficulty": "zor",
        "tags": ["ayrılma hakkı", "önemli nitelikteki işlemler", "fiyat tespiti"]
    },
    {
        "id": "q_1001_master_105",
        "module_id": "1001",
        "number": 105,
        "source": "master",
        "topic": "Kamuyu Aydınlatma ve Erteleme",
        "chapter": "Bölüm 4: Kamuyu Aydınlatma ve Şeffaflık",
        "text": "Özel Durumlar Tebliği (II-15.1) uyarınca, ihraççıların içsel bilgilerin kamuya açıklanmasını erteleme yetkisi ve şartları hakkında aşağıdakilerden hangisi DOĞRUDUR?",
        "options": [
            {"key": "A", "text": "Meşru menfaatlerin korunması, kamuoyunun yanıltılmaması ve bilginin gizliliğinin sağlanması şartıyla erteleme kararı alınabilir."},
            {"key": "B", "text": "İhraççılar içsel bilgilerin açıklanmasını diledikleri gerekçeyle ve süre sınırlaması olmaksızın serbestçe erteleyebilirler."},
            {"key": "C", "text": "İçsel bilginin açıklanmasının ertelenmesi için Borsa İstanbul Yönetim Kurulu'ndan 3 iş günü önceden izin alınması şarttır."},
            {"key": "D", "text": "Erteleme süresi boyunca içsel bilginin basına sızması halinde dahi ihraççının KAP'ta açıklama yapma zorunluluğu doğmaz."},
            {"key": "E", "text": "İçsel bilgilerin ertelenmesi kararı genel kurulun 3/4 çoğunluğuyla alınmadıkça hukuken hiçbir geçerlilik taşımaz."}
        ],
        "correct_answer": "A",
        "explanation": "Özel Durumlar Tebliği m.6 uyarınca ihraççı, meşru menfaatlerinin zarar görmemesi için kendi sorumluluğunda içsel bilginin kamuya açıklanmasını erteleyebilir. Ancak bu ertelemenin kamuoyunun yanıltılmasına yol açmaması ve bilginin gizliliğinin korunması zorunludur. Bilginin gizliliği korunamadığı (sızdığı) anda derhal KAP'ta özel durum açıklaması yapılmalıdır.",
        "trap": "Erteleme için SPK veya Borsa'dan önceden izin alınmaz, sorumluluk ihraççının yönetim kurulundadır. Ancak gizlilik bozulursa anında kamuya açıklanmak zorundadır.",
        "difficulty": "orta",
        "tags": ["içsel bilgi", "erteleme", "özel durumlar"]
    },

    # Modül 1003: 5 Questions
    {
        "id": "q_1003_master_101",
        "module_id": "1003",
        "number": 101,
        "source": "master",
        "topic": "Tahvil Temiz ve Kirli Fiyat",
        "chapter": "Bölüm 3: Sabit Getirili Menkul Kıymetler",
        "text": "Tahvil piyasasında 'Temiz Fiyat' (Clean Price) ile 'Kirli Fiyat' (Dirty Price) arasındaki matematiksel ilişkiyi ve hesaplamayı gösteren doğru formül aşağıdakilerden hangisidir?",
        "options": [
            {"key": "A", "text": "Kirli Fiyat = Temiz Fiyat + Birikmiş Faiz (Kupon döneminde biriken faiz tutarı temiz fiyata eklenerek kirli fiyat bulunur)"},
            {"key": "B", "text": "Kirli Fiyat = Temiz Fiyat - Birikmiş Faiz (Kupon döneminde biriken faiz temiz fiyattan düşülerek kirli fiyat bulunur)"},
            {"key": "C", "text": "Temiz Fiyat = Kirli Fiyat + BSMV ve Komisyon Giderleri (Vergi ve kesintiler kirli fiyata eklenerek temiz fiyat bulunur)"},
            {"key": "D", "text": "Kirli Fiyat = Nominal Fiyat / (1 + Kupon Faiz Oranı) (Tahvilin bugünkü iskonto edilmiş nakit akış değeridir)"},
            {"key": "E", "text": "Temiz Fiyat = Kirli Fiyat * (Kalan Gün Sayısı / 365) (Yıllık basit faiz getirisinin kalan vadeye orantılanmasıdır)"}
        ],
        "correct_answer": "A",
        "explanation": "Tahvil piyasasında kotasyonlar piyasa dalgalanmalarını net yansıtmak amacıyla 'Temiz Fiyat' üzerinden verilir. Ancak takas anında alıcının satıcıya ödeyeceği fiili tutar 'Kirli Fiyat'tır. Kirli Fiyat = Temiz Fiyat + Birikmiş Faiz (Accrued Interest) formülüyle hesaplanır. Birikmiş faiz, son kupon ödeme tarihinden takas gününe kadar geçen günlerde hak edilen faizdir.",
        "trap": "Kirli Fiyat her zaman Temiz Fiyat + Birikmiş Faizdir. Kupon ödeme gününde birikmiş faiz sıfır olduğundan Kirli Fiyat = Temiz Fiyat olur.",
        "difficulty": "orta",
        "tags": ["tahvil", "temiz fiyat", "kirli fiyat", "birikmiş faiz"]
    },
    {
        "id": "q_1003_master_102",
        "module_id": "1003",
        "number": 102,
        "source": "master",
        "topic": "Kira Sertifikaları Türleri",
        "chapter": "Bölüm 4: Kira Sertifikaları (Sukuk)",
        "text": "Kira Sertifikaları Tebliği (III-61.1) uyarınca, VKŞ'nin alıcı, kaynak kuruluşun satıcı olduğu ve varlığın peşin alınıp vadeli olarak kaynak kuruluşa veya üçüncü kişilere kâr payı eklenerek satılmasına dayanan sukuk türü hangisidir?",
        "options": [
            {"key": "A", "text": "Alım-Satıma Dayalı Kira Sertifikası (Murabaha Sukuku)"},
            {"key": "B", "text": "Eser Sözleşmesine Dayalı Kira Sertifikası (İstisna Sukuku)"},
            {"key": "C", "text": "Ortaklığa Dayalı Kira Sertifikası (Mudaraba / Müşareke Sukuku)"},
            {"key": "D", "text": "Mülkiyete ve Kiralamaya Dayalı Kira Sertifikası (İcara Sukuku)"},
            {"key": "E", "text": "Yatırım Vekaletine Dayalı Kira Sertifikası (Vekalet Sukuku)"}
        ],
        "correct_answer": "A",
        "explanation": "Murabaha (Alım-Satıma Dayalı Sukuk), bir varlığın VKŞ tarafından peşin satın alınıp vadeli olarak maliyet artı kâr marjıyla (kâr payı eklenerek) müşteriye/kaynak kuruluşa satılması işlemine dayanır. Eser sözleşmesine dayalı sukuk İstisna, kiralamaya dayalı sukuk İcara, emek-sermaye ortaklığına dayalı sukuk ise Mudaraba olarak adlandırılır.",
        "trap": "İstisna eser/üretim sözleşmesidir, İcara kiralamadır, Murabaha ise maliyet+kâr ile vadeli alım-satımdır.",
        "difficulty": "orta",
        "tags": ["kira sertifikası", "sukuk", "murabaha", "istisna"]
    },
    {
        "id": "q_1003_master_103",
        "module_id": "1003",
        "number": 103,
        "source": "master",
        "topic": "Varantlarda Moneyness ve Asli Değer",
        "chapter": "Bölüm 5: Varantlar ve Sertifikalar",
        "text": "Bir hisse senedi üzerine yazılmış Alım Varantında (Call Warrant) kullanım fiyatı 50 TL iken dayanak hissenin spot piyasa fiyatı 60 TL ise, bu varantın durumu ve Asli Değeri (Intrinsic Value) hakkında hangisi DOĞRUDUR?",
        "options": [
            {"key": "A", "text": "Varant 'Kârda' (In the Money) durumundadır ve pozitif asli değere sahiptir (Asli Değer = 60 - 50 = 10 TL * Çarpan)."},
            {"key": "B", "text": "Varant 'Zararda' (Out of the Money) durumundadır ve asli değeri negatiftir (Asli Değer = -10 TL * Çarpan)."},
            {"key": "C", "text": "Varant 'Başa Baş' (At the Money) durumundadır ve piyasa değeri yalnızca zaman değerinden oluşur."},
            {"key": "D", "text": "Alım varantlarında spot fiyat kullanım fiyatını aştığında ihraççı varantı derhal re'sen itfa etmek zorundadır."},
            {"key": "E", "text": "Varantın asli değeri sıfır olup piyasada yalnızca vade sonu volatilite primine göre fiyatlanır."}
        ],
        "correct_answer": "A",
        "explanation": "Alım varantında (Call), Dayanak Varlık Fiyatı > Kullanım Fiyatı (60 > 50) ise varant 'KÂRDA'dır (In the Money). Alım varantında Asli Değer = (Spot Fiyat - Kullanım Fiyatı) * Çarpan formülüyle hesaplanır ve pozitiftir (60 - 50 = 10 TL * Çarpan). Zararda olan varantların asli değeri sıfırdır, asla negatif olamaz.",
        "trap": "Varantlarda asli değer ASLA negatif olamaz; ya pozitiftir (kârda ise) ya da sıfırdır (başa baş veya zararda ise).",
        "difficulty": "zor",
        "tags": ["varant", "asli değer", "in the money", "moneyness"]
    },
    {
        "id": "q_1003_master_104",
        "module_id": "1003",
        "number": 104,
        "source": "master",
        "topic": "Katılma İntifa Senetleri",
        "chapter": "Bölüm 2: Paylar ve Pay Benzeri Menkul Kıymetler",
        "text": "Anonim ortaklıklar tarafından ihraç edilebilen 'Katılma İntifa Senetleri'nin (KİS) sağladığı haklar ve yasal sınırlamalarla ilgili aşağıdakilerden hangisi DOĞRUDUR?",
        "options": [
            {"key": "A", "text": "Sahibine kârdan pay alma ve tasfiye bakiyesinden yararlanma hakkı verir ancak hiçbir şekilde genel kurulda oy hakkı vermez."},
            {"key": "B", "text": "Sahibine şirket yönetim kuruluna doğrudan üye seçme hakkı ve genel kurulda imtiyazlı oy hakkı tanır."},
            {"key": "C", "text": "Şirketin esas sermaye payını temsil eden bir menkul kıymet olup nama yazılı olarak çıkarılması zorunludur."},
            {"key": "D", "text": "KİS sahiplerine her yıl kâr dağıtımı yapılmasa dahi kanunen asgari Hazine faizi oranında nakit ödeme garantisi verilir."},
            {"key": "E", "text": "Yalnızca halka arz edilmemiş kapalı aile şirketleri tarafından çıkarılabilen ve borsada işlem görmeyen borçlanma aracıdır."}
        ],
        "correct_answer": "A",
        "explanation": "Katılma İntifa Senetleri (KİS); ortaklık esas sermaye payını temsil etmeyen, sahibine ortaklık hakları içinde sadece mali haklar (şirket kârından pay alma, tasfiye bakiyesinden pay alma, yeni pay alma hakkı) sağlayan; ancak yönetim ve genel kurulda OY HAKKI ile idari haklar VERMEYEN menkul kıymet niteliğinde sermaye piyasası araçlarıdır.",
        "trap": "KİS sahipleri şirketin ortağı veya pay sahibi değildir, sermayeyi temsil etmez ve genel kurulda OY HAKLARI YOKTUR.",
        "difficulty": "orta",
        "tags": ["katılma intifa senedi", "KİS", "oy hakkı yasağı"]
    },
    {
        "id": "q_1003_master_105",
        "module_id": "1003",
        "number": 105,
        "source": "master",
        "topic": "Finansman Bonosu ve Tahvil Farkları",
        "chapter": "Bölüm 3: Borçlanma Araçları",
        "text": "Sermaye Piyasası Kanunu uyarınca borçlanma araçlarından Finansman Bonoları ile Tahviller arasındaki temel farklar hakkında aşağıdakilerden hangisi DOĞRUDUR?",
        "options": [
            {"key": "A", "text": "Finansman bonoları en fazla 1 yıl (365 gün) vadeli ve iskontolu ihraç edilirken; tahviller 1 yıldan uzun vadeli ihraç edilir."},
            {"key": "B", "text": "Tahviller sadece anonim şirketler tarafından çıkarılabilirken; finansman bonoları yalnızca belediyeler tarafından çıkarılır."},
            {"key": "C", "text": "Finansman bonoları hamiline genel kurulda oy hakkı verirken; tahviller hiçbir ortaklık hakkı tanımaz."},
            {"key": "D", "text": "Tahvillerde kupon ödemesi yapılması kanunen yasak olup; finansman bonolarında üç ayda bir değişken faiz kuponu ödenir."},
            {"key": "E", "text": "Finansman bonolarında vade süresi en az 5 yıl olmak zorundayken; tahvillerde vade serbestçe belirlenir."}
        ],
        "correct_answer": "A",
        "explanation": "Borçlanma Araçları Tebliği (VII-128.8) uyarınca Finansman Bonoları, ihraççının kısa vadeli borçlanma amacıyla çıkardığı, vadesi 30 günden az 365 günden (1 yıldan) fazla olamayan, kural olarak iskontolu satılan sermaye piyasası araçlarıdır. Tahviller ise vadeleri 1 yıl (365 gün) ve daha uzun olan orta ve uzun vadeli borçlanma senetleridir.",
        "trap": "Bono kısa vadeli (max 365 gün), tahvil orta/uzun vadeli (min 1 yıl/365 gün) borçlanma aracıdır.",
        "difficulty": "orta",
        "tags": ["finansman bonosu", "tahvil", "vade farkı"]
    }
]

def apply_upgrades(file_path):
    print(f"Guncelleniyor: {file_path}")
    if not os.path.exists(file_path):
        print(f"Hata: {file_path} bulunamadi!")
        return 0, 0
        
    with open(file_path, 'r', encoding='utf-8') as f:
        questions = json.load(f)
        
    replaced_count = 0
    for q in questions:
        qid = q.get('id')
        if qid in REPLACEMENTS:
            rep = REPLACEMENTS[qid]
            q['text'] = rep['text']
            q['options'] = rep['options']
            q['correct_answer'] = rep['correct_answer']
            q['explanation'] = rep['explanation']
            replaced_count += 1
            
    # Add new questions if not present
    existing_ids = {q['id'] for q in questions}
    added_count = 0
    for nq in NEW_QUESTIONS:
        if nq['id'] not in existing_ids:
            questions.append(nq)
            existing_ids.add(nq['id'])
            added_count += 1
            
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(questions, f, ensure_ascii=False, indent=2)
        
    print(f"  -> {replaced_count} soru basariyla guncellendi/revize edildi.")
    print(f"  -> {added_count} yeni soru basariyla eklendi.")
    print(f"  -> Toplam soru sayisi: {len(questions)}")
    return replaced_count, added_count

if __name__ == '__main__':
    rep1, add1 = apply_upgrades('src/data/all_questions.json')
    rep2, add2 = apply_upgrades('src/data/questions_master.json')
    print("\n--- Butun Guncellemeler Tamamlandi ---")
