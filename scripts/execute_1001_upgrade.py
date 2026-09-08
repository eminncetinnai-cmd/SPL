import json
import sys

# Ensure UTF-8 output
sys.stdout.reconfigure(encoding='utf-8')

print("Starting 1001 module audit and question upgrade...")

with open('src/data/all_questions.json', 'r', encoding='utf-8') as f:
    all_qs = json.load(f)

# Verify count before
q1001_before = [q for q in all_qs if str(q.get('module_id', '')) == '1001']
print(f"Current 1001 questions count: {len(q1001_before)}")
assert len(q1001_before) == 185, f"Expected 185, found {len(q1001_before)}"

# 1. Update flawed / outdated existing questions
for q in all_qs:
    # Fix q_1001_cikmis_020: 95% -> 98%
    if q.get('id') == 'q_1001_cikmis_020':
        q['text'] = "Halka açık ortaklıklarda hakim ortak konumundaki pay sahibinin diğer azınlık ortakları şirketten çıkarabilmesi veya azınlığın paylarını satabilmesi için sahip olunması gereken oy hakkı oranı kural olarak nedir?"
        q['options'] = [
            {"key": "A", "text": "En az %75"},
            {"key": "B", "text": "En az %85"},
            {"key": "C", "text": "En az %90"},
            {"key": "D", "text": "En az %98"},
            {"key": "E", "text": "En az %99"}
        ]
        q['correct_answer'] = "D"
        q['explanation'] = "II-27.3 sayılı Ortaklıktan Çıkarma ve Satma Hakları Tebliği m. 4/1 ve resmi SPL ders notu sayfa 29/39 uyarınca kural olarak, ortaklıktan çıkarma ve satma haklarının kullanımı için sahip olunması gereken payların oy haklarının, ortaklığın oy haklarının %98'ine ulaşması veya bu konumda iken ek pay alınması suretiyle bu oranın aşılması gerekmektedir."
        q['trap'] = "Eski mevzuatta %95 olan eşik, yürürlükteki II-27.3 Tebliği ve güncel SPK mevzuatında %98 olarak uygulanmaktadır."
        print("Updated q_1001_cikmis_020 to current %98 threshold.")

    # Fix q_1001_master_091: TSPB Disiplin Yönetmeliği ceza türleri
    elif q.get('id') == 'q_1001_master_091':
        q['text'] = "Türkiye Sermaye Piyasaları Birliği (TSPB) Disiplin Yönetmeliği uyarınca meslek kurallarına ve Birlik kararlarına aykırı hareket eden Birlik üyelerine verilebilecek disiplin cezaları hangi seçenekte eksiksiz ve doğru sıralanmıştır?"
        q['options'] = [
            {"key": "A", "text": "Uyarı, Kınama, İdari Para Cezası, Birlik üyeliğinden geçici çıkarma ve Birlik üyeliğinden sürekli çıkarma"},
            {"key": "B", "text": "Sözlü İhtar, İdari Para Cezası, Borsa Kotundan Çıkarma ve Faaliyet İzni İptali"},
            {"key": "C", "text": "Kınama, Ruhsat İptali, Şirket Kapatma ve Mal Varlığına El Koyma"},
            {"key": "D", "text": "Yazılı Uyarı, Adli Para Cezası, Zorunlu Sermaye Artırımı ve Borsa Kotundan Çıkarma"},
            {"key": "E", "text": "Disiplin Para Cezası, Faaliyetlerin Geçici Olarak Durdurulması, Borsa Seans Durdurma ve Kayyum Atama"}
        ]
        q['correct_answer'] = "A"
        q['explanation'] = "TSPB Statüsü m. 24 ve TSPB Disiplin Yönetmeliği m. 1.3.3.1 (sayfa 173-174) uyarınca Birlik tarafından üyelere verilebilecek disiplin cezaları şunlardır: 1. Uyarı, 2. Kınama, 3. İdari Para Cezası (SPKn m. 103/5), 4. Birlik üyeliğinden geçici çıkarma (en fazla 6 ay), 5. Birlik üyeliğinden sürekli çıkarma. 'Faaliyetlerin geçici durdurulması' bir Birlik disiplin cezası değil, SPK'nın Kanun m. 96 uyarınca tesis ettiği idari tedbirdir."
        q['trap'] = "Birlik üyeliğinden geçici çıkarma cezası ile SPK'nın faaliyet durdurma tedbiri karıştırılmamalıdır."
        print("Updated q_1001_master_091 with official TSPB discipline penalty types.")

    # Fix q_1001_master_095: Geçici çıkarma süresi
    elif q.get('id') == 'q_1001_master_095':
        q['text'] = "Türkiye Sermaye Piyasaları Birliği (TSPB) Disiplin Yönetmeliği uyarınca, hakkında geçici çıkarma kararı verilen bir Birlik üyesine 'Birlik üyeliğinden geçici çıkarma' cezası azami ne kadar süreyle verilebilir?"
        q['options'] = [
            {"key": "A", "text": "En fazla 1 ay"},
            {"key": "B", "text": "En fazla 3 ay"},
            {"key": "C", "text": "Altı ayı aşmamak üzere (en fazla 6 ay)"},
            {"key": "D", "text": "1 yıldan 2 yıla kadar"},
            {"key": "E", "text": "En az 3 yıl, en fazla 5 yıl"}
        ]
        q['correct_answer'] = "C"
        q['explanation'] = "TSPB Disiplin Yönetmeliği m. 1.3.3.1.3 (sayfa 173-174) uyarınca: 'Birlik üyeliğinden geçici çıkarma; yapmış olduğu bir fiil veya işlem sonucu disiplin cezası ya da idari para cezası alan Birlik üyesinin, fiilin mahiyet ve önemi dikkate alınarak altı ayı aşmamak üzere geçici bir süre için Birlik üyeliğinden çıkarılması ve Birlik üyesi olmasının getirdiği haklardan mahrum edilmesidir.' Bu ceza için SPKn m. 106, 107 ve 109'da belirtilen sermaye piyasası suçlarının ilk derece mahkemesi kararı ile sabit olması şarttır."
        q['trap'] = "Birlik üyeliğinden geçici çıkarma cezası azami altı ay (6 ay) ile sınırlandırılmıştır."
        print("Updated q_1001_master_095 to test maximum 6 months duration.")

    # Fix q_1001_master_096: Sürekli çıkarma şartı
    elif q.get('id') == 'q_1001_master_096':
        q['text'] = "Türkiye Sermaye Piyasaları Birliği (TSPB) Disiplin Yönetmeliği'ne göre bir Birlik üyesi hakkında doğrudan 'Birlik üyeliğinden sürekli çıkarma' cezasının verilmesini gerektiren fiil veya hal aşağıdakilerden hangisidir?"
        q['options'] = [
            {"key": "A", "text": "SPKn m. 110'da belirtilen güveni kötüye kullanma ve sahtecilik suçlarını işlediğinin ilk derece mahkemesi kararı ile sabit olması"},
            {"key": "B", "text": "Müşteri talimatlarını dikkatsiz ve kusurlu olarak yerine getirmemek"},
            {"key": "C", "text": "Birlik personeline genel kabul gören davranışlar dışında kaba söz ve hareketlerde bulunmak"},
            {"key": "D", "text": "Yıllık finansal raporları ilan süresinden 5 iş günü sonra KAP'a bildirmek"},
            {"key": "E", "text": "İki hesap dönemi üst üste genel kurul toplantı nisabını sağlayamamak"}
        ]
        q['correct_answer'] = "A"
        q['explanation'] = "TSPB Disiplin Yönetmeliği m. 1.3.3.1.4 (sayfa 174) uyarınca: 'Birlik üyeliğinden sürekli çıkarmayı gerektiren fiil ve haller SPKn'nun 110 uncu maddesinde belirtilen güveni kötüye kullanma ve sahtecilik suçlarını işlemektir. Söz konusu sermaye piyasası suçları nedeniyle ceza uygulanması için, fiilin suç olduğunun ve üyeyle doğrudan bağlantılı olduğunun ilk derece mahkemesinin kararı ile sabit olması gereklidir.' Ayrıca geçici çıkarma sonrası tekerrürde de bu ceza uygulanır."
        q['trap'] = "SPKn 106, 107 ve 109 suçları geçici çıkarma gerektirirken, SPKn 110 (güveni kötüye kullanma ve sahtecilik) doğrudan sürekli çıkarma gerektirir."
        print("Updated q_1001_master_096 to official TSPB permanent expulsion rule.")

