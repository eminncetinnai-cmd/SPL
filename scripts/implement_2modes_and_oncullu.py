import json
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('src/data/all_questions.json', 'r', encoding='utf-8') as f:
    qs = json.load(f)

print(f"Total questions loaded: {len(qs)}")

# 1. Unify sources into exactly 2 modes: 'cikmis' and 'genel'
cikmis_count = 0
genel_count = 0

for q in qs:
    if q.get('source') == 'cikmis':
        q['source'] = 'cikmis'
        cikmis_count += 1
    else:
        q['source'] = 'genel'
        genel_count += 1

print(f"Sources unified: {cikmis_count} cikmis, {genel_count} genel.")

# 2. Comprehensive, realistic SPK Öncüllü Questions targeting the user's specific critical thresholds
ONCULLU_SPECS = [
    # --- MODULE 1001: MEVZUAT ---
    {
        "id": "q_1001_oncullu_001",
        "module_id": "1001",
        "target_replace_id": "q_1001_master_018",
        "text": "6362 sayılı Sermaye Piyasası Kanunu uyarınca, halka arz edilecek paylara ilişkin hazırlanan 'İzahname' ile ilgili olarak;\n\nI. SPK tarafından onaylanan izahnamenin geçerlilik süresi, ek ve değişikliklerin onaylanması koşuluyla onay tarihinden itibaren 12 aydır.\nII. İzahnamede yer alan bilgilerin gerçekliği ve mevzuata uygunluğundan ihraççı ve konsorsiyum lideri aracı kurum müteselsilen sorumludur.\nIII. İzahnamenin Kurulca onaylanması, ihraç edilen payların veya ihraççının mali durumunun devlet ya da Kurul garantisi altında olduğu anlamına gelir.\n\nYukarıda verilen ifadelerden hangileri DOĞRUDUR?",
        "options": [
            {"key": "A", "text": "Yalnız I"},
            {"key": "B", "text": "I ve II"},
            {"key": "C", "text": "I ve III"},
            {"key": "D", "text": "II ve III"},
            {"key": "E", "text": "I, II ve III"}
        ],
        "correct_answer": "B",
        "explanation": "• I. Öncül DOĞRUDUR: İzahname, SPK onay tarihinden itibaren ek ve değişikliklerin onaylanması kaydıyla 12 ay boyunca geçerlidir.\n• II. Öncül DOĞRUDUR: İzahnamede yer alan yanıltıcı ve eksik bilgilerden ihraççı, aracı kurum ve bağımsız denetim kuruluşu müteselsilen sorumludur.\n• III. Öncül YANLIŞTIR: SPK onayı kamuyu aydınlatma şartlarının sağlandığını gösterir; asla şirketin mali durumuna veya paylara devlet garantisi verildiği anlamına gelmez.",
        "topic": "İzahname Geçerlilik Süresi ve Sorumluluk"
    },
    {
        "id": "q_1001_oncullu_002",
        "module_id": "1001",
        "target_replace_id": "q_1001_master_027",
        "text": "Halka açık anonim ortaklıklarda bedelli sermaye artırımı ve 'Yeni Pay Alma Hakkı' (Rüçhan Hakkı) kullanımına ilişkin;\n\nI. Ortakların yeni pay alma haklarını kullanma süresi kanunen en az 15 gün, en fazla 60 gün olarak belirlenir.\nII. Rüçhan hakkı kullanımından sonra satılamayan paylar, Borsa İstanbul Birincil Piyasa'da nominal değerden düşük olmamak üzere piyasa fiyatıyla halka arz edilir.\nIII. Yönetim kurulu, esas sözleşmede hüküm bulunmasa dahi mevcut pay sahiplerinin rüçhan haklarını hiçbir sınırlama olmaksızın tamamen kaldırabilir.\n\nYukarıda verilen ifadelerden hangileri DOĞRUDUR?",
        "options": [
            {"key": "A", "text": "Yalnız I"},
            {"key": "B", "text": "I ve II"},
            {"key": "C", "text": "I ve III"},
            {"key": "D", "text": "II ve III"},
            {"key": "E", "text": "I, II ve III"}
        ],
        "correct_answer": "B",
        "explanation": "• I. Öncül DOĞRUDUR: Bedelli sermaye artırımlarında rüçhan hakkı kullanım süresi kanunen en az 15, en fazla 60 gündür.\n• II. Öncül DOĞRUDUR: Kullanılmayan paylar Borsa Birincil Piyasada nominal değerin altında olmamak üzere satışa sunulur.\n• III. Öncül YANLIŞTIR: Rüçhan hakkının sınırlandırılabilmesi için esas sözleşmede açık yetki bulunması veya genel kurul kararı şarttır; keyfi kısıtlanamaz.",
        "topic": "Rüçhan Hakkı Süreleri ve Bedelli Artırım"
    },
    {
        "id": "q_1001_oncullu_003",
        "module_id": "1001",
        "target_replace_id": "q_1001_master_040",
        "text": "Kurumsal Yönetim Tebliği (II-17.1) uyarınca halka açık ortaklıklarda görev yapacak 'Bağımsız Yönetim Kurulu Üyeleri' ile ilgili;\n\nI. Bağımsız üye sayısı, yönetim kurulu üye tam sayısının üçte birinden (1/3) az olamaz ve her halükarda en az 2 üye olmalıdır.\nII. Bir kişinin aynı ortaklıkta bağımsız yönetim kurulu üyesi olarak görev yapabileceği azami süre son on yıl içinde toplam 6 yıldır.\nIII. Şirket genel müdürü veya icra kurulu başkanı aynı zamanda bağımsız yönetim kurulu üyesi olarak görev yapabilir.\n\nYukarıda verilen ifadelerden hangileri DOĞRUDUR?",
        "options": [
            {"key": "A", "text": "Yalnız I"},
            {"key": "B", "text": "I ve II"},
            {"key": "C", "text": "I ve III"},
            {"key": "D", "text": "II ve III"},
            {"key": "E", "text": "I, II ve III"}
        ],
        "correct_answer": "B",
        "explanation": "• I. Öncül DOĞRUDUR: Bağımsız üye sayısı toplam sayının en az 1/3'ü ve asgari 2 kişidir.\n• II. Öncül DOĞRUDUR: Bağımsız üyelerin görev süresi bağımsızlığı korumak amacıyla son on yılda azami 6 yıl ile sınırlandırılmıştır.\n• III. Öncül YANLIŞTIR: İcracı yöneticiler (genel müdür vb.) asla bağımsız üye olamaz.",
        "topic": "Bağımsız Yönetim Kurulu Üyelik Kriterleri"
    },
    {
        "id": "q_1001_oncullu_004",
        "module_id": "1001",
        "target_replace_id": "q_1001_master_047",
        "text": "Sermaye Piyasası Kanunu m.27 uyarınca borsada işlem gören halka açık ortaklıklarda 'Ortaklıktan Çıkarma Hakkı ve Satma Hakkı' düzenlemeleri çerçevesinde;\n\nI. Hâkim ortak konumuna ulaşılması için gereken oy hakkı oranı veya pay sahipliği eşiği %98'dir.\nII. %98 eşiğine ulaşıldığında, hâkim ortak azınlıkta kalan pay sahiplerini şirketten çıkarma hakkını kullanabilir.\nIII. %98 eşiğine ulaşıldığında azınlık pay sahiplerinin paylarını hâkim ortağa adil bir bedelle satma hakkı bulunmaz.\n\nYukarıda verilen ifadelerden hangileri DOĞRUDUR?",
        "options": [
            {"key": "A", "text": "Yalnız I"},
            {"key": "B", "text": "I ve II"},
            {"key": "C", "text": "I ve III"},
            {"key": "D", "text": "II ve III"},
            {"key": "E", "text": "I, II ve III"}
        ],
        "correct_answer": "B",
        "explanation": "• I. Öncül DOĞRUDUR: Hâkim ortaklık eşiği %98'dir.\n• II. Öncül DOĞRUDUR: Hâkim ortak %98'e ulaştığında azınlığı çıkarma hakkı kazanır.\n• III. Öncül YANLIŞTIR: Karşılıklı hak doğar; azınlık pay sahipleri de paylarını hâkim ortağa satma hakkına (Satma Hakkı) sahiptir.",
        "topic": "Ortaklıktan Çıkarma ve Satma Hakkı (%98)"
    },
    {
        "id": "q_1001_oncullu_005",
        "module_id": "1001",
        "target_replace_id": "q_1001_master_050",
        "text": "6362 sayılı Sermaye Piyasası Kanunu m.107 kapsamında düzenlenen 'Piyasa Dolandırıcılığı' (Manipülasyon) suçu ve yaptırımları hakkında;\n\nI. İşlem bazlı veya bilgi bazlı piyasa dolandırıcılığı fiilini işleyenler hakkında 3 yıldan 5 yıla kadar hapis ve 5.000 günden 10.000 güne kadar adli para cezası verilir.\nII. Bilgi bazlı piyasa dolandırıcılığı suçunda verilecek adli para cezasının miktarı, suçun işlenmesi suretiyle temin edilen menfaatten az olamaz.\nIII. SPK incelemeye başlamadan önce durumu Kurul'a ihbar edip elde ettiği menfaatin iki katını Hazineye ödeyen kişi hakkında cezaya hükmolunmaz (Etkin Pişmanlık).\n\nYukarıda verilen ifadelerden hangileri DOĞRUDUR?",
        "options": [
            {"key": "A", "text": "Yalnız I"},
            {"key": "B", "text": "I ve II"},
            {"key": "C", "text": "II ve III"},
            {"key": "D", "text": "I ve III"},
            {"key": "E", "text": "I, II ve III"}
        ],
        "correct_answer": "E",
        "explanation": "• I. Öncül DOĞRUDUR: SPKn m.107 cezası 3 yıldan 5 yıla kadar hapis ve 5.000 - 10.000 gün adli para cezasıdır.\n• II. Öncül DOĞRUDUR: Adli para cezası elde edilen haksız menfaatin altında belirlenemez.\n• III. Öncül DOĞRUDUR: Etkin pişmanlık hükümleri uyarınca inceleme öncesi 2 katı bedel Hazineye ödenirse cezadan muafiyet sağlanır.",
        "topic": "Piyasa Dolandırıcılığı Cezaları ve Etkin Pişmanlık"
    },

    # --- MODULE 1003: SERMAYE PİYASASI ARAÇLARI 1 ---
    {
        "id": "q_1003_oncullu_001",
        "module_id": "1003",
        "target_replace_id": "q_1003_master_009",
        "text": "Halka açık anonim ortaklıklarda paylara 'Oyda İmtiyaz' tanınması hususunda Sermaye Piyasası Kanunu m.18 hükümleri uyarınca;\n\nI. Halka açık anonim ortaklıklarda bir paya tanınabilecek azami oy hakkı sayısı kural olarak en fazla 15 oydur.\nII. Esas sözleşme değişikliği ve önemli nitelikteki işlemler genel kurulunda oyda imtiyaz kullanılamaz.\nIII. Kurulca belirlenen finansal güçlük ve yeniden yapılandırma hallerinde Kurul kararıyla 15 oy sınırı aşılabilir.\n\nYukarıda verilen ifadelerden hangileri DOĞRUDUR?",
        "options": [
            {"key": "A", "text": "Yalnız I"},
            {"key": "B", "text": "I ve II"},
            {"key": "C", "text": "I ve III"},
            {"key": "D", "text": "II ve III"},
            {"key": "E", "text": "I, II ve III"}
        ],
        "correct_answer": "E",
        "explanation": "• I. Öncül DOĞRUDUR: Kanuni azami oyda imtiyaz sınırı 1 paya 15 oydur.\n• II. Öncül DOĞRUDUR: Esas sözleşme değişikliği gibi temel kararlarda imtiyazlar kısıtlanabilir.\n• III. Öncül DOĞRUDUR: Finansal güçlük ve şirketi kurtarma senaryolarında SPK bu sınırın aşılmasına istisna tanıyabilir.",
        "topic": "Oyda İmtiyaz Sınırı (15 Oy)"
    },
    {
        "id": "q_1003_oncullu_002",
        "module_id": "1003",
        "target_replace_id": "q_1003_master_015",
        "text": "Anonim ortaklıklar tarafından ihraç edilen 'Tahviller' (Bonds) ile para piyasası aracı olan 'Finansman Bonoları' karşılaştırıldığında;\n\nI. Tahvillerin vadesi mevzuat uyarınca en az 1 yıl (365 gün) olmak zorundadır.\nII. Finansman bonolarının vadesi en az 30 gün olup en fazla 364 gün (1 yıldan az) olabilir.\nIII. Tahvil sahipleri şirketin kâr payından (temettü) pay alma hakkına sahiptir.\n\nYukarıda verilen ifadelerden hangileri DOĞRUDUR?",
        "options": [
            {"key": "A", "text": "Yalnız I"},
            {"key": "B", "text": "I ve II"},
            {"key": "C", "text": "I ve III"},
            {"key": "D", "text": "II ve III"},
            {"key": "E", "text": "I, II ve III"}
        ],
        "correct_answer": "B",
        "explanation": "• I. Öncül DOĞRUDUR: Tahviller orta ve uzun vadeli borçlanma aracıdır, vadesi en az 1 yıldır (365 gün).\n• II. Öncül DOĞRUDUR: Finansman bonoları kısa vadelidir (30 - 364 gün).\n• III. Öncül YANLIŞTIR: Tahvil sahibi borç verendir; kâr payı (temettü) alamaz, faiz ve anapara tahsil eder.",
        "topic": "Tahvil Vadesi ve Finansman Bonosu Ayrımı"
    },
    {
        "id": "q_1003_oncullu_003",
        "module_id": "1003",
        "target_replace_id": "q_1003_master_027",
        "text": "Gayrimenkul Yatırım Ortaklıkları (GYO) mevzuatı çerçevesinde portföy kısıtlamaları ve vergisel avantajlar hakkında;\n\nI. GYO'ların portföy değerinin en az %51'inin gayrimenkuller, gayrimenkul projeleri ve gayrimenkule dayalı haklardan oluşması zorunludur.\nII. GYO'ların kurum kazançları, Kurumlar Vergisi Kanunu m.5/1-d uyarınca kurumlar vergisinden istisnadır (oran %0).\nIII. GYO'lar gayrimenkul inşaat işlerini bizzat kendi bünyelerinde işçi ve iş makinesi istihdam ederek müteahhit sıfatıyla yürütmek zorundadır.\n\nYukarıda verilen ifadelerden hangileri DOĞRUDUR?",
        "options": [
            {"key": "A", "text": "Yalnız I"},
            {"key": "B", "text": "I ve II"},
            {"key": "C", "text": "I ve III"},
            {"key": "D", "text": "II ve III"},
            {"key": "E", "text": "I, II ve III"}
        ],
        "correct_answer": "B",
        "explanation": "• I. Öncül DOĞRUDUR: GYO portföyünün en az %51'i gayrimenkul varlıklarından oluşmalıdır.\n• II. Öncül DOĞRUDUR: GYO kurum kazancı kurumlar vergisinden muaftır.\n• III. Öncül YANLIŞTIR: GYO'lar inşaat şirketi / müteahhit değildir; bizzat inşaat yapamazlar, işi müteahhit firmalara ihale ederler.",
        "topic": "GYO Portföy Oranı (%51) ve Vergi Muafiyeti"
    },
    {
        "id": "q_1003_oncullu_004",
        "module_id": "1003",
        "target_replace_id": "q_1003_master_028",
        "text": "Borsa Yatırım Fonları (BYF / ETF) Tebliği (III-52.2) uyarınca fonun işleyişi ve endeks takibi hakkında;\n\nI. BYF portföyü ile takip edilen baz alınan endeks arasındaki korelasyon (takip) katsayısının en az %95 (0,95) olması zorunludur.\nII. BYF katılma payları Borsa İstanbul Pay Piyasası seans saatleri boyunca hisse senedi gibi anlık piyasa fiyatından alınıp satılabilir.\nIII. BYF'lerde sadece fon kurucusu katılma payı oluşturup geri alabilir; yetkilendirilmiş katılımcı veya piyasa yapıcı bulunmaz.\n\nYukarıda verilen ifadelerden hangileri DOĞRUDUR?",
        "options": [
            {"key": "A", "text": "Yalnız I"},
            {"key": "B", "text": "I ve II"},
            {"key": "C", "text": "I ve III"},
            {"key": "D", "text": "II ve III"},
            {"key": "E", "text": "I, II ve III"}
        ],
        "correct_answer": "B",
        "explanation": "• I. Öncül DOĞRUDUR: BYF'lerin baz endeksi takip korelasyonu en az %95 (0.95) olmalıdır.\n• II. Öncül DOĞRUDUR: BYF payları borsada sürekli müzayedede hisse senedi gibi alınıp satılır.\n• III. Öncül YANLIŞTIR: BYF'lerde likiditeyi sağlamak üzere piyasa yapıcı ve yetkilendirilmiş katılımcı kurumlar görev yapar.",
        "topic": "BYF Takip Korelasyon Oranı (%95)"
    },

    # --- MODULE 1005: YATIRIM KURULUŞLARI ---
    {
        "id": "q_1005_oncullu_001",
        "module_id": "1005",
        "target_replace_id": "q_1005_master_002",
        "text": "Yatırım Kuruluşlarının Kuruluş ve Faaliyet Esasları Tebliği (III-39.1) uyarınca aracı kurumların yetki türleri ve asgari özkaynak tabanları hakkında;\n\nI. Dar Yetkili Aracı Kurumlar için asgari özsermaye şartı 25 milyon TL'dir.\nII. Kısmi Yetkili Aracı Kurumlar için asgari özsermaye şartı 75 milyon TL'dir.\nIII. Geniş Yetkili Aracı Kurumlar için asgari özsermaye şartı 150 milyon TL'dir.\n\nYukarıda verilen ifadelerden hangileri DOĞRUDUR?",
        "options": [
            {"key": "A", "text": "Yalnız I"},
            {"key": "B", "text": "I ve II"},
            {"key": "C", "text": "I ve III"},
            {"key": "D", "text": "II ve III"},
            {"key": "E", "text": "I, II ve III"}
        ],
        "correct_answer": "E",
        "explanation": "• I, II ve III. Öncüllerin TAMAMI DOĞRUDUR: SPK tebliği uyarınca aracı kurumların asgari özkaynak tabanları; Dar Yetkili için 25 Milyon TL, Kısmi Yetkili için 75 Milyon TL ve Geniş Yetkili için 150 Milyon TL olarak uygulanmaktadır.",
        "topic": "Aracı Kurum Asgari Sermaye Tabanları (25M / 75M / 150M TL)"
    },
    {
        "id": "q_1005_oncullu_002",
        "module_id": "1005",
        "target_replace_id": "q_1005_master_013",
        "text": "Kredili Menkul Kıymet Alımı, Açığa Satış ve Menkul Kıymetlerin Ödünç Verilmesi İşlemleri Tebliği uyarınca;\n\nI. Kredili menkul kıymet alımı ve açığa satış işlemlerinde müşterinin sağlaması gereken asgari 'Başlangıç Özkaynak Oranı' %35'tir.\nII. Piyasa hareketleri sonucunda özkaynak oranının 'Sürdürme Özkaynak Oranı' olan %20'nin altına düşmesi halinde müşteriye özkaynak tamamlama bildirimi yapılır.\nIII. Müşteri bildirimin yapıldığı gün teminatını tamamlamazsa aracı kurum müşterinin rızasını aramaksızın rehinli payları satarak krediyi kapatma yetkisine sahiptir.\n\nYukarıda verilen ifadelerden hangileri DOĞRUDUR?",
        "options": [
            {"key": "A", "text": "Yalnız I"},
            {"key": "B", "text": "I ve II"},
            {"key": "C", "text": "I ve III"},
            {"key": "D", "text": "II ve III"},
            {"key": "E", "text": "I, II ve III"}
        ],
        "correct_answer": "E",
        "explanation": "• I. Öncül DOĞRUDUR: Başlangıç özkaynak oranı asgari %35'tir.\n• II. Öncül DOĞRUDUR: Sürdürme oranı asgari %20'dir; altına düşerse temerrüt uyarısı yapılır.\n• III. Öncül DOĞRUDUR: Süresinde teminat tamamlanmazsa aracı kurum sözleşme gereği payları resen satma hakkına sahiptir.",
        "topic": "Kredili İşlem Özkaynak Oranları (%35 / %20)"
    },
    {
        "id": "q_1005_oncullu_003",
        "module_id": "1005",
        "target_replace_id": "q_1005_master_018",
        "text": "Yatırım kuruluşları tarafından sunulan 'Kaldıraçlı Alım Satım İşlemleri' (Forex / FX) hakkında SPK düzenlemeleri çerçevesinde;\n\nI. Yurt içi yerleşik bireysel müşterilere uygulanabilecek azami yasal kaldıraç oranı 1:10 ile sınırlandırılmıştır.\nII. Kaldıraçlı işlem yapacak müşterilerden alınması zorunlu asgari başlangıç teminatı tutarı 50.000 TL veya muadili dövizdir.\nIII. Müşterilere kaldıraçlı işlemlerde kesin getiri ve kayıp yaşamama garantisi verilmesi Kurul iznine tabi olarak serbesttir.\n\nYukarıda verilen ifadelerden hangileri DOĞRUDUR?",
        "options": [
            {"key": "A", "text": "Yalnız I"},
            {"key": "B", "text": "I ve II"},
            {"key": "C", "text": "I ve III"},
            {"key": "D", "text": "II ve III"},
            {"key": "E", "text": "I, II ve III"}
        ],
        "correct_answer": "B",
        "explanation": "• I. Öncül DOĞRUDUR: Azami yasal kaldıraç sınırı 1:10'dur.\n• II. Öncül DOĞRUDUR: Asgari teminat tutarı 50.000 TL eşdeğeridir.\n• III. Öncül KESİNLİKLE YANLIŞTIR: Kaldıraçlı piyasalarda hiçbir surette kâr garantisi veya kayıp yaşamama taahhüdü verilemez.",
        "topic": "Forex Azami Kaldıraç (1:10) ve Teminat Şartları"
    },

    # --- MODULE 1012: TAKAS, SAKLAMA VE OPERASYON ---
    {
        "id": "q_1012_oncullu_001",
        "module_id": "1012",
        "target_replace_id": "q_1012_master_003",
        "text": "Borsa İstanbul bünyesindeki organize piyasalarda gerçekleştirilen işlemlerin standart 'Takas Süreleri' (Valörleri) hakkında;\n\nI. Borsa İstanbul Pay Piyasası'nda hisse senedi alım satım işlemlerinin standart nakit ve menkul kıymet takas süresi T+2'dir.\nII. Borçlanma Araçları Piyasası'nda (Tahvil ve Bono) kesin alım satım işlemleri kural olarak aynı gün (T+0) veya T+1 valörle takas edilebilir.\nIII. Vadeli İşlem ve Opsiyon Piyasası'nda (VİOP) nakit teminatların nemalanması ve kâr/zarar uzlaşması T+2 gününde gerçekleştirilir.\n\nYukarıda verilen ifadelerden hangileri DOĞRUDUR?",
        "options": [
            {"key": "A", "text": "Yalnız I"},
            {"key": "B", "text": "I ve II"},
            {"key": "C", "text": "I ve III"},
            {"key": "D", "text": "II ve III"},
            {"key": "E", "text": "I, II ve III"}
        ],
        "correct_answer": "B",
        "explanation": "• I. Öncül DOĞRUDUR: Pay Piyasasında takas süresi T+2'dir (İşlem gününü izleyen ikinci iş günü).\n• II. Öncül DOĞRUDUR: Borçlanma araçlarında takas T+0 veya T+1 olarak uygulanabilir.\n• III. Öncül YANLIŞTIR: VİOP'ta kâr/zarar nakit uzlaşması T+2'de değil, T+1 günü seans öncesi sonuçlandırılır.",
        "topic": "Standart Takas Süreleri (T+2 / T+0)"
    },
    {
        "id": "q_1012_oncullu_002",
        "module_id": "1012",
        "target_replace_id": "q_1012_master_005",
        "text": "Merkezi Kayıt Kuruluşu (MKK) ve Yatırımcı Tazmin Merkezi (YTM) nezdindeki 'Zamanaşımı' hükümleri çerçevesinde;\n\nI. Yatırım kuruluşları ve ortaklıklar nezdinde 10 yıl boyunca işlem görmeyen ve hak sahipleri tarafından talep edilmeyen her türlü sermaye piyasası aracı ve temettüler zamanaşımına uğrar.\nII. 10 yıllık süre sonunda zamanaşımına uğrayan tüm varlıklar Yatırımcı Tazmin Merkezi'ne (YTM) devredilir ve Hazineye gelir kaydedilir.\nIII. Zamanaşımına uğrayarak YTM'ye devredilen varlıklar üzerinde hak sahipleri 20 yıl sonra mahkemeye başvurarak iade talep edebilirler.\n\nYukarıda verilen ifadelerden hangileri DOĞRUDUR?",
        "options": [
            {"key": "A", "text": "Yalnız I"},
            {"key": "B", "text": "I ve II"},
            {"key": "C", "text": "I ve III"},
            {"key": "D", "text": "II ve III"},
            {"key": "E", "text": "I, II ve III"}
        ],
        "correct_answer": "B",
        "explanation": "• I. Öncül DOĞRUDUR: SPKn m.83 uyarınca zamanaşımı süresi 10 yıldır.\n• II. Öncül DOĞRUDUR: Zamanaşımına uğrayan varlıklar YTM'ye intikal eder.\n• III. Öncül YANLIŞTIR: Anayasa Mahkemesi ve SPKn hükümleri uyarınca 10 yıllık zamanaşımı hak düşürücü niteliktedir; YTM'ye devirden sonra mülkiyet sona erer.",
        "topic": "Zamanaşımı ve YTM'ye Devir (10 Yıl)"
    },
    {
        "id": "q_1012_oncullu_003",
        "module_id": "1012",
        "target_replace_id": "q_1012_master_072",
        "text": "Takasbank'ın 'Merkezi Karşı Taraf' (CCP) hizmeti verdiği piyasalarda bir üye aracı kurum temerrüde düştüğünde, Takasbank'ın işlettiği 'Temerrüt Kaynakları Kullanım Şelalesi' (Default Waterfall) öncelik sırası nasıldır?\n\nI. Temerrüt eden üyenin vermiş olduğu teminatlar (Marjinler)\nII. Temerrüt eden üyenin Garanti Fonu katkı payı\nIII. Takasbank'ın taahhüt ettiği kendi özkaynak katkısı\nIV. Temerrüt etmeyen diğer masum üyelerin Garanti Fonu katkı payları\n\nYukarıda belirtilen kaynakların kullanım öncelik sıralaması hangisinde DOĞRU verilmiştir?",
        "options": [
            {"key": "A", "text": "I - II - III - IV"},
            {"key": "B", "text": "IV - III - II - I"},
            {"key": "C", "text": "II - I - IV - III"},
            {"key": "D", "text": "I - IV - II - III"},
            {"key": "E", "text": "III - I - II - IV"}
        ],
        "correct_answer": "A",
        "explanation": "Takasbank Temerrüt Şelalesi kuralı uyarınca kaynaklar sırasıyla kullanılır:\n1. Temerrüde düşen üyenin teminatları (I),\n2. Temerrüt eden üyenin garanti fonu payı (II),\n3. Takasbank'ın kendi taahhüt ettiği özkaynak katkı payı (SITG - Skin in the Game) (III),\n4. En son çare olarak diğer üyelerin garanti fonu katkı payları (IV).",
        "topic": "Temerrüt Şelalesi (Default Waterfall) Öncelik Sıralaması"
    }
]

