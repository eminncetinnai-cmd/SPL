from pathlib import Path
import fitz  # PyMuPDF

PDF_FILE = Path(r"C:\Users\e.cetin\Desktop\SPL\kaynak\1012_MKT_30062026_202607141057.pdf")

def extract_text_from_pdf(pdf_path):
    """PDF'den metin çıkarır"""
    text = ""
    doc = fitz.open(pdf_path)
    for page_num in range(len(doc)):
        page = doc[page_num]
        text += page.get_text() + "\n"
    doc.close()
    return text

try:
    print("PDF'den metin çıkarılıyor...")
    pdf_text = extract_text_from_pdf(PDF_FILE)
    print(f"Toplam {len(pdf_text)} karakter çıkarıldı.")

    # Dosyaya kaydet
    output_file = Path(r"C:\Users\e.cetin\Desktop\SPL\kaynak\1012_text.txt")
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(pdf_text)
    print(f"Metin {output_file} dosyasına kaydedildi.")

    # İlk 500 karakteri göster
    print(f"\nİlk 500 karakter:\n{pdf_text[:500]}")

except ImportError:
    print("PyMuPDF kütüphanesi yüklü değil. Yükleniyor...")
    import subprocess
    subprocess.run(['pip', 'install', 'PyMuPDF'])
    print("Yükleme tamamlandı. Lütfen script'i tekrar çalıştırın.")
except Exception as e:
    print(f"Hata: {e}")
