import json
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('src/data/topic_notes.json', 'r', encoding='utf-8') as f:
    notes = json.load(f)

print("Auditing all 29 sections in topic_notes.json for regulatory consistency:\n")

# Known critical exam thresholds
THRESHOLDS = {
    '1001': [
        ('12 ay', 'İzahname geçerlilik süresi'),
        ('15 gün', 'Rüçhan hakkı asgari süresi'),
        ('60 gün', 'Rüçhan hakkı azami süresi'),
        ('1/3', 'Bağımsız yönetim kurulu üyesi asgari oranı'),
        ('2 üye', 'Bağımsız yönetim kurulu asgari kişi sayısı'),
        ('%98', 'Ortaklıktan çıkarma ve satma hakkı oy oranı'),
        ('3 yıl', 'Manipülasyon hapis cezası alt sınırı'),
        ('5 yıl', 'Manipülasyon hapis cezası üst sınırı'),
        ('2 kat', 'Etkin pişmanlıkta Hazineye ödenecek menfaat katı'),
        ('5 yıl', 'Kayıtlı sermaye tavan yetki azami süresi')
    ],
    '1003': [
        ('15 oy', '1 paya tanınabilecek azami oy imtiyazı'),
        ('1 yıl', 'Tahvil asgari vadesi (365 gün)'),
        ('%95', 'BYF baz endeks takip korelasyon oranı'),
        ('%51', 'GYO asgari gayrimenkul varlık oranı'),
        ('%80', 'Hisse senedi yoğun fon asgari hisse oranı')
    ],
    '1005': [
        ('25 Milyon', 'Dar yetkili aracı kurum asgari sermayesi'),
        ('75 Milyon', 'Kısmi yetkili aracı kurum asgari sermayesi'),
        ('150 Milyon', 'Geniş yetkili aracı kurum asgari sermayesi'),
        ('%35', 'Kredili işlem asgari başlangıç özkaynak oranı'),
        ('%20', 'Kredili işlem asgari sürdürme özkaynak oranı'),
        ('1:10', 'Kaldıraçlı alım satım (Forex) azami kaldıraç sınırı'),
        ('50.000 TL', 'Forex asgari başlangıç teminatı'),
        ('30 gün', 'Personel hisse elde tutma asgari süresi')
    ],
    '1012': [
        ('T+2', 'Pay Piyasası standart takas valörü'),
        ('T+0', 'Borçlanma Araçları Piyasası valörü'),
        ('T+1', 'VİOP günlük nakit uzlaşma valörü'),
        ('10 yıl', 'Zamanaşımı süresi'),
        ('Garanti Fonu', 'MKT risk havuzu'),
        ('SITG', 'Takasbank özkaynak katkısı'),
        ('15:00', 'Pay piyasası takas son saati')
    ]
}

total_sections = 0
for mod_id, data in notes.items():
    print(f"=== MODÜL {mod_id}: {data['module_name']} ({len(data['sections'])} Bölüm) ===")
    mod_text = ""
    for sec in data['sections']:
        total_sections += 1
        sec_title = sec['title']
        all_text = " ".join(sec['content']) + " " + " ".join(sec.get('concrete_examples', [])) + " " + " ".join(sec['key_takeaways']) + " " + " ".join(sec['exam_traps'])
        mod_text += " " + all_text
        print(f"  [{sec['id']}] {sec_title}")
        print(f"     İçerik: {len(sec['content'])} paragraf, Örnek: {len(sec.get('concrete_examples', []))}, Tablo: {len(sec.get('tables', []))}")
    
    # Check if this module contains its critical thresholds
    print(f"\n  Eşik Uyumluluk Kontrolü (Modül {mod_id}):")
    for val, desc in THRESHOLDS.get(mod_id, []):
        if val.lower() in mod_text.lower():
            print(f"    ✓ {val:<12} -> Mevzuata tam uygun ({desc})")
        else:
            print(f"    ❌ EKSİK: {val} ({desc})")
    print("-" * 75)

print(f"\nToplam İncelenen Master Bölüm: {total_sections}")
