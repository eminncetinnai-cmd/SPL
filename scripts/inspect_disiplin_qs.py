import json

with open('src/data/all_questions.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

q1001 = [q for q in data if str(q.get('module_id', '')) == '1001']
for q in q1001:
    if q['id'] in ['q_1001_master_091', 'q_1001_master_094', 'q_1001_master_095', 'q_1001_master_096', 'q_1001_master_097', 'q_1001_master_098', 'q_1001_master_099']:
        print(q['id'])
        print('Q:', q['text'])
        print('Ans:', q['correct_answer'])
        for o in q['options']:
            print("  " + o['key'] + ") " + o['text'])
        print('Exp:', q['explanation'])
        print('-'*50)
