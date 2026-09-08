import json
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('src/data/all_questions.json', 'r', encoding='utf-8') as f:
    questions = json.load(f)

mod_1012 = [q for q in questions if str(q.get('module_id')) == '1012']

print(f"Total questions in Module 1012: {len(mod_1012)}")

sources = {}
for q in mod_1012:
    src = q.get('source', 'unknown')
    sources[src] = sources.get(src, 0) + 1

print(f"Sources distribution: {sources}")

silly_patterns = [
    r"\bçay\b", r"\bkahve\b", r"\btatil\b", r"\bmadalya\b", r"\bhediye\b",
    r"\bnoter\b", r"\bmuhtar\b", r"\bpolis\b", r"\bimam\b", r"\bbelediye\b",
    r"\bhapse\b", r"\bkovul\b", r"\bkafasına göre\b", r"\bhiçbir şey yapmaz\b",
    r"\btelevizyon\b", r"\bgüvercin\b", r"\bel koy\b", r"\bikramiye\b",
    r"\bbatır\b", r"\bzengin\b", r"\bsevdiği\b", r"\byok olur\b", r"\byanar\b",
    r"\bsilinir\b", r"\bdondur\b", r"(?<![eE]-)\bposta\b", r"\btelefon\b", r"\bhaber\b",
    r"\bkaybol\b", r"\bçalar\b", r"\bkaçak\b", r"\bceza almaz\b", r"\bserbesttir\b"
]

flagged = []

for q in mod_1012:
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
    
    # 1. Reverse length bias
    if len(corr_text) < 20 and avg_wrong > 50:
        reasons.append(f"REVERSE_LENGTH_BIAS: Correct is '{corr_text}' ({len(corr_text)} chars) vs wrong avg {avg_wrong:.1f}")
        
    # 2. Extreme length bias
    if len(corr_text) > 80 and avg_wrong < 45:
        reasons.append(f"EXTREME_LENGTH_BIAS: Correct is {len(corr_text)} chars vs wrong avg {avg_wrong:.1f}")

    # 3. Silly patterns
    for o in opts:
        for pat in silly_patterns:
            if re.search(pat, o['text'].lower()):
                reasons.append(f"SILLY: [{o['key']}] '{o['text'][:40]}'")
                break
                
    # 4. Non-parallel options (numbers/days/hours vs long statements)
    is_corr_num = bool(re.match(r'^(T\+\d|%\s*\d+|\d+\s*(gün|yıl|ay|saat|iş günü|TL|lira))', corr_text.strip(), re.IGNORECASE))
    statement_wrongs = [o for o in wrong_opts if len(o['text'].split()) > 6]
    if is_corr_num and len(statement_wrongs) >= 2:
        reasons.append(f"NON_PARALLEL: Correct is '{corr_text}' but wrong options are long statements")

    if reasons:
        flagged.append((q, reasons))

print(f"\nTotal flagged questions in Module 1012: {len(flagged)}")
with open('scripts/flagged_1012.txt', 'w', encoding='utf-8') as out:
    for q, r in flagged:
        out.write(f"\n==================================================\n")
        out.write(f"ID: {q['id']} ({q.get('source')})\n")
        out.write(f"Soru: {q['text']}\n")
        out.write(f"Doğru: {q['correct_answer']}\n")
        for o in q['options']:
            mark = "✓" if o['key'] == q['correct_answer'] else " "
            out.write(f"  [{o['key']}] {mark} ({len(o['text']):3d} kr) {o['text']}\n")
        out.write(f"Nedenler: {', '.join(r)}\n")

print("Dumped flagged questions to scripts/flagged_1012.txt")
