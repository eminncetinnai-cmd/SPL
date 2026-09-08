import json
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('src/data/all_questions.json', 'r', encoding='utf-8') as f:
    questions = json.load(f)

mod_1005_questions = [q for q in questions if str(q.get('module_id')) == '1005']

print(f"Total 1005 questions: {len(mod_1005_questions)}")

# Let's inspect all 1005 questions and check for any distractor quality issues:
# 1. Reverse length bias (correct option is tiny like '7 yıl' while 4 wrong options are 100-char paragraphs copied from elsewhere!)
# 2. Extreme length bias (correct option is 150+ chars, wrong options are 20-30 chars)
# 3. Silly/unrealistic distractors (e.g. notary clerk, notary, mayor, police, madalya, etc.)
# 4. Inconsistent option types (e.g., question asks for a percentage or year or institution, but options are full policy sentences)

issues = []

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
    
    q_issues = []
    
    # Check 1: Wrong options are huge paragraphs copied from elsewhere (reverse length bias)
    # e.g., question asks for a number/year, but wrong options are 100-char regulatory paragraphs!
    if len(corr_text) < 20 and avg_wrong > 60:
        q_issues.append(f"REVERSE_LENGTH_BIAS: Correct is '{corr_text}' ({len(corr_text)} chars) but wrong options are long paragraphs (avg {avg_wrong:.1f} chars).")
        
    # Check 2: Correct option is a huge paragraph while wrong options are short trivial phrases
    if len(corr_text) > 80 and avg_wrong < 40:
        q_issues.append(f"EXTREME_LENGTH_BIAS: Correct is {len(corr_text)} chars, wrong avg is {avg_wrong:.1f} chars.")

    # Check 3: Check for silly/informal/unrealistic distractors
    silly_patterns = [
        r"\bçay\b", r"\bkahve\b", r"\btatil\b", r"\bmadalya\b", r"\bhediye\b",
        r"\bnoter\b", r"\bmuhtar\b", r"\bpolis\b", r"\bimam\b", r"\bbelediye\b",
        r"\bhapse\b", r"\bkovul\b", r"\bkafasına göre\b", r"\bhiçbir şey yapmaz\b",
        r"\btelevizyon\b", r"\bgüvercin\b", r"\bel koy\b"
    ]
    for o in opts:
        for pat in silly_patterns:
            if re.search(pat, o['text'].lower()):
                q_issues.append(f"SILLY_DISTRACTOR in [{o['key']}]: '{o['text']}'")
                
    # Check 4: Non-parallel options (e.g. correct is a number/time, wrong is a statement)
    # or vice versa
    is_corr_num = bool(re.match(r'^(%\s*\d+|\d+\s*(gün|yıl|ay|saat|TL|lira|kat|puan))', corr_text.strip(), re.IGNORECASE))
    statement_wrongs = [o for o in wrong_opts if len(o['text'].split()) > 7]
    if is_corr_num and len(statement_wrongs) >= 2:
        q_issues.append(f"NON_PARALLEL: Correct is number/time '{corr_text}', but wrong options are full statements!")

    if q_issues:
        issues.append({
            "id": q['id'],
            "source": q.get('source'),
            "text": q['text'],
            "correct_answer": corr_k,
            "correct_text": corr_text,
            "options": opts,
            "issues": q_issues
        })

print(f"Found {len(issues)} problematic questions in Module 1005.\n")
for it in issues:
    print(f"[{it['id']}] ({it['source']}) {it['text'][:80]}...")
    for iss in it['issues']:
        print(f"   -> {iss}")
