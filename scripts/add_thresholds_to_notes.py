with open('scripts/generate_master_topic_notes.py', 'r', encoding='utf-8') as f:
    text = f.read()

target1 = '"1. BIST Pay Piyasası (Hisse Senetleri): Standart takas süresi T+2\'DİR (İşlem gününü izleyen İKİNCİ iş günü). Pazartesi günü alınan bir hissenin bedeli ve mülkiyeti Çarşamba günü takas edilir. Cuma günü yapılan işlemin takası ise araya hafta sonu girdiği için Salı günü gerçekleşir.",'
repl1 = '"1. BIST Pay Piyasası (Hisse Senetleri): Standart takas süresi T+2\'DİR (İşlem gününü izleyen İKİNCİ iş günü). Pazartesi günü alınan bir hissenin bedeli ve mülkiyeti Çarşamba günü takas edilir. Cuma günü yapılan işlemin takası ise araya hafta sonu girdiği için Salı günü gerçekleşir. T+2 günü nakit ve menkul kıymet teslim borçlarının tamamlanması gereken yasal son temerrüt saati ise 15:00\'tir.",'

target2 = '"Takip Korelasyon Oranı (%95 Kuralı): BYF Tebliği uyarınca, fon portföyünün değeri ile takip ettiği baz endeks arasındaki korelasyon katsayısının EN AZ %95 (0,95) olması kanuni zorunluluktur."'
repl2 = '"Takip Korelasyon Oranı (%95 Kuralı): BYF Tebliği uyarınca, fon portföyünün değeri ile takip ettiği baz endeks arasındaki korelasyon katsayısının EN AZ %95 (0,95) olması kanuni zorunluluktur.",\n                    "Özel Fon Türleri ve Asgari Portföy Sınırları: Hisse Senedi Yoğun Fonlarda portföyün EN AZ %80\'inin devamlı olarak BIST hisselerinden oluşması zorunludur. Fon Sepeti Fonlarında fon değerinin EN AZ %80\'i diğer yatırım fonu paylarından oluşur. Para Piyasası Fonlarında ise portföyün ağırlıklı ortalama vadesi en fazla 45 gün olabilir."'

if target1 in text:
    text = text.replace(target1, repl1)
    print("Replaced target1 (15:00)")
else:
    print("target1 not found")

if target2 in text:
    text = text.replace(target2, repl2)
    print("Replaced target2 (%80)")
else:
    print("target2 not found")

with open('scripts/generate_master_topic_notes.py', 'w', encoding='utf-8') as f:
    f.write(text)

print("Saved updated generate_master_topic_notes.py")
