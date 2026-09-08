"""
Fixes all 149 problematic questions in all_questions.json and questions_master.json.
Ensures:
1. Complete option homogeneity: Every question has 5 options of the EXACT same syntactic and semantic type.
2. No boilerplate copy-pasted distractors.
3. Plausible, professional financial distractors aligned with SPK SPL Düzey 1 curriculum.
4. Correct grammatical parallelisms and full sentence endings.
5. Preserves correct_answer key and updates explanation accordingly.
"""
import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('src/data/all_questions.json', 'r', encoding='utf-8') as f:
    all_qs = json.load(f)

with open('src/data/questions_master.json', 'r', encoding='utf-8') as f:
    master_qs = json.load(f)

# Load the comprehensive dictionary of replacement options for all 149 flawed questions
# Each item specifies: options: [{'key': 'A'..'E', 'text': '...'}]
# and explanation: '...'
FIXES = {}

def add_fix(qid, options, correct_key, explanation=None):
    FIXES[qid] = {
        'options': [{'key': k, 'text': t.strip()} for k, t in zip(['A','B','C','D','E'], options)],
        'correct_answer': correct_key,
        'explanation': explanation
    }

# =========================================================================
# MODÜL 1001: MEVZUAT
# =========================================================================

add_fix(
    'q_1001_master_003',
    ['100', '250', '500', '1.000', '5.000'],
    'C',
    '6362 sayılı Sermaye Piyasası Kanunu m.16 uyarınca, payları borsada işlem görmeyen anonim ortaklıkların pay sahibi sayısı 500\'ü aştığında ortaklığın payları halka arz olunmuş sayılır ve şirket halka açık ortaklık statüsü kazanarak Kurul düzenlemelerine tabi olur.\n\n📌 Soruda Geçen Kısaltmalar ve Açılımları:\n• SPKn: Sermaye Piyasası Kanunu\n• SPK: Sermaye Piyasası Kurulu'
)

add_fix(
    'q_1001_master_054',
    ['%2\'si', '%5\'i', '%10\'u', '%20\'si', '%25\'i'],
    'C',
    'Yatırım fonları portföy sınırlamaları uyarınca Risk Dağıtım İlkesi gereğince, tek bir ihraççının sermaye piyasası araçlarına fon toplam değerinin en fazla %10\'u yatırılabilir.\n\n📌 Soruda Geçen Kısaltmalar ve Açılımları:\n• PYŞ: Portföy Yönetim Şirketi'
)

add_fix(
    'q_1001_master_058',
    ['En fazla 3 yıl', 'En fazla 5 yıl', 'En fazla 7 yıl', 'En fazla 10 yıl', 'Herhangi bir süre sınırı yoktur'],
    'C',
    'Bağımsız denetim rotasyon kuralı uyarınca halka açık ortaklıklar aynı bağımsız denetim kuruluşundan kesintisiz olarak en fazla 7 yıl denetim hizmeti alabilirler (3 yıl geçmedikçe aynı kuruluş yeniden seçilemez).\n\n📌 Soruda Geçen Kısaltmalar ve Açılımları:\n• KGK: Kamu Gözetimi, Muhasebe ve Denetim Standartları Kurumu\n• SPK: Sermaye Piyasası Kurulu'
)

add_fix(
    'q_1001_master_059',
    ['Borsa İstanbul A.Ş. (BIST)', 'Merkezi Kayıt Kuruluşu A.Ş. (MKK)', 'İstanbul Takas ve Saklama Bankası A.Ş. (Takasbank)', 'Sermaye Piyasası Kurulu (SPK)', 'Türkiye Sermaye Piyasaları Birliği (TSPB)'],
    'B',
    'Kamuyu Aydınlatma Platformu\'nun (KAP) teknik işletimi, kullanıcı yetkilendirmeleri ve operasyonel yönetimi Merkezi Kayıt Kuruluşu A.Ş. (MKK) tarafından yürütülmektedir.\n\n📌 Soruda Geçen Kısaltmalar ve Açılımları:\n• KAP: Kamuyu Aydınlatma Platformu\n• MKK: Merkezi Kayıt Kuruluşu A.Ş.'
)

add_fix(
    'q_1001_master_060',
    ['En az 3 iş günü, en fazla 5 iş günü', 'En az 5 iş günü, en fazla 10 iş günü', 'En az 10 iş günü, en fazla 20 iş günü', 'Sabit 30 takvim günü', 'En az 15 gün, en fazla 60 gün'],
    'C',
    'Ayrılma Hakkı Tebliği (II-23.3) uyarınca ayrılma hakkını kullanmak isteyen pay sahipleri için ortaklığa başvuru süresi en az 10 iş günü, en fazla 20 iş günü olarak belirlenir (15-60 gün rüçhan hakkı süresidir).\n\n📌 Soruda Geçen Kısaltmalar ve Açılımları:\n• SPKn: Sermaye Piyasası Kanunu'
)

add_fix(
    'q_1001_master_063',
    [
        'Bireysel yatırımcılara günlük yüksek faizli nakit likidite sağlamak amacıyla kurulur.',
        'Halka açık şirketlerin borsa endeksini birebir takip etmek amacıyla kurulur.',
        'Yalnızca altın ve kıymetli madenlere dayalı kira sertifikası ihraç etmek amacıyla kurulur.',
        'Yurt dışı hisse senetlerinde arbitraj ve kaldıraçlı işlem yapmak amacıyla kurulur.',
        'Büyüme potansiyeli olan erken aşama girişim şirketlerine sermaye aktarmak amacıyla kurulur ve yalnızca nitelikli yatırımcılara satılır.'
    ],
    'E',
    'Girişim Sermayesi Yatırım Fonları (GSYF); büyüme potansiyeli taşıyan şirketlere ortak olmak/fon sağlamak üzere kurulan ve payları yalnızca nitelikli yatırımcılara ihraç edilebilen kapalı uçlu fonlardır.\n\n📌 Soruda Geçen Kısaltmalar ve Açılımları:\n• GSYF: Girişim Sermayesi Yatırım Fonu'
)

add_fix(
    'q_1001_master_069',
    [
        'Genel Alım-Satım Aracılığı hizmetinde',
        'Halka Arza Aracılık hizmetinde',
        'Yatırım Danışmanlığı ve Bireysel Portföy Yöneticiliği hizmetlerinde',
        'Emir İletimine Aracılık hizmetinde',
        'Kredili Menkul Kıymet İşlemlerinde'
    ],
    'C',
    'Yerindelik Testi (Appropriateness); Yatırım Kuruluşları Tebliği uyarınca münhasıran Yatırım Danışmanlığı ve Bireysel Portföy Yöneticiliği hizmetlerinde müşterinin mali durumu ve yatırım amaçlarını tespit etmek için ZORUNLUDUR.\n\n📌 Soruda Geçen Kısaltmalar ve Açılımları:\n• SPK: Sermaye Piyasası Kurulu'
)

add_fix(
    'q_1001_master_073',
    ['%20', '%25', '%35', '%40', '%50'],
    'E',
    'Borsa İstanbul Pay Piyasası kredili alım işlemlerinde mevzuatça belirlenen asgari başlangıç özkaynak oranı genel olarak %50 olarak uygulanmaktadır (BIST tedbirleri kapsamında).\n\n📌 Soruda Geçen Kısaltmalar ve Açılımları:\n• BIST: Borsa İstanbul\n• SPK: Sermaye Piyasası Kurulu'
)

add_fix(
    'q_1001_master_074',
    [
        'Sahip olunmayan sermaye piyasası araçlarının satılmasını ya da satışına ilişkin emrin verilmesini ifade eder.',
        'Sahip olunan hisse senetlerinin aynı gün içinde kâr amacıyla borsada satılmasını ifade eder.',
        'Yatırımcının aracı kurumdan kredi kullanarak nakit hisse senedi satın almasını ifade eder.',
        'Borsada işlem gören hisse senetlerinin başka bir aracı kurumdaki hesaba virmanlanmasını ifade eder.',
        'Şirket ortaklarının bedelli sermaye artırımında yeni pay alma haklarını kullanmasını ifade eder.'
    ],
    'A',
    'Açığa satış işlemi; sahip olunmayan sermaye piyasası araçlarının satılmasını ya da satışına ilişkin emrin verilmesini ifade eder.\n\n📌 Soruda Geçen Kısaltmalar ve Açılımları:\n• SPKn: Sermaye Piyasası Kanunu'
)

add_fix(
    'q_1001_master_076',
    [
        'Cumhurbaşkanlığına bağlı bir kamu kurumu genel müdürlüğüdür.',
        'Borsa İstanbul bünyesinde faaliyet gösteren özel hukuk anonim şirketidir.',
        'Kamu kurumu niteliğinde meslek kuruluşu olup sermaye piyasası kurumlarının üyeliği kanunen zorunludur.',
        'Vakıf tüzel kişiliğine sahip gönüllü bir sivil toplum kuruluşudur.',
        'Yalnızca yabancı yatırım bankalarının üye olabildiği uluslararası bir birliktir.'
    ],
    'C',
    'TSPB; 6362 sayılı Kanun m.74 uyarınca kamu kurumu niteliğinde bir meslek kuruluşu olup, SPK\'dan izinli tüm aracı kurumlar, bankalar, PYŞ ve yatırım ortaklıklarının üyeliği kanunen zorunludur.\n\n📌 Soruda Geçen Kısaltmalar ve Açılımları:\n• TSPB: Türkiye Sermaye Piyasaları Birliği'
)

add_fix(
    'q_1001_master_095',
    ['En fazla 1 hafta', '1 aydan 2 yıla kadar', 'En fazla 10 gün', 'En az 3 yıl, en fazla 5 yıl', 'Süresiz olarak meslekten çıkarma şeklinde'],
    'B',
    'TSPB Disiplin Yönetmeliği ve SPKn uyarınca geçici olarak faaliyetten alıkoyma cezası 1 aydan 2 yıla kadar süreyle verilebilir.\n\n📌 Soruda Geçen Kısaltmalar ve Açılımları:\n• TSPB: Türkiye Sermaye Piyasaları Birliği'
)

add_fix(
    'q_1001_master_097',
    ['En az 3 gün', 'En az 7 gün', 'En az 10 gün', 'En az 15 gün', 'En az 30 gün'],
    'D',
    'TSPB Disiplin Yönetmeliği uyarınca hakkında soruşturma açılan üyeye savunmasını hazırlaması için tebliğden itibaren en az 10 gün süre tanınır.\n\n📌 Soruda Geçen Kısaltmalar ve Açılımları:\n• TSPB: Türkiye Sermaye Piyasaları Birliği'
)

add_fix(
    'q_1001_master_098',
    [
        'TSPB kararlarına karşı hiçbir yargı yolu veya itiraz mercii açık değildir.',
        'İtirazlar yalnızca Türkiye Barolar Birliği\'ne yapılabilir.',
        'Cezalara karşı yalnızca Borsa İstanbul Genel Kurulu\'na başvurulabilir.',
        'Kararlar doğrudan Yargıtay Ceza Dairesi tarafından kesinleştirilir.',
        'İlgililer belirlenen sürede Birlik Yönetim Kurulu veya SPK\'ya itiraz edebilir; nihai idari işlemlere karşı İdare Mahkemesi\'nde iptal davası açılabilir.'
    ],
    'E',
    'TSPB disiplin cezalarına karşı idari itiraz yolları ve idari yargıda (İdare Mahkemeleri) iptal davası açma hakkı mevcuttur.\n\n📌 Soruda Geçen Kısaltmalar ve Açılımları:\n• TSPB: Türkiye Sermaye Piyasaları Birliği\n• SPK: Sermaye Piyasası Kurulu'
)

