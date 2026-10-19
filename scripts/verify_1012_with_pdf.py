import csv
import json
from pathlib import Path

# Dosya yolları
CSV_FILE = Path(r"C:\Users\e.cetin\Downloads\SPK_SPL_Hatali_Sorular_2026-09-09.csv")
QUESTIONS_FILE = Path(r"C:\Users\e.cetin\Desktop\SPL\src\data\all_questions.json")
PDF_TEXT_FILE = Path(r"C:\Users\e.cetin\Desktop\SPL\kaynak\1012_text.txt")

# PDF metnini yükle
with open(PDF_TEXT_FILE, 'r', encoding='utf-8') as f:
    pdf_text = f.read()

# Soruları yükle
with open(QUESTIONS_FILE, 'r', encoding='utf-8') as f:
    questions = json.load(f)

# CSV'de tutarsız soruları oku
mismatched_questions = []
with open(CSV_FILE, 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f, delimiter=';')
    for row in reader:
        module = row.get('\ufeffModül', row.get('Modül', ''))
        if '1012' in module:
            question_id = row.get('\ufeffSoru ID', row.get('Soru ID', ''))
            csv_correct = row.get('Doğru Cevap', '')
            question_text = row.get('Soru Metni', '')

            # Veritabanında soruyu bul
            db_question = None
            for q in questions:
                if q.get('id') == question_id:
                    db_question = q
                    break

            if db_question:
                db_correct = db_question.get('correct_answer', '')
                if db_correct != csv_correct:
                    mismatched_questions.append({
                        'id': question_id,
                        'question': question_text[:100],
                        'db_answer': db_correct,
                        'csv_answer': csv_correct
                    })

print(f"Toplam {len(mismatched_questions)} tutarsiz soru analiz ediliyor...\n")

# Ilk 5 soruyu PDF'de ara
for i, q in enumerate(mismatched_questions[:5], 1):
    print(f"{i}. Soru ID: {q['id']}")
    print(f"   Soru: {q['question']}...")
    print(f"   Veritabani: {q['db_answer']}, CSV: {q['csv_answer']}")

    # Soru metninin PDF'de gecip gecmedigini kontrol et
    # Anahtar kelimeleri al
    question_words = q['question'].split()[:5]
    search_terms = ' '.join(question_words)

    if search_terms in pdf_text:
        print(f"   [OK] PDF'de bulundu (benzer metin)")
    else:
        print(f"   [X] PDF'de bulunamadi")
    print()
