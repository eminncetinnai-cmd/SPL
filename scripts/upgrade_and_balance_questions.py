import json
import random
import re
import sys
from collections import Counter, defaultdict

sys.stdout.reconfigure(encoding='utf-8')

# Set fixed seed for reproducibility
random.seed(42)

with open('src/data/all_questions.json', 'r', encoding='utf-8') as f:
    all_qs = json.load(f)

print(f"Loaded {len(all_qs)} questions.")

# High quality SPK legal and financial distractor pools by module
DISTRACTORS = {
    '1012': [
        "Merkezi Kayıt Kuruluşu (MKK) nezdindeki hak sahipliği sicil kayıtlarının eşzamanlı güncellenmesi",
        "Takasbank Para Piyasası (TPP) nezdinde teminatların üç katı oranında bloke edilmesi",
        "Takasbank'ın Doğrudan Borçlandırma Sistemi (DBS) üzerinden gün içi likidite tahsis etmesi",
        "Merkezi Karşı Taraf (CCP) sıfatıyla alıcıya karşı satıcı, satıcıya karşı alıcı konumuna geçilmesi",
        "Yatırımcı Tazmin Merkezi (YTM) tarafından zamanaşımına uğrayan alacakların Hazine'ye aktarılması",
        "Takas Süresi T+2 olup nakit ve menkul kıymet borçlarının çoklu netleştirme ile tasfiyesi",
        "Ödünç Pay Piyasası'nda (ÖPA) belirlenen özkaynak oranının %100'ün altına düşmesi halinde temerrüt bildirimi yapılması",
        "Borsa İstanbul Pay Piyasası takas işlemlerinde teslim karşılığı ödeme (DVP - Delivery Versus Payment) kuralının işletilmesi",
        "Takasbank Garanti Fonu katkı paylarının ilgili üye aracı kurum tarafından seans öncesinde yatırılması",
        "Hak kullanım süreçlerinde (temettü, bedelli, rüçhan) MKK ihraççı havuz hesaplarının blokaj altına alınması",
        "Kolektif Yatırım Kuruluşları saklama hizmeti veren portföy saklayıcısının üçer aylık mutabakat raporları",
        "Sermaye Piyasası Kurulu'nun takas esaslarına ilişkin tip sözleşmelerde yer alan genel işlem şartları",
        "BİSTPAY ödeme sistemi üzerinden yapılan EFT ve havale mutabakatlarının seans bitiminde kesinleşmesi",
        "Üyelerin Takasbank nezdindeki nakit hesaplarının rehin ve temlik edilemez varlık niteliğinde korunması",
        "Kıymetli Madenler ve Kıymetli Taşlar Piyasası fiziki teslimatlarının Takasbank özel kasalarında saklanması",
        "Kaldıraçlı işlemler müşteri teminatlarının aracı kurumun kendi aktiflerinden fiziki ve hesaben ayrı tutulması",
        "Takas alacaklısı üyenin pay teslim borcunu yerine getirmeyen üyeye karşı temerrüt faizi işletmesi",
        "Yurt dışı saklama kuruluşları (Euroclear, Clearstream) ile kurulan omnibus saklama hesapları bağlantısı",
        "Elektronik Ürün Senedi (ELÜS) işlemlerinin Türkiye Ürün İhtisas Borsası takas kurallarına tabi olması",
        "Takas netleştirmesi neticesinde oluşan menkul kıymet açığının temerrüt pazarında kapatılması zorunluluğu"
    ],
    '1005': [
        "Geniş Yetkili Aracı Kurum asgari özsermaye tabanının Kurul düzenlemelerine uygun olarak 150 milyon TL'ye yükseltilmesi",
        "Kısmi Yetkili Aracı Kurumların yalnızca en iyi gayret aracılığı ve emir iletimi faaliyetinde bulunabilmesi",
        "Müşterinin Genel Müşteri veya Profesyonel Müşteri olarak sınıflandırılması ve Yerindelik Testi yapılması",
        "Portföy aracılığı yetki belgesi bulunmayan kurumların kendi nam ve hesabına işlem yapmasının yasaklanması",
        "Kredili menkul kıymet alımı ve açığa satış işlemlerinde asgari %35 başlangıç özkaynak oranının korunması",
        "Aracı kurum genel müdür ve müdür yardımcılarının SPK Düzey 3 ve Türev Araçlar Lisansı sahibi olması zorunluluğu",
        "İç denetim ve teftiş raporlarının yılda en az bir kez Yönetim Kurulu'na ve Kurul'a sunulması",
        "Müşteri emirlerinin zaman önceliği kuralına tabi olarak Borsa işlem sistemine iletilmesi",
        "Kaldıraçlı alım satım işlemlerinde (FX) maksimum kaldıraç oranının 1:10 ile sınırlandırılması",
        "Aracı kurumun özsermaye yeterliliği tabanının risk karşılıkları toplamından düşük olmaması şartı",
        "Yatırım danışmanlığı sözleşmesi imzalanmadan müşteriye özel portföy yönlendirmesi yapılmasının yasak olması",
        "Müşteri nakitlerinin aracı kurum hesaplarından ayrı olarak Takasbank nezdinde müşteri bazında nemalandırılması",
        "Bağımsız denetim kuruluşları tarafından altı aylık ve yıllık ara mali tabloların denetime tabi tutulması",
        "Aracı kurum yönetim kurulu üyelerinin çoğunluğunun icracı olmayan bağımsız üyelerden teşekkül etmesi",
        "Merkez dışı örgütlerin (şube ve irtibat bürosu) açılabilmesi için SPK'dan önceden izin alınması zorunluluğu",
        "Finansal Duran Varlıklar tebliği uyarınca aracı kurumun iştirak sınırlarının özkaynağın %25'ini aşamaması",
        "Müşteri sırrı ve ticari sır niteliğindeki bilgilerin üçüncü şahıslara veya grup şirketlerine aktarılamaması",
        "Aracı kurumun likidite yükümlülüğü oranının belirlenen minimum standart rasyonun üzerinde tutulması",
        "İç kontrolden sorumlu personelin doğrudan aracı kurum Yönetim Kurulu'na bağlı olarak görev yapması",
        "Çıkar çatışması politikası gereğince analist raporlarının yayımlanmadan önce ilgili ihraççıya iletilmemesi"
    ],
    '1003': [
        "Pay sahiplerine tanınan yeni pay alma hakkının (rüçhan hakkı) kullanım süresinin en az 15, en fazla 60 gün olması",
        "Varlığa Dayalı Menkul Kıymetlerin (VDMK) Fon Kurulu tarafından yönetilen bağımsız bir varlık teminatına dayanması",
        "Kira sertifikalarında (Sukuk) mülkiyete dayalı (İcare) veya yönetim sözleşmesine dayalı getiri yapısı kurulması",
        "VİOP bünyesinde işlem gören pay vadeli işlem sözleşmelerinde fiziki veya nakdi uzlaşma esaslarının geçerli olması",
        "İpotek Teminatlı Menkul Kıymetlerin (İTMK) ihraç limitinin ihraççının özkaynak büyüklüğü ile sınırlandırılması",
        "Varantlarda ihraçcının piyasa yapıcı sıfatıyla sürekli likidite ve kotasyon sağlama taahhüdü altında bulunması",
        "Yatırım fonu katılma paylarının net aktif değer (NAD) üzerinden günlük fiyatlanması ve TEFAS'ta işlem görmesi",
        "Katılma İntifa Senetlerinin (KİS) şirket sermayesinde pay temsil etmeksizin yalnızca kardan pay alma hakkı tanıması",
        "Borsa yatırım fonlarının (BYF) dayanak endeksi asgari %95 korelasyon ile birebir takip etme zorunluluğu",
        "Eurobond ihraçlarında yurt dışı yerleşiklere satış zorunluluğu ve kupon ödemelerinin yabancı para cinsinden yapılması",
        "Paylara dönüştürülebilir tahvillerin (PDT) vadesinde hisse senedi veya nakit olarak itfa edilebilme opsiyonu",
        "Hazine Müsteşarlığı Varlık Kiralama Şirketi tarafından ihraç edilen DİBS niteliğindeki kamu kira sertifikaları",
        "Gelir Ortaklığı Senetlerinin (GOS) köprü, otoyol, baraj gibi kamu altyapı tesislerinin gelirlerine endekslenmesi",
        "Gayrimenkul Yatırım Ortaklıklarının (GYO) portföylerinin en az %51'ini gayrimenkul ve gayrimenkule dayalı haklardan oluşturması",
        "Girişim Sermayesi Yatırım Fonlarının (GSYF) yalnızca Nitelikli Yatırımcılara satılabilen kapalı uçlu fon niteliği taşıması"
    ],
    '1001': [
        "6362 sayılı Sermaye Piyasası Kanunu uyarınca izahnamenin geçerlilik süresinin onay tarihinden itibaren 12 ay olması",
        "Halka açık ortaklıklarda ilişkili taraf işlemlerinin bağımsız yönetim kurulu üyelerinin çoğunluk oyuyla onaylanması",
        "İçeriden öğrenenlerin ticareti (insider trading) suçunda 2 yıldan 5 yıla kadar hapis veya adli para cezası öngörülmesi",
        "Özel durum açıklamalarının (KAP) menfi veya müspet bilginin öğrenilmesini takip eden en geç ertesi iş günü yapılması zorunluluğu",
        "Piyasa dolandırıcılığı (manipülasyon) eylemlerinde etkin pişmanlık hükümlerinden faydalanılabilmesi için elde edilen menfaatin iadesi",
        "Ortaklıktan çıkarma ve satma haklarının kullanılabilmesi için hakim ortaklık pay oranının asgari %98'e ulaşmış olması şartı",
        "Kurul'un idari para cezası kararlarına karşı 30 gün içinde yetkili İdare Mahkemesi nezdinde iptal davası açılabilmesi",
        "Kayıtlı sermaye sisteminde yönetim kuruluna verilen sermaye artırma yetkisinin azami 5 yıl ile sınırlandırılmış olması",
        "Önemli nitelikteki işlemlere muhalefet şerhi koyduran pay sahiplerinin adil bedel üzerinden ayrılma hakkını kullanabilmesi",
        "Sermaye Piyasası Kurulu üyelerinin Cumhurbaşkanı tarafından beş yıllık süre için atanması ve bağımsızlığı güvencesi",
        "Halka arzlarda konsorsiyum lideri aracı kurumun fiyat istikrarı işlemlerini en fazla 30 gün boyunca sürdürebilmesi",
        "Finansal raporların TMS/TFRS standartlarına tam uyumlu olarak bağımsız denetimden geçmiş haliyle ilan edilmesi zorunluluğu"
    ]
}

