import json
import os
import re
import sys
from collections import defaultdict

sys.stdout.reconfigure(encoding='utf-8')

# Read current questions
with open('src/data/all_questions.json', 'r', encoding='utf-8') as f:
    all_qs = json.load(f)

print(f"Initial total questions: {len(all_qs)}")

def normalize(text):
    t = re.sub(r'\[.*?\]', '', text)
    t = re.sub(r'\(.*?\)', '', t)
    t = re.sub(r'[^a-zA-Z0-9çğıöşüÇĞİÖŞÜ]', '', t).lower()
    return t

# 1. Separate by source category
master_qs = []
konu_qs = []
ogretici_qs = []
cikmis_raw_qs = []

for q in all_qs:
    qid = q['id']
    if '_master_' in qid:
        q['source'] = 'master'
        master_qs.append(q)
    elif '_konu_' in qid:
        q['source'] = 'konu'
        konu_qs.append(q)
    elif '_ogretici_' in qid:
        q['source'] = 'ogretici'
        ogretici_qs.append(q)
    elif '_web_' in qid or '_exam_' in qid:
        cikmis_raw_qs.append(q)
    else:
        # Fallback based on q['source']
        if q.get('source') == 'ogretici':
            ogretici_qs.append(q)
        else:
            master_qs.append(q)

print(f"Extracted: master={len(master_qs)}, konu={len(konu_qs)}, ogretici={len(ogretici_qs)}, cikmis_raw={len(cikmis_raw_qs)}")

# 2. Deduplicate cikmis_raw_qs against existing master, konu, ogretici, and within itself
seen_fingerprints = set()
for q in master_qs + konu_qs + ogretici_qs:
    seen_fingerprints.add(normalize(q['text']))

unique_cikmis_by_mod = defaultdict(list)
duplicate_count = 0

for q in cikmis_raw_qs:
    fp = normalize(q['text'])
    if fp in seen_fingerprints:
        duplicate_count += 1
        continue
    seen_fingerprints.add(fp)
    unique_cikmis_by_mod[q['module_id']].append(q)

print(f"Removed {duplicate_count} duplicate/redundant questions from cikmis pool!")

# 3. Format cikmis questions cleanly
formatted_cikmis = []
for mod in ['1001', '1003', '1005', '1012']:
    mod_qs = unique_cikmis_by_mod[mod]
    for idx, q in enumerate(mod_qs, start=1):
        clean_q = {
            "id": f"q_{mod}_cikmis_{idx:03d}",
            "module_id": mod,
            "number": idx,
            "source": "cikmis",
            "topic": q.get("topic", "Çıkmış Sınav Sorusu"),
            "chapter": q.get("chapter", f"Modül {mod} Çıkmış Sınav Soruları"),
            "text": re.sub(r'\[Test Soru No: \d+\]', '', q["text"]).strip(),
            "options": q["options"],
            "correct_answer": q["correct_answer"],
            "explanation": q["explanation"],
            "trap": q.get("trap", ""),
            "difficulty": q.get("difficulty", "medium"),
            "tags": [mod, "Çıkmış Sınav Sorusu", q.get("topic", "")]
        }
        # Clean any remaining trailing bracket artifacts
        clean_q["text"] = re.sub(r'\s*\[.*?\]\s*$', '', clean_q["text"]).strip()
        formatted_cikmis.append(clean_q)

print(f"Final formatted unique cikmis questions: {len(formatted_cikmis)}")
for mod in ['1001', '1003', '1005', '1012']:
    print(f"  Modül {mod}: {len([q for q in formatted_cikmis if q['module_id'] == mod])} Çıkmış Soru")

# 4. Final combined pool
final_all_qs = master_qs + konu_qs + ogretici_qs + formatted_cikmis

# 5. Strict verification of ZERO duplicates across the entire database
all_fps = set()
global_dups = []
for q in final_all_qs:
    fp = normalize(q['text'])
    if fp in all_fps:
        global_dups.append(q['id'])
    all_fps.add(fp)

assert len(global_dups) == 0, f"Found unexpected global duplicates: {global_dups}"
print(f"VERIFICATION SUCCESSFUL: 0 duplicate questions in entire database! Total: {len(final_all_qs)}")

# 6. Save updated databases
with open('src/data/all_questions.json', 'w', encoding='utf-8') as f:
    json.dump(final_all_qs, f, ensure_ascii=False, indent=2)

with open('src/data/questions_master.json', 'w', encoding='utf-8') as f:
    json.dump(master_qs, f, ensure_ascii=False, indent=2)

# Save dedicated questions_cikmis.json
with open('src/data/questions_cikmis.json', 'w', encoding='utf-8') as f:
    json.dump(formatted_cikmis, f, ensure_ascii=False, indent=2)

print("\n=== FINAL CLEAN DATABASE BREAKDOWN ===")
print(f"🎯 Çıkmış Sınav Soruları (`source: 'cikmis'`): {len(formatted_cikmis)} Soru")
print(f"👑 Master Soru Bankası (`source: 'master'`): {len(master_qs)} Soru")
print(f"📖 Konu Anlatımı Çözümlü (`source: 'konu'`): {len(konu_qs)} Soru")
print(f"💡 Öğretici & Tuzak Bankası (`source: 'ogretici'`): {len(ogretici_qs)} Soru")
print(f"📚 GENEL TOPLAM HAVUZ: {len(final_all_qs)} Soru")
