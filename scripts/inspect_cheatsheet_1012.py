import re

with open("src/pages/CheatSheetPage.tsx", "r", encoding="utf-8") as f:
    text = f.read()

durations_1012 = re.findall(r'id:\s*[\'"](dur_\d+)[\'"],\s*module:\s*[\'"]1012[\'"]', text)
ratios_1012 = re.findall(r'id:\s*[\'"](rat_\d+)[\'"],\s*module:\s*[\'"]1012[\'"]', text)
comparisons_1012 = re.findall(r'id:\s*[\'"](comp_\d+)[\'"],\s*module:\s*[\'"]1012[\'"]', text)
traps_1012 = re.findall(r'id:\s*[\'"](trap_\d+)[\'"],\s*module:\s*[\'"]1012[\'"]', text)

print(f"1012 Durations: {len(durations_1012)} -> {durations_1012}")
print(f"1012 Ratios: {len(ratios_1012)} -> {ratios_1012}")
print(f"1012 Comparisons: {len(comparisons_1012)} -> {comparisons_1012}")
print(f"1012 Traps: {len(traps_1012)} -> {traps_1012}")
print(f"Total 1012 items: {len(durations_1012) + len(ratios_1012) + len(comparisons_1012) + len(traps_1012)}")
