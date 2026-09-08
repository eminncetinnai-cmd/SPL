import re

with open("src/pages/CheatSheetPage.tsx", "r", encoding="utf-8") as f:
    text = f.read()

for prefix in ['dur', 'rat', 'comp', 'trap']:
    nums = [int(n) for n in re.findall(rf'{prefix}_(\d+)', text)]
    if nums:
        print(f"Max {prefix}: {prefix}_{max(nums)}, total={len(nums)}")
