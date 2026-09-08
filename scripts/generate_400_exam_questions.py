import json
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

# Read existing questions to guarantee zero duplication
with open('src/data/all_questions.json', 'r', encoding='utf-8') as f:
    existing_all = json.load(f)

existing_texts = {q['text'].lower().replace(' ', '')[:40] for q in existing_all}
print(f"Loaded {len(existing_all)} existing questions for duplicate prevention.")
