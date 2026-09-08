import json, re

with open('src/data/questions_master.json', 'r', encoding='utf-8') as f:
    qs = json.load(f)

m1012 = [q for q in qs if str(q.get('module_id')) == '1012']

print('--- LENGTH OUTLIERS (>1.8x) ---')
outliers = []
for q in m1012:
    opts = q['options']
    c_key = q['correct_answer']
    c_opt = next((o for o in opts if o['key'] == c_key), None)
    if not c_opt: continue
    c_len = len(c_opt['text'])
    wrong_lens = [len(o['text']) for o in opts if o['key'] != c_key]
    avg_wrong = sum(wrong_lens) / len(wrong_lens) if wrong_lens else 1
    if c_len > 1.8 * avg_wrong and c_len > 60:
        outliers.append((q['id'], round(c_len/avg_wrong, 2), c_opt['text']))
        print(f"{q['id']} | ratio={c_len/avg_wrong:.2f} | C: {c_opt['text'][:70]}...")

print(f"\nTotal outliers (>1.8x): {len(outliers)}")

print('\n--- GIVEAWAY PARENTHETICALS ---')
giveaways = []
for q in m1012:
    opts = q['options']
    c_key = q['correct_answer']
    c_opt = next((o for o in opts if o['key'] == c_key), None)
    c_has_paren = bool(re.search(r'\(.*?\)', c_opt['text']))
    wrong_has_paren = any(re.search(r'\(.*?\)', o['text']) for o in opts if o['key'] != c_key)
    if c_has_paren and not wrong_has_paren:
        giveaways.append((q['id'], c_opt['text']))

print(f"Total giveaway parentheticals: {len(giveaways)}")
for gid, gtxt in giveaways[:15]:
    print(f"  {gid} | {gtxt}")
