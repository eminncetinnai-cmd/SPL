import json

with open("src/data/questions_master.json", "r", encoding="utf-8") as f:
    master_qs = json.load(f)

for q in master_qs:
    if q["id"] == "q_1012_master_082":
        q["options"] = [
            {"key": "A", "text": "Borsa İstanbul Olağanüstü Durum Yedek Fonu"},
            {"key": "B", "text": "TCMB Bankalararası Para Piyasası Garanti Blokesi"},
            {"key": "C", "text": "Yatırımcı Tazmin Merkezi Genel Tazmin Fonu Hesabı"},
            {"key": "D", "text": "Takasbank Karşılanmış Risklere Tahsis Edilen Sermayesi"},
            {"key": "E", "text": "Sermaye Piyasası Kurulu İdari Para Cezaları Havuzu"}
        ]

with open("src/data/questions_master.json", "w", encoding="utf-8") as f:
    json.dump(master_qs, f, ensure_ascii=False, indent=2)

print("Fixed q_1012_master_082")
