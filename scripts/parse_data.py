import zipfile
import xml.etree.ElementTree as ET
import os
import re
import json
import sys

if sys.stdout.encoding != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

def get_docx_xml_paragraphs(docx_path):
    with zipfile.ZipFile(docx_path) as z:
        tree = ET.fromstring(z.read('word/document.xml'))
        paragraphs = []
        for p in tree.iter('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}p'):
            p_text = ''.join(node.text for node in p.iter('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}t') if node.text)
            p_text = p_text.strip()
            if p_text:
                paragraphs.append(p_text)
        return paragraphs

def parse_master_questions(docx_path, module_id):
    pars = get_docx_xml_paragraphs(docx_path)
    questions = []
    current_q = None
    state = "LOOKING_FOR_Q"
    current_chapter = "Genel"
    
    i = 0
    while i < len(pars):
        p = pars[i].strip()
        if re.match(r'^(BÖLÜM\s+\d+|✔\s*Bölüm\s+\d+|📘|✔\s*\d+\.\s*Bölüm)', p, re.IGNORECASE):
            current_chapter = p
            i += 1
            continue
            
        q_match = re.match(r'^SORU\s+(\d+)\s*(?:\[(.*?)\])?', p, re.IGNORECASE)
        if q_match:
            if current_q and current_q.get("options") and current_q.get("correct_answer"):
                questions.append(current_q)
                
            q_num = int(q_match.group(1))
            topic = q_match.group(2) if q_match.group(2) else current_chapter
            current_q = {
                "id": f"q_{module_id}_master_{q_num:03d}",
                "module_id": module_id,
                "number": q_num,
                "source": "master",
                "topic": topic,
                "chapter": current_chapter,
                "text": "",
                "options": [],
                "correct_answer": "",
                "explanation": "",
                "trap": "",
                "difficulty": "medium",
                "tags": [module_id, topic]
            }
            state = "IN_QUESTION"
            i += 1
            continue
            
        if current_q and state in ("IN_QUESTION", "IN_OPTIONS"):
            ans_match = re.search(r'✔\s*Doğru\s*Cevap\s*:\s*([A-E])', p, re.IGNORECASE)
            if ans_match:
                current_q["correct_answer"] = ans_match.group(1).upper()
                
                exp_text = ""
                if "💡" in p or "Analitik Çözüm" in p:
                    exp_parts = re.split(r'💡|Analitik Çözüm & Sınav İpucu:\s*', p)
                    if len(exp_parts) > 1:
                        exp_text = exp_parts[-1].strip()
                else:
                    exp_text = p[ans_match.end():].strip()
                    if exp_text.startswith(":") or exp_text.startswith("-"):
                        exp_text = exp_text[1:].strip()
                
                current_q["explanation"] = exp_text
                state = "IN_EXPLANATION"
                i += 1
                continue
                
            opt_match = re.match(r'^([A-E])\)\s*(.+)$', p)
            if opt_match:
                state = "IN_OPTIONS"
                current_q["options"].append({
                    "key": opt_match.group(1).upper(),
                    "text": opt_match.group(2).strip()
                })
                i += 1
                continue
                
            if state == "IN_QUESTION":
                if current_q["text"]:
                    current_q["text"] += "\n" + p
                else:
                    current_q["text"] = p
                i += 1
                continue
                
            if state == "IN_OPTIONS" and current_q["options"]:
                current_q["options"][-1]["text"] += " " + p
                i += 1
                continue
                
        if current_q and state == "IN_EXPLANATION":
            if not re.match(r'^SORU\s+\d+', p, re.IGNORECASE) and not re.match(r'^(BÖLÜM|📘)', p, re.IGNORECASE):
                if current_q["explanation"]:
                    current_q["explanation"] += "\n" + p
                else:
                    current_q["explanation"] = p
                i += 1
                continue
                
        i += 1

    if current_q and current_q.get("options") and current_q.get("correct_answer"):
        questions.append(current_q)
        
    return questions