# Absurd/weak distractor patterns to purge
BAD_PATTERNS = [
    r'noter', r'döviz büro', r'fabrika', r'belediye', r'birleşmiş millet', 
    r'harç öden', r'kiralanmasıdır', r'kamu bakanlığı', r'vakıftır', 
    r'zararını devlet adına', r'her yatırımcıya getiri garantisi', 
    r'tüm ticari sırlarını', r'birbirine tavsiye vermesini', 
    r'en kıdemsiz', r'10 gün beklet', r'sadece yabancı para ile',
    r'tek başına satın', r'hiçbir koşulda kısıtlanamaz', r'küçük - orta - büyük',
    r'yerel - bölgesel - ulusal', r'a tipi - b tipi - c tipi', r'kamu - özel - yabancı',
    r'sigorta şirketleri ve noterler', r'ticaret odaları ve sanayi odaları'
]

def is_bad_distractor(text):
    t = text.lower()
    for p in BAD_PATTERNS:
        if re.search(p, t):
            return True
    if len(text.strip()) < 12:
        return True
    return False

# Function to balance and upgrade questions
def upgrade_question(q, target_key):
    mod = q.get('module_id', '1001')
    source = q.get('source', 'master')
    
    # 1. Identify the current correct option text
    current_correct_key = q['correct_answer']
    correct_text = None
    existing_wrong_texts = []
    
    for opt in q['options']:
        if opt['key'] == current_correct_key:
            correct_text = opt['text'].strip()
        else:
            txt = opt['text'].strip()
            if not is_bad_distractor(txt):
                existing_wrong_texts.append(txt)
    
    if not correct_text:
        correct_text = q['options'][0]['text'].strip()
        
    # 2. Get replacement distractors if needed
    pool = DISTRACTORS.get(mod, DISTRACTORS['1001'])
    # Filter out pool items that are too similar to correct text
    available_replacements = [d for d in pool if d.lower() != correct_text.lower() and d not in existing_wrong_texts]
    random.shuffle(available_replacements)
    
    # We need 4 distinct wrong options
    final_wrong = []
    for w in existing_wrong_texts:
        if len(final_wrong) < 4 and w not in final_wrong and w.lower() != correct_text.lower():
            final_wrong.append(w)
            
    while len(final_wrong) < 4 and available_replacements:
        cand = available_replacements.pop()
        if cand not in final_wrong and cand.lower() != correct_text.lower():
            final_wrong.append(cand)
            
    # Fallback if still under 4
    if len(final_wrong) < 4:
        fallback_pool = DISTRACTORS['1001'] + DISTRACTORS['1005']
        for cand in fallback_pool:
            if len(final_wrong) >= 4:
                break
            if cand not in final_wrong and cand.lower() != correct_text.lower():
                final_wrong.append(cand)

    # 3. Form 5 options with target_key as correct
    keys = ['A', 'B', 'C', 'D', 'E']
    wrong_keys = [k for k in keys if k != target_key]
    
    new_options = []
    for k in keys:
        if k == target_key:
            new_options.append({"key": k, "text": correct_text})
        else:
            w_txt = final_wrong.pop(0) if final_wrong else f"{k} seçeneği mevzuat koşulu"
            new_options.append({"key": k, "text": w_txt})
            
    q['options'] = new_options
    q['correct_answer'] = target_key
    
    # 4. Update explanation if it references old letter
    # e.g., "Doğru cevap A şıkkıdır" -> "Doğru cevap {target_key} şıkkıdır"
    expl = q.get('explanation', '')
    expl = re.sub(r'([Dd]oğru\s+cevap\s+)[A-E](\s+şık)', rf'\g<1>{target_key}\g<2>', expl)
    q['explanation'] = expl
    
    return q

