import json
import re
import sys
from collections import defaultdict

sys.stdout.reconfigure(encoding='utf-8')

ABBREVIATIONS = {
    "MKK": "Merkezi Kayıt Kuruluşu A.Ş. (Türkiye'nin Merkezi Saklama Kuruluşu ve Hak Sahipliği Sicili)",
    "CCP": "Merkezi Karşı Taraf (Central Counterparty - Takas odasının alıcıya karşı satıcı, satıcıya karşı alıcı olması)",
    "MKT": "Merkezi Karşı Taraf (Central Counterparty - Takas odasının takasın tamamlanmasını mali olarak garanti etmesi)",
    "Takasbank": "İstanbul Takas ve Saklama Bankası A.Ş. (Merkezi Takas Kuruluşu)",
    "SPK": "Sermaye Piyasası Kurulu (Sermaye piyasalarının düzenleyici ve denetleyici kamu otoritesi)",
    "SPKn": "6362 sayılı Sermaye Piyasası Kanunu",
    "BIST": "Borsa İstanbul A.Ş. (Türkiye'nin organize menkul kıymet, kıymetli maden ve türev piyasası borsası)",
    "BİST": "Borsa İstanbul A.Ş. (Türkiye'nin organize piyasası)",
    "TSPB": "Türkiye Sermaye Piyasaları Birliği (Öz düzenleyici meslek kuruluşu)",
    "YTM": "Yatırımcı Tazmin Merkezi (Aracı kurumların iflası/tasfiyesinde yatırımcı varlıklarını tazmin eden kurum)",
    "BDDK": "Bankacılık Düzenleme ve Denetleme Kurumu",
    "TCMB": "Türkiye Cumhuriyet Merkez Bankası",
    "KAP": "Kamuyu Aydınlatma Platformu (Şirketlerin özel durum ve finansal rapor bildirim sistemi)",
    "TEFAS": "Türkiye Elektronik Fon Alım Satım Platformu (Yatırım fonlarının merkezi alım-satım sistemi)",
    "VİOP": "Vadeli İşlem ve Opsiyon Piyasası (BIST bünyesindeki türev araçlar piyasası)",
    "VDMK": "Varlığa Dayalı Menkul Kıymet (Alacak havuzları teminatıyla ihraç edilen borçlanma aracı)",
    "İTMK": "İpotek Teminatlı Menkul Kıymet (Konut ve gayrimenkul kredileri teminatlı menkul kıymet)",
    "BYF": "Borsa Yatırım Fonu (Borsada hisse senedi gibi anlık işlem gören endeks fonu - ETF)",
    "ETF": "Exchange Traded Fund (Borsa Yatırım Fonu)",
    "DVP": "Teslim Karşılığı Ödeme (Delivery Versus Payment - Menkul kıymet teslimi ile nakit ödemenin eşanlı yapılması)",
    "NAD": "Net Aktif Değeri (Fon toplam varlıklarından borçların düşülmesiyle bulunan pay fiyatı - NAV)",
    "NAV": "Net Asset Value (Net Aktif Değeri)",
    "ELÜS": "Elektronik Ürün Senedi (Lisanslı depolarda saklanan tarım ürünlerini temsil eden kıymetli evrak)",
    "TÜRİB": "Türkiye Ürün İhtisas Borsası A.Ş.",
    "ÖPA": "Ödünç Pay Piyasası (Açığa satış veya teslim yükümlülüğü için hisse ödünç alınan Takasbank piyasası)",
    "TPP": "Takasbank Para Piyasası (Üyelerin karşılıklı Türk Lirası likidite borçlanıp borç verdiği piyasa)",
    "DİBS": "Devlet İç Borçlanma Senetleri (Hazine Müsteşarlığı/Bakanlığı tarafından ihraç edilen Bono ve Tahviller)",
    "GYO": "Gayrimenkul Yatırım Ortaklığı (Portföyünün en az %51'i gayrimenkulden oluşan sermaye piyasası kurumu)",
    "GSYF": "Girişim Sermayesi Yatırım Fonu (Büyüme potansiyeli olan şirketlere ortak olan fon)",
    "GSYO": "Girişim Sermayesi Yatırım Ortaklığı",
    "PDT": "Paylara Dönüştürülebilir Tahvil (Vadesinde hisse senedine dönüştürülme hakkı veren borçlanma aracı)",
    "TTK": "6102 sayılı Türk Ticaret Kanunu",
    "TMS": "Türkiye Muhasebe Standartları",
    "TFRS": "Türkiye Finansal Raporlama Standartları",
    "MASAK": "Mali Suçları Araştırma Kurulu (Karapara aklama ve terörün finansmanıyla mücadele otoritesi)",
    "FX": "Forex / Kaldıraçlı Alım Satım İşlemleri (Foreign Exchange)",
    "Forex": "Kaldıraçlı Döviz ve Emtia Alım Satım Piyasası",
    "KİS": "Katılma İntifa Senedi (Şirket ortaklığı vermeksizin sadece kardan pay alma hakkı veren senet)",
    "GOS": "Gelir Ortaklığı Senedi (Altyapı tesislerinin gelirlerine ortaklık sağlayan senet)",
    "VKŞ": "Varlık Kiralama Şirketi (Kira sertifikası - Sukuk ihraç etmek üzere kurulan özel şirket)",
    "DBS": "Doğrudan Borçlandırma Sistemi",
    "EFT": "Elektronik Fon Transferi",
    "OTC": "Tezgahüstü Piyasa (Over-The-Counter - Borsa dışı serbest piyasa işlemleri)",
    "KYK": "Kolektif Yatırım Kuruluşları (Yatırım Fonları ve Yatırım Ortaklıkları)",
    "PYŞ": "Portföy Yönetim Şirketi (Fon ve portföyleri yönetmekle münhasıran yetkili kurum)"
}

