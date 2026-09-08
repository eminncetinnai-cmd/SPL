import zipfile
import xml.etree.ElementTree as ET

with zipfile.ZipFile('Konu Anlatım/SPL_Duzey_1_X5_Detayli_Calisma_Kitabi.docx') as z:
    tree = ET.fromstring(z.read('word/document.xml'))
    ns = {'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}
    body = tree.find('w:body', ns)
    pars = []
    for p in body.findall('w:p', ns):
        texts = [t.text for t in p.findall('.//w:t', ns) if t.text]
        if texts:
            pars.append(''.join(texts))

print(f"X5 docx total paragraphs: {len(pars)}")
# Print paragraphs from index 250 to 320
for idx in range(250, min(330, len(pars))):
    safe_p = pars[idx].encode('ascii', errors='replace').decode('ascii')
    print(f"[{idx}]: {safe_p}")
