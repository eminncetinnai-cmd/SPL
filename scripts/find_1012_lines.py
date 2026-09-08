with open("src/pages/CheatSheetPage.tsx", "r", encoding="utf-8") as f:
    lines = f.readlines()

for idx, line in enumerate(lines):
    if "moduleId: '1012'" in line or 'moduleId: "1012"' in line:
        print(f"Line {idx+1}: {line.strip()}")
