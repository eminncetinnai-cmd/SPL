import json
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

for fpath in ['src/data/all_questions.json', 'src/data/questions_master.json']:
    with open(fpath, 'r', encoding='utf-8') as f:
        questions = json.load(f)

    fixed = 0
    for q in questions:
        exp = q.get('explanation', '')
        corr = q.get('correct_answer', '')
        
        # Look for "Doğru cevap X'dir" pattern
        m = re.search(r'(do[ğg]ru\s+cevap\s+)([A-E])([\'’]?[a-z]*)', exp, re.IGNORECASE)
        if m:
            old_ans = m.group(2).upper()
            if old_ans != corr:
                # Replace with the real correct answer
                prefix = m.group(1)
                suffix = m.group(3)
                old_full = m.group(0)
                new_full = f"{prefix}{corr}'dir"
                q['explanation'] = exp.replace(old_full, new_full)
                fixed += 1

    with open(fpath, 'w', encoding='utf-8') as f:
        json.dump(questions, f, ensure_ascii=False, indent=2)

    print(f"{fpath}: Fixed {fixed} explanation mismatches.")