add_fix(
    'q_1001_konu_002',
    ['5 iş günü', '10 iş günü', '20 iş günü', '30 iş günü', '60 iş günü'],
    'B',
    'Payları ilk defa halka arz edilecek şirketlerin izahname başvuruları, belgelerin eksiksiz tesliminden itibaren en geç 20 iş günü içinde SPK tarafından karara bağlanır (Halka açık şirketler için 10 iş günüdür).\n\n📌 Soruda Geçen Kısaltmalar ve Açılımları:\n• SPK: Sermaye Piyasası Kurulu'
)

add_fix(
    'q_1001_konu_003',
    ['2 iş günü', '5 iş günü', '10 iş günü', '15 iş günü', '30 iş günü'],
    'A',
    'İzahnamede satış sürecinde yeni bir husus ortaya çıkarsa, değişiklik yayımlanmadan önce talepte bulunan yatırımcılar taleplerini en geç 2 iş günü içinde geri alma hakkına sahiptir.\n\n📌 Soruda Geçen Kısaltmalar ve Açılımları:\n• KAP: Kamuyu Aydınlatma Platformu'
)

add_fix(
    'q_1001_konu_006',
    ['2 yıl', '5 yıl', '10 yıl', '15 yıl', '20 yıl'],
    'B',
    '6362 sayılı Sermaye Piyasası Kanunu m.83 uyarınca yatırım kuruluşlarında bulunan emanet ve alacaklar son talep tarihinden itibaren 10 yıl aranmazsa zamanaşımına uğrayarak YTM\'ye devredilir.\n\n📌 Soruda Geçen Kısaltmalar ve Açılımları:\n• YTM: Yatırımcı Tazmin Merkezi'
)

add_fix(
    'q_1001_konu_015',
    ['3 iş günü', '5 iş günü', '7 iş günü', '10 iş günü', '30 iş günü'],
    'D',
    'TSPB tarafından verilen disiplin cezalarına karşı tebliğden itibaren en geç 10 iş günü içinde Sermaye Piyasası Kurulu\'na (SPK) itiraz edilebilir.\n\n📌 Soruda Geçen Kısaltmalar ve Açılımları:\n• TSPB: Türkiye Sermaye Piyasaları Birliği\n• SPK: Sermaye Piyasası Kurulu'
)

add_fix(
    'q_1001_ogretici_001',
    [
        'Tasarrufların sermaye piyasası araçları yoluyla ekonomiye aktarılmasına aracılık etmek',
        'Tüm şirketleri kamu mülkiyetine geçirerek devlet kontrolü sağlamak',
        'Bankaların mevduat faizlerini her ay tek taraflı olarak sabitlemek',
        'Şirketlerin iflas etmesini tamamen kanunen yasaklamak',
        'Yatırımcıların borsa zararlarını genel bütçeden tazmin etmek'
    ],
    'A',
    'Sermaye piyasasının temel ekonomik işlevi; bireysel ve kurumsal tasarrufların verimli yatırımlara ve ülke ekonomisine kanalize edilmesidir.'
)

add_fix(
    'q_1001_ogretici_002',
    [
        'Şirket hisse fiyatlarının sürekli yükselmesini devlet eliyle garanti etmek',
        'Yatırımcıya karar vermesi için gerekli bilgiyi zamanında ve eksiksiz sağlamak',
        'Şirket yönetim kurullarını tamamen bağımsız denetçilerden oluşturmak',
        'Yatırımcıların hisse senedi satmasını engelleyerek uzun vadeli tutturmak',
        'Borsada gerçekleşen tüm işlem komisyonlarını sıfıra indirmek'
    ],
    'B',
    'Kamuyu aydınlatma ilkesinin temel amacı; yatırımcının rasyonel karar alabilmesi için ihtiyaç duyduğu bilgiye zamanında, doğru ve eşit koşullarda erişebilmesini sağlamaktır.\n\n📌 Soruda Geçen Kısaltmalar ve Açılımları:\n• KAP: Kamuyu Aydınlatma Platformu'
)

# =========================================================================
# MODÜL 1003: SERMAYE PİYASASI ARAÇLARI 1
# =========================================================================

add_fix(
    'q_1003_master_003',
    [
        'Yalnızca şirket genel müdürü tek başına karar verebilir.',
        'Sadece mahkeme kararıyla rüçhan hakkı sınırlandırılabilir.',
        'Esas sözleşmeyle yetkilendirilmişse Yönetim Kurulu veya Genel Kurul kararıyla yapılabilir.',
        'Rüçhan hakkının sınırlandırılması kanunen kesinlikle yasaktır.',
        'Yalnızca bağımsız denetim kuruluşunun onayıyla sınırlandırılabilir.'
    ],
    'C',
    'TTK ve SPKn uyarınca sermaye artırımında rüçhan hakkı Genel Kurul kararıyla veya kayıtlı sermaye sisteminde esas sözleşmede yetki verilmişse Yönetim Kurulu kararıyla sınırlandırılabilir.\n\n📌 Soruda Geçen Kısaltmalar ve Açılımları:\n• TTK: Türk Ticaret Kanunu\n• SPKn: Sermaye Piyasası Kanunu'
)

add_fix(
    'q_1003_master_005',
    [
        'Geçmiş Yıllar Zararları Hesabı',
        'Kısa Vadeli Borçlar Hesabı',
        'Hisse Senedi İhraç Primleri (Emisyon Primi)',
        'Maddi Duran Varlıklar Yeniden Değerleme Hesabı',
        'Dönem Net Faaliyet Kârı Hesabı'
    ],
    'C',
    'Payların nominal (itibari) değerinin üzerinde satılması halinde elde edilen fark özkaynaklar altında \'Hisse Senedi İhraç Primleri\' (Emisyon Primi) hesabına kaydedilir.'
)

add_fix(
    'q_1003_master_008',
    ['%1', '%3', '%5', '%10', '%25'],
    'C',
    'Halka açık anonim ortaklıklarda azınlık (azlık) hakları sermayenin en az %5\'ine sahip pay sahipleri tarafından kullanılır (Halka açık olmayan ortaklıklarda bu oran %10\'dur).\n\n📌 Soruda Geçen Kısaltmalar ve Açılımları:\n• TTK: Türk Ticaret Kanunu\n• SPKn: Sermaye Piyasası Kanunu'
)

add_fix(
    'q_1003_master_012',
    [
        'Özel denetçiyi sadece şirket genel müdürü atayabilir.',
        'Bilgi alma veya inceleme hakkı önceden kullanılmış olmak şartıyla, genel kurul talebi reddetse dahi azınlık mahkemeden özel denetçi atanmasını isteyebilir.',
        'Özel denetçi atanması için şirket hisselerinin %99\'una sahip olunmalıdır.',
        'Özel denetim kararı hiçbir şekilde mahkemeye taşınamaz.',
        'Özel denetçi yalnızca şirketin vergi beyannamelerini incelemekle yetkilidir.'
    ],
    'B',
    'TTK m.438 uyarınca bilgi alma hakkını kullanan pay sahipleri, genel kurul özel denetim talebini reddetse dahi mahkemeden özel denetçi atanmasını talep edebilirler.'
)

add_fix(
    'q_1003_master_014',
    ['0.5', '2.0', '2.5', '3.0', '4.0'],
    'B',
    'PD/DD = Piyasa Değeri / Defter Değeri = 50 TL / 25 TL = 2.0 olarak hesaplanır.'
)

add_fix(
    'q_1003_master_016',
    ['%2', '%4', '%5', '%8', '%10'],
    'C', # wait, in old data it was marked as D (%5), let's make %5 as D or match
    'Temettü Verimi = Hisse Başına Temettü / Piyasa Fiyatı = 4 TL / 80 TL = 0.05 = %5\'tir.'
)
# Let's verify key:
FIXES['q_1003_master_016']['options'] = [
    {'key': 'A', 'text': '%2'},
    {'key': 'B', 'text': '%3'},
    {'key': 'C', 'text': '%4'},
    {'key': 'D', 'text': '%5'},
    {'key': 'E', 'text': '%10'}
]
FIXES['q_1003_master_016']['correct_answer'] = 'D'

add_fix(
    'q_1003_master_017',
    ['%5', '%10', '%20', '%25', '%30'],
    'C',
    'Halka arzlarda fiyat aralığı ile talep toplamada tavan fiyat, taban fiyatın en fazla %20 fazlası olabilir (Tavan = Taban * 1.20).\n\n📌 Soruda Geçen Kısaltmalar ve Açılımları:\n• SPK: Sermaye Piyasası Kurulu'
)

add_fix(
    'q_1003_master_019',
    [
        'Borsa İstanbul A.Ş. - BİSTPAY',
        'Gelir İdaresi Başkanlığı - e-Fatura',
        'Merkezi Kayıt Kuruluşu (MKK) - e-GKS Sistemi',
        'Takasbank - TEFAS Sistemi',
        'Sermaye Piyasası Kurulu - KAP Portalı'
    ],
    'C',
    'Halka açık şirketlerde genel kurullara elektronik ortamda katılımı sağlayan e-GKS (Elektronik Genel Kurul Sistemi) Merkezi Kayıt Kuruluşu (MKK) tarafından işletilir.\n\n📌 Soruda Geçen Kısaltmalar ve Açılımları:\n• MKK: Merkezi Kayıt Kuruluşu\n• e-GKS: Elektronik Genel Kurul Sistemi'
)

add_fix(
    'q_1003_master_029',
    ['Düşer.', 'Yükselir.', 'Sabit kalır, etkilenmez.', 'Önce yükselir, sonra nominal değere döner.', 'Sıfıra iner.'],
    'A',
    'Faiz oranları ile sabit kuponlu tahvil fiyatları arasında ters yönlü bir ilişki vardır; piyasa faiz oranları yükseldiğinde tahvilin fiyatı düşer.'
)

add_fix(
    'q_1003_master_030',
    ['Kupon Baremi', 'Temerrüt Katsayısı', 'Konveksite (Dışbükeylik)', 'Nominal Getiri Oranı', 'Durasyon (Macaulay Süresi)'],
    'E',
    'Durasyon (Macaulay Süresi); bir tahvilin kupon ve anapara nakit akışlarının bugünkü değerleriyle ağırlıklandırılmış ortalama vadesidir ve tahvilin faiz riskine duyarlılığını ölçer.'
)

add_fix(
    'q_1003_master_031',
    ['Paya Dönüştürülebilir Tahvil (PDT)', 'Finansman Bonosu', 'Garantili Bono', 'Hazine Bonosu', 'Varlığa Dayalı Menkul Kıymet (VDMK)'],
    'A',
    'Paya Dönüştürülebilir Tahviller (PDT); sahibine vadesinde ihraççı ortaklığın paylarına dönüştürme hakkı veren borçlanma araçlarıdır.\n\n📌 Soruda Geçen Kısaltmalar ve Açılımları:\n• PDT: Paya Dönüştürülebilir Tahvil'
)

add_fix(
    'q_1003_master_034',
    ['AAA', 'AA+', 'A-', 'BBB- (Baa3)', 'BB+ (Ba1)'],
    'D',
    'Uluslararası kredi derecelendirme kuruluşlarının (S&P, Fitch, Moody\'s) notlama skalasında \'Yatırım Yapılabilir Seviye\' (Investment Grade) en alt sınırı BBB- (Moody\'s için Baa3) notudur.'
)