def parse_ogretici_questions(docx_path):
    pars = get_docx_xml_paragraphs(docx_path)
    all_questions = []
    current_module = "1001"
    current_q = None
    state = "LOOKING_FOR_Q"
    
    i = 0
    while i < len(pars):
        p = pars[i].strip()
        if "1001 – Dar Kapsamlı" in p or "1001 - Dar Kapsamlı" in p:
            current_module = "1001"
            i += 1
            continue
        elif "1003 – Sermaye Piyasası" in p or "1003 - Sermaye Piyasası" in p:
            current_module = "1003"
            i += 1
            continue
        elif "1005 – Yatırım Kuruluşları" in p or "1005 - Yatırım Kuruluşları" in p:
            current_module = "1005"
            i += 1
            continue
        elif "1012 – Takas, Saklama" in p or "1012 - Takas, Saklama" in p:
            current_module = "1012"
            i += 1
            continue
            
        q_match = re.match(r'^Soru\s+(\d+)$', p, re.IGNORECASE)
        if q_match:
            if current_q and current_q.get("options") and current_q.get("correct_answer"):
                all_questions.append(current_q)
                
            q_num = int(q_match.group(1))
            current_q = {
                "id": f"q_{current_module}_ogretici_{q_num:03d}",
                "module_id": current_module,
                "number": q_num,
                "source": "ogretici",
                "topic": "Öğretici Kavram Soruları",
                "chapter": f"Modül {current_module} Öğretici Banka",
                "text": "",
                "options": [],
                "correct_answer": "",
                "explanation": "",
                "trap": "",
                "difficulty": "medium",
                "tags": [current_module, "öğretici", "tuzak-analizi"]
            }
            state = "IN_QUESTION"
            i += 1
            continue
            
        if current_q and state in ("IN_QUESTION", "IN_OPTIONS"):
            ans_match = re.match(r'^Doğru\s*cevap\s*:\s*([A-E])(?:\.|\:|\s*)(.*)$', p, re.IGNORECASE)
            if ans_match:
                current_q["correct_answer"] = ans_match.group(1).upper()
                current_q["explanation"] = ans_match.group(2).strip()
                state = "IN_EXPLANATION"
                i += 1
                continue
                
            opt_match = re.match(r'^([A-E])\)\s*(.+)$', p)
            if opt_match:
                state = "IN_OPTIONS"
                current_q["options"].append({
                    "key": opt_match.group(1).upper(),
                    "text": opt_match.group(2).strip()
                })
                i += 1
                continue
                
            if state == "IN_QUESTION":
                if current_q["text"]:
                    current_q["text"] += "\n" + p
                else:
                    current_q["text"] = p
                i += 1
                continue
                
            if state == "IN_OPTIONS" and current_q["options"]:
                current_q["options"][-1]["text"] += " " + p
                i += 1
                continue
                
        if current_q and state in ("IN_EXPLANATION", "IN_TRAP"):
            trap_match = re.match(r'^Sınav\s*tuzağı\s*:\s*(.*)$', p, re.IGNORECASE)
            if trap_match:
                current_q["trap"] = trap_match.group(1).strip()
                state = "IN_TRAP"
                i += 1
                continue
                
            if not re.match(r'^Soru\s+\d+$', p, re.IGNORECASE) and not any(k in p for k in ["1001 –", "1003 –", "1005 –", "1012 –"]):
                if state == "IN_TRAP":
                    current_q["trap"] += " " + p
                elif state == "IN_EXPLANATION":
                    current_q["explanation"] += " " + p
                i += 1
                continue
                
        i += 1

    if current_q and current_q.get("options") and current_q.get("correct_answer"):
        all_questions.append(current_q)
        
    return all_questions

