import json
from pathlib import Path

QUESTIONS_FILE = Path(r"C:\Users\e.cetin\Desktop\SPL\src\data\all_questions.json")

# Soruları yükle
with open(QUESTIONS_FILE, 'r', encoding='utf-8') as f:
    questions = json.load(f)

# Tablodaki soruların anahtar kelimeleri
table_questions = [
    {
        'number': 23,
        'module': '1001',
        'topic': 'Piyasa Dolandırıcılığı Cezaları ve Etkin Pişmanlık',
        'keywords': ['piyasa', 'dolandırıcılığı', 'etkin', 'pişmanlık', 'menfaatin', '2 katı']
    },
    {
        'number': 25,
        'module': '1001',
        'topic': 'Kurumsal Yönetim Şirket Gruplandırması ve Eşik Değerler',
        'keywords': ['kurumsal', 'yönetim', 'gruplandırma', 'eşik', 'değerler', 'yeniden değerleme']
    },
    {
        'number': 40,
        'module': '1003',
        'topic': 'Oyda İmtiyaz Sınırı ve Kullanılamayacağı Haller',
        'keywords': ['oyda', 'imtiyaz', 'sınırı', 'kullanılamayacağı', 'önemli', 'nitelik']
    },
    {
        'number': 62,
        'module': '1003',
        'topic': 'BASK Karar Nisabı',
        'keywords': ['BASK', 'karar', 'nisabı', 'borçlanma', 'araç', 'sahipleri']
    }
]

print("Tablodaki soruların ID'leri tespit ediliyor...\n")

for target in table_questions:
    module = target['module']
    keywords = target['keywords']
    
    # Modüle göre soruları filtrele
    module_questions = [q for q in questions if q.get('module_id') == module]
    
    # Her soruyu kontrol et
    best_match = None
    best_score = 0
    
    for q in module_questions:
        q_text = q.get('text', '').lower()
        q_topic = q.get('topic', '').lower()
        
        # Anahtar kelime eşleşme skoru
        score = 0
        for keyword in keywords:
            if keyword.lower() in q_text or keyword.lower() in q_topic:
                score += 1
        
        if score > best_score and score >= 2:  # En az 2 anahtar kelime eşleşmeli
            best_score = score
            best_match = q
    
    if best_match:
        print(f"Soru {target['number']} (Modül {module}):")
        print(f"  ID: {best_match['id']}")
        print(f"  Konu: {best_match.get('topic', 'N/A')}")
        print(f"  Mevcut cevap: {best_match.get('correct_answer', 'N/A')}")
        print(f"  Skor: {best_score}/{len(keywords)}")
        print()
    else:
        print(f"Soru {target['number']} (Modül {module}): BULUNAMADI")
        print()
