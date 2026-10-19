import json
import shutil
import os

print("--- MERGING 200 HARD QUESTIONS INTO MASTER QUESTION DATASETS ---")

# Backup original files just in case
shutil.copyfile("src/data/all_questions.json", "src/data/all_questions.json.bak")
shutil.copyfile("src/data/questions_master.json", "src/data/questions_master.json.bak")

with open("src/data/all_questions.json", "r", encoding="utf-8") as f:
    orig_all = json.load(f)

with open("src/data/questions_master.json", "r", encoding="utf-8") as f:
    orig_master = json.load(f)

assert len(orig_all) == 935, f"Expected 935 questions, got {len(orig_all)}"
assert orig_all == orig_master, "all_questions and questions_master are not identical"

batches = [
    ("1001", "scripts/data_1001_hard.json", 50),
    ("1003", "scripts/data_1003_hard.json", 50),
    ("1005", "scripts/data_1005_hard.json", 50),
    ("1012", "scripts/data_1012_hard.json", 50)
]

new_questions = []
for mod, path, exp_count in batches:
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
    assert len(data) == exp_count, f"Batch {mod} expected {exp_count}, got {len(data)}"
    for q in data:
        assert q["module_id"] == mod
        new_questions.append(q)

print(f"Total new questions to append: {len(new_questions)}")

# Check ID uniqueness
existing_ids = set(q["id"] for q in orig_all)
for q in new_questions:
    assert q["id"] not in existing_ids, f"ID conflict: {q['id']}"

combined = list(orig_all) + new_questions
assert len(combined) == 1135, f"Expected 1135, got {len(combined)}"

# Check counts per module
mod_counts = {m: sum(1 for q in combined if q["module_id"] == m) for m in ["1001", "1003", "1005", "1012"]}
expected_counts = {"1001": 283, "1003": 290, "1005": 288, "1012": 274}
print("Final module counts:", mod_counts)
assert mod_counts == expected_counts, f"Counts mismatch: {mod_counts} vs {expected_counts}"

# Save to both files
with open("src/data/all_questions.json", "w", encoding="utf-8") as f:
    json.dump(combined, f, ensure_ascii=False, indent=2)

with open("src/data/questions_master.json", "w", encoding="utf-8") as f:
    json.dump(combined, f, ensure_ascii=False, indent=2)

# Remove backups if successful
if os.path.exists("src/data/all_questions.json.bak"):
    os.remove("src/data/all_questions.json.bak")
if os.path.exists("src/data/questions_master.json.bak"):
    os.remove("src/data/questions_master.json.bak")

print("SUCCESS: 200 hard questions successfully appended to all_questions.json and questions_master.json!")