def extract_body_elements_with_tables(docx_path):
    with zipfile.ZipFile(docx_path) as z:
        tree = ET.fromstring(z.read('word/document.xml'))
        ns = {'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}
        body = tree.find('w:body', ns)
        elements = []
        if body is None:
            return elements
            
        for child in body:
            tag = child.tag.split('}')[-1]
            if tag == 'p':
                p_text = ''.join(n.text for n in child.iter('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}t') if n.text).strip()
                if p_text:
                    elements.append(('p', p_text))
            elif tag == 'tbl':
                rows = []
                for tr in child.iter('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}tr'):
                    cells = []
                    for tc in tr.iter('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}tc'):
                        cell_text = ' '.join(''.join(n.text for n in p.iter('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}t') if n.text).strip() for p in tc.iter('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}p'))
                        cells.append(cell_text.strip())
                    if any(cells):
                        rows.append(cells)
                if rows:
                    elements.append(('tbl', rows))
        return elements

def parse_topic_notes_advanced(docx_path, module_id, title):
    elements = extract_body_elements_with_tables(docx_path)
    sections = []
    
    current_sec = {
        "id": f"sec_{module_id}_01",
        "title": "Giriş ve Temel Esaslar",
        "content": [],
        "key_takeaways": [],
        "exam_traps": [],
        "tables": []
    }
    
    for elem_type, data in elements:
        if elem_type == 'p':
            p = data.strip()
            is_heading = False
            title_candidate = p
            
            if re.match(r'^\d+\.\s+[A-ZÇĞİÖŞÜ]', p) or re.match(r'^[A-ZÇĞİÖŞÜ]\)\s+[A-ZÇĞİÖŞÜ]', p):
                if len(p) <= 110:
                    is_heading = True
                elif ":" in p[:80]:
                    parts = p.split(":", 1)
                    title_candidate = parts[0].strip()
                    is_heading = True
                else:
                    is_heading = False
            
            if is_heading:
                if current_sec["content"] or current_sec["key_takeaways"] or current_sec["tables"]:
                    sections.append(current_sec)
                sec_idx = len(sections) + 1
                current_sec = {
                    "id": f"sec_{module_id}_{sec_idx:02d}",
                    "title": title_candidate,
                    "content": [],
                    "key_takeaways": [],
                    "exam_traps": [],
                    "tables": []
                }
                if len(p) > 110 and ":" in p[:80]:
                    current_sec["content"].append(p.split(":", 1)[1].strip())
            else:
                if "SINAVDA SIKÇA ÇIKAR" in p or "Sınav İpucu" in p or "Kritik Süre" in p or "ÖNEMLİ" in p:
                    current_sec["exam_traps"].append(p)
                elif p.startswith("•") or p.startswith("-"):
                    current_sec["key_takeaways"].append(p.lstrip("•- ").strip())
                else:
                    current_sec["content"].append(p)
                    
        elif elem_type == 'tbl':
            rows = data
            if len(rows) >= 2:
                headers = rows[0]
                body_rows = rows[1:]
                current_sec["tables"].append({
                    "headers": headers,
                    "rows": body_rows
                })
            elif len(rows) == 1:
                current_sec["tables"].append({
                    "headers": rows[0],
                    "rows": []
                })
                
    if current_sec["content"] or current_sec["key_takeaways"] or current_sec["tables"]:
        sections.append(current_sec)
        
    return {
        "module_id": module_id,
        "title": title,
        "total_sections": len(sections),
        "sections": sections
    }

def parse_flashcards(docx_path, module_id):
    pars = get_docx_xml_paragraphs(docx_path)
    cards = []
    current_chapter = 'Genel'
    current_card = None
    
    for p in pars:
        if re.match(r'^(BÖLÜM\s+\d+|✔\s*Bölüm\s+\d+|📘)', p, re.IGNORECASE):
            current_chapter = p
            continue
            
        card_match = re.match(r'^KART\s+(\d+)\s*:\s*(.*)$', p, re.IGNORECASE)
        if card_match:
            if current_card and current_card.get('definition'):
                cards.append(current_card)
            c_num = int(card_match.group(1))
            c_title = card_match.group(2).strip()
            current_card = {
                'id': f'fc_{module_id}_{c_num:03d}',
                'module_id': module_id,
                'number': c_num,
                'title': c_title,
                'chapter': current_chapter,
                'definition': '',
                'example': '',
                'trap': ''
            }
            continue
            
        if current_card:
            if '📌' in p or 'Temel Tanım & Mantık:' in p:
                parts = re.split(r'📌|Temel Tanım & Mantık:\s*', p)
                current_card['definition'] = parts[-1].strip()
            elif '💡' in p or 'Akılda Kalıcı Somut Örnek:' in p:
                parts = re.split(r'💡|Akılda Kalıcı Somut Örnek:\s*', p)
                current_card['example'] = parts[-1].strip()
            elif '⚠️' in p or 'Sınav Tuzağı & Kritik Ayrım:' in p:
                parts = re.split(r'⚠️|Sınav Tuzağı & Kritik Ayrım:\s*', p)
                current_card['trap'] = parts[-1].strip()
            else:
                if current_card['trap']:
                    current_card['trap'] += ' ' + p
                elif current_card['example']:
                    current_card['example'] += ' ' + p
                elif current_card['definition']:
                    current_card['definition'] += ' ' + p

    if current_card and current_card.get('definition'):
        cards.append(current_card)
        
    return cards

def parse_x5_study_guide(docx_path):
    """
    Parses SPL_Duzey_1_X5_Detayli_Calisma_Kitabi.docx into structured chapters, concept pairs, and 80 drill questions.
    """
    pars = get_docx_xml_paragraphs(docx_path)
    
    # 1. Parse Answer Key from Section 7
    ans_key = {}
    for p in pars:
        m = re.match(r'^(\d+)\.\s+([A-E])\s+\|\s+(\d+)', p)
        if m:
            q_num = int(m.group(1))
            ans = m.group(2)
            mod = m.group(3)
            ans_key[q_num] = {'answer': ans, 'module': mod}

    # 2. Parse 80 Drill Questions
    drill_questions = []
    current_dq = None

    for p in pars:
        qm = re.match(r'^(\d+)\.\s+\[(\d+)\]\s+(.*)$', p)
        if qm:
            if current_dq and current_dq.get('text'):
                drill_questions.append(current_dq)
            q_num = int(qm.group(1))
            mod_id = qm.group(2)
            q_text = qm.group(3).strip()
            ans_val = ans_key.get(q_num, {}).get('answer', 'A')
            current_dq = {
                'number': q_num,
                'module_id': mod_id,
                'text': q_text,
                'options': [],
                'correct_answer': ans_val,
                'explanation': f'Doğru cevap: {ans_val}. Modül {mod_id} temel kavram kontrolü.'
            }
            continue
            
        if current_dq:
            opt_m = re.match(r'^([A-E])\)\s+(.*)$', p)
            if opt_m:
                current_dq['options'].append({
                    'key': opt_m.group(1),
                    'text': opt_m.group(2).strip()
                })
                continue
            elif 'Cevabım:' in p or 'BÖLÜM 7' in p:
                if current_dq and current_dq.get('text'):
                    drill_questions.append(current_dq)
                    current_dq = None
                if 'BÖLÜM 7' in p:
                    break

    if current_dq and current_dq.get('text'):
        drill_questions.append(current_dq)

    # 3. Parse Chapters
    chapters = []
    current_ch = {
        'id': 'x5_ch0',
        'title': 'BÖLÜM 0 – SINAV ÇÖZME MOTORU & STRATEJİLER',
        'subtitle': 'Her Soruda 5 Adım • Yanlış Analiz Sistemi • 4 Modülü Tek Haritada Birleştir',
        'content': [],
        'bullets': [],
        'traps': []
    }

    in_questions_section = False

    for p in pars:
        if 'BÖLÜM 6' in p or '80 SORULUK' in p:
            in_questions_section = True
            break

        if re.match(r'^(BÖLÜM\s+\d+|ANA\s+ŞİFRE|1001\s+–|1003\s+–|1005\s+–|1012\s+–)', p):
            if current_ch['content'] or current_ch['bullets']:
                chapters.append(current_ch)
            ch_idx = len(chapters)
            current_ch = {
                'id': f'x5_ch{ch_idx}',
                'title': p,
                'subtitle': '',
                'content': [],
                'bullets': [],
                'traps': []
            }
        else:
            if 'SINAV MERCEĞİ:' in p or 'TUZAK:' in p:
                current_ch['traps'].append(p)
            elif p.startswith('▸') or p.startswith('•') or p.startswith('-') or p.startswith('Adım') or '□' in p:
                current_ch['bullets'].append(p)
            else:
                current_ch['content'].append(p)

    if current_ch['content'] or current_ch['bullets']:
        chapters.append(current_ch)

    return {
        'title': 'SPL Düzey 1 X5 Detaylı Sınav Çalışma Kitabı',
        'description': '1001 • 1003 • 1005 • 1012 Derin Konu Anlatımı, Kavram Haritaları, Sınav Çözme Motoru ve 80 Aktif Kavram Kontrol Sorusu',
        'total_chapters': len(chapters),
        'chapters': chapters,
        'drill_questions': drill_questions
    }

def main():
    os.makedirs("src/data", exist_ok=True)
    
    modules = [
        {
            "id": "1001",
            "code": "1001",
            "name": "Dar Kapsamlı Sermaye Piyasası Mevzuatı ve Meslek Kuralları",
            "short_name": "Mevzuat & Meslek Kuralları",
            "category": "Mevzuat",
            "description": "6362 sayılı Sermaye Piyasası Kanunu, Kurumsal Yönetim, Özel Durumlar, TSPB Meslek Kuralları ve Disiplin Hükümleri.",
            "color": "from-emerald-500/20 to-teal-500/20",
            "borderColor": "border-emerald-500/30",
            "accentColor": "text-emerald-400",
            "icon": "Scale",
            "total_exam_questions": 25,
            "passing_score": 50,
            "target_score": 70
        },
        {
            "id": "1003",
            "code": "1003",
            "name": "Sermaye Piyasası Araçları 1",
            "short_name": "Sermaye Piyasası Araçları",
            "category": "Finansal Araçlar",
            "description": "Paylar (Hisseler), Borçlanma Araçları (Tahvil/Bono), Kira Sertifikaları (Sukuk), Varantlar, Fonlar ve Depo Sertifikaları.",
            "color": "from-cyan-500/20 to-blue-500/20",
            "borderColor": "border-cyan-500/30",
            "accentColor": "text-cyan-400",
            "icon": "Coins",
            "total_exam_questions": 25,
            "passing_score": 50,
            "target_score": 70
        },
        {
            "id": "1005",
            "code": "1005",
            "name": "Yatırım Kuruluşları",
            "short_name": "Yatırım Kuruluşları",
            "category": "Kurumsal",
            "description": "Aracı Kurumlar, Bankalar, Yetki Belgeleri, Müşteri Sınıflandırması, Uygunluk Testleri, Kredili İşlemler ve YTM.",
            "color": "from-purple-500/20 to-indigo-500/20",
            "borderColor": "border-purple-500/30",
            "accentColor": "text-purple-400",
            "icon": "Building2",
            "total_exam_questions": 25,
            "passing_score": 50,
            "target_score": 70
        },
        {
            "id": "1012",
            "code": "1012",
            "name": "Takas, Saklama ve Operasyon İşlemleri",
            "short_name": "Takas, Saklama & Operasyon",
            "category": "Operasyon",
            "description": "Takasbank, Merkezi Kayıt Kuruluşu (MKK), Merkezi Karşı Taraf (MKT), T+2 Takas Döngüsü, DvP ve Temerrüt Yönetimi.",
            "color": "from-amber-500/20 to-orange-500/20",
            "borderColor": "border-amber-500/30",
            "accentColor": "text-amber-400",
            "icon": "ShieldCheck",
            "total_exam_questions": 25,
            "passing_score": 50,
            "target_score": 70
        }
    ]
    
    with open("src/data/modules.json", "w", encoding="utf-8") as f:
        json.dump(modules, f, ensure_ascii=False, indent=2)
    print("[OK] modules.json created")
    
    # Parse Master Question Banks
    master_files = {
        "1001": "Sorular/SPL_1001_Dar_Kapsamli_Sermaye_Piyasasi_Mevzuati_100_Soru_Bankasi.docx",
        "1003": "Sorular/SPL_1003_Sermaye_Piyasasi_Araclari_1_100_Soru_Bankasi.docx",
        "1005": "Sorular/SPL_1005_Yatirim_Kuruluslari_100_Soru_Bankasi.docx",
        "1012": "Sorular/SPL_1012_Takas_Saklama_ve_Operasyon_100_Soru_Bankasi.docx"
    }
    
    master_questions = []
    for mod, path in master_files.items():
        if os.path.exists(path):
            qs = parse_master_questions(path, mod)
            print(f"[OK] Master {mod}: {len(qs)} questions parsed")
            master_questions.extend(qs)
        
    with open("src/data/questions_master.json", "w", encoding="utf-8") as f:
        json.dump(master_questions, f, ensure_ascii=False, indent=2)
        
    # Parse Ogretici Question Bank
    ogretici_path = "Sorular/SPL_Duzey1_400_Soru_Ogretici_Soru_Bankasi.docx"
    if os.path.exists(ogretici_path):
        ogretici_questions = parse_ogretici_questions(ogretici_path)
        print(f"[OK] Ogretici bank: {len(ogretici_questions)} questions parsed")
    else:
        ogretici_questions = []
    
    with open("src/data/questions_ogretici.json", "w", encoding="utf-8") as f:
        json.dump(ogretici_questions, f, ensure_ascii=False, indent=2)
        
    # Combine all questions (800 questions)
    all_questions = master_questions + ogretici_questions
    with open("src/data/all_questions.json", "w", encoding="utf-8") as f:
        json.dump(all_questions, f, ensure_ascii=False, indent=2)
    print(f"[OK] Total questions in all_questions.json: {len(all_questions)}")
    
    # Parse Topic Notes
    note_files = {
        "1001": ("Konu Anlatım/sermaye-piyasasi-mevzuati.docx", "Dar Kapsamlı Sermaye Piyasası Mevzuatı ve Meslek Kuralları"),
        "1003": ("Konu Anlatım/sermaye-piyasasi-araclari.docx", "Sermaye Piyasası Araçları 1"),
        "1005": ("Konu Anlatım/yatirim-kuruluslari.docx", "Yatırım Kuruluşları"),
        "1012": ("Konu Anlatım/takas-saklama-operasyon.docx", "Takas, Saklama ve Operasyon İşlemleri")
    }
    
    topic_notes = {}
    for mod, (path, title) in note_files.items():
        if os.path.exists(path):
            notes = parse_topic_notes_advanced(path, mod, title)
            total_tables = sum(len(s.get("tables", [])) for s in notes["sections"])
            print(f"[OK] Topic notes {mod}: {notes['total_sections']} sections, {total_tables} tables parsed")
            topic_notes[mod] = notes
        
    with open("src/data/topic_notes.json", "w", encoding="utf-8") as f:
        json.dump(topic_notes, f, ensure_ascii=False, indent=2)
    print("[OK] topic_notes.json created with tables")

    # Parse Flashcards (Öğrenme Kartları)
    flashcard_files = {
        "1001": "Öğrenme Kartları/SPL_1001_Flashcards_100_Ogrenme_Karti.docx",
        "1003": "Öğrenme Kartları/SPL_1003_Flashcards_100_Ogrenme_Karti.docx",
        "1005": "Öğrenme Kartları/SPL_1005_Flashcards_100_Ogrenme_Karti.docx",
        "1012": "Öğrenme Kartları/SPL_1012_Flashcards_100_Ogrenme_Karti.docx"
    }

    all_flashcards = []
    for mod, path in flashcard_files.items():
        if os.path.exists(path):
            cards = parse_flashcards(path, mod)
            print(f"[OK] Flashcards {mod}: {len(cards)} cards parsed")
            all_flashcards.extend(cards)

    with open("src/data/flashcards.json", "w", encoding="utf-8") as f:
        json.dump(all_flashcards, f, ensure_ascii=False, indent=2)
    print(f"[OK] Total flashcards in flashcards.json: {len(all_flashcards)}")

    # Parse X5 Detailed Study Book
    x5_path = "Konu Anlatım/SPL_Duzey_1_X5_Detayli_Calisma_Kitabi.docx"
    if os.path.exists(x5_path):
        x5_data = parse_x5_study_guide(x5_path)
        with open("src/data/x5_study_guide.json", "w", encoding="utf-8") as f:
            json.dump(x5_data, f, ensure_ascii=False, indent=2)
        print(f"[OK] X5 Study Guide parsed: {x5_data['total_chapters']} chapters, {len(x5_data['drill_questions'])} drill questions")

if __name__ == "__main__":
    main()
