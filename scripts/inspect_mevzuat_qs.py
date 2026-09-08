import zipfile
import re
import xml.etree.ElementTree as ET

def get_docx_pars(docx_path):
    with zipfile.ZipFile(docx_path) as z:
        tree = ET.fromstring(z.read('word/document.xml'))
        ns = {'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}
        body = tree.find('w:body', ns)
        pars = []
        if body is None:
            return pars
        for p in body.findall('w:p', ns):
            texts = [t.text for t in p.findall('.//w:t', ns) if t.text]
            if texts:
                pars.append(''.join(texts))
        return pars

pars = get_docx_pars('Konu Anlatım/sermaye-piyasasi-mevzuati.docx')

print(f"Total paragraphs: {len(pars)}")
# Find Soru 1
for i in range(60, min(120, len(pars))):
    safe_p = pars[i].encode('ascii', errors='replace').decode('ascii')
    print(f"[{i}]: {safe_p}")
