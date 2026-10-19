import json
import sys

def validate_questions(file_path, expected_count=50, expected_mod=None):
    with open(file_path, 'r', encoding='utf-8') as f:
        qs = json.load(f)
        
    print(f"\n--- VALIDATING {file_path} ({len(qs)} questions) ---")
    errors = []
    
    if len(qs) != expected_count:
        errors.append(f"Count mismatch: expected {expected_count}, got {len(qs)}")
        
    key_counts = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0}
    ids = set()
    giveaway_words = ['yukarıdakilerin hepsi', 'yukarıdakilerin tamamı', 'hiçbiri', 'a ve b', 'b ve c', 'c ve d', 'a ve c', 'hepsi', 'tamamı']
    
    stages = [
        "1. MEVZUAT DAYANAĞI",
        "2. HUKUKİ",
        "3. ADIM ADIM",
        "4. DOĞRU CEVAP",
        "5. ÇELDİRİCİ TUZAĞI"
    ]
    
    for i, q in enumerate(qs):
        qid = q.get('id', f'idx_{i}')
        if qid in ids:
            errors.append(f"{qid}: Duplicate ID")
        ids.add(qid)
        
        if expected_mod and q.get('module_id') != expected_mod:
            errors.append(f"{qid}: Expected module {expected_mod}, got {q.get('module_id')}")
            
        corr = q.get('correct_answer')
        if corr not in key_counts:
            errors.append(f"{qid}: Invalid correct_answer '{corr}'")
        else:
            key_counts[corr] += 1
            
        opts = q.get('options', [])
        if len(opts) != 5:
            errors.append(f"{qid}: Expected 5 options, got {len(opts)}")
            
        opt_keys = [o.get('key') for o in opts]
        if opt_keys != ['A', 'B', 'C', 'D', 'E']:
            errors.append(f"{qid}: Option keys not A-E: {opt_keys}")
            
        opt_dict = {o['key']: o['text'] for o in opts if 'key' in o and 'text' in o}
        
        # Giveaway check
        for k, text in opt_dict.items():
            t_low = text.strip().lower()
            for gw in giveaway_words:
                if t_low == gw or t_low.startswith(gw + " ") or t_low.endswith(" " + gw):
                    errors.append(f"{qid}: Giveaway found in option {k}: '{text}'")
                    
        # Length outlier check
        if corr in opt_dict:
            c_len = len(opt_dict[corr])
            w_lens = [len(v) for k, v in opt_dict.items() if k != corr]
            if w_lens:
                avg_w = sum(w_lens) / len(w_lens)
                if avg_w > 0 and (c_len / avg_w) > 1.8:
                    errors.append(f"{qid}: Length outlier ratio {c_len / avg_w:.2f} (corr {c_len} chars vs avg wrong {avg_w:.1f} chars)")
                    
        # Explanation check
        exp = q.get('explanation', '')
        for stage in stages:
            if stage not in exp:
                errors.append(f"{qid}: Explanation missing stage keyword '{stage}'")
                
        # Trap check
        if not q.get('trap'):
            errors.append(f"{qid}: Missing trap field")
            
        # Skill check
        skill = q.get('cognitive_skill')
        if skill not in ['KB1_Kavramsal', 'KB2_Muhakeme', 'KB3_Vaka']:
            errors.append(f"{qid}: Invalid cognitive_skill '{skill}'")
            
    print(f"Key distribution: {key_counts}")
    if any(c != 10 for c in key_counts.values()) and expected_count == 50:
        print(f"WARNING: Key distribution not strictly balanced (10 each): {key_counts}")
        
    if errors:
        print(f"FAILED with {len(errors)} errors:")
        for err in errors[:20]:
            print(f"  [ERROR] {err}")
        if len(errors) > 20:
            print(f"  ... and {len(errors) - 20} more errors.")
        return False
    else:
        print("ALL CHECKS PASSED (100% SUCCESS)!")
        return True

if __name__ == '__main__':
    target_file = sys.argv[1] if len(sys.argv) > 1 else 'scripts/data_1001_hard.json'
    mod = sys.argv[2] if len(sys.argv) > 2 else '1001'
    res = validate_questions(target_file, expected_count=50, expected_mod=mod)
    sys.exit(0 if res else 1)
