import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('src/data/all_questions.json', 'r', encoding='utf-8') as f:
    questions = json.load(f)

sukuk_qs = [q for q in questions if 'kira sertifika' in q['text'].lower() or 'sukuk' in q['text'].lower() or 'vkş' in q['text'].lower() or 'istisna' in q['text'].lower()]

print(f"Total Sukuk / Kira Sertifikası questions: {len(sukuk_qs)}")
for q in sukuk_qs:
    print(f"\n--- [{q['id']}] Topic: {q.get('topic')} ---")
    print(f"Soru: {q['text']}")
    print(f"Doğru: {q['correct_answer']}")
    for opt in q['options']:
        mark = "✓" if opt['key'] == q['correct_answer'] else " "
        print(f"  [{opt['key']}] {mark} {opt['text']}")
