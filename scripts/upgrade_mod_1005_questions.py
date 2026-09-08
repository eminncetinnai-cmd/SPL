import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('src/data/all_questions.json', 'r', encoding='utf-8') as f:
    questions = json.load(f)

# Comprehensive dictionary of upgraded Module 1005 questions
REPLACEMENTS_1005 = {
    "q_1005_master_004": {
        "text": "Aşağıdaki yatırım hizmet ve faaliyetlerinden hangisi mevzuat uyarınca YALNIZCA 'Geniş Yetkili Aracı Kurumlar' tarafından yerine getirilebilir?",
        "options": [
            {"key": "A", "text": "Müşteri emirlerinin borsaya iletilmesi (Emir İletimine Aracılık)"},
            {"key": "B", "text": "Müşteri namına ve hesabına işlem gerçekleştirilmesi (İşlem Aracılığı)"},
            {"key": "C", "text": "Halka arzda satılamayan payları satın alma taahhüdü olmaksızın satış (En İyi Gayret Aracılığı)"},
            {"key": "D", "text": "Kendi nam ve hesabına sermaye piyasası aracı alım satımı (Portföy Aracılığı) ve Bakiye Yüklenimi"},
            {"key": "E", "text": "Sermaye piyasası araçlarına ilişkin genel yatırım tavsiyesi ve piyasa bülteni hazırlanması"}
        ],
        "correct_answer": "D",
        "explanation": "SPK Yatırım Kuruluşları Tebliği (III-39.1) uyarınca; Portföy Aracılığı (kendi nam ve hesabına alım-satım) ve Halka Arzda Bakiye/Tümünü Yüklenim faaliyetleri yalnızca Geniş Yetkili Aracı Kurumlar tarafından yürütülebilir. Kısmi ve Dar yetkili kurumlar bu faaliyetleri yapamaz."
    },
    "q_1005_master_009": {
        "text": "Aracı kurum yönetim kurulu üyelerinin çoğunluğunun sağlaması gereken asgari eğitim ve mesleki tecrübe şartı aşağıdakilerden hangisidir?",
        "options": [
            {"key": "A", "text": "En az 2 yıllık ön lisans mezunu olmak ve 1 yıl aracı kurumda çalışmış olmak"},
            {"key": "B", "text": "En az 4 yıllık yükseköğrenim mezunu olmak ve finans/ekonomi alanında en az 3 yıllık tecrübeye sahip olmak"},
            {"key": "C", "text": "İktisadi ve idari bilimler alanında yüksek lisans veya doktora derecesine sahip olmak"},
            {"key": "D", "text": "Hukuk veya mühendislik fakültesi mezunu olup en az 10 yıl kamu tecrübesi bulunmak"},
            {"key": "E", "text": "SPK Düzey 3 ve Türev Araçlar Lisanslarının tamamına şahsen sahip olmak"}
        ],
        "correct_answer": "B",
        "explanation": "SPK Yatırım Kuruluşları Tebliği (III-39.1) m.9 uyarınca; aracı kurum yönetim kurulu üyelerinin çoğunluğunun 4 yıllık yükseköğrenim mezunu olması ve finans, iktisat, işletme veya hukuk alanlarında en az 3 yıllık mesleki tecrübeye sahip olması kanunen şarttır."
    },
    "q_1005_master_010": {
        "text": "Aracı kurum Genel Müdürünün yasal olarak taşıması gereken asgari nitelikler bakımından aşağıdakilerden hangisi DOĞRUDUR?",
        "options": [
            {"key": "A", "text": "En az 2 yıllık meslek yüksekokulu mezunu ve 3 yıllık finans tecrübesine sahip olmak"},
            {"key": "B", "text": "En az 4 yıllık lisans mezunu olmak ve sermaye piyasaları alanında en az 5 yıllık tecrübe taşımak"},
            {"key": "C", "text": "4 yıllık lisans mezunu olmak, finans veya işletmecilik alanında en az 7 yıllık tecrübeye ve Düzey 3 Lisansına sahip olmak"},
            {"key": "D", "text": "Yalnızca bankacılık alanında en az 10 yıl şube müdürlüğü yapmış olmak"},
            {"key": "E", "text": "Kurumun sermayesinde en az %10 pay sahibi kurucu ortak olmak"}
        ],
        "correct_answer": "C",
        "explanation": "Aracı kurum genel müdürlerinin 4 yıllık lisans mezunu olmaları, finans veya işletmecilik alanında en az 7 yıllık mesleki deneyime sahip bulunmaları ve SPK Düzey 3 Lisansı taşımaları kanunen zorunludur."
    },
    "q_1005_master_016": {
        "text": "Sermaye piyasası işlemlerinin risklerini açıklayan 'Genel Risk Bildirim Formu'nun müşteriye verilme usulü ve zamanlaması ile ilgili hangisi DOĞRUDUR?",
        "options": [
            {"key": "A", "text": "Müşterinin ilk borsa işleminde zarar etmesi durumunda takip eden 10 iş günü içinde tebliğ edilir"},
            {"key": "B", "text": "Yalnızca kredili işlem ve açığa satış yetkisi talep eden müşterilere hesap açılışından 1 ay sonra gönderilir"},
            {"key": "C", "text": "Yalnızca tüzel kişi profesyonel müşterilere noter kanalıyla iadeli taahhütlü olarak iletilir"},
            {"key": "D", "text": "Çerçeve sözleşmenin imzalanmasından önce veya imza anında müşteriye verilip içeriği açıklanarak imzalı teyidi alınır"},
            {"key": "E", "text": "Müşterinin talebi olmaksızın verilmesi aracı kurumlar açısından ticari sır ihlali sayılır"}
        ],
        "correct_answer": "D",
        "explanation": "Genel Risk Bildirim Formu, aracılık çerçeve sözleşmesinin imzalanmasından önce veya imza anında müşteriye verilmek, riskleri izah edilmek ve bir örneğinin teslim alındığına dair müşterinin yazılı/elektronik onayı alınmak zorundadır."
    },
    "q_1005_master_023": {
        "text": "Aracı kurumun kendi nam ve hesabına sermaye piyasası araçlarının alım ve satımını yapması faaliyeti mevzuatta nasıl adlandırılır?",
        "options": [
            {"key": "A", "text": "Emir İletimine Aracılık"},
            {"key": "B", "text": "İşlem Aracılığı"},
            {"key": "C", "text": "Portföy Aracılığı"},
            {"key": "D", "text": "Yatırım Danışmanlığı"},
            {"key": "E", "text": "Portföy Yöneticiliği"}
        ],
        "correct_answer": "C",
        "explanation": "Aracı kurumun kendi nam ve hesabına sermaye piyasası araçlarında işlem yapması, piyasa yapıcılığı ve likidite sağlayıcılığı 'Portföy Aracılığı' (Principal Dealing) olarak tanımlanır."
    },
    "q_1005_master_030": {
        "text": "Yatırım kuruluşlarının web sitelerinde yayımlamak zorunda oldukları 'Çıkar Çatışması Politikası'nın temel yasal amacı nedir?",
        "options": [
            {"key": "A", "text": "Kurumun halka açık şirketlerdeki pay sahipliği oranlarını borsa bülteninde ilan etmek"},
            {"key": "B", "text": "Aracı kurum çalışanlarının kendi aralarındaki prim ve komisyon paylaşımını düzenlemek"},
            {"key": "C", "text": "Müşteriler arası veya müşteri ile kurum arasındaki çıkar çatışmalarını tespit etmek, önlemek ve adil biçimde yönetmek"},
            {"key": "D", "text": "Kurumun mali tablolarındaki gider kalemlerini vergi denetiminden istisna tutmak"},
            {"key": "E", "text": "Borsa işlemlerinde kurumun kendi emirlerine müşteri emirleri karşısında öncelik tanımak"}
        ],
        "correct_answer": "C",
        "explanation": "Çıkar Çatışması Politikası; yatırım kuruluşunun müşterileriyle, çalışanlarıyla veya müşterilerin kendi aralarında ortaya çıkabilecek menfaat çatışmalarını tespit etmek, önlemek ve yönetmek amacıyla hazırlanır."
    },
    "q_1005_master_032": {
        "text": "İnternet ve mobil kanallardan emir kabul eden aracı kurumların iki faktörlü kimlik doğrulama (2FA) uygulaması getirmesinin temel yasal gerekçesi nedir?",
        "options": [
            {"key": "A", "text": "İnternet üzerinden iletilen emirlerin borsa işlem komisyonu oranlarını artırmak"},
            {"key": "B", "text": "Yalnızca yabancı para cinsinden verilen sınır ötesi transferleri denetlemek"},
            {"key": "C", "text": "Yatırımcıların gün içindeki işlem sıklığını ve spekülatif pozisyonlarını sınırlandırmak"},
            {"key": "D", "text": "İşlem log kayıtlarının MKK yerine yalnızca aracı kurum bünyesinde tutulmasını sağlamak"},
            {"key": "E", "text": "Müşteri hesaplarının yetkisiz erişimlere ve siber dolandırıcılığa karşı güvenliğini en üst düzeyde sağlamak"}
        ],
        "correct_answer": "E",
        "explanation": "Elektronik ortamda emir iletiminde iki faktörlü kimlik doğrulama (2FA); müşteri kimliğinin ve hesap güvenliğinin teyidi, yetkisiz üçüncü kişilerin hesaba erişiminin engellenmesi için SPK tarafından zorunlu tutulmuştur."
    },
    "q_1005_master_033": {
        "text": "Halka arz konsorsiyumunda 'Konsorsiyum Lideri' olan aracı kurumun temel yasal görev ve sorumluluğu nedir?",
        "options": [
            {"key": "A", "text": "Halka arz edilecek payların borsadaki günlük fiyat tabanını tek başına finanse etmek"},
            {"key": "B", "text": "İhraççı şirketin yönetim kurulundaki bağımsız üye seçimlerini bizzat yürütmek"},
            {"key": "C", "text": "Konsorsiyum üyelerinin tamamının vergi borçlarını kendi özkaynaklarından ödemek"},
            {"key": "D", "text": "İzahnameyi hazırlamak, SPK ve Borsa süreçlerini koordine etmek ve konsorsiyum üyeleri arasındaki pay dağıtımını yönetmek"},
            {"key": "E", "text": "Halka arz gelirlerini şirket adına faizsiz hazine bonolarına plase etmek"}
        ],
        "correct_answer": "D",
        "explanation": "Konsorsiyum lideri; halka arz sürecinde izahnamenin hazırlanması, SPK ve Borsa onaylarının alınması, konsorsiyum sözleşmesinin akdedilmesi ve talep toplama ile dağıtımın koordinasyonundan sorumlu lider kuruluştur."
    },
    "q_1005_master_036": {
        "text": "Kısmi yetkili aracı kurumların verebileceği 'Sınırlı Saklama Hizmeti'nin yasal kapsamı aşağıdakilerden hangisidir?",
        "options": [
            {"key": "A", "text": "Yatırım fonlarının ve emeklilik fonlarının portföy saklayıcılığını üstlenme yetkisi"},
            {"key": "B", "text": "Borsa İstanbul Kıymetli Madenler Piyasası nezdinde külçe altın saklama yetkisi"},
            {"key": "C", "text": "Yurt dışında yerleşik saklama kuruluşları nezdinde global saklama hesabı açma yetkisi"},
            {"key": "D", "text": "Yalnızca kendi aracılık ettiği işlemlerle sınırlı olarak müşteri varlıklarını Takasbank ve MKK nezdinde izleme yetkisi"},
            {"key": "E", "text": "Halka açık şirketlerin fiziki hisse senedi ve tahvil basımlarını noter onaylı yürütme yetkisi"}
        ],
        "correct_answer": "D",
        "explanation": "Sınırlı saklama yetkisi; aracı kurumun yalnızca kendi aracılık ettiği sermaye piyasası işlemlerinden doğan müşteri nakit ve kıymetlerini Takasbank ve MKK nezdinde kendi alt hesaplarında izleyebilmesini ifade eder; genel saklama hizmeti veremez."
    },
    "q_1005_master_037": {
        "text": "Aracı kurumlarda 'İç Kontrol Birimi'nin temel yasal fonksiyonu ve görevi nedir?",
        "options": [
            {"key": "A", "text": "Kurumun pazarlama stratejilerini belirleyerek yeni müşteri portföyü oluşturmak"},
            {"key": "B", "text": "Kurumun tüm faaliyetlerinin mevzuata, kurum içi prosedürlere ve yönetim kararlarına uygunluğunu sürekli denetlemek"},
            {"key": "C", "text": "Yatırımcılara günlük hisse alım-satım ve arbitraj tavsiyeleri üretmek"},
            {"key": "D", "text": "Kurum portföyündeki menkul kıymetlerin borsadaki günlük alım satımını yönetmek"},
            {"key": "E", "text": "Aracı kurumun altı aylık ve yıllık bağımsız denetim raporlarını onaylamak"}
        ],
        "correct_answer": "B",
        "explanation": "İç Kontrol Birimi; yatırım kuruluşunun tüm birim ve faaliyetlerinin sermaye piyasası mevzuatına, iç tüzüklere ve yönetim kurulu politikalarına uygun olarak yürütülmesini sürekli olarak denetleyen bağımsız birimdir."
    },
    "q_1005_master_045": {
        "text": "Portföy yönetim şirketlerinin yönettikleri fon ve bireysel portföylerden 'Başarı Primi' (Performans Ücreti) tahsil edebilmesi için aranan yasal şart nedir?",
        "options": [
            {"key": "A", "text": "Portföyün son üç ayda BIST 100 endeksi ile aynı getiriyi sağlamış olması"},
            {"key": "B", "text": "Portföy büyüklüğünün SPK'nın belirlediği asgari kurumsal fon limitine ulaşması"},
            {"key": "C", "text": "Portföy getirisinin sözleşmede veya izahnamede belirlenen Karşılaştırma Ölçütünü (Benchmark / Eşik Değer) aşmış olması"},
            {"key": "D", "text": "İlgili dönemde piyasa faiz oranlarının TCMB politika faizinin altına gerilemesi"},
            {"key": "E", "text": "Müşterinin yazılı talepte bulunarak portföy yöneticisine ek prim teklif etmesi"}
        ],
        "correct_answer": "C",
        "explanation": "Başarı primi (performans ücreti); portföy getirisinin sözleşmede baştan belirlenen karşılaştırma ölçütünü veya eşik değeri aşması halinde bu aşan getiri kısmı üzerinden tahsil edilebilir."
    },
    "q_1005_master_049": {
        "text": "Halka arza liderlik eden aracı kurum analistlerinin halka arz öncesinde ve sonrasında araştırma raporu yayımlayamadıkları yasal kısıtlama dönemine ne ad verilir?",
        "options": [
            {"key": "A", "text": "Fiyat İstikrarı Dönemi"},
            {"key": "B", "text": "Konsorsiyum Talep Toplama Dönemi"},
            {"key": "C", "text": "Kotasyon ve Tescil Dönemi"},
            {"key": "D", "text": "İtfa ve Tasfiye Dönemi"},
            {"key": "E", "text": "Sessizlik Dönemi (Quiet Period)"}
        ],
        "correct_answer": "E",
        "explanation": "Halka arza aracılık eden lider ve konsorsiyum üyelerinin araştırma birimleri, yatırımcıları yönlendirmemek ve çıkar çatışmasını önlemek amacıyla halka arz öncesi ve sonrasındaki belirli süre boyunca şirket hakkında rapor yayımlayamazlar; buna 'Sessizlik Dönemi' (Quiet Period) denir."
    },
    "q_1005_master_050": {
        "text": "Bir yatırım kuruluşunda 'Bireysel Yatırım Danışmanı' olarak görev yapabilmek için aşağıdaki lisanslardan hangisine sahip olunması mevzuaten ZORUNLUDUR?",
        "options": [
            {"key": "A", "text": "Gayrimenkul Değerleme Lisansı"},
            {"key": "B", "text": "Kredi Derecelendirme Lisansı"},
            {"key": "C", "text": "Kurumsal Yönetim Derecelendirme Lisansı"},
            {"key": "D", "text": "Sermaye Piyasası Faaliyetleri Düzey 3 Lisansı ve Yatırım Danışmanlığı Lisansı"},
            {"key": "E", "text": "Konut Değerleme Lisansı"}
        ],
        "correct_answer": "D",
        "explanation": "Yatırım Danışmanlığı hizmeti verecek uzman personelin SPK Sermaye Piyasası Faaliyetleri Düzey 3 Lisansı ve ilgili lisans belgelerine sahip olması zorunludur."
    },
    "q_1005_master_058": {
        "text": "Yatırım kuruluşlarında genel müşterilere uygulanan 'Uygunluk Testi'nin (Appropriateness) temel amacı nedir?",
        "options": [
            {"key": "A", "text": "Müşterinin bilgi ve tecrübesinin talep ettiği ürünün risklerini anlamaya yeterli olup olmadığını tespit etmek"},
            {"key": "B", "text": "Müşterinin vergi matrahını ve gelir vergisi beyannamesini MASAK standartlarına göre doğrulamak"},
            {"key": "C", "text": "Müşteriye yalnızca risksiz kamu borçlanma araçları satılmasını zorunlu kılmak"},
            {"key": "D", "text": "Müşterinin toplam nakit varlığını öğrenerek asgari hesap açılış limitini belirlemek"},
            {"key": "E", "text": "Aracı kurumun geçmiş yıl bilanço zararlarını müşteri hesaplarına oransal yansıtmak"}
        ],
        "correct_answer": "A",
        "explanation": "Uygunluk testi; genel müşterinin talep ettiği sermaye piyasası aracının veya hizmetinin risklerini kavrayacak düzeyde bilgi ve tecrübeye sahip olup olmadığını değerlendirmek amacıyla yapılır."
    },
    "q_1005_master_059": {
        "text": "'Yerindelik Testi'nde (Suitability), uygunluk testine ek olarak müşterinin hangi kapsamlı bilgileri analiz edilir?",
        "options": [
            {"key": "A", "text": "Müşterinin yatırım amaçları, risk toleransı, mali durumu ve olası zararları karşılama kapasitesi"},
            {"key": "B", "text": "Müşterinin yalnızca adli sicil kaydı ve geçmiş ticari dava dosyaları"},
            {"key": "C", "text": "Müşterinin diğer bankalardaki vadesiz mevduat hesaplarının günlük faiz oranları"},
            {"key": "D", "text": "Müşterinin gayrimenkul varlıklarının belediye emlak vergi beyannameleri"},
            {"key": "E", "text": "Müşterinin ticaret siciline kayıtlı ortaklarının ikametgah bilgileri"}
        ],
        "correct_answer": "A",
        "explanation": "Yerindelik testi; portföy yöneticiliği ve yatırım danışmanlığı hizmetlerinde, müşterinin sadece bilgi ve tecrübesini değil; yatırım amaçlarını, risk-getiri tercihlerini ve mali durumunun zararı karşılama kapasitesini ölçer."
    },
    "q_1005_master_064": {
        "text": "Profesyonel müşteri statüsündeki bir yatırımcının, mevzuatın sağladığı korumalardan yararlanmak üzere 'Genel Müşteri' statüsüne geçme talebi karşısında aracı kurum ne yapmak zorundadır?",
        "options": [
            {"key": "A", "text": "Kurum bu talebi gerekçe göstermeksizin reddetme hakkına sahiptir"},
            {"key": "B", "text": "Talebin geçerli olması için müşterinin portföyünün %50'sini nakde çevirmesi şarttır"},
            {"key": "C", "text": "Kurum bu talebi SPK Karar Organı onayına sunmakla yükümlüdür"},
            {"key": "D", "text": "Statü değişikliği yalnızca takvim yılı başlarında yılda bir kez yapılabilir"},
            {"key": "E", "text": "Kurum bu talebi koşulsuz kabul etmek ve müşteriyi genel müşteri haklarından yararlandırmak zorundadır"}
        ],
        "correct_answer": "E",
        "explanation": "Profesyonel müşteriler diledikleri zaman yazılı başvuruda bulunarak Genel Müşteri olarak muamele görmeyi talep edebilirler. Yatırım kuruluşu bu talebi kabul etmek ve müşteriyi genel müşteri koruma hükümlerine tabi kılmak zorundadır."
    },
    "q_1005_master_066": {
        "text": "Uygunluk testi sonucunda müşterinin talep ettiği ürün veya hizmet risk profiline 'Uygun Değildir' sonucu çıkarsa aracı kurumun izleyeceği yasal prosedür nedir?",
        "options": [
            {"key": "A", "text": "Kurum müşterinin hesabını derhal kapatarak tüm varlıklarını bloke eder"},
            {"key": "B", "text": "Müşteriyi sermaye piyasasında işlem yapmaktan 1 yıl süreyle men eder"},
            {"key": "C", "text": "Ürünün uygun olmadığını müşteriye yazılı bildirir; müşteri yazılı ısrar ederse emri gerçekleştirebilir"},
            {"key": "D", "text": "Emri doğrudan Borsa İstanbul Disiplin Kurulu'nun onayına sevk eder"},
            {"key": "E", "text": "Müşterinin onayını aramaksızın ürünü en düşük riskli hazine bonosu ile değiştirir"}
        ],
        "correct_answer": "C",
        "explanation": "Ürünün müşteriye uygun olmaması durumunda aracı kurum bu hususu müşteriye açıkça yazılı/elektronik olarak bildirir (Uyarı Bildirimi). Müşteri buna rağmen işlemi gerçekleştirmekte yazılı olarak ısrar ederse kurum işlemi yapabilir."
    },
    "q_1005_master_069": {
        "text": "Müşterilerine 'Doğrudan Piyasa Erişimi' (DMA / Doğrudan Borsa İletimi) olanağı sunan aracı kurumların almak zorunda olduğu temel yasal tedbir nedir?",
        "options": [
            {"key": "A", "text": "Tüm emirleri seans bitiminden sonra topluca eşleştirmek"},
            {"key": "B", "text": "DMA kullanan müşterilerden komisyon ve borsa payı almamak"},
            {"key": "C", "text": "Emirlerin borsaya iletilmesini en az 15 dakika geciktirmek"},
            {"key": "D", "text": "İşlemleri yalnızca mesai saatleri dışındaki serbest marj seansına yönlendirmek"},
            {"key": "E", "text": "Sisteme ön işlem risk kontrolleri (fiyat, miktar, emir/işlem oranı filtreleri) entegre etmek"}
        ],
        "correct_answer": "E",
        "explanation": "Doğrudan piyasa erişimi (DMA) sağlayan aracı kurumlar, hatalı ve piyasayı bozucu emirleri engellemek üzere emirlerin borsa sistemine gitmesinden önce otomatik çalışan ön işlem risk filtreleri (Pre-Trade Risk Controls) uygulamak zorundadır."
    },
    "q_1005_master_070": {
        "text": "Müşteri temsilcisi (Broker), müşterinin yazılı veya ses kaydı alınmış açık talimatı olmaksızın kendi inisiyatifiyle müşteri hesabında işlem yapabilir mi?",
        "options": [
            {"key": "A", "text": "Kesinlikle yapamaz; talimatsız işlem yetkisiz işlemdir ve ağır mevzuat ihlalidir"},
            {"key": "B", "text": "Portföyün günlük zarar etme riskini önlemek amacıyla genel müdür onayıyla yapabilir"},
            {"key": "C", "text": "Günlük işlem hacmi 100.000 TL'yi aşmamak kaydıyla re'sen işlem gerçekleştirebilir"},
            {"key": "D", "text": "Müşteriyle akrabalık ilişkisi varsa yazılı talimatsız emir girebilir"},
            {"key": "E", "text": "Hisse fiyatında tavan veya taban oluşması halinde temsilci inisiyatif kullanabilir"}
        ],
        "correct_answer": "A",
        "explanation": "Müşterinin yazılı veya ses kayıt sistemi üzerinden açık talimatı olmaksızın müşteri hesabında alım-satım yapılması kesinlikle yasaktır ve yetkisiz işlem kapsamında ağır idari ve cezai yaptırıma tabidir."
    },
    "q_1005_master_075": {
        "text": "Kredili işlem yapan bir yatırımcı, yapılan özkaynak tamamlama çağrısına (Margin Call) verilen sürede uymazsa aracı kurumun yasal yetkisi nedir?",
        "options": [
            {"key": "A", "text": "Müşteri aleyhine doğrudan iflas davası açarak hesapları 1 yıl dondurmak"},
            {"key": "B", "text": "Müşteriye temerrüt kredisi açarak borcu vadesiz mevduata dönüştürmek"},
            {"key": "C", "text": "İhbar veya ihtara gerek kalmaksızın özkaynak oranını sağlayacak miktarda hisseyi re'sen borsada satmak"},
            {"key": "D", "text": "Teminat açığını kapatmak üzere aracı kurum ortaklarının şahsi hisselerini rehnetmek"},
            {"key": "E", "text": "Borcun tamamını Yatırımcı Tazmin Merkezi'ne (YTM) devrederek hesabı kapatmak"}
        ],
        "correct_answer": "C",
        "explanation": "Özkaynak tamamlama çağrısına süresi içinde uymayan müşterinin hesabındaki menkul kıymetler, aracı kurum tarafından hiçbir ihbara gerek olmaksızın re'sen satılarak kredi borcu kapatılır."
    },
    "q_1005_master_081": {
        "text": "Borsa İstanbul bünyesinde yapılan 'Ödünç Pay Piyasası' işlemlerinde ödünç verilen payların mülkiyeti kime geçer?",
        "options": [
            {"key": "A", "text": "Mülkiyet Takasbank nezdinde emanet kütüğünde kilitli kalır, hiç kimseye devrolmaz"},
            {"key": "B", "text": "Mülkiyet Borsa İstanbul A.Ş. tüzel kişiliğine intikal eder"},
            {"key": "C", "text": "Mülkiyet ödünç süresince aracı kurumun kendi aktiflerine tescil edilir"},
            {"key": "D", "text": "Mülkiyet ödünç süresi boyunca geçici olarak ödünç alana geçer; vade sonunda mislen iade edilir"},
            {"key": "E", "text": "Payların mülkiyeti ihraççı şirketin kurucu ortaklarına devredilir"}
        ],
        "correct_answer": "D",
        "explanation": "Ödünç işleminde ödünç konusu sermaye piyasası aracının mülkiyeti ödünç alana geçer. Ödünç alan vade sonunda aynı cins ve miktarda menkul kıymeti (mislen) ödünç verene iade etmekle yükümlüdür."
    },
    "q_1005_master_082": {
        "text": "Ödünç verilen bir hisse senedine ödünç süresi içinde nakit temettü (kâr payı) dağıtılması halinde bu temettünün ekonomik sahibi kimdir?",
        "options": [
            {"key": "A", "text": "Temettü doğrudan ödünç alan kişiye ait olur ve iade edilmez"},
            {"key": "B", "text": "Ödünç veren asıl pay sahibine aittir; ödünç alan bu tutarı ödünç verene tazmin etmekle yükümlüdür"},
            {"key": "C", "text": "Temettü tutarı Takasbank Garanti Fonu'na irat kaydedilir"},
            {"key": "D", "text": "Temettü dağıtımı ödünç sözleşmesi süresince dondurulur ve şirkette kalır"},
            {"key": "E", "text": "Temettü tutarı doğrudan Hazine ve Maliye Bakanlığı hesaplarına aktarılır"}
        ],
        "correct_answer": "B",
        "explanation": "Ödünç süresi içinde hissenin getirdiği nakit temettü, bedelsiz pay veya rüçhan haklarının tamamı ekonomik olarak ödünç verene aittir. Ödünç alan bu hakları ödünç verene aynen veya nakden tazmin etmek zorundadır."
    },
    "q_1005_master_083": {
        "text": "Bir aracı kurumun tek bir müşterisine kullandırabileceği kredili işlem tutarı kural olarak kurumun özsermayesinin en fazla yüzde kaçını aşamaz?",
        "options": [
            {"key": "A", "text": "%2"},
            {"key": "B", "text": "%5"},
            {"key": "C", "text": "%10 (Belirli istisnai risk gruplarında en fazla %25)"},
            {"key": "D", "text": "%35"},
            {"key": "E", "text": "%50"}
        ],
        "correct_answer": "C",
        "explanation": "Kredili İşlemler Tebliği uyarınca; bir aracı kurumun tek bir müşterisine açabileceği kredi tutarı aracı kurum özsermayesinin %10'unu (belirli grup şirketleri için azami %25'ini) aşamaz."
    },
    "q_1005_master_084": {
        "text": "Bir müşteriye kredili menkul kıymet alımı veya açığa satış yaptırılabilmesi için aşağıdaki sözleşmelerden hangisinin akdedilmesi kanunen ZORUNLUDUR?",
        "options": [
            {"key": "A", "text": "Yalnızca genel hesap açılış formu doldurulması ve sözlü onay alınması yeterlidir"},
            {"key": "B", "text": "Müşteri ile noter onaylı genel ticari vekaletname akdedilmesi zorunludur"},
            {"key": "C", "text": "Standart Çerçeve Sözleşmeye ek olarak 'Kredili Menkul Kıymet İşlemleri Çerçeve Sözleşmesi' imzalanması şarttır"},
            {"key": "D", "text": "Müşterinin Takasbank ile doğrudan ikili kredi garanti sözleşmesi imzalaması gerekir"},
            {"key": "E", "text": "Yalnızca banka kefaleti içeren borç senedi tanzim edilmesi yeterlidir"}
        ],
        "correct_answer": "C",
        "explanation": "Kredili menkul kıymet alımı, açığa satış ve ödünç işlemleri yapılabilmesi için müşteriyle standart alım-satım sözleşmesine ek olarak ayrı bir Kredili Menkul Kıymet İşlemleri Çerçeve Sözleşmesi imzalanması zorunludur."
    },
    "q_1005_master_090": {
        "text": "Yatırım kuruluşları nezdinde bulunan ve hak sahipleri tarafından aranmayan emanet ve alacaklar son işlem tarihinden itibaren kaç yıl sonra YTM'ye devredilir?",
        "options": [
            {"key": "A", "text": "1 yıl"},
            {"key": "B", "text": "3 yıl"},
            {"key": "C", "text": "5 yıl"},
            {"key": "D", "text": "10 yıl"},
            {"key": "E", "text": "20 yıl"}
        ],
        "correct_answer": "D",
        "explanation": "6362 sayılı Sermaye Piyasası Kanunu m.83 uyarınca; yatırım kuruluşları nezdinde hak sahipleri tarafından 10 yıl boyunca aranmayan her türlü emanet ve alacak Yatırımcı Tazmin Merkezi'ne (YTM) devredilir."
    },
    "q_1005_master_093": {
        "text": "Mali durumu bozulan ve taahhütlerini yerine getiremeyen yatırım kuruluşlarının malvarlığının tasfiyesi için SPK gözetiminde uygulanan özel hukuki sürece ne ad verilir?",
        "options": [
            {"key": "A", "text": "Konkordato İlanı"},
            {"key": "B", "text": "İflas Erteleme"},
            {"key": "C", "text": "Tahsisli Tasfiye"},
            {"key": "D", "text": "Tedrici Tasfiye"},
            {"key": "E", "text": "Kayyım Ataması"}
        ],
        "correct_answer": "D",
        "explanation": "6362 sayılı Kanun m.97 uyarınca; mali durumu bozulan yatırım kuruluşlarının müşteri haklarının korunması amacıyla SPK ve YTM tarafından tasfiye edilmesine 'Tedrici Tasfiye' denir."
    },
    "q_1005_master_095": {
        "text": "SPK, sermaye yeterliliği veya mevzuat ihlali nedeniyle bir yatırım kuruluşunun faaliyetlerini en fazla ne kadar süreyle geçici olarak durdurabilir?",
        "options": [
            {"key": "A", "text": "1 ay (en fazla 1 ay uzatılabilir)"},
            {"key": "B", "text": "3 ay (en fazla 3 ay uzatılabilir)"},
            {"key": "C", "text": "6 ay (gerektiğinde 6 ay daha uzatılabilir)"},
            {"key": "D", "text": "1 yıl (uzatılamaz)"},
            {"key": "E", "text": "2 yıl (kesin süreli)"}
        ],
        "correct_answer": "C",
        "explanation": "SPK, mevzuata aykırılık veya sermaye yetersizliği tespit edilen yatırım kuruluşlarının faaliyetlerini 6 aya kadar geçici olarak durdurabilir; bu süre gerektiğinde en fazla 6 ay daha uzatılabilir."
    },
    "q_1005_master_099": {
        "text": "Tüzel kişi müşteri hesaplarında şirketin arkasındaki yüzde kaçı aşan nihai gerçek kişi ortakların (UBO) kimlik tespiti MASAK ve SPK mevzuatı gereği zorunludur?",
        "options": [
            {"key": "A", "text": "%5'i aşan pay sahipleri"},
            {"key": "B", "text": "%10'u aşan pay sahipleri"},
            {"key": "C", "text": "%20'yi aşan pay sahipleri"},
            {"key": "D", "text": "%25'i aşan pay sahipleri"},
            {"key": "E", "text": "%51'i aşan pay sahipleri"}
        ],
        "correct_answer": "D",
        "explanation": "Suç gelirlerinin aklanmasının önlenmesi (MASAK) ve SPK mevzuatı uyarınca; tüzel kişi müşterilerde şirketin sermayesinin veya oy haklarının %25'ini aşan hisseye sahip nihai gerçek kişi faydalanıcıların (UBO) kimliklerinin tespit edilmesi kanunen mecburidir."
    },
    "q_1005_master_100": {
        "text": "Sermaye piyasası mevzuatına göre aşağıdakilerden hangisi 'Müşteri Sırrının İhlali' KAPSAMINDA SAYILMAZ?",
        "options": [
            {"key": "A", "text": "Müşterinin borsa işlem geçmişinin aynı gruptaki başka bir şirketin pazarlama birimiyle paylaşılması"},
            {"key": "B", "text": "SPK denetçileri, mahkemeler, savcılıklar ve MASAK'ın kanuni bilgi taleplerine resmi yanıt verilmesi"},
            {"key": "C", "text": "Müşterinin portföy büyüklüğünün ve nakit bakiyesinin aracı kurumun diğer müşterilerine açıklanması"},
            {"key": "D", "text": "Müşterinin açık yazılı rızası olmaksızın portföy dökümünün basın yayın organlarına iletilmesi"},
            {"key": "E", "text": "Kurum çalışanının işten ayrılırken müşteri emir ve pozisyon listesini üçüncü kişilere aktarması"}
        ],
        "correct_answer": "B",
        "explanation": "SPK, mahkemeler, savcılıklar, Hazine ve Maliye Bakanlığı ile MASAK gibi kanunen yetkili mercilere yasal yetkileri çerçevesinde bilgi ve belge verilmesi müşteri sırrının ihlali sayılmaz."
    },
    "q_1005_konu_007": {
        "text": "Kredili menkul kıymet hesabında teminat açığı oluşan bir müşterinin, hesabını yasal asgari özkaynak oranına (%35) getirebilmesi için yatırması gereken asgari nakit tutar nedir?",
        "options": [
            {"key": "A", "text": "2.500 TL"},
            {"key": "B", "text": "5.000 TL"},
            {"key": "C", "text": "7.500 TL"},
            {"key": "D", "text": "10.000 TL"},
            {"key": "E", "text": "15.000 TL"}
        ],
        "correct_answer": "D",
        "explanation": "Kredili işlemlerde özkaynak tamamlama çağrısı (Margin Call) yapıldığında müşteri, hesabını tekrar kanuni asgari özkaynak oranı olan %35 (veya sözleşmedeki sürdürme seviyesine) getirecek nakit veya kabul edilebilir menkul kıymeti yatırmakla yükümlüdür."
    },
    "q_1005_konu_015": {
        "text": "Aracı kurum genel müdür ve genel müdür yardımcılarının yasal olarak sahip olmaları gereken asgari mesleki deneyim süresi mali piyasalar veya işletmecilik alanında en az kaç yıldır?",
        "options": [
            {"key": "A", "text": "3 yıl"},
            {"key": "B", "text": "5 yıl"},
            {"key": "C", "text": "7 yıl"},
            {"key": "D", "text": "10 yıl"},
            {"key": "E", "text": "12 yıl"}
        ],
        "correct_answer": "C",
        "explanation": "SPK Yatırım Kuruluşları Tebliği uyarınca; aracı kurum genel müdür ve genel müdür yardımcılarının en az 7 yıllık mesleki deneyime ve Düzey 3 Lisansına sahip olmaları kanunen zorunludur."
    },
    "q_1005_ogretici_001": {
        "text": "Yatırım hizmet ve faaliyetleri kapsamında müşteri emirlerinin alınması ve iletilmesi faaliyeti temel olarak neyi amaçlar?",
        "options": [
            {"key": "A", "text": "Müşteri talimatlarının mevzuata uygun biçimde borsaya veya ilgili infaz kuruluşuna iletilmesini"},
            {"key": "B", "text": "Müşterinin sermaye piyasasındaki tüm yatırım risklerinin aracı kurumca üstlenilmesini"},
            {"key": "C", "text": "Kurumun kendi nam ve hesabına piyasada sürekli likidite ve kotasyon sağlamasını"},
            {"key": "D", "text": "Yatırımcının portföyündeki menkul kıymetlerin re'sen şirket ortaklarına devredilmesini"},
            {"key": "E", "text": "Müşteriye borsada gerçekleşecek tüm işlemler için kesin anapara kâr garantisi sunulmasını"}
        ],
        "correct_answer": "A",
        "explanation": "Emir iletimine aracılık; müşteriden alınan sermaye piyasası aracı alım veya satım emirlerinin borsa işlem sistemine veya yetkili diğer infaz kuruluşuna mevzuata uygun şekilde ulaştırılması faaliyetidir."
    },
    "q_1005_ogretici_004": {
        "text": "Yatırım kuruluşlarında uygulanan 'Yerindelik Testi'nin (Suitability) temel yasal amacı nedir?",
        "options": [
            {"key": "A", "text": "Müşterinin borsa işlemlerinden doğacak gelir vergisi kesintilerini hesaplamak"},
            {"key": "B", "text": "Aracı kurumun sermaye yeterliliği tabanını Borsa İstanbul'a raporlamak"},
            {"key": "C", "text": "Müşterinin kredi geçmişini inceleyerek bankalar arası limitini belirlemek"},
            {"key": "D", "text": "Portföy yönetimi ve yatırım danışmanlığında ürünün müşterinin mali gücüne ve risk profiline uygunluğunu ölçmek"},
            {"key": "E", "text": "Müşterinin yalnızca Merkezi Kayıt Kuruluşu (MKK) sicil kaydını oluşturmak"}
        ],
        "correct_answer": "D",
        "explanation": "Yerindelik testi; portföy yöneticiliği ve yatırım danışmanlığı kapsamında tavsiye edilecek ürün ve hizmetlerin müşterinin mali durumu, risk toleransı ve yatırım hedefleriyle tam örtüşüp örtüşmediğini denetler."
    },
    "q_1005_ogretici_005": {
        "text": "Yatırım hizmetlerinde 'Uygunluk Değerlendirmesi' (Appropriateness) yapılması ile ilgili temel kural nedir?",
        "options": [
            {"key": "A", "text": "Müşteriye yalnızca en yüksek komisyon getiren karmaşık türev ürünlerin tavsiye edilmesi"},
            {"key": "B", "text": "Müşterinin hiçbir bilgi ve tecrübesi sorgulanmaksızın tüm piyasalarda işlem yaptırılması"},
            {"key": "C", "text": "Müşteri profilinin yalnızca yılda bir defa vergi dairesi verilerine göre güncellenmesi"},
            {"key": "D", "text": "Değerlendirmenin yalnızca tüzel kişi müşteriler için yapılıp bireysel müşterilere uygulanmaması"},
            {"key": "E", "text": "Talep edilen ürünün içerdiği risklerin müşteri tarafından anlaşılıp anlaşılamayacağının tespiti"}
        ],
        "correct_answer": "E",
        "explanation": "Uygunluk testi; genel müşterilerin talep ettikleri ürün veya hizmetin barındırdığı riskleri kavrayabilecek düzeyde tecrübe ve finansal bilgiye sahip olup olmadığını ortaya koyar."
    },
    "q_1005_ogretici_007": {
        "text": "Kredili menkul kıymet işlemlerinin temel ekonomik ve finansal niteliği aşağıdakilerden hangisidir?",
        "options": [
            {"key": "A", "text": "Yatırımcının işlem tutarının tamamını hiçbir teminat yatırmaksızın finanse etmesi"},
            {"key": "B", "text": "Özkaynak üzerine borçlanma imkanı sağlanarak kaldıraç etkisiyle kâr ve zarar potansiyelinin katlanması"},
            {"key": "C", "text": "Piyasa dalgalanmalarından bağımsız olarak yatırımcının zarar ihtimalinin sıfırlanması"},
            {"key": "D", "text": "Yalnızca Hazine Müsteşarlığı tarafından ihraç edilen kamu iç borçlanma senetlerine uygulanabilmesi"},
            {"key": "E", "text": "İşlemin yapıldığı günün sonunda tüm borcun aracı kurumca hibeye dönüştürülmesi"}
        ],
        "correct_answer": "B",
        "explanation": "Kredili hisse senedi alımı; yatırımcının yatırdığı özkaynak oranına bağlı olarak kaldıraç oluşturur. Bu kaldıraç etkisi getiriyi artırabileceği gibi piyasa ters gittiğinde zararı da aynı oranda katlar."
    },
    "q_1005_ogretici_008": {
        "text": "Sermaye piyasasında 'Açığa Satış' (Short Sale) işleminin temel finansal tanımı ve işleyişi nedir?",
        "options": [
            {"key": "A", "text": "Portföyde fiziken mevcut olan hisse senetlerinin uzun vadeli temettü için tutulması"},
            {"key": "B", "text": "Halka açık şirketin genel kurul kararıyla sermayesini azaltarak pay iptal etmesi"},
            {"key": "C", "text": "Sahip olunmayan veya ödünç alınan sermaye piyasası aracının satılıp fiyat düşüşünde daha düşükten yerine konulması"},
            {"key": "D", "text": "Yatırım fonu katılma paylarının TEFAS üzerinden başka bir fona dönüştürülmesi"},
            {"key": "E", "text": "Şirket ortaklarının kendi paylarını halka arz yoluyla borsada satışa sunması"}
        ],
        "correct_answer": "C",
        "explanation": "Açığa satış; sahip olunmayan veya ödünç alınan menkul kıymetlerin fiyat düşüş beklentisiyle satılması ve bilahare piyasadan daha düşük fiyattan satın alınarak takas yükümlülüğünün kapatılması sürecidir."
    },
    "q_1005_ogretici_010": {
        "text": "Yatırım kuruluşlarında uzaktan (elektronik ortamda) müşteri kimlik tespiti yapılmasının temel amacı nedir?",
        "options": [
            {"key": "A", "text": "Yatırımcının kimlik doğrulama yükümlülüğünü tamamen ortadan kaldırmak"},
            {"key": "B", "text": "Müşterinin borsa işlemlerindeki piyasa riskini tamamen sıfıra indirmek"},
            {"key": "C", "text": "Müşteriden alınacak borsa payı ve komisyon oranlarını otomatik olarak silmek"},
            {"key": "D", "text": "Müşteri emirlerinin borsaya iletimini mesai saatleriyle sınırlamak"},
            {"key": "E", "text": "Güvenli biyometrik ve kriptografik yöntemlerle kimliği doğrulayarak uzaktan hukuki sözleşme kurmak"}
        ],
        "correct_answer": "E",
        "explanation": "Uzaktan kimlik tespiti tebliği; şubeye gitmeksizin NFC çipli kimlik kartı, canlılık ve yüz tanıma gibi güvenilir elektronik yöntemlerle müşteri kimliğinin doğrulanmasını ve sözleşme kurulmasını düzenler."
    },
    "q_1005_ogretici_014": {
        "text": "Yatırım kuruluşlarında 'Uygunluk Testi' ile 'Yerindelik Testi' arasındaki temel yasal fark hangisinde DOĞRU açıklanmıştır?",
        "options": [
            {"key": "A", "text": "Uygunluk testi yalnızca kurumsal nitelikli yatırımcılara, yerindelik testi ise yalnızca yabancı ülke vatandaşlarına uygulanır"},
            {"key": "B", "text": "İki test birbiriyle tamamen aynı içeriğe sahip olup kanundaki kullanım yerleri yalnızca şekli bir ayrımdan ibarettir"},
            {"key": "C", "text": "Yerindelik testi borsa işlemlerinde, uygunluk testi ise yalnızca vadeli mevduat ve sigorta poliçelerinde aranır"},
            {"key": "D", "text": "Uygunluk testi genel aracılıkta müşterinin ürün bilgi ve tecrübesini ölçerken; Yerindelik testi portföy yönetimi ve danışmanlıkta mali güç ve hedefleri de kapsar"},
            {"key": "E", "text": "Uygunluk testini geçemeyen müşteriye hesap açılması yasakken, yerindelik testinde müşterinin beyanı esas alınır"}
        ],
        "correct_answer": "D",
        "explanation": "Uygunluk testi genel alım-satım aracılığında müşterinin ürün bilgisi ve tecrübesini ölçer. Yerindelik testi ise bireysel portföy yönetimi ve yatırım danışmanlığında zorunlu olup müşterinin risk-getiri hedeflerini ve mali gücünü de kapsayan çok daha derin bir analizdir."
    },
    "q_1005_ogretici_018": {
        "text": "Aracı kurumların müşterilerine ait nakit ve menkul kıymet varlıkları ile ilgili 'Müşteri Varlıklarının Ayrılığı' ilkesi neyi emreder?",
        "options": [
            {"key": "A", "text": "Müşteri nakitlerinin aracı kurumun merkez ofisindeki fiziki şirket çelik kasasında saklanmasını"},
            {"key": "B", "text": "Kurum nakit darboğazına girdiğinde müşteri paralarını geçici şirket giderlerinde kullanabilmesini"},
            {"key": "C", "text": "Müşteri nakitlerinin Takasbank'ta, menkul kıymetlerin MKK'da müşteri bazında ayrı izlenip kurum aktifleriyle karıştırılamamasını"},
            {"key": "D", "text": "Tüm müşteri hisse senetlerinin aracı kurum hâkim ortağının şahsi hesabına virmanlanmasını"},
            {"key": "E", "text": "Müşteri nakit ve hisselerinin aracı kurumun kendi bilançosunda duran varlık olarak muhasebeleştirilmesini"}
        ],
        "correct_answer": "C",
        "explanation": "Müşteri Varlıklarının Ayrılığı ilkesi; müşterilere ait nakitlerin Takasbank nezdinde müşteri namına açılan hesaplarda nemalandırılmasını, menkul kıymetlerin ise MKK nezdinde hak sahibi bazında ayrı saklanmasını ve aracı kurumun borçları için haczedilemeyeceğini emreder."
    },
    "q_1005_ogretici_020": {
        "text": "Aracı kurumlarda 'Yatırım Danışmanlığı' hizmeti sunulabilmesi için aşağıdaki yasal koşullardan hangisi ZORUNLUDUR?",
        "options": [
            {"key": "A", "text": "Sosyal medya veya mesajlaşma grupları üzerinden anonim hesapla hisse tavsiyesi yayımlanması"},
            {"key": "B", "text": "Müşteriye borsada gerçekleştirilecek alım satımlar için kesin kâr ve anapara garantisi verilmesi"},
            {"key": "C", "text": "Hizmetin yalnızca aracı kurumun sermayesinde pay sahibi olan hâkim ortaklara sunulması"},
            {"key": "D", "text": "Danışmanlık yapacak personelin yalnızca üniversitelerin mühendislik bölümlerinden mezun olması"},
            {"key": "E", "text": "SPK'dan Yatırım Danışmanlığı yetki belgesi alınmış olması ve müşteriyle yazılı çerçeve sözleşmesi imzalanması"}
        ],
        "correct_answer": "E",
        "explanation": "Yatırım Danışmanlığı faaliyeti; SPK'dan yetki belgesi alınmasını, lisanslı uzman personel istihdam edilmesini ve müşteriyle yazılı yatırım danışmanlığı sözleşmesi imzalanmasını zorunlu kılar."
    },
    "q_1005_cikmis_010": {
        "text": "SPK Yatırım Hizmetleri Tebliği uyarınca 'Uygunluk Testi'nin (Appropriateness) temel amacı nedir?",
        "options": [
            {"key": "A", "text": "Müşterinin geçmiş vergi borçlarını ve gelir vergisi matrahını denetlemek"},
            {"key": "B", "text": "Müşterinin talep ettiği ürünün risklerini anlayabilecek bilgi ve tecrübeye sahip olup olmadığını değerlendirmek"},
            {"key": "C", "text": "Müşterinin bankalar nezdindeki kredi notunu yükselterek teminat limitini artırmak"},
            {"key": "D", "text": "Müşteriye gayrimenkul ve kıymetli maden yatırımı yapma zorunluluğu getirmek"},
            {"key": "E", "text": "Müşterinin borsa işlemlerindeki tüm getirisini aracı kurum kârına ortak etmek"}
        ],
        "correct_answer": "B",
        "explanation": "Uygunluk testi; genel müşterilerin talep ettikleri ürün veya hizmetin içerdiği riskleri anlayacak bilgi ve tecrübeye sahip olup olmadıklarını ortaya koyan resmi bir değerlendirme aracıdır."
    },
    "q_1005_cikmis_014": {
        "text": "Kredili işlem yapan bir müşterinin özkaynak tamamlama çağrısına (Margin Call) verilen sürede uymaması halinde aracı kurumun kanuni yetkisi nedir?",
        "options": [
            {"key": "A", "text": "Müşterinin tüm banka hesaplarını bloke ederek aracı kurum adına el koymak"},
            {"key": "B", "text": "Özkaynak oranını asgari yasal sınıra getirecek miktarda hisse senedini borsada re'sen satmak"},
            {"key": "C", "text": "Müşterinin borsa işlem yetkisini ve medeni haklarını mahkeme kararı olmadan süresiz dondurmak"},
            {"key": "D", "text": "Oluşan temerrüt borcunu Sermaye Piyasası Kurulu'nun genel bütçesine devretmek"},
            {"key": "E", "text": "Müşteri aleyhine aynı gün içinde doğrudan ceza davası açarak hapis talep etmek"}
        ],
        "correct_answer": "B",
        "explanation": "Özkaynak tamamlama çağrısına verilen sürede uymayan müşterinin kredili hisse senetleri, aracı kurum tarafından hiçbir ihbara gerek olmaksızın özkaynak oranını %50'ye tamamlayacak tutarda re'sen borsada satılır."
    },
    "q_1005_cikmis_022": {
        "text": "Nitelikli olmayan (genel) bireysel yatırımcıların bir takvim yılında paya dayalı kitle fonlaması yoluyla yapabilecekleri azami yatırım tutarı mevzuatta nasıl sınırlandırılmıştır?",
        "options": [
            {"key": "A", "text": "Sabit olarak hiçbir istisna olmaksızın en fazla 50.000 TL ile sınırlandırılmıştır"},
            {"key": "B", "text": "Beyan edilen yıllık net gelirin %10'u (Kurulca belirlenen azami yasal tavanı aşmamak kaydıyla)"},
            {"key": "C", "text": "Yatırımcının bankadaki toplam vadeli mevduat tutarının %50'si ile sınırlandırılmıştır"},
            {"key": "D", "text": "Yatırımcının son bir yıl içinde borsada yaptığı toplam işlem hacminin %25'i kadar"},
            {"key": "E", "text": "Kitle fonlamasında bireysel yatırımcılar için herhangi bir yasal üst sınır bulunmamaktadır"}
        ],
        "correct_answer": "B",
        "explanation": "Kitle Fonlaması Tebliği uyarınca; nitelikli olmayan gerçek kişi yatırımcılar bir takvim yılında beyan ettikleri yıllık net gelirin en fazla %10'unu (SPK'nın her yıl güncellediği azami tavanı aşmamak kaydıyla) yatırabilirler."
    }
}

updated = 0
for q in questions:
    qid = q['id']
    if qid in REPLACEMENTS_1005:
        rep = REPLACEMENTS_1005[qid]
        q['text'] = rep.get('text', q['text'])
        q['options'] = rep['options']
        q['correct_answer'] = rep['correct_answer']
        if 'explanation' in rep:
            q['explanation'] = rep['explanation']
        updated += 1
        print(f"Upgraded {qid}")

with open('src/data/all_questions.json', 'w', encoding='utf-8') as f:
    json.dump(questions, f, ensure_ascii=False, indent=2)

with open('src/data/questions_master.json', 'w', encoding='utf-8') as f:
    json.dump(questions, f, ensure_ascii=False, indent=2)

print(f"\nSuccessfully upgraded {updated} questions in Module 1005 to professional SPK exam standards!")
