import json
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('src/data/all_questions.json', 'r', encoding='utf-8') as f:
    all_qs = json.load(f)

# Define 40 distinct, multi-angled, complementary questions for ogretici 011-020 in modules 1001, 1003, 1005, 1012
# These measure the exact same broad topics as 001-010, but from complementary angles:
# Legal exception, Numerical limits, Procedural hierarchy, Prohibitions, and Case scenarios.

NEW_OGRETICI_QUESTIONS = {
    # MODULE 1001: SERMAYE PİYASASI MEVZUATI
    "q_1001_ogretici_011": {
        "text": "6362 sayılı Sermaye Piyasası Kanunu uyarınca, Sermaye Piyasası Kurulu'nun (SPK) piyasa gözetimi ve denetimi yetkileri kapsamında aşağıdakilerden hangisi Kurul'un doğrudan alabileceği tedbirlerden biri DEĞİLDİR?",
        "options": [
            {"key": "A", "text": "Kanuna aykırı ihraç edilen sermaye piyasası araçlarının bedellerinin iadesi için dava açmak"},
            {"key": "B", "text": "Halka açık ortaklıkların tüm yönetim kurulu üyelerini hiçbir mahkeme kararı olmaksızın derhal kamu görevinden men etmek"},
            {"key": "C", "text": "Piyasa dolandırıcılığı şüphesi bulunan gerçek veya tüzel kişilerin borsa işlemlerini geçici veya sürekli yasaklamak"},
            {"key": "D", "text": "Hukuka aykırı faaliyet gösteren internet sitelerine erişimin engellenmesini BTK'dan talep etmek"},
            {"key": "E", "text": "İlgili şirket ve kuruluşların defter, kayıt ve bilgi işlem sistemlerini yerinde denetlemek"}
        ],
        "correct_answer": "B",
        "explanation": "SPK, kanuna aykırı işlemlerde dava açabilir, işlem yasağı koyabilir ve erişim engeli isteyebilir. Ancak şirket yöneticilerini doğrudan kamu görevinden azletme yetkisi bulunmaz; gerektiğinde mahkemeden yönetim kurulu üyelerinin görevden uzaklaştırılmasını veya kayyum atanmasını talep edebilir.",
        "topic": "SPK'nın Düzenleme ve Denetleme Yetkileri"
    },
    "q_1001_ogretici_012": {
        "text": "Sermaye piyasasında yatırımcıların aydınlatılması ve kamuyu aydınlatma ilkesi çerçevesinde onaylanan bir izahnamenin geçerlilik süresi kanunen ne kadardır?",
        "options": [
            {"key": "A", "text": "Onay tarihinden itibaren 30 gün"},
            {"key": "B", "text": "Onay tarihinden itibaren 6 ay"},
            {"key": "C", "text": "Ek ve değişikliklerin Kurulca onaylanması şartıyla, onay tarihinden itibaren 12 ay"},
            {"key": "D", "text": "Süresizdir, şirket faaliyetine devam ettiği sürece geçerlidir"},
            {"key": "E", "text": "Takvim yılı sonuna kadar (31 Aralık)"}
        ],
        "correct_answer": "C",
        "explanation": "6362 sayılı SPKn uyarınca onaylanan izahname, ilgili ek ve değişikliklerin Kurulca onaylanması koşuluyla onaylandığı tarihten itibaren 12 ay boyunca geçerlidir.",
        "topic": "İzahname Geçerlilik Süresi"
    },
    "q_1001_ogretici_013": {
        "text": "6362 sayılı Kanun m.106 uyarınca 'İçsel Bilgiye Dayalı Ticaret' (İnsider Trading) suçunun oluşabilmesi için aşağıdakilerden hangisi zorunlu bir yasal unsurdur?",
        "options": [
            {"key": "A", "text": "İşlemin yalnızca aracı kurum yönetim kurulu başkanı tarafından yapılması"},
            {"key": "B", "text": "Henüz kamuya açıklanmamış, doğrudan veya dolaylı sermaye piyasası aracının değerini etkileyebilecek nitelikteki bilgiye dayanarak menfaat temin edilmiş olması"},
            {"key": "C", "text": "Yapılan işlemin tutarının en az 10 milyon TL üzerinde olması"},
            {"key": "D", "text": "Şirketin yalnızca banka statüsünde bir kurum olması"},
            {"key": "E", "text": "İçsel bilginin yazılı olarak noter onaylı tebliğ edilmiş olması"}
        ],
        "correct_answer": "B",
        "explanation": "İçsel bilgi suçu; henüz kamuya duyurulmamış, fiyatı etkileyebilecek önemdeki gizli bilgiye dayanılarak işlem yapılması ve bu suretle haksız menfaat sağlanması veya zarardan kaçınılması ile oluşur.",
        "topic": "İçsel Bilgi Suçunun Unsurları"
    },
    "q_1001_ogretici_014": {
        "text": "Piyasa dolandırıcılığı (manipülasyon) eylemlerinde 6362 sayılı Kanun'da yer alan 'Etkin Pişmanlık' hükümlerinden faydalanmak isteyen bir kişi hakkında aşağıdakilerden hangisi DOĞRUDUR?",
        "options": [
            {"key": "A", "text": "Piyasa dolandırıcılığı suçlarında hiçbir aşamada etkin pişmanlık hükümleri uygulanamaz"},
            {"key": "B", "text": "Kurul tarafından henüz incelemeye başlanmadan önce durumu bildirerek elde ettiği menfaatin iki katını Hazineye öderse hakkında cezaya hükmolunmaz"},
            {"key": "C", "text": "Yalnızca hapis cezasının yarısı affedilir, adli para cezası aynen tahsil edilir"},
            {"key": "D", "text": "Mahkeme kararından 5 yıl sonra başvurulursa etkin pişmanlık uygulanır"},
            {"key": "E", "text": "Etkin pişmanlıktan yararlanmak için borsa üyeliğinden istifa etmek yeterlidir"}
        ],
        "correct_answer": "B",
        "explanation": "SPKn m.107/3 uyarınca; Kurul incelemeye başlamadan önce durumu Kurul'a ihbar eden ve elde ettiği menfaatin iki katı tutarı Hazineye ödeyen kişi hakkında cezaya hükmolunmaz (Soruşturma aşamasında öderse ceza indirimine gidilir).",
        "topic": "Manipülasyonda Etkin Pişmanlık"
    },
    "q_1001_ogretici_015": {
        "text": "Halka açık anonim ortaklıklarda 'Önemli Nitelikteki İşlemler' (örneğin tüm malvarlığının devri veya birleşme) genel kurulda onaylandığında, muhalefet şerhi koyduran pay sahiplerinin kullanabileceği yasal hak hangisidir?",
        "options": [
            {"key": "A", "text": "Yalnızca temettü avansı talep hakkı"},
            {"key": "B", "text": "Paylarını adil bedel karşılığında ortaklığa geri satarak çıkma hakkı (Ayrılma Hakkı)"},
            {"key": "C", "text": "Şirketin tüm yönetimini derhal tasfiye memurlarına devretme hakkı"},
            {"key": "D", "text": "Şirketin genel kurulunu iptal ederek borçlarını hükümsüz kılma hakkı"},
            {"key": "E", "text": "Borsa kotasyonunu tek taraflı durdurma hakkı"}
        ],
        "correct_answer": "B",
        "explanation": "Önemli nitelikteki işlemlere muhalif kalarak genel kurul tutanağına muhalefet şerhi işleten pay sahipleri, paylarını Kurul düzenlemelerine uygun adil bir bedelle şirkete satarak ortaklıktan ayrılma hakkına (SPKn m.24) sahiptir.",
        "topic": "Ayrılma Hakkı ve Önemli İşlemler"
    },
    "q_1001_ogretici_016": {
        "text": "Kurumsal Yönetim Tebliği (II-17.1) uyarınca BIST Yıldız Pazar'da işlem gören birinci grup halka açık ortaklıklarda bağımsız yönetim kurulu üyelerinin sayısı ve oranı en az ne kadar olmalıdır?",
        "options": [
            {"key": "A", "text": "Yönetim kurulu üye tam sayısının en az yarısı ve asgari 5 üye"},
            {"key": "B", "text": "Yönetim kurulu üye tam sayısının üçte birinden az olamaz ve her halükarda en az 2 kişi olmalıdır"},
            {"key": "C", "text": "Yalnızca 1 üye olması yeterlidir"},
            {"key": "D", "text": "Yönetim kurulundaki tüm üyelerin bağımsız olması zorunludur"},
            {"key": "E", "text": "Bağımsız üye bulundurma zorunluluğu tamamen isteğe bağlıdır"}
        ],
        "correct_answer": "B",
        "explanation": "Kurumsal Yönetim İlkeleri gereğince, yönetim kurulu içindeki bağımsız üye sayısı toplam üye sayısının üçte birinden (1/3) az olamaz ve her durumda en az iki üyeden oluşmalıdır.",
        "topic": "Bağımsız Yönetim Kurulu Üyeleri"
    },
    "q_1001_ogretici_017": {
        "text": "6362 sayılı Kanun uyarınca Yatırım Fonu malvarlığı ile ilgili olarak aşağıda yer alan temel yasal koruma hükümlerinden hangisi DOĞRUDUR?",
        "options": [
            {"key": "A", "text": "Fon malvarlığı kurucunun veya portföy saklayıcısının borçları nedeniyle haczedilemez, rehin edilemez ve iflas masasına dahil edilemez"},
            {"key": "B", "text": "Kurucu şirket iflas ederse fon varlıkları kurucunun ticari borçlularına dağıtılır"},
            {"key": "C", "text": "Fon katılma payları yatırımcı adına değil, yalnızca fon yöneticisi adına kayden izlenir"},
            {"key": "D", "text": "Fon malvarlığı Takasbank tarafından rehin alınarak serbestçe kredi teminatı yapılabilir"},
            {"key": "E", "text": "Yatırım fonu katılma belgeleri Türk Ticaret Kanunu uyarınca fiziki nama yazılı basılır"}
        ],
        "correct_answer": "A",
        "explanation": "SPKn m.53 uyarınca 'Malvarlığı Ayrılığı İlkesi' geçerlidir: Fon malvarlığı kurucunun ve portföy saklayıcısının malvarlığından tamamen ayrıdır; kamu alacakları dahil hiçbir borç için haczedilemez, iflas masasına dahil edilemez.",
        "topic": "Yatırım Fonunda Malvarlığı Ayrılığı"
    },
    "q_1001_ogretici_018": {
        "text": "Türkiye Sermaye Piyasaları Birliği (TSPB) Disiplin Yönetmeliği kapsamında üye aracı kurum ve çalışanlara verilebilecek disiplin cezalarının hafiften ağıra doğru sıralanışı hangisidir?",
        "options": [
            {"key": "A", "text": "Uyarı - Kınama - Para Cezası - Geçici Olarak Faaliyetten Alıkoyma - Birlik Üyeliğinden Çıkarma"},
            {"key": "B", "text": "Hapis Cezası - Adli Para Cezası - Kınama"},
            {"key": "C", "text": "Yalnızca İhtar ve İflas Bildirimi"},
            {"key": "D", "text": "Kınama - Şirketi Kapatma - Kayyum Atama"},
            {"key": "E", "text": "Uyarı - Borsa Kotundan Çıkarma - İflas"}
        ],
        "correct_answer": "A",
        "explanation": "TSPB disiplin cezaları kademeli olarak: Uyarı, Kınama, Para Cezası, Geçici Faaliyetten Alıkoyma ve Birlik Üyeliğinden Çıkarma (İhraç) şeklinde kanuni yaptırımlara bağlanmıştır.",
        "topic": "TSPB Disiplin Cezaları Hiyerarşisi"
    },
    "q_1001_ogretici_019": {
        "text": "Sermaye Piyasası Kanunu'na göre, borsada işlem gören halka açık ortaklıkların kayıtlı sermaye sisteminde yönetim kuruluna verilen sermaye artırma yetkisi en fazla kaç yıl için geçerlidir?",
        "options": [
            {"key": "A", "text": "1 yıl"},
            {"key": "B", "text": "2 yıl"},
            {"key": "C", "text": "En fazla 5 yıl"},
            {"key": "D", "text": "10 yıl"},
            {"key": "E", "text": "Süresizdir"}
        ],
        "correct_answer": "C",
        "explanation": "Kayıtlı sermaye sisteminde esas sözleşmeyle yönetim kuruluna tanınan tavan içinde sermaye artırma yetki süresi en fazla 5 yıldır. Süre bitiminde genel kuruldan yeni 5 yıllık izin alınması gerekir.",
        "topic": "Kayıtlı Sermaye Yetki Süresi"
    },
    "q_1001_ogretici_020": {
        "text": "Kamuyu Aydınlatma Platformu'na (KAP) yapılacak 'Özel Durum Açıklamaları' ile ilgili olarak ertelenmiş bir bilginin kamuya açıklanması zorunluluğu ne zaman doğar?",
        "options": [
            {"key": "A", "text": "Erteleme gerekçeleri ortadan kalkar kalkmaz veya bilginin gizliliği korunamadığı (sızdığı) anda derhal"},
            {"key": "B", "text": "İlgili yılın yıllık olağan genel kurul toplantısında"},
            {"key": "C", "text": "SPK başkanının şahsen yazılı talimatı ulaştıktan 30 gün sonra"},
            {"key": "D", "text": "Şirketin bağımsız denetim raporu onaylandıktan sonra"},
            {"key": "E", "text": "Hiçbir zaman kamuya açıklanması zorunlu değildir"}
        ],
        "correct_answer": "A",
        "explanation": "Özel Durumlar Tebliği (II-15.1) uyarınca; ortaklık meşru menfaatlerini korumak için bilgiyi ertelemiş olsa bile, erteleme sebebi kalktığında veya bilginin gizliliği bozulduğunda (fısıltı/haber çıkması halinde) derhal KAP açıklaması yapılmalıdır.",
        "topic": "KAP Açıklaması ve Erteleme Esasları"
    },

    # MODULE 1003: SERMAYE PİYASASI ARAÇLARI
    "q_1003_ogretici_011": {
        "text": "Anonim ortaklıklarda nama yazılı paylar ile hamiline yazılı payların Borsa İstanbul Pay Piyasası'nda işlem görmesi ve devri açısından temel kural nedir?",
        "options": [
            {"key": "A", "text": "Borsada işlem gören payların tamamı MKK nezdinde kaydileştirilmiş olmak zorundadır ve fiziki senet devri yapılamaz"},
            {"key": "B", "text": "Hamiline yazılı paylar borsada işlem göremez, sadece nama yazılı paylar işlem görür"},
            {"key": "C", "text": "Nama yazılı pay devirleri mutlaka mahkeme sicil onayına tabidir"},
            {"key": "D", "text": "Borsa payları noter huzurunda ciro edilerek elden teslim edilir"},
            {"key": "E", "text": "Yabancı yatırımcılar yalnızca hamiline yazılı pay satın alabilir"}
        ],
        "correct_answer": "A",
        "explanation": "6362 sayılı Kanun m.13 uyarınca borsada işlem gören paylar kaydileştirilmiştir; MKK nezdinde hak sahipleri bazında elektronik ortamda izlenir, fiziki teslimat veya zilyetlik devri söz konusu olamaz.",
        "topic": "Kaydi Paylar ve Devir Esasları"
    },
    "q_1003_ogretici_012": {
        "text": "Halka açık anonim ortaklıklarda esas sözleşme ile paylara 'Oyda İmtiyaz' tanınması durumunda SPK düzenlemelerine göre uygulanacak yasal azami sınır nedir?",
        "options": [
            {"key": "A", "text": "Bir paya en fazla 15 oy hakkı tanınabilir"},
            {"key": "B", "text": "Sınırsızdır, bir paya 1000 oy dahi verilebilir"},
            {"key": "C", "text": "Halka açık ortaklıklarda hiçbir şekilde oyda imtiyaz tanınamaz"},
            {"key": "D", "text": "Sadece genel kurul onaylarsa en fazla 3 oy verilebilir"},
            {"key": "E", "text": "Oyda imtiyaz sadece kamu payları için geçerlidir"}
        ],
        "correct_answer": "A",
        "explanation": "SPKn m.18 uyarınca halka açık ortaklıklarda oyda imtiyaz tanınması halinde, bir paya tanınabilecek azami oy hakkı 15 oydur (Kurulca muafiyet tanınan durumlar saklıdır).",
        "topic": "Oyda İmtiyaz Sınırı"
    },
    "q_1003_ogretici_013": {
        "text": "Bedelli sermaye artırımında ortakların yeni pay alma hakkını (rüçhan hakkı) kullanabilmeleri için tanınması gereken kanuni asgari ve azami süreler hangileridir?",
        "options": [
            {"key": "A", "text": "En az 15 gün, en fazla 60 gün"},
            {"key": "B", "text": "En az 3 gün, en fazla 7 gün"},
            {"key": "C", "text": "En az 1 ay, en fazla 1 yıl"},
            {"key": "D", "text": "Her durumda sabit 10 iş günü"},
            {"key": "E", "text": "En az 90 gün, en fazla 180 gün"}
        ],
        "correct_answer": "A",
        "explanation": "Ortakların bedelli sermaye artırımında yeni pay alma haklarını kullanma süresi esas sözleşmede veya yönetim kurulu kararında belirtilmek kaydıyla en az 15 gün, en fazla 60 gün olarak belirlenir.",
        "topic": "Rüçhan Hakkı Süre Sınırları"
    },
    "q_1003_ogretici_014": {
        "text": "Tahvil ihraç eden bir anonim ortaklığın finansal durumu ile tahvil sahiplerinin hukuki konumu bakımından aşağıdakilerden hangisi KESİNLİKLE YANLIŞTIR?",
        "options": [
            {"key": "A", "text": "Tahvil sahibi şirketin alacaklısıdır, şirket kâr etmese dahi faiz ve anapara alacağını talep etme hakkı vardır"},
            {"key": "B", "text": "Tahvil sahipleri şirketin genel kurul toplantılarına katılarak oy kullanma ve temettü alma hakkına sahiptir"},
            {"key": "C", "text": "Şirketin tasfiyesi halinde tahvil alacaklıları, pay sahiplerinden önce tasfiye bakiyesinden alacağını tahsil eder"},
            {"key": "D", "text": "Tahviller sabit veya değişken faizli olarak ihraç edilebilir"},
            {"key": "E", "text": "Tahvillerin vadesi en az 1 yıl (365 gün) olmak zorundadır"}
        ],
        "correct_answer": "B",
        "explanation": "Tahvil sahipleri ortaklığın pay sahibi değil, alacaklısıdır. Bu nedenle şirket genel kurulunda oy kullanma, yönetime katılma veya temettü alma hakları bulunmaz; sadece anapara ve faiz alacağı talep ederler.",
        "topic": "Tahvil Sahibinin Hukuki Hakları"
    },
    "q_1003_ogretici_015": {
        "text": "Kira Sertifikaları (Sukuk) Tebliği'ne göre, ihraç edilen kira sertifikalarının dayanağı olan varlık veya hakların devredildiği ve münhasıran bu amaçla kurulan tüzel kişilik hangisidir?",
        "options": [
            {"key": "A", "text": "Varlık Kiralama Şirketi (VKŞ)"},
            {"key": "B", "text": "Yatırımcı Tazmin Merkezi (YTM)"},
            {"key": "C", "text": "Kredi Kayıt Bürosu (KKB)"},
            {"key": "D", "text": "Merkezi Takas Kuruluşu"},
            {"key": "E", "text": "Varlık Yönetim Şirketi (TMSF)"}
        ],
        "correct_answer": "A",
        "explanation": "Kira sertifikaları münhasıran Sermaye Piyasası Kurulu'ndan izin alınarak anonim şirket şeklinde kurulan Varlık Kiralama Şirketleri (VKŞ) tarafından ihraç edilir.",
        "topic": "Varlık Kiralama Şirketi ve Sukuk"
    },
    "q_1003_ogretici_016": {
        "text": "VİOP'ta işlem gören Vadeli İşlem (Futures) ve Opsiyon (Options) sözleşmelerinde takas güvencesini sağlamak üzere alınan 'Başlangıç Teminatı' pozisyon süresince hangi seviyenin altına düşerse yatırımcıya 'Teminat Tamamlama Çağrısı' (Margin Call) yapılır?",
        "options": [
            {"key": "A", "text": "Sürdürme Teminatı seviyesinin altına düştüğünde"},
            {"key": "B", "text": "Nominal değerin %10'una ulaştığında"},
            {"key": "C", "text": "BIST100 endeksi %5 düştüğünde"},
            {"key": "D", "text": "Vade bitimine 3 gün kaldığında"},
            {"key": "E", "text": "Yalnızca pozisyon kapatıldığında"}
        ],
        "correct_answer": "A",
        "explanation": "Ters fiyat hareketleri sonucu hesap bakiyesi Sürdürme Teminatı (Maintenance Margin) seviyesinin altına düşerse, Takasbank tarafından aracı kuruma ve yatırımcıya teminatı başlangıç seviyesine tamamlaması için Teminat Tamamlama Çağrısı yapılır.",
        "topic": "VİOP Teminat Tamamlama Çağrısı"
    },
    "q_1003_ogretici_017": {
        "text": "Varantlar (Warrants) ile VİOP Opsiyon Sözleşmeleri karşılaştırıldığında aşağıdakilerden hangisi Varantların ayırt edici bir özelliğidir?",
        "options": [
            {"key": "A", "text": "Varantlar menkul kıymet niteliğinde olup yalnızca ihraççı kurum tarafından ihraç edilir ve teminat tamamlama çağrısı (Margin Call) bulunmaz"},
            {"key": "B", "text": "Varantlarda yatırımcının zararı sınırsızdır"},
            {"key": "C", "text": "Varantlar hiçbir şekilde Borsa İstanbul'da işlem göremez"},
            {"key": "D", "text": "Varant alıcısı sözleşme karşılığında fiziki altın teslim etmek zorundadır"},
            {"key": "E", "text": "Varantların vadesi en az 10 yıl olmak zorundadır"}
        ],
        "correct_answer": "A",
        "explanation": "Varantlar menkul kıymetleştirilmiş türev araçlardır. Alıcı sadece ödediği primi riske atar, zararı primle sınırlıdır ve vadeli işlemlerdeki gibi teminat tamamlama (margin call) mekanizması işlemez.",
        "topic": "Varantların Ayırt Edici Özellikleri"
    },
    "q_1003_ogretici_018": {
        "text": "Gayrimenkul Yatırım Ortaklıkları (GYO) ile ilgili olarak portföy sınırlamaları ve kazanç istisnası bakımından aşağıdakilerden hangisi DOĞRUDUR?",
        "options": [
            {"key": "A", "text": "GYO'lar kurumlar vergisinden muaftır ve portföylerinin en az %51'i gayrimenkul ve gayrimenkule dayalı haklardan oluşmalıdır"},
            {"key": "B", "text": "GYO'lar sadece altın ve kıymetli maden yatırımı yapmak zorundadır"},
            {"key": "C", "text": "GYO portföyünde hiçbir şekilde nakit veya mevduat bulundurulamaz"},
            {"key": "D", "text": "GYO'ların halka açılma zorunluluğu bulunmaz, tamamen kapalı kalabilirler"},
            {"key": "E", "text": "GYO payları Takasbank güvencesi dışındadır"}
        ],
        "correct_answer": "A",
        "explanation": "Kurumlar Vergisi Kanunu m.5/1-d uyarınca GYO kazançları kurumlar vergisinden istisnadır. SPK düzenlemelerine göre GYO portföyünün en az %51'i gayrimenkul, gayrimenkul projeleri ve haklardan oluşmak zorundadır.",
        "topic": "GYO Portföy Sınırlamaları ve Vergi İstisnası"
    },
    "q_1003_ogretici_019": {
        "text": "Borsa Yatırım Fonları (BYF / ETF) paylarının işlem görme biçimi geleneksel menkul kıymet yatırım fonlarından hangi temel yönüyle ayrılır?",
        "options": [
            {"key": "A", "text": "Geleneksel fonlar gün sonunda tek fiyattan (NAD) işlem görürken, BYF payları borsa seans saatleri boyunca hisse senedi gibi anlık piyasa fiyatından alınıp satılır"},
            {"key": "B", "text": "BYF'ler sadece devlet bankaları tarafından satın alınabilir"},
            {"key": "C", "text": "BYF katılma payları hiçbir şekilde borsaya kote edilemez"},
            {"key": "D", "text": "Geleneksel fonlar seans içinde anlık işlem görürken BYF'ler ayda bir fiyatlanır"},
            {"key": "E", "text": "BYF'lerde portföy yöneticisi bulunması kanunen yasaktır"}
        ],
        "correct_answer": "A",
        "explanation": "Borsa Yatırım Fonları (BYF); borsa pay piyasasında sürekli müzayede sistemiyle seans süresince hisse senedi gibi anlık fiyatlarla işlem görür. Geleneksel fonlar ise TEFAS'ta gün sonu açıklanan tek net aktif değer (NAD) üzerinden takaslanır.",
        "topic": "BYF ile Geleneksel Fon Farkları"
    },
    "q_1003_ogretici_020": {
        "text": "Varlığa Dayalı Menkul Kıymetler (VDMK) ihracında teminat havuzuna alınabilecek alacak türleri arasında aşağıdakilerden hangisi YER ALAMAZ?",
        "options": [
            {"key": "A", "text": "Tüketici, konut ve taşıt kredisi alacakları"},
            {"key": "B", "text": "Finansal kiralama (leasing) sözleşmelerinden doğan gelecekteki kira alacakları"},
            {"key": "C", "text": "Şirket yönetim kurulu başkanının şahsi kumar ve bahis borç senetleri"},
            {"key": "D", "text": "İhracat işlemlerinden doğan faturalı ticari alacaklar"},
            {"key": "E", "text": "İpotekli konut finansmanı alacakları"}
        ],
        "correct_answer": "C",
        "explanation": "VDMK teminat havuzuna sadece SPK tebliğinde açıkça sayılan meşru, temlik edilebilir tüketici, konut, ihracat, faktoring ve leasing gibi ticari ve finansal alacaklar dahil edilebilir; şahsi gayrimeşru alacaklar konu edilemez.",
        "topic": "VDMK Teminat Havuzu Nitelikleri"
    },

    # MODULE 1005: YATIRIM KURULUŞLARI
    "q_1005_ogretici_011": {
        "text": "Yatırım Kuruluşlarının Kuruluş ve Faaliyet Esasları Tebliği (III-39.1) uyarınca, yetki belgelerine göre aracı kurumların sınıflandırılması hangisinde DOĞRU verilmiştir?",
        "options": [
            {"key": "A", "text": "Dar Yetkili - Kısmi Yetkili - Geniş Yetkili Aracı Kurumlar"},
            {"key": "B", "text": "A Grubu - B Grubu - C Grubu Bankalar"},
            {"key": "C", "text": "Mahalli - Bölgesel - Uluslararası Kurumlar"},
            {"key": "D", "text": "Anonim - Limited - Komandit Yatırım Şirketleri"},
            {"key": "E", "text": "Birincil - İkincil - Üçüncül Brokerlar"}
        ],
        "correct_answer": "A",
        "explanation": "Tebliğ uyarınca aracı kurumlar icra edebilecekleri yatırım hizmet ve faaliyetlerinin kapsamına ve asgari özsermaye şartlarına göre: Dar Yetkili, Kısmi Yetkili ve Geniş Yetkili olmak üzere üç kategoriye ayrılır.",
        "topic": "Aracı Kurumların Yetki Sınıflandırması"
    },
    "q_1005_ogretici_012": {
        "text": "Aracı kurumlarda 'Dar Yetkili Aracı Kurum' statüsündeki bir kuruluş aşağıda yer alan faaliyetlerden hangisini KESİNLİKLE GERÇEKLEŞTİREMEZ?",
        "options": [
            {"key": "A", "text": "Emir İletimine Aracılık (Acentelik)"},
            {"key": "B", "text": "En İyi Gayret Aracılığıyla Halka Arz"},
            {"key": "C", "text": "Kendi nam ve hesabına Portföy Aracılığı yapmak ve Kredili Alım / Açığa Satış işlemi gerçekleştirmek"},
            {"key": "D", "text": "Genel yatırım tavsiyesi sunmak"},
            {"key": "E", "text": "Sermaye piyasası araçları hakkında tanıtım faaliyetinde bulunmak"}
        ],
        "correct_answer": "C",
        "explanation": "Dar yetkili aracı kurumlar kendi nam ve hesaplarına işlem (portföy aracılığı) yapamaz, müşteriye kredi açamaz ve açığa satış yaptıramaz; yalnızca emir iletimine ve en iyi gayret halka arzına aracılık edebilir.",
        "topic": "Dar Yetkili Kurumların Faaliyet Yasakları"
    },
    "q_1005_ogretici_013": {
        "text": "Kredili menkul kıymet alımı, açığa satış ve ödünç alma işlemlerinde mevzuat uyarınca yatırımcının sağlaması gereken asgari 'Başlangıç Özkaynak Oranı' yüzde kaçtır?",
        "options": [
            {"key": "A", "text": "%10"},
            {"key": "B", "text": "%20"},
            {"key": "C", "text": "%35"},
            {"key": "D", "text": "%50"},
            {"key": "E", "text": "%75"}
        ],
        "correct_answer": "C",
        "explanation": "Seri: V, No: 65 Tebliği uyarınca, kredili menkul kıymet alımı ve açığa satış işlemlerinde müşterinin temin etmesi gereken asgari başlangıç özkaynak oranı %35'tir (Sürdürme özkaynak oranı ise asgari %20'dir).",
        "topic": "Kredili İşlemlerde Özkaynak Oranları"
    },
    "q_1005_ogretici_014": {
        "text": "Yatırım kuruluşlarında 'Uygunluk Testi' (Suitability) ile 'Yerindelik Testi' (Appropriateness) arasındaki temel yasal fark hangisinde DOĞRU açıklanmıştır?",
        "options": [
            {"key": "A", "text": "Uygunluk testi genel emir iletimi ve alım-satım aracılığında müşterinin ürün bilgisini ölçer; Yerindelik testi ise Portföy Yöneticiliği ve Yatırım Danışmanlığı hizmetlerinde mali güç ve yatırım amaçlarını da kapsayacak biçimde zorunludur"},
            {"key": "B", "text": "Uygunluk testi sadece yabancılara yapılır, yerindelik testi sadece şirketlere yapılır"},
            {"key": "C", "text": "İki test arasında hiçbir yasal fark yoktur, isimleri eşanlamlıdır"},
            {"key": "D", "text": "Yerindelik testi yalnızca 18 yaşından küçükler için uygulanır"},
            {"key": "E", "text": "Uygunluk testini geçemeyen müşteriye hesap açılması kanunen suçtur"}
        ],
        "correct_answer": "A",
        "explanation": "Uygunluk testi genel alım-satım aracılığında ürünün bilgi ve tecrübeyle uyumunu ölçer. Yerindelik testi ise daha kapsamlı olup portföy yöneticiliği ve yatırım danışmanlığında müşterinin mali durumu ve risk tercihine uygunluğunu belirlemek için zorunludur.",
        "topic": "Uygunluk Testi vs Yerindelik Testi"
    },
    "q_1005_ogretici_015": {
        "text": "Sermaye Piyasası Kurulu düzenlemelerine göre 'Profesyonel Müşteri' tanımı kapsamında aşağıdakilerden hangisi doğrudan Profesyonel Müşteri KABUL EDİLMEZ?",
        "options": [
            {"key": "A", "text": "Bankalar ve aracı kurumlar"},
            {"key": "B", "text": "Emeklilik yatırım fonları ve sigorta şirketleri"},
            {"key": "C", "text": "Hiçbir finansal varlığı ve piyasa tecrübesi bulunmayan ev hanımı veya öğrenci"},
            {"key": "D", "text": "Aktif toplamı 50 milyon TL, yıllık net hasılatı 90 milyon TL üzerinde olan şirketler"},
            {"key": "E", "text": "Kolektif yatırım kuruluşları ve portföy yönetim şirketleri"}
        ],
        "correct_answer": "C",
        "explanation": "Finansal kuruluşlar, kurumsal yatırımcılar ve kanunda belirtilen aktif/özsermaye/hasılat eşiklerini aşan şirketler doğrudan Profesyonel Müşteridir. Bireysel perakende yatırımcılar ise aksi yazılı talep edilip şartlar sağlanmadıkça 'Genel Müşteri' statüsündedir.",
        "topic": "Profesyonel Müşteri Kriterleri"
    },
    "q_1005_ogretici_016": {
        "text": "Aracı kurumlarda 'İç Kontrol Sistemi' ve 'İç Denetim Birimi' yöneticileri kurumsal hiyerarşide kural olarak doğrudan kime bağlı olarak görev yaparlar?",
        "options": [
            {"key": "A", "text": "Doğrudan aracı kurum Yönetim Kurulu'na veya Denetimden Sorumlu Komiteye"},
            {"key": "B", "text": "En çok işlem hacmi yapan borsa brokerına"},
            {"key": "C", "text": "Borsa İstanbul Genel Müdürlüğü'ne"},
            {"key": "D", "text": "Pazarlama ve Satış Departmanı Müdürüne"},
            {"key": "E", "text": "Takasbank Operasyon Şefine"}
        ],
        "correct_answer": "A",
        "explanation": "İç kontrol, iç denetim ve risk yönetiminden sorumlu birimler bağımsızlıklarının korunması amacıyla icracı birimlerden ayrı tutulur ve doğrudan Yönetim Kurulu'na veya Yönetim Kurulu adına yetkilendirilen Denetim Komitesine bağlıdır.",
        "topic": "İç Denetim Biriminin Bağlılığı"
    },
    "q_1005_ogretici_017": {
        "text": "Kaldıraçlı alım satım (Forex / FX) işlemlerinde SPK mevzuatı gereğince aracı kurumların müşterilerine uygulayabileceği azami yasal kaldıraç oranı kaçtır?",
        "options": [
            {"key": "A", "text": "1:10 (Yatırılan teminatın en fazla 10 katı)"},
            {"key": "B", "text": "1:100"},
            {"key": "C", "text": "1:400"},
            {"key": "D", "text": "1:2"},
            {"key": "E", "text": "Kaldıraç sınırı bulunmaz, serbestçe belirlenir"}
        ],
        "correct_answer": "A",
        "explanation": "SPK düzenlemeleri uyarınca yurt içi kaldıraçlı alım satım (Forex) işlemlerinde uygulanabilecek azami yasal kaldıraç oranı 1:10 ile sınırlandırılmış olup asgari başlangıç teminatı şartı bulunmaktadır.",
        "topic": "Forex Kaldıraç Sınırı"
    },
    "q_1005_ogretici_018": {
        "text": "Aracı kurumların müşterilerine ait nakit ve menkul kıymet varlıklarını saklama biçimi ile ilgili 'Müşteri Varlıklarının Ayrılığı' ilkesi neyi emreder?",
        "options": [
            {"key": "A", "text": "Müşterilere ait nakitler Takasbank nezdindeki müşteri hesaplarında, menkul kıymetler ise MKK nezdinde müşteri bazında ayrı izlenir; kurumun kendi aktifleriyle karıştırılamaz"},
            {"key": "B", "text": "Müşteri nakitleri aracı kurumun şirket kasasında fiziki nakit olarak tutulmalıdır"},
            {"key": "C", "text": "Kurum nakit sıkışıklığına düşerse müşteri paralarını geçici olarak kendi şirket giderlerinde kullanabilir"},
            {"key": "D", "text": "Tüm hisse senetleri aracı kurum genel müdürünün şahsi hesabına tescil edilir"},
            {"key": "E", "text": "Müşteri varlıkları noter emanetine tevdi edilmek zorundadır"}
        ],
        "correct_answer": "A",
        "explanation": "SPKn m.46 uyarınca yatırım kuruluşları müşteri varlıklarını kendi malvarlığından ayrı tutmak zorundadır. Nakitler Takasbank'ta müşteri adına, menkul kıymetler ise MKK'da alt hesaplarda takip edilir.",
        "topic": "Müşteri Varlıklarının Ayrılığı"
    },
    "q_1005_ogretici_019": {
        "text": "Aracı kurumların sermaye yeterliliği tabanının hesaplanmasında aşağıdakilerden hangisi özkaynaklardan bir indirim kalemi (risk karşılığı) olarak dikkate alınır?",
        "options": [
            {"key": "A", "text": "Pozisyon riski, karşı taraf riski, piyasa riski ve operasyonel risk karşılıkları"},
            {"key": "B", "text": "Yalnızca şirketin ödenmiş sermayesi"},
            {"key": "C", "text": "Kira gelirleri ve temettü tahsilatları"},
            {"key": "D", "text": "Müşterilerin portföy büyüklüğü"},
            {"key": "E", "text": "Takasbank Para Piyasası faiz oranları"}
        ],
        "correct_answer": "A",
        "explanation": "Sermaye yeterliliği hesaplamalarında aracı kurumun özkaynak tabanı; pozisyon riski, karşı taraf riski, döviz kuru riski ve operasyonel risk karşılıkları toplamından düşük olamaz.",
        "topic": "Sermaye Yeterliliği ve Risk Karşılıkları"
    },
    "q_1005_ogretici_020": {
        "text": "Aracı kurumlarda 'Yatırım Danışmanlığı' hizmeti sunulabilmesi için aşağıdaki yasal koşullardan hangisi ZORUNLUDUR?",
        "options": [
            {"key": "A", "text": "SPK'dan Yatırım Danışmanlığı yetki belgesi alınmış olması ve müşteri ile yazılı çerçeve sözleşmesi imzalanması"},
            {"key": "B", "text": "Sosyal medya üzerinden anonim hesapla hisse tavsiyesi verilmesi"},
            {"key": "C", "text": "Müşteriye mutlaka kesin kâr garantisi taahhüt edilmesi"},
            {"key": "D", "text": "Yalnızca yabancı bankalara danışmanlık verilmesi"},
            {"key": "E", "text": "Danışmanın noter katibi unvanına sahip olması"}
        ],
        "correct_answer": "A",
        "explanation": "Yatırım danışmanlığı faaliyeti; Kurul'dan yetki belgesi alınarak, lisanslı uzmanlarca ve müşteri ile yazılı bir sözleşme akdedilerek icra edilir. Kâr garantisi verilmesi kesinlikle yasaktır.",
        "topic": "Yatırım Danışmanlığı Yetki Şartları"
    },

    # MODULE 1012: TAKAS VE SAKLAMA
    "q_1012_ogretici_011": {
        "text": "Borsa İstanbul Pay Piyasası'nda gerçekleştirilen hisse senedi alım satım işlemlerinin standart nakit ve menkul kıymet takas süresi kural olarak nedir?",
        "options": [
            {"key": "A", "text": "T+0 (Aynı gün akşamı)"},
            {"key": "B", "text": "T+2 (İşlem gününü izleyen İKİNCİ iş günü)"},
            {"key": "C", "text": "T+5 (İşlem gününü izleyen beşinci iş günü)"},
            {"key": "D", "text": "T+30 (İşlem ayının son iş günü)"},
            {"key": "E", "text": "Her cuma akşamı topluca"}
        ],
        "correct_answer": "B",
        "explanation": "BIST Pay Piyasasında standart takas dönemi T+2'dir; yani pazartesi günü gerçekleşen bir işlemin takas ve teslim yükümlülüğü çarşamba günü sonuçlandırılır.",
        "topic": "Standart Takas Süresi T+2"
    },
    "q_1012_ogretici_012": {
        "text": "Takasbank'ın 'Merkezi Karşı Taraf' (CCP) sıfatıyla hizmet verdiği piyasalarda bir üye aracı kurum temerrüde düştüğünde (borcunu ödeyemediğinde) Takasbank'ın işlettiği 'Temerrüt Kaynakları Kullanım Hiyerarşisi' nasıldır?",
        "options": [
            {"key": "A", "text": "Önce temerrüt eden üyenin teminatları ve katkı payı -> Sonra Takasbank'ın özkaynak katkısı -> Sonra diğer üyelerin Garanti Fonu katkı payları"},
            {"key": "B", "text": "Önce masum diğer üyelerin paraları -> Sonra mahkeme kararı"},
            {"key": "C", "text": "Tüm borsa işlemleri süresiz iptal edilir"},
            {"key": "D", "text": "Yalnızca Merkez Bankası kaynakları kullanılır"},
            {"key": "E", "text": "Zarar doğrudan hisse senedini satan yatırımcıya yüklenir"}
        ],
        "correct_answer": "A",
        "explanation": "CCP temerrüt yönetiminde Takasbank 'Temerrüt Şelalesi'ni (Default Waterfall) işletir: Sırasıyla temerrüde düşen üyenin marjin teminatları ve garanti fonu payı kullanılır, yetmezse Takasbank'ın önceden taahhüt ettiği sermaye payı, o da yetmezse diğer üyelerin fon payları devreye girer.",
        "topic": "Temerrüt Yönetim Hiyerarşisi (Default Waterfall)"
    },
    "q_1012_ogretici_013": {
        "text": "Merkezi Kayıt Kuruluşu (MKK) nezdinde kaydileştirilen hisse senetleri üzerinde yatırımcıların hak sahipliğini ispat etmelerini sağlayan temel kayıt ilkesi nedir?",
        "options": [
            {"key": "A", "text": "MKK nezdindeki elektronik kayıtlar kurucu nitelikte olup hak sahipliği bu kayıtlara göre belirlenir"},
            {"key": "B", "text": "Yatırımcının elindeki basılı matbu sertifika her zaman MKK kaydından üstündür"},
            {"key": "C", "text": "Yalnızca şirketin pay defterine ıslak imza atılması hak kazandırır"},
            {"key": "D", "text": "MKK kayıtları sadece istatistik amaçlıdır, hukuki geçerliliği yoktur"},
            {"key": "E", "text": "Hisse devri için Borsa İstanbul binasına gidip onaylatmak gerekir"}
        ],
        "correct_answer": "A",
        "explanation": "6362 sayılı Kanun m.13 uyarınca kaydi sermaye piyasası araçlarına ilişkin haklar MKK nezdinde oluşturulan hesap kayıtlarına dayanır. Bu kayıtlar hak sahipliğini ispata yarayan tek yetkili kurucu hukuki sicildir.",
        "topic": "MKK Kayıtlarının Hukuki Niteliği"
    },
    "q_1012_ogretici_014": {
        "text": "Yatırımcı Tazmin Merkezi (YTM) hangi durumların ortaya çıkması halinde aracı kurumlardaki yatırımcıların varlıklarını kanuni tazmin limitine kadar korumakla yükümlüdür?",
        "options": [
            {"key": "A", "text": "Yatırımcının borsa fiyatlarındaki düşüş nedeniyle zarar etmesi halinde"},
            {"key": "B", "text": "Yatırım kuruluşunun iflası veya hakkında tedrici tasfiye kararı verilmesi halinde nakit ve menkul kıymet teslim borçlarının karşılanamaması durumunda"},
            {"key": "C", "text": "Şirketin kâr payı dağıtmaması durumunda"},
            {"key": "D", "text": "Hisse senedi fiyatının taban yapması durumunda"},
            {"key": "E", "text": "Yatırımcının kredi kartı borçlarını ödeyememesi durumunda"}
        ],
        "correct_answer": "B",
        "explanation": "YTM piyasadaki piyasa riski veya yatırım zararını değil; aracı kuruluşun mali acze düşmesi, iflası veya tasfiyesi nedeniyle yatırımcılara ait hisse ve nakitleri tevdi edememesi durumundaki dolandırıcılık/mali yetersizlik riskini tazmin eder.",
        "topic": "YTM Tazmin Kapsamı"
    },
    "q_1012_ogretici_015": {
        "text": "Takas işlemlerinde 'Teslim Karşılığı Ödeme' (Delivery Versus Payment - DVP) ilkesi temel olarak hangi risk türünü tamamen ortadan kaldırmayı amaçlar?",
        "options": [
            {"key": "A", "text": "Enflasyon riskini"},
            {"key": "B", "text": "Anapara/Temerrüt Riskini (Principal Risk / Karşı tarafın menkul kıymeti alıp parayı ödememesi riskini)"},
            {"key": "C", "text": "Faiz oranlarının yükselmesi riskini"},
            {"key": "D", "text": "Şirketin fabrika makinelerinin arızalanması riskini"},
            {"key": "E", "text": "Döviz kurunun dalgalanması riskini"}
        ],
        "correct_answer": "B",
        "explanation": "DVP prensibi; nakit ödeme ile menkul kıymet tesliminin Takasbank ve MKK sisteminde eşzamanlı takaslanmasıdır. Biri gerçekleşmeden diğeri gerçekleşmez, böylece parayı verip hisseyi alamama (temerrüt/anapara) riski sıfırlanır.",
        "topic": "DVP ve Anapara Riski"
    },
    "q_1012_ogretici_016": {
        "text": "MKK nezdinde kayden izlenen hisse senetleri üzerinde temettü, bedelli/bedelsiz sermaye artırımı ve kupon ödemesi gibi 'Hak Kullanımı' (Corporate Actions) işlemleri kim tarafından yürütülür?",
        "options": [
            {"key": "A", "text": "MKK ve Takasbank işbirliğiyle elektronik havuz hesapları üzerinden otomatik olarak hak sahiplerinin hesaplarına aktarılır"},
            {"key": "B", "text": "Yatırımcıların bizzat şirket genel merkezine giderek elden nakit tahsil etmesiyle"},
            {"key": "C", "text": "Noter kanalıyla tebligat gönderilerek"},
            {"key": "D", "text": "Yalnızca Vergi Dairesi memurları tarafından"},
            {"key": "E", "text": "Her yatırımcının kendi banka şubesinden çek yazmasıyla"}
        ],
        "correct_answer": "A",
        "explanation": "Hak kullanım süreçleri; ihraççı şirket, MKK ve Takasbank sistemleri arasında entegre olarak yürütülür. Temettü ve yeni paylar hak kullanım günü doğrudan yatırımcının aracı kurumdaki hesabına otomatik yansıtılır.",
        "topic": "Elektronik Hak Kullanımı Süreçleri"
    },
    "q_1012_ogretici_017": {
        "text": "Takasbank Para Piyasası (TPP) ile ilgili olarak aşağıda yer alan temel operasyonel kurallardan hangisi DOĞRUDUR?",
        "options": [
            {"key": "A", "text": "Üyeler nakit borçlanabilmek için Takasbank'a mevzuatça kabul edilen menkul kıymet teminatı vermek zorundadır ve işlemler çok taraflı kör havuzda eşleşir"},
            {"key": "B", "text": "TPP'de hiçbir teminat verilmeden sınırsız borçlanılabilir"},
            {"key": "C", "text": "Yalnızca gerçek kişiler kendi aralarında borç alıp verebilir"},
            {"key": "D", "text": "TPP faiz oranları her yıl başında sabitlenir, yıl boyu değişmez"},
            {"key": "E", "text": "Takasbank bu piyasada hiçbir şekilde merkezi takas hizmeti sunmaz"}
        ],
        "correct_answer": "A",
        "explanation": "TPP; üyelerin likidite ihtiyaçlarını Takasbank'ın belirlediği teminatlar (DİBS, BIST payları, döviz, nakit) karşılığında ve kör havuzda anonim olarak karşıladığı organize para piyasasıdır.",
        "topic": "Takasbank Para Piyasası İşleyişi"
    },
    "q_1012_ogretici_018": {
        "text": "Borsa İstanbul Pay Piyasası'nda açığa satış yapan veya takas günü teslim yükümlülüğünü karşılayamayan bir aracı kurumun başvurabileceği organize Takasbank piyasası hangisidir?",
        "options": [
            {"key": "A", "text": "Ödünç Pay Piyasası (ÖPA)"},
            {"key": "B", "text": "Döviz Efektif Piyasası"},
            {"key": "C", "text": "Vadeli İşlem ve Opsiyon Piyasası"},
            {"key": "D", "text": "Hazine Müsteşarlığı İhale Sistemi"},
            {"key": "E", "text": "Yatırımcı Tazmin Merkezi Havuz Hesabı"}
        ],
        "correct_answer": "A",
        "explanation": "Ödünç Pay Piyasası (ÖPA); pay piyasasında açığa satış yapan veya takas yükümlülüğünü yerine getirmek için hisse senedine ihtiyaç duyan üyelerin, belirli bir komisyon ve teminat karşılığında hisse ödünç alabildiği Takasbank piyasasıdır.",
        "topic": "Ödünç Pay Piyasası (ÖPA)"
    },
    "q_1012_ogretici_019": {
        "text": "MKK sistemi üzerinde yatırımcıların kendi portföylerindeki payların bilgileri dışında başka hesaplara transfer edilmesini engellemek üzere kullanabildikleri güvenlik özelliği hangisidir?",
        "options": [
            {"key": "A", "text": "e-YATIRIMCI Yatırımcı Blokajı Hizmeti"},
            {"key": "B", "text": "Borsa Kotundan Çıkarma Talimatı"},
            {"key": "C", "text": "İflas Masası Devir Protokolü"},
            {"key": "D", "text": "Kamu Aydınlatma Platformu Şifresi"},
            {"key": "E", "text": "Fiziki Senet Talep Formu"}
        ],
        "correct_answer": "A",
        "explanation": "MKK e-YATIRIMCI uygulaması üzerinden yatırımcılar 'Yatırımcı Blokajı' koyarak aracı kurum dahil hiç kimsenin kendi rızası dışında payları transfer edememesini sağlar; işlem yapacağı zaman blokajı kendisi kaldırır.",
        "topic": "MKK Yatırımcı Blokajı"
    },
    "q_1012_ogretici_020": {
        "text": "Merkezi Saklama Kuruluşu (MKK) nezdinde 10 yıl boyunca hiçbir işlem görmeyen ve hak sahipleri tarafından aranmayan zamanaşımına uğramış sermaye piyasası araçları ve temettüler nereye aktarılır?",
        "options": [
            {"key": "A", "text": "Yatırımcı Tazmin Merkezi'ne (YTM) devredilerek emanet ve gelir kaydedilir"},
            {"key": "B", "text": "Doğrudan aracı kurumun kendi kâr hanesine kaydedilir"},
            {"key": "C", "text": "İlgili şirketin genel müdürüne bağışlanır"},
            {"key": "D", "text": "Tamamen yok sayılarak imha edilir"},
            {"key": "E", "text": "Borsa İstanbul yönetim kurulu üyelerine dağıtılır"}
        ],
        "correct_answer": "A",
        "explanation": "6362 sayılı Kanun m.83 uyarınca; yatırım kuruluşları ve ortaklıklar nezdinde 10 yıl süreyle aranmayan her türlü sermaye piyasası aracı, temettü ve alacaklar zamanaşımına uğrayarak Yatırımcı Tazmin Merkezi'ne (YTM) intikal eder.",
        "topic": "Zamanaşımı ve YTM'ye Devir"
    }
}

