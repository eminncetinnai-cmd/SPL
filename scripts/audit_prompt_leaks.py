import json
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('src/data/all_questions.json', 'r', encoding='utf-8') as f:
    questions = json.load(f)

print(f"Auditing all {len(questions)} questions for prompt-answer leaks and asymmetric options:\n")

prompt_leaks = []
asymmetric_options = []

for q in questions:
    corr_key = q['correct_answer']
    corr_opt = next((o for o in q['options'] if o['key'] == corr_key), None)
    if not corr_opt:
        continue
    
    # 1. Prompt leak check: does the question prompt literally say the answer?
    q_clean = q['text'].lower()
    c_clean = corr_opt['text'].lower()
    
    # Ignore single common words like "hangisidir", "kurul", "pay"
    words = re.findall(r'\b[a-zçğıöşü]{4,}\b', c_clean)
    # Check for bigrams or trigrams in prompt
    for i in range(len(words)-1):
        bigram = f"{words[i]} {words[i+1]}"
        if bigram in q_clean and len(bigram) > 10:
            # e.g. "eser sözleşmesine"
            if bigram not in ['aşağıdakilerden hangisidir', 'hangisi doğrudur', 'hangisi yanlıştır']:
                prompt_leaks.append({
                    'id': q['id'],
                    'module': q['module_id'],
                    'bigram': bigram,
                    'prompt': q['text'][:80],
                    'answer': corr_opt['text']
                })
                break

    # 2. Asymmetric option lengths: correct answer is more than 3x longer than average of wrong answers
    wrong_lens = [len(o['text']) for o in q['options'] if o['key'] != corr_key]
    avg_wrong = sum(wrong_lens) / len(wrong_lens) if wrong_lens else 0
    if avg_wrong > 0 and len(corr_opt['text']) > 3 * avg_wrong and len(corr_opt['text']) > 40:
        asymmetric_options.append({
            'id': q['id'],
            'module': q['module_id'],
            'corr_len': len(corr_opt['text']),
            'avg_wrong': avg_wrong,
            'answer': corr_opt['text'][:60],
            'prompt': q['text'][:70]
        })

print(f"Found {len(prompt_leaks)} questions where prompt contains significant keyphrase of the correct answer:")
for p in prompt_leaks[:15]:
    print(f"  [{p['id']}] Match: '{p['bigram']}'")
    print(f"     Soru  : {p['prompt']}")
    print(f"     Cevap : {p['answer']}")

print(f"\nFound {len(asymmetric_options)} questions with heavily asymmetric correct answer length:")
for a in asymmetric_options[:15]:
    print(f"  [{a['id']}] Corr len: {a['corr_len']} vs Wrong avg: {a['avg_wrong']:.1f}")
    print(f"     Soru  : {a['prompt']}")
    print(f"     Cevap : {a['answer']}")