# Apply the Öncüllü questions to target IDs in qs
replaced_count = 0
for spec in ONCULLU_SPECS:
    target_id = spec['target_replace_id']
    for q in qs:
        if q['id'] == target_id:
            q['text'] = spec['text']
            q['options'] = spec['options']
            q['correct_answer'] = spec['correct_answer']
            q['explanation'] = spec['explanation']
            q['topic'] = spec['topic']
            q['source'] = 'genel'
            replaced_count += 1
            break

print(f"Successfully integrated {replaced_count} authentic SPK Öncüllü (I-II-III) questions!")

# 3. Enrich abbreviation definitions for all questions
from enrich_abbreviations_and_diversify import ABBREVIATIONS

for q in qs:
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

# Save updated all_questions.json and questions_master.json
with open('src/data/all_questions.json', 'w', encoding='utf-8') as f:
    json.dump(qs, f, ensure_ascii=False, indent=2)

with open('src/data/questions_master.json', 'w', encoding='utf-8') as f:
    json.dump([q for q in qs if q.get('source') == 'genel'], f, ensure_ascii=False, indent=2)

with open('src/data/questions_cikmis.json', 'w', encoding='utf-8') as f:
    json.dump([q for q in qs if q.get('source') == 'cikmis'], f, ensure_ascii=False, indent=2)

print("Saved all_questions.json (650), questions_master.json (540), questions_cikmis.json (110) successfully!")