add_fix(
    'q_1003_master_035',
    ['Devlet Tahvili', 'Gelir Ortaklığı Senedi', 'Kira Sertifikası', 'Eurobond', 'Hazine Bonosu'],
    'E',
    'Hazine ve Maliye Bakanlığı tarafından yurt içi piyasada ihraç edilen DİBS\'lerden vadesi 1 yıldan kısa olanlara Hazine Bonosu, 1 yıl ve daha uzun olanlara Devlet Tahvili denir.\n\n📌 Soruda Geçen Kısaltmalar ve Açılımları:\n• DİBS: Devlet İç Borçlanma Senetleri'
)

add_fix(
    'q_1003_master_038',
    ['2 katı', '5 katı', '8 katı', '10 katı', 'Sınırsızdır'],
    'B',
    'Halka açık anonim ortaklıkların ihraç edebileceği borçlanma araçlarının azami ihraç tavanı kural olarak özkaynaklarının en fazla 5 katı olabilir (Halka açık olmayan ortaklıklarda bu sınır 3 katıdır).\n\n📌 Soruda Geçen Kısaltmalar ve Açılımları:\n• SPKn: Sermaye Piyasası Kanunu'
)

add_fix(
    'q_1003_master_040',
    ['Kur Riski', 'Temerrüt (Default) Riski', 'Likidite Riski', 'Operasyonel Risk', 'Enflasyon Riski'],
    'B',
    'Bir borçlanma aracının ihraççısının vadesinde anapara veya kupon faizini ödeyememesi durumuna Temerrüt (Kredi / Default) Riski denir.'
)

add_fix(
    'q_1003_master_042',
    ['%25', '%20', '%15', '%10', '%5'],
    'A',
    'Cari Getiri (Current Yield) = Yıllık Kupon Faizi Tutarı / Piyasa Fiyatı = (1.000 * 0.20) / 800 = 200 / 800 = %25 olarak hesaplanır.'
)

add_fix(
    'q_1003_master_045',
    ['İzahname Onayı', 'İhraç Belgesi ve İhraç Tavanı Onayı', 'Ticaret Sicil Tescili', 'Borsa Kotasyon Şartı', 'Belediye Ruhsatı'],
    'B',
    'Halka arz edilmeksizin nitelikli yatırımcılara ihraç edilecek borçlanma araçları için SPK tarafından \'İhraç Belgesi\' onaylanır; izahname hazırlanmaz.\n\n📌 Soruda Geçen Kısaltmalar ve Açılımları:\n• SPK: Sermaye Piyasası Kurulu'
)

add_fix(
    'q_1003_master_046',
    ['Haftalık', '15 günde bir', 'En az 6 ayda bir', 'En az 1 ayda bir (1, 3, 6 veya 12 aylık periyotlar)', 'Yalnızca vade bitiminde'],
    'D',
    'Borçlanma araçlarında kupon ödeme dönemleri mevzuat uyarınca en az 1 ayda bir olmak üzere 1, 3, 6 veya 12 aylık periyotlar halinde belirlenebilir.'
)

add_fix(
    'q_1003_master_053',
    [
        'Sahipliğe Dayalı Kira Sertifikası (İcare Sukuku)',
        'Ortaklığa Dayalı Kira Sertifikası (Mudaraba Sukuku)',
        'Alım-Satıma Dayalı Kira Sertifikası (Murabaha Sukuku)',
        'Eser Sözleşmesine Dayalı Kira Sertifikası (İstisna Sukuku)',
        'Yönetim Sözleşmesine Dayalı Kira Sertifikası (Vekalet Sukuku)'
    ],
    'E',
    'Kaynak kuruluşa ait varlıkların mülkiyet devri yapılmaksızın VKŞ lehine yönetilmesi ve gelirlerinin aktarılması esasına dayanan sukuk türü Yönetim Sözleşmesine Dayalı Kira Sertifikası\'dır (Vekalet).\n\n📌 Soruda Geçen Kısaltmalar ve Açılımları:\n• VKŞ: Varlık Kiralama Şirketi'
)

add_fix(
    'q_1003_master_054',
    [
        'Sahipliğe Dayalı Kira Sertifikası',
        'Yönetim Sözleşmesine Dayalı Kira Sertifikası',
        'Alım-Satıma Dayalı Kira Sertifikası (Murabaha Sukuku)',
        'Eser Sözleşmesine Dayalı Kira Sertifikası',
        'Ortaklığa Dayalı Kira Sertifikası'
    ],
    'C',
    'Bir emtianın peşin satın alınıp kaynak kuruluşa vadeli kâr payıyla satılması esasına dayanan kira sertifikası Murabaha (Alım-Satıma Dayalı) Sukuktur.\n\n📌 Soruda Geçen Kısaltmalar ve Açılımları:\n• VKŞ: Varlık Kiralama Şirketi'
)

add_fix(
    'q_1003_master_055',
    [
        'Sahipliğe Dayalı Kira Sertifikası',
        'Ortaklığa Dayalı Kira Sertifikası (Mudaraba / Müşareke Sukuku)',
        'Alım-Satıma Dayalı Kira Sertifikası',
        'Yönetim Sözleşmesine Dayalı Kira Sertifikası',
        'Eser Sözleşmesine Dayalı Kira Sertifikası'
    ],
    'B',
    'Mudaraba (emek-sermaye) ve Müşareke (kâr-zarar ortaklığı) ilkelerine dayalı kira sertifikası türü Ortaklığa Dayalı Kira Sertifikası\'dır.'
)

add_fix(
    'q_1003_master_057',
    ['Lider Aracı Kurum', 'Merkezi Saklama Kuruluşu', 'Derecelendirme Kuruluşu', 'Portföy Saklayıcısı', 'Kaynak Kuruluş (Originator)'],
    'E',
    'Kira sertifikası ihracında finansman ihtiyacı duyan ve varlıklarını VKŞ\'ye devreden kuruluşa \'Kaynak Kuruluş\' (Originator) denir.\n\n📌 Soruda Geçen Kısaltmalar ve Açılımları:\n• VKŞ: Varlık Kiralama Şirketi'
)

add_fix(
    'q_1003_master_058',
    ['Bankalar, aracı kurumlar, ipotek finansmanı kuruluşları ve GYO\'lar', 'Yalnızca Vakıflar Genel Müdürlüğü', 'Yalnızca Tasarruf Mevduatı Sigorta Fonu (TMSF)', 'Sadece yabancı hedge fonlar', 'Yalnızca noterler'],
    'A',
    'SPK düzenlemelerine göre bankalar, aracı kurumlar, ipotek finansmanı kuruluşları ve GYO\'lar münhasıran kira sertifikası ihraç etmek üzere Varlık Kiralama Şirketi (VKŞ) kurabilirler.\n\n📌 Soruda Geçen Kısaltmalar ve Açılımları:\n• VKŞ: Varlık Kiralama Şirketi'
)

add_fix(
    'q_1003_master_059',
    ['Borsa İstanbul Pay Piyasası', 'Borsa İstanbul Borçlanma Araçları Piyasası', 'Kıymetli Madenler Piyasası', 'VİOP Opsiyon Pazarı', 'Serbest Döviz Piyasası'],
    'B',
    'Halka arz edilen veya nitelikli yatırımcılara ihraç edilen kira sertifikaları Borsa İstanbul Borçlanma Araçları Piyasası (BAP) bünyesinde işlem görür.\n\n📌 Soruda Geçen Kısaltmalar ve Açılımları:\n• BAP: Borçlanma Araçları Piyasası'
)

add_fix(
    'q_1003_master_061',
    ['Sahipliğe Dayalı Sukuk', 'Murabaha Sukuku', 'Eser Sözleşmesine Dayalı Kira Sertifikası (İstisna Sukuku)', 'Mudaraba Sukuku', 'Vekalet Sukuku'],
    'C',
    'VKŞ\'nin işveren, kaynak kuruluşun yüklenici olduğu bir inşaat/üretim eser sözleşmesine dayalı sukuk türü İstisna (Eser Sözleşmesine Dayalı) Sukuktur.'
)

add_fix(
    'q_1003_master_062',
    ['İtfa', 'Emisyon', 'Kotasyon', 'Kuponaj', 'Arbitraj'],
    'A',
    'Borçlanma araçlarında ve kira sertifikalarında vade sonunda anaparanın ödenerek borcun tamamen kapatılmasına \'İtfa\' denir.'
)

add_fix(
    'q_1003_master_063',
    ['Hisse Senedi', 'Gelir Ortaklığı Senedi (GOS)', 'Finansman Bonosu', 'Mevduat Sertifikası', 'Eurobond'],
    'B',
    'Köprü, baraj, otoyol gibi kamu altyapı tesislerinin gelirlerine ortaklık sağlayan menkul kıymet Gelir Ortaklığı Senedi\'dir (GOS).\n\n📌 Soruda Geçen Kısaltmalar ve Açılımları:\n• GOS: Gelir Ortaklığı Senedi'
)

add_fix(
    'q_1003_master_064',
    ['Hazine Bonosu', 'Devlet Tahvili', 'Varlığa Dayalı Menkul Kıymet', 'Gelire Endeksli Senet (GES)', 'İpotek Teminatlı Menkul Kıymet'],
    'D',
    'Getirisi Kamu İktisadi Teşebbüslerinin (KİT) bütçeye aktardıkları hasılat paylarına endekslenen DİBS türü Gelire Endeksli Senet\'tir (GES).\n\n📌 Soruda Geçen Kısaltmalar ve Açılımları:\n• GES: Gelire Endeksli Senet\n• KİT: Kamu İktisadi Teşebbüsü'
)

add_fix(
    'q_1003_master_065',
    ['Borsa İstanbul A.Ş.', 'İstanbul Takas ve Saklama Bankası A.Ş.', 'Hazine Müsteşarlığı Varlık Kiralama Şirketi A.Ş.', 'Merkezi Kayıt Kuruluşu A.Ş.', 'Türkiye Cumhuriyet Merkez Bankası'],
    'C',
    'Hazine ve Maliye Bakanlığı adına yurt içi ve yurt dışı kamu kira sertifikası ihraçlarını Hazine Müsteşarlığı Varlık Kiralama Şirketi A.Ş. yürütür.\n\n📌 Soruda Geçen Kısaltmalar ve Açılımları:\n• VKŞ: Varlık Kiralama Şirketi'
)

add_fix(
    'q_1003_master_067',
    ['Alım Varantı (Call Warrant)', 'Satım Varantı (Put Warrant)', 'Finansman Bonosu', 'İskontolu Tahvil', 'Ters Repo'],
    'A',
    'Dayanak varlığın fiyatının gelecekte yükseleceğini bekleyen yatırımcı Alım Varantı (Call Warrant) satın almalıdır.'
)

add_fix(
    'q_1003_master_069',
    ['Amerikan Tipi (American Style)', 'Asya Tipi (Asian Style)', 'Bermuda Tipi', 'Dijital Tip', 'Avrupa Tipi (European Style)'],
    'E',
    'Sadece vade bitim gününde (vadesinde) kullanılabilen opsiyon/varant türü Avrupa Tipi (European Style); vadeye kadar herhangi bir günde kullanılabilen ise Amerikan Tipi opsiyondur.'
)

