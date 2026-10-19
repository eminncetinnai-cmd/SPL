import csv
import json
from pathlib import Path

# Dosya yolları
CSV_FILE = Path(r"C:\Users\e.cetin\Downloads\SPK_SPL_Hatali_Sorular_2026-09-09.csv")
QUESTIONS_FILE = Path(r"C:\Users\e.cetin\Desktop\SPL\src\data\all_questions.json")

# Soruları yükle
with open(QUESTIONS_FILE, 'r', encoding='utf-8') as f:
    questions = json.load(f)

# Soru ID'den soru bulma fonksiyonu
def find_question_by_id(question_id):
    for q in questions:
        if q.get('id') == question_id:
            return q
    return None

# CSV dosyasını oku
mistakes_1012 = []
with open(CSV_FILE, 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f, delimiter=';')
    for row in reader:
        # BOM karakterini temizle
        module = row.get('\ufeffModül', row.get('Modül', ''))
        if '1012' in module:
            mistakes_1012.append(row)

print(f"Modül 1012'de toplam {len(mistakes_1012)} yanlış soru analiz ediliyor...\n")

# Her soruyu karşılaştır
issues_found = []
for m in mistakes_1012:
    question_id = m.get('\ufeffSoru ID', m.get('Soru ID', ''))
    csv_correct = m.get('Doğru Cevap', '')
    csv_explanation = m.get('Açıklama & Sınav İpucu', '')

    # Veritabanında soruyu bul
    db_question = find_question_by_id(question_id)

    if not db_question:
        issues_found.append({
            'question_id': question_id,
            'issue': 'Soru veritabanında bulunamadı',
            'csv_correct': csv_correct
        })
        continue

    db_correct = db_question.get('correct_answer', '')
    db_explanation = db_question.get('explanation', '')

    # Doğru cevap karşılaştırma
    if db_correct != csv_correct:
        issues_found.append({
            'question_id': question_id,
            'issue': 'correct_answer_mismatch',
            'db_answer': db_correct,
            'csv_answer': csv_correct,
            'question_text': db_question.get('text', '')[:80]
        })

    # Açıklama karşılaştırma (basit kontrol)
    if db_explanation and csv_explanation:
        if db_explanation[:100] != csv_explanation[:100]:
            issues_found.append({
                'question_id': question_id,
                'issue': 'explanation_difference',
                'note': 'Açıklama farklı (ilk 100 karakter)'
            })

print(f"Toplam {len(issues_found)} tespit edilen tutarsızlık:\n")

for i, issue in enumerate(issues_found, 1):
    print(f"{i}. Soru ID: {issue['question_id']}")
    if issue['issue'] == 'correct_answer_mismatch':
        print(f"   TÜR: Doğru cevap tutarsızlığı")
        print(f"   Veritabanı: {issue['db_answer']}")
        print(f"   CSV: {issue['csv_answer']}")
        print(f"   Soru: {issue['question_text']}...")
    else:
        print(f"   TÜR: {issue['issue']}")
        if 'note' in issue:
            print(f"   Not: {issue['note']}")
    print()
