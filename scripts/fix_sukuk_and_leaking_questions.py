import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('src/data/all_questions.json', 'r', encoding='utf-8') as f:
    questions = json.load(f)

SUKUK_STANDARD_OPTIONS = [
    {"key": "A", "text": "İcara (Sahipliğe Dayalı Kira Sertifikası)"},
    {"key": "B", "text": "Murabaha (Alım-Satıma Dayalı Kira Sertifikası)"},
    {"key": "C", "text": "İstisna (Eser Sözleşmesine Dayalı Kira Sertifikası)"},
    {"key": "D", "text": "Mudaraba (Emek-Sermaye Ortaklığına Dayalı Kira Sertifikası)"},
    {"key": "E", "text": "Vekalet (Yönetim Sözleşmesine Dayalı Kira Sertifikası)"}
]

updated_count = 0

for q in questions:
    qid = q['id']
    
    # 1. Fix q_1003_master_061 (the exact question the user encountered)
    if qid == 'q_1003_master_061':
        q['text'] = "Varlık Kiralama Şirketinin (VKŞ) işveren, kaynak kuruluşun veya üçüncü bir tarafın yüklenici olduğu; henüz mevcut olmayan bir tesis, bina veya projenin meydana getirilmesi amacıyla ihraç edilen kira sertifikası (sukuk) türü aşağıdakilerden hangisidir?"
        q['options'] = [
            {"key": "A", "text": "İcara (Sahipliğe Dayalı Kira Sertifikası)"},
            {"key": "B", "text": "Murabaha (Alım-Satıma Dayalı Kira Sertifikası)"},
            {"key": "C", "text": "İstisna (Eser Sözleşmesine Dayalı Kira Sertifikası)"},
            {"key": "D", "text": "Mudaraba (Emek-Sermaye Ortaklığına Dayalı Kira Sertifikası)"},
            {"key": "E", "text": "Vekalet (Yönetim Sözleşmesine Dayalı Kira Sertifikası)"}
        ]
        q['correct_answer'] = "C"
        q['explanation'] = "SPK Kira Sertifikaları Tebliği (III-61.1) Madde 9 uyarınca; VKŞ'nin işveren, kaynak kuruluşun veya üçüncü kişilerin yüklenici olduğu ve henüz mevcut olmayan bir eserin (inşaat, fabrika, altyapı vb.) meydana getirilmesi/üretilmesi amacıyla ihraç edilen kira sertifikası 'Eser Sözleşmesine Dayalı Kira Sertifikası'dır (İslam finans literatüründeki adı İstisna Sukuku'dur).\n\n📌 Soruda Geçen Kısaltmalar & Terimler:\n• VKŞ: Varlık Kiralama Şirketi (Münhasıran kira sertifikası ihraç etmek üzere anonim şirket şeklinde kurulan sermaye piyasası kurumu)\n• İstisna (Eser Sözleşmesi): Henüz ortada olmayan bir eserin sipariş ve bedel karşılığı inşa ettirilmesini konu alan sözleşme"
        updated_count += 1
        print("Updated q_1003_master_061 with exam-grade phrasing and balanced options.")

    # 2. Harmonize q_1003_master_052 (Sahipliğe Dayalı / İcara)
    elif qid == 'q_1003_master_052':
        q['text'] = "Kaynak kuruluşa ait bir gayrimenkul veya hakkın VKŞ tarafından satın alınarak kaynak kuruluşa geri kiralanması ve kira gelirlerinin yatırımcılara dağıtılması esasına dayanan kira sertifikası (sukuk) türü hangisidir?"
        q['options'] = [
            {"key": "A", "text": "İcara (Sahipliğe Dayalı Kira Sertifikası)"},
            {"key": "B", "text": "Murabaha (Alım-Satıma Dayalı Kira Sertifikası)"},
            {"key": "C", "text": "İstisna (Eser Sözleşmesine Dayalı Kira Sertifikası)"},
            {"key": "D", "text": "Mudaraba (Emek-Sermaye Ortaklığına Dayalı Kira Sertifikası)"},
            {"key": "E", "text": "Vekalet (Yönetim Sözleşmesine Dayalı Kira Sertifikası)"}
        ]
        q['correct_answer'] = "A"
        q['explanation'] = "SPK Tebliği m.5 uyarınca varlık veya hakkın VKŞ tarafından satın alınarak kiralanması ve kira bedelinin sertifika sahiplerine dağıtılması 'Sahipliğe Dayalı Kira Sertifikası'dır (İcara Sukuku).\n\n📌 Soruda Geçen Kısaltmalar & Terimler:\n• İcara: Varlık veya hakkın mülkiyetinin devredilerek kiraya verilmesi esasına dayanan faizsiz kiralama modeli"
        updated_count += 1
        print("Harmonized q_1003_master_052")

    # 3. Harmonize q_1003_master_053 (Yönetim Sözleşmesine Dayalı / Vekalet)
    elif qid == 'q_1003_master_053':
        q['text'] = "Kaynak kuruluşa ait varlık veya hakların mülkiyet devri yapılmaksızın VKŞ lehine yönetilmesi ve elde edilen gelirlerin sertifika sahiplerine aktarılması esasına dayanan kira sertifikası türü hangisidir?"
        q['options'] = [
            {"key": "A", "text": "İcara (Sahipliğe Dayalı Kira Sertifikası)"},
            {"key": "B", "text": "Murabaha (Alım-Satıma Dayalı Kira Sertifikası)"},
            {"key": "C", "text": "İstisna (Eser Sözleşmesine Dayalı Kira Sertifikası)"},
            {"key": "D", "text": "Mudaraba (Emek-Sermaye Ortaklığına Dayalı Kira Sertifikası)"},
            {"key": "E", "text": "Vekalet (Yönetim Sözleşmesine Dayalı Kira Sertifikası)"}
        ]
        q['correct_answer'] = "E"
        q['explanation'] = "SPK Tebliği m.6 uyarınca varlık veya hakların mülkiyeti devredilmeksizin VKŞ adına yönetilmesi ve gelirlerinin aktarılması 'Yönetim Sözleşmesine Dayalı Kira Sertifikası'dır (Vekalet Sukuku).\n\n📌 Soruda Geçen Kısaltmalar & Terimler:\n• Vekalet (Yönetim Sözleşmesi): Varlıkların mülkiyet devri olmadan gelir getirmek üzere yönetilmesi sözleşmesi"
        updated_count += 1
        print("Harmonized q_1003_master_053")

    # 4. Harmonize q_1003_master_054 (Alım-Satıma Dayalı / Murabaha)
    elif qid == 'q_1003_master_054':
        q['text'] = "VKŞ'nin bir emtiayı peşin satın alıp vadeli olarak kâr marjıyla kaynak kuruluşa veya üçüncü şahıslara satması esasına dayanan kira sertifikası türü hangisidir?"
        q['options'] = [
            {"key": "A", "text": "İcara (Sahipliğe Dayalı Kira Sertifikası)"},
            {"key": "B", "text": "Vekalet (Yönetim Sözleşmesine Dayalı Kira Sertifikası)"},
            {"key": "C", "text": "Murabaha (Alım-Satıma Dayalı Kira Sertifikası)"},
            {"key": "D", "text": "İstisna (Eser Sözleşmesine Dayalı Kira Sertifikası)"},
            {"key": "E", "text": "Mudaraba (Emek-Sermaye Ortaklığına Dayalı Kira Sertifikası)"}
        ]
        q['correct_answer'] = "C"
        q['explanation'] = "SPK Tebliği m.7 uyarınca bir varlığın peşin alınıp vadeli kâr marjıyla satılması 'Alım-Satıma Dayalı Kira Sertifikası'dır (Murabaha Sukuku).\n\n📌 Soruda Geçen Kısaltmalar & Terimler:\n• Murabaha: Alım maliyeti ve kâr payı baştan açıkça belirlenerek vadeli satış yapılması işlemi"
        updated_count += 1
        print("Harmonized q_1003_master_054")

    # 5. Harmonize q_1003_master_055 (Ortaklığa Dayalı / Mudaraba & Müşareke)
    elif qid == 'q_1003_master_055':
        q['text'] = "Bir tarafın sermaye diğer tarafın emek koyduğu (emek-sermaye) veya tarafların birlikte sermaye koyduğu ortaklık girişiminin kâr/zararına dayalı kira sertifikası türü hangisidir?"
        q['options'] = [
            {"key": "A", "text": "İcara (Sahipliğe Dayalı Kira Sertifikası)"},
            {"key": "B", "text": "Mudaraba / Müşareke (Ortaklığa Dayalı Kira Sertifikası)"},
            {"key": "C", "text": "Murabaha (Alım-Satıma Dayalı Kira Sertifikası)"},
            {"key": "D", "text": "Vekalet (Yönetim Sözleşmesine Dayalı Kira Sertifikası)"},
            {"key": "E", "text": "İstisna (Eser Sözleşmesine Dayalı Kira Sertifikası)"}
        ]
        q['correct_answer'] = "B"
        q['explanation'] = "SPK Tebliği m.8 uyarınca ortaklık girişimine fon sağlamak amacıyla ihraç edilen ve kâr-zarar paylaşımı esasına dayanan sertifikalar 'Ortaklığa Dayalı Kira Sertifikası'dır (Mudaraba veya Müşareke).\n\n📌 Soruda Geçen Kısaltmalar & Terimler:\n• Mudaraba: Bir tarafın sermaye, diğer tarafın emek koyduğu kâr ortaklığı\n• Müşareke: İki veya daha fazla tarafın birlikte sermaye koyduğu kâr-zarar ortaklığı"
        updated_count += 1
        print("Harmonized q_1003_master_055")

# Save to all_questions.json and questions_master.json
with open('src/data/all_questions.json', 'w', encoding='utf-8') as f:
    json.dump(questions, f, ensure_ascii=False, indent=2)

with open('src/data/questions_master.json', 'w', encoding='utf-8') as f:
    json.dump(questions, f, ensure_ascii=False, indent=2)

print(f"\nSuccessfully synchronized and saved {updated_count} questions!")
