import glob
import re
import sys
import zipfile
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

files = sorted(glob.glob('Konu Anlatım/*.docx'))

for f in files:
    pars = get_docx_pars(f)
    print("=" * 60)
    print(f"DOSYA: {f} | Toplam Paragraf: {len(pars)}")
    
    # Check for question patterns
    q_indices = []
    for idx, p in enumerate(pars):
        clean_p = p.strip()
        if re.match(r'^(Soru\s*\d+|SORU\s*\d+|Örnek\s*Soru|\d+[\.\)]\s*Soru|BÖLÜM\s*6|80\s*SORULUK)', clean_p, re.IGNORECASE):
            q_indices.append((idx, clean_p))
            
    print(f"Bulunan Soru / Bölüm Başlığı Sayısı: {len(q_indices)}")
    for idx, q_title in q_indices[:8]:
        safe_title = q_title.encode('ascii', errors='replace').decode('ascii')
        print(f"  [Index {idx}]: {safe_title[:75]}")

    # Check for options
    opt_count = sum(1 for p in pars if re.match(r'^[A-E][\)\.]\s+', p.strip()))
    print(f"Seçenek (A-E şıkkı) içeren paragraf sayısı: {opt_count}")
