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

# Belirli bir soruyu PDF'de detaylı ara
def find_answer_in_pdf(question_text, pdf_text):
    """PDF'de sorunun cevabını arar"""
    # Soru metninin anahtar kelimelerini al
    question_lower = question_text.lower()

    # PDF'de soru metninin geçtiği bölümü bul
    if question_lower not in pdf_text.lower():
        return None, "Soru PDF'de bulunamadi"

    # Sorunun PDF'deki konumunu bul
    start_idx = pdf_text.lower().find(question_lower)
    # Sorudan sonraki 2000 karakteri al (cevap orada olabilir)
    context = pdf_text[start_idx:start_idx + 2000]

    return context, "Bulundu"

# Kritik soruları manuel kontrol et
critical_questions = [
    'q_1012_master_006',  # VİOP takas süresi
    'q_1012_konu_008',  # Portföy saklama
    'q_1012_master_040',  # Virman işlemi
    'q_1012_master_066',  # Ters repo
]

print("Kritik sorular PDF'de detaylı araniyor...\n")

for q_id in critical_questions:
    # Veritabanında soruyu bul
    db_question = None
    for q in questions:
        if q.get('id') == q_id:
            db_question = q
            break

    if not db_question:
        print(f"{q_id}: Veritabaninda bulunamadi")
        continue

    question_text = db_question.get('text', '')
    db_answer = db_question.get('correct_answer', '')

    # PDF'de ara
    context, status = find_answer_in_pdf(question_text, pdf_text)

    print(f"Soru ID: {q_id}")
    print(f"Veritabani cevabi: {db_answer}")
    print(f"Durum: {status}")
    if status == "Bulundu":
        print(f"PDF context (ilk 500 karakter):\n{context[:500]}")
    print()
