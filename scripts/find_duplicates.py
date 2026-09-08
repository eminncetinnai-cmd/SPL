import json
import re
import sys
from collections import defaultdict
from difflib import SequenceMatcher

if sys.stdout.encoding != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

def normalize_text(text):
    text = text.lower()
    text = text.replace('ı', 'i').replace('ğ', 'g').replace('ü', 'u').replace('ş', 's').replace('ö', 'o').replace('ç', 'c')
    text = re.sub(r'[^\w\s]', '', text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text

with open('src/data/all_questions.json', encoding='utf-8') as f:
    questions = json.load(f)

print(f"Toplam taranan soru sayısı: {len(questions)}")

# 1. Exact text match
exact_matches = defaultdict(list)
for q in questions:
    norm = normalize_text(q['text'])
    exact_matches[norm].append(q)

exact_dups = {k: v for k, v in exact_matches.items() if len(v) > 1}
print(f"\n1. BİREBİR AYNI METNE SAHİP TEKRAR EDEN SORU GRUBU: {len(exact_dups)} adet")

for i, (norm, group) in enumerate(list(exact_dups.items())[:15]):
    ids = [g['id'] for g in group]
    modules = [g['module_id'] for g in group]
    sources = [g['source'] for g in group]
    print(f"\n   [Grup {i+1}] {len(group)} Tekrar:")
    print(f"   ID'ler: {ids} | Kaynaklar: {sources} | Modüller: {modules}")
    print(f"   Soru Metni: {group[0]['text'][:110]}...")

# 2. Near-duplicate match (Fuzzy similarity >= 85%) within the same module
print("\n" + "=" * 65)
print("2. YÜKSEK BENZERLİKLİ (Fuzzy Similarity >= 85%) KLON SORU ANALİZİ:")
fuzzy_dups = []
for mod in ['1001', '1003', '1005', '1012']:
    mod_qs = [q for q in questions if q['module_id'] == mod]
    for i in range(len(mod_qs)):
        for j in range(i + 1, len(mod_qs)):
            q1 = mod_qs[i]
            q2 = mod_qs[j]
            norm1 = normalize_text(q1['text'])
            norm2 = normalize_text(q2['text'])
            if norm1 == norm2:
                continue
            ratio = SequenceMatcher(None, norm1, norm2).ratio()
            if ratio >= 0.85:
                fuzzy_dups.append((ratio, q1, q2))

print(f"Fuzzy >= %85 Benzer Soru Çifti Sayısı: {len(fuzzy_dups)}")
for i, (ratio, q1, q2) in enumerate(fuzzy_dups[:10]):
    print(f"\n   [Çift {i+1}] Benzerlik: %{ratio*100:.1f}")
    print(f"   Soru 1 ({q1['id']} - {q1['source']}): {q1['text'][:90]}...")
    print(f"   Soru 2 ({q2['id']} - {q2['source']}): {q2['text'][:90]}...")

# 3. Analyze overlap between Master and Öğretici banks
print("\n" + "=" * 65)
print("3. MASTER BANKA İLE ÖĞRETİCİ BANKA ARASINDAKİ ÇAKIŞMA ANALİZİ:")
master_qs = [q for q in questions if q['source'] == 'master']
ogretici_qs = [q for q in questions if q['source'] == 'ogretici']

cross_exact = 0
for mq in master_qs:
    mnorm = normalize_text(mq['text'])
    for oq in ogretici_qs:
        if mnorm == normalize_text(oq['text']):
            cross_exact += 1
            break

print(f"Master Banka ve Öğretici Banka arasında birebir aynı metne sahip soru sayısı: {cross_exact}")