# Process all questions by group
keys_cycle = ['A', 'B', 'C', 'D', 'E']

# Group questions by (module_id, source)
groups = defaultdict(list)
cikmis_qs = []

for q in all_qs:
    if q.get('source') == 'cikmis':
        cikmis_qs.append(q)
    else:
        groups[(q['module_id'], q.get('source', 'master'))].append(q)

upgraded_qs = []

for (mod, src), q_list in groups.items():
    print(f"Upgrading Module {mod} - Source {src} ({len(q_list)} questions)...")
    # Shuffle the list to randomize which question gets which key
    random.shuffle(q_list)
    for idx, q in enumerate(q_list):
        assigned_key = keys_cycle[idx % 5]
        upgraded_q = upgrade_question(q, assigned_key)
        upgraded_qs.append(upgraded_q)

# Put back together
final_qs = []
# Keep original order structure: master, konu, ogretici, cikmis
for q in all_qs:
    if q.get('source') == 'cikmis':
        final_qs.append(q)
    else:
        # Find the upgraded version by id
        u = next((item for item in upgraded_qs if item['id'] == q['id']), q)
        final_qs.append(u)

print("\n=== VERIFYING ANSWER DISTRIBUTION AFTER UPGRADE ===")
for src in ['master', 'ogretici', 'konu', 'cikmis']:
    src_qs = [q for q in final_qs if q.get('source') == src]
    dist = Counter(q['correct_answer'] for q in src_qs)
    print(f"Source: {src:<10} (Count: {len(src_qs)}) -> {dict(sorted(dist.items()))}")

print("\n=== BREAKDOWN BY MODULE FOR MASTER ===")
for mod in ['1001', '1003', '1005', '1012']:
    mod_master = [q for q in final_qs if q['module_id'] == mod and q.get('source') == 'master']
    dist = Counter(q['correct_answer'] for q in mod_master)
    print(f"Module {mod} Master (Count: {len(mod_master)}) -> {dict(sorted(dist.items()))}")

print("\n=== BREAKDOWN FOR OGRETICI (ALL 4 MODULES) ===")
ogretici_list = [q for q in final_qs if q.get('source') == 'ogretici']
dist = Counter(q['correct_answer'] for q in ogretici_list)
print(f"Ogretici Bank (Count: {len(ogretici_list)}) -> {dict(sorted(dist.items()))}")

# Save updated files
with open('src/data/all_questions.json', 'w', encoding='utf-8') as f:
    json.dump(final_qs, f, ensure_ascii=False, indent=2)

with open('src/data/questions_master.json', 'w', encoding='utf-8') as f:
    json.dump([q for q in final_qs if q.get('source') == 'master'], f, ensure_ascii=False, indent=2)

print("\nSuccessfully saved all_questions.json and questions_master.json!")
