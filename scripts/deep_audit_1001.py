import json
import sys

# Ensure UTF-8 output
sys.stdout.reconfigure(encoding='utf-8')

with open('src/data/all_questions.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

q1001 = [q for q in data if str(q.get('module_id', '')) == '1001']

print(f"Loaded {len(q1001)} questions for Module 1001.\n")

# Check for specific questions
audit_records = []
for q in q1001:
    qid = q['id']
    qtext = q.get('text', '')
    exp = q.get('explanation', '')
    full = (qtext + ' ' + exp).lower()
    
    # Flags to check
    flags = []
    if 'faaliyetten men' in full or 'faaliyetin geçici durdurulması' in full:
        flags.append("TSPB disiplin cezası terminology (faaliyetten men vs Birlik üyeliğinden çıkarma)")
    if '95' in full and ('çıkarma' in full or 'satma hakkı' in full or 'hakim ortak' in full):
        flags.append("Ortaklıktan çıkarma oranı (%95 vs %98)")
    if '10.000.000' in full or '15.000.000' in full or '5.000.000' in full:
        flags.append("Parasal tutar kontrolü")
    if 'kitle fonlama' in full:
        flags.append("Kitle fonlama")
    if 'kripto' in full:
        flags.append("Kripto")
        
    if flags:
        audit_records.append((qid, qtext, q.get('correct_answer'), exp, flags))

print(f"Total flagged existing questions: {len(audit_records)}\n")
for qid, qtext, ans, exp, flags in audit_records:
    print(f"ID: {qid} | Flags: {flags}")
    print(f"Text: {qtext}")
    print(f"Ans: {ans}")
    print(f"Exp: {exp[:200]}...")
    print("-" * 60)