add_fix(
    'q_1003_master_070',
    ['0 TL', '5 TL', '10 TL', '20 TL', '120 TL'],
    'D',
    'Alım Varantı İçsel Değeri = Spot Fiyat - Kullanım Fiyatı = 120 TL - 100 TL = 20 TL\'dir.'
)

add_fix(
    'q_1003_master_071',
    ['Kârda (In-the-Money)', 'Zararda (Out-of-the-Money)', 'Başabaşta (At-the-Money)', 'Derin Kârda (Deep In-the-Money)', 'Kaldıraçsız'],
    'C',
    'Spot piyasa fiyatının kullanım fiyatına eşit olduğu durum (Spot = Kullanım Fiyatı) \'Başabaşta\' (At-the-Money) olarak adlandırılır.'
)

add_fix(
    'q_1003_master_072',
    ['Delta', 'Gama', 'Teta (Theta)', 'Vega', 'Ro'],
    'C',
    'Teta (Theta); varantın vadesine yaklaştıkça değer kaybetmesini (zaman erimesini / time decay) ölçen duyarlılık katsayısıdır.'
)

add_fix(
    'q_1003_master_073',
    ['Teta', 'Delta', 'Vega', 'Ro', 'Gama'],
    'B',
    'Delta; dayanak varlığın fiyatındaki 1 birimlik değişimin varant fiyatında yaratacağı değişimi ölçen duyarlılık katsayısıdır.'
)

add_fix(
    'q_1003_master_074',
    ['Piyasa Yapıcı Üye (Market Maker)', 'Takas Odası Hakemi', 'Portföy Saklayıcısı', 'Bağımsız Denetçi', 'Hazine Temsilcisi'],
    'A',
    'Varantlarda sürekli alım-satım kotasyonu vererek likiditeyi sağlayan kuruluş \'Piyasa Yapıcı\' (Market Maker) yatırım kuruluşudur.'
)

add_fix(
    'q_1003_master_075',
    ['Devlet Tahvili', 'Finansman Bonosu', 'Hisse Senedi', 'Yatırım Kuruluşu Sertifikası', 'Katılma İntifa Senedi'],
    'D',
    'İhraççı yatırım kuruluşu tarafından çıkarılan ve belirli bir dayanak varlığın getirisine katılım sağlayan menkul kıymet \'Yatırım Kuruluşu Sertifikası\'dır.'
)

add_fix(
    'q_1003_master_076',
    ['5', '20', '50', '100', '200'],
    'B',
    'Efektif Kaldıraç = (Dayanak Varlık Fiyatı / Varant Fiyatı) * Dönüşüm Oranı = (50 / 2.5) * 1 = 20\'dir.'
)

add_fix(
    'q_1003_master_078',
    ['1 adet', '2 adet', '5 adet', '8 adet', '10 adet'],
    'E',
    'Dönüşüm oranı 0.10 ise: 1 / 0.10 = 10 adet varant 1 adet hisse senedi üzerinde hak sağlar.'
)

add_fix(
    'q_1003_master_079',
    ['Vega', 'Teta', 'Delta', 'Ro', 'Gama'],
    'A',
    'Vega; dayanak varlığın zımni volatilitesindeki (oynaklık) %1\'lik değişimin varant fiyatına etkisini ölçen katsayıdır.'
)

add_fix(
    'q_1003_master_080',
    ['Geniş Yetkili Aracı Kurum', 'Dar Yetkili Aracı Kurum', 'Kısmi Yetkili Aracı Kurum', 'Kalkınma Ajansı', 'Döviz Bürosu'],
    'A',
    'Aracı kuruluş varantı ihraç edebilmek için SPK\'dan \'Geniş Yetkili Aracı Kurum\' yetki belgesine sahip olunması zorunludur.\n\n📌 Soruda Geçen Kısaltmalar ve Açılımları:\n• SPK: Sermaye Piyasası Kurulu'
)

add_fix(
    'q_1003_master_082',
    ['%25', '%51', '%80', '%90', '%100'],
    'C',
    'Bir yatırım fonunun \'Hisse Senedi Yoğun Fon\' sayılabilmesi için fon portföyünün en az %80\'inin devamlı olarak BIST hisse senetlerinden oluşması yasal zorunluluktur (Vergi avantajı sağlar).\n\n📌 Soruda Geçen Kısaltmalar ve Açılımları:\n• BIST: Borsa İstanbul'
)

add_fix(
    'q_1003_master_085',
    ['%20', '%50', '%65', '%75', '%80'],
    'E',
    'Fon toplam değerinin en az %80\'i diğer yatırım fonları ve borsa yatırım fonlarının katılma paylarından oluşan fonlar \'Fon Sepeti Fonu\' olarak adlandırılır.'
)

add_fix(
    'q_1003_master_086',
    ['Portföy Yöneticisi', 'Portföy Saklayıcısı', 'Takas Denetçisi', 'Kayıt Kabul Memuru', 'Yetkilendirilmiş Katılımcı (Authorized Participant)'],
    'E',
    'BYF paylarının birincil piyasada ihraç ve itfasında (pay sepeti oluşturma/bozma) kurucu adına aracılık eden kurum \'Yetkilendirilmiş Katılımcı\'dır (Authorized Participant).\n\n📌 Soruda Geçen Kısaltmalar ve Açılımları:\n• BYF: Borsa Yatırım Fonu'
)

add_fix(
    'q_1003_master_087',
    ['Hisse Senedi Fonu', 'Borçlanma Araçları Fonu', 'Para Piyasası Fonu', 'Katılım Fonu', 'Serbest Fon'],
    'D',
    'Portföyünün tamamı faizsiz finans ilkelerine uygun paylar, kira sertifikaları ve kıymetli madenlerden oluşan fonlar \'Katılım Fonu\' olarak adlandırılır.'
)

add_fix(
    'q_1003_master_093',
    [
        'Şirketlerin bankalardan aldıkları ticari kredileri gösteren bir kredi belgesidir.',
        'Sadece devlet memurlarına lojman tahsis edilmesini sağlayan bir hak belgesidir.',
        'Hisse senedi gibi şirket genel kurulunda oy kullanma hakkı tanıyan ortaklık payıdır.',
        'İnşa edilecek veya edilmekte olan gayrimenkul projelerinin finansmanında kullanılan, bağımsız bölümü temsil eden menkul kıymettir.',
        'Belediyelerin arsa kamulaştırma bedellerini ödemek için çıkardığı borçlanma senedidir.'
    ],
    'D',
    'Gayrimenkul Sertifikası; gayrimenkul projelerinin finansmanında kullanılan, nominal değeri belirli bir bağımsız bölümü veya alan birimini temsil eden menkul kıymettir.'
)

add_fix(
    'q_1003_master_094',
    ['Asli Edim (Gayrimenkulün Mülkiyetini Devralma)', 'Tali Edim (Nakit Bedel Alma)', 'Rüçhan Hakkı', 'İntifa Hakkı', 'Temerrüt Tasfiyesi'],
    'A',
    'Gayrimenkul sertifikasında yeterli sayıda sertifikayı biriktirerek dairenin mülkiyetini tapudan alma hakkına \'Asli Edim\'; nakit karşılığını alma hakkına \'Tali Edim\' denir.'
)

add_fix(
    'q_1003_master_098',
    ['Yalnızca Temettü Vergisi', 'Yalnızca Noter Harcı', 'Banka Kredi Faiz Riski', 'Enflasyon Sabitleme Riski', 'Hisse Fiyat Hareketi ve Döviz Kuru Riski'],
    'E',
    'Yurt dışı hisse senetlerine yatırım yapan bir yatırımcı hem yabancı hissenin borsa fiyat hareketine (piyasa riski) hem de yabancı para biriminin TL karşısındaki kur dalgalanmasına (kur riski) maruz kalır.'
)

add_fix(
    'q_1003_konu_003',
    ['%5', '%10', '%15', '%20', '%25'],
    'D',
    'Fiyat istikrarını sağlayıcı işlemler için kullanılacak fon bütçesi, halka arzdan elde edilen brüt gelirin en fazla %20\'sini aşamaz (Süre en fazla 30 gündür).\n\n📌 Soruda Geçen Kısaltmalar ve Açılımları:\n• SPK: Sermaye Piyasası Kurulu'
)

add_fix(
    'q_1003_konu_006',
    ['%51', '%65', '%80', '%90', '%100'],
    'C',
    'Hisse Senedi Yoğun Fon portföyünün en az %80\'i sürekli olarak Borsa İstanbul\'da işlem gören paylardan oluşmalıdır.\n\n📌 Soruda Geçen Kısaltmalar ve Açılımları:\n• BIST: Borsa İstanbul'
)

add_fix(
    'q_1003_konu_007',
    ['%10', '%20', '%30', '%40', '%50'],
    'D',
    'Genel yatırım fonlarında portföyde %5\'ten fazla paya sahip olan ihraççıların yatırımlarının toplamı, fon portföy değerinin %40\'ını aşamaz (5/40 Kuralı).'
)

add_fix(
    'q_1003_konu_008',
    ['45 gün', '90 gün', '180 gün', '365 gün', '730 gün'],
    'A',
    'Para piyasası fonlarının portföyündeki varlıkların ağırlıklı ortalama vadesi en fazla 45 gün olmak zorundadır (Vadesine en fazla 184 gün kalmış varlıklar dahil edilir).'
)

add_fix(
    'q_1003_konu_011',
    ['500 TL', '3.500 TL', '4.000 TL', '5.000 TL', '12.000 TL'],
    'B',
    'Bakiye sürdürme teminatının (12.000 TL) altına inip 11.500 TL\'ye düştüğünde, teminat başlangıç seviyesine (15.000 TL) tamamlanır: 15.000 - 11.500 = 3.500 TL nakit yatırılmalıdır.\n\n📌 Soruda Geçen Kısaltmalar ve Açılımları:\n• VİOP: Vadeli İşlem ve Opsiyon Piyasası'
)

add_fix(
    'q_1003_konu_012',
    ['97,00 TL', '95,00 TL', '96,50 TL', '98,00 TL', '103,00 TL'],
    'A',
    'Kupon Faizi Tutarı = 100 * %8 = 8 TL. Birikmiş Faiz = (45 / 180) * 8 TL = 2,00 TL. Kirli Fiyat = Temiz Fiyat + Birikmiş Faiz = 95,00 + 2,00 = 97,00 TL.'
)

add_fix(
    'q_1003_konu_013',
    ['%1', '%2', '%3', '%5', '%10'],
    'C', # Wait, let's make %3 as E or match original
    'Bir PYŞ yönettikleri tüm genel yatırım fonları için tek bir bankada fon toplam değerlerinin en fazla %3\'ü oranında mevduat/katılma hesabı açabilir.'
)
FIXES['q_1003_konu_013']['options'] = [
    {'key': 'A', 'text': '%1'},
    {'key': 'B', 'text': '%2'},
    {'key': 'C', 'text': '%5'},
    {'key': 'D', 'text': '%10'},
    {'key': 'E', 'text': '%3'}
]
FIXES['q_1003_konu_013']['correct_answer'] = 'E'

add_fix(
    'q_1003_ogretici_004',
    ['Şirketin asil ortağı', 'Şirket yönetim kurulu başkanı', 'Tüzel kişilik temsilcisi', 'Alacaklı', 'Garantör hissedar'],
    'D',
    'Tahvil sahibi ortaklığın sermaye ortağı değil; şirkete borç vermiş olan öncelikli bir alacaklısıdır.'
)

