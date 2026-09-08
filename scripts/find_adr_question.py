import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('src/data/all_questions.json', 'r', encoding='utf-8') as f:
    questions = json.load(f)

for q in questions:
    if 'ADR' in q.get('text', '') or any('ADR' in opt['text'] for opt in q.get('options', [])):
        print("Found ADR question:")
        print("ID:", q['id'])
        print("Text:", q['text'])
        for o in q['options']:
            print(f"  {o['key']}: {o['text']}")
        print("Correct:", q['correct_answer'])
        break
