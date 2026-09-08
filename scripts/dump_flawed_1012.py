import json

with open("scripts/flagged_1012_detail.json", "r", encoding="utf-8") as f:
    d = json.load(f)

flawed = {}
for q in d["outliers"]:
    flawed[q["id"]] = {"data": q, "outlier": True, "giveaway": False}
for q in d["giveaways"]:
    if q["id"] in flawed:
        flawed[q["id"]]["giveaway"] = True
    else:
        flawed[q["id"]] = {"data": q, "outlier": False, "giveaway": True}

with open("scripts/flawed_1012_readable.txt", "w", encoding="utf-8") as f:
    for qid, info in sorted(flawed.items()):
        q = info["data"]
        f.write(f"ID: {qid} | Outlier: {info['outlier']} | Giveaway: {info['giveaway']}\n")
        f.write(f"Text: {q['text']}\n")
        for o in q["options"]:
            marker = " [CORRECT]" if o["key"] == q["correct_answer"] else ""
            f.write(f"  {o['key']}: {o['text']} (len={len(o['text'])}){marker}\n")
        f.write(f"Explanation: {q['explanation']}\n")
        f.write("-" * 80 + "\n")

print(f"Written {len(flawed)} questions to scripts/flawed_1012_readable.txt")
