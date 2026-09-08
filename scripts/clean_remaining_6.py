import json, re

with open("src/data/questions_master.json", "r", encoding="utf-8") as f:
    master_qs = json.load(f)

for q in master_qs:
    if q["id"] == "q_1012_master_049":
        for o in q["options"]:
            if o["key"] == q["correct_answer"]:
                o["text"] = "Aksine bir sözleşme veya mahkeme kararı olmadıkça payın asıl pay sahibi oy hakkını kullanır"
    elif q["id"] == "q_1012_master_069":
        for o in q["options"]:
            if o["key"] == q["correct_answer"]:
                o["text"] = "TÜBİTAK onaylı resmi Zaman Damgası ve Nitelikli Elektronik Sertifika ile"
    elif q["id"] == "q_1012_master_075":
        for o in q["options"]:
            if o["key"] == q["correct_answer"]:
                o["text"] = "Takasbank Temerrüt Pazarında Zorunlu Alım yaparak veya Ödünç Piyasasından temin ederek hisseyi teslim eder"
    elif q["id"] == "q_1012_master_077":
        for o in q["options"]:
            if o["key"] == q["correct_answer"]:
                o["text"] = "İşlem gününü izleyen T+1 günü en geç saat 15:00'e kadar"
    elif q["id"] == "q_1012_master_082":
        for o in q["options"]:
            if o["key"] == q["correct_answer"]:
                o["text"] = "Takasbank Karşılanmış Risklere Tahsis Edilen Özkaynak Katkısı"
    elif q["id"] == "q_1012_ogretici_020":
        for o in q["options"]:
            if o["key"] == q["correct_answer"]:
                o["text"] = "Yatırımcı Tazmin Merkezi'ne devredilir"

with open("src/data/questions_master.json", "w", encoding="utf-8") as f:
    json.dump(master_qs, f, ensure_ascii=False, indent=2)

print("Cleaned remaining 6.")
