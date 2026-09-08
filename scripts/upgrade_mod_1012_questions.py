import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('src/data/all_questions.json', 'r', encoding='utf-8') as f:
    questions = json.load(f)

# Comprehensive replacement dictionary for Module 1012
REPLACEMENTS_1012 = {
    # 1. q_1012_master_001
    "q_1012_master_001": {
        "text": "Sermaye piyasasında 'Takas' (Settlement / Clearing) işlemi aşağıdakilerden hangisini ifade eder?",
        "options": [
            {"key": "A", "text": "Halka açık şirketlerin genel kurullarında pay sahiplerine kâr payı dağıtılması sürecidir"},
            {"key": "B", "text": "Aracı kurumların müşterilerine özkaynak karşılığı kredili menkul kıymet tahsis etmesidir"},
            {"key": "C", "text": "İhraççı şirketlerin bedelli sermaye artırımı amacıyla SPK'ya izahname sunması işlemidir"},
            {"key": "D", "text": "Hisse senetlerinin Borsa İstanbul kotasyon yönergesi uyarınca pazar değiştirmesi sürecidir"},
            {"key": "E", "text": "Borsada gerçekleşen işlemlerden doğan kıymet teslim ve nakit ödeme borçlarının tasfiye edilmesidir"}
        ],
        "correct_answer": "E",
        "explanation": "Takas; borsada veya teşkilatlanmış piyasalarda alım satımı yapılan sermaye piyasası araçlarının teslimi ile bunların bedellerinin ödenmesine ilişkin borç ve alacakların karşılıklı olarak tasfiye edilip sonuçlandırılması sürecidir."
    },

    # 2. q_1012_master_009
    "q_1012_master_009": {
        "text": "Takasbank mevzuatına göre takas üyeleri yetki ve sorumlulukları bakımından hangi iki temel gruba ayrılır?",
        "options": [
            {"key": "A", "text": "Doğrudan Takas Üyesi (DCM) ve Genel Takas Üyesi (GCM)"},
            {"key": "B", "text": "Bireysel Takas Üyesi ve Kurumsal Takas Üyesi"},
            {"key": "C", "text": "Yerli Takas Üyesi ve Yabancı Takas Üyesi"},
            {"key": "D", "text": "Kısa Vadeli Takas Üyesi ve Uzun Vadeli Takas Üyesi"},
            {"key": "E", "text": "Teminatlı Takas Üyesi ve Teminatsız Takas Üyesi"}
        ],
        "correct_answer": "A",
        "explanation": "Takasbank Merkezi Karşı Taraf mevzuatında üyeler; yalnızca kendi ve müşterilerinin işlemlerini takas eden 'Doğrudan Takas Üyesi' (Direct Clearing Member) ve diğer aracı kuruluşların işlemlerinin takasını da üstlenebilen 'Genel Takas Üyesi' (General Clearing Member) olarak ikiye ayrılır."
    },

    # 3. q_1012_master_013
    "q_1012_master_013": {
        "text": "Yatırımcıların VİOP veya teminat hesaplarında bulunan nakit Türk Lirası bakiyeleri Takasbank tarafından nasıl değerlendirilir?",
        "options": [
            {"key": "A", "text": "Vadesiz hesapta bloke edilerek faizsiz ve nemasız olarak bekletilir"},
            {"key": "B", "text": "Doğrudan Hazine ve Maliye Bakanlığı'nın genel bütçesine gelir kaydedilir"},
            {"key": "C", "text": "Yalnızca yurt dışı tezgahüstü türev piyasalarda arbitraj amacıyla kullanılır"},
            {"key": "D", "text": "Takasbank Para Piyasası veya repo/ters repoda nemalandırılarak getirisi yatırımcıya aktarılır"},
            {"key": "E", "text": "Aracı kurumların özkaynak açığını kapatmak üzere yedek akçeye dönüştürülür"}
        ],
        "correct_answer": "D",
        "explanation": "Takasbank nezdindeki nakit Türk Lirası teminatları, Takasbank Para Piyasası, gecelik repo veya ters repo işlemlerinde değerlendirilerek elde edilen nema getirisi yatırımcı hesaplarına düzenli olarak yansıtılır."
    },

    # 4. q_1012_master_014
    "q_1012_master_014": {
        "text": "6362 sayılı Sermaye Piyasası Kanunu m.78 uyarınca takas sistemine iletilen emirler ve gerçekleşen takas mutabakatı ile ilgili hangisi DOĞRUDUR?",
        "options": [
            {"key": "A", "text": "Takas mutabakatı gerçekleştikten sonra kesinlikle geri alınamaz, iptal edilemez ve iflas masasına dahil edilemez"},
            {"key": "B", "text": "İşlem yapan aracı kurum iflas ederse takas mutabakatı 30 gün geriye dönük olarak tamamen hükümsüz kalır"},
            {"key": "C", "text": "Takas mutabakatı yalnızca takas tarihini takip eden iş günü mesai bitimine kadar mahkemece askıya alınabilir"},
            {"key": "D", "text": "Borsa yönetim kurulu kararıyla gerçekleşmiş tüm takas işlemleri gerekçesiz olarak tek taraflı feshedilebilir"},
            {"key": "E", "text": "Nakit ve kıymet mutabakatları aracı kurum genel kurulunda onaylanmadığı sürece hukuki kesinlik kazanmaz"}
        ],
        "correct_answer": "A",
        "explanation": "SPKn m.78'de düzenlenen 'Takasın Kesinliği İlkesi' uyarınca; takas sistemine intikal eden transfer emirleri ve takas işlemleri, üyenin iflası dahil hiçbir gerekçeyle geri alınamaz, iptal edilemez ve iflas masasına dahil edilemez."
    },

    # 5. q_1012_master_015
    "q_1012_master_015": {
        "text": "Borsa İstanbul ve SPK tarafından olağandışı fiyat ve miktar hareketleri nedeniyle bir hisse hakkında 'Brüt Takas' tedbiri uygulandığında ne olur?",
        "options": [
            {"key": "A", "text": "Aynı gün alınan hisse aynı gün satılamaz (netleştirme yapılamaz), takas T+2'de brüt nakit ve menkul kıymetle yapılır"},
            {"key": "B", "text": "İlgili hisse senedi derhal Borsa kotundan çıkarılarak tüm tahtası kalıcı olarak işleme kapatılır"},
            {"key": "C", "text": "Şirketin tüm yönetimi Sermaye Piyasası Kurulu tarafından atanan geçici kayyıma devredilir"},
            {"key": "D", "text": "İşlem takas süresi T+2 valöründen T+0 anlık teslimat valörüne dönüştürülür"},
            {"key": "E", "text": "Yalnızca profesyonel nitelikli yatırımcıların alım satım yapmasına izin verilir"}
        ],
        "correct_answer": "A",
        "explanation": "Brüt takas uygulaması getirilen paylarda; gün içi alım satımlarda takas netleştirmesi yapılamaz, aynı gün alınan hisse aynı gün satılamaz, kredili alım ve açığa satış yapılamaz; takas T+2'de brüt olarak gerçekleştirilir."
    },

    # 6. q_1012_master_016
    "q_1012_master_016": {
        "text": "Ödünç Pay Piyasasında ödünç alan tarafın iade yükümlülüğünü yerine getirmemesi (temerrüt) halinde Takasbank ne yapar?",
        "options": [
            {"key": "A", "text": "Ödünç verene herhangi bir ifa yapmaksızın tarafları adli mahkemelere sevk eder"},
            {"key": "B", "text": "Ödünç alanın teminatlarını nakde çevirerek piyasadan hisseyi satın alır ve ödünç verene teslim eder"},
            {"key": "C", "text": "Ödünç sözleşmesini tek taraflı olarak feshedip hisse teslim borcunu tamamen siler"},
            {"key": "D", "text": "Hisse açığını karşılamak üzere şirketin bedelsiz sermaye artırımı yapmasını talep eder"},
            {"key": "E", "text": "Takas yükümlülüğünü süresiz olarak askıya alıp dosya borcunu dondurur"}
        ],
        "correct_answer": "B",
        "explanation": "Takasbank Merkezi Karşı Taraf (MKT) sıfatıyla; ödünç alanın temerrüde düşmesi durumunda teminatları paraya çevirir, Buy-In (zorunlu alım) yaparak veya piyasadan temin ederek menkul kıymeti ödünç verene eksiksiz teslim eder."
    },

    # 7. q_1012_master_021
    "q_1012_master_021": {
        "text": "Sermaye piyasası operasyonlarında 'Valör' (Value Date) kavramı aşağıdakilerden hangisini ifade eder?",
        "options": [
            {"key": "A", "text": "Hisse senedinin nominal değeri üzerinden genel kurulca onaylanan kâr payı tutarını"},
            {"key": "B", "text": "Borsada gerçekleşen bir işlemin tescil edildiği andaki anlık işlem puanını"},
            {"key": "C", "text": "Aracı kurumun müşteriden tahsil edeceği yasal komisyon oranını"},
            {"key": "D", "text": "İşlemin gerçekleştiği tarih ile nakit ve kıymet takasının fiilen yapılacağı tarih arasındaki vadeyi"},
            {"key": "E", "text": "Halka arzda talep toplanan payların borsada ilk işlem görmeye başladığı seansı"}
        ],
        "correct_answer": "D",
        "explanation": "Valör; bir finansal işlemin yapıldığı tarih (işlem tarihi - T) ile o işlemden doğan nakit veya menkul kıymet teslim borcunun fiilen yerine getirileceği takas tarihi arasındaki zamanı ifade eder (örn. Pay Piyasasında T+2)."
    },

    # 8. q_1012_master_024
    "q_1012_master_024": {
        "text": "Takasbank'ın nakit netleştirmelerinde Türk Lirası büyük tutarlı nihai fon transferleri hangi ulusal sistem üzerinden sonuçlandırılır?",
        "options": [
            {"key": "A", "text": "Bankalararası Kart Merkezi (BKM) Sistemi"},
            {"key": "B", "text": "Uluslararası SWIFT Mesajlaşma Ağı"},
            {"key": "C", "text": "TCMB Elektronik Fon Transferi (EFT) Sistemi"},
            {"key": "D", "text": "Borsa İstanbul İç İletişim Portalı"},
            {"key": "E", "text": "Merkezi Nüfus İdaresi Sistemi (MERNİS)"}
        ],
        "correct_answer": "C",
        "explanation": "Takasbank nakit netleştirmelerinden doğan nihai büyük tutarlı Türk Lirası fon transferleri, Türkiye Cumhuriyet Merkez Bankası (TCMB) bünyesindeki Elektronik Fon Transferi (EFT) sistemi üzerinden gerçekleştirilir."
    },

    # 9. q_1012_master_028
    "q_1012_master_028": {
        "text": "Türkiye'deki MKK sisteminin dünyadaki birçok saklama modelinden farklı olan en temel ayırt edici güvence özelliği nedir?",
        "options": [
            {"key": "A", "text": "Menkul kıymetlerin aracı kurum havuzu yerine doğrudan yatırımcının kendi T.C./Vergi No adına alt hesaplarda tutulması"},
            {"key": "B", "text": "Payların yalnızca fiziki basılı kıymetli evrak karşılığında banka kasalarında saklanabilmesi"},
            {"key": "C", "text": "Yatırımcıların borsa emirlerini yalnızca yazılı dilekçeyle doğrudan MKK merkezine iletebilmesi"},
            {"key": "D", "text": "Hesapların mülkiyetinin aracı kurum ortaklarının şahsi tüzel kişiliklerine tescil edilmesi"},
            {"key": "E", "text": "Sermaye piyasası araçlarının takasının hiçbir merkezi takas kuruluşu olmaksızın ikili yapılması"}
        ],
        "correct_answer": "A",
        "explanation": "Türkiye'deki MKK sistemi 'Doğrudan Hak Sahipliği' (Direct Holding) modelidir. Paylar aracı kurum omnibus (havuz) hesaplarında değil; doğrudan nihai yatırımcının T.C. Kimlik / Vergi Numarası ile açılan kendi alt hesaplarında kayden izlenir."
    },

    # 10. q_1012_master_029
    "q_1012_master_029": {
        "text": "MKK'nın 'e-YATIRIMCI' uygulaması üzerinden yatırımcılara sunduğu 'Yatırımcı Blokajı' hizmetinin temel fonksiyonu nedir?",
        "options": [
            {"key": "A", "text": "Borsadaki hisse senetlerinin piyasa fiyat dalgalanmalarına karşı tavan-taban koruması sağlaması"},
            {"key": "B", "text": "İlgili şirketin genel kurul kararıyla temettü ödemelerini durdurmasını talep etmesi"},
            {"key": "C", "text": "Yatırımcının borsa işlemlerinden doğan gelir vergisi stopajını sıfırlaması"},
            {"key": "D", "text": "Yatırımcının hisselerini bizzat kilitleyerek izni olmaksızın aracı kurumca transfer ve satışını engellemesi"},
            {"key": "E", "text": "Hesaptaki tüm hisse senetlerinin otomatik olarak devlet tahvillerine dönüştürülmesi"}
        ],
        "correct_answer": "D",
        "explanation": "Yatırımcı Blokajı; yatırımcının e-YATIRIMCI üzerinden kendi paylarına şahsen blokaj koyarak, blokajı kendisi kaldırıncaya kadar aracı kurumun dahi bu payları transfer etmesini veya satmasını engelleyen benzersiz bir güvenlik kalkanıdır."
    },

    # 11. q_1012_master_031
    "q_1012_master_031": {
        "text": "Türk Ticaret Kanunu ve Sermaye Piyasası Kanunu uyarınca kaydi sermaye piyasası araçları üzerindeki hak sahipliğinin ispatında hangi kayıtlar esas alınır?",
        "options": [
            {"key": "A", "text": "Aracı kurum çalışanlarının tuttuğu şirket içi Excel çalışma tabloları"},
            {"key": "B", "text": "Merkezi Kayıt Kuruluşu (MKK) nezdinde tutulan elektronik kayıtlar kesin delil teşkil eder"},
            {"key": "C", "text": "İhraççı şirketin ticaret sicil müdürlüğüne verdiği sözlü kurucu beyanları"},
            {"key": "D", "text": "Yatırımcının banka hesap cüzdanındaki eski vadesiz mevduat çıktıları"},
            {"key": "E", "text": "Borsa aracı kurumunun basılı aylık müşteri tanıtım broşürleri"}
        ],
        "correct_answer": "B",
        "explanation": "SPKn m.13 uyarınca kaydileştirilen sermaye piyasası araçlarına ilişkin hakların ispatında ve üçüncü kişilere karşı ileri sürülmesinde MKK nezdinde tutulan elektronik kayıtlar kesin delil teşkil eder."
    },

    # 12. q_1012_master_032
    "q_1012_master_032": {
        "text": "MKK tarafından işletilen Elektronik Genel Kurul Sistemi'nin (e-GKS) sağladığı temel yasal imkan nedir?",
        "options": [
            {"key": "A", "text": "Pay sahiplerinin genel kurula uzaktan canlı katılıp görüş bildirmesi ve güvenli e-imza ile oy kullanabilmesi"},
            {"key": "B", "text": "Şirket yönetim kurulu üyelerinin huzur hakkı ve maaşlarının Borsa İstanbul'ca ödenmesi"},
            {"key": "C", "text": "Halka açık anonim şirketlerin genel kurul toplantısı yapma yükümlülüğünün tamamen kaldırılması"},
            {"key": "D", "text": "Azınlık pay sahiplerinin genel kuruldaki tüm oy haklarının şirkete devredilmesi"},
            {"key": "E", "text": "Şirketin tüm bilanço zararlarının otomatik olarak MKK sermayesinden karşılanması"}
        ],
        "correct_answer": "A",
        "explanation": "e-GKS (Elektronik Genel Kurul Sistemi); pay sahiplerinin genel kurullara fiziken gitmeksizin elektronik ortamda canlı yayınla katılmalarına, görüş bildirmelerine, muhalefet şerhi koymalarına ve güvenli elektronik imza ile oy kullanmalarına imkan tanıyan yasal sistemdir."
    },

    # 13. q_1012_master_035
    "q_1012_master_035": {
        "text": "Bir yatırımcının Türkiye sermaye piyasalarında kaç adet benzersiz MKK Sicil Numarası bulunabilir?",
        "options": [
            {"key": "A", "text": "T.C. Kimlik / Vergi Numarası ile eşleşen tek bir benzersiz MKK Sicil Numarası üretilir"},
            {"key": "B", "text": "Yatırımcının hesap açtığı her bir aracı kurum için ayrı bir MKK Sicil Numarası verilir"},
            {"key": "C", "text": "Yatırımcının portföyündeki her bir farklı hisse senedi için ayrı sicil tescil edilir"},
            {"key": "D", "text": "MKK Sicil Numarası her takvim yılı başında mevzuat gereğince yenilenir"},
            {"key": "E", "text": "Yalnızca profesyonel müşterilere sicil verilir, genel müşterilere numara tahsis edilmez"}
        ],
        "correct_answer": "A",
        "explanation": "MKK sisteminde her gerçek ve tüzel kişi yatırımcı için T.C. Kimlik Numarası veya Vergi Numarası esas alınarak ömür boyu geçerli olan tek bir benzersiz 'MKK Sicil Numarası' üretilir; yatırımcı 10 farklı aracı kurumda hesap açsa dahi sicil numarası değişmez."
    },

    # 14. q_1012_master_039
    "q_1012_master_039": {
        "text": "MKK kayıtlarına güvenerek borsada kaydi sermaye piyasası aracı iktisap eden iyiniyetli üçüncü kişinin mülkiyeti ile ilgili kural nedir?",
        "options": [
            {"key": "A", "text": "MKK kayıtlarının hukuki bağlayıcılığı bulunmadığından mülkiyet hakkı her zaman iptal edilebilir"},
            {"key": "B", "text": "MKK kayıtlarına güvenilerek yapılan pay iktisapları kanunen tam korunur; mülkiyet iptal edilemez"},
            {"key": "C", "text": "Satın alan iyiniyetli yatırımcı payları ihraççı şirkete derhal iade etmekle yükümlüdür"},
            {"key": "D", "text": "Mülkiyet yalnızca Borsa İstanbul Teftiş Kurulu onay verirse geçerli hale gelir"},
            {"key": "E", "text": "İyiniyetli iktisap yalnızca Hazine bonolarında geçerli olup hisse senetlerinde korunmaz"}
        ],
        "correct_answer": "B",
        "explanation": "SPKn m.13 uyarınca; MKK nezdinde tutulan kayıtlara güvenerek iyiniyetle pay veya hak iktisap eden üçüncü kişilerin bu iktisapları kanunen korunur (Tapu sicilindeki iyiniyetli iktisabın korunması prensibi gibidir)."
    },

    # 15. q_1012_master_041
    "q_1012_master_041": {
        "text": "MKK'nın 'e-CAS' (Yatırımcı Bilgilendirme Sistemi) uygulaması yatırımcılara temel olarak hangi güvenlik bildirimini sağlar?",
        "options": [
            {"key": "A", "text": "Hesaptan menkul kıymet çıkışı veya virman gerçekleştiğinde anında SMS ve e-posta ile bildirim iletilmesi"},
            {"key": "B", "text": "Borsada işlem gören şirketlerin çeyreklik bilanço kâr tahminlerinin yatırımcıya gönderilmesi"},
            {"key": "C", "text": "Aracı kurumların günlük hisse alım-satım ve teknik analiz tavsiyelerinin ulaştırılması"},
            {"key": "D", "text": "Yatırımcının banka hesaplarındaki vadeli mevduat faiz oranlarının kıyaslanması"},
            {"key": "E", "text": "Şirketlerin yönetim kurulu toplantı tutanaklarının basılı nüsha olarak postalanması"}
        ],
        "correct_answer": "A",
        "explanation": "e-CAS sistemi; yatırımcının MKK'daki hesaplarından herhangi bir hisse senedi veya menkul kıymet çıkışı, virmanı veya rehni gerçekleştiğinde yatırımcının cep telefonuna anında SMS ve e-posta uyarısı gönderen güvenlik sistemidir."
    },

    # 16. q_1012_master_046
    "q_1012_master_046": {
        "text": "Özel sektör tahvilleri ve finansman bonoları ne zaman ve hangi aşamada MKK sisteminde kaydileştirilir?",
        "options": [
            {"key": "A", "text": "İhraççı şirketin iflas tasfiye masasına başvurması anında"},
            {"key": "B", "text": "Vade bitiminde anapara ve faiz ödemesi tamamlandıktan sonra"},
            {"key": "C", "text": "Satış bedelleri tahsil edilip ihraç tamamlandığı anda MKK'da yatırımcı hesaplarına aktarılarak"},
            {"key": "D", "text": "Tahviller Borsa kotundan çıkarılıp fiziki senede dönüştürüldüğünde"},
            {"key": "E", "text": "Yalnızca tahvil faiz oranları Merkez Bankası politika faizini aştığında"}
        ],
        "correct_answer": "C",
        "explanation": "Özel sektör borçlanma araçları; satış süreci tamamlanıp satış bedelleri yatırıldığı anda MKK nezdinde hak sahipleri adına açılan hesaplarda kayden oluşturulur ve izlenir."
    },

    # 17. q_1012_master_047
    "q_1012_master_047": {
        "text": "Borsada işlem görmeyen halka kapalı anonim şirketlerin paylarının MKK sistemine dahil edilmesiyle ilgili hangisi DOĞRUDUR?",
        "options": [
            {"key": "A", "text": "Halka açık olmayan şirketlerin MKK sisteminde hiçbir surette kaydı yapılamaz"},
            {"key": "B", "text": "Halka kapalı şirketler yalnızca tahvil ihraç ederlerse MKK'ya bildirimde bulunurlar"},
            {"key": "C", "text": "Halka kapalı A.Ş.'ler de genel kurul kararıyla paylarını MKK'da kaydileştirebilir ve hamiline payları bildirmek zorundadır"},
            {"key": "D", "text": "Halka kapalı şirket paylarının kaydı yalnızca Hazine ve Maliye Bakanlığı'nın talebiyle yapılır"},
            {"key": "E", "text": "Pay devirleri MKK yerine yalnızca yerel noterliklerin tasdik defterinde tutulur"}
        ],
        "correct_answer": "C",
        "explanation": "Halka kapalı anonim ortaklıklar da genel kurul kararıyla paylarını MKK nezdinde kaydileştirebilirler. Ayrıca TTK uyarınca hamiline yazılı pay senedi sahiplerinin MKK bünyesindeki Hamiline Pay Kayıt Sistemi'ne (HPKS) bildirilmesi kanunen zorunludur."
    },

    # 18. q_1012_master_048
    "q_1012_master_048": {
        "text": "MKK'nın kendi sistemindeki kusurlu ve hatalı kayıtlar sebebiyle hak sahiplerinin uğradığı zararlardan sorumluluğu nedir?",
        "options": [
            {"key": "A", "text": "MKK kamu tüzel kişisi niteliğinde olduğundan hiçbir maddi zarardan sorumlu tutulamaz"},
            {"key": "B", "text": "MKK kusurundan doğan zararlardan hukuken sorumludur ve bu riske karşı mesleki sorumluluk sigortası yaptırır"},
            {"key": "C", "text": "Maddi zararlar yalnızca aracı kurumların genel müdürleri tarafından şahsen tazmin edilir"},
            {"key": "D", "text": "MKK yalnızca kusurlu personeli görevden uzaklaştırır, maddi tazminat ödemez"},
            {"key": "E", "text": "Sorumluluk tamamen Merkezi Kayıt Kuruluşu üyeleri olan yatırımcılara aittir"}
        ],
        "correct_answer": "B",
        "explanation": "SPKn m.81 uyarınca MKK, kendi sistemindeki yanlış veya eksik kayıtlardan doğan zararlardan genel hükümlere göre sorumludur ve mevzuat gereği bu riskleri karşılamak üzere mesleki sorumluluk sigortası yaptırmakla yükümlüdür."
    },

    # 19. q_1012_master_049
    "q_1012_master_049": {
        "text": "Hesabında rehin veya haciz blokajı bulunan bir hisse senedinin genel kurulda oy hakkını kural olarak kim kullanır?",
        "options": [
            {"key": "A", "text": "İcra dairesi müdürü veya alacaklı taraf oy hakkını bizzat kullanır"},
            {"key": "B", "text": "Hacizli payların genel kuruldaki tüm oy hakları kanunen askıya alınır"},
            {"key": "C", "text": "Oy hakkı otomatik olarak şirketin yönetim kurulu başkanına intikal eder"},
            {"key": "D", "text": "Paylar genel kurulda Borsa İstanbul A.Ş. temsilcisi tarafından temsil edilir"},
            {"key": "E", "text": "Aksine bir sözleşme veya mahkeme kararı olmadıkça payın asıl maliki (ortağı) oy hakkını kullanır"}
        ],
        "correct_answer": "E",
        "explanation": "Türk Ticaret Kanunu uyarınca; pay üzerinde intifa hakkı varsa oy hakkı intifa hakkı sahibinindir. Ancak rehin veya haciz halinde aksine bir mahkeme kararı veya rehin sözleşmesi hükmü bulunmadıkça mülkiyet sahibi pay sahibi oy hakkını kullanmaya devam eder."
    },

    # 20. q_1012_master_053
    "q_1012_master_053": {
        "text": "Bedelli sermaye artırımında rüçhan hakkını kullanarak bedelini yatıran yatırımcının yeni payları hesabına ne zaman kayden aktarılır?",
        "options": [
            {"key": "A", "text": "Rüçhan kullanım bedelinin yatırıldığı andan itibaren 6 ay sonra"},
            {"key": "B", "text": "İhraççı şirketin ilk olağan genel kurul toplantısının yapıldığı gün"},
            {"key": "C", "text": "Şirketin sermaye artırımını tamamlayıp ticaret siciline tescil ettirmesinin ardından MKK tarafından"},
            {"key": "D", "text": "Halka arz edilen payların tamamı ikinci el piyasada satıldıktan sonra"},
            {"key": "E", "text": "Yalnızca şirketin ilgili takvim yılında nakit kâr payı dağıtması durumunda"}
        ],
        "correct_answer": "C",
        "explanation": "Bedelli sermaye artırımında rüçhan hakkı kullanımı tamamlandıktan sonra, yeni sermaye ticaret siciline tescil edilir ve SPK/MKK süreçleri neticesinde yeni kaydi paylar hak sahiplerinin MKK hesaplarına yüklenir."
    },

    # 21. q_1012_master_054
    "q_1012_master_054": {
        "text": "Bedelli sermaye artırımına katılmak istemeyen bir pay sahibi rüçhan hakkını nasıl değerlendirebilir?",
        "options": [
            {"key": "A", "text": "Rüçhan hakkını yalnızca ihraççı şirketin genel müdürüne bedelsiz devredebilir"},
            {"key": "B", "text": "Rüçhan hakkı devredilemez bir hak olup kullanılmadığı takdirde kendiliğinden sona erer"},
            {"key": "C", "text": "Borsa İstanbul'da açılan Rüçhan Hakkı Kupon Pazarında kullanım süresi içinde satarak nakde çevirebilir"},
            {"key": "D", "text": "Rüçhan hakkını vadesiz opsiyon sözleşmesine dönüştürerek süresiz saklayabilir"},
            {"key": "E", "text": "Hakkını doğrudan Yatırımcı Tazmin Merkezi'ne devrederek karşılığında tazminat alabilir"}
        ],
        "correct_answer": "C",
        "explanation": "Bedelli artırıma nakit koymak istemeyen yatırımcılar, bedelli süresi boyunca Borsa İstanbul'da işlem gören Rüçhan Hakkı Kupon Pazarı'nda kuponlarını satarak nakit gelir elde edebilirler."
    },

    # 22. q_1012_master_055
    "q_1012_master_055": {
        "text": "Halka açık anonim ortaklıkların genel kurullarına katılabilecek pay sahiplerinin listesi (Hazır Bulunanlar Listesi) kim tarafından ve neye göre hazırlanır?",
        "options": [
            {"key": "A", "text": "MKK tarafından genel kurul gününden bir gün önceki MKK kayıtları esas alınarak hazırlanıp şirkete teslim edilir"},
            {"key": "B", "text": "Şirketin merkez ofisinde pay defterine fiziken kayıtlı ortaklar arasından yönetim kurulunca seçilir"},
            {"key": "C", "text": "Borsa İstanbul Teftiş Kurulu tarafından son 1 yılda işlem yapan hesaplar taranarak oluşturulur"},
            {"key": "D", "text": "Yalnızca şirkette en az %5 paya sahip olan kurumsal ortaklar tarafından belirlenir"},
            {"key": "E", "text": "Türkiye Sermaye Piyasaları Birliği tarafından kura yöntemiyle belirlenir"}
        ],
        "correct_answer": "A",
        "explanation": "SPKn m.30 uyarınca genel kurula katılabilecek pay sahipleri listesi, genel kurul gününden bir önceki gün MKK nezdinde hak sahibi olan kişilerin listesi esas alınarak MKK tarafından güvenli elektronik ortamda oluşturulur."
    },

    # 23. q_1012_master_056
    "q_1012_master_056": {
        "text": "Yatırım kuruluşları gün sonunda açık kalan pozisyonlarını, nakit durumlarını ve müşteri teminatlarını mevzuat uyarınca kime raporlamak zorundadır?",
        "options": [
            {"key": "A", "text": "Rekabet Kurumu ve Kamu İhale Kurumu'na"},
            {"key": "B", "text": "Türkiye İstatistik Kurumu ve Hazineye"},
            {"key": "C", "text": "Türkiye Noterler Birliği Başkanlığı'na"},
            {"key": "D", "text": "Takasbank ve Sermaye Piyasası Kurulu'na"},
            {"key": "E", "text": "Yalnızca yerel ticaret ve sanayi odalarına"}
        ],
        "correct_answer": "D",
        "explanation": "Yatırım kuruluşları, takas ve teminat yükümlülüklerinin izlenmesi ve sermaye yeterliliği denetimi amacıyla gün sonu pozisyon ve teminat raporlarını Takasbank ve SPK'ya düzenli olarak raporlamakla yükümlüdür."
    },

    # 24. q_1012_master_058
    "q_1012_master_058": {
        "text": "VİOP'ta teminatı sürdürme seviyesinin altına düşen ve verilen sürede teminat tamamlamayan müşterinin pozisyonları nasıl kapatılır?",
        "options": [
            {"key": "A", "text": "Pozisyonlar müşteri onay verene kadar takas merkezinde süresiz açık tutulur"},
            {"key": "B", "text": "Müşteriye Takasbank tarafından faizsiz hibe kredi açılarak teminat borcu kapatılır"},
            {"key": "C", "text": "Pozisyonlar aracı kurumun diğer müşterilerinin hesaplarına oransal paylaştırılır"},
            {"key": "D", "text": "Müşterinin portföyündeki tüm hisse senetleri Hazineye gelir kaydedilir"},
            {"key": "E", "text": "Takasbank ve aracı kurum tarafından piyasa fiyatından ters işlem yapılarak re'sen tasfiye edilir"}
        ],
        "correct_answer": "E",
        "explanation": "Margin call çağrısına (saat 15:00'e kadar) uymayan VİOP hesaplarında, Takasbank ve aracı kurum piyasada ters işlem (kapatıcı işlem) yaparak pozisyonları piyasa fiyatından re'sen likide eder."
    },

    # 25. q_1012_master_061
    "q_1012_master_061": {
        "text": "Bir takas üyesinin Takasbank Para Piyasasından teminat vermeksizin borçlanabilmesi hukuken mümkün müdür?",
        "options": [
            {"key": "A", "text": "Evet; aracı kurumun BIST 30 paylarında piyasa yapıcılık taahhüdü bulunması kaydıyla mümkündür"},
            {"key": "B", "text": "Evet; kamu sermayeli mevduat bankaları Takasbank nezdinde teminatsız borçlanma limiti kullanabilir"},
            {"key": "C", "text": "Evet; aracı kurum yönetim kurulu üyelerinin müştereken şahsi kefalet tesis etmesiyle mümkündür"},
            {"key": "D", "text": "Evet; gün içi geçici nakit açıklarında aynı gün seans bitimine kadar teminatsız izin verilir"},
            {"key": "E", "text": "Hayır; Takasbank Para Piyasası'ndaki tüm borçlanmalar kabul edilebilir teminatlar karşılığı yapılır"}
        ],
        "correct_answer": "E",
        "explanation": "Takasbank Para Piyasası'nda ve takas sisteminde teminatsız işlem yapılması kesinlikle yasaktır; tüm borçlanmalar Takasbank tarafından belirlenen teminat katsayılarına uygun nakit veya menkul kıymet karşılığında gerçekleşir."
    },

    # 26. q_1012_master_064
    "q_1012_master_064": {
        "text": "BIST 30 Endeks Vadeli İşlem Sözleşmelerinde vade sonu takas ve uzlaşması nasıl gerçekleştirilir?",
        "options": [
            {"key": "A", "text": "Endeksi oluşturan 30 şirketin hisse senetlerinin tek tek fiziki teslim edilmesiyle"},
            {"key": "B", "text": "Sözleşme tutarının tamamının Amerikan Doları cinsinden Takasbank'a ödenmesiyle"},
            {"key": "C", "text": "Tarafların karşılıklı altın külçesi transferi gerçekleştirmesi yöntemiyle"},
            {"key": "D", "text": "Sözleşme vadesinin otomatik olarak bir sonraki takvim yılına ertelenmesiyle"},
            {"key": "E", "text": "Kâr/zarar farkının taraflar arasında nakden tahsil edilip ödenmesiyle (Nakit Uzlaşma)"}
        ],
        "correct_answer": "E",
        "explanation": "Endeks vadeli işlem sözleşmeleri fiziki teslime konu edilemez; vade sonundaki uzlaşma fiyatı ile pozisyon fiyatı arasındaki fark nakit olarak hesaplar arasında tahsil edilip ödenir (Nakit Uzlaşma / Cash Settlement)."
    },

    # 27. q_1012_master_067
    "q_1012_master_067": {
        "text": "Özel sektör tahvilinin dönemsel kupon faiz ödeme gününde Takasbank ve MKK operasyonu nasıl işler?",
        "options": [
            {"key": "A", "text": "Kupon bedelleri nakit olarak şirketin muhasebe veznesinden hak sahiplerine elden dağıtılır"},
            {"key": "B", "text": "İhraççı tutarı Takasbank'a aktarır; Takasbank MKK kayıtlarındaki hak sahiplerinin hesaplarına kuponu net dağıtır"},
            {"key": "C", "text": "Kupon bedelleri zorunlu olarak şirketin ihraç edeceği yeni pay senetlerine dönüştürülür"},
            {"key": "D", "text": "Kupon ödemeleri Takasbank tarafından kendi özkaynaklarından finanse edilir"},
            {"key": "E", "text": "Kupon tutarı yalnızca genel kurula fiziken katılan tahvil sahiplerine ödenir"}
        ],
        "correct_answer": "B",
        "explanation": "Kupon gününde ihraççı şirket nakit kupon tutarını Takasbank'a yatırır. Takasbank, MKK'dan gelen hak sahipleri listesine göre yatırımcıların hesaplarına kupon faizlerini elektronik ortamda otomatik olarak aktarır."
    },

    # 28. q_1012_master_068
    "q_1012_master_068": {
        "text": "Halka açık bir ortaklığın eşzamanlı sermaye artırımı ve azaltımı (özsermaye telafisi) operasyonunda MKK'nın görevi nedir?",
        "options": [
            {"key": "A", "text": "Şirketin borsadaki tüm işlem sıralarını kalıcı olarak iptal etmek"},
            {"key": "B", "text": "Şirketin yönetim kurulunu feshederek tasfiye memuru atamak"},
            {"key": "C", "text": "Pay sahiplerinin borsa hesaplarını 1 yıl süreyle işleme kapatmak"},
            {"key": "D", "text": "Ortaklığın geçmiş yıl zararlarını kendi sermayesinden tazmin etmek"},
            {"key": "E", "text": "Eski payların belirlenen oranda itfasını ve yeni payların kayden oluşturularak hesaplara aktarılmasını sağlamak"}
        ],
        "correct_answer": "E",
        "explanation": "Eşzamanlı sermaye artırımı ve azaltımında MKK; azaltılan kısma isabet eden kaydi payları sistemden itfa eder (iptal eder) ve eşzamanlı olarak artırılan yeni payları hak sahiplerinin hesaplarına kayden yansıtır."
    },

    # 29. q_1012_master_069
    "q_1012_master_069": {
        "text": "MKK ve KAP sistemine yüklenen elektronik bildirimlerin hukuki zaman kanıtı nasıl sağlanır?",
        "options": [
            {"key": "A", "text": "TÜBİTAK onaylı resmi Zaman Damgası (Time Stamp) ve Nitelikli Elektronik Sertifika (e-İmza) ile"},
            {"key": "B", "text": "İlçe Ticaret Sicil Müdürlüğü'nün fiziki defter tasdik mührü ile"},
            {"key": "C", "text": "Şirket yönetim kurulu başkanının ıslak imzalı onay beyannamesi ile"},
            {"key": "D", "text": "Borsa İstanbul Teftiş Kurulu'nun haftalık onay yazısı ile"},
            {"key": "E", "text": "Türkiye Sermaye Piyasaları Birliği'nin basılı resmî bülteni ile"}
        ],
        "correct_answer": "A",
        "explanation": "KAP ve MKK sistemlerindeki elektronik bildirimlerin değiştirilmediğini ve kesin zamanını kanıtlamak üzere 5070 sayılı Elektronik İmza Kanunu uyarınca Nitelikli Elektronik Sertifika ve TÜBİTAK Zaman Damgası kullanılır."
    },

    # 30. q_1012_master_071
    "q_1012_master_071": {
        "text": "Sermaye piyasası takas ve mutabakat işlemlerinde 'Temerrüt' hali ne zaman ortaya çıkar?",
        "options": [
            {"key": "A", "text": "Borsada işlem gören hisse senetlerinin piyasa fiyatının taban yapması durumunda"},
            {"key": "B", "text": "Şirketin genel kurulunda kâr payının nakit yerine bedelsiz hisse olarak dağıtılmasında"},
            {"key": "C", "text": "Aracı kurumun müşteri sayısının SPK asgari standartlarının altına gerilemesi halinde"},
            {"key": "D", "text": "Takas üyesinin, takas gününde nakit ödeme veya menkul kıymet teslim yükümlülüğünü süresinde yerine getirememesi durumunda"},
            {"key": "E", "text": "Müşterinin borsa hesabındaki tüm menkul kıymetleri başka bir kuruma virmanlaması halinde"}
        ],
        "correct_answer": "D",
        "explanation": "Temerrüt; takas üyesinin veya yatırımcının, takas gününde (valörde) teslim etmekle yükümlü olduğu menkul kıymeti veya ödemekle yükümlü olduğu nakit tutarı Takasbank'a süresi içinde tevdi edememesi durumudur."
    },

    # 31. q_1012_master_075
    "q_1012_master_075": {
        "text": "Satış yapan bir üyenin takas gününde hisse senetlerini Takasbank'a teslim edememesi (kıymet temerrüdü) halinde Takasbank bu açığı nasıl kapatır?",
        "options": [
            {"key": "A", "text": "Alıcı tarafa hisse teslimi yapılmaz, gerçekleşen borsa işlemi Borsa Yönetim Kurulu kararıyla feshedilir"},
            {"key": "B", "text": "Alıcı takas üyesinden yazılı feragat alınarak ilgili takas mutabakatı tarafların mutabakatıyla iptal edilir"},
            {"key": "C", "text": "Kıymet teslim yükümlülüğü temerrüt faizi işletilmeksizin bir sonraki takvim ayının ilk iş gününe ertelenir"},
            {"key": "D", "text": "Takasbank 'Buy-In' (Zorunlu Alım) yaparak veya Ödünç Pay Piyasasından temin ederek hisseyi alıcıya teslim eder"},
            {"key": "E", "text": "Alıcı üyeye pay senedi yerine aracı kurumun kendi portföyündeki borçlanma araçları zorunlu devredilir"}
        ],
        "correct_answer": "D",
        "explanation": "Kıymet temerrüdünde Takasbank MKT garantisi kapsamında; önce Ödünç Pay Piyasası'ndan hisseyi temin eder veya piyasada bizzat 'Buy-In' (Zorunlu Satın Alma) işlemi yaparak hisseyi alır ve alıcıya verir; tüm maliyet ve cezaları temerrüt eden üyeye fatura eder."
    },

    # 32. q_1012_master_076
    "q_1012_master_076": {
        "text": "Temerrüt borcunu verilen yasal ek sürede kapatmayan aracı kurum hakkında Takasbank ve Borsa ne yapar?",
        "options": [
            {"key": "A", "text": "Kuruma Takasbank bütçesinden faizsiz uzun vadeli yapılandırma kredisi tahsis eder"},
            {"key": "B", "text": "Kurumun borcunu Borsa İstanbul A.Ş.'nin genel gider bütçesine hibe olarak kaydeder"},
            {"key": "C", "text": "Kurumun takas borcunu kanunen silerek dosyayı adli mercilere bildirmeden kapatır"},
            {"key": "D", "text": "Aracı kurumu yalnızca yazılı kınama cezası ile tecziye edip işlemlere devam ettirir"},
            {"key": "E", "text": "Kurumun borsa işlem yetkisini ve takas üyeliğini derhal askıya alır / geçici olarak durdurur"}
        ],
        "correct_answer": "E",
        "explanation": "Temerrüt yükümlülüğünü yerine getirmeyen takas üyesinin teminatları paraya çevrilir, Garanti Fonu devreye sokulur ve üyenin takas üyeliği ile Borsa işlem yapma yetkisi derhal durdurulur."
    },

    # 33. q_1012_master_080
    "q_1012_master_080": {
        "text": "SPKn m.79 uyarınca üyelerin Takasbank'a verdikleri teminatlar üzerindeki Takasbank'ın yasal hakkı ve imtiyazı nedir?",
        "options": [
            {"key": "A", "text": "Teminatlar mahkeme ilamı kesinleşmeden hiçbir şekilde paraya çevrilemez"},
            {"key": "B", "text": "Teminat tutarları öncelikle kamu vergi borçlarına mahsup edilmek zorundadır"},
            {"key": "C", "text": "Teminatlar üyenin iflası durumunda doğrudan genel iflas masasına devredilir"},
            {"key": "D", "text": "Takasbank teminatları mahkeme kararına gerek olmaksızın re'sen paraya çevirmede birinci derece imtiyazlı hakka sahiptir"},
            {"key": "E", "text": "Takasbank teminatları yalnızca üyenin genel kurulunun yazılı onayı ile nakde dönüştürebilir"}
        ],
        "correct_answer": "D",
        "explanation": "SPKn m.79 uyarınca Takasbank'a verilen teminatlar; kamu alacakları dahil hiçbir borç için haczedilemez, iflas masasına dahil edilemez ve Takasbank temerrüt anında bu teminatları re'sen nakde çevirmede mutlak rüçhan hakkına sahiptir."
    },

    # 34. q_1012_master_092
    "q_1012_master_092": {
        "text": "Aracı kurum kayıtları ile MKK kayıtları arasında herhangi bir hisse senedi mutabakatsızlığı tespit edilirse aracı kurum ne yapmak zorundadır?",
        "options": [
            {"key": "A", "text": "Mutabakatsızlığı takip eden üç aylık bağımsız denetim dönemine kadar gizli tutmalıdır"},
            {"key": "B", "text": "İlgili müşteri hesabını derhal kapatarak kayıtları şirket içi arşivden silmelidir"},
            {"key": "C", "text": "Farkı aynı gün içinde araştırıp düzeltmek ve giderilemeyen uyumsuzlukları derhal SPK ve MKK'ya bildirmek zorundadır"},
            {"key": "D", "text": "Eksik hisse miktarını müşterinin rızasını aramaksızın nakit olarak tahsil etmelidir"},
            {"key": "E", "text": "Mutabakat farkını aracı kurumun geçmiş yıl kârları hesabına otomatik mahsup etmelidir"}
        ],
        "correct_answer": "C",
        "explanation": "MKK Kaydileştirme Tebliği uyarınca; aracı kurumlar her gün MKK kayıtlarıyla kendi kayıtlarını mutabakatlaştırmak, fark çıkması halinde aynı gün düzelterek çözülemeyenleri SPK ve MKK'ya derhal yazılı bildirmek zorundadır."
    },

    # 35. q_1012_master_094
    "q_1012_master_094": {
        "text": "Kaydileştirme sisteminin fiziki basılı pay senetlerine kıyasla ortadan kaldırdığı en temel operasyonel riskler nelerdir?",
        "options": [
            {"key": "A", "text": "Hisselerin piyasa fiyatındaki dalgalanmalar ve sermaye kaybı riskleri"},
            {"key": "B", "text": "Sahte hisse basımı, senetlerin çalınması, yangında/afette kaybolması ve fiziki yıpranma riskleri"},
            {"key": "C", "text": "Şirketin kâr dağıtmaması ve ticari faaliyetlerinde zarar etmesi riskleri"},
            {"key": "D", "text": "Sermaye piyasası araçlarından alınan gelir vergisi stopajı kesintileri"},
            {"key": "E", "text": "Borsa şirketlerinin yabancı para borçlarından doğan kur riski dalgalanmaları"}
        ],
        "correct_answer": "B",
        "explanation": "Kaydileştirme sistemi; hisse senetlerinin fiziken basılması, saklanması ve nakliyesi sırasındaki sahtecilik, çalınma, kaybolma, yıpranma ve kuponaj risklerini tamamen ortadan kaldırmıştır."
    },

    # 36. q_1012_master_098
    "q_1012_master_098": {
        "text": "Borsada gerçekleşen hatalı bir işlemin iptali veya düzeltilmesi mevzuatta hangi kurallara tabidir?",
        "options": [
            {"key": "A", "text": "Aracı kurumlar müşteri onayı olmaksızın diledikleri borsa işlemini tek taraflı iptal edebilirler"},
            {"key": "B", "text": "Borsada gerçekleşmiş hiçbir işlem hangi gerekçeyle olursa olsun asla iptal edilemez"},
            {"key": "C", "text": "İşlemlerin iptali yalnızca ilgili şirket yönetim kurulu başkanının yazılı izniyle mümkündür"},
            {"key": "D", "text": "Borsa İstanbul İşlem Yönergesi'ndeki katı şartlar, zaman limitleri ve Borsa Genel Müdürlüğü onayı ile istisnai yapılabilir"},
            {"key": "E", "text": "İptal talebi yalnızca hafta sonları aracı kurumlar birliğine iletilebilir"}
        ],
        "correct_answer": "D",
        "explanation": "Borsa İstanbul kuralları uyarınca işlem iptalleri; yalnızca açık ve bariz sistemsel/maddi hatalarda, çok kısa süreler içinde ve Borsa İstanbul Yönetiminin onayı ile istisnai olarak gerçekleştirilebilir."
    },

    # 37. q_1012_master_099
    "q_1012_master_099": {
        "text": "MKK ve aracı kurumların yatırımcılara sunduğu periyodik hesap bildirimlerinin güvenliği mevzuata göre hangi yöntemlerle sağlanır?",
        "options": [
            {"key": "A", "text": "Yalnızca kurum içi ağdan şahsen başvuran müşterilere sözlü aktarım yapılması yöntemiyle"},
            {"key": "B", "text": "Sermaye Piyasası Kurulu haftalık bülteninde maskelenmiş müşteri kodlarıyla ilan edilmesiyle"},
            {"key": "C", "text": "Hesap özetlerinin aracı kurumun internet portalında şifresiz genel duyuru olarak paylaşılmasıyla"},
            {"key": "D", "text": "Borsa İstanbul bülteni ekinde aracı kuruluş bazında konsolide edilerek yayımlanmasıyla"},
            {"key": "E", "text": "Güvenli elektronik imza, iki aşamalı SMS doğrulama ve e-Devlet kapısı entegrasyonuyla"}
        ],
        "correct_answer": "E",
        "explanation": "Müşteri hesap bildirimleri ve ekstreleri; müşteri sırrını korumak amacıyla şifreli e-posta, SMS doğrulama, e-Devlet kapısı ve güvenli elektronik imza gibi yüksek güvenlikli kanallardan iletilir."
    },

    # 38. q_1012_master_100
    "q_1012_master_100": {
        "text": "Borsa İstanbul (İşlem Eşleştirme) -> Takasbank (Merkezi Takas & MKT) -> MKK (Merkezi Saklama) üçlü zincirinin oluşturduğu kurumsal yapıya ne ad verilir?",
        "options": [
            {"key": "A", "text": "Merkezi Bankacılık Konsorsiyumu Altyapısı"},
            {"key": "B", "text": "Türkiye Sermaye Piyasaları Entegre İşlem ve İşlem Sonrası Altyapısı"},
            {"key": "C", "text": "Uluslararası Para Fonu Bölgesel Takas Birliği"},
            {"key": "D", "text": "Interbank Para ve Kambiyo Piyasaları Federasyonu"},
            {"key": "E", "text": "Avrupa Birliği Sermaye Piyasaları Saklama Komisyonu"}
        ],
        "correct_answer": "B",
        "explanation": "Borsa İstanbul (alım satım), Takasbank (merkezi takas ve karşı taraf) ve MKK (merkezi saklama ve kaydi sistem) birlikte Türkiye'nin entegre işlem ve işlem sonrası ekosistemini (Post-Trade Infrastructure) oluşturur."
    },

    # 39. q_1012_ogretici_001
    "q_1012_ogretici_001": {
        "text": "Sermaye piyasasında takas işleminin temel kurumsal işlevi aşağıdakilerden hangisidir?",
        "options": [
            {"key": "A", "text": "Borsada gerçekleşen işlemlerden doğan borç ve alacakların belirlenen kurallarla netleştirilip sonuçlandırılması"},
            {"key": "B", "text": "Yatırımcılara borsa işlemlerinde oluşabilecek tüm sermaye kayıpları için kesin teminat garantisi verilmesi"},
            {"key": "C", "text": "Halka açık ortaklıkların sermaye artırımı tescil işlemlerinin Borsa tarafından tek taraflı yapılması"},
            {"key": "D", "text": "Müşterilere sermaye piyasasında bağımsız yatırım danışmanlığı tavsiyeleri üretilmesi"},
            {"key": "E", "text": "Borsadaki tüm hisse senetlerinin piyasa fiyatlarının günlük olarak sabitlenmesi"}
        ],
        "correct_answer": "A",
        "explanation": "Takas işlemi; piyasada oluşan alım-satım işlemlerinin netleştirilmesi, menkul kıymetlerin teslimi ve nakit bedellerin transferi ile yükümlülüklerin ifa edilmesini sağlar."
    },

    # 40. q_1012_ogretici_002
    "q_1012_ogretici_002": {
        "text": "Sermaye piyasası mevzuatında 'Saklama Hizmeti'nin temel amacı nedir?",
        "options": [
            {"key": "A", "text": "Yatırımcıların portföylerindeki kıymetler için asgari getiri taahhüdünde bulunmak"},
            {"key": "B", "text": "Sermaye piyasası araçları ve bunlara ilişkin hakların güvenli şekilde muhafaza ve takibini yürütmek"},
            {"key": "C", "text": "Yatırım kararlarının ve portföy tahsislerinin saklama kuruluşu tarafından re'sen verilmesi"},
            {"key": "D", "text": "Hisse senetlerinin borsadaki alım satım komisyon oranlarını piyasaya dikte etmek"},
            {"key": "E", "text": "İhraççı şirketlerin finansal tablolarını bağımsız denetimden muaf tutmak"}
        ],
        "correct_answer": "B",
        "explanation": "Saklama hizmeti; yatırımcılara ait menkul kıymetlerin çalınma, kaybolma ve yetkisiz işlemlere karşı güvenli biçimde kayden veya fiziken muhafaza edilmesini ve hak kullanımlarının izlenmesini temin eder."
    },

    # 41. q_1012_ogretici_003
    "q_1012_ogretici_003": {
        "text": "Sermaye piyasasında 'Kaydileştirme' (Dematerialization) kavramı en doğru nasıl açıklanır?",
        "options": [
            {"key": "A", "text": "Sermaye piyasası araçlarının tamamının fiziki olarak basılarak şirket kasalarında saklanmasıdır"},
            {"key": "B", "text": "Aracı kurumların müşterilerine ait tüm nakit mevduatları döviz cinsine dönüştürmesidir"},
            {"key": "C", "text": "Hakların fiziki senet yerine bilgisayar ortamında elektronik hesaplar üzerinden kayden izlenmesidir"},
            {"key": "D", "text": "Borsadaki hisse senetlerinin alım satımının yalnızca mesai saatleriyle sınırlandırılmasıdır"},
            {"key": "E", "text": "Yatırım fonlarının katılma paylarının borsa kotundan tamamen çıkarılmasıdır"}
        ],
        "correct_answer": "C",
        "explanation": "Kaydileştirme; menkul kıymetlerin fiziki basımına son verilerek bunlara bağlı ortaklık ve alacak haklarının elektronik ortamda MKK nezdinde hak sahipleri adına açılan hesaplarda kayden izlenmesidir."
    },

    # 42. q_1012_ogretici_006
    "q_1012_ogretici_006": {
        "text": "Takas işlemlerinde 'Netleştirme' (Netting) mekanizmasının sağladığı temel operasyonel ve finansal fayda nedir?",
        "options": [
            {"key": "A", "text": "Karşılıklı borç ve alacakların mahsup edilerek gereken nakit ve kıymet transfer miktarının minimize edilmesi"},
            {"key": "B", "text": "Borsadaki her bir işlemin takasının ayrı ayrı brüt olarak sonuçlandırılmasını zorunlu kılması"},
            {"key": "C", "text": "Yatırımcıların borsa işlemlerinden doğan tüm vergi yükümlülüklerini tamamen ortadan kaldırması"},
            {"key": "D", "text": "Aracı kurumların Takasbank nezdinde teminat yatırma yükümlülüğünü tamamen kaldırması"},
            {"key": "E", "text": "Takas süresinin kanunen T+2 valöründen T+30 gün valörüne uzatılmasını sağlaması"}
        ],
        "correct_answer": "A",
        "explanation": "Netleştirme; aynı üyenin gün içindeki alım ve satım borç/alacaklarının karşılıklı mahsup edilerek sadece net bakiye kadar nakit ve menkul kıymet transferi yapılmasını, böylece likidite ihtiyacının ve operasyonel riskin büyük oranda düşürülmesini sağlar."
    },

    # 43. q_1012_ogretici_007
    "q_1012_ogretici_007": {
        "text": "Yatırım fonlarında 'Portföy Saklama Hizmeti'nin temel kurumsal koruma yaklaşımı nedir?",
        "options": [
            {"key": "A", "text": "Saklayıcı kuruluşun fon portföyünün piyasa değerini her durumda kâr garantisiyle sigortalaması"},
            {"key": "B", "text": "Fon varlıklarının kurucu şirketten bağımsız izlenerek mevzuata ve fon içtüzüğüne uygunluğunun denetlenmesi"},
            {"key": "C", "text": "Tüm fon alım satım ve hisse seçimi kararlarının saklama kuruluşu yöneticileri tarafından verilmesi"},
            {"key": "D", "text": "Fon katılma payı sahiplerinin genel kurul toplantılarında oy hakkı kullanmasının yasaklanması"},
            {"key": "E", "text": "Fon portföyündeki menkul kıymetlerin kurucu portföy yönetim şirketinin aktifine kaydedilmesi"}
        ],
        "correct_answer": "B",
        "explanation": "Portföy saklayıcısı; fon malvarlığının kurucunun malvarlığından ayrı olarak saklanmasını, fon varlıklarının haczedilememesini ve fon işlemlerinin mevzuat ile fon bilgilendirme dokümanlarına uygunluğunu gözetmekle yükümlüdür."
    },

    # 44. q_1012_ogretici_008
    "q_1012_ogretici_008": {
        "text": "Türev piyasalarda ve vadeli işlem sözleşmelerinde 'Uzlaşma' (Settlement) kavramı neyi ifade eder?",
        "options": [
            {"key": "A", "text": "Sözleşmeye taraf olan yatırımcıların aracı kurum sermayesine pay sahibi olarak ortak edilmesini"},
            {"key": "B", "text": "İhraççı şirketin borçlanma senetlerini erken itfa ederek yatırımcılara prim ödemesini"},
            {"key": "C", "text": "Sözleşmeden doğan teslim ve ödeme yükümlülüklerinin nakdi veya fiziki olarak sonuçlandırılmasını"},
            {"key": "D", "text": "Vadeli işlem sözleşmesinin vadesi dolmadan önce taraflarca mahkemeye intikal ettirilmesini"},
            {"key": "E", "text": "Takasbank'ın türev işlem komisyonlarını her takvim ayı sonunda iki katına çıkarmasını"}
        ],
        "correct_answer": "C",
        "explanation": "Türev araçlarda uzlaşma; sözleşme vadesinde veya pozisyon kapatıldığında, kâr/zararın nakit olarak mahsuplaşılması (nakdi uzlaşma) veya dayanak varlığın fiilen teslim edilmesi (fiziki uzlaşma) suretiyle pozisyonun kapatılmasıdır."
    },

    # 45. q_1012_ogretici_009
    "q_1012_ogretici_009": {
        "text": "Takasbank tarafından uygulanan 'Teminat Yönetimi' sisteminin temel yasal ve finansal amacı nedir?",
        "options": [
            {"key": "A", "text": "Borsadaki hisse senedi fiyatlarının değer kaybetmesini yasal olarak engellemek"},
            {"key": "B", "text": "Yatırımcılara borsa işlemlerinde %100 kesin anapara kâr garantisi sunmak"},
            {"key": "C", "text": "Piyasadaki tüm alım satım emirlerinin kredili işleme dönüştürülmesini zorunlu kılmak"},
            {"key": "D", "text": "Karşı taraf ve piyasa risklerine karşı takas yükümlülüklerinin güvenle ifasını temin etmek"},
            {"key": "E", "text": "Aracı kurumların sermaye piyasasında işlem yapma yetkilerini sınırlandırmak"}
        ],
        "correct_answer": "D",
        "explanation": "Teminat yönetimi; Takasbank'ın Merkezi Karşı Taraf olarak üstlendiği takas garantisini sürdürebilmesi amacıyla piyasa katılımcılarından risk düzeylerine göre başlangıç ve sürdürme teminatı alarak takas sistemini koruma mekanizmasıdır."
    },

    # 46. q_1012_ogretici_015
    "q_1012_ogretici_015": {
        "text": "Takas işlemlerinde 'Teslim Karşılığı Ödeme' (Delivery Versus Payment - DVP) ilkesi temel olarak hangi risk türünü ortadan kaldırmayı amaçlar?",
        "options": [
            {"key": "A", "text": "Makroekonomik enflasyon ve satın alma gücü kaybı riskini"},
            {"key": "B", "text": "Piyasa faiz oranlarının yükselmesiyle tahvil fiyatlarının düşmesi riskini"},
            {"key": "C", "text": "Halka açık ortaklıkların üretim tesislerinde oluşabilecek operasyonel kaza riskini"},
            {"key": "D", "text": "Döviz kurlarındaki aşırı dalgalanmalar nedeniyle oluşan kur farkı riskini"},
            {"key": "E", "text": "Karşı tarafın menkul kıymeti alıp parasını ödememesi veya tersi durumdaki Anapara/Temerrüt Riskini"}
        ],
        "correct_answer": "E",
        "explanation": "DVP (Teslim Karşılığı Ödeme) ilkesi; menkul kıymetin devri ile nakit bedelin ödenmesinin eşzamanlı olarak gerçekleşmesini sağlayarak, taraflardan birinin yükümlülüğünü ifa edip diğerinin ifa etmemesi riskini (Principal / Anapara Temerrüt Riski) tamamen sıfırlar."
    },

    # 47. q_1012_ogretici_016
    "q_1012_ogretici_016": {
        "text": "MKK nezdinde kayden izlenen hisse senetlerinde temettü, bedelli/bedelsiz sermaye artırımı gibi 'Hak Kullanımı' (Corporate Actions) işlemleri nasıl yürütülür?",
        "options": [
            {"key": "A", "text": "MKK ve Takasbank entegrasyonuyla elektronik sistem üzerinden otomatik olarak hak sahiplerinin hesaplarına aktarılır"},
            {"key": "B", "text": "Pay sahiplerinin hisse senetlerine ait fiziki kâr payı kuponlarını ihraççı şirket merkezine ibraz etmeleri suretiyle"},
            {"key": "C", "text": "Hak kullanım tutarlarının aracı kuruluşlarca bloke edilip yalnızca mali yıl sonunda topluca yatırımcılara devriyle"},
            {"key": "D", "text": "Yatırımcıların her hak kullanımı dönemi öncesinde Kamuyu Aydınlatma Platformu üzerinden yazılı talepte bulunmasıyla"},
            {"key": "E", "text": "Pay sahiplerinin Merkezi Kayıt Kuruluşu yerine doğrudan Borsa İstanbul Takas ve Operasyon Bölümüne başvurmasıyla"}
        ],
        "correct_answer": "A",
        "explanation": "Kaydi sistemde hak kullanımları (temettü, bedelli, bedelsiz); ihraççı şirketin MKK ve Takasbank ile koordinasyonu neticesinde merkezi elektronik kayıtlar üzerinden hak sahiplerinin yatırım hesaplarına otomatik olarak aktarılır."
    },

    # 48. q_1012_cikmis_010
    "q_1012_cikmis_010": {
        "text": "Olağandışı fiyat ve miktar hareketleri nedeniyle SPK veya Borsa tarafından brüt takasa alınan bir hisse senedinde hangi kural geçerlidir?",
        "options": [
            {"key": "A", "text": "Aynı gün içinde alınan hisse aynı gün satılabilir ve gün içi netleştirme uygulanır"},
            {"key": "B", "text": "Netleştirme uygulanmaz; alım bedeli peşin nakit, satım hissesi hazır olmalıdır (aynı gün satılamaz)"},
            {"key": "C", "text": "Kredili alım, açığa satış ve ödünç alma işlemleri serbest marjla yapılabilir"},
            {"key": "D", "text": "Takas mutabakatı Borsa İstanbul tarafından iptal edilerek hesaplar bir önceki güne döndürülür"},
            {"key": "E", "text": "Yalnızca şirketin imtiyazlı pay sahiplerinin alım satım yapmasına izin verilir"}
        ],
        "correct_answer": "B",
        "explanation": "Brüt takas tedbirinde; yatırımcıların gün içi alım-satım farkı üzerinden netleştirme yapmasına izin verilmez. Alım için hesapta nakdin peşin bulunması, satım için ise hissenin portföyde hazır bulunması şarttır; aynı gün alınan pay aynı gün satılamaz."
    },

    # 49. q_1012_cikmis_012
    "q_1012_cikmis_012": {
        "text": "6362 sayılı Sermaye Piyasası Kanunu m.81 uyarınca Merkezi Kayıt Kuruluşu'nun (MKK) münhasır yasal görevi nedir?",
        "options": [
            {"key": "A", "text": "Halka açık anonim ortaklıkların altı aylık ve yıllık finansal tablolarının bağımsız denetimini yapmak"},
            {"key": "B", "text": "Sermaye piyasası araçlarının kaydileştirilerek hak sahipleri bazında elektronik ortamda merkezi kaydını tutmak"},
            {"key": "C", "text": "Borsada işlem gören şirket paylarının halka arz fiyatını ve iskonto oranını re'sen belirlemek"},
            {"key": "D", "text": "Borsa İstanbul bünyesindeki hisse senedi endekslerini ve volatilite oranlarını hesaplamak"},
            {"key": "E", "text": "Yatırım kuruluşlarına sermaye piyasasında faaliyet izni ve yetki belgesi tahsis etmek"}
        ],
        "correct_answer": "B",
        "explanation": "MKK; sermaye piyasası araçlarının kaydileştirilmesine ilişkin işlemleri yürütmek ve bu araçlara bağlı hakları hak sahipleri bazında kayden izlemek üzere kurulan merkezi saklama kuruluşudur."
    },

    # 50. q_1012_cikmis_014
    "q_1012_cikmis_014": {
        "text": "MKK'nın Yatırımcı Bilgilendirme ve Blokaj Sistemi üzerinden bir yatırımcı kendi payları üzerine bizzat 'Yatırımcı Blokajı' koyduğunda ne gerçekleşir?",
        "options": [
            {"key": "A", "text": "Paylar derhal Borsa İstanbul Pay Piyasası'nda taban fiyattan satışa sunulur"},
            {"key": "B", "text": "Yatırımcı blokajı kaldırmadıkça aracı kurum dahil hiç kimse o paylar üzerinde transfer veya satış yapamaz"},
            {"key": "C", "text": "İhraççı ortaklık ilgili paylara ilişkin temettü ve bedelsiz hakkı dağıtımını iptal eder"},
            {"key": "D", "text": "Bloke edilen hisseler kanunen Hazine ve Maliye Bakanlığı hesaplarına mülkiyet olarak devredilir"},
            {"key": "E", "text": "Pay sahibinin genel kurula katılma ve elektronik ortamda oy kullanma hakkı tamamen sona erer"}
        ],
        "correct_answer": "B",
        "explanation": "Yatırımcı Blokajı; yatırımcının MKK nezdindeki kendi hisselerini kilitleyerek, blokajı yine kendisi e-YATIRIMCI şifresiyle kaldırıncaya kadar aracı kurumun dahi o payları satmasını veya başka bir hesaba aktarmasını engelleyen en üst düzey mülkiyet koruma mekanizmasıdır."
    }
}

updated = 0
for q in questions:
    qid = q['id']
    if qid in REPLACEMENTS_1012:
        rep = REPLACEMENTS_1012[qid]
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

print(f"\nSuccessfully upgraded all {updated} questions in Module 1012 to SPK exam committee standards!")