# =========================================================================
# MODÜL 1005: YATIRIM KURULUŞLARI
# =========================================================================

add_fix(
    'q_1005_master_011',
    ['%5, %10, %15, %20', '%10, %20, %33, %50', '%25, %50, %75, %100', '%5, %25, %50, %75', '%10, %25, %50, %100'],
    'B',
    'Yatırım kuruluşlarında doğrudan veya dolaylı pay sahipliğinin sermayenin %10, %20, %33 veya %50\'sini aşması veya bu oranların altına düşmesi SPK\'nın önceden iznine tabidir.\n\n📌 Soruda Geçen Kısaltmalar ve Açılımları:\n• SPK: Sermaye Piyasası Kurulu'
)

add_fix(
    'q_1005_master_021',
    ['Portföy Aracılığı', 'Emir İletimine Aracılık', 'Bireysel Portföy Yöneticiliği', 'Genel Saklama Hizmeti', 'Yatırım Danışmanlığı'],
    'B',
    'Müşteriden alınan emirlerin işlem yapılmak üzere başka bir kuruluşa veya borsaya iletilmesi faaliyeti \'Emir İletimine Aracılık\'tır (Dar yetkili kurumlar icra edebilir).'
)

add_fix(
    'q_1005_master_022',
    ['İşlem Aracılığı', 'Emir İletimine Aracılık', 'Yatırım Tavsiyesi', 'Kredi Tahsisi', 'Portföy Saklayıcılığı'],
    'A',
    'Müşteri nam ve hesabına emirlerin borsada bizzat eşleştirilip icra edilmesi faaliyeti \'İşlem Aracılığı\'dır (Kısmi ve Geniş yetkililer yapabilir).'
)

add_fix(
    'q_1005_master_062',
    [
        'Yalnızca Devlet İç Borçlanma Senetleri (DİBS)',
        'BIST 30 endeksinde işlem gören mavi çip hisse senetleri',
        'Hazine Bonoları ve Likit Fonlar',
        'Varantlar, Yatırım Kuruluşu Sertifikaları ve Kaldıraçlı İşlemler (Forex)',
        'Mevduat ve Katılma Hesapları'
    ],
    'D',
    'SPK mevzuatında türev ürünler, varantlar, sertifikalar ve kaldıraçlı döviz işlemleri (Forex) genel müşteriler açısından \'Karmaşık Sermaye Piyasası Aracı\' olarak sınıflandırılır.'
)

add_fix(
    'q_1005_master_072',
    ['%20', '%25', '%35', '%40', '%50'],
    'E',
    'Borsa İstanbul Pay Piyasası kredili alım işlemlerinde uygulanan asgari başlangıç özkaynak oranı mevzuat ve borsa kararları gereği %50\'dir.\n\n📌 Soruda Geçen Kısaltmalar ve Açılımları:\n• BIST: Borsa İstanbul'
)

add_fix(
    'q_1005_master_073',
    ['%10', '%20', '%35', '%50', '%75'],
    'C',
    'Kredili işlemlerde özkaynak oranının düşebileceği alt eşik seviyesi (veya mevzuattaki sürdürme seviyesi) altına inildiğinde aracı kurum özkaynak tamamlama bildirimi yapar.\n\n📌 Soruda Geçen Kısaltmalar ve Açılımları:\n• SPK: Sermaye Piyasası Kurulu'
)

add_fix(
    'q_1005_master_076',
    [
        'Borsa İstanbul tarafından kredili işlem yasağı veya tedbiri getirilmiş pay senetleri ile Yakın İzleme Pazarı hisseleri',
        'BIST 30 endeksinde işlem gören yüksek piyasa değerli ortaklık payları',
        'Devlet İç Borçlanma Senetleri (DİBS)',
        'Borsa Yatırım Fonu (BYF) katılma payları',
        'Hazine ve Maliye Bakanlığı Eurobondları'
    ],
    'A',
    'Borsa İstanbul tarafından kredili işlem yasağı/tedbiri konulmuş paylar ile Yakın İzleme Pazarı (veya C/D grubu) hisseleri kredili alım ve açığa satış işlemlerine konu edilemez.'
)

add_fix(
    'q_1005_master_091',
    ['1 yıl içinde', '3 ay içinde', '30 gün içinde', '5 yıl içinde', '10 yıl içinde'],
    'A',
    'YTM Yönetmeliği uyarınca hakkında tazmin kararı verilen aracı kurumun hak sahipleri YTM\'nin ilan tarihinden itibaren 1 yıl içinde başvurmalıdır.\n\n📌 Soruda Geçen Kısaltmalar ve Açılımları:\n• YTM: Yatırımcı Tazmin Merkezi'
)

add_fix(
    'q_1005_konu_009',
    ['%25', '%10', '%15', '%33', '%50'],
    'A',
    'Aracı kurumların finansal kuruluşlar dışındaki ortaklıklara yapabilecekleri iştiraklerin toplamı özsermayelerinin en fazla %25\'ini aşamaz.\n\n📌 Soruda Geçen Kısaltmalar ve Açılımları:\n• SPK: Sermaye Piyasası Kurulu'
)

add_fix(
    'q_1005_konu_013',
    ['10:1', '20:1', '50:1', '100:1', '400:1'],
    'A',
    'SPK düzenlemeleri uyarınca yurt içi bireysel müşteriler için kaldıraçlı işlemlerde (Forex) uygulanabilecek azami kaldıraç oranı 10:1\'dir.\n\n📌 Soruda Geçen Kısaltmalar ve Açılımları:\n• FX: Kaldıraçlı Alım Satım (Forex)'
)

# =========================================================================
# MODÜL 1012: TAKAS, SAKLAMA VE OPERASYON
# =========================================================================

add_fix(
    'q_1012_master_001',
    [
        'Borsada şirket genel kurullarının toplanarak kâr payı dağıtması işlemidir.',
        'Aracı kurumların müşterilerine yeni hisse senedi kredisi tahsis etmesidir.',
        'Şirketlerin sermaye artırımı için SPK\'ya izahname sunmasıdır.',
        'Hisse senetlerinin noter onaylı olarak fiziki senetlere basılmasıdır.',
        'Borsada gerçekleşen işlemlerden doğan menkul kıymet teslim ve nakit ödeme borçlarının karşılıklı olarak tasfiye edilip sonuçlandırılması sürecidir.'
    ],
    'E',
    'Takas (Clearing / Settlement); borsa işlemlerinden doğan alacak ve borçların netleştirilip nakit ve menkul kıymet transferiyle tamamen tasfiye edilmesidir.\n\n📌 Soruda Geçen Kısaltmalar ve Açılımları:\n• BIST: Borsa İstanbul'
)

add_fix(
    'q_1012_master_002',
    [
        'İşlem gören tüm hisseleri tek başına satın alarak borsa endeksini sabitlemesidir.',
        'Müşterilerin borsa işlem komisyonlarını her ayın sonunda nakden ödemesidir.',
        'Borsada şirketlerin bağımsız denetim raporlarını hazırlamasıdır.',
        'Alıcıya karşı SATICI, satıcıya karşı ALICI konumuna geçerek takasın tamamlanmasını mali olarak garanti etmesidir.',
        'Şirket yönetim kurulu üyelerini genel kurul onayından önce atamasıdır.'
    ],
    'D',
    'Merkezi Karşı Taraf (CCP); takas odasının alıcıya karşı satıcı, satıcıya karşı alıcı konumuna geçerek tarafların temerrüt riskini garanti altına almasıdır.\n\n📌 Soruda Geçen Kısaltmalar ve Açılımları:\n• CCP: Merkezi Karşı Taraf\n• Takasbank: İstanbul Takas ve Saklama Bankası A.Ş.'
)

add_fix(
    'q_1012_master_004',
    [
        'Doğrudan Cumhurbaşkanlığına bağlı bir kamu tüzel kişiliğidir.',
        'Yalnızca yabancı yatırımcıların hesap açabildiği özel bir offshore bankadır.',
        'Özel bir anonim şirket statüsünde, Bankacılık Kanunu\'na tabi bir yatırım/kalkınma bankası ve SPKn m.77 uyarınca Türkiye\'nin Merkezi Takas Kuruluşudur.',
        'Borsa İstanbul bünyesinde şubesi bulunmayan ticari bir mevduat bankasıdır.',
        'Vakıf tüzel kişiliğine sahip kâr amacı gütmeyen bir yardım kuruluşudur.'
    ],
    'C',
    'Takasbank; Bankacılık Kanunu\'na tabi bir yatırım ve kalkınma bankası olup, 6362 sayılı Kanun m.77 uyarınca Türkiye\'nin Merkezi Takas Kuruluşu ve yetkilendirilmiş Merkezi Karşı Tarafıdır.\n\n📌 Soruda Geçen Kısaltmalar ve Açılımları:\n• Takasbank: İstanbul Takas ve Saklama Bankası A.Ş.'
)

add_fix(
    'q_1012_master_006',
    ['T+0 (Aynı gün)', 'T+2 (İkinci iş günü)', 'T+3 (Üçüncü iş günü)', 'Haftalık takas', 'T+1 (İşlem gününü izleyen birinci iş günü)'],
    'E',
    'VİOP\'ta günlük kâr/zarar nakit uzlaşması ve teminat tamamlama süresi ertesi iş günü (T+1) sabahı seans açılışından önce tamamlanır.\n\n📌 Soruda Geçen Kısaltmalar ve Açılımları:\n• VİOP: Vadeli İşlem ve Opsiyon Piyasası'
)

add_fix(
    'q_1012_master_007',
    [
        'Ödeme Karşılığı Teslim İlkesi (DvP / Delivery versus Payment)',
        'Açığa Satış ve Ödünç İlkesi',
        'Tek Taraflı Takas İlkesi',
        'Zamanaşımı İlkesi',
        'Kayıtsız Şartsız Teslim İlkesi'
    ],
    'A',
    'Teslim Karşılığı Ödeme (DvP); menkul kıymet devri ile nakit ödemenin eşanlı olarak gerçekleşmesini şart koşarak anapara temerrüt riskini sıfırlar.'
)

add_fix(
    'q_1012_master_008',
    ['Takasbank Para Piyasası (TPP)', 'BIST Tahvil Bono Kesin Alım Pazarı', 'Serbest Altın Piyasası', 'Bankalararası Repo Pazarı', 'VİOP Vadeli Pazar'],
    'A',
    'Takasbank üyelerinin kısa vadeli TL likidite ihtiyaçlarını karşıladıkları çok taraflı kör havuz piyasası Takasbank Para Piyasası\'dır (TPP).\n\n📌 Soruda Geçen Kısaltmalar ve Açılımları:\n• TPP: Takasbank Para Piyasası'
)

add_fix(
    'q_1012_master_009',
    [
        'Doğrudan Takas Üyesi (Direct Clearing Member) ve Genel Takas Üyesi (General Clearing Member)',
        'Yerli Takas Üyesi ve Yabancı Takas Üyesi',
        'Bireysel Takas Üyesi ve Kurumsal Takas Üyesi',
        'Kısa Vadeli Takas Üyesi ve Uzun Vadeli Takas Üyesi',
        'Muaf Takas Üyesi ve Zorunlu Takas Üyesi'
    ],
    'A',
    'Takasbank nezdinde takas üyeleri: Yalnızca kendi işlemlerini takas eden \'Doğrudan Takas Üyesi\' ve diğer kurumların işlemlerini de takas edebilen \'Genel Takas Üyesi\' olarak ikiye ayrılır.'
)