# Update all matching questions
updated_count = 0
for q in all_qs:
    qid = q['id']
    if qid in NEW_OGRETICI_QUESTIONS:
        new_data = NEW_OGRETICI_QUESTIONS[qid]
        q['text'] = new_data['text']
        q['options'] = new_data['options']
        q['correct_answer'] = new_data['correct_answer']
        q['explanation'] = new_data['explanation']
        q['topic'] = new_data['topic']
        updated_count += 1

print(f"Successfully upgraded {updated_count} questions with advanced multi-angled questions!")

# Re-run abbreviation enrichment to make sure the newly authored questions also get their definitions
from enrich_abbreviations_and_diversify import ABBREVIATIONS

for q in all_qs:
    full_text = q['text'] + ' ' + ' '.join(opt['text'] for opt in q['options']) + ' ' + q.get('explanation', '')
    found_abbrs = []
    for abbr, desc in ABBREVIATIONS.items():
        pattern = r'\b' + re.escape(abbr) + r'\b'
        if re.search(pattern, full_text):
            found_abbrs.append((abbr, desc))
            
    if found_abbrs:
        expl = q.get('explanation', '')
        if "📌 Soruda Geçen Kısaltmalar" in expl or "📌 Terim & Kısaltma Sözlüğü" in expl:
            expl = re.split(r'\n+📌', expl)[0].strip()
            
        glossary_lines = ["\n\n📌 Soruda Geçen Kısaltmalar & Terimler:"]
        for abbr, desc in found_abbrs:
            glossary_lines.append(f"• {abbr}: {desc}")
            
        q['explanation'] = expl + '\n'.join(glossary_lines)

# Save updated files
with open('src/data/all_questions.json', 'w', encoding='utf-8') as f:
    json.dump(all_qs, f, ensure_ascii=False, indent=2)

with open('src/data/questions_master.json', 'w', encoding='utf-8') as f:
    json.dump([q for q in all_qs if q.get('source') == 'master'], f, ensure_ascii=False, indent=2)

print("Saved updated questions data files successfully!")
