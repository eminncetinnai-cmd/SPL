import json

with open('src/data/all_questions.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

q1001 = [q for q in data if str(q.get('module_id', '')) == '1001']

with open('scripts/all_1001_questions_dump.txt', 'w', encoding='utf-8') as out:
    for idx, q in enumerate(q1001, 1):
        out.write(f"[{idx}] ID: {q.get('id')} | Source: {q.get('source')} | Topic: {q.get('topic')}\n")
        out.write(f"Chapter: {q.get('chapter')}\n")
        out.write(f"Question: {q.get('text')}\n")
        for opt in q.get('options', []):
            out.write(f"  {opt.get('key')}) {opt.get('text')}\n")
        out.write(f"Correct: {q.get('correct_answer')}\n")
        out.write(f"Explanation: {q.get('explanation')}\n")
        if 'trap' in q:
            out.write(f"Trap: {q.get('trap')}\n")
        out.write('-'*70 + '\n')

print(f'Dumped {len(q1001)} questions to scripts/all_1001_questions_dump.txt')
