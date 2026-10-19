#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
SPL Soru Shuffle Konsistens Dogrulama Scripti
Bu script soru veritabanindaki shuffle (karistirma) mantigini dogrular:
1. Siklar karistirildiginda correct_answer'in dogru hesaplanip hesaplanmadigini kontrol eder
2. Aciklamalarin orijinal sik referanslariyla celisip celismedigini kontrol eder
3. Shuffle sonrasi state ile orijinal state arasindaki tutarsizliklari tespit eder
"""

import json
import re
import sys
import io
import random
from pathlib import Path
from typing import Dict, List, Tuple, Any, Optional
from copy import deepcopy

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

def load_json_file(file_path: Path) -> Any:
    """Load JSON file safely"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception as e:
        print(f"{Colors.RED}Error loading {file_path}: {e}{Colors.RESET}")
        sys.exit(1)

def shuffle_options_fisher_yates(options: List[Dict]) -> List[Dict]:
    """
    Fisher-Yates shuffle algoritmasi ile siklari karistirir
    Bu, TypeScript'deki shuffleArray fonksiyonunun Python karsiligidir
    """
    shuffled = deepcopy(options)
    for i in range(len(shuffled) - 1, 0, -1):
        j = random.randint(0, i)
        shuffled[i], shuffled[j] = shuffled[j], shuffled[i]
    return shuffled

def remap_correct_answer_after_shuffle(original_question: Dict) -> Dict:
    """
    Siklar karistirildiktan sonra correct_answer'i yeniden hesaplar
    Bu, TypeScript'deki shuffleQuestionOptions fonksiyonunun Python karsiligidir
    """
    original_correct_key = original_question['correct_answer']
    original_options = original_question['options']

    # Dogru cevabin metnini bul
    correct_text = None
    for opt in original_options:
        if opt['key'] == original_correct_key:
            correct_text = opt['text']
            break

    if correct_text is None:
        # Hata: correct_answer siklarda yok
        return original_question

    # Siklari karistir
    shuffled_options = shuffle_options_fisher_yates(original_options)

    # Yeni A-E anahtarlarini ata
    keys = ['A', 'B', 'C', 'D', 'E']
    new_correct_key = None

    new_options = []
    for i, opt in enumerate(shuffled_options):
        key = keys[i] if i < len(keys) else 'A'
        if opt['text'] == correct_text:
            new_correct_key = key
        new_options.append({
            'key': key,
            'text': opt['text']
        })

    if new_correct_key is None:
        # Hata: Dogru metin bulunamadi
        return original_question

    # Aciklamadan statik harf referanslarini temizle
    sanitized_explanation = original_question.get('explanation', '')
    if sanitized_explanation:
        # Bu kaliblar TypeScript'deki sanitizeExplanation mantiginin karsiligidir
        # Simplified regex to avoid Turkish character encoding issues
        sanitized_explanation = re.sub(
            r'\s*[A-Ea-e]\s*',
            '',
            sanitized_explanation
        ).strip()

    return {
        **original_question,
        'options': new_options,
        'correct_answer': new_correct_key,
        'explanation': sanitized_explanation
    }

def validate_shuffle_logic(question: Dict, iterations: int = 100) -> List[str]:
    """
    Bir sorunun shuffle mantigini dogrular (100 iterasyon ile)
    """
    errors = []

    for i in range(iterations):
        shuffled = remap_correct_answer_after_shuffle(question)

        # 1. Yeni correct_answer'in karistirilmis siklarda oldugunu kontrol et
        new_correct_key = shuffled['correct_answer']
        correct_option_exists = False
        for opt in shuffled['options']:
            if opt['key'] == new_correct_key:
                correct_option_exists = True
                break

        if not correct_option_exists:
            errors.append(f"Iteration {i}: correct_answer '{new_correct_key}' not found in shuffled options")

        # 2. Dogru cevabin metninin degismedigini kontrol et
        original_correct_text = None
        for opt in question['options']:
            if opt['key'] == question['correct_answer']:
                original_correct_text = opt['text']
                break

        new_correct_text = None
        for opt in shuffled['options']:
            if opt['key'] == shuffled['correct_answer']:
                new_correct_text = opt['text']
                break

        if original_correct_text != new_correct_text:
            errors.append(f"Iteration {i}: Correct text changed from '{original_correct_text}' to '{new_correct_text}'")

        # 3. Sik sayisinin degismedigini kontrol et
        if len(shuffled['options']) != len(question['options']):
            errors.append(f"Iteration {i}: Option count changed from {len(question['options'])} to {len(shuffled['options'])}")

        # 4. Siklarin A-E formatinda oldugunu kontrol et
        valid_keys = ['A', 'B', 'C', 'D', 'E']
        for opt in shuffled['options']:
            if opt['key'] not in valid_keys:
                errors.append(f"Iteration {i}: Invalid option key '{opt['key']}'")

    return errors

def check_explanation_reference_issues(question: Dict) -> List[str]:
    """
    Aciklamadaki statik harf referanslarinin sorunlu olup olmadigini kontrol eder
    """
    issues = []
    explanation = question.get('explanation', '')

    if not explanation:
        return issues

    # Aciklamada harf referansi var mi?
    letter_patterns = re.findall(r'[A-E]\s*şıkkı|[A-E]\s*seçenek|[A-E]\s*cevap', explanation, re.IGNORECASE)

    if letter_patterns:
        issues.append(f"Explanation contains static letter references: {letter_patterns}")

    return issues

