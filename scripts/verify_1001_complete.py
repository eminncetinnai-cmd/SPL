import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

print("=" * 60)
print("🔍 1001 MODÜLÜ VE TÜM SORU VERİ TABANI DOĞRULAMASI")
print("=" * 60)

with open('src/data/all_questions.json', 'r', encoding='utf-8') as f:
    all_qs = json.load(f)

with open('src/data/questions_master.json', 'r', encoding='utf-8') as f:
    master_qs = json.load(f)

assert all_qs == master_qs, "all_questions.json and questions_master.json are not identical!"
print("✔ all_questions.json ve questions_master.json birebir eşit.")

# Total counts
total = len(all_qs)
print(f"✔ Toplam soru sayısı: {total}")

modules = {}
for q in all_qs:
    m = str(q.get('module_id', ''))
    modules[m] = modules.get(m, 0) + 1

print(f"✔ Modül soru dağılımı: {modules}")
assert modules.get('1001') == 200, f"Expected 200 questions for 1001, got {modules.get('1001')}"
print("✔ 1001 modülü soru sayısı tam olarak 200!")

# Detailed check for 1001 questions
q1001 = [q for q in all_qs if str(q.get('module_id', '')) == '1001']
ids = set()
texts = set()
ans_dist = {}

for idx, q in enumerate(q1001, 1):
    qid = q.get('id')
    assert qid, f"Q{idx} missing id"
    assert qid not in ids, f"Duplicate ID: {qid}"
    ids.add(qid)
    
    txt = q.get('text', '').strip().lower()
    assert len(txt) > 10, f"Q{idx} text too short"
    assert txt not in texts, f"Duplicate question text: {q.get('text')}"
    texts.add(txt)
    
    opts = q.get('options', [])
    assert len(opts) == 5, f"Q{idx} ({qid}) does not have 5 options"
    keys = [o['key'] for o in opts]
    assert keys == ['A', 'B', 'C', 'D', 'E'], f"Q{idx} ({qid}) invalid keys: {keys}"
    for o in opts:
        assert len(o['text'].strip()) > 0, f"Q{idx} ({qid}) option {o['key']} empty"
        
    ans = q.get('correct_answer')
    assert ans in ['A', 'B', 'C', 'D', 'E'], f"Q{idx} ({qid}) invalid answer {ans}"
    ans_dist[ans] = ans_dist.get(ans, 0) + 1
    
    assert len(q.get('explanation', '').strip()) > 10, f"Q{idx} ({qid}) explanation too short"

print(f"✔ 200 sorunun tamamı benzersiz, 5 seçenekli (A-E) ve geçerli cevap anahtarına sahip.")
print(f"✔ 1001 genel cevap anahtarı dağılımı: {sorted(ans_dist.items())}")

# Check 15 newly added questions
new_ids = [f"q_1001_master_{i}" for i in range(116, 131)]
found_new = [q for q in q1001 if q['id'] in new_ids]
print(f"✔ Yeni eklenen soruların sayısı: {len(found_new)}/15")
assert len(found_new) == 15, "Not all 15 new questions found!"

new_ans = {}
for q in found_new:
    a = q['correct_answer']
    new_ans[a] = new_ans.get(a, 0) + 1
print(f"✔ Yeni 15 sorunun cevap dağılımı: {sorted(new_ans.items())}")

print("=" * 60)
print("🎉 TÜM DOĞRULAMA KONTROLLERİ BAŞARIYLA GEÇTİ!")
print("=" * 60)
