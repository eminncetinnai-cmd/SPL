import zipfile
import xml.etree.ElementTree as ET

def inspect_file(docx_path):
    with zipfile.ZipFile(docx_path) as z:
        tree = ET.fromstring(z.read('word/document.xml'))
        ns = {'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}
        body = tree.find('w:body', ns)
        pars = []
        if body is None:
            return
        for p in body.findall('w:p', ns):
            texts = [t.text for t in p.findall('.//w:t', ns) if t.text]
            if texts:
                pars.append(''.join(texts))
                
    print(f"\n=================== {docx_path} ===================")
    for idx, p in enumerate(pars):
        if any(w in p.lower() for w in ['soru 1:', 'soru 15:', 'doğru cevap', 'çözüm']):
            safe = p.encode('ascii', errors='replace').decode('ascii')
            print(f"[{idx}]: {safe[:90]}")

for f in [
    'Konu Anlatım/sermaye-piyasasi-mevzuati.docx',
    'Konu Anlatım/sermaye-piyasasi-araclari.docx',
    'Konu Anlatım/yatirim-kuruluslari.docx',
    'Konu Anlatım/takas-saklama-operasyon.docx'
]:
    inspect_file(f)
