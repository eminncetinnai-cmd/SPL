import json
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('src/data/all_questions.json', 'r', encoding='utf-8') as f:
    qs = json.load(f)

mismatches = []
broken_endings = []
suspicious_options = []

for q in qs:
    opts = [o['text'].strip() for o in q['options']]
    lengths = [len(o) for o in opts]
    
    # 1. Look for questions where some options are numbers/single words while others are long sentences
    # e.g., options like "10 Yıl", "5 Yıl", "1 Yıl", but one option is "Şirket yönetim kurulu kararıyla..."
    # or options are long sentences, but one option is just "25 Milyon TL"
    is_short = [len(o.split()) <= 3 for o in opts]
    if any(is_short) and not all(is_short):
        # Count how many are short vs long
        short_count = sum(is_short)
        long_count = len(opts) - short_count
        if short_count in [1, 2] and long_count in [3, 4]:
            avg_long = sum(lengths[i] for i, s in enumerate(is_short) if not s) / long_count
            avg_short = sum(lengths[i] for i, s in enumerate(is_short) if s) / short_count
            if avg_long > 40 and avg_short < 15:
                mismatches.append({
                    'id': q['id'],
                    'module': q['module_id'],
                    'text': q['text'],
                    'options': opts,
                    'correct': q['correct_answer'],
                    'issue': f'Mixed types: {short_count} short vs {long_count} long sentences'
                })

    # 2. Check for broken/truncated sentence endings
    for idx, o in enumerate(opts):
        # Ends with dangling conjunction or preposition
        if re.search(r'\b(ile|ve|veya|veya|için|olarak|tarafından|göre|bu|bir|şu)\s*$', o, re.IGNORECASE):
            broken_endings.append({
                'id': q['id'],
                'option': chr(65 + idx),
                'text': o,
                'issue': 'Dangling word at end'
            })
        elif o.endswith((',', '-', ':', ';', '...')):
            broken_endings.append({
                'id': q['id'],
                'option': chr(65 + idx),
                'text': o,
                'issue': 'Trailing punctuation'
            })
        elif len(o.split()) > 2:
            last_word = o.split()[-1].strip('.,!?;:"()[]')
            # Check if last word is a single or 2-letter fragment that is not a known Turkish abbreviation
            if len(last_word) <= 2 and last_word.lower() not in ['tl', 'ay', 'yıl', 'gün', 'm.', 'oy', 've', 'ek', 'ön', 'iç', 'dış', 'öz', 'net', 'tam', 'üst', 'alt', 'ilk', 'son']:
                broken_endings.append({
                    'id': q['id'],
                    'option': chr(65 + idx),
                    'text': o,
                    'issue': f'Suspicious short ending word: "{last_word}"'
                })

print(f"Total questions analyzed: {len(qs)}")
print(f"Total type/length mismatches detected: {len(mismatches)}")
for m in mismatches[:10]:
    print(f"\n[MISMATCH] {m['id']} (Modül {m['module']})")
    print(f"  Soru: {m['text'][:80]}...")
    for idx, o in enumerate(m['options']):
        print(f"    {chr(65+idx)}) [{len(o)} kr] {o}")

print(f"\nTotal broken endings detected: {len(broken_endings)}")
for b in broken_endings[:15]:
    print(f"  [ENDING] {b['id']} ({b['option']}) [{b['issue']}]: \"{b['text']}\"")
