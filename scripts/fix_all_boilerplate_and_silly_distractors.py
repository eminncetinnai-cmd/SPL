import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('src/data/all_questions.json', 'r', encoding='utf-8') as f:
    questions = json.load(f)

print(f"Loaded {len(questions)} questions.")

FIXES = {
    # 1. q_1003_master_092 (The exact ADR question user posted)
    "q_1003_master_092": {
        "options": [
            {"key": "A", "text": "GDR (Global Depository Receipt)"},
            {"key": "B", "text": "EDR (European Depository Receipt)"},
            {"key": "C", "text": "IDR (International Depository Receipt)"},
            {"key": "D", "text": "TRD (Türk Depo Sertifikası)"},
            {"key": "E", "text": "ADR (American Depository Receipt)"}
        ],
        "explanation": "ABD sermaye piyasalarında ve New York Borsası (NYSE), NASDAQ gibi Amerikan borsalarında işlem görmek üzere ihraç edilen yabancı şirket hisselerini temsil eden depo sertifikalarına 'ADR' (American Depository Receipt) adı verilir. Diğer uluslararası borsalarda işlem görenler ise GDR (Global Depository Receipt) olarak adlandırılır.\n\n📌 Soruda Geçen Kısaltmalar & Terimler:\n• ADR: American Depository Receipt (Amerikan Depo Sertifikası)\n• GDR: Global Depository Receipt (Küresel Depo Sertifikası)"
    },

    # 2. q_1003_master_088 (Forward Pricing in Mutual Funds)
    "q_1003_master_088": {
        "options": [
            {"key": "A", "text": "Spot Fiyatlama Yöntemi"},
            {"key": "B", "text": "Tarihsel Maliyet Yöntemi"},
            {"key": "C", "text": "Marjin Fiyatlama Yöntemi"},
            {"key": "D", "text": "İskontolu Nakit Akışı Yöntemi"},
            {"key": "E", "text": "İleri Fiyatlama Yöntemi (Forward Pricing)"}
        ],
        "explanation": "Yatırım fonlarında katılma payı alım satım emirlerinin verildiği anki fiyattan değil; emrin verildiği günün kapanışında portföy değerine göre hesaplanan Net Aktif Değer (NAD) üzerinden gerçekleşmesine 'İleri Fiyatlama Yöntemi' (Forward Pricing) denir."
    },

    # 3. q_1003_master_096 (Gayrimenkul sertifikası hakediş)
    "q_1003_master_096": {
        "options": [
            {"key": "A", "text": "Satış bittiği anda tüm para tek seferde şirkete ödenir."},
            {"key": "B", "text": "Para şirket ortaklarının şahsi hesaplarına paylaştırılır."},
            {"key": "C", "text": "İnşaatın ilerleme oranına (hakediş raporlarına) paralel olarak yetkili bankadaki özel hesaptan dilimler halinde aktarılır."},
            {"key": "D", "text": "İnşaat tamamen bitip iskan alınana kadar hiçbir ödeme yapılmaz."},
            {"key": "E", "text": "Çevre ve Şehircilik Bakanlığı'nın talebi üzerine belediyeye aktarılır."}
        ]
    },

    # 4. q_1003_master_100 (MKK merkezi saklama kuruluşu)
    "q_1003_master_100": {
        "options": [
            {"key": "A", "text": "Borsa İstanbul A.Ş. (BIST)"},
            {"key": "B", "text": "İstanbul Takas ve Saklama Bankası A.Ş. (Takasbank)"},
            {"key": "C", "text": "Sermaye Piyasası Kurulu (SPK)"},
            {"key": "D", "text": "Merkezi Kayıt Kuruluşu A.Ş. (MKK)"},
            {"key": "E", "text": "Yatırımcı Tazmin Merkezi (YTM)"}
        ],
        "explanation": "Türkiye'de ihraç edilen tüm kaydi sermaye piyasası araçlarının hak sahipleri bazında elektronik ortamda izlendiği tek yasal merkezi saklama kuruluşu Merkezi Kayıt Kuruluşu A.Ş.'dir (MKK)."
    },

    # 5. q_1005_konu_010 (Kitle fonlaması yatırım limiti)
    "q_1005_konu_010": {
        "options": [
            {"key": "A", "text": "100.000 TL"},
            {"key": "B", "text": "500.000 TL"},
            {"key": "C", "text": "1.000.000 TL"},
            {"key": "D", "text": "2.500.000 TL"},
            {"key": "E", "text": "5.000.000 TL"}
        ]
    },

    # 6. q_1005_konu_011 (Kitle fonlaması cayma hakkı)
    "q_1005_konu_011": {
        "options": [
            {"key": "A", "text": "48 saat"},
            {"key": "B", "text": "24 saat"},
            {"key": "C", "text": "72 saat"},
            {"key": "D", "text": "7 iş günü"},
            {"key": "E", "text": "15 takvim günü"}
        ]
    },

    # 7. q_1005_master_044 (Sosyal medya tüyosu cezası)
    "q_1005_master_044": {
        "options": [
            {"key": "A", "text": "Herhangi bir yaptırım uygulanmaz."},
            {"key": "B", "text": "Yalnızca sosyal medya hesabı kapatılır."},
            {"key": "C", "text": "SPKn m.107 ve m.109 uyarınca piyasa dolandırıcılığı veya yetkisiz sermaye piyasası faaliyeti kapsamında 2 yıldan 5 yıla kadar hapis cezası ve adli para cezasıyla yargılanır."},
            {"key": "D", "text": "Yalnızca meslek odası tarafından yazılı ihtar verilir."},
            {"key": "E", "text": "Sadece 1.000 TL idari para cezası verilir."}
        ]
    },

    # 8. q_1005_master_096 (Şüpheli işlem bildirimi)
    "q_1005_master_096": {
        "options": [
            {"key": "A", "text": "Kurumun Uyum Görevlisine ve MASAK'a (Mali Suçları Araştırma Kurulu)"},
            {"key": "B", "text": "Yalnızca şirket güvenlik amirine"},
            {"key": "C", "text": "Yalnızca ilgili müşterinin kendisine"},
            {"key": "D", "text": "Borsa İstanbul Disiplin Kuruluna"},
            {"key": "E", "text": "Türkiye Bankalar Birliğine"}
        ]
    },

    # 9. q_1012_master_062 (Devre kesicide takas)
    "q_1012_master_062": {
        "options": [
            {"key": "A", "text": "Tüm gerçekleşen işlemler iptal edilir."},
            {"key": "B", "text": "Takas süresi 1 yıl ertelenir."},
            {"key": "C", "text": "Paralar aracı kurumun kendi hesabında bloke kalır."},
            {"key": "D", "text": "İşlemlerin takası iptal edilerek portföyler seans açılış durumuna döndürülür."},
            {"key": "E", "text": "Devre kesici devreye girene kadar gerçekleşmiş tüm işlemler geçerlidir ve takası normal valöründe (T+2) yapılır."}
        ]
    },

    # 10. q_1012_master_075 (Buy-In işlemi)
    "q_1012_master_075": {
        "options": [
            {"key": "A", "text": "Alıcıya hisse teslimatı yapılmaz, işlem tamamen silinir."},
            {"key": "B", "text": "Alıcı üyeden işlemi iptal etmesi talep edilir."},
            {"key": "C", "text": "İşlem süresiz ertelenir."},
            {"key": "D", "text": "Takasbank piyasadan bizzat 'Buy-In' (Zorunlu Satın Alma) işlemi yaparak veya Ödünç Pay Piyasasından ödünç alarak hisseyi temin eder ve faturayı temerrüt eden üyeye keser."},
            {"key": "E", "text": "Alıcıya hisse yerine Türk Lirası faiz ödenerek dosya kapatılır."}
        ]
    },

    # 11. q_1012_master_076 (Temerrüt borcunu kapatmayan kurum)
    "q_1012_master_076": {
        "options": [
            {"key": "A", "text": "Kuruma Takasbank tarafından ek temerrüt kredisi açılır."},
            {"key": "B", "text": "Kuruma faizsiz uzun vadeli yapılandırma kredisi açılır."},
            {"key": "C", "text": "Kurumun takas borcu silinir."},
            {"key": "D", "text": "Borç Takasbank'ın genel bütçesine hibe kaydedilir."},
            {"key": "E", "text": "Kurumun borsa işlem yetkisini ve takas üyeliğini derhal askıya alır / geçici olarak işlem yapmasını durdurur."}
        ]
    },

    # 12. q_1012_master_090 (PYŞ ve Saklayıcı ilişkisi)
    "q_1012_master_090": {
        "options": [
            {"key": "A", "text": "Saklayıcı kuruluş PYŞ'nin hiyerarşik bağlı alt birimidir."},
            {"key": "B", "text": "İki kurum tek bir tüzel kişilik altında birleşmiştir."},
            {"key": "C", "text": "Saklama kuruluşu kurucu PYŞ'den tamamen bağımsızdır ve PYŞ'nin tüm fon işlemlerinin mevzuata uygunluğunu gözetmek ve denetlemekle yükümlüdür."},
            {"key": "D", "text": "Saklayıcı kuruluş fonun yatırım stratejisini bizzat yönetir."},
            {"key": "E", "text": "Saklama kuruluşu fon üzerinde hiçbir denetim yetkisine sahip değildir."}
        ]
    },

    # 13. q_1012_master_091 (İflasta MKK hisseleri)
    "q_1012_master_091": {
        "options": [
            {"key": "A", "text": "Hisseler aracı kurumun borçlularına dağıtılır."},
            {"key": "B", "text": "Hisseler aracı kurumun iflas masasına DAHİL EDİLEMEZ; yatırımcı hisselerini MKK üzerinden başka bir aracı kuruma virmanlayarak mülkiyetini aynen korur."},
            {"key": "C", "text": "Hisseler Hazineye gelir kaydedilir."},
            {"key": "D", "text": "Hisseler otomatik nakde çevrilip iflas masasına devredilir."},
            {"key": "E", "text": "Hisselerin mülkiyeti aracı kurumun hâkim ortaklarına geçer."}
        ]
    },

    # 14. q_1012_master_099 (MKK periyodik bildirimleri)
    "q_1012_master_099": {
        "options": [
            {"key": "A", "text": "Sözlü telefon görüşmesiyle"},
            {"key": "B", "text": "Müşterinin ikametgah muhtarlığına elden teslimle"},
            {"key": "C", "text": "Sosyal medyada genel duyuru olarak paylaşarak"},
            {"key": "D", "text": "Yerel gazetelerde ilan yoluyla"},
            {"key": "E", "text": "Güvenli elektronik imza, şifreli e-posta ve e-Devlet kapısı entegrasyonuyla"}
        ]
    },

    # 15. q_1012_ogretici_020 (10 yıl aranmayan varlıklar)
    "q_1012_ogretici_020": {
        "options": [
            {"key": "A", "text": "Aracı kurumun kâr hanesine aktarılır"},
            {"key": "B", "text": "Yatırımcı Tazmin Merkezi'ne (YTM) devredilir"},
            {"key": "C", "text": "Aracı kurumun özkaynaklarına gelir olarak kaydedilir"},
            {"key": "D", "text": "Süresiz olarak MKK havuzunda bekletilir"},
            {"key": "E", "text": "Diğer müşterilere temettü olarak dağıtılır"}
        ]
    },

    # 16. q_1012_master_030 (Kaydileştirilmeyen paylar)
    "q_1012_master_030": {
        "options": [
            {"key": "A", "text": "Paylar sahibinin talebine gerek olmaksızın otomatik borsada satılır."},
            {"key": "B", "text": "Yatırımcıya fiziksel olarak altın teslim edilir."},
            {"key": "C", "text": "Paylar bedelsiz olarak şirket yönetim kurulu üyelerine devredilir."},
            {"key": "D", "text": "Kaydileştirilmeyen paylar kanunen YTM'ye devredilir ve Hazineye intikal eder; pay sahiplerinin hakları sona erer."},
            {"key": "E", "text": "Paylar süresiz olarak fiziki olarak saklanmaya devam eder."}
        ]
    }
}

count = 0
for q in questions:
    if q['id'] in FIXES:
        fix_data = FIXES[q['id']]
        if 'options' in fix_data:
            q['options'] = fix_data['options']
        if 'explanation' in fix_data:
            q['explanation'] = fix_data['explanation']
        count += 1
        print(f"Fixed question {q['id']}")

print(f"\nApplied fixes to {count} questions.")

# Save to all_questions.json and questions_master.json
with open('src/data/all_questions.json', 'w', encoding='utf-8') as f:
    json.dump(questions, f, ensure_ascii=False, indent=2)

with open('src/data/questions_master.json', 'w', encoding='utf-8') as f:
    json.dump(questions, f, ensure_ascii=False, indent=2)

print("Saved updated question banks successfully!")
