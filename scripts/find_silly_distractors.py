import json
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('src/data/all_questions.json', 'r', encoding='utf-8') as f:
    questions = json.load(f)

silly_words = [
    "güvercin", "madalya", "genel müdüre", "hiçbir şey yapmaz",
    "televizyon", "emir kulu", "posta güvercini", "imha edilir",
    "10 yıl ertelenir", "yeni şirket kurar", "silinir"
]

found_silly = []

for q in questions:
    for opt in q['options']:
        text_l = opt['text'].lower()
        for sw in silly_words:
            if sw in text_l:
                found_silly.append((q['id'], q['module_id'], opt['key'], opt['text'], q['text']))
                break

print(f"Found {len(found_silly)} options with silly/lazy distractors:")
for fid, mod, key, opt_text, q_text in found_silly:
    print(f"\n[{fid}] Modül {mod}: Option [{key}]: '{opt_text}'")
    print(f"  Soru: {q_text[:90]}")
