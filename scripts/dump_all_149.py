import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('scripts/all_problematic_questions.json', 'r', encoding='utf-8') as f:
    qs = json.load(f)

print(f"Loaded {len(qs)} problematic questions.")
# Group by module
by_mod = {}
for q in qs:
    mod = q['module_id']
    by_mod.setdefault(mod, []).append(q)

for mod, list_q in by_mod.items():
    print(f"\n==================== MODÜL {mod} ({len(list_q)} soru) ====================")
    for q in list_q:
        c_opt = next(o['text'].strip() for o in q['options'] if o['key'] == q['correct_answer'])
        print(f"[{q['id']}] Ans: {q['correct_answer']} -> '{c_opt}'")
        print(f"  Q: {q['text']}")