with open('src/data/all_questions.json', 'r', encoding='utf-8') as f:
    qs = json.load(f)

print(f"Loaded {len(qs)} questions.")

enriched_count = 0

for q in qs:
    full_text = q['text'] + ' ' + ' '.join(opt['text'] for opt in q['options']) + ' ' + q.get('explanation', '')
    
    # Identify matching abbreviations (use word boundaries)
    found_abbrs = []
    for abbr, desc in ABBREVIATIONS.items():
        # Match whole word
        pattern = r'\b' + re.escape(abbr) + r'\b'
        if re.search(pattern, full_text):
            found_abbrs.append((abbr, desc))
            
    if found_abbrs:
        # Check if explanation already has glossary
        expl = q.get('explanation', '')
        if "📌 Soruda Geçen Kısaltmalar" in expl or "📌 Terim & Kısaltma Sözlüğü" in expl:
            # Remove previous glossary if any to regenerate cleanly
            expl = re.split(r'\n+📌', expl)[0].strip()
            
        glossary_lines = ["\n\n📌 Soruda Geçen Kısaltmalar & Terimler:"]
        for abbr, desc in found_abbrs:
            glossary_lines.append(f"• {abbr}: {desc}")
            
        q['explanation'] = expl + '\n'.join(glossary_lines)
        enriched_count += 1

print(f"Enriched {enriched_count} questions with comprehensive abbreviation definitions!")

# Check sample
sample_q = next((q for q in qs if 'MKK' in q['text'] or 'CCP' in q['text']), None)
if sample_q:
    print("\n--- SAMPLE ENRICHED EXPLANATION ---")
    print("ID:", sample_q['id'])
    print("Text:", sample_q['text'][:80])
    print("Explanation:\n", sample_q['explanation'])
    print("-----------------------------------")

# Save updated files
with open('src/data/all_questions.json', 'w', encoding='utf-8') as f:
    json.dump(qs, f, ensure_ascii=False, indent=2)

with open('src/data/questions_master.json', 'w', encoding='utf-8') as f:
    json.dump([q for q in qs if q.get('source') == 'master'], f, ensure_ascii=False, indent=2)

with open('src/data/questions_cikmis.json', 'w', encoding='utf-8') as f:
    json.dump([q for q in qs if q.get('source') == 'cikmis'], f, ensure_ascii=False, indent=2)

print("Saved all_questions.json, questions_master.json, and questions_cikmis.json successfully!")
