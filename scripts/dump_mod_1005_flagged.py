import json
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('src/data/all_questions.json', 'r', encoding='utf-8') as f:
    questions = json.load(f)

mod_1005_questions = [q for q in questions if str(q.get('module_id')) == '1005']

silly_patterns = [
    r"\bçay\b", r"\bkahve\b", r"\btatil\b", r"\bmadalya\b", r"\bhediye\b",
    r"\bnoter\b", r"\bmuhtar\b", r"\bpolis\b", r"\bimam\b", r"\bbelediye\b",
    r"\bhapse\b", r"\bkovul\b", r"\bkafasına göre\b", r"\bhiçbir şey yapmaz\b",
    r"\btelevizyon\b", r"\bgüvercin\b", r"\bel koy\b"
]

flagged = []
for q in mod_1005_questions:
    opts = q['options']
    corr_k = q['correct_answer']
    corr_opt = next((o for o in opts if o['key'] == corr_k), None)
    if not corr_opt:
        continue
    corr_text = corr_opt['text']
    wrong_opts = [o for o in opts if o['key'] != corr_k]
    wrong_lens = [len(o['text']) for o in wrong_opts]
    avg_wrong = sum(wrong_lens) / len(wrong_lens) if wrong_lens else 0
    
    reasons = []
    if len(corr_text) < 20 and avg_wrong > 60:
        reasons.append("REVERSE_LENGTH_BIAS")
    if len(corr_text) > 80 and avg_wrong < 40:
        reasons.append("EXTREME_LENGTH_BIAS")
    for o in opts:
        for pat in silly_patterns:
            if re.search(pat, o['text'].lower()):
                reasons.append(f"SILLY: [{o['key']}] {o['text']}")
    is_corr_num = bool(re.match(r'^(%\s*\d+|\d+\s*(gün|yıl|ay|saat|TL|lira|kat|puan))', corr_text.strip(), re.IGNORECASE))
    statement_wrongs = [o for o in wrong_opts if len(o['text'].split()) > 7]
    if is_corr_num and len(statement_wrongs) >= 2:
        reasons.append("NON_PARALLEL")
        
    if reasons:
        flagged.append((q, reasons))

with open('scripts/flagged_1005.txt', 'w', encoding='utf-8') as out:
    out.write(f"Total flagged: {len(flagged)}\n")
    for q, r in flagged:
        out.write(f"\n==================================================\n")
        out.write(f"ID: {q['id']} ({q.get('source')})\n")
        out.write(f"Soru: {q['text']}\n")
        out.write(f"Doğru: {q['correct_answer']}\n")
        for o in q['options']:
            mark = "✓" if o['key'] == q['correct_answer'] else " "
            out.write(f"  [{o['key']}] {mark} {o['text']}\n")
        out.write(f"Nedenler: {', '.join(r)}\n")

print(f"Dumped {len(flagged)} questions to scripts/flagged_1005.txt")
