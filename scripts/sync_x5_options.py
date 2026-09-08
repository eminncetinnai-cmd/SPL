import json

def main():
    with open('src/data/all_questions.json', encoding='utf-8') as f:
        all_qs = json.load(f)

    # Extract the 80 X5 questions
    x5_map = {}
    for q in all_qs:
        if 'x5' in q['id']:
            x5_map[q['number']] = q

    print(f"all_questions.json içinde bulunan 5 şıklı X5 soru sayısı: {len(x5_map)}")

    with open('src/data/x5_study_guide.json', encoding='utf-8') as f:
        x5_guide = json.load(f)

    updated_drills = []
    for dq in x5_guide.get('drill_questions', []):
        num = dq['number']
        if num in x5_map:
            full_q = x5_map[num]
            updated_drills.append({
                'number': num,
                'module_id': full_q['module_id'],
                'text': full_q['text'],
                'options': full_q['options'],
                'correct_answer': full_q['correct_answer'],
                'explanation': full_q['explanation']
            })
        else:
            updated_drills.append(dq)

    x5_guide['drill_questions'] = updated_drills

    with open('src/data/x5_study_guide.json', 'w', encoding='utf-8') as f:
        json.dump(x5_guide, f, ensure_ascii=False, indent=2)

    print("x5_study_guide.json drill_questions başarıyla 5 şıklı olarak güncellendi!")
    first_q = x5_guide['drill_questions'][0]
    print(f"Soru 1 Şık Sayısı: {len(first_q['options'])}")
    for opt in first_q['options']:
        print(f"  {opt['key']}) {opt['text']}")

if __name__ == '__main__':
    main()
