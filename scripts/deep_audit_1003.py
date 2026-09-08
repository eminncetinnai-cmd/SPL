import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('src/data/all_questions.json', 'r', encoding='utf-8') as f:
    all_qs = json.load(f)

q1003 = [q for q in all_qs if str(q.get('module_id', '')) == '1003']
print(f"Total 1003 questions: {len(q1003)}")

# Check for specific terms in 1003 questions:
audit_flags = []
for idx, q in enumerate(q1003, 1):
    qid = q['id']
    qtext = q.get('text', '')
    exp = q.get('explanation', '')
    full = (qtext + ' ' + exp).lower()
    
    flags = []
    # Check for outdated numbers or terms
    if 'yüklenim' in full and any(x in full for x in ['20 milyon', '40 milyon', '10 milyon']):
        flags.append("Eski yüklenim eşikleri (20/40 milyon yerine 2026: 750M / 1.5B TL)")
    if 'satışa hazır' in full and '40 milyon' in full:
        flags.append("Eski satışa hazır bekletilen pay eşiği (40M yerine 2026: 950M TL)")
    if 'girişim sermayesi pazarı' in full and any(x in full for x in ['20 milyon', '10 milyon']):
        flags.append("Eski GSP eşikleri (2026: 50M / 25M / 25M TL)")
    if 'pay satış bilgi formu' in full and '%10' in full and 'yüzde üç' not in full:
        flags.append("Pay satış bilgi formu eşiği (%10 yerine 2023 ilke kararı %3)")
    if 'virman' in full or '90 gün' in full or '180 gün' in full:
        flags.append("19/09/2024 i-SPK 128.23 kısıtlamaları")
        
    if flags:
        audit_flags.append((qid, qtext[:70], q.get('correct_answer'), flags))

print(f"\nFlagged existing questions: {len(audit_flags)}")
for qid, txt, ans, fl in audit_flags:
    print(f"[{qid}] {txt}... | Ans: {ans} | Flags: {fl}")

# Check options count and structure
structural_issues = []
for idx, q in enumerate(q1003, 1):
    opts = q.get('options', [])
    if len(opts) != 5:
        structural_issues.append(f"Q{idx} ({q['id']}): {len(opts)} options")
    opt_keys = [o['key'] for o in opts]
    if opt_keys != ['A', 'B', 'C', 'D', 'E']:
        structural_issues.append(f"Q{idx} ({q['id']}): invalid keys {opt_keys}")
    if q.get('correct_answer') not in ['A', 'B', 'C', 'D', 'E']:
        structural_issues.append(f"Q{idx} ({q['id']}): invalid answer {q.get('correct_answer')}")

print(f"Structural issues: {len(structural_issues)}")
for iss in structural_issues:
    print(" ", iss)
