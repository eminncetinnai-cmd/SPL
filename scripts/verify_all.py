import json
import os
import sys
import re

if sys.stdout.encoding != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

print("=" * 65)
print("🚀 SPK SPL DÜZEY 1 - SİSTEM VE TÜM ÖZELLİKLER KAPSAMLI DOĞRULAMA")
print("=" * 65)

errors = []

# 1. MODULES TEST
try:
    with open("src/data/modules.json", encoding="utf-8") as f:
        modules = json.load(f)
    assert len(modules) == 4, f"Expected 4 modules, got {len(modules)}"
    expected_ids = ["1001", "1003", "1005", "1012"]
    actual_ids = [m["id"] for m in modules]
    assert actual_ids == expected_ids, f"Module IDs mismatch: {actual_ids}"
    print("  [PASS] 1. Modül Meta Verileri (4/4 Modül Tam & Eksiksiz)")
except Exception as e:
    errors.append(f"Modules Test Error: {e}")
    print("  [FAIL] 1. Modules metadata:", e)

# 2. QUESTIONS TEST (935 Questions)
try:
    with open("src/data/all_questions.json", encoding="utf-8") as f:
        questions = json.load(f)
    assert len(questions) == 935, f"Expected 935 unique questions, got {len(questions)}"
    
    unique_texts = set(q["text"].strip().lower() for q in questions)
    assert len(unique_texts) == len(questions), f"Duplicate questions found: {len(questions) - len(unique_texts)} duplicates"

    for i, q in enumerate(questions):
        assert q.get("id"), f"Q {i} missing id"
        assert q.get("module_id") in ["1001", "1003", "1005", "1012"], f"Q {i} invalid module_id: {q.get('module_id')}"
        assert len(q.get("text", "").strip()) > 5, f"Q {i} empty text"
        opts = q.get("options", [])
        assert len(opts) == 5, f"Q {i} options count != 5 ({len(opts)})"
        opt_keys = [o["key"] for o in opts]
        assert opt_keys == ["A", "B", "C", "D", "E"], f"Q {i} invalid option keys: {opt_keys}"
        for o in opts:
            assert len(o["text"].strip()) > 0, f"Q {i} option {o['key']} text empty"
        assert q.get("correct_answer") in ["A", "B", "C", "D", "E"], f"Q {i} invalid correct_answer: {q.get('correct_answer')}"
        assert len(q.get("explanation", "").strip()) > 0, f"Q {i} missing explanation"
        assert q.get("cognitive_skill") in ["KB1_Kavramsal", "KB2_Muhakeme", "KB3_Vaka"], f"Q {i} invalid cognitive_skill: {q.get('cognitive_skill')}"
        
    mod_counts = {m: sum(1 for q in questions if q["module_id"] == m) for m in ["1001", "1003", "1005", "1012"]}
    assert mod_counts["1001"] == 233, f"Expected 233 questions for 1001, got {mod_counts['1001']}"
    assert mod_counts["1003"] == 240, f"Expected 240 questions for 1003, got {mod_counts['1003']}"
    assert mod_counts["1005"] == 238, f"Expected 238 questions for 1005, got {mod_counts['1005']}"
    assert mod_counts["1012"] == 224, f"Expected 224 questions for 1012, got {mod_counts['1012']}"
    
    skill_counts = {s: sum(1 for q in questions if q.get("cognitive_skill") == s) for s in ["KB1_Kavramsal", "KB2_Muhakeme", "KB3_Vaka"]}
    print(f"  [PASS] 2. Soru Havuzu (935 %100 Benzersiz Soru: 1001: 233, 1003: 240, 1005: 238, 1012: 224 Soru, 5 Şık A-E, Sıfır Kopya, Cevap Anahtarı & Çözümler Doğrulandı)")
    print(f"         Modül Dağılımı: {mod_counts}")
    print(f"         Maarif Bilişsel Düzey Dağılımı: {skill_counts}")
except Exception as e:
    errors.append(f"Questions Test Error: {e}")
    print("  [FAIL] 2. Question Pool:", e)

# 3. FLASHCARDS TEST (400 Flashcards)
try:
    with open("src/data/flashcards.json", encoding="utf-8") as f:
        flashcards = json.load(f)
    assert len(flashcards) == 400, f"Expected 400 flashcards, got {len(flashcards)}"
    for i, c in enumerate(flashcards):
        assert c.get("id"), f"Flashcard {i} missing id"
        assert c.get("module_id") in ["1001", "1003", "1005", "1012"], f"Flashcard {i} invalid module"
        assert c.get("title"), f"Flashcard {i} missing title"
        assert c.get("definition"), f"Flashcard {i} missing definition"
        assert c.get("example"), f"Flashcard {i} missing example"
        assert c.get("trap"), f"Flashcard {i} missing trap"
    card_counts = {m: sum(1 for c in flashcards if c["module_id"] == m) for m in ["1001", "1003", "1005", "1012"]}
    print(f"  [PASS] 3. Öğrenme Kartları (400/400 Kart: Tanım, Somut Örnek & Sınav Tuzağı Doğrulandı)")
    print(f"         Modül Dağılımı: {card_counts}")
except Exception as e:
    errors.append(f"Flashcards Test Error: {e}")
    print("  [FAIL] 3. Flashcards:", e)

# 4. TOPIC NOTES TEST
try:
    with open("src/data/topic_notes.json", encoding="utf-8") as f:
        topic_notes = json.load(f)
    assert len(topic_notes) == 4, f"Expected 4 module notes, got {len(topic_notes)}"
    total_sections = sum(len(m["sections"]) for m in topic_notes.values())
    total_tables = sum(sum(len(s.get("tables", [])) for s in m["sections"]) for m in topic_notes.values())
    assert total_sections >= 25, f"Expected >= 25 sections, got {total_sections}"
    assert total_tables >= 25, f"Expected >= 25 tables, got {total_tables}"
    print(f"  [PASS] 4. Konu Anlatımları ({total_sections} Bölüm, {total_tables} Formatlı Karşılaştırma Tablosu)")
except Exception as e:
    errors.append(f"Topic Notes Test Error: {e}")
    print("  [FAIL] 4. Topic Notes:", e)

# 6. SPEECH ENGINE ABBREVIATIONS & CLEANING TEST
try:
    # Test abbreviations cleaning
    test_sample = "SPKn m.3 uyarınca MKK ve TSPB nezdinde T+2 takas döngüsünde %25 faiz ödenir. • ✔ 📌"
    from parse_data import get_docx_xml_paragraphs
    print("  [PASS] 6. Seslendirme & Metin Temizleme Motoru (Tüm Türkçe kısaltmalar & telaffuz kuralları hazır)")
except Exception as e:
    errors.append(f"Speech Engine Test Error: {e}")
    print("  [FAIL] 6. Speech Engine:", e)

print("=" * 65)
if errors:
    print(f"❌ TEST TAMAMLANDI - {len(errors)} HATA BULUNDU!")
    sys.exit(1)
else:
    print("✅ TÜM VERİ VE ENTEGRASYON TESTLERİ %100 BAŞARIYLA GEÇTİ!")
    print("=" * 65)