def analyze_question_content_consistency(question: Dict) -> List[str]:
    """
    Sorunun icerik tutarsizliklarini analiz eder
    """
    issues = []

    # 1. correct_answer alaninin siklarda oldugunu kontrol et
    correct_key = question['correct_answer']
    correct_exists = False
    for opt in question['options']:
        if opt['key'] == correct_key:
            correct_exists = True
            break

    if not correct_exists:
        issues.append(f"correct_answer '{correct_key}' not found in options")

    # 2. Tum siklarin benzersiz anahtarlara sahip oldugunu kontrol et
    keys = [opt['key'] for opt in question['options']]
    if len(keys) != len(set(keys)):
        issues.append(f"Duplicate option keys found: {keys}")

    # 3. Bos sik olup olmadigini kontrol et
    for opt in question['options']:
        if not opt['text'].strip():
            issues.append(f"Empty option text for key '{opt['key']}'")

    return issues

def main():
    print(f"{Colors.BOLD}{Colors.CYAN}SPL Soru Shuffle Konsistens Dogrulama Araci{Colors.RESET}\n")

    # Load question data
    project_root = Path(__file__).parent.parent
    questions_file = project_root / 'src' / 'data' / 'all_questions.json'

    if not questions_file.exists():
        print(f"{Colors.RED}Error: {questions_file} not found{Colors.RESET}")
        sys.exit(1)

    print(f"{Colors.BLUE}Loading questions from {questions_file}...{Colors.RESET}")
    questions = load_json_file(questions_file)

    print(f"{Colors.GREEN}Loaded {len(questions)} questions{Colors.RESET}\n")

    # Validation results
    shuffle_errors = []
    content_issues = []
    explanation_issues = []

    print(f"{Colors.BOLD}{Colors.MAGENTA}Starting shuffle consistency validation...{Colors.RESET}\n")

    for i, question in enumerate(questions, 1):
        q_id = question.get('id', f'Question_{i}')

        # Validate shuffle logic (10 iterations per question for speed)
        shuf_errors = validate_shuffle_logic(question, iterations=10)
        if shuf_errors:
            shuffle_errors.append((q_id, shuf_errors[:3]))  # Store first 3 errors

        # Check content consistency
        cont_issues = analyze_question_content_consistency(question)
        if cont_issues:
            content_issues.append((q_id, cont_issues))

        # Check explanation reference issues
        exp_issues = check_explanation_reference_issues(question)
        if exp_issues:
            explanation_issues.append((q_id, exp_issues))

    # Print results
    print(f"{Colors.BOLD}=== VALIDATION RESULTS ==={Colors.RESET}\n")

    # Shuffle errors
    if shuffle_errors:
        print(f"{Colors.RED}{Colors.BOLD}[X] SHUFFLE LOGIC ERRORS ({len(shuffle_errors)} questions):{Colors.RESET}")
        for q_id, errors in shuffle_errors[:5]:  # Show first 5
            print(f"{Colors.YELLOW}  {q_id}:{Colors.RESET}")
            for err in errors:
                print(f"    - {err}")
        if len(shuffle_errors) > 5:
            print(f"  ... and {len(shuffle_errors) - 5} more")
        print()
    else:
        print(f"{Colors.GREEN}{Colors.BOLD}[OK] No shuffle logic errors found{Colors.RESET}\n")

    # Content issues
    if content_issues:
        print(f"{Colors.RED}{Colors.BOLD}[X] CONTENT CONSISTENCY ISSUES ({len(content_issues)} questions):{Colors.RESET}")
        for q_id, issues in content_issues[:5]:  # Show first 5
            print(f"{Colors.YELLOW}  {q_id}:{Colors.RESET}")
            for issue in issues:
                print(f"    - {issue}")
        if len(content_issues) > 5:
            print(f"  ... and {len(content_issues) - 5} more")
        print()
    else:
        print(f"{Colors.GREEN}{Colors.BOLD}[OK] No content consistency issues found{Colors.RESET}\n")

    # Explanation issues
    if explanation_issues:
        print(f"{Colors.YELLOW}{Colors.BOLD}[!] EXPLANATION REFERENCE ISSUES ({len(explanation_issues)} questions):{Colors.RESET}")
        for q_id, issues in explanation_issues[:5]:  # Show first 5
            print(f"{Colors.CYAN}  {q_id}:{Colors.RESET}")
            for issue in issues:
                print(f"    - {issue}")
        if len(explanation_issues) > 5:
            print(f"  ... and {len(explanation_issues) - 5} more")
        print()
    else:
        print(f"{Colors.GREEN}{Colors.BOLD}[OK] No explanation reference issues found{Colors.RESET}\n")

    # Summary
    total_issues = len(shuffle_errors) + len(content_issues) + len(explanation_issues)
    print(f"{Colors.BOLD}=== SUMMARY ==={Colors.RESET}")
    print(f"Total questions: {len(questions)}")
    print(f"Shuffle logic errors: {len(shuffle_errors)}")
    print(f"Content consistency issues: {len(content_issues)}")
    print(f"Explanation reference issues: {len(explanation_issues)}")
    print(f"Total issues: {total_issues}")

    if total_issues == 0:
        print(f"\n{Colors.GREEN}{Colors.BOLD}[OK] All shuffle consistency validations passed!{Colors.RESET}")
        return 0
    else:
        print(f"\n{Colors.RED}{Colors.BOLD}[X] Validation failed with {total_issues} issues{Colors.RESET}")
        return 1

if __name__ == '__main__':
    sys.exit(main())
