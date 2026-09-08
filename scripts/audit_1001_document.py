import json
import re

with open('src/data/all_questions.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

q1001 = [q for q in data if str(q.get('module_id', '')) == '1001']

print(f"Total 1001 questions: {len(q1001)}")

# Check sources
sources = {}
for q in q1001:
    s = q.get('source', 'unknown')
    sources[s] = sources.get(s, 0) + 1
print("Sources distribution:", sources)

# Check options count and duplicate options
issues = []
for idx, q in enumerate(q1001, 1):
    opts = q.get('options', [])
    if len(opts) != 5:
        issues.append(f"Q{idx} ({q['id']}): has {len(opts)} options, expected 5")
    texts = [o['text'].strip() for o in opts]
    if len(set(texts)) != len(texts):
        issues.append(f"Q{idx} ({q['id']}): duplicate options found")
    ans = q.get('correct_answer')
    if ans not in ['A', 'B', 'C', 'D', 'E']:
        issues.append(f"Q{idx} ({q['id']}): invalid correct_answer {ans}")
    if not q.get('explanation'):
        issues.append(f"Q{idx} ({q['id']}): empty explanation")

print(f"Basic validation issues: {len(issues)}")
for iss in issues[:10]:
    print(" ", iss)

# Check specifically for known potential discrepancies with the official document:
# 1. Ortaklıktan çıkarma / satma hakkı oy hakkı oranı: In II-27.3 it is 98% (not 95%)
# 2. İdari sorumlular ve ana ortak işlem açıklama sınırı: 2026 yılı için 15.000.000 TL
# 3. Kripto varlık hizmet sağlayıcılar: 7518 sayılı Kanun (02.07.2024), Tebliğler III-35/B.1 ve III-35/B.2 (13.03.2025)
#    Zimmet (SPKn 110/A: 8-14 yıl / nitelikli 14-20 yıl, 3 katı APC), İzinsiz KVHS faaliyeti (SPKn 109/A: 3-5 yıl hapis, 5.000-10.000 gün APC)
#    Şahsi iflas ve sorumluluk (SPKn 110/B)
#    TÜBİTAK kriterleri, MKK entegrasyonu
# 4. Teminat Yöneticisi ve Sözleşmesi: SPKn md. 31/B (teminat yöneticisi genel saklama yetkili yatırım kuruluşu, ticaret siciline tescil ve TTSG ilan, TCK 155/2 cezası en az 5 yıl!)
# 5. Borçlanma Aracı Sahipleri Kurulu: SPKn md. 31/A (asgari yarısının olumlu oyu, temerrütte takiplerin durması, tedbir/haciz uygulanmaması)
# 6. Fon toplam gideri azami oranları (Para Piyasası %1,65, Koruma/Garantili/Kıymetli Maden/Endeks %2,19, Kısa Vadeli Borçlanma %2,56, Fon Sepeti %4,38, Diğer %3,65)
# 7. TSPB Disiplin Komitesi üye yapısı: 7 üye (2 aracı kurum, 1 banka, 1 PYŞ, 1 payları borsada işlem gören YO, 1 kripto varlık hizmet sağlayıcı, 1 kitle fonlama platformu; görev süresi 2 yıl, raportör Hukuk İşleri Müdürü)
# 8. Sürdürülebilirlik Uyum Çerçevesi & Yeşil Borçlanma Aracı Rehberi

print("\n--- Scanning for specific terms in existing questions ---")
checks = {
    'kripto': 0,
    'teminat yöneticisi': 0,
    '31/b': 0,
    '31/a': 0,
    'borçlanma aracı sahipleri kurulu': 0,
    '110/a': 0,
    '110/b': 0,
    '109/a': 0,
    'tübitak': 0,
    '%98': 0,
    '%95': 0,
    '15.000.000': 0,
    'şemsiye fon': 0,
    'fon sepeti': 0,
    'fon toplam gider': 0,
    'yeşil borçlanma': 0,
    'sürdürülebilirlik': 0,
    'disiplin komitesi': 0,
    '7 üye': 0
}

for q in q1001:
    full_text = (q.get('text', '') + ' ' + q.get('explanation', '') + ' ' + ' '.join(o['text'] for o in q.get('options', []))).lower()
    for term in checks:
        if term in full_text:
            checks[term] += 1

for term, count in checks.items():
    print(f"  '{term}': {count} questions")
