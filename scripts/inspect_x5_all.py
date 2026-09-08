import json

with open('src/data/x5_study_guide.json', encoding='utf-8') as f:
    x5 = json.load(f)

drill = x5.get('drill_questions', [])
print(f"Total X5 drill questions: {len(drill)}")

by_mod = {}
for q in drill:
    m = q['module_id']
    by_mod.setdefault(m, []).append(q)

for m, qs in by_mod.items():
    print(f"\nModül {m}: {len(qs)} sorular")
    for q in qs[:5]:
        corr = q['options'][0]['text'] if q['options'] else ''
        print(f"  {q['number']}. {q['text']} -> [Doğru: {corr}]")
