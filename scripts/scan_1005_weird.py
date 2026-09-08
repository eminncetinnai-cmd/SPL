import json
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('src/data/all_questions.json', 'r', encoding='utf-8') as f:
    questions = json.load(f)

weird_words = [
    "çay", "kahve", "sohbet", "arkadaş", "hediye", "noter",
    "ilkokul", "milletvekili", "menü", "yemek", "polis", "muhtar",
    "tapu rengi", "ehliyet", "faks",
    "silinir", "yok olur", "yanar", "tatil", "hapse", "kovulur",
    "şirket bekçisi", "güvenlik görevlisi", "hava durumu", "şişman parmak"
]

all_flagged = {}

for mod in ['1001', '1003', '1005', '1012']:
    mod_qs = [q for q in questions if str(q.get('module_id')) == mod]
    flagged = []
    
    for q in mod_qs:
        opts = q.get('options', [])
        corr_k = q.get('correct_answer')
        corr_opt = next((o for o in opts if o['key'] == corr_k), None)
        if not corr_opt:
            flagged.append((q['id'], q['text'][:60], ["NO_CORRECT_OPTION"]))
            continue
            
        corr_text = corr_opt['text']
        wrong_opts = [o for o in opts if o['key'] != corr_k]
        wrong_lens = [len(o['text']) for o in wrong_opts]
        avg_wrong = sum(wrong_lens) / len(wrong_lens) if wrong_lens else 0
        
        reasons = []
        # Length bias
        if len(corr_text) > 85 and avg_wrong < 45:
            reasons.append(f"EXTREME_LENGTH_BIAS: Correct ({len(corr_text)} chars) vs wrong avg ({avg_wrong:.1f})")
        if len(corr_text) < 18 and avg_wrong > 50:
            reasons.append(f"REVERSE_LENGTH_BIAS: Correct ({len(corr_text)} chars) vs wrong avg ({avg_wrong:.1f})")
            
        # Silly terms
        for o in opts:
            for w in weird_words:
                if re.search(rf"\b{w}\b", o['text'].lower()):
                    reasons.append(f"SILLY: [{o['key']}] '{w}' in '{o['text'][:40]}'")
                    break
                    
        # Non-parallel (short numbers/tenures vs long sentences)
        is_num = bool(re.match(r'^(T\+\d|G\+\d|V\+\d|%\s*\d+([,.]\d+)?|\d+([,.]\d+)?\s*(gün|yıl|ay|saat|iş günü|TL|lira)?)$', corr_text.strip(), re.IGNORECASE))
        long_wrongs = [o for o in wrong_opts if len(o['text'].split()) > 7]
        if is_num and len(long_wrongs) >= 2:
            reasons.append(f"NON_PARALLEL: Correct is '{corr_text}' but wrong options are long statements")
            
        if reasons:
            flagged.append((q['id'], q['text'][:70], reasons))
            
    all_flagged[mod] = flagged
    print(f"Modül {mod} (Toplam {len(mod_qs)} soru): Kusurlu / Bayraklı Soru Sayısı = {len(flagged)}")

with open('scripts/all_flagged_report.txt', 'w', encoding='utf-8') as f:
    for mod, flist in all_flagged.items():
        f.write(f"\n{'='*60}\nMODUL {mod} - TOPLAM {len(flist)} KUSURLU SORU\n{'='*60}\n")
        for qid, qtext, reas in flist:
            f.write(f"\nID: {qid}\nSoru: {qtext}\nNedenler:\n")
            for r in reas:
                f.write(f"  - {r}\n")
                
print("\nRapor 'scripts/all_flagged_report.txt' dosyasına kaydedildi.")
