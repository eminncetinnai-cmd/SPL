import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('src/data/all_questions.json', 'r', encoding='utf-8') as f:
    questions = json.load(f)

print(f"Total questions loaded: {len(questions)}")

leaks = []
for q in questions:
    topic = q.get('topic', '')
    if not topic:
        continue
    
    # Get correct option text
    corr_key = q.get('correct_answer')
    corr_text = ""
    for opt in q.get('options', []):
        if opt['key'] == corr_key:
            corr_text = opt['text']
            break
            
    # Check if topic is a substring of correct option or vice versa
    # (excluding very generic words)
    clean_topic = topic.lower().strip()
    clean_corr = corr_text.lower().strip()
    
    # Significant overlap check
    if len(clean_topic) > 8 and (clean_topic in clean_corr or clean_corr in clean_topic):
        leaks.append({
            'id': q['id'],
            'module_id': q['module_id'],
            'topic': topic,
            'correct_answer': corr_key,
            'corr_text': corr_text,
            'question_text': q['text'][:80]
        })

print(f"\nFound {len(leaks)} questions where 'topic' directly leaks the correct answer:")
for l in leaks[:15]:
    print(f"  [{l['id']}] Topic: '{l['topic']}' -> Correct ({l['correct_answer']}): '{l['corr_text']}'")

if len(leaks) > 15:
    print(f"  ... and {len(leaks) - 15} more.")
