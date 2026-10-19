import re
from pathlib import Path

PDF_TEXT_FILE = Path(r"C:\Users\e.cetin\Desktop\SPL\kaynak\1012_text.txt")

# PDF metnini yükle
with open(PDF_TEXT_FILE, 'r', encoding='utf-8') as f:
    pdf_text = f.read()

# PDF'ten soruları çıkarmak için regex pattern'leri
# Soru başlangıç pattern'leri (genellikle rakam veya soru işareti ile başlar)
question_patterns = [
    r'\d+\.\s+[A-ZÇĞİÖŞÜ\s]+',  # "1. TERS REPO İŞLEMİ" gibi
    r'\d+\-\s+[A-ZÇĞİÖŞÜ\s]+',  # "1- TERS REPO İŞLEMİ" gibi
    r'[A-ZÇĞİÖŞÜ]+\s+\d+\.',  # "SORU 1." gibi
]

# Cevap anahtarlarını ara
answer_patterns = [
    r'Cevap:\s*([A-E])',
    r'Dogru Cevap:\s*([A-E])',
    r'Doğru Cevap:\s*([A-E])',
    r'Cevap\s*[A-ZÇĞİÖŞÜ]+:\s*([A-E])',
]

print("PDF metni analiz ediliyor...\n")

# Bölüm soruları bölümlerini bul
# İçindekiler'de "BÖLÜM SORULARI" ve sayfa numaraları var
section_pattern = r'BÖLÜM SORULARI\s*\.\.\.\.\.\.\.\.\s*(\d+)'
sections = re.findall(section_pattern, pdf_text)

print(f"Bulunan bölüm soruları sayfaları: {sections}")

# PDF'te soru pattern'lerini ara
# Önce soru başlıklarını bul
question_headings = re.findall(r'[A-ZÇĞİÖŞÜ\s]+\d+\.', pdf_text[:5000])

print(f"\nİlk 5000 karakterde bulunan soru başlıkları: {question_headings[:10]}")

# Soru-cevap pattern'lerini daha detaylı ara
# Genellikle sorular arasında boş satırlar olur
paragraphs = pdf_text.split('\n\n')

questions_found = []
for i, para in enumerate(paragraphs):
    # Cevap pattern'ini ara
    for pattern in answer_patterns:
        match = re.search(pattern, para, re.IGNORECASE)
        if match:
            answer = match.group(1)
            # Önceki paragrafları soru metni olarak al
            question_text = paragraphs[max(0, i-5):i]
            questions_found.append({
                'answer': answer,
                'text': '\n'.join(question_text)[:200]
            })
            break

print(f"\nToplam {len(questions_found)} potansiyel soru-cevap çifti bulundu")
print("\nİlk 5 örnek:")
for i, q in enumerate(questions_found[:5], 1):
    print(f"{i}. Cevap: {q['answer']}")
    print(f"   Metin: {q['text']}")
    print()