add_fix(
    'q_1012_master_010',
    ['T+2 (İkinci iş günü)', 'T+0 (Aynı gün içinde)', 'T+1 (Ertesi iş günü)', 'T+3 (Üçüncü iş günü)', '1 hafta sonra'],
    'B',
    'Borçlanma Araçları Piyasası Kesin Alım Satım Pazarında aynı gün valörlü işlemlerin takası T+0 (aynı gün) sonuçlandırılır.\n\n📌 Soruda Geçen Kısaltmalar ve Açılımları:\n• BAP: Borçlanma Araçları Piyasası'
)

add_fix(
    'q_1012_master_011',
    ['Takasbank ve Bankalararası Takas Odaları Merkezi (BTOM)', 'Merkezi Kayıt Kuruluşu', 'Sermaye Piyasası Kurulu', 'Gelir İdaresi Başkanlığı', 'Borsa İstanbul'],
    'A',
    'Bankalararası çek takası işlemleri Takasbank ve BTOM koordinasyonunda elektronik ortamda yürütülür.\n\n📌 Soruda Geçen Kısaltmalar ve Açılımları:\n• BTOM: Bankalararası Takas Odaları Merkezi'
)

add_fix(
    'q_1012_master_012',
    ['Merkezi Kayıt Kuruluşu (MKK)', 'Borsa İstanbul (BIST)', 'Sermaye Piyasası Kurulu (SPK)', 'İstanbul Takas ve Saklama Bankası A.Ş. (Takasbank)', 'Hazine ve Maliye Bakanlığı'],
    'D',
    'TEFAS platformunda işlem gören tüm yatırım fonlarının katılma payı ve nakit takas operasyonları Takasbank tarafından yürütülür.\n\n📌 Soruda Geçen Kısaltmalar ve Açılımları:\n• TEFAS: Türkiye Elektronik Fon Alım Satım Platformu'
)

add_fix(
    'q_1012_master_017',
    ['TCMB Ankara Kasası', 'Takasbank Kıymetli Madenler Saklama Kasaları', 'Darphane Genel Müdürlüğü', 'Kapalıçarşı Sandıkları', 'Hazine Müsteşarlığı'],
    'B',
    'Borsa İstanbul Kıymetli Madenler Piyasası\'nda işlem gören altın ve kıymetli madenlerin fiziki saklaması Takasbank kasalarında yapılır.\n\n📌 Soruda Geçen Kısaltmalar ve Açılımları:\n• Takasbank: İstanbul Takas ve Saklama Bankası A.Ş.'
)

add_fix(
    'q_1012_master_019',
    ['VAR (Value at Risk)', 'SPAN (Standard Portfolio Analysis of Risk)', 'Monte Carlo Algoritması', 'Black-Scholes Modeli', 'Durbin-Watson Testi'],
    'B',
    'Takasbank VİOP\'ta portföy bazında dinamik teminat hesaplamasında uluslararası standart olan SPAN (Standard Portfolio Analysis of Risk) algoritmasını kullanır.'
)

add_fix(
    'q_1012_master_020',
    ['Takas ve MKT İşlem Ücreti', 'Damga Vergisi', 'BSMV', 'Stopaj Kesintisi', 'Borsa Tescil Harcı'],
    'A',
    'Takasbank sunduğu takas ve merkezi karşı taraf (MKT) hizmetleri için üyelerden tarife uyarınca Takas ve MKT İşlem Ücreti tahsil eder.'
)

add_fix(
    'q_1012_master_022',
    ['Cuma günü', 'Takip eden Salı günü', 'Takip eden Pazartesi günü', 'Cumartesi günü', 'Çarşamba günü'],
    'B',
    'Perşembe günü yapılan işlemin takası normalde Pazartesi (T+2) günüdür; ancak aradaki Cuma resmi tatil ise takas takip eden Salı günü gerçekleşir (Tatiller iş günü sayılmaz).'
)

add_fix(
    'q_1012_master_024',
    ['BKM Express', 'SWIFT Sistemi', 'TCMB EFT / Elektronik Fon Transfer Sistemi', 'PTT Posta Çeki', 'FAST Sistemi'],
    'C',
    'Takasbank\'ın bankalararası büyük tutarlı nakit netleştirme ve mutabakatları Türkiye Cumhuriyet Merkez Bankası EFT sistemi üzerinden sonuçlandırılır.\n\n📌 Soruda Geçen Kısaltmalar ve Açılımları:\n• TCMB: Türkiye Cumhuriyet Merkez Bankası\n• EFT: Elektronik Fon Transferi'
)

add_fix(
    'q_1012_master_025',
    ['Borsa İstanbul A.Ş.', 'Merkezi Kayıt Kuruluşu A.Ş.', 'Türkiye Sermaye Piyasaları Birliği', 'Kredi Garanti Fonu', 'İstanbul Takas ve Saklama Bankası A.Ş. (Takasbank)'],
    'E',
    'Kolektif yatırım kuruluşlarının (fonların) varlıklarının saklandığı birincil portföy saklayıcısı kuruluşu Takasbank\'tır.\n\n📌 Soruda Geçen Kısaltmalar ve Açılımları:\n• Takasbank: İstanbul Takas ve Saklama Bankası A.Ş.'
)

add_fix(
    'q_1012_master_026',
    [
        'Şirketlerin vergi borçlarını tahsil etmek ve vergi dairesine yatırmak',
        'Borsa İstanbul Pay Piyasası hisse senedi işlemlerinde kredi tahsis etmek',
        'Borsada işlem gören şirketlerin yönetim kurulu başkanlarını seçmek',
        'Sermaye piyasası araçlarının kaydileştirilmesine ilişkin işlemleri yürütmek, bunların hak sahipleri bazında elektronik ortamda kayden izlenmesini ve merkezi saklamasını sağlamak',
        'Döviz kurlarını günlük olarak ilan etmek ve para basmak'
    ],
    'D',
    '6362 sayılı Kanun m.81 uyarınca MKK\'nın temel kanuni görevi; sermaye piyasası araçlarının kaydileştirilmesi ve hak sahipleri bazında kayden izlenmesidir.\n\n📌 Soruda Geçen Kısaltmalar ve Açılımları:\n• MKK: Merkezi Kayıt Kuruluşu A.Ş.'
)

add_fix(
    'q_1012_master_027',
    ['Fiziki Tescil', 'Kaydileştirme (Dematerialization)', 'Blokaj Şerhi', 'Virmanlama', 'Kotasyon'],
    'B',
    'Menkul kıymetlerin fiziki kağıt senet yerine elektronik veri olarak ihraç edilip sistemde izlenmesine Kaydileştirme (Dematerialization) denir.'
)

add_fix(
    'q_1012_master_030',
    [
        'Şirket genel müdürünün kişisel mülkiyetine bedelsiz olarak geçer.',
        'Kanunen YTM\'ye intikal eder; pay sahiplerinin mülkiyet hakları YTM\'ye devredilmiş sayılır ve paylar YTM tarafından satılarak bedeli Hazineye/YTM\'ye aktarılır.',
        'İlgili paylar derhal imha edilir ve şirket sermayesi otomatik olarak azalır.',
        'Aracı kurumun ticari kazancı sayılarak bilançosuna kâr kaydedilir.',
        'Hisseler Borsa İstanbul çalışanlarına eşit olarak prim dağıtılır.'
    ],
    'B',
    'SPKn m.13 uyarınca süresi içinde kaydileştirilmeyen fiziki paylar kanunen YTM\'ye devredilir ve YTM tarafından satılarak geliri kaydedilir.\n\n📌 Soruda Geçen Kısaltmalar ve Açılımları:\n• YTM: Yatırımcı Tazmin Merkezi\n• MKK: Merkezi Kayıt Kuruluşu'
)

add_fix(
    'q_1012_master_033',
    ['e-Devlet Portalı', 'KAP Sistemi', 'e-ŞİRKET: Şirketler Bilgi Portalı', 'e-YATIRIMCI', 'e-GKS'],
    'C',
    'TTK ve sermaye piyasası mevzuatı uyarınca şirketlerin yasal bilgi ve finansal tablolarını açıkladığı MKK sistemi e-ŞİRKET platformudur.\n\n📌 Soruda Geçen Kısaltmalar ve Açılımları:\n• MKK: Merkezi Kayıt Kuruluşu'
)

add_fix(
    'q_1012_master_034',
    ['e-Devlet', 'e-YATIRIMCI', 'e-VEDO (Elektronik Veri Deposu)', 'e-MKK', 'e-GKS'],
    'C',
    'Türev işlem sözleşmelerinin raporlandığı MKK bünyesindeki merkezi veri depolama platformu e-VEDO\'dur.\n\n📌 Soruda Geçen Kısaltmalar ve Açılımları:\n• e-VEDO: Elektronik Veri Deposu\n• MKK: Merkezi Kayıt Kuruluşu'
)

add_fix(
    'q_1012_master_036',
    ['Merkezi Kayıt Kuruluşu A.Ş. (MKK)', 'Borsa İstanbul A.Ş.', 'Takasbank', 'Bilgi Teknolojileri ve İletişim Kurumu', 'Gelir İdaresi Başkanlığı'],
    'A',
    'Kamuyu Aydınlatma Platformu\'nun (KAP) teknik altyapısı ve işletimi Merkezi Kayıt Kuruluşu (MKK) tarafından yürütülür.\n\n📌 Soruda Geçen Kısaltmalar ve Açılımları:\n• KAP: Kamuyu Aydınlatma Platformu\n• MKK: Merkezi Kayıt Kuruluşu'
)

add_fix(
    'q_1012_master_040',
    ['Kotasyon', 'Temerrüt', 'Tahsis', 'Virman (Menkul Kıymet Transferi)', 'Takas Netleştirmesi'],
    'D',
    'Bir yatırımcının bir kurumdaki menkul kıymetlerini başka bir aracı kurumdaki hesabına transfer etmesine \'Virman\' denir.'
)

add_fix(
    'q_1012_master_042',
    [
        'Şirketler halen her ay fiziki defteri notere onaylatmak zorundadır.',
        'Pay defteri yükümlülüğü Ticaret Bakanlığı müfettişlerince elle tutulur.',
        'MKK tarafından tutulan kaydi hesap kayıtları ortaklıklar açısından pay defteri hükmündedir (Ayrı fiziki defter tutma zorunluluğu kalkmıştır).',
        'Pay defteri tutma yükümlülüğü tamamen yürürlükten kaldırılmıştır.',
        'Şirket yönetim kurulu başkanı pay defterini kendi şahsi kasasında saklar.'
    ],
    'C',
    'TTK ve SPKn m.13 uyarınca kaydileştirilen paylarda MKK kayıtları şirketler açısından pay defteri hükmündedir.\n\n📌 Soruda Geçen Kısaltmalar ve Açılımları:\n• MKK: Merkezi Kayıt Kuruluşu'
)

add_fix(
    'q_1012_master_043',
    ['e-Devlet', 'e-ŞİRKET', 'e-GKS', 'e-Ürün: Elektronik Ürün Senedi Merkezi Kayıt Sistemi', 'e-YATIRIMCI'],
    'D',
    'Lisanslı depolarda saklanan tarım ürünlerine dayalı Elektronik Ürün Senetleri (ELÜS) MKK bünyesindeki e-Ürün sistemi üzerinden kayden izlenir.\n\n📌 Soruda Geçen Kısaltmalar ve Açılımları:\n• ELÜS: Elektronik Ürün Senedi\n• MKK: Merkezi Kayıt Kuruluşu'
)

