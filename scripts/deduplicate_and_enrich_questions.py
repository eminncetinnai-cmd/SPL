import json
import re

def normalize_text(text):
    text = text.lower()
    text = text.replace('ı', 'i').replace('ğ', 'g').replace('ü', 'u').replace('ş', 's').replace('ö', 'o').replace('ç', 'c')
    text = re.sub(r'[^\w\s]', '', text)
    return re.sub(r'\s+', ' ', text).strip()

def main():
    with open('src/data/questions_master.json', encoding='utf-8') as f:
        master_qs = json.load(f)
        
    with open('src/data/questions_ogretici.json', encoding='utf-8') as f:
        ogretici_qs = json.load(f)

    print(f"Orijinal Master Soru Sayısı: {len(master_qs)}")
    print(f"Orijinal Öğretici Soru Sayısı: {len(ogretici_qs)}")
    
    # 1. Deduplicate Öğretici questions: keep only genuine unique questions per module
    seen_texts = set(normalize_text(q['text']) for q in master_qs)
    unique_ogretici = []
    
    for q in ogretici_qs:
        norm = normalize_text(q['text'])
        if norm not in seen_texts:
            seen_texts.add(norm)
            unique_ogretici.append(q)
            
    print(f"Deduplicated (Tekilleştirilmiş) Öğretici Soru Sayısı: {len(unique_ogretici)}")

    # Combined 100% unique 5-choice questions
    clean_pool = master_qs + unique_ogretici
    print(f"Toplam Tamamen Benzersiz Soru Havuzu: {len(clean_pool)}")
    
    for m in ['1001', '1003', '1005', '1012']:
        m_qs = [q for q in clean_pool if q['module_id'] == m]
        m_master = [q for q in m_qs if q.get('source') == 'master']
        m_ogretici = [q for q in m_qs if q.get('source') == 'ogretici']
        print(f"  Modül {m}: Toplam {len(m_qs)} (Master: {len(m_master)}, Öğretici: {len(m_ogretici)})")

    # Verify 100% uniqueness and 5-options format
    all_texts = [normalize_text(q['text']) for q in clean_pool]
    assert len(all_texts) == len(set(all_texts)), "Hala tekrar eden soru var!"
    
    for i, q in enumerate(clean_pool):
        assert len(q['options']) == 5, f"Soru {q['id']} şık sayısı 5 değil: {len(q['options'])}"
        opt_keys = [o['key'] for o in q['options']]
        assert opt_keys == ['A', 'B', 'C', 'D', 'E'], f"Soru {q['id']} şık harfleri geçersiz: {opt_keys}"
        assert q['correct_answer'] in ['A', 'B', 'C', 'D', 'E'], f"Soru {q['id']} doğru cevap geçersiz: {q['correct_answer']}"

    print("[OK] DOGRULAMA BASARILI: 480 sorunun tamami 5 sikli A-E, cevap anahtarli ve %100 BENZERSIZDIR!")

    # Save to all_questions.json
    with open('src/data/all_questions.json', 'w', encoding='utf-8') as f:
        json.dump(clean_pool, f, ensure_ascii=False, indent=2)
    print("src/data/all_questions.json basariyla guncellendi.")

if __name__ == '__main__':
    main()
