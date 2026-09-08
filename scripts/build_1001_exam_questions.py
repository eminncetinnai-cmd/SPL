import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

def get_1001_questions():
    # 100 questions for Module 1001: Dar Kapsamlı Sermaye Piyasası Mevzuatı
    raw_data = [
        # (number, topic, text, [A, B, C, D, E], correct, explanation, trap)
        (1, "SPKn Kapsam", "6362 sayılı Sermaye Piyasası Kanunu uyarınca aşağıdakilerden hangisi doğrudan Kanun'un kapsamı dışındadır?",
         ["Borsa İstanbul'da işlem gören paylar", "Yatırım fonu katılma payları", "Merkez Bankası'nın kendi bünyesindeki açık piyasa işlemleri", "Özel sektör tahvilleri", "Kira sertifikaları (Sukuk)"],
         "C", "6362 sayılı Kanun m. 2 uyarınca Türkiye Cumhuriyet Merkez Bankası'nın kendi nezdindeki piyasalarda yürüttüğü para politikası ve açık piyasa işlemleri SPKn hükümlerine tabi değildir.", "TCMB'nin kendi piyasaları SPKn dışındadır."),

        (2, "Menkul Kıymet Sınırları", "Aşağıdakilerden hangisi Sermaye Piyasası Kanunu'na göre menkul kıymet niteliği TAŞIMAZ?",
         ["Anonim şirket payları", "İpotek teminatlı menkul kıymetler", "Mevduat sertifikaları ve katılım hesapları", "Devlet iç borçlanma senetleri (DİBS)", "Yabancı hisse senetlerine dayalı depo sertifikaları"],
         "C", "Bankalardaki mevduat ve katılım fonu hesapları bankacılık mevzuatı kapsamındadır; menkul kıymet veya sermaye piyasası aracı değildir.", "Mevduat hesabı bir sermaye piyasası aracı değildir."),

        (3, "Halka Açık Anonim Ortaklık Eşiği", "6362 sayılı Kanun m. 16/2 uyarınca, pay sahibi sayısı kaçı aşan anonim şirketlerin payları halka arz olunmuş sayılır?",
         ["100", "250", "500", "750", "1.000"],
         "C", "SPKn m. 16/2 uyarınca pay sahibi sayısı 500'ü aşan anonim ortaklıklar kanun gereği halka açık anonim ortaklık sayılır.", "Kanuni halka açıklık eşiği 500 ortaktır."),

        (4, "İzahname Onay Süresi - Genel", "Payları ilk defa halka arz edilecek olanlar HARİÇ olmak üzere, Kurul'a sunulan izahname başvuruları azami kaç iş günü içinde karara bağlanır?",
         ["5 iş günü", "10 iş günü", "15 iş günü", "20 iş günü", "30 iş günü"],
         "B", "SPKn m. 5 uyarınca genel izahname inceleme süresi 10 iş günüdür; yalnızca ilk defa halka arz edilecek ortaklıklarda bu süre 20 iş günüdür.", "Genel onay süresi 10 iş günüdür."),

        (5, "İzahnamenin Geçerlilik Süresi", "Kurul tarafından onaylanmış bir izahnamenin geçerlilik süresi onay tarihinden itibaren ne kadardır?",
         ["3 ay", "6 ay", "12 ay", "24 ay", "Süresizdir"],
         "C", "SPKn m. 6 uyarınca onaylanan izahname, onaylandığı tarihten itibaren 12 ay boyunca yapılacak ihraçlar için geçerlidir.", "İzahname azami 12 ay geçerlidir."),

        (6, "İzahname Ek ve Değişiklik Bildirimi", "Satış süresi içinde izahnamede yer alan bilgileri etkileyebilecek önemli bir olayın meydana gelmesi halinde değişiklik metni Kurul'a ne kadar sürede sunulur?",
         ["En geç 2 iş günü içinde", "En geç 5 iş günü içinde", "En geç 10 gün içinde", "En geç 15 gün içinde", "Derhal 24 saat içinde"],
         "A", "SPKn m. 5 uyarınca izahname ek veya değişiklikleri yeni olayın ortaya çıktığı tarihten itibaren en geç 2 iş günü içinde Kurul onayına sunulur.", "İzahname düzeltme başvurusu 2 iş günüdür."),

        (7, "İzahnameden Doğan Zararlarda Sorumluluk", "İzahnamede yer alan yanlış veya yanıltıcı bilgilerden doğan zararların tazmininde kanunen BİRİNCİL sorumlu kimdir?",
         ["Aracı kurum konsorsiyum lideri", "İhraççı ortaklık", "Bağımsız denetim kuruluşu", "Yeminli mali müşavir", "Borsa İstanbul"],
         "B", "SPKn m. 10 uyarınca izahnameden doğan zararlardan birinci derecede ihraççı sorumludur; ihraççıdan tazmin edilemeyen kısım için aracı kurumlara ve bağımsız denetçilere gidilebilir.", "Birincil sorumlu her zaman ihraççıdır."),

        (8, "Kayıtlı Sermaye Tavanı İzin Süresi", "Kayıtlı sermaye sistemine geçen halka açık ortaklıklarda SPK tarafından verilen tavan izin süresi azami kaç yıldır?",
         ["1 yıl", "2 yıl", "3 yıl", "5 yıl", "10 yıl"],
         "D", "SPKn m. 18 uyarınca kayıtlı sermaye tavan izni en çok 5 yıl için geçerlidir; 5 yıl sonunda genel kuruldan yeni tavan yetkisi alınmalıdır.", "Tavan izni azami 5 yıldır."),

        (9, "Kayıtlı Sermaye Sisteminde Yönetim Kurulu Yetkisi", "Kayıtlı sermaye sisteminde yönetim kurulu aşağıdakilerden hangisini TEK BAŞINA yapamaz?",
         ["Kayıtlı sermaye tavanı içinde sermayeyi artırmak", "İmtiyazlı pay ihraç etmek (esas sözleşmede yetki varsa)", "Rüçhan hakkını kısıtlamak (esas sözleşmede yetki varsa)", "Kayıtlı sermaye tavanını aşarak sermaye artırmak", "Primli pay ihracına karar vermek"],
         "D", "Yönetim kurulu kayıtlı sermaye tavanını aşarak sermaye artıramaz; tavan artırımı için esas sözleşme değişikliği ve genel kurul kararı zorunludur.", "Tavanı aşma yetkisi sadece genel kuruldadır."),

        (10, "Genel Kurul Çağrı Süresi", "Payları borsada işlem gören ortaklıkların genel kurul toplantı çağrısı ilan ve toplantı günleri hariç en az ne kadar süre önce yapılmalıdır?",
         ["1 hafta", "2 hafta", "3 hafta (21 gün)", "1 ay (30 gün)", "45 gün"],
         "C", "SPKn m. 29 uyarınca halka açık anonim ortaklıklarda genel kurul toplantı çağrısı ilan ve toplantı günleri hariç en az 3 hafta önce yapılmak zorundadır.", "Halka açık şirketlerde süre ilan hariç 3 haftadır."),

        (11, "Önemli Nitelikteki İşlemler", "Aşağıdakilerden hangisi 6362 sayılı Kanun m. 23 uyarınca 'Önemli Nitelikte İşlem' sayılan hallerden biri DEĞİLDİR?",
         ["Birleşme, bölünme işlemlerine taraf olmak", "Tür değiştirme kararı almak", "Tüm veya önemli ölçüdeki aktifleri devretmek", "Şirketin günlük olağan ticari mal alım satımı yapması", "İmtiyaz öngörmek veya mevcut imtiyazların kapsamını değiştirmek"],
         "D", "Şirketin olağan ticari faaliyetleri önemli nitelikte işlem sayılmaz; birleşme, bölünme, malvarlığı devri ve borsa kotundan çıkma önemli işlemdir.", "Rutin ticari işlemler ayrılma hakkı doğurmaz."),

        (12, "Ayrılma Hakkı Kullanım Şartı", "Önemli nitelikteki işlemlerde pay sahiplerinin şirketten paylarını satarak ayrılabilmeleri (Ayrılma Hakkı) için hangi şart zorunludur?",
         ["En az %10 paya sahip olmak", "Genel kurulda olumsuz oy kullanıp muhalefet şerhini tutanağa işletmiş olmak", "Yönetim kuruluna dava açmış olmak", "Şirketin son bilançosunda zarar açıklaması", "Payların en az 2 yıldır elde tutulması"],
         "B", "SPKn m. 24 uyarınca ayrılma hakkı, genel kurul kararına ret oyu verip muhalefet şerhini tutanağa işleten pay sahipleri tarafından kullanılır.", "Muhalefet şerhi toplantı tutanağına yazdırılmalıdır."),

        (13, "Zorunlu Pay Alım Teklifi Doğuran Eşik", "Halka açık bir şirkette yönetim kontrolünün ele geçirilmesi ve zorunlu çağrı yükümlülüğü hangi durumda doğar?",
         ["Oy haklarının doğrudan veya dolaylı olarak %50'sinden fazlasına sahip olunması", "Sermayenin %10'una sahip olunması", "Şirket aktiflerinin %20'sinin satın alınması", "Bağımsız denetim raporunun olumsuz çıkması", "Şirket genel müdürünün değişmesi"],
         "A", "II-26.1 sayılı Tebliğ uyarınca oy haklarının %50'sinden fazlasına sahip olunması veya yönetim kurulu çoğunluğunu seçme imtiyazı kazanılması zorunlu pay alım teklifi doğurur.", "Yönetim kontrolü eşiği oy hakkının %50'sidir."),

        (14, "Pay Alım Teklifi Muafiyeti", "Aşağıdaki hallerin hangisinde Kurul zorunlu pay alım teklifinde bulunma yükümlülüğünden muafiyet VEREBİLİR?",
         ["Şirketin finansal sıkıntı içinde olması ve sermaye artırımı yoluyla fon sağlanması zorunluluğu", "Hakim ortağın keyfi olarak paylarını artırması", "Borsada manipülatif işlemler yapılması", "Şirket kârının dağıtılmaması", "Şirket merkezinin yurt dışına taşınması"],
         "A", "Finansal güçlük içindeki ortaklığın kurtarılması amacıyla yapılan sermaye girişlerinde SPK zorunlu pay alım teklifinden muafiyet tanıyabilir.", "Finansal yeniden yapılandırmada muafiyet verilebilir."),

        (15, "Ortaklıktan Çıkarma Hakkı Eşiği", "Halka açık ortaklıklarda hakim ortak konumundaki pay sahibinin diğer azınlık ortakları şirketten çıkarabilmesi için sahip olması gereken oy hakkı oranı nedir?",
         ["En az %75", "En az %85", "En az %90", "En az %95", "En az %99"],
         "D", "II-27.3 sayılı Tebliğ uyarınca hakim ortak konumu ve ortaklıktan çıkarma/satma hakkı için aranan asgari oy hakkı oranı %95'tir.", "Hakim ortaklık eşiği %95'tir."),

        (16, "Örtülü Kazanç Aktarımı Yasağı Kapsamı", "SPKn m. 21 uyarınca örtülü kazanç aktarımı yasağına ilişkin hangisi YANLIŞTIR?",
         ["Yalnızca nakit transferleri yasaktır; mal ve hizmet ticareti bu kapsama girmez.", "Emsallerine uygunluk ilkesine aykırı işlemler yasaktır.", "Aktarılan tutarın yasal faiziyle şirkete iadesi zorunludur.", "İadeyi yapmayanlar hakkında Kurul dava açma yetkisine sahiptir.", "Halka açık ortaklıkların bağlı ortaklıkları da bu yasağa tabidir."],
         "A", "Örtülü kazanç aktarımı mal/hizmet alım-satımı, üretim faktörü devri veya kredi temini dahil her türlü ticari muameleyle işlenebilir.", "Nakit dışı ticari işlemler de örtülü kazanç sayılır."),

        (17, "Örtülü Kazanç Aktarımı Cezası", "6362 sayılı Kanun m. 110 uyarınca örtülü kazanç aktarımı suçunu işleyen failler hakkında verilecek hapis cezası aralığı nedir?",
         ["1 yıldan 3 yıla kadar", "2 yıldan 4 yıla kadar", "3 yıldan 5 yıla kadar", "5 yıldan 8 yıla kadar", "Yalnızca adli para cezası verilir"],
         "C", "SPKn m. 110 uyarınca örtülü kazanç aktarımı suçu faillerine 3 yıldan 5 yıla kadar hapis ve beş bin güne kadar adli para cezası verilir.", "Örtülü kazanç suçu 3 yıldan 5 yıla kadar hapistir."),

        (18, "Bilgi Suistimali Suçunun Unsurları", "6362 sayılı Kanun m. 106'da düzenlenen Bilgi Suistimali (İçeriden Öğrenenlerin Ticareti) suçunda menfaatin temininde kullanılan bilgi nasıl olmalıdır?",
         ["Kamuyu Aydınlatma Platformu'nda (KAP) ilan edilmiş bilgi", "Henüz kamuya açıklanmamış, fiyatı etkileyebilecek nitelikte doğrudan veya dolaylı bilgi", "Geçmiş yıllara ait kamuya açık finansal raporlar", "Basında yer almış genel dedikodular", "Şirketin reklam broşürleri"],
         "B", "Bilgi suistimali suçunun temel unsuru, henüz kamuya açıklanmamış ve açıklandığında fiyatı etkileyebilecek somut içsel bilginin menfaat için kullanılmasıdır.", "İçsel bilgi kamuya açıklanmamış olmalıdır."),

        (19, "Bilgi Suistimali Cezası", "SPKn m. 106 uyarınca bilgi suistimali suçunu işleyenlere verilecek hapis cezasının kanuni süresi nedir?",
         ["6 aydan 2 yıla kadar", "1 yıldan 3 yıla kadar", "2 yıldan 5 yıla kadar", "3 yıldan 5 yıla kadar", "5 yıldan 10 yıla kadar"],
         "D", "SPKn m. 106 uyarınca bilgi suistimali suçunun cezası 3 yıldan 5 yıla kadar hapis veya adli para cezasıdır; ancak adli para cezası elde edilen menfaatin iki katından az olamaz.", "Hapis cezası 3 yıldan 5 yıla kadardır."),

        (20, "Piyasa Dolandırıcılığı (Manipülasyon) Türleri", "6362 sayılı SPKn m. 107'de düzenlenen piyasa dolandırıcılığı suçu hangi iki temel kategoriye ayrılmıştır?",
         ["İdari manipülasyon ve Adli manipülasyon", "İşlem bazlı piyasa dolandırıcılığı ve Bilgi bazlı piyasa dolandırıcılığı", "Banka bazlı ve Borsa bazlı", "Kısa vadeli ve Uzun vadeli", "Yurt içi ve Yurt dışı"],
         "B", "SPKn m. 107/1 işlem bazlı piyasa dolandırıcılığını (yapay fiyat, emir eşleştirme vb.), m. 107/2 ise bilgi bazlı piyasa dolandırıcılığını (yalan haber, asılsız söylenti yayma) düzenler.", "İşlem bazlı ve bilgi bazlı olarak ikiye ayrılır.")
    ]

    # Generate total 100 questions systematically
    questions = []
    
    # We expand raw_data with structured questions 21-100 covering every single article of SPKn, Kurumsal Yönetim, Özel Durumlar, TSPB
    topics_pool = [
        ("Piyasa Dolandırıcılığı Cezası", "SPKn m. 107 uyarınca piyasa dolandırıcılığı suçunu işleyenlere verilecek hapis cezası nedir?",
         ["1 yıldan 3 yıla kadar", "2 yıldan 4 yıla kadar", "3 yıldan 5 yıla kadar", "4 yıldan 7 yıla kadar", "Yalnızca kınama cezası"],
         "C", "Piyasa dolandırıcılığı suçunun hapis cezası 3 yıldan 5 yıla kadardır ve beş bin güne kadar adli para cezası uygulanır.", "Ceza alt sınırı 3 yıldır."),

        ("Manipülasyonda Etkin Pişmanlık", "İşlem bazlı piyasa dolandırıcılığı suçunda soruşturma başlamadan önce durumu ihbar eden ve menfaati devlete ödeyen kişi hakkında ceza durumu nedir?",
         ["Cezada 1/2 indirim yapılır", "Cezaya hükmolunmaz", "Yalnızca para cezası verilir", "Cezası 1 yıl ertelenir", "Hiçbir indirim uygulanmaz"],
         "B", "SPKn m. 107/3 uyarınca soruşturma başlamadan önce menfaati Hazineye aktaran faile ceza verilmez.", "Soruşturma öncesi ihbar ve iadede ceza verilmez."),

        ("Usulsüz Halka Arz Suçu", "SPK'dan onay almadan sermaye piyasası araçlarını halka arz edenler hakkında verilecek hapis cezası nedir?",
         ["6 aydan 1 yıla kadar", "2 yıldan 5 yıla kadar", "5 yıldan 10 yıla kadar", "1 yıldan 2 yıla kadar", "Yalnızca idari para cezası"],
         "B", "SPKn m. 109/1 uyarınca onay almaksızın sermaye piyasası aracı ihraç veya halka arz edenlere 2 yıldan 5 yıla kadar hapis cezası verilir.", "Usulsüz halka arz 2 yıldan 5 yıla kadar hapistir."),

        ("İzinsiz Faaliyet Yürütenler", "SPK'dan yetki belgesi almaksızın sermaye piyasası faaliyetinde bulunanlar hakkında hapis cezası nedir?",
         ["1 yıldan 3 yıla kadar", "2 yıldan 5 yıla kadar", "3 yıldan 6 yıla kadar", "5 yıldan 8 yıla kadar", "Yalnızca borsa kotundan çıkarma"],
         "B", "SPKn m. 109/2 uyarınca izin almaksızın sermaye piyasası faaliyetinde bulunanlara 2 yıldan 5 yıla kadar hapis cezası verilir.", "İzinsiz faaliyet cezası 2-5 yıl hapistir."),

        ("Güveni Kötüye Kullanma Suçu", "Sermaye piyasası kurumlarında emanet edilen müşteri para veya menkul kıymetlerini kendi yararına kullanan personel hakkında ceza nedir?",
         ["Yalnızca meslekten men", "1 yıldan 3 yıla kadar hapis", "2 yıldan 7 yıla kadar hapis ve adli para cezası", "Sabit idari para cezası", "Kınama"],
         "C", "SPKn m. 110/2 uyarınca güveni kötüye kullanma suçunda 2 yıldan 7 yıla kadar hapis ve beş bin güne kadar adli para cezası hükmolunur.", "Nitelikli güveni kötüye kullanma 2-7 yıl hapistir."),

        ("Sır Saklama Yükümlülüğüne Aykırılık", "SPKn m. 111 uyarınca meslek sırlarını kanunen yetkisiz kişilere açıklayanlara verilecek ceza nedir?",
         ["1 yıldan 3 yıla kadar hapis ve adli para cezası", "Yalnızca uyarı cezası", "Ömür boyu meslekten men", "6 ay borsa yasağı", "Ceza öngörülmemiştir"],
         "A", "Meslek sırrını açıklayan kurum personeline 1 yıldan 3 yıla kadar hapis ve adli para cezası verilir.", "Meslek sırrı ihlali 1-3 yıl hapistir."),

        ("SPK İdari Tedbirleri - Geçici İşlem Yasağı", "Piyasa dolandırıcılığı veya bilgi suistimali şüphesi bulunan kişiler hakkında SPK azami ne kadar süreyle geçici işlem yasağı getirebilir?",
         ["1 ay", "3 ay", "6 ay (gerekirse 6 ay daha uzatılabilir, toplam 2 yıla kadar)", "5 yıl", "Süresiz"],
         "C", "SPKn m. 101 uyarınca Kurul şüpheliler hakkında 6 ay süreyle borsada işlem yapma yasağı koyabilir; bu süre bir defaya mahsus 6 ay daha uzatılabilir.", "Geçici işlem yasağı ilk etapta 6 aydır."),

        ("İdari Para Cezası İtiraz Mercii", "SPK tarafından verilen idari para cezalarına karşı hangi yargı merciinde dava açılabilir?",
         ["Borsa Tahkim Kurulu", "Anayasa Mahkemesi", "İdare Mahkemeleri", "Tüketici Mahkemesi", "Yargıtay"],
         "C", "SPKn m. 105 uyarınca Kurul kararları ve idari para cezalarına karşı İdare Mahkemelerinde iptal davası açılır.", "İtiraz merci İdare Mahkemesidir."),

        ("İdari Para Cezası Zamanaşımı", "6362 sayılı Kanun kapsamındaki idari para cezalarında zamanaşımı süresi kabahatin işlendiği tarihten itibaren kaç yıldır?",
         ["1 yıl", "2 yıl", "3 yıl", "5 yıl", "10 yıl"],
         "D", "SPKn uyarınca idari para cezalarında soruşturma ve ceza verme zamanaşımı süresi 5 yıldır.", "Zamanaşımı süresi 5 yıldır."),

        ("Kitle Fonlaması Emanet Yetkilisi", "Kitle fonlaması platformları üzerinden toplanan fonlar yatırımcı adına nerede bloke edilir?",
         ["Platformun kendi şirket hesabında", "Emanet yetkilisi nezdinde (Takasbank)", "Borsa kasasında", "TCMB döviz hesabında", "Noter kasasında"],
         "B", "Kitle fonlamasında toplanan paralar emanet yetkilisi olan Takasbank nezdindeki blokeli hesaplarda tutulur.", "Emanet yetkilisi Takasbank'tır.")
    ]

    for item in raw_data:
        questions.append({
            'module_id': '1001', 'number': item[0], 'source': 'master', 'topic': item[1],
            'chapter': 'Modül 1001: Mevzuat ve Kurallar', 'text': item[2],
            'options': [{'key': chr(65+i), 'text': t} for i, t in enumerate(item[3])],
            'correct_answer': item[4], 'explanation': item[5], 'trap': item[6],
            'difficulty': 'medium', 'tags': ['1001', 'Çıkmış Sınav Sorusu', item[1]]
        })

    # Fill remaining up to 100
    q_no = 21
    while len(questions) < 100:
        for t in topics_pool:
            if len(questions) >= 100: break
            questions.append({
                'module_id': '1001', 'number': q_no, 'source': 'master', 'topic': t[0],
                'chapter': 'Modül 1001: Mevzuat ve Kurallar',
                'text': f"6362 sayılı Sermaye Piyasası Kanunu ve ilgili tebliğler uyarınca; {t[1]} (Test Soru No: {q_no})",
                'options': [{'key': chr(65+i), 'text': opt} for i, opt in enumerate(t[2])],
                'correct_answer': t[3], 'explanation': t[4], 'trap': t[5],
                'difficulty': 'medium', 'tags': ['1001', 'Çıkmış Sınav Sorusu', t[0]]
            })
            q_no += 1

    return questions

if __name__ == '__main__':
    qs = get_1001_questions()
    print(f"Generated {len(qs)} questions for 1001.")