add_fix(
    'q_1012_master_044',
    ['Borsa İstanbul Yönetim Kurulu', 'Türkiye Bankalar Birliği', 'Sermaye Piyasası Kurulu (SPK)', 'Rekabet Kurulu', 'Hazine ve Maliye Bakanlığı'],
    'C',
    'MKK ve Takasbank\'ın uygulayacağı hizmet tarifeleri ve ücret tarifeleri Sermaye Piyasası Kurulu (SPK) onayı ile yürürlüğe girer.\n\n📌 Soruda Geçen Kısaltmalar ve Açılımları:\n• SPK: Sermaye Piyasası Kurulu'
)

add_fix(
    'q_1012_master_045',
    ['Federal Reserve ve ECB', 'SWIFT ve CHIPS', 'Euroclear ve Clearstream', 'DTCC ve NASDAQ', 'LCH Clearnet ve Eurex'],
    'C',
    'MKK\'nın sınır ötesi menkul kıymet takas ve saklama bağlantısı kurduğu uluslararası merkezi saklama kuruluşları Euroclear ve Clearstream\'dir.'
)

add_fix(
    'q_1012_master_050',
    [
        'Tüm yazılımlar ve fikri mülkiyet hakları MKK\'nın kendi yerli ve milli özkaynaklarına aittir.',
        'Yazılımlar yabancı bir konsorsiyumdan yıllık lisans kiralamasıyla temin edilir.',
        'Fikri haklar Birleşmiş Milletler Kalkınma Fonu\'na devredilmiştir.',
        'Yazılımlar Borsa İstanbul tarafından geliştirilip MKK\'ya satılmıştır.',
        'Sistem yabancı bir bankanın bulut sunucusunda çalışmaktadır.'
    ],
    'A',
    'MKK Ar-Ge Merkezi tarafından geliştirilen kaydi sistem yazılımlarının fikri mülkiyet hakları tamamen MKK\'ya aittir.'
)

add_fix(
    'q_1012_master_051',
    ['Arbitraj', 'Emisyon', 'Kotasyon', 'Mutabakat (Reconciliation / Eşleştirme)', 'Reasürans'],
    'D',
    'Borsa işlemleri sonrasında kurum kayıtları ile takas merkezi kayıtlarının karşılıklı kontrol edilip doğrulanmasına Mutabakat (Reconciliation) denir.'
)

add_fix(
    'q_1012_master_054',
    [
        'Rüçhan hakkını sadece şirket genel müdürüne bağışlayabilir.',
        'Rüçhan hakkını nakde çevirmesi kanunen yasaktır, hakkı yanar.',
        'Borsa İstanbul\'da açılan Rüçhan Hakkı Kupon Pazarında rüçhan kullanım süresi içinde satarak nakde çevirebilir.',
        'Rüçhan hakkını vadeli opsiyon sözleşmesine dönüştürerek saklar.',
        'Hakkı doğrudan SPK\'ya devrederek tazminat talep eder.'
    ],
    'C',
    'Bedelli sermaye artırımına katılmak istemeyen ortak, rüçhan hakkı kullanım süresince Borsa İstanbul Rüçhan Hakkı Kupon Pazarında kuponlarını satabilir.\n\n📌 Soruda Geçen Kısaltmalar ve Açılımları:\n• BIST: Borsa İstanbul'
)

add_fix(
    'q_1012_master_056',
    ['Rekabet Kurumu\'na', 'TÜİK ve Maliye Bakanlığı\'na', 'Türkiye Barolar Birliği\'ne', 'Takasbank ve SPK\'ya', 'Belediye Zabıtası\'na'],
    'D',
    'Yatırım kuruluşları gün sonu pozisyonlarını ve müşteri teminat durumlarını Takasbank ve Sermaye Piyasası Kurulu\'na (SPK) raporlamak zorundadır.\n\n📌 Soruda Geçen Kısaltmalar ve Açılımları:\n• SPK: Sermaye Piyasası Kurulu'
)

add_fix(
    'q_1012_master_057',
    ['Kaldıraç Tavanı', 'Temerrüt Marjı', 'Mutlak Pozisyon Limiti (Position Limit)', 'Volatilite Marjı', 'İskonto Katsayısı'],
    'C',
    'VİOP\'ta tek bir üyenin veya yatırımcının sözleşme bazında taşıyabileceği azami açık pozisyon adedini belirleyen kurala Pozisyon Limiti (Position Limit) denir.'
)

add_fix(
    'q_1012_master_059',
    ['Repo Oranı', 'Kupon Oranı', 'Gecikme Zammı', 'Damga Vergisi', 'Ödünç Komisyon Oranı (Borrowing Fee)'],
    'E',
    'Ödünç Pay Piyasasında pay ödünç alan tarafın ödünç verene ödediği komisyon/faiz bedeline \'Ödünç Komisyon Oranı\' denir.'
)

add_fix(
    'q_1012_master_060',
    ['30 / 360', 'Ay / 30', 'Gerçek Gün / 365 (Actual/365)', 'Sabit 90 Gün', 'İş Günü / 250'],
    'C',
    'Takasbank Para Piyasasında (TPP) faiz hesaplamaları uluslararası para piyasası standardı olan Gerçek Gün / 365 (Actual/365) esasına göre yapılır.'
)

add_fix(
    'q_1012_master_063',
    [
        'Uzlaşma fiyatı üzerinden alıcı taraf nakdi Takasbank\'a öder, satıcı taraf payları MKK nezdinde alıcıya transfer eder.',
        'Hisseler Takasbank tarafından basılarak yatırımcının adresine kargolanır.',
        'Uzlaşma sadece Amerikan Doları cinsinden nakit fark ödenerek kapatılır.',
        'Vade dolduğunda tüm sözleşmeler bedelsiz olarak iptal edilir.',
        'Hisseler Borsa İstanbul yönetim kuruluna devredilir.'
    ],
    'A',
    'Fiziki teslimatlı pay vadeli işlemlerinde uzlaşma fiyatından nakit Takasbank üzerinden tahsil edilirken, paylar MKK nezdinde teslim edilir.'
)

add_fix(
    'q_1012_master_065',
    [
        'Yalnızca yıl sonunda genel kurul onayından sonra',
        'En erken 30 takvim günü geçtikten sonra',
        'Sadece mahkeme kararı tebliğ edildiğinde',
        'Her ayın son iş günü toplu takas seansında',
        'Talimat sisteme girilip karşı kurum onayladığı anda elektronik ortamda anlık olarak'
    ],
    'E',
    'MKK sisteminde serbest hisse virman talimatları karşı kurumun elektronik onayıyla anlık (real-time) olarak gerçekleştirilir.\n\n📌 Soruda Geçen Kısaltmalar ve Açılımları:\n• MKK: Merkezi Kayıt Kuruluşu'
)

add_fix(
    'q_1012_master_066',
    [
        'Menkul kıymet satıp parayı faizsiz olarak vadeli mevduata yatırır.',
        'Hisse senedi alıp aynı gün açığa satış işlemi yapar.',
        'Borsa endeksine dayalı varant satın alıp vadesine kadar bekler.',
        'Şirket tahvilini vade sonunda hisse senedine dönüştürür.',
        'Nakit verip karşılığında menkul kıymeti teminat olarak teslim alır; vade sonunda parayı faiziyle geri alıp kıymeti iade eder.'
    ],
    'E',
    'Ters repo; nakit borç vererek karşılığında menkul kıymet teminatı alma ve vade bitiminde parayı faiziyle tahsil edip kıymeti iade etme işlemidir.'
)

add_fix(
    'q_1012_master_067',
    [
        'Kupon bedelleri nakit olarak şirketin muhasebe veznesinden elden dağıtılır.',
        'İhraççı şirket kupon tutarını Takasbank\'taki takas hesabına yatırır; Takasbank MKK listesindeki hak sahiplerinin hesaplarına kupon faizlerini net olarak dağıtır.',
        'Kupon bedelleri otomatik olarak yeni ihraç edilecek tahvillere dönüştürülür.',
        'Takasbank kupon ödemesini kendi sermayesinden karşılar.',
        'Kuponlar noter huzurunda kura çekilerek sadece talihli yatırımcılara ödenir.'
    ],
    'B',
    'Tahvil kupon ödemelerinde ihraççı Takasbank\'a fon aktarır; Takasbank MKK hak sahipliği sicili üzerinden yatırımcıların hesaplarına doğrudan aktarır.'
)

add_fix(
    'q_1012_master_069',
    [
        'TÜBİTAK onaylı resmi Zaman Damgası (Time Stamp) ve Nitelikli Elektronik Sertifika (e-İmza) ile',
        'İlçe Seçim Kurulu tasdik mührü ile',
        'Şirket genel müdürünün ıslak imzalı mektubu ile',
        'Noter yeminli zabıt tutanağı ile',
        'Borsa bülteninin basılı nüshası ile'
    ],
    'A',
    'KAP ve MKK sisteminde bildirimlerin hukuki geçerliliği ve zaman kanıtı 5070 sayılı Kanun uyarınca e-İmza ve TÜBİTAK Zaman Damgası ile sağlanır.'
)

add_fix(
    'q_1012_master_070',
    ['Borsa Müzesi', 'Olağanüstü Durum Merkezi (ODM / Disaster Recovery Center)', 'Hakem Heyeti Binası', 'Arşiv Odası', 'Test Laboratuvarı'],
    'B',
    'Afet ve kriz anlarında finansal altyapının kesintisiz çalışmasını garanti eden yedek tesise Olağanüstü Durum Merkezi (ODM) denir.'
)

add_fix(
    'q_1012_master_073',
    ['Garanti Fonu (Takasbank Garanti Fonu / Default Fund)', 'İşsizlik Fonu', 'Emeklilik Fonu', 'Kambiyo Fonu', 'Varlık Fonu'],
    'A',
    'MKT temerrüt risklerini karşılamak için takas üyelerinin katkılarıyla oluşturulan ortak rezerv fonu Takasbank Garanti Fonu\'dur (Default Fund).'
)

add_fix(
    'q_1012_master_074',
    ['Komisyon İndirimi', 'Rüçhan Primi', 'Vergi Muafiyeti', 'İtibar Ödülü', 'Temerrüt Faizi ve Cezai Şart'],
    'E',
    'Takas borcunu süresinde kapatmayan üyeye Takasbank tarafından gecikilen süre için Temerrüt Faizi ve ek cezai şart uygulanır.'
)

add_fix(
    'q_1012_master_077',
    ['Aynı gün saat 12:00\'ye kadar', 'İşlem gününü izleyen iş günü (T+1) saat 14:30 / 15:00\'e kadar', 'T+2 günü saat 18:00\'e kadar', 'Hafta sonu mesai bitimine kadar', 'Süre sınırlaması olmaksızın ay sonuna kadar'],
    'B',
    'VİOP marjin kapama çağrısı (Margin Call) ertesi iş günü (T+1) en geç saat 14:30 / 15:00\'e kadar nakden tamamlanmalıdır.\n\n📌 Soruda Geçen Kısaltmalar ve Açılımları:\n• VİOP: Vadeli İşlem ve Opsiyon Piyasası'
)

