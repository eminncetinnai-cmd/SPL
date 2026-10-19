import json
import re
from pathlib import Path

# Dosya yolları
QUESTIONS_FILE = Path(r"C:\Users\e.cetin\Desktop\SPL\src\data\all_questions.json")
MASTER_FILE = Path(r"C:\Users\e.cetin\Desktop\SPL\src\data\questions_master.json")

# Soruları yükle
with open(QUESTIONS_FILE, 'r', encoding='utf-8') as f:
    questions = json.load(f)

with open(MASTER_FILE, 'r', encoding='utf-8') as f:
    master_questions = json.load(f)

# ID'den soru bulma fonksiyonu
def find_question_by_text(text, module_id):
    """Soru metninden benzer soruyu bul"""
    text_normalized = text.lower().strip()
    best_match = None
    best_score = 0

    for q in questions:
        if q.get('module_id') != module_id:
            continue

        q_text = q.get('text', '').lower().strip()
        # Basit benzerlik skoru (ortak kelime sayısı)
        words1 = set(text_normalized.split())
        words2 = set(q_text.split())
        common = len(words1 & words2)
        total = len(words1 | words2)

        if total > 0:
            score = common / total
            if score > best_score and score > 0.5:  # En az %50 benzerlik
                best_score = score
                best_match = q

    return best_match

# Analiz fonksiyonu
def analyze_mistake(mistake_data):
    """Tek bir yanlış soruyu analiz et"""
    module = mistake_data.get('module', '')
    question_text = mistake_data.get('question_text', '')
    user_answer = mistake_data.get('your_answer', '')
    correct_answer = mistake_data.get('correct_answer', '')
    explanation = mistake_data.get('explanation', '')

    # Modül ID'sini çıkar
    module_id = module.replace('Modül ', '').strip()

    # Veritabanında soruyu bul
    db_question = find_question_by_text(question_text, module_id)

    if not db_question:
        return {
            'status': 'not_found',
            'module': module,
            'question_text': question_text[:100] + '...',
            'issue': 'Soru veritabanında bulunamadı'
        }

    # Karşılaştır
    issues = []

    # Doğru cevap kontrolü
    if db_question.get('correct_answer') != correct_answer:
        issues.append({
            'type': 'correct_answer_mismatch',
            'db_answer': db_question.get('correct_answer'),
            'displayed_answer': correct_answer
        })

    # Açıklama kontrolü
    db_explanation = db_question.get('explanation', '')
    if db_explanation != explanation:
        issues.append({
            'type': 'explanation_mismatch',
            'note': 'Açıklama farklı'
        })

    # Seçenekler kontrolü
    db_options = db_question.get('options', {})
    displayed_options = mistake_data.get('options', {})

    if db_options != displayed_options:
        issues.append({
            'type': 'options_mismatch',
            'note': 'Seçenekler farklı'
        })

    return {
        'status': 'analyzed',
        'module': module,
        'question_id': db_question.get('id'),
        'question_text': question_text[:100] + '...',
        'db_correct_answer': db_question.get('correct_answer'),
        'displayed_correct_answer': correct_answer,
        'user_answer': user_answer,
        'issues': issues
    }

print("Analiz scripti hazır. Lütfen yanlış soru verisini JSON formatında mistakes_data.json dosyasına kaydedin.")
