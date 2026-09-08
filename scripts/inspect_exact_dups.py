import json
from collections import defaultdict

with open('src/data/all_questions.json', encoding='utf-8') as f:
    questions = json.load(f)

# Group by normalized text
def norm(t):
    return ''.join(c.lower() for c in t if c.isalnum())

by_text = defaultdict(list)
for q in questions:
    by_text[norm(q['text'])].append(q)

dups = {k: v for k, v in by_text.items() if len(v) > 1}
print(f"Total unique question texts: {len(by_text)} out of {len(questions)} total questions")
print(f"Total duplicate text clusters: {len(dups)}")

master_dups = 0
ogretici_dups = 0
cross_dups = 0

for k, group in dups.items():
    sources = set(g['source'] for g in group)
    if sources == {'master'}:
        master_dups += len(group)
    elif sources == {'ogretici'}:
        ogretici_dups += len(group)
    else:
        cross_dups += len(group)

print(f"Duplicates purely within Master bank: {master_dups}")
print(f"Duplicates purely within Öğretici bank: {ogretici_dups}")
print(f"Duplicates across Master <-> Öğretici: {cross_dups}")

# Inspect some sample duplicates in Öğretici
print("\nSample duplicates in Öğretici:")
ogretici_samples = [v for v in dups.values() if any(g['source'] == 'ogretici' for g in v)]
for s in ogretici_samples[:5]:
    print(f"- Text: {s[0]['text'][:80]}...")
    for q in s:
        print(f"   ID: {q['id']}, Module: {q['module_id']}, Source: {q['source']}")

# Inspect some sample duplicates in Master
print("\nSample duplicates in Master:")
master_samples = [v for v in dups.values() if all(g['source'] == 'master' for g in v)]
for s in master_samples[:5]:
    print(f"- Text: {s[0]['text'][:80]}...")
    for q in s:
        print(f"   ID: {q['id']}, Module: {q['module_id']}, Source: {q['source']}")
