import json
from pathlib import Path

# Dosya yolları
QUESTIONS_FILE = Path(r"C:\Users\e.cetin\Desktop\SPL\src\data\all_questions.json")

# Soruları yükle
with open(QUESTIONS_FILE, 'r', encoding='utf-8') as f:
    questions = json.load(f)

# 1012 modül sorularını filtrele
module_1012_questions = [q for q in questions if q.get('module_id') == '1012']

print(f"Modül 1012'de toplam {len(module_1012_questions)} soru bulunuyor.")
print(f"\nİlk 5 sorunun ID'leri:")
for q in module_1012_questions[:5]:
    print(f"  - {q['id']}: {q['text'][:60]}...")
