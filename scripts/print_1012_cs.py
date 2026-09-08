import re

with open("src/pages/CheatSheetPage.tsx", "r", encoding="utf-8") as f:
    text = f.read()

items = re.findall(r'(\{[^{}]*moduleId:\s*[\'"]1012[\'"][^{}]*\})', text)
for i, item in enumerate(items):
    print(f"Item {i+1}:")
    print(item)
    print("-" * 40)