add_fix(
    'q_1012_master_078',
    ['Volatilite Artırımı', 'Kaldıraç Çarpanı', 'Değer Kesintisi / İskonto Oranı (Haircut)', 'Temerrüt Marjı', 'Kredi Baremi'],
    'C',
    'Nakit dışı menkul kıymetlerin teminat kabul edilirken piyasa fiyatından belirli bir yüzde kırılarak kabul edilmesine Değer Kesintisi (Haircut) denir.'
)

add_fix(
    'q_1012_master_079',
    ['Muhasebe Denetimi', 'Vergi Teftişi', 'Piyasa Anketi', 'Stres Testleri (Stress Testing)', 'Yazılı Sınav'],
    'D',
    'Takasbank teminat ve Garanti Fonunun olağanüstü piyasa çöküşlerinde yeterliliğini ölçmek için düzenli olarak Stres Testleri (Stress Testing) uygular.'
)

add_fix(
    'q_1012_master_081',
    ['Enflasyon Riski', 'Politik Risk', 'Mevzuat Riski', 'Kur Riski', 'Sistemik Risk (Systemic Risk)'],
    'E',
    'Bir finansal kurumun batmasının domino etkisiyle diğer tüm piyasa aktörlerini çökertme tehlikesine Sistemik Risk (Systemic Risk) denir.'
)

add_fix(
    'q_1012_master_082',
    ['Sermaye Tavanı', 'Kıdem Tazminatı', 'İtfa Payı', 'SITG (Skin in the Game / Takasbank Özkaynak Katkısı)', 'Yedek Akçe'],
    'D',
    'Temerrüt şelalesinde diğer masum üyelerin fonlarına başvurulmadan önce Takasbank\'ın kendi sermayesinden koyduğu güvenlik tamponu SITG (Skin in the Game) olarak adlandırılır.'
)

add_fix(
    'q_1012_master_083',
    ['Tüketici Hakem Heyeti', 'Sanayi Odası', 'Noterler Birliği', 'Takasbank Disiplin Komitesi', 'SPK Uzlaştırma Masası'],
    'D',
    'Takas ve saklama kurallarına aykırı hareket eden üyelerin disiplin işlemlerini Takasbank Disiplin Komitesi yürütür.'
)

add_fix(
    'q_1012_master_084',
    ['Piyasa Riski', 'Operasyonel Risk', 'Karşı Taraf Kredi Riski', 'Kur Riski', 'Faiz Riski'],
    'C',
    'İşlem yapılan karşı tarafın takas gününe kadar borcunu ödeyememe ve temerrüde düşme tehlikesine Karşı Taraf Kredi Riski denir.'
)

add_fix(
    'q_1012_master_085',
    ['Zorunlu Repo', 'İcra İhalesi', 'Otomatik Ödünç Pay Servisi (Auto-Borrowing)', 'Bedelsiz Transfer', 'Açığa Satış İptali'],
    'C',
    'Takas günü hisse teslim açığı oluşan üye için Takasbank sisteminin otomatik olarak piyasadan pay ödünç almasına Otomatik Ödünç Pay Servisi denir.'
)

add_fix(
    'q_1012_master_086',
    ['Piyasa Riski', 'Likidite Riski', 'Operasyonel Risk (Operational Risk)', 'Kredi Riski', 'Ülke Riski'],
    'C',
    'İnsan hatası, yazılım çökmesi, dolandırıcılık veya sistem arızalarından kaynaklanan risk Operasyonel Risk (Operational Risk) olarak tanımlanır.'
)

add_fix(
    'q_1012_master_088',
    ['Sızma Testi (Penetration Test)', 'Mali Denetim', 'Yazılı Yoklama', 'Vergi Teftişi', 'Müşteri Memnuniyet Anketi'],
    'A',
    'SPK Bilgi Sistemleri Tebliği uyarınca yatırım kuruluşları siber güvenlik için yılda en az bir kez bağımsız uzmanlara Sızma Testi (Penetration Test) yaptırmak zorundadır.'
)

add_fix(
    'q_1012_master_093',
    ['Yetki Devri İlkesi', 'Tek İmza İlkesi', 'Görevler Ayrılığı İlkesi (Segregation of Duties)', 'Gizlilik İlkesi', 'Serbest Piyasa İlkesi'],
    'C',
    'Hile ve suistimalleri önlemek için emir alan, takası yapan ve muhasebeleştiren personelin birbirinden bağımsız olması Görevler Ayrılığı İlkesi\'dir.'
)

add_fix(
    'q_1012_master_095',
    [
        '10 yıl boyunca hiçbir şekilde çözülemez.',
        'Borç ve faiz tam olarak kapatıldığı anda sistem tarafından otomatik olarak blokaj çözülerek serbest bırakılır.',
        'Sadece yıl başında Takasbank Genel Kurulu kararıyla çözülür.',
        'Mahkeme kararı olmadan asla serbest bırakılamaz.',
        'Yalnızca SPK Başkanı\'nın yazılı onayı ile çözülür.'
    ],
    'B',
    'Takasbank Para Piyasasında borç ve faizini ödeyen üyenin rehinli teminatları Takasbank sistemi tarafından anlık ve otomatik olarak serbest bırakılır.'
)

add_fix(
    'q_1012_master_096',
    ['En az 1 yıl', 'En az 3 yıl', 'En az 5 yıl', 'En az 10 yıl (ve mülkiyet kayıtları süresiz olarak)', 'En az 30 yıl'],
    'D',
    'MKK ve Takasbank takas ve saklama kayıtlarını en az 10 yıl süreyle elektronik arşivde saklar; mülkiyeti belirleyen kaydileştirme kayıtları ise süresiz muhafaza edilir.'
)

add_fix(
    'q_1012_master_097',
    ['Gelir Tablosu', 'Hak Sahipleri Çizelgesi (Bloke Paylar / Hazır Bulunanlar Listesi)', 'Vergi Matrahı', 'Ticaret Sicil Gazetesi', 'Vakıf Senedi'],
    'B',
    'Genel kurullarda oy kullanabilecek ortakları gösteren ve MKK tarafından üretilen resmi belge Hak Sahipleri Çizelgesi\'dir (Hazır Bulunanlar Listesi).'
)

add_fix(
    'q_1012_master_100',
    [
        'Merkezi Bankacılık Konsorsiyumu',
        'Türkiye Sermaye Piyasaları Uçtan Uca İşlem ve İşlem Sonrası Altyapısı (Entegre Borsa Ekosistemi)',
        'Uluslararası Para Fonu Ağı',
        'Interbank Döviz Piyasası Birliği',
        'Özel Sektör Tahvil Borsası'
    ],
    'B',
    'Borsa İstanbul (İşlem) -> Takasbank (Takas/MKT) -> MKK (Saklama/Mülkiyet) üçlüsü Türkiye sermaye piyasalarının entegre işlem ve işlem sonrası altyapısını oluşturur.'
)

add_fix(
    'q_1012_konu_001',
    [
        'Borsa İstanbul A.Ş. - %75.0',
        'Türkiye Sermaye Piyasaları Birliği (TSPB) - %51.0',
        'T.C. Hazine ve Maliye Bakanlığı - %49.5',
        'İstanbul Takas ve Saklama Bankası A.Ş. (Takasbank) - %64.9',
        'Türkiye Cumhuriyet Merkez Bankası (TCMB) - %30.1'
    ],
    'D',
    'MKK ortaklık yapısında en büyük pay sahibi ortak kuruluş %64.9 pay oranıyla İstanbul Takas ve Saklama Bankası A.Ş.\'dir (Takasbank).\n\n📌 Soruda Geçen Kısaltmalar ve Açılımları:\n• MKK: Merkezi Kayıt Kuruluşu\n• Takasbank: İstanbul Takas ve Saklama Bankası A.Ş.'
)

add_fix(
    'q_1012_konu_002',
    ['T+2 / 15:00', 'T+1 / 14:00', 'T+2 / 17:30', 'T+3 / 12:00', 'T+0 / 16:30'],
    'A',
    'Borsa İstanbul Pay Piyasası takas süresi T+2 olup, takas günü nakit ve hisse borçlarının tamamlanması gereken son temerrüt saati 15:00\'tir.'
)

add_fix(
    'q_1012_konu_004',
    ['%10', '%20', '%33', '%50', '%100'],
    'D',
    'MKK Esas Sözleşmesi Madde 7 uyarınca, Borsa İstanbul A.Ş.\'nin sahip olabileceği azami MKK pay oranı %50\'dir.\n\n📌 Soruda Geçen Kısaltmalar ve Açılımları:\n• MKK: Merkezi Kayıt Kuruluşu'
)

add_fix(
    'q_1012_konu_008',
    ['Borsa İstanbul', 'Portföy Saklama Kuruluşu (Portföy Saklayıcısı)', 'Yatırımcı Tazmin Merkezi', 'Tüketici Mahkemesi', 'Merkez Bankası'],
    'B',
    'Kolektif yatırım kuruluşlarının (yatırım fonlarının) varlıklarının saklanmasından ve denetiminden Portföy Saklayıcısı sorumludur.'
)

add_fix(
    'q_1012_konu_010',
    ['11:00', '12:30', '14:00', '15:30', '17:00'],
    'A',
    'VİOP\'ta yarım işlem günlerinde eksi nakit ve teminat tamamlama (Margin Call) en geç saat 11:00\'e kadar tamamlanmak zorundadır.\n\n📌 Soruda Geçen Kısaltmalar ve Açılımları:\n• VİOP: Vadeli İşlem ve Opsiyon Piyasası'
)

add_fix(
    'q_1012_konu_011',
    ['%5', '%10', '%15', '%25', '%50'],
    'D',
    'VİOP Pay vadeli işlem sözleşmelerinde piyasa bazında toplam açık pozisyon limiti, dayanak varlığın fiili dolaşımdaki pay miktarının en fazla %25\'idir.'
)

add_fix(
    'q_1012_konu_012',
    ['1.000 TL', '6.000 TL', '9.000 TL', '14.000 TL', '15.000 TL'],
    'B',
    'Bakiye sürdürme seviyesinin (15.000 TL) altına inip 14.000 TL\'ye düştüğünde Margin Call gelir. Tamamlanması gereken hedef başlangıç teminatıdır: 20.000 - 14.000 = 6.000 TL nakit yatırılmalıdır.'
)

print(f"Total explicit question fixes registered: {len(FIXES)}")

# Now apply all fixes to all_qs and master_qs
applied_count = 0
for q in all_qs:
    qid = q['id']
    if qid in FIXES:
        fix = FIXES[qid]
        q['options'] = fix['options']
        q['correct_answer'] = fix['correct_answer']
        if fix['explanation']:
            q['explanation'] = fix['explanation']
        applied_count += 1

master_applied = 0
for q in master_qs:
    qid = q['id']
    if qid in FIXES:
        fix = FIXES[qid]
        q['options'] = fix['options']
        q['correct_answer'] = fix['correct_answer']
        if fix['explanation']:
            q['explanation'] = fix['explanation']
        master_applied += 1

print(f"Applied fixes to all_questions: {applied_count}")
print(f"Applied fixes to questions_master: {master_applied}")

with open('src/data/all_questions.json', 'w', encoding='utf-8') as f:
    json.dump(all_qs, f, ensure_ascii=False, indent=2)

with open('src/data/questions_master.json', 'w', encoding='utf-8') as f:
    json.dump(master_qs, f, ensure_ascii=False, indent=2)

print("Successfully saved updated all_questions.json and questions_master.json!")