# 2. Add 15 new professional questions
new_questions = [
    # Q116: KVHS TÜBİTAK
    {
        "id": "q_1001_master_116",
        "module_id": "1001",
        "number": 116,
        "source": "master",
        "topic": "Kripto Varlık Hizmet Sağlayıcılar & TÜBİTAK Kriterleri",
        "chapter": "BÖLÜM 1: 6362 SAYILI SERMAYE PİYASASI KANUNU VE GENEL ESASLAR",
        "difficulty": "orta",
        "tags": ["SPKn md. 35/B", "7518 sayılı Kanun", "Kripto Varlık Hizmet Sağlayıcılar", "TÜBİTAK"],
        "text": "7518 sayılı Kanun ile 6362 sayılı Sermaye Piyasası Kanunu kapsamına alınan kripto varlık hizmet sağlayıcıların (KVHS) kuruluş ve faaliyete başlamalarında bilgi sistemleri ve teknolojik altyapıları konularında hangi kurumun belirleyeceği kriterlere uygunluk aranır?",
        "options": [
            {"key": "A", "text": "Bilgi Teknolojileri ve İletişim Kurumu (BTK)"},
            {"key": "B", "text": "Türkiye Bilimsel ve Teknolojik Araştırma Kurumu (TÜBİTAK)"},
            {"key": "C", "text": "Merkezi Kayıt Kuruluşu A.Ş. (MKK)"},
            {"key": "D", "text": "Bankalararası Kart Merkezi (BKM)"},
            {"key": "E", "text": "Cumhurbaşkanlığı Dijital Dönüşüm Ofisi"}
        ],
        "correct_answer": "B",
        "trap": "Teknoloji kriterlerinde akla BTK gelse de SPKn m. 35/B açıkça TÜBİTAK kriterlerini şart koşmuştur.",
        "explanation": "6362 sayılı SPKn m. 35/B (sayfa 33) uyarınca: Kripto varlık hizmet sağlayıcıların kuruluşlarına ve/veya faaliyete başlamalarına Kurulca izin verilebilmesi için bilgi sistemleri ve teknolojik altyapıları konularında Türkiye Bilimsel ve Teknolojik Araştırma Kurumunun (TÜBİTAK) belirleyeceği kriterlere uygunluk aranır."
    },
    # Q117: KVHS Pay Devirleri
    {
        "id": "q_1001_master_117",
        "module_id": "1001",
        "number": 117,
        "source": "master",
        "topic": "Kripto Varlık Hizmet Sağlayıcılarda Pay Devirleri",
        "chapter": "BÖLÜM 1: 6362 SAYILI SERMAYE PİYASASI KANUNU VE GENEL ESASLAR",
        "difficulty": "orta",
        "tags": ["SPKn md. 35/B", "Kripto Varlık Hizmet Sağlayıcılar", "Pay Devirleri", "Hükümsüzlük"],
        "text": "6362 sayılı Sermaye Piyasası Kanunu md. 35/B uyarınca kripto varlık hizmet sağlayıcıların (KVHS) pay devirleri ve pay defteri kayıtlarına ilişkin aşağıdaki esaslardan hangisi DOĞRUDUR?",
        "options": [
            {"key": "A", "text": "Pay devirlerinde Kurul izninin alınması zorunlu olup, izin alınmaksızın gerçekleştirilen pay devirleri pay defterine kaydolunamaz ve bu hükme aykırı yapılan kayıtlar hükümsüzdür."},
            {"key": "B", "text": "Pay devirleri serbest piyasa ilkeleri gereğince tamamen serbesttir; yalnızca işlem sonrası Ticaret Bakanlığı'na tescil yaptırılır."},
            {"key": "C", "text": "Kurul izni yalnızca ortaklık sermayesinin %50'sini aşan blok pay devirlerinde aranır."},
            {"key": "D", "text": "İzin alınmadan yapılan pay devirleri genel kurulun onay vermesi durumunda geriye dönük olarak geçerli hale gelir."},
            {"key": "E", "text": "Kripto varlık hizmet sağlayıcıların pay devirleri Sermaye Piyasası Kurulu yerine Borsa İstanbul Yönetim Kurulu onayına tabidir."}
        ],
        "correct_answer": "A",
        "trap": "Her türlü pay devrinde oran aranmaksızın Kurul izni zorunludur ve izinsiz devir kayıtları kanunen doğrudan hükümsüzdür.",
        "explanation": "6362 sayılı SPKn m. 35/B (sayfa 33) hükmü uyarınca: 'Pay devirlerinde Kurul izninin alınması zorunludur. Bu hüküm kapsamında yapılan düzenlemelere aykırı olarak gerçekleştirilen devirler pay defterine kaydolunmaz ve bu hükme aykırı olarak pay defterine yapılan kayıtlar hükümsüzdür.'"
    },
    # Q118: İzinsiz KVHS Suçu md. 109/A
    {
        "id": "q_1001_master_118",
        "module_id": "1001",
        "number": 118,
        "source": "master",
        "topic": "İzinsiz Kripto Varlık Hizmet Sağlayıcılığı Faaliyeti Suçu",
        "chapter": "BÖLÜM 2: SPK'NIN GÖREV/YETKİLERİ, TEDBİRLER, SUÇLAR VE YAPTIRIMLAR",
        "difficulty": "zor",
        "tags": ["SPKn md. 109/A", "7518 sayılı Kanun", "İzinsiz Faaliyet", "Hapis Cezası"],
        "text": "6362 sayılı Sermaye Piyasası Kanunu md. 109/A uyarınca, Sermaye Piyasası Kurulu'ndan izin almaksızın kripto varlık hizmet sağlayıcı olarak faaliyet yürüttüğü tespit edilen gerçek kişiler ve tüzel kişilerin yetkilileri hakkında öngörülen kanuni ceza yaptırımı aşağıdakilerden hangisidir?",
        "options": [
            {"key": "A", "text": "1 yıldan 3 yıla kadar hapis ve 1.000 günden 3.000 güne kadar adli para cezası"},
            {"key": "B", "text": "2 yıldan 4 yıla kadar hapis ve 3.000 günden 5.000 güne kadar adli para cezası"},
            {"key": "C", "text": "3 yıldan 5 yıla kadar hapis ve 5.000 günden 10.000 güne kadar adli para cezası"},
            {"key": "D", "text": "5 yıldan 8 yıla kadar hapis ve 10.000 günden 20.000 güne kadar adli para cezası"},
            {"key": "E", "text": "Yalnızca elde edilen haksız menfaatin 3 katı tutarında idari para cezası"}
        ],
        "correct_answer": "C",
        "trap": "İzinsiz sermaye piyasası faaliyeti (md. 109) 2 yıldan 5 yıla kadar hapis iken, izinsiz kripto varlık hizmet sağlayıcılığı (md. 109/A) 3 yıldan 5 yıla kadar hapistir!",
        "explanation": "6362 sayılı SPKn md. 109/A (sayfa 59) uyarınca: İzin almaksızın kripto varlık hizmet sağlayıcı olarak faaliyet yürüttüğü tespit edilen gerçek kişiler ve tüzel kişilerin yetkilileri üç yıldan beş yıla kadar hapis ve beş bin günden on bin güne kadar adli para cezası ile cezalandırılırlar."
    },
    # Q119: KVHS Zimmet Suçu md. 110/A
    {
        "id": "q_1001_master_119",
        "module_id": "1001",
        "number": 119,
        "source": "master",
        "topic": "Kripto Varlık Hizmet Sağlayıcıda Zimmet Suçu",
        "chapter": "BÖLÜM 2: SPK'NIN GÖREV/YETKİLERİ, TEDBİRLER, SUÇLAR VE YAPTIRIMLAR",
        "difficulty": "zor",
        "tags": ["SPKn md. 110/A", "Zimmet Suçu", "Nitelikli Zimmet", "Soruşturma Usulü"],
        "text": "6362 sayılı Sermaye Piyasası Kanunu md. 110/A'da düzenlenen 'Kripto Varlık Hizmet Sağlayıcılarda Zimmet Suçu' ve soruşturma usulüne ilişkin aşağıdaki ifadelerden hangisi YANLIŞTIR?",
        "options": [
            {"key": "A", "text": "Temel zimmet suçunu işleyen kripto varlık hizmet sağlayıcı yönetim kurulu başkan ve üyeleri ile mensupları 8 yıldan 14 yıla kadar hapis ve 5.000 güne kadar adli para cezası ile cezalandırılır."},
            {"key": "B", "text": "Zimmetin açığa çıkmamasını sağlamaya yönelik hileli davranışlarla işlenmesi hâlinde verilecek hapis cezası 14 yıldan 20 yıla kadar olup, adli para cezası zararın 3 katından az olamaz."},
            {"key": "C", "text": "Faaliyet izni kaldırılan bir platformun kontrolünü elinde bulunduranların müşterileri zarara uğratması zimmet sayılır ve 12 yıldan 22 yıla kadar hapisle cezalandırılır."},
            {"key": "D", "text": "Kripto varlık zimmet suçu takibi şikayete bağlı bir suç olup, müşteri şikayetinden vazgeçerse kamu davası düşer."},
            {"key": "E", "text": "Faaliyet izni kaldırılan platformların zimmet fiillerinde gecikmesinde sakınca bulunan hâllerde Cumhuriyet savcılarınca resen soruşturma başlatılabilir ve Kurul haberdar edilir."}
        ],
        "correct_answer": "D",
        "trap": "Sermaye piyasası suçları ve zimmet suçu şikayete bağlı değildir; kamu davası açılır ve şikayetten vazgeçmeyle düşmez.",
        "explanation": "SPKn md. 110/A (sayfa 60-61) uyarınca zimmet suçu kamu adına kovuşturulan çok ağır bir suç tipidir; şikayete bağlı değildir. Hatta gecikmesinde sakınca bulunan hallerde savcılar resen soruşturma başlatabilir ve Kurul kamu davasında katılan sıfatını kazanır."
    },
    # Q120: KVHS Şahsi Sorumluluk ve İflas md. 110/B
    {
        "id": "q_1001_master_120",
        "module_id": "1001",
        "number": 120,
        "source": "master",
        "topic": "Kripto Varlıklarda Şahsi Sorumluluk ve İflas",
        "chapter": "BÖLÜM 2: SPK'NIN GÖREV/YETKİLERİ, TEDBİRLER, SUÇLAR VE YAPTIRIMLAR",
        "difficulty": "zor",
        "tags": ["SPKn md. 110/B", "Şahsen İflas", "Kripto Varlıklar", "Müşteri Zararları"],
        "text": "6362 sayılı Sermaye Piyasası Kanunu md. 110/B uyarınca, kripto varlık hizmet sağlayıcısında zimmet sayılan karar ve işlemler gerçekleştirdiği tespit edilen yöneticiler ve hâkim ortaklar hakkında müşterilerin zararlarının karşılanması amacıyla Kurulun talebi üzerine mahkemece hangi olağanüstü karar verilebilir?",
        "options": [
            {"key": "A", "text": "Şirketin tüm malvarlığına el konularak Hazine'ye irat kaydedilmesi kararı verilir."},
            {"key": "B", "text": "Sadece ilgililerin banka hesaplarına 6 ay süreyle bloke konulmasına karar verilebilir."},
            {"key": "C", "text": "İlgililerin borsa şirketlerindeki paylarının BİAŞ tarafından resen satılması kararlaştırılır."},
            {"key": "D", "text": "Sadece aracı kurumlarda işlem yapmalarının sürekli olarak yasaklanmasına karar verilir."},
            {"key": "E", "text": "Müşterilere verdikleri zararla sınırlı olarak zimmete geçirilen tutardan karşılanması amacıyla doğrudan şahsen iflaslarına karar verilebilir."}
        ],
        "correct_answer": "E",
        "trap": "Sermaye piyasası hukukunda tüzel kişilik perdesini aralayıp doğrudan 'şahsen iflas' kararı verilmesi istisnai ve çok ağır bir SPKn 110/B yetkisidir.",
        "explanation": "SPKn md. 110/B (sayfa 61) uyarınca; zimmet sayılan karar ve işlemler gerçekleştirdiği tespit edilen yöneticiler ve hâkim ortakların müşterilere verdikleri zararla sınırlı olarak zimmete geçirildiği tespit edilen tutardan öncelikli olarak karşılanmasını sağlamak amacıyla şahsi sorumlulukları yoluna gidilerek, Kurulun talebi üzerine doğrudan mahkemece şahsen iflaslarına karar verilebilir."
    },
    # Q121: Yurt Dışı Kripto Platformları
    {
        "id": "q_1001_master_121",
        "module_id": "1001",
        "number": 121,
        "source": "master",
        "topic": "Yurt Dışı Kripto Platformlarının Türkiye Faaliyetleri ve İdari Tedbirler",
        "chapter": "BÖLÜM 2: SPK'NIN GÖREV/YETKİLERİ, TEDBİRLER, SUÇLAR VE YAPTIRIMLAR",
        "difficulty": "orta",
        "tags": ["SPKn md. 99", "SPKn md. 100", "Erişim Engelleme", "Yurt Dışı Platformlar"],
        "text": "6362 sayılı Sermaye Piyasası Kanunu md. 99 ve 100 uyarınca, yurt dışında yerleşik kripto varlık platformlarının Türkiye'de yerleşik kişilere yönelik faaliyetlerinin tespiti ve uygulanacak tedbirler hakkında aşağıdaki ifadelerden hangisi YANLIŞTIR?",
        "options": [
            {"key": "A", "text": "Yurt dışında yerleşik bir platformun Türkiye'de iş yeri açması halinde faaliyetlerin Türkiye'de yerleşik kişilere yönelik olduğu kabul edilir."},
            {"key": "B", "text": "Platform tarafından Türkçe internet sitesi oluşturulması durumunda faaliyet izinsiz kripto hizmet sağlayıcılığı kapsamında değerlendirilir."},
            {"key": "C", "text": "Doğrudan veya Türkiye'de yerleşik kişiler aracılığıyla tanıtım ve pazarlama yapılması faaliyetin Türkiye'ye yönelik olduğunu gösterir."},
            {"key": "D", "text": "Türkiye'de yerleşik kişilere yönelik izinsiz faaliyette bulunan internet sitelerine erişimin engellenmesine mahkeme yerine doğrudan Borsa İstanbul karar verir."},
            {"key": "E", "text": "Kurulca internet aracılığıyla yapılan yayınlarla ilgili içeriğin çıkarılması veya erişimin engellenmesi kararı uygulanmak üzere Erişim Sağlayıcıları Birliğine gönderilir."}
        ],
        "correct_answer": "D",
        "trap": "Erişimin engellenmesi kararını Borsa İstanbul değil, Sermaye Piyasası Kurulu (SPK) alır ve Erişim Sağlayıcıları Birliğine bildirir.",
        "explanation": "SPKn md. 99, 100 ve sayfa 55-56 uyarınca internet üzerinden yapılan izinsiz kripto varlık hizmet sağlayıcılığı yayınlarında içeriğin çıkarılması ve erişimin engellenmesi kararı Kurul (SPK) tarafından verilir ve uygulanmak üzere Erişim Sağlayıcıları Birliği'ne gönderilir; Borsa İstanbul'un böyle bir yetkisi yoktur."
    },
    # Q122: Teminat Yöneticisi SPKn md. 31/B
    {
        "id": "q_1001_master_122",
        "module_id": "1001",
        "number": 122,
        "source": "master",
        "topic": "Teminat Yöneticisi ve Teminat Yönetim Sözleşmesi",
        "chapter": "BÖLÜM 1: 6362 SAYILI SERMAYE PİYASASI KANUNU VE GENEL ESASLAR",
        "difficulty": "zor",
        "tags": ["SPKn md. 31/B", "Teminat Yöneticisi", "Genel Saklama", "Resen Satış"],
        "text": "6362 sayılı Sermaye Piyasası Kanunu md. 31/B uyarınca ihraç edilen sermaye piyasası araçlarına ilişkin yükümlülüklerin teminat altına alınmasında görevlendirilen 'Teminat Yöneticisi' hakkında aşağıdaki ifadelerden hangisi DOĞRUDUR?",
        "options": [
            {"key": "A", "text": "Teminata konu varlıkların mülkiyeti, teminaten genel saklama yetkisine sahip yatırım kuruluşu niteliğini haiz teminat yöneticisine devredilir veya lehine sınırlı ayni hak tesis edilir."},
            {"key": "B", "text": "Teminat yöneticisi yalnızca bir bağımsız denetim kuruluşu veya derecelendirme şirketi olabilir."},
            {"key": "C", "text": "Teminata konu varlıklar teminat yöneticisinin malvarlığına dahil sayılır ve onun vergi borçları için haczedilebilir."},
            {"key": "D", "text": "Temerrüt halinde teminat yöneticisi teminatları satabilmek için mutlaka asliye ticaret mahkemesinden onay almak ve açık artırma yapmak zorundadır."},
            {"key": "E", "text": "Teminat yönetim sözleşmesine konulacak bir madde ile teminat yöneticisinin yatırımcılara karşı her türlü hukuki sorumluluğu tamamen kaldırılabilir."}
        ],
        "correct_answer": "A",
        "trap": "Teminat yöneticisinin genel saklama yetkili yatırım kuruluşu olması şarttır ve temerrüt halinde mahkeme veya açık artırma şartı olmaksızın teminatı resen satabilir!",
        "explanation": "SPKn md. 31/B (sayfa 12-13) uyarınca teminat yöneticisi genel saklama yetkisine sahip yatırım kuruluşudur. Teminat varlıkları yöneticinin malvarlığından ayrıdır, kamu alacakları için dahi haczedilemez, iflas masasına girmez. Temerrüt halinde mahkeme onayı veya açık artırma gibi bir ön şart olmaksızın teminat yöneticisi varlıkları resen satıp yatırımcılara paylaştırır. Sorumluluğu kaldıran hükümler geçersizdir."
    },
    # Q123: Teminat Yöneticisi Cezai Sorumluluk
    {
        "id": "q_1001_master_123",
        "module_id": "1001",
        "number": 123,
        "source": "master",
        "topic": "Teminat Yöneticisinin Cezai Sorumluluğu",
        "chapter": "BÖLÜM 2: SPK'NIN GÖREV/YETKİLERİ, TEDBİRLER, SUÇLAR VE YAPTIRIMLAR",
        "difficulty": "orta",
        "tags": ["SPKn md. 31/B", "TCK md. 155/2", "Güveni Kötüye Kullanma", "Hapis Cezası"],
        "text": "6362 sayılı SPKn md. 31/B uyarınca, teminat yöneticisinin teminaten mülkiyeti kendisine devredilen varlıkları tasarruf amacı dışında kullanması halinde 5237 sayılı Türk Ceza Kanunu m. 155/2'ye göre hükmedilecek hapis cezasının alt sınırı nedir?",
        "options": [
            {"key": "A", "text": "1 yıldan az olamaz"},
            {"key": "B", "text": "2 yıldan az olamaz"},
            {"key": "C", "text": "5 yıldan az olamaz"},
            {"key": "D", "text": "8 yıldan az olamaz"},
            {"key": "E", "text": "10 yıldan az olamaz"}
        ],
        "correct_answer": "C",
        "trap": "Genel TCK 155/2 hükmündeki alt sınır 1 yıl olmasına karşın, SPKn 31/B özel hükmü gereğince ceza 5 YILDAN AZ OLAMAZ!",
        "explanation": "6362 sayılı SPKn m. 31/B'nin onuncu fıkrası (sayfa 13) uyarınca: 'Teminat yöneticisinin teminaten mülkiyeti devredilen varlıkları tasarruf amacı dışında kullanması durumunda 5237 sayılı Türk Ceza Kanunu'nun 155 inci maddesinin ikinci fıkrasına göre hükmedilecek ceza beş yıldan az olamaz.'"
    },
    # Q124: Borçlanma Aracı Sahipleri Kurulu (BİSK)
    {
        "id": "q_1001_master_124",
        "module_id": "1001",
        "number": 124,
        "source": "master",
        "topic": "Borçlanma Aracı Sahipleri Kurulu (BİSK) ve Temerrüt Esasları",
        "chapter": "BÖLÜM 1: 6362 SAYILI SERMAYE PİYASASI KANUNU VE GENEL ESASLAR",
        "difficulty": "zor",
        "tags": ["SPKn md. 31/A", "BİSK", "Karar Nisabı", "Takiplerin Durması"],
        "text": "6362 sayılı SPKn md. 31/A uyarınca Borçlanma Aracı Sahipleri Kurulu (BİSK) ve borçlanma araçlarının temerrüdü sonrasındaki hukuki süreç hakkında aşağıdaki ifadelerden hangisi YANLIŞTIR?",
        "options": [
            {"key": "A", "text": "İhraççının tedavülde bulunan borçlanma araçlarının sahipleri veya her bir tertip borçlanma aracı sahipleri ayrı bir kurul oluşturabilir."},
            {"key": "B", "text": "Kurulda karar alınabilmesi için aksi ağırlaştırılmadıkça tedavüldeki nominal bedelin asgari yarısını temsil eden borçlanma aracı sahiplerinin olumlu oyu şarttır."},
            {"key": "C", "text": "Nitelikli çoğunlukla alınacak BİSK kararları, bu kararlara olumlu oy vermeyen borçlanma aracı sahipleri için de bağlayıcıdır ve hüküm ifade eder."},
            {"key": "D", "text": "Borçlanma araçlarının temerrüdü sonrasında hüküm ve şartların değiştirilmesi halinde temerrüt nedeniyle başlatılmış tüm takipler durur, ihtiyati tedbir ve ihtiyati haciz kararları uygulanmaz."},
            {"key": "E", "text": "Borçlanma aracı sahipleri kuruluna yalnızca ihraççı ortaklığın yönetim kurulu başkanı başkanlık edebilir; kurulun temsilci atama yetkisi yoktur."}
        ],
        "correct_answer": "E",
        "trap": "SPKn m. 31/A açıkça borçlanma aracı sahiplerini temsil etmek üzere temsilci atanabileceğini hükme bağlamıştır.",
        "explanation": "SPKn md. 31/A (sayfa 21) uyarınca borçlanma aracı sahiplerini temsil etmek üzere temsilci atanabilir. İhraççı yönetim kurulu başkanının zorunlu başkanlığı gibi bir kural yoktur. Alınan nitelikli kararlar muhalif kalanları da bağlar ve temerrüt sonrası şartlar değiştiğinde tüm haciz ve icra takipleri durur."
    },
    # Q125: İdari Sorumlular İşlem Bildirim Eşiği 2026
    {
        "id": "q_1001_master_125",
        "module_id": "1001",
        "number": 125,
        "source": "master",
        "topic": "İdari Sorumlular ve Ana Ortak İşlem Bildirim Eşiği",
        "chapter": "BÖLÜM 3: ÖZEL DURUMLAR TEBLİĞİ (II-15.1), İÇSEL BİLGİLER VE KAMUYU AYDINLATMA",
        "difficulty": "orta",
        "tags": ["Özel Durumlar Tebliği II-15.1", "2026 Eşiği", "15 Milyon TL", "İdari Sorumlular"],
        "text": "Özel Durumlar Tebliği (II-15.1) uyarınca, sermayeyi temsil eden paylar ve paya dayalı araçlara ilişkin olarak idari sorumluluğu bulunan kişiler veya ihraççının ana ortağının bir takvim yılı içinde gerçekleştirdiği işlemlerin kamuya açıklanması için Kurulca 2026 yılı için belirlenen parasal eşik tutarı aşağıdakilerden hangisidir?",
        "options": [
            {"key": "A", "text": "5.000.000 TL"},
            {"key": "B", "text": "10.000.000 TL"},
            {"key": "C", "text": "15.000.000 TL"},
            {"key": "D", "text": "20.000.000 TL"},
            {"key": "E", "text": "30.000.000 TL"}
        ],
        "correct_answer": "C",
        "trap": "Eski yıllardaki 5 milyon TL veya 10 milyon TL değil; resmi Temmuz 2026 ders notundaki güncel Kurul eşiği 15.000.000 TL'dir.",
        "explanation": "Özel Durumlar Tebliği (II-15.1) md. 11 ve resmi SPL ders notu sayfa 69 uyarınca: İdari sorumluluğu bulunan kişiler ve bunlarla yakından ilişkili kişiler ya da ihraççının ana ortağının her biri hesabına yapılan işlemlerin toplam tutarı bir takvim yılı içerisinde Kurulca belirlenmiş olan (2026 yılı için 15.000.000 TL) tutara ulaşmadıkça açıklama yapılmaz; bu tutarı aşan işlemlerden itibaren sonraki tüm işlemler kamuya açıklanır."
    },
    # Q126: Sermaye Yapısı Değişiklik Bildirim Süresi ve MKK
    {
        "id": "q_1001_master_126",
        "module_id": "1001",
        "number": 126,
        "source": "master",
        "topic": "Sermaye Yapısı Değişiklik Bildirim Süresi ve MKK",
        "chapter": "BÖLÜM 3: ÖZEL DURUMLAR TEBLİĞİ (II-15.1), İÇSEL BİLGİLER VE KAMUYU AYDINLATMA",
        "difficulty": "zor",
        "tags": ["Özel Durumlar Tebliği II-15.1", "Sermaye Yapısı Eşikleri", "MKK Bildirimi", "Süre"],
        "text": "Özel Durumlar Tebliği (II-15.1) çerçevesinde, payları borsada işlem gören bir ihraççının sermaye yapısı ve oy haklarına ilişkin eşiklerin (%5, %10, %15, %20, %25, %33, %50, %67, %95) aşılması veya altına düşülmesi halinde yapılacak kamuya açıklamalara ilişkin aşağıdaki ifadelerden hangisi DOĞRUDUR?",
        "options": [
            {"key": "A", "text": "Açıklamalar en geç işlemin gerçekleştiği gün seans bitiminden önce ihraççı tarafından SPK'ya elden bildirilir."},
            {"key": "B", "text": "Açıklamalar en geç işlemin gerçekleşmesini izleyen üçüncü iş günü saat 09.00'a kadar yapılır; doğrudan pay sahipliğinde açıklama MKK tarafından yerine getirilir."},
            {"key": "C", "text": "Birlikte hareket edenler ile dolaylı pay sahipliğinde açıklama yükümlülüğü kişilere değil, doğrudan MKK'ya aittir."},
            {"key": "D", "text": "Payları borsada işlem görmeyen ortaklıklarda da aynı dokuz eşiğin tamamı (%5, %10, %15...) aynen aranır."},
            {"key": "E", "text": "Oy hakkının donduğu durumlardaki paylar söz konusu oranların ve eşiklerin hesaplanmasında dikkate alınmaz."}
        ],
        "correct_answer": "B",
        "trap": "Süre 'izleyen üçüncü iş günü saat 09.00'dur' ve doğrudan pay değişimini MKK otomatik yapar, dolaylı/birlikte hareketi ise kişi bildirir!",
        "explanation": "Özel Durumlar Tebliği II-15.1 (sayfa 70, 75) uyarınca sermaye yapısı değişiklik bildirimleri Tebliğ ekindeki form ile en geç işlemin gerçekleşmesini izleyen üçüncü iş günü saat 09.00'a kadar yapılır. Borsada işlem gören doğrudan pay sahipliği değişikliklerini MKK otomatik açıklar; dolaylı ve birlikte hareket hallerini ise ilgililer bildirir. Oy hakkı donmuş olsa dahi hesaplamada dikkate alınır."
    },
    # Q127: Kurumsal Yönetim Şirket Gruplandırması
    {
        "id": "q_1001_master_127",
        "module_id": "1001",
        "number": 127,
        "source": "master",
        "topic": "Kurumsal Yönetim Şirket Gruplandırması ve Eşik Değerler",
        "chapter": "BÖLÜM 5: KURUMSAL YÖNETİM İLKELERİ (II-17.1) VE YÖNETİM KURULU KOMİTELERİ",
        "difficulty": "orta",
        "tags": ["Kurumsal Yönetim Tebliği II-17.1", "Şirket Grupları", "Piyasa Değeri", "Yeniden Değerleme"],
        "text": "II-17.1 sayılı Kurumsal Yönetim Tebliği uyarınca payları Borsa İstanbul'da işlem gören ortaklıkların sistemik önemlerine göre ayrıldıkları gruplar ve kriterler hakkında aşağıdaki ifadelerden hangisi DOĞRUDUR?",
        "options": [
            {"key": "A", "text": "Birinci grup ortaklıklar; ortalama piyasa değeri 3 milyar TL'nin ve fiili dolaşımdaki paylarının piyasa değeri ortalaması 750 milyon TL'nin üzerinde olan ortaklıklardır; bu eşikler her yıl yeniden değerlemeye tabi tutulmaz."},
            {"key": "B", "text": "Şirket gruplandırmasında belirlenen parasal eşikler her takvim yılı başında Vergi Usul Kanunu yeniden değerleme oranında otomatik olarak güncellenir."},
            {"key": "C", "text": "İkinci grup ortaklıklar için aranan piyasa değeri eşiği en az 5 milyar TL, fiili dolaşım piyasa değeri eşiği ise en az 1 milyar TL'dir."},
            {"key": "D", "text": "Payları borsada ilk defa işlem görmeye başlayan ortaklıklar, işlem gördükleri ilk genel kurula kadar otomatikman birinci grup sayılırlar."},
            {"key": "E", "text": "Ortaklıkların dahil oldukları grupların yeniden belirlenmesi her yıl Temmuz ayında Borsa İstanbul tarafından yapılarak ilan edilir."}
        ],
        "correct_answer": "A",
        "trap": "Eşikler (3 Milyar TL / 750 Milyon TL) yeniden değerlemeye tabi TUTULMAZ ve hesaplama her yıl Ocak ayında Kurulca yapılır!",
        "explanation": "Kurumsal Yönetim Tebliği II-17.1 (sayfa 92) uyarınca: Birinci grup; ortalama piyasa değeri 3 milyar TL ve fiili dolaşım piyasa değeri 750 milyon TL üzerinde olanlardır. İkinci grup ise 1 milyar TL ve 250 milyon TL üzeridir. Bu eşikler kesinlikle yeniden değerlemeye tabi tutulmaz; hesaplama her yıl Ocak ayında SPK tarafından yapılır."
    },
    # Q128: Yatırım Fonu Portföy Sınırlamaları ve İşlem Yasakları
    {
        "id": "q_1001_master_128",
        "module_id": "1001",
        "number": 128,
        "source": "master",
        "topic": "Yatırım Fonu Portföy Sınırlamaları ve İşlem Yasakları",
        "chapter": "BÖLÜM 4: YATIRIM FONLARI VE KOLEKTİF YATIRIM KURULUŞLARI",
        "difficulty": "zor",
        "tags": ["Yatırım Fonları Tebliği III-52.1", "5/40 Kuralı", "Açığa Satış Yasağı", "Portföy Sınırlamaları"],
        "text": "III-52.1 sayılı Yatırım Fonlarına İlişkin Esaslar Tebliği uyarınca genel yatırım fonlarının portföy sınırlamaları ve yapabilecekleri işlemler hakkında aşağıdaki ifadelerden hangisi YANLIŞTIR?",
        "options": [
            {"key": "A", "text": "Fon toplam değerinin %10'undan fazlası tek bir ihraççının para ve sermaye piyasası araçlarına yatırılamaz (İTMK/VDMK hariç)."},
            {"key": "B", "text": "Fon toplam değerinin %5'inden fazla yatırım yapılan ihraççıların para ve sermaye piyasası araçlarının toplam değeri fon toplam değerinin %40'ını aşamaz."},
            {"key": "C", "text": "Fon toplam değerinin %20'sinden fazlası Kurulun finansal raporlama düzenlemeleri kapsamındaki aynı grubun sermaye piyasası araçlarına yatırılamaz."},
            {"key": "D", "text": "Tek bir bankada değerlendirilebilecek vadeli mevduat/katılma hesabı tutarı fon toplam değerinin %3'ünü aşamaz (katılım fonlarında %10)."},
            {"key": "E", "text": "Fon portföy yöneticisi piyasa koşullarına bağlı olarak fon portföyünün %15'ine kadar açığa satış veya kredili menkul kıymet işlemi yapabilir."}
        ],
        "correct_answer": "E",
        "trap": "Yatırım fonları için açığa satış ve kredili işlem yapmak KESİNLİKLE YASAKTIR; hiçbir istisnası veya oranı yoktur!",
        "explanation": "III-52.1 sayılı Fon Tebliği m. 23 ve sayfa 128 açıkça belirtir: 'Fon, açığa satış ve kredili menkul kıymet işlemi YAPAMAZ.' Dolayısıyla fonların herhangi bir oranda açığa satış veya kredili işlem yapabileceğine dair ifadeler mutlak olarak yanlıştır."
    },
    # Q129: Azami Fon Toplam Gider Oranları
    {
        "id": "q_1001_master_129",
        "module_id": "1001",
        "number": 129,
        "source": "master",
        "topic": "Fon Türleri Bazında Azami Fon Toplam Gider Oranları (FTGK Tavanı)",
        "chapter": "BÖLÜM 4: YATIRIM FONLARI VE KOLEKTİF YATIRIM KURULUŞLARI",
        "difficulty": "orta",
        "tags": ["Yatırım Fonları Tebliği III-52.1", "Fon Toplam Gider Oranı", "Gider Tavanı Tablosu"],
        "text": "III-52.1 sayılı Yatırım Fonlarına İlişkin Esaslar Tebliği'nde yer alan 'Fon Türleri Bazında Uygulanacak Azami Fon Toplam Gider Oranları' tablosuna göre, yıllık bazda en düşük ve en yüksek azami fon toplam gider tavanına sahip fon türleri hangi seçenekte doğru verilmiştir?",
        "options": [
            {"key": "A", "text": "En düşük: Hisse Senedi Şemsiye Fonu (%1,20) — En yüksek: Borçlanma Araçları Fonu (%3,65)"},
            {"key": "B", "text": "En düşük: Para Piyasası Fonları (%1,65) — En yüksek: Fon Sepeti Fonları (%4,38)"},
            {"key": "C", "text": "En düşük: Katılım Şemsiye Fonu (%1,10) — En yüksek: Garantili Fonlar (%2,85)"},
            {"key": "D", "text": "En düşük: Kıymetli Madenler Fonu (%1,65) — En yüksek: Serbest Fonlar (%5,50)"},
            {"key": "E", "text": "En düşük: Kısa Vadeli Borçlanma Fonları (%1,65) — En yüksek: Değişken Fonlar (%4,00)"}
        ],
        "correct_answer": "B",
        "trap": "Serbest fonlar gider tavanına tabi değildir; tebliğ tablosunda en düşük tavan Para Piyasası (%1,65), en yüksek tavan ise Fon Sepeti (%4,38)'dir.",
        "explanation": "Tebliğ md. 1.2.3.30 (sayfa 135) Azami Fon Toplam Gider Oranları Tablosu: Para Piyasası Fonları: Yıllık %1,65 (günlük yüzbinde 4,5) ile en düşük tavandır. Fon Sepeti Fonları: Yıllık %4,38 (günlük yüzbinde 12) ile en yüksek tavandır. (Koruma/Garantili/Kıymetli Maden/Endeks: %2,19; Kısa Vadeli Borçlanma: %2,56; Diğer Fonlar: %3,65)."
    },
    # Q130: TSPB Disiplin Komitesi Güncel Yapısı ve Soruşturma Usulü
    {
        "id": "q_1001_master_130",
        "module_id": "1001",
        "number": 130,
        "source": "master",
        "topic": "TSPB Disiplin Komitesi Güncel Yapısı ve Soruşturma Usulü",
        "chapter": "BÖLÜM 7: TSPB MESLEK KURALLARI, ETİK İLKELER, ÇIKAR ÇATIŞMALARI VE DİSİPLİN HÜKÜMLERİ",
        "difficulty": "zor",
        "tags": ["TSPB Disiplin Yönetmeliği", "Disiplin Komitesi", "7 Üye", "Soruşturma Süreçleri"],
        "text": "Türkiye Sermaye Piyasaları Birliği (TSPB) Disiplin Yönetmeliği uyarınca Disiplin Komitesi'nin üye kompozisyonu, görev süresi ve soruşturma usulüne ilişkin aşağıdaki ifadelerden hangisi DOĞRUDUR?",
        "options": [
            {"key": "A", "text": "Disiplin Komitesi 5 üyeden oluşur, üyelerin görev süresi 3 yıldır ve komite raportörlüğünü SPK Başuzmanı yürütür."},
            {"key": "B", "text": "Birlik Yönetim Kurulu'nun verdiği disiplin cezalarına karşı kararın tebliğinden itibaren 30 gün içinde doğrudan Bölge İdare Mahkemesine başvurulur."},
            {"key": "C", "text": "Disiplin soruşturmasında üyeye savunma için verilen süre 3 iş günüdür ve mazeret halinde dahi uzatılamaz."},
            {"key": "D", "text": "Disiplin Komitesi 7 üyeden oluşur (2 aracı kurum, 1 banka, 1 PYŞ, 1 borsa YO, 1 kripto varlık hizmet sağlayıcı, 1 kitle fonlama platformu); görev süresi 2 yıldır ve raportör Birlik Hukuk İşleri Müdürüdür."},
            {"key": "E", "text": "Disiplin cezasını gerektiren fiillerde soruşturmaya başlanabilmesi için fiilin işlendiği tarihten itibaren 3 yıl geçmemiş olması gerekir."}
        ],
        "correct_answer": "D",
        "trap": "Yeni düzenlemeyle Disiplin Komitesi 7 üyedir (kripto varlık ve kitle fonlama temsilcileri eklenmiştir), görev süresi 2 yıldır ve raportör Hukuk İşleri Müdürüdür.",
        "explanation": "TSPB Disiplin Yönetmeliği m. 1.3.3.2.1 ve m. 1.3.3.2.3 (sayfa 174-176) uyarınca: Disiplin Komitesi 7 üyeden oluşur (2 aracı kurum, 1 banka, 1 portföy yönetim şirketi, 1 payları borsada işlem gören yatırım ortaklığı, 1 kripto varlık hizmet sağlayıcı, 1 kitle fonlama platformu). Görev süresi 2 yıldır. Raportör Hukuk İşleri Müdürüdür. Savunma süresi 10 iş günüdür (mazeretle 20 gün). İtiraz 10 iş günü içinde SPK'ya yapılır. Soruşturma zamanaşımı fiilden itibaren 1 yıldır."
    }
]

# Append new questions to all_qs
all_qs.extend(new_questions)

# Verify 1001 count after
q1001_after = [q for q in all_qs if str(q.get('module_id', '')) == '1001']
print(f"New 1001 questions count: {len(q1001_after)}")
assert len(q1001_after) == 200, f"Expected 200, found {len(q1001_after)}"
print(f"Total all questions count: {len(all_qs)}")
assert len(all_qs) == 750, f"Expected 750, found {len(all_qs)}"

# Save to src/data/all_questions.json
with open('src/data/all_questions.json', 'w', encoding='utf-8') as f:
    json.dump(all_qs, f, ensure_ascii=False, indent=2)
print("Saved src/data/all_questions.json successfully!")

# Save to src/data/questions_master.json
with open('src/data/questions_master.json', 'w', encoding='utf-8') as f:
    json.dump(all_qs, f, ensure_ascii=False, indent=2)
print("Saved src/data/questions_master.json successfully!")

print("\n--- Answer Key Distribution of the 15 New Questions ---")
ans_counts = {}
for q in new_questions:
    a = q['correct_answer']
    ans_counts[a] = ans_counts.get(a, 0) + 1
print("Distribution:", sorted(ans_counts.items()))
print("All tasks completed successfully!")
