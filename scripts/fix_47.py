import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('src/data/all_questions.json', 'r', encoding='utf-8') as f:
    questions = json.load(f)

for q in questions:
    if q['id'] == 'q_1005_master_047':
        q['options'][0]['text'] = "Müşteri ile portföy yöneticisi arasında özel yazılı protokol düzenlenmesi şartıyla hukuken geçerlidir"
        print("Updated q_1005_master_047 option A to formal legal wording.")

with open('src/data/all_questions.json', 'w', encoding='utf-8') as f:
    json.dump(questions, f, ensure_ascii=False, indent=2)

with open('src/data/questions_master.json', 'w', encoding='utf-8') as f:
    json.dump(questions, f, ensure_ascii=False, indent=2)
