import json
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')
sys.path.append('scripts')

from build_1001_exam_questions import get_1001_questions
from build_1003_exam_questions import get_1003_questions
from build_1005_exam_questions import get_1005_questions
from build_1012_exam_questions import get_1012_questions

# 1. Generate 100 questions for each module
q1001 = get_1001_questions()
q1003 = get_1003_questions()
q1005 = get_1005_questions()
q1012 = get_1012_questions()

print(f"Loaded: 1001={len(q1001)}, 1003={len(q1003)}, 1005={len(q1005)}, 1012={len(q1012)}")
assert len(q1001) == 100
assert len(q1003) == 100
assert len(q1005) == 100
assert len(q1012) == 100

new_exam_questions = []
for mod, q_list in [('1001', q1001), ('1003', q1003), ('1005', q1005), ('1012', q1012)]:
    for idx, q in enumerate(q_list, start=1):
        q_obj = {
            "id": f"q_{mod}_exam_{idx:03d}",
            "module_id": mod,
            "number": 120 + idx,
            "source": "master",
            "topic": q.get("topic", "Çıkmış Sınav Sorusu"),
            "chapter": q.get("chapter", f"Modül {mod} Sınav Soruları"),
            "text": q["text"],
            "options": q["options"],
            "correct_answer": q["correct_answer"],
            "explanation": q["explanation"],
            "trap": q.get("trap", ""),
            "difficulty": q.get("difficulty", "medium"),
            "tags": [mod, "Çıkmış Sınav Sorusu", "Web Çıkmış Sınav Sorusu", q.get("topic", "")]
        }
        new_exam_questions.append(q_obj)

print(f"Total new exam questions prepared: {len(new_exam_questions)} (400 questions)")

# 2. Read existing questions from all_questions.json
with open('src/data/all_questions.json', 'r', encoding='utf-8') as f:
    existing_all = json.load(f)

# Filter out any existing 'exam' questions if previously added to make it idempotent
existing_filtered = [q for q in existing_all if not q['id'].startswith('q_') or '_exam_' not in q['id']]
print(f"Existing questions retained (master + konu + ogretici + web): {len(existing_filtered)}")

# 3. Combine with new exam questions
combined = existing_filtered + new_exam_questions
print(f"Combined total questions: {len(combined)}")

# 4. Verification of uniqueness
ids = set()
duplicates = []
for q in combined:
    if q['id'] in ids:
        duplicates.append(q['id'])
    ids.add(q['id'])

if duplicates:
    print(f"ERROR: Duplicate IDs found: {duplicates[:10]}")
    sys.exit(1)

# Check text uniqueness
text_fps = set()
text_dups = 0
for q in combined:
    fp = q['text'].strip().lower()[:50]
    if fp in text_fps:
        text_dups += 1
    text_fps.add(fp)

print(f"Distinct question text fingerprints: {len(text_fps)}, duplicates: {text_dups}")

# 5. Save updated database
with open('src/data/all_questions.json', 'w', encoding='utf-8') as f:
    json.dump(combined, f, ensure_ascii=False, indent=2)

print("src/data/all_questions.json successfully updated!")

# 6. Detailed statistics
master_qs = [q for q in combined if q['source'] == 'master']
ogretici_qs = [q for q in combined if q['source'] == 'ogretici']

print("\n=== FINAL POOL BREAKDOWN ===")
print(f"🎯 Çıkmış Sınav / Master Soruları: {len(master_qs)} Soru")
print(f"💡 Öğretici Banka: {len(ogretici_qs)} Soru")
print(f"📚 Genel Toplam Havuz: {len(combined)} Soru")

by_mod_master = {}
for q in master_qs:
    by_mod_master[q['module_id']] = by_mod_master.get(q['module_id'], 0) + 1

print("\nMaster / Çıkmış Soru Dağılımı (Modül Başına):")
for m, c in sorted(by_mod_master.items()):
    print(f"  Modül {m}: {c} Soru")
