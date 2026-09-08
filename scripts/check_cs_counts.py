import re

with open("src/pages/CheatSheetPage.tsx", "r", encoding="utf-8") as f:
    text = f.read()

for mod in ['1001', '1003', '1005', '1012']:
    count = len(re.findall(rf"moduleId:\s*['\"]{mod}['\"]", text))
    print(f"Module {mod}: {count} items")
