# -*- coding: utf-8 -*-
import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('src/data/topic_notes.json', 'r', encoding='utf-8') as f:
    tn = json.load(f)

for mod, data in tn.items():
    print(f"\n{'='*60}\nMODUL {mod}: {data.get('title')}\n{'='*60}")
    for s in data.get('sections', []):
        print(f"\nID: {s['id']} | Başlık: {s['title']}")
        print(f"  Paragraf Sayısı: {len(s.get('content', []))}")
        print("  Örnekler:")
        for ex in s.get('concrete_examples', []):
            print(f"    - {ex[:100]}...")
        print("  Sınav Tuzakları:")
        for tr in s.get('exam_traps', []):
            print(f"    - {tr[:100]}...")
        print("  Özet Çıkarımlar:")
        for tk in s.get('key_takeaways', []):
            print(f"    - {tk[:100]}...")
