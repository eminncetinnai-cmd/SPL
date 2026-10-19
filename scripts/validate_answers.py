#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
SPL Soru Cevap Dogrulama Scripti
Bu script soru veritabanindaki tutarsizliklari tespit eder:
1. correct_answer alaninin siklarla uyumunu kontrol eder
2. Aciklama iceriginin dogru cevapla celisip celismedigini kontrol eder
3. Siklarin A-E formatinda olup olmadigini kontrol eder
"""

import json
import re
import sys
import io
from pathlib import Path
from typing import Dict, List, Tuple, Any

# Set UTF-8 encoding for stdout
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')
else:
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# Colors for terminal output
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

def validate_question_structure(question: Dict) -> List[str]:
    """Validate basic question structure"""
    errors = []

    # Check required fields
    required_fields = ['id', 'module_id', 'text', 'options', 'correct_answer', 'explanation']
    for field in required_fields:
        if field not in question:
            errors.append(f"Missing required field: {field}")

    # Check options structure
    if 'options' in question:
        if not isinstance(question['options'], list):
            errors.append("Options must be a list")
        else:
            valid_keys = ['A', 'B', 'C', 'D', 'E']
            for opt in question['options']:
                if not isinstance(opt, dict):
                    errors.append("Each option must be a dictionary")
                    continue
                if 'key' not in opt or 'text' not in opt:
                    errors.append("Option must have 'key' and 'text' fields")
                elif opt['key'] not in valid_keys:
                    errors.append(f"Invalid option key: {opt['key']} (must be A-E)")

    # Check correct_answer format
    if 'correct_answer' in question:
        if question['correct_answer'] not in ['A', 'B', 'C', 'D', 'E']:
            errors.append(f"Invalid correct_answer: {question['correct_answer']} (must be A-E)")

    return errors

def validate_answer_consistency(question: Dict) -> List[str]:
    """Validate that correct_answer matches the options"""
    errors = []

    if 'options' not in question or 'correct_answer' not in question:
        return errors

    correct_key = question['correct_answer']
    correct_option = None

    for opt in question['options']:
        if opt['key'] == correct_key:
            correct_option = opt
            break

    if correct_option is None:
        errors.append(f"correct_answer '{correct_key}' not found in options")
    elif not correct_option['text'].strip():
        errors.append(f"correct_answer '{correct_key}' has empty text")

    return errors

def validate_explanation_consistency(question: Dict) -> List[str]:
    """Validate that explanation doesn't contradict the correct answer"""
    errors = []
    warnings = []

    if 'explanation' not in question or 'correct_answer' not in question:
        return errors

    explanation = question['explanation']
    correct_key = question['correct_answer']

    # Check if explanation mentions different letter as correct
    # Patterns like "A şıkkı doğrudur", "Doğru cevap B", etc.
    conflicting_patterns = [
        r'[A-E]\s*şıkkı\s+(?:doğru|cevap|yanlış)',
        r'[Dd]oğru\s+(?:seçenek|cevap|şık)\s+[A-E]',
        r'[Yy]anlış\s+(?:seçenek|cevap|şık)\s+[A-E]',
    ]

    for pattern in conflicting_patterns:
        matches = re.findall(pattern, explanation, re.IGNORECASE)
        for match in matches:
            # Extract the letter from the match
            letter_match = re.search(r'[A-E]', match)
            if letter_match:
                mentioned_letter = letter_match.group()
                if mentioned_letter != correct_key:
                    warnings.append(f"Explanation mentions '{mentioned_letter}' but correct_answer is '{correct_key}'")

    # Check if explanation explicitly states the correct answer is wrong
    negative_patterns = [
        rf'{correct_key}\s*şıkkı\s+yanlış',
        rf'[Dd]oğru\s+(?:cevap|şık)\s+(?!{correct_key})[A-E]',
    ]

    for pattern in negative_patterns:
        if re.search(pattern, explanation, re.IGNORECASE):
            errors.append(f"Explanation seems to contradict correct_answer '{correct_key}'")

    return errors, warnings

def check_duplicate_questions(questions: List[Dict]) -> List[Tuple[str, str]]:
    """Check for duplicate question texts"""
    duplicates = []
    seen_texts = {}

    for q in questions:
        text = q.get('text', '').strip().lower()
        if text in seen_texts:
            duplicates.append((seen_texts[text], q['id']))
        else:
            seen_texts[text] = q['id']

    return duplicates

