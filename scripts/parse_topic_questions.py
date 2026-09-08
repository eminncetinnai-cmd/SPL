import zipfile
import xml.etree.ElementTree as ET
import re

def extract_all_runs_text(element, ns):
    texts = []
    for node in element.iter():
        if node.tag == f"{{{ns['w']}}}t":
            if node.text:
                texts.append(node.text)
    return ''.join(texts)

def parse_topic_file_questions(docx_path, module_id):
    with zipfile.ZipFile(docx_path) as z:
        tree = ET.fromstring(z.read('word/document.xml'))
        ns = {'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}
        body = tree.find('w:body', ns)
        
        paragraphs = []
        for p in body.findall('.//w:p', ns):
            t = extract_all_runs_text(p, ns).strip()
            if t:
                paragraphs.append(t)
                
    questions = []
    current_q = None
    
    i = 0
    while i < len(paragraphs):
        p = paragraphs[i]
        
        # Check for Soru X:
        m_q = re.match(r'^Soru\s*(\d+)\s*:\s*(.*)$', p, re.IGNORECASE)
        if m_q:
            if current_q and current_q['options'] and current_q['correct_answer']:
                questions.append(current_q)
                
            q_num = int(m_q.group(1))
            current_q = {
                'id': f"q_{module_id}_konu_{q_num:03d}",
                'module_id': module_id,
                'number': q_num,
                'source': 'master',
                'topic': 'Konu Anlatımı Çözümlü Deneme Soruları',
                'chapter': f"Modül {module_id} Resmi Konu Anlatımı",
                'text': m_q.group(2).strip(),
                'options': [],
                'correct_answer': '',
                'explanation': '',
                'difficulty': 'hard',
                'tags': [module_id, 'konu-anlatimi', 'orijinal']
            }
            i += 1
            continue
            
        if current_q:
            # Check for correct answer
            m_ans = re.search(r'(?:DOĞRU\s*CEVAP|Doğru\s*Cevap)\s*(?:VE\s*AYRINTILI\s*YASAL\s*ANALİZ)?\s*:\s*(?:Doğru\s*Cevap\s*:\s*)?([A-E])(?:\)|\.|\s*)(.*)', p, re.IGNORECASE)
            if m_ans:
                current_q['correct_answer'] = m_ans.group(1).upper()
                exp = m_ans.group(2).strip()
                if exp:
                    current_q['explanation'] = exp
                i += 1
                continue
                
            # Check for option
            m_opt = re.match(r'^([A-E])[\)\.]\s*(.+)$', p)
            if m_opt and len(current_q['options']) < 5:
                current_q['options'].append({
                    'key': m_opt.group(1).upper(),
                    'text': m_opt.group(2).strip()
                })
                i += 1
                continue
                
            # If in question text
            if not current_q['options']:
                current_q['text'] += ' ' + p
                i += 1
                continue
                
            # If in explanation
            if current_q['correct_answer']:
                if not re.match(r'^Soru\s*\d+', p, re.IGNORECASE) and not re.match(r'^\d+\.', p):
                    if current_q['explanation']:
                        current_q['explanation'] += ' ' + p
                    else:
                        current_q['explanation'] = p
                i += 1
                continue
                
        i += 1
        
    if current_q and current_q['options'] and current_q['correct_answer']:
        questions.append(current_q)
        
    return questions

for mod, path in [
    ('1001', 'Konu Anlatım/sermaye-piyasasi-mevzuati.docx'),
    ('1003', 'Konu Anlatım/sermaye-piyasasi-araclari.docx'),
    ('1005', 'Konu Anlatım/yatirim-kuruluslari.docx'),
    ('1012', 'Konu Anlatım/takas-saklama-operasyon.docx')
]:
    qs = parse_topic_file_questions(path, mod)
    print(f"Modül {mod}: Parsed {len(qs)} questions from {path}")
    for q in qs[:3]:
        print(f"  - [{q['id']}] Ans: {q['correct_answer']}, Opts: {len(q['options'])}, Exp len: {len(q['explanation'])}")
        print(f"    Text: {q['text'][:70]}...")
