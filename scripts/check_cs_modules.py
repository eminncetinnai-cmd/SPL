import re

with open("src/pages/CheatSheetPage.tsx", "r", encoding="utf-8") as f:
    text = f.read()

print("All modules in CheatSheetPage:")
print(set(re.findall(r'module:\s*[\'"](\d+)[\'"]', text)))
