import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('src/data/all_questions.json', 'r', encoding='utf-8') as f:
    questions = json.load(f)

print(f"Loaded {len(questions)} questions.")

boilerplate_clues = [
    "pay sahiplerine tanınan yeni pay alma hakkının",
    "varantlarda ihraçcının piyasa yapıcı",
    "varantlarda ihraççının piyasa yapıcı",
    "kullanım süresinin en az 15, en fazla 60 gün olması",
    "sürekli likidite ve kotasyon sağlama taahhüdü"
]

corrupted_questions = []

for q in questions:
    q_text = q['text']
    bad_opts = []
    for opt in q['options']:
        text_lower = opt['text'].lower()
        for clue in boilerplate_clues:
            if clue in text_lower:
                # check if question is actually about that clue
                if "rüçhan" not in q_text.lower() and "varant" not in q_text.lower():
                    bad_opts.append((opt['key'], opt['text']))
                    break
    if bad_opts:
        corrupted_questions.append((q, bad_opts))

print(f"\nFound {len(corrupted_questions)} questions with known boilerplate corruption:")
for q, bad_opts in corrupted_questions:
    print(f"\n--- [{q['id']}] Modül {q['module_id']} ---")
    print(f"Soru: {q['text']}")
    print(f"Bozuk Şıklar: {bad_opts}")
    print("Tüm Şıklar:")
    for opt in q['options']:
        print(f"  {opt['key']}: {opt['text']}")
