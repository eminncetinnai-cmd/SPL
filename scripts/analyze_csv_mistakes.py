import csv
import json
from pathlib import Path

# Dosya yolları
CSV_FILE = Path(r"C:\Users\e.cetin\Downloads\SPK_SPL_Hatali_Sorular_2026-09-09.csv")
QUESTIONS_FILE = Path(r"C:\Users\e.cetin\Desktop\SPL\src\data\all_questions.json")

# Soruları yükle
with open(QUESTIONS_FILE, 'r', encoding='utf-8') as f:
    questions = json.load(f)

# CSV dosyasını oku
mistakes_1012 = []
with open(CSV_FILE, 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f, delimiter=';')
    # İlk satırdaki sütunları yazdır
    first_row = next(reader)
    print("CSV Sütunları:", list(first_row.keys()))
    f.seek(0)
    reader = csv.DictReader(f, delimiter=';')
    for row in reader:
        # Modül sütununu kontrol et
        module = row.get('Modül', '')
        if '1012' in module:
            mistakes_1012.append(row)

print(f"\nModül 1012'de toplam {len(mistakes_1012)} yanlış soru bulundu.")
if mistakes_1012:
    print(f"\nİlk 3 soru:")
    for i, m in enumerate(mistakes_1012[:3], 1):
        keys = list(m.keys())
        print(f"{i}. Anahtarlar: {keys}")
        break
