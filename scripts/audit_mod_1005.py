import json
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('src/data/all_questions.json', 'r', encoding='utf-8') as f:
    questions = json.load(f)

mod_1005_questions = [q for q in questions if str(q.get('module_id')) == '1005']

print(f"Total questions in Module 1005: {len(mod_1005_questions)}")

# Categorize by source
sources = {}
for q in mod_1005_questions:
    src = q.get('source', 'unknown')
    sources[src] = sources.get(src, 0) + 1

print(f"Sources distribution: {sources}")

# Check for potential issues:
# 1. Obvious length disparities
# 2. Silly / non-academic terms
# 3. Predictable patterns

silly_terms = [
    "çay", "kahve", "tatil", "güvercin", "madalya", "hediye", "televizyon",
    "polis", "muhtar", "noter", "imam", "belediye", "maaş", "ikramiye",
    "istifa", "kovulur", "kapatır gider", "hiçbir şey", "emir kulu",
    "silinir", "yok sayılır", "el konur", "hapse atılır", "dondurur",
    "yasaklanır", "ceza almaz", "bedava", "serbesttir", "kafasına göre"
]

flagged = []

for q in mod_1005_questions:
    qid = q['id']
    corr_key = q['correct_answer']
    opts = q['options']
    corr_opt = next((o for o in opts if o['key'] == corr_key), None)
    
    reasons = []
    
    # Check length disparity
    lens = [len(o['text']) for o in opts]
    corr_len = len(corr_opt['text']) if corr_opt else 0
    wrong_lens = [len(o['text']) for o in opts if o['key'] != corr_key]
    avg_wrong = sum(wrong_lens) / len(wrong_lens) if wrong_lens else 0
    
    if avg_wrong > 0 and corr_len > 2.5 * avg_wrong and corr_len > 50:
        reasons.append(f"Length bias: correct is {corr_len} chars vs wrong avg {avg_wrong:.1f} chars")
    elif avg_wrong > 0 and avg_wrong > 2.5 * corr_len and avg_wrong > 50:
        reasons.append(f"Reverse length bias: correct is {corr_len} chars vs wrong avg {avg_wrong:.1f} chars")
        
    # Check silly terms
    found_silly = []
    for o in opts:
        for st in silly_terms:
            if re.search(rf"\b{st}\b", o['text'].lower()):
                found_silly.append(f"{o['key']}: '{st}' in '{o['text']}'")
    if found_silly:
        reasons.append("Silly/informal terms: " + "; ".join(found_silly))
        
    # Check for lazy distractors like "Hiçbiri", "Hepsi", or single word vs full sentence
    single_word_wrong = [o for o in opts if o['key'] != corr_key and len(o['text'].split()) <= 2]
    if len(single_word_wrong) >= 3 and len(corr_opt['text'].split()) > 8:
        reasons.append(f"Lazy distractors: {len(single_word_wrong)} wrong options are <=2 words while correct is {len(corr_opt['text'].split())} words")

    if reasons:
        flagged.append((q, reasons))

print(f"\nTotal flagged questions in Module 1005: {len(flagged)}")
for q, r in flagged:
    print(f"\n[{q['id']}] ({q.get('source')}) Soru: {q['text']}")
    print(f"  Doğru: {q['correct_answer']}")
    for o in q['options']:
        mark = "✓" if o['key'] == q['correct_answer'] else " "
        print(f"    [{o['key']}] {mark} ({len(o['text']):3d} kr) {o['text']}")
    for reason in r:
        print(f"  ⚠️ {reason}")
