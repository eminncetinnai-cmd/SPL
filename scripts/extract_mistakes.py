#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
LocalStorage Yanlış Sorular Çıkarma Scripti
Bu script localStorage'daki yanlış soruları çıkarır ve analiz için hazırlar
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

def create_browser_script() -> str:
    """Create JavaScript code to extract localStorage data"""
    return """
// Run this in browser console to extract mistakes data
(function() {
    const STORAGE_KEY = 'spk_spl1_progress_v6';
    const data = JSON.parse(localStorage.getItem(STORAGE_KEY) || '{}');
    
    if (!data.mistakes || Object.keys(data.mistakes).length === 0) {
        console.log('No mistakes found in localStorage');
        return null;
    }
    
    const mistakes = Object.values(data.mistakes).filter(m => !m.resolved);
    
    const extracted = mistakes.map(m => ({
        question_id: m.question.id,
        module_id: m.question.module_id,
        question_text: m.question.text,
        options: m.question.options,
        correct_answer: m.question.correct_answer,
        explanation: m.question.explanation,
        your_answer: m.last_selected_option,
        wrong_count: m.wrong_count,
        last_wrong_date: m.last_wrong_date
    }));
    
    return JSON.stringify(extracted, null, 2);
})();
"""

def analyze_mistakes_from_json(mistakes_json: str, questions_data: List[Dict]) -> Dict[str, Any]:
    """Analyze mistakes from JSON string"""
    try:
        mistakes = json.loads(mistakes_json)
    except json.JSONDecodeError as e:
        print(f"{Colors.RED}Error parsing mistakes JSON: {e}{Colors.RESET}")
        return {"error": "Invalid JSON"}

    if not mistakes:
        return {"error": "No mistakes found"}

    # Create question lookup map
    question_map = {q['id']: q for q in questions_data}

    analysis = {
        "total_mistakes": len(mistakes),
        "by_module": {},
        "mistakes_detail": []
    }

    for mistake in mistakes:
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

            analysis['mistakes_detail'].append({
                "question_id": q_id,
                "module_id": module_id,
                "question_text": mistake['question_text'][:100] + "...",
                "your_answer": mistake['your_answer'],
                "correct_answer": mistake['correct_answer'],
                "wrong_count": mistake['wrong_count'],
                "is_consistent": is_consistent,
                "needs_pdf_check": True
            })
        else:
            analysis['mistakes_detail'].append({
                "question_id": q_id,
                "module_id": module_id,
                "question_text": mistake['question_text'][:100] + "...",
                "your_answer": mistake['your_answer'],
                "correct_answer": mistake['correct_answer'],
                "wrong_count": mistake['wrong_count'],
                "is_consistent": False,
                "needs_pdf_check": True,
                "warning": "Question not found in database"
            })

    return analysis

def main():
    print(f"{Colors.BOLD}{Colors.CYAN}LocalStorage Yanlış Sorular Çıkarma Aracı{Colors.RESET}\n")

    # Load questions data
    print(f"{Colors.BLUE}Loading questions database...{Colors.RESET}")
    questions_data = load_questions_data()
    print(f"{Colors.GREEN}Loaded {len(questions_data)} questions{Colors.RESET}\n")

    # Provide browser script
    print(f"{Colors.BOLD}{Colors.MAGENTA}=== ADIM 1: Tarayıcıda Bu Script'i Çalıştırın ==={Colors.RESET}\n")
    print(f"{Colors.YELLOW}1. Tarayıcıda http://localhost:5174 adresine gidin{Colors.RESET}")
    print(f"{Colors.YELLOW}2. F12 tuşuna basarak Console'u açın{Colors.RESET}")
    print(f"{Colors.YELLOW}3. Aşağıdaki JavaScript kodunu kopyalayıp console'a yapıştırın ve Enter'a basın{Colors.RESET}\n")
    print(f"{Colors.CYAN}{Colors.BOLD}--- JAVASCRIPT KODU ---{Colors.RESET}")
    print(create_browser_script())
    print(f"{Colors.CYAN}{Colors.BOLD}--- JAVASCRIPT KODU SONU ---{Colors.RESET}\n")
    print(f"{Colors.YELLOW}4. Console'da çıkan JSON verisini kopyalayın{Colors.RESET}")
    print(f"{Colors.YELLOW}5. Bu veriyi bana gönderin veya aşağıdaki dosyaya kaydedin{Colors.RESET}\n")

    # Create output file for manual paste
    output_file = Path(__file__).parent.parent / 'mistakes_data.json'
    print(f"{Colors.BLUE}Alternatif: JSON verisini şu dosyaya kaydedebilirsiniz:{Colors.RESET}")
    print(f"{Colors.GREEN}{output_file}{Colors.RESET}\n")

    # Check if file already exists
    if output_file.exists():
        print(f"{Colors.YELLOW}Not: {output_file} zaten var. Eğer buraya yeni veri yapıştırırsanız analiz edebilirim.{Colors.RESET}\n")

    print(f"{Colors.BOLD}{Colors.MAGENTA}=== ADIM 2: Analiz için Hazır ==={Colors.RESET}\n")
    print(f"{Colors.GREEN}Veriyi aldığınızda 'analiz' komutunu kullanabilirim{Colors.RESET}")
    print(f"{Colors.GREEN}Örnek: Lütfen şu veriyi analiz et: [JSON verisi]{Colors.RESET}\n")

if __name__ == '__main__':
    main()
