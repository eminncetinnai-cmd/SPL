#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Yanlış Sorular Analiz Scripti
Bu script çıkarılan yanlış soruları analiz eder ve PDF kontrolü için hazırlar
"""

import json
import sys
import io
from pathlib import Path
from typing import Dict, List, Any

# Set UTF-8 encoding for stdout
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')
else:
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

class Colors:
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    MAGENTA = '\033[95m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'
    RESET = '\033[0m'
    BOLD = '\033[1m'

def load_questions_data() -> List[Dict]:
    """Load questions from all_questions.json"""
    project_root = Path(__file__).parent.parent
    questions_file = project_root / 'src' / 'data' / 'all_questions.json'

    if not questions_file.exists():
        print(f"{Colors.RED}Error: {questions_file} not found{Colors.RESET}")
        sys.exit(1)

    with open(questions_file, 'r', encoding='utf-8') as f:
        return json.load(f)

def analyze_mistakes(mistakes_data: List[Dict], questions_data: List[Dict]) -> Dict[str, Any]:
    """Analyze mistakes against question database"""
    # Create question lookup map
    question_map = {q['id']: q for q in questions_data}

    analysis = {
        "total_mistakes": len(mistakes_data),
        "by_module": {},
        "mistakes_detail": [],
        "needs_pdf_check": []
    }

    for mistake in mistakes_data:
        q_id = mistake['question_id']
        module_id = mistake['module_id']

        # Update module count
        if module_id not in analysis['by_module']:
            analysis['by_module'][module_id] = 0
        analysis['by_module'][module_id] += 1

        # Check if question exists in database
        original_question = question_map.get(q_id)
        if original_question:
            # Compare with database
            is_consistent = (
                original_question['correct_answer'] == mistake['correct_answer'] and
                original_question['text'] == mistake['question_text']
            )

            detail = {
                "question_id": q_id,
                "module_id": module_id,
                "question_text": mistake['question_text'],
                "your_answer": mistake['your_answer'],
                "correct_answer": mistake['correct_answer'],
                "wrong_count": mistake['wrong_count'],
                "is_consistent": is_consistent,
                "explanation": mistake.get('explanation', '')
            }

            analysis['mistakes_detail'].append(detail)
            analysis['needs_pdf_check'].append(detail)
        else:
            detail = {
                "question_id": q_id,
                "module_id": module_id,
                "question_text": mistake['question_text'],
                "your_answer": mistake['your_answer'],
                "correct_answer": mistake['correct_answer'],
                "wrong_count": mistake['wrong_count'],
                "is_consistent": False,
                "explanation": mistake.get('explanation', ''),
                "warning": "Question not found in database"
            }

            analysis['mistakes_detail'].append(detail)
            analysis['needs_pdf_check'].append(detail)

    return analysis

def main():
    print(f"{Colors.BOLD}{Colors.CYAN}Yanlış Sorular Analiz Aracı{Colors.RESET}\n")

    # Check for mistakes data file
    mistakes_file = Path(__file__).parent.parent / 'mistakes_data.json'

    if not mistakes_file.exists():
        print(f"{Colors.RED}Error: {mistakes_file} not found{Colors.RESET}")
        print(f"{Colors.YELLOW}Please first run extract_mistakes.py and paste the JSON data{Colors.RESET}")
        sys.exit(1)

    # Load mistakes data
    print(f"{Colors.BLUE}Loading mistakes data from {mistakes_file}...{Colors.RESET}")
    with open(mistakes_file, 'r', encoding='utf-8') as f:
        mistakes_data = json.load(f)

    if not mistakes_data:
        print(f"{Colors.YELLOW}No mistakes found in the data file{Colors.RESET}")
        sys.exit(0)

    print(f"{Colors.GREEN}Loaded {len(mistakes_data)} mistakes{Colors.RESET}\n")

    # Load questions data
    print(f"{Colors.BLUE}Loading questions database...{Colors.RESET}")
    questions_data = load_questions_data()
    print(f"{Colors.GREEN}Loaded {len(questions_data)} questions{Colors.RESET}\n")

    # Analyze mistakes
    print(f"{Colors.BOLD}{Colors.MAGENTA}=== ANALİZ BAŞLATILIYOR ==={Colors.RESET}\n")
    analysis = analyze_mistakes(mistakes_data, questions_data)

    # Print analysis results
    print(f"{Colors.BOLD}=== ÖZET ==={Colors.RESET}")
    print(f"Toplam Yanlış Soru: {analysis['total_mistakes']}")
    print(f"Modül Dağılımı:")
    for module_id, count in analysis['by_module'].items():
        print(f"  Modül {module_id}: {count} soru")
    print()

    # Print detailed analysis
    print(f"{Colors.BOLD}{Colors.MAGENTA}=== DETAYLI ANALİZ ==={Colors.RESET}\n")

    for i, mistake in enumerate(analysis['mistakes_detail'], 1):
        print(f"{Colors.CYAN}{i}. Soru ID: {mistake['question_id']}{Colors.RESET}")
        print(f"   Modül: {mistake['module_id']}")
        print(f"   Soru: {mistake['question_text'][:80]}...")
        print(f"   Sizin Cevabınız: {mistake['your_answer']}")
        print(f"   Doğru Cevap: {mistake['correct_answer']}")
        print(f"   Yanlış Sayısı: {mistake['wrong_count']}")
        
        if 'warning' in mistake:
            print(f"   {Colors.RED}UYARI: {mistake['warning']}{Colors.RESET}")
        elif not mistake['is_consistent']:
            print(f"   {Colors.YELLOW}DİKKAT: Veritabanı ile tutarsızlık tespit edildi{Colors.RESET}")
        else:
            print(f"   {Colors.GREEN}✓ Veritabanı ile tutarlı{Colors.RESET}")
        
        print()

    # Save analysis results
    analysis_file = Path(__file__).parent.parent / 'mistakes_analysis.json'
    with open(analysis_file, 'w', encoding='utf-8') as f:
        json.dump(analysis, f, ensure_ascii=False, indent=2)

    print(f"{Colors.GREEN}Analiz sonuçları kaydedildi: {analysis_file}{Colors.RESET}\n")

    print(f"{Colors.BOLD}{Colors.MAGENTA}=== SONRAKİ ADIM: PDF KONTROLÜ ==={Colors.RESET}\n")
    print(f"{Colors.YELLOW}Şu sorular PDF kontrolü için hazırlanmış durumda:{Colors.RESET}")
    print(f"{Colors.CYAN}Toplam {len(analysis['needs_pdf_check'])} soru PDF'den kontrol edilecek{Colors.RESET}\n")

if __name__ == '__main__':
    main()