def main():
    print(f"{Colors.BOLD}{Colors.CYAN}SPL Soru Cevap Doğrulama Aracı{Colors.RESET}\n")

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
    structure_errors = []
    consistency_errors = []
    explanation_warnings = []
    duplicates = []

    print(f"{Colors.BOLD}{Colors.MAGENTA}Starting validation...{Colors.RESET}\n")

    for i, question in enumerate(questions, 1):
        q_id = question.get('id', f'Question_{i}')

        # Validate structure
        struct_errors = validate_question_structure(question)
        if struct_errors:
            structure_errors.append((q_id, struct_errors))

        # Validate answer consistency
        ans_errors = validate_answer_consistency(question)
        if ans_errors:
            consistency_errors.append((q_id, ans_errors))

        # Validate explanation consistency
        exp_errors, exp_warnings = validate_explanation_consistency(question)
        if exp_errors:
            consistency_errors.append((q_id, exp_errors))
        if exp_warnings:
            explanation_warnings.append((q_id, exp_warnings))

    # Check for duplicates
    duplicates = check_duplicate_questions(questions)

    # Print results
    print(f"{Colors.BOLD}=== VALIDATION RESULTS ==={Colors.RESET}\n")

    # Structure errors
    if structure_errors:
        print(f"{Colors.RED}{Colors.BOLD}[X] STRUCTURE ERRORS ({len(structure_errors)} questions):{Colors.RESET}")
        for q_id, errors in structure_errors[:10]:  # Show first 10
            print(f"{Colors.YELLOW}  {q_id}:{Colors.RESET}")
            for err in errors:
                print(f"    - {err}")
        if len(structure_errors) > 10:
            print(f"  ... and {len(structure_errors) - 10} more")
        print()
    else:
        print(f"{Colors.GREEN}{Colors.BOLD}[OK] No structure errors found{Colors.RESET}\n")

    # Consistency errors
    if consistency_errors:
        print(f"{Colors.RED}{Colors.BOLD}[X] CONSISTENCY ERRORS ({len(consistency_errors)} questions):{Colors.RESET}")
        for q_id, errors in consistency_errors[:10]:  # Show first 10
            print(f"{Colors.YELLOW}  {q_id}:{Colors.RESET}")
            for err in errors:
                print(f"    - {err}")
        if len(consistency_errors) > 10:
            print(f"  ... and {len(consistency_errors) - 10} more")
        print()
    else:
        print(f"{Colors.GREEN}{Colors.BOLD}[OK] No consistency errors found{Colors.RESET}\n")

    # Explanation warnings
    if explanation_warnings:
        print(f"{Colors.YELLOW}{Colors.BOLD}[!] EXPLANATION WARNINGS ({len(explanation_warnings)} questions):{Colors.RESET}")
        for q_id, warnings in explanation_warnings[:10]:  # Show first 10
            print(f"{Colors.CYAN}  {q_id}:{Colors.RESET}")
            for warn in warnings:
                print(f"    - {warn}")
        if len(explanation_warnings) > 10:
            print(f"  ... and {len(explanation_warnings) - 10} more")
        print()
    else:
        print(f"{Colors.GREEN}{Colors.BOLD}[OK] No explanation warnings found{Colors.RESET}\n")

    # Duplicates
    if duplicates:
        print(f"{Colors.YELLOW}{Colors.BOLD}[!] DUPLICATE QUESTIONS ({len(duplicates)} pairs):{Colors.RESET}")
        for id1, id2 in duplicates[:10]:  # Show first 10
            print(f"  {id1} <-> {id2}")
        if len(duplicates) > 10:
            print(f"  ... and {len(duplicates) - 10} more")
        print()
    else:
        print(f"{Colors.GREEN}{Colors.BOLD}[OK] No duplicate questions found{Colors.RESET}\n")

    # Summary
    total_issues = len(structure_errors) + len(consistency_errors) + len(explanation_warnings) + len(duplicates)
    print(f"{Colors.BOLD}=== SUMMARY ==={Colors.RESET}")
    print(f"Total questions: {len(questions)}")
    print(f"Structure errors: {len(structure_errors)}")
    print(f"Consistency errors: {len(consistency_errors)}")
    print(f"Explanation warnings: {len(explanation_warnings)}")
    print(f"Duplicate pairs: {len(duplicates)}")
    print(f"Total issues: {total_issues}")

    if total_issues == 0:
        print(f"\n{Colors.GREEN}{Colors.BOLD}[OK] All validations passed!{Colors.RESET}")
        return 0
    else:
        print(f"\n{Colors.RED}{Colors.BOLD}[X] Validation failed with {total_issues} issues{Colors.RESET}")
        return 1

if __name__ == '__main__':
    sys.exit(main())
