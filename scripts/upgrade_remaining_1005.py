import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('src/data/all_questions.json', 'r', encoding='utf-8') as f:
    questions = json.load(f)

REMAINING_1005 = {
    "q_1005_master_003": {
        "text": "Dar Yetkili Aracı Kurumlar aşağıdaki yatırım hizmet ve faaliyetlerinden hangisini mevzuat gereği KESİNLİKLE YAPAMAZ?",
        "options": [
            {"key": "A", "text": "Yatırımcılara sermaye piyasası araçlarıyla ilgili genel tavsiyede bulunmak"},
            {"key": "B", "text": "Kendi adına veya müşteri nam ve hesabına emir icra etmek (İşlem ve Portföy Aracılığı)"},
            {"key": "C", "text": "Yurt içi piyasalarda müşteri emirlerini başka bir aracı kuruma iletmek (Emir İletimine Aracılık)"},
            {"key": "D", "text": "Finansal planlama ve genel piyasa araştırması bülteni yayımlamak"},
            {"key": "E", "text": "Halka arzlarda konsorsiyuma yalnızca emir iletici aracı kurum olarak katılmak"}
        ],
        "correct_answer": "B",
        "explanation": "Dar yetkili aracı kurumlar emirleri bizzat icra edemez (İşlem Aracılığı yapamaz), kendi nam ve hesabına işlem yapamaz (Portföy Aracılığı yapamaz); yalnızca emir iletimine aracılık yapabilirler."
    },
    "q_1005_master_012": {
        "text": "Aracı kurumların sahip olmak ve korumak zorunda olduğu asgari özsermaye yükümlülüğü ile ilgili hangisi DOĞRUDUR?",
        "options": [
            {"key": "A", "text": "Tüm aracı kurumlar yetki belgesi türüne bakılmaksızın aynı sabit özsermaye tutarını korumak zorundadır"},
            {"key": "B", "text": "Özsermaye tutarı, yürütülen faaliyetlerin gerektirdiği asgari sermaye tabanı ve risk karşılıkları toplamından az olamaz"},
            {"key": "C", "text": "Asgari özsermaye yükümlülüğü yalnızca takvim yılı sonlarında bağımsız denetim raporuyla aranır"},
            {"key": "D", "text": "Özsermaye açığı oluşan kurumlara SPK tarafından 2 yıl boyunca hiçbir yaptırım uygulanmaz"},
            {"key": "E", "text": "Kısmi yetkili kurumlar için özsermaye kuralı bulunmayıp yalnızca banka teminat mektubu yeterlidir"}
        ],
        "correct_answer": "B",
        "explanation": "Yatırım Kuruluşlarının Sermaye Yeterliliği Tebliği uyarınca; aracı kurumun özsermayesi, sahip olduğu yetki belgelerinin gerektirdiği asgari özsermaye tabanından ve pozisyon, karşı taraf, piyasa gibi risk karşılıkları toplamından az olamaz."
    },
    "q_1005_master_016": {
        "text": "Sermaye piyasası işlemlerinin risklerini açıklayan 'Genel Risk Bildirim Formu'nun müşteriye verilme usulü ve zamanlaması ile ilgili hangisi DOĞRUDUR?",
        "options": [
            {"key": "A", "text": "Müşterinin ilk borsa işleminde zarar etmesi durumunda takip eden 10 iş günü içinde tebliğ edilir"},
            {"key": "B", "text": "Yalnızca kredili işlem ve açığa satış yetkisi talep eden müşterilere hesap açılışından 1 ay sonra gönderilir"},
            {"key": "C", "text": "Yalnızca kurumsal profesyonel müşterilere iadeli taahhütlü posta yoluyla iletilir"},
            {"key": "D", "text": "Çerçeve sözleşmenin imzalanmasından önce veya imza anında müşteriye verilip içeriği açıklanarak imzalı teyidi alınır"},
            {"key": "E", "text": "Müşterinin talebi olmaksızın verilmesi aracı kurumlar açısından ticari sır ihlali sayılır"}
        ],
        "correct_answer": "D",
        "explanation": "Genel Risk Bildirim Formu, aracılık çerçeve sözleşmesinin imzalanmasından önce veya imza anında müşteriye verilmek, riskleri izah edilmek ve bir örneğinin teslim alındığına dair müşterinin imzalı teyidi alınmak zorundadır."
    },
    "q_1005_master_017": {
        "text": "Kaldıraçlı alım satım (Forex) işlemlerine aracılık edebilmek için aracı kurumun taşıması gereken yasal şart nedir?",
        "options": [
            {"key": "A", "text": "Dar Yetkili Aracı Kurum statüsünde bulunup yalnızca emir iletimi yetkisi almak"},
            {"key": "B", "text": "Yurt dışı bir aracı kurumun Türkiye'deki resmi temsilcisi sıfatını taşımak"},
            {"key": "C", "text": "Yalnızca banka iştiraki olan yatırım ortaklığı şeklinde anonim şirket kurmak"},
            {"key": "D", "text": "Kredili işlem ve açığa satış izinlerinin tamamından feragat etmiş olmak"},
            {"key": "E", "text": "SPK'dan Kaldıraçlı Alım Satım Yetki Belgesi almış olmak ve gerekli teminat altyapısını sağlamak"}
        ],
        "correct_answer": "E",
        "explanation": "Kaldıraçlı alım satım (Forex) işlemlerine aracılık edilebilmesi için SPK'dan ilgili yetki belgesinin alınması, müşteri teminatlarının Takasbank nezdinde izlenmesi ve gerekli sermaye/teknik altyapının sağlanması şarttır."
    },
    "q_1005_master_026": {
        "text": "Yatırım kuruluşu, müşterinin verdiği bir sermaye piyasası emrini aşağıdaki durumların hangisinde haklı olarak REDDEDEBİLİR?",
        "options": [
            {"key": "A", "text": "Müşterinin borsa işlemi için talep ettiği komisyon oranında indirim istemesi halinde"},
            {"key": "B", "text": "Müşterinin aynı gün içinde beşten fazla hisse senedinde işlem gerçekleştirmek istemesi halinde"},
            {"key": "C", "text": "Verilen emrin tutarının aracı kurumun aylık ortalama işlem hacminin altında kalması halinde"},
            {"key": "D", "text": "Müşterinin hesap açılışının üzerinden henüz altı ay geçmemiş olması durumunda"},
            {"key": "E", "text": "Emrin mevzuata veya borsa kurallarına aykırı olması, teminat açığı bulunması veya manipülasyon şüphesi taşıması halinde"}
        ],
        "correct_answer": "E",
        "explanation": "Yatırım kuruluşları; mevzuata veya borsa kurallarına açıkça aykırı olan, hesapta yeterli bakiye/teminat bulunmayan veya manipülasyon/içsel bilgi suistimali şüphesi taşıyan emirleri haklı olarak reddetmekle yükümlüdür."
    },
    "q_1005_master_035": {
        "text": "Müşterilere ait kaydi sermaye piyasası araçlarının saklanması kural olarak nerede ve nasıl gerçekleştirilir?",
        "options": [
            {"key": "A", "text": "Aracı kurumların merkez binalarındaki fiziki emanet kasalarında müşteri bazında saklanır"},
            {"key": "B", "text": "İlgili hisse senetlerini ihraç eden ortaklıkların kendi pay defterlerinde fiziken muhafaza edilir"},
            {"key": "C", "text": "Merkezi Kayıt Kuruluşu (MKK) nezdinde hak sahipleri adına açılan hesaplarda kayden izlenir"},
            {"key": "D", "text": "Yalnızca Borsa İstanbul A.Ş. Teftiş Kurulu Başkanlığı gözetimindeki havuz hesapta tutulur"},
            {"key": "E", "text": "Müşterinin ikamet ettiği yerdeki yerel ticaret odası veya sanayi odası sicilinde saklanır"}
        ],
        "correct_answer": "C",
        "explanation": "Kaydileştirilen sermaye piyasası araçları, hak sahipleri bazında elektronik ortamda Merkezi Kayıt Kuruluşu (MKK) nezdinde tutulan hesaplarda kayden izlenir."
    },
    "q_1005_master_036": {
        "text": "Kısmi yetkili aracı kurumların verebileceği 'Sınırlı Saklama Hizmeti'nin yasal kapsamı aşağıdakilerden hangisidir?",
        "options": [
            {"key": "A", "text": "Yatırım fonlarının ve emeklilik fonlarının portföy saklayıcılığını üstlenme yetkisi"},
            {"key": "B", "text": "Borsa İstanbul Kıymetli Madenler Piyasası nezdinde külçe altın saklama yetkisi"},
            {"key": "C", "text": "Yurt dışında yerleşik saklama kuruluşları nezdinde global saklama hesabı açma yetkisi"},
            {"key": "D", "text": "Yalnızca kendi aracılık ettiği işlemlerle sınırlı olarak müşteri varlıklarını Takasbank ve MKK nezdinde izleme yetkisi"},
            {"key": "E", "text": "Halka açık şirketlerin fiziki hisse senedi basımlarını aracılık sözleşmesi kapsamında yürütme yetkisi"}
        ],
        "correct_answer": "D",
        "explanation": "Sınırlı saklama yetkisi; aracı kurumun yalnızca kendi aracılık ettiği sermaye piyasası işlemlerinden doğan müşteri nakit ve kıymetlerini Takasbank ve MKK nezdinde kendi alt hesaplarında izleyebilmesini ifade eder."
    },
    "q_1005_master_052": {
        "text": "Bireysel portföy yöneticisi, müşterinin tüm portföyünü tek bir hisse senedine yatırabilir mi?",
        "options": [
            {"key": "A", "text": "Evet; portföy yöneticisi piyasadaki beklentilerine göre dilediği hisseye serbestçe yatırım yapabilir"},
            {"key": "B", "text": "Evet; hisse BIST 30 endeksinde yer alıyorsa risk dağıtımı yapma zorunluluğu kanunen aranmaz"},
            {"key": "C", "text": "Hayır; SPK düzenlemelerine göre hiçbir portföyde hisse oranı %10'un üzerine çıkarılamaz"},
            {"key": "D", "text": "Hayır; müşteriyle imzalanan çerçeve sözleşmedeki risk dağıtım ve yatırım stratejisi sınırlarına uyulmak zorundadır"},
            {"key": "E", "text": "Evet; yalnızca takvim yılının son çeyreğinde portföy kârını artırmak amacıyla tam yoğunlaşma yapılabilir"}
        ],
        "correct_answer": "D",
        "explanation": "Portföy yöneticisi, müşteriyle imzalanan Portföy Yönetim Sözleşmesinde kararlaştırılan yatırım stratejisine, risk profiline ve mevzuatın öngördüğü risk dağıtım kurallarına uymak zorundadır; keyfi yoğunlaşma yapamaz."
    },
    "q_1005_master_055": {
        "text": "Medyada veya internette sermaye piyasası yorumu yapan lisanslı uzmanların yayımlamak zorunda olduğu SPK yasal uyarı metninin temel amacı nedir?",
        "options": [
            {"key": "A", "text": "Paylaşılan analizlerin yatırımcılara kesin kâr sağlama taahhüdü içerdiğini beyan etmek"},
            {"key": "B", "text": "Bilgilerin kişiye özel yatırım danışmanlığı kapsamında olmayıp genel nitelikte olduğunu hatırlatmak"},
            {"key": "C", "text": "İlgili hisse senetlerinin SPK tarafından onaylanarak garanti altına alındığını bildirmek"},
            {"key": "D", "text": "Yalnızca yabancı para birimi cinsinden yatırım yapan kurumsal müşterilere hitap ettiğini açıklamak"},
            {"key": "E", "text": "Yorum yapan uzmanın ilgili şirkette doğrudan imtiyazlı pay sahibi olduğunu teyit etmek"}
        ],
        "correct_answer": "B",
        "explanation": "Mevzuat gereğince kamuya açık yorumlarda; yer alan bilgilerin kişiye özel yatırım danışmanlığı kapsamında olmadığı, genel yatırım tavsiyesi niteliğinde olup mali durum ve risk tercihlerine uymayabileceği uyarısı zorunludur."
    },
    "q_1005_master_059": {
        "text": "'Yerindelik Testi'nde (Suitability), uygunluk testine ek olarak müşterinin hangi kapsamlı bilgileri analiz edilir?",
        "options": [
            {"key": "A", "text": "Müşterinin yatırım amaçları, risk toleransı, mali durumu ve olası zararları karşılama kapasitesi"},
            {"key": "B", "text": "Müşterinin yalnızca adli sicil kaydı ve geçmiş ticari dava dosyaları"},
            {"key": "C", "text": "Müşterinin diğer bankalardaki vadesiz mevduat hesaplarının günlük faiz oranları"},
            {"key": "D", "text": "Müşterinin gayrimenkul varlıklarının ekspertiz ve tapu sicil kayıtları"},
            {"key": "E", "text": "Müşterinin ticaret siciline kayıtlı ortaklarının ikametgah bilgileri"}
        ],
        "correct_answer": "A",
        "explanation": "Yerindelik testi; portföy yöneticiliği ve yatırım danışmanlığı hizmetlerinde, müşterinin sadece bilgi ve tecrübesini değil; yatırım amaçlarını, risk-getiri tercihlerini ve mali durumunun zararı karşılama kapasitesini ölçer."
    },
    "q_1005_master_060": {
        "text": "Genel müşteri uygunluk testini doldurmaktan imtina ederse yatırım kuruluşu nasıl hareket eder?",
        "options": [
            {"key": "A", "text": "Müşterinin hesap açılışını iptal ederek durumu derhal cumhuriyet savcılığına bildirir"},
            {"key": "B", "text": "Test yapılmadığı için risk değerlendirmesi yapılamayacağını bildirir; müşteri yazılı talep ederse emri icra edebilir"},
            {"key": "C", "text": "Müşteriye mevzuat gereğince resen Profesyonel Müşteri statüsü tanıyarak işlem açar"},
            {"key": "D", "text": "Müşterinin varlıklarını hiçbir emir almaksızın otomatik olarak kamu hazine bonolarına yönlendirir"},
            {"key": "E", "text": "Aracı kurum testi müşteri yerine kendi belirleyeceği varsayımsal cevaplarla doldurur"}
        ],
        "correct_answer": "B",
        "explanation": "Müşterinin uygunluk testini doldurmaması halinde aracı kurum, hizmet veya ürünün uygunluğunun değerlendirilemeyeceğini müşteriye yazılı bildirir. Müşteri buna rağmen yazılı talepte bulunursa emir icra edilebilir."
    },
    "q_1005_master_076": {
        "text": "Aşağıdaki sermaye piyasası araçlarından hangisi kredili menkul kıymet işlemlerine KONU EDİLEMEZ?",
        "options": [
            {"key": "A", "text": "Borsa İstanbul tarafından kredili işlem yasağı getirilmiş paylar ve Yakın İzleme Pazarı hisseleri"},
            {"key": "B", "text": "BIST 50 endeksine dahil olan ve fiili dolaşım oranı yüksek şirket payları"},
            {"key": "C", "text": "Hazine ve Maliye Bakanlığı tarafından ihraç edilmiş Devlet İç Borçlanma Senetleri (DİBS)"},
            {"key": "D", "text": "Borsa İstanbul'da işlem gören hisse senedi yoğun Borsa Yatırım Fonu (BYF) katılma payları"},
            {"key": "E", "text": "Hazine garantisi taşıyan kamu kira sertifikaları ve Eurobond ihraçları"}
        ],
        "correct_answer": "A",
        "explanation": "Borsa İstanbul düzenlemeleri uyarınca; Yakın İzleme Pazarı'nda (Gözaltı Pazarı) işlem gören paylar ile tedbir getirilerek kredili alım yasağı konulan paylar kredili işleme konu edilemez."
    },
    "q_1005_master_078": {
        "text": "Açığa satış işlemlerinde uygulanan 'Yukarı Adım Kuralı' (Up-Tick Rule) ne anlama gelir?",
        "options": [
            {"key": "A", "text": "Açığa satış emrinin yalnızca borsa seansının açılış ve kapanış fiyat aralıklarında verilebilmesidir"},
            {"key": "B", "text": "Açığa satılacak pay miktarının gün içindeki toplam işlem hacminin %10'unu aşamaması kuralıdır"},
            {"key": "C", "text": "Satış emrinin doğrudan günün en yüksek tavan fiyatından sisteme iletilmesi zorunluluğudur"},
            {"key": "D", "text": "Açığa satış emrinin en son gerçekleşen işlem fiyatından daha yüksek bir fiyat seviyesinden verilmesi şartıdır"},
            {"key": "E", "text": "Açığa satış işleminden elde edilen nakit gelirin vadeli mevduatta nemalandırılması zorunluluğudur"}
        ],
        "correct_answer": "D",
        "explanation": "Yukarı Adım Kuralı (Up-Tick Rule); hisse fiyatlarının düşüş baskısını frenlemek amacıyla açığa satış emrinin en son gerçekleşen fiyattan daha yüksek bir fiyattan girilmesini zorunlu kılan kuraldır (son fiyat bir öncekinden yüksekse son fiyattan da girilebilir)."
    },
    "q_1005_master_083": {
        "text": "Bir aracı kurumun tek bir müşterisine kullandırabileceği kredili işlem tutarı kural olarak kurumun özsermayesinin en fazla yüzde kaçını aşamaz?",
        "options": [
            {"key": "A", "text": "%2 seviyesini"},
            {"key": "B", "text": "%5 seviyesini"},
            {"key": "C", "text": "%10 seviyesini (istisnai gruplarda azami %25)"},
            {"key": "D", "text": "%35 seviyesini"},
            {"key": "E", "text": "%50 seviyesini"}
        ],
        "correct_answer": "C",
        "explanation": "Kredili İşlemler Tebliği uyarınca; bir aracı kurumun tek bir müşterisine açabileceği kredi tutarı aracı kurum özsermayesinin %10'unu (belirli grup şirketleri için azami %25'ini) aşamaz."
    },
    "q_1005_master_084": {
        "text": "Bir müşteriye kredili menkul kıymet alımı veya açığa satış yaptırılabilmesi için aşağıdaki sözleşmelerden hangisinin akdedilmesi kanunen ZORUNLUDUR?",
        "options": [
            {"key": "A", "text": "Yalnızca genel hesap açılış formu doldurulması ve sözlü onay alınması yeterlidir"},
            {"key": "B", "text": "Müşteri ile banka teminat mektubu teslimine ilişkin protokol akdedilmesi zorunludur"},
            {"key": "C", "text": "Standart Çerçeve Sözleşmeye ek olarak 'Kredili Menkul Kıymet İşlemleri Çerçeve Sözleşmesi' imzalanması şarttır"},
            {"key": "D", "text": "Müşterinin Takasbank ile doğrudan ikili kredi garanti sözleşmesi imzalaması gerekir"},
            {"key": "E", "text": "Yalnızca banka kefaleti içeren borç senedi tanzim edilmesi yeterlidir"}
        ],
        "correct_answer": "C",
        "explanation": "Kredili menkul kıymet alımı, açığa satış ve ödünç işlemleri yapılabilmesi için müşteriyle standart alım-satım sözleşmesine ek olarak ayrı bir Kredili Menkul Kıymet İşlemleri Çerçeve Sözleşmesi imzalanması zorunludur."
    },
    "q_1005_master_087": {
        "text": "Yatırımcı Tazmin Merkezi (YTM) kanun uyarınca yatırımcıların hangi varlıklarını tazmin kapsamına alır?",
        "options": [
            {"key": "A", "text": "Kurumun iflası halinde müşteriye ait tevdi edilmiş hisse senedi, tahvil ve nakit varlıkları"},
            {"key": "B", "text": "Borsada işlem gören hisse senetlerinin piyasa fiyatının düşmesinden doğan sermaye kayıplarını"},
            {"key": "C", "text": "İhraççı şirketin genel kurulda kâr payı (temettü) dağıtmama kararından doğan getiri kayıplarını"},
            {"key": "D", "text": "Döviz kurlarındaki dalgalanmalar nedeniyle yabancı para varlıklarda oluşan kur zararlarını"},
            {"key": "E", "text": "Yatırım fonlarının negatif getiri sağlaması sonucunda portföyde oluşan dönemsel değer kayıplarını"}
        ],
        "correct_answer": "A",
        "explanation": "YTM; aracı kurum veya yatırım kuruluşunun iflası veya mali yapısının bozulması durumunda müşterilerine teslim edemediği hisse senedi, borçlanma aracı ve nakit alacaklarını mevzuattaki azami limit dahilinde tazmin eder. Piyasa fiyat hareketlerinden kaynaklanan zararlar asla tazmin edilmez."
    },
    "q_1005_master_094": {
        "text": "Bir aracı kurum hakkında SPK tarafından 'Tedrici Tasfiye' kararı verildiğinde hukuken aşağıdakilerden hangisi gerçekleşir?",
        "options": [
            {"key": "A", "text": "Kurumun tüm yönetim yetkisi Türkiye Sermaye Piyasaları Birliği Disiplin Kurulu'na devredilir"},
            {"key": "B", "text": "Kurum aleyhine icra takipleri durur, faizler kesilir ve kurumun idaresi YTM'ye geçer"},
            {"key": "C", "text": "Aracı kurum Borsa İstanbul Pay Piyasası'nda kendi adına portföy aracılığına devam eder"},
            {"key": "D", "text": "Kurumun sermayesi otomatik olarak Borsa İstanbul A.Ş.'nin özkaynaklarına aktarılır"},
            {"key": "E", "text": "Tüm müşteri alacakları hiçbir inceleme yapılmaksızın aynı gün Hazine tarafından ödenir"}
        ],
        "correct_answer": "B",
        "explanation": "Tedrici tasfiye kararı verildiğinde; kurumun yönetim ve denetimi YTM'ye geçer, kurum hakkındaki tüm icra ve haciz takipleri kanunen durur, faiz işlemesi sona erer ve tasfiye süreci başlar."
    },
    "q_1005_ogretici_003": {
        "text": "Bireysel Portföy Yöneticiliği faaliyetinin diğer yatırım hizmetlerinden temel ayırt edici yönü nedir?",
        "options": [
            {"key": "A", "text": "Müşteriye yalnızca borsa haber bültenlerinin ve şirket bilançolarının iletilmesi"},
            {"key": "B", "text": "Yatırımcıya gerçekleştirilecek her işlem için kesin anapara getiri taahhüdü verilmesi"},
            {"key": "C", "text": "Müşteriyle yapılan sözleşme çerçevesinde portföyün yönetici tarafından vekaleten bizzat yönetilmesi"},
            {"key": "D", "text": "Müşterinin her bir emir için seans anında yazılı onay verme zorunluluğunun bulunması"},
            {"key": "E", "text": "Portföydeki tüm menkul kıymetlerin doğrudan aracı kurumun kendi bilançosuna kaydedilmesi"}
        ],
        "correct_answer": "C",
        "explanation": "Bireysel Portföy Yöneticiliği; müşterinin sermaye piyasası araçlarından oluşan portföyünün, müşteriyle imzalanan sözleşme kapsamında vekil sıfatıyla yönetici tarafından doğrudan ve serbestçe yönetilmesidir."
    },
    "q_1005_ogretici_006": {
        "text": "Sermaye piyasası mevzuatında bir müşterinin 'Profesyonel Müşteri' olarak sınıflandırılmasının temel yasal sonucu nedir?",
        "options": [
            {"key": "A", "text": "Genel müşterilere tanınan bazı mevzuat korumalarından (örneğin uygunluk testi zorunluluğundan) muaf olması"},
            {"key": "B", "text": "Borsada gerçekleştireceği tüm alım satım işlemlerinde borsa payı ve vergilerden tamamen muaf tutulması"},
            {"key": "C", "text": "Aracı kurumlara olan tüm kredi ve komisyon borçlarının Yatırımcı Tazmin Merkezi'nce ödenmesi"},
            {"key": "D", "text": "Müşteri emirlerinin borsa emir defterinde diğer tüm emirlerin önüne geçirilerek öncelik kazanması"},
            {"key": "E", "text": "Müşteriye aracı kurumun genel kurul toplantılarına katılarak oy kullanma hakkı verilmesi"}
        ],
        "correct_answer": "A",
        "explanation": "Profesyonel müşteriler; piyasa bilgisine ve finansal tecrübeye sahip kabul edildiklerinden, genel müşterilere sunulan bazı koruma mekanizmalarından (risk bildirim formu, uygunluk testi gibi) muaf tutulurlar."
    },
    "q_1005_ogretici_012": {
        "text": "'Dar Yetkili Aracı Kurum' statüsündeki bir kuruluş aşağıda yer alan faaliyetlerden hangisini kanunen YÜRÜTEBİLİR?",
        "options": [
            {"key": "A", "text": "Kendi nam ve hesabına menkul kıymet alım satımı yapmak (Portföy Aracılığı)"},
            {"key": "B", "text": "Yurt içi piyasalarda müşteri emirlerini alarak başka bir yetkili aracı kuruma iletmek (Emir İletimi)"},
            {"key": "C", "text": "Halka arzlarda satılamayan payları satın alma taahhüdü vererek bakiye yükleniminde bulunmak"},
            {"key": "D", "text": "Müşterilere bireysel portföy yöneticiliği ve saklama hizmeti sunmak"},
            {"key": "E", "text": "Kaldıraçlı alım satım (Forex) işlemlerinde piyasa yapıcılığı üstlenmek"}
        ],
        "correct_answer": "B",
        "explanation": "Dar yetkili aracı kurumlar; yalnızca müşteri emirlerini alıp işlem aracılığı yapmaya yetkili başka bir aracı kuruma iletme (Emir İletimine Aracılık) faaliyetinde bulunabilirler."
    }
}

updated = 0
for q in questions:
    qid = q['id']
    if qid in REMAINING_1005:
        rep = REMAINING_1005[qid]
        q['text'] = rep.get('text', q['text'])
        q['options'] = rep['options']
        q['correct_answer'] = rep['correct_answer']
        if 'explanation' in rep:
            q['explanation'] = rep['explanation']
        updated += 1
        print(f"Upgraded remaining {qid}")

with open('src/data/all_questions.json', 'w', encoding='utf-8') as f:
    json.dump(questions, f, ensure_ascii=False, indent=2)

with open('src/data/questions_master.json', 'w', encoding='utf-8') as f:
    json.dump(questions, f, ensure_ascii=False, indent=2)

print(f"\nSuccessfully upgraded all {updated} remaining questions in Module 1005!")
