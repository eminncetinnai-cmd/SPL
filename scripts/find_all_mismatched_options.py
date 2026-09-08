import json
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('src/data/all_questions.json', 'r', encoding='utf-8') as f:
    questions = json.load(f)

print(f"Total questions: {len(questions)}")

suspicious = []

for q in questions:
    opts = q['options']
    lens = [len(o['text']) for o in opts]
    min_len = min(lens)
    max_len = max(lens)
    
    # Check if some options are short phrases (<25 chars) while others are huge sentences (>75 chars)
    short_opts = [o for o in opts if len(o['text']) <= 25]
    long_opts = [o for o in opts if len(o['text']) >= 75]
    
    if short_opts and long_opts and len(short_opts) >= 2:
        # Suspicious length mismatch
        suspicious.append((q, short_opts, long_opts))

print(f"\nFound {len(suspicious)} questions with extreme option length mismatch:")
for q, s_opts, l_opts in suspicious:
    print(f"\n--- [{q['id']}] Modül {q['module_id']} ---")
    print(f"Soru: {q['text']}")
    print(f"Doğru Seçenek: {q['correct_answer']}")
    print("Şıklar:")
    for o in q['options']:
        mark = "✓" if o['key'] == q['correct_answer'] else " "
        print(f"  [{o['key']}] {mark} ({len(o['text']):3d} kr) {o['text']}")
