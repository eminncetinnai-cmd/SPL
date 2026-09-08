import json
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('src/data/all_questions.json', 'r', encoding='utf-8') as f:
    qs = json.load(f)

print(f"Total questions in database: {len(qs)}")

problematic_ids = set()
details = []

# List of all pasted boilerplate phrases from the previous session's scripts
BOILERPLATE_SUBSTRINGS = [
    "Hazine Müsteşarlığı Varlık Kiralama",
    "Kira sertifikalarında (Sukuk) mülkiyete",
    "Katılma İntifa Senetlerinin (KİS)",
    "VİOP bünyesinde işlem gören pay vadeli",
    "Varlığa Dayalı Menkul Kıymetlerin (VDMK) Fon",
    "Özel durum açıklamalarının (KAP) menfi",
    "Gelir Ortaklığı Senetlerinin (GOS)",
    "Girişim Sermayesi Yatırım Fonlarının (GSYF)",
    "Borsa yatırım fonlarının (BYF) dayanak",
    "Halka açık ortaklıklarda ilişkili taraf işlemlerinin",
    "Kayıtlı sermaye sisteminde yönetim kuruluna verilen",
    "Ortaklıktan çıkarma ve satma haklarının kullanılabilmesi için",
    "Kurul'un idari para cezası kararlarına karşı",
    "Piyasa dolandırıcılığı (manipülasyon) eylemlerinde etkin pişmanlık",
    "İçeriden öğrenenlerin ticareti (insider trading) suçunda",
    "Paylara dönüştürülebilir tahvillerin (PDT)",
    "Takas alacaklısı üyenin pay teslim borcunu",
    "Hak kullanım süreçlerinde (temettü, bedelli, rüçhan)",
    "Kıymetli Madenler ve Kıymetli Taşlar Piyasası fiziki teslimatlarının",
    "BİSTPAY ödeme sistemi üzerinden yapılan",
    "Elektronik Ürün Senedi (ELÜS) işlemlerinin Türkiye Ürün",
    "Takasbank'ın Doğrudan Borçlandırma Sistemi (DBS)",
    "Takasbank Para Piyasası (TPP) nezdinde teminatların",
    "Ödünç Pay Piyasası'nda (ÖPA) belirlenen özkaynak",
    "Sermaye Piyasası Kurulu'nun takas esaslarına ilişkin tip sözleşmelerde",
    "Kolektif Yatırım Kuruluşları saklama hizmeti veren",
    "Kaldıraçlı işlemler müşteri teminatlarının aracı kurumun kendi aktiflerinden",
    "Üyelerin Takasbank nezdindeki nakit hesaplarının rehin ve temlik",
    "Yurt dışı saklama kuruluşları (Euroclear, Clearstream)",
    "Borsa İstanbul Pay Piyasası takas işlemlerinde teslim karşılığı ödeme",
    "Takas netleştirmesi neticesinde oluşan menkul kıymet açığının",
    "Merkezi Kayıt Kuruluşu (MKK) nezdindeki hak sahipliği sicil",
    "Yatırımcı Tazmin Merkezi (YTM) tarafından zamanaşımına",
    "Takas Süresi T+2 olup nakit ve menkul kıymet"
]

for q in qs:
    opts = [o['text'].strip() for o in q['options']]
    lens = [len(o) for o in opts]
    
    # Check 1: Boilerplate distractor present
    has_bp = any(any(bp in o for bp in BOILERPLATE_SUBSTRINGS) for o in opts)
    if has_bp:
        problematic_ids.add(q['id'])
        details.append((q['id'], q['module_id'], 'Has boilerplate distractor', q['text'][:60], opts))
        continue
        
    # Check 2: Extreme length or type asymmetry
    # (e.g. 1 option < 12 chars while 4 options > 40 chars, or 1 option > 70 chars while 4 options < 20 chars)
    min_len = min(lens)
    max_len = max(lens)
    
    # Case A: exactly 1 number/short option among long narrative options
    is_numeric = [bool(re.match(r'^[%0-9\.,\s\+T\-:\(\)]+$', o)) for o in opts]
    if sum(is_numeric) == 1 and all(len(opts[i]) > 35 for i in range(5) if not is_numeric[i]):
        problematic_ids.add(q['id'])
        details.append((q['id'], q['module_id'], 'Single numeric among 4 long texts', q['text'][:60], opts))
        continue
        
    # Case B: 4 short terms (e.g. 10-15 chars) and 1 giant narrative sentence (>70 chars)
    if max_len > 60 and sum(1 for l in lens if l < 25) >= 4:
        problematic_ids.add(q['id'])
        details.append((q['id'], q['module_id'], 'Single long sentence among 4 short terms', q['text'][:60], opts))
        continue

print(f"\nTotal problematic questions identified: {len(problematic_ids)}")
from collections import Counter
mod_counts = Counter(d[1] for d in details)
print("Breakdown by module:", mod_counts)

with open('scripts/all_problematic_questions.json', 'w', encoding='utf-8') as f:
    json.dump([q for q in qs if q['id'] in problematic_ids], f, ensure_ascii=False, indent=2)

print("Saved all problematic questions to scripts/all_problematic_questions.json")
