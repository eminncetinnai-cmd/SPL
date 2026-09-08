import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('scripts/all_problematic_questions.json', 'r', encoding='utf-8') as f:
    qs = json.load(f)

for idx, q in enumerate(qs[:25]):
    correct_opt = next(o['text'].strip() for o in q['options'] if o['key'] == q['correct_answer'])
    print(f"=== [{idx+1}/149] ID: {q['id']} (Modül {q['module_id']}) Correct [{q['correct_answer']}]: '{correct_opt}' ===")
    print("Soru: " + q['text'])
    for o in q['options']:
        print(f"   {o['key']}) [{len(o['text'])} kr] {o['text']}")
    print("-" * 80)
