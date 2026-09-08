import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('scripts/generate_master_topic_notes.py', 'r', encoding='utf-8') as f:
    code = f.read()

# 1. Enrich sec_1003_02 key_takeaways, exam_traps, exam_tips
target_sec_02 = '''                "key_takeaways": [
                    "Tahvil asgari vadesi: Kesin olarak en az 1 yıl (365 gün).",
                    "Finansman bonosu vadesi: 30 gün ile 364 gün arası.",
                    "Tahvil sahibi şirketin ortağı değil, öncelikli alacaklısıdır."
                ],
                "exam_traps": [
                    "⚠️ DİKKAT: 'Tahvil sahipleri genel kurulda oy kullanabilir' ifadesi kesinlikle YANLIŞTIR. Alacaklıların oy hakkı yoktur."
                ],'''

repl_sec_02 = '''                "key_takeaways": [
                    "Tahvil asgari vadesi: Kesin olarak en az 1 yıl (365 gün).",
                    "Finansman bonosu vadesi: 30 gün ile 364 gün arası.",
                    "Tahvil sahibi şirketin ortağı değil, öncelikli alacaklısıdır.",
                    "Temiz Fiyat (Clean Price): Borsa ekranında kote edilen, kupon işlemiş faizi HARİÇ piyasa fiyatıdır.",
                    "Kirli Fiyat (Dirty Price): Takas gününde alıcının satıcıya cebinden çıkarıp FİİLEN ÖDEDİĞİ tutardır (Kirli = Temiz + İşlemiş Faiz).",
                    "Kupon ödeme gününde (veya hemen ertesi gün) işlemiş faiz sıfırlandığı için Temiz Fiyat = Kirli Fiyat olur."
                ],
                "exam_traps": [
                    "⚠️ DİKKAT: 'Tahvil sahipleri genel kurulda oy kullanabilir' ifadesi kesinlikle YANLIŞTIR. Alacaklıların oy hakkı yoktur.",
                    "⚠️ DİKKAT: 'Alıcı takasta borsa ekranında kote edilen temiz fiyatı öder' öncülü sınavın klasik tuzağıdır; alıcı satıcıya işlemiş faizi de içeren KİRLİ FİYATI öder.",
                    "⚠️ DİKKAT: Kupon ödemesi yapıldığı gün İşlemiş Faiz = 0 olduğu için Temiz Fiyat ile Kirli Fiyat birbirine EŞİTTİR; kupon vadesine yaklaştıkça makas açılır."
                ],
                "exam_tips": [
                    "Tahvil hesaplama sorularında 'yatırımcının cebinden çıkan fiili nakit tutar' sorulduğunda Temiz Fiyata İşlemiş Faizi ekleyerek KİRLİ FİYATI hesaplayın.",
                    "İşlemiş Faiz = Nominal Değer × Yıllık Kupon Oranı × (Geçen Gün / 365) formülünü sınavda doğrudan uygulayın."
                ],'''

if target_sec_02 in code:
    code = code.replace(target_sec_02, repl_sec_02)
    print("Enriched sec_1003_02 takeaways, traps, tips")
else:
    print("target_sec_02 not found")

# 2. Enrich sec_1003_06 key_takeaways, exam_traps, exam_tips
target_sec_06 = '''                "key_takeaways": [
                    "Futures sözleşmelerinde her iki taraf yükümlüdür; opsiyonlarda alıcı hak sahibi, satıcı yükümlüdür.",
                    "Teminat Tamamlama Çağrısı (Margin Call) hesap bakiyesi Sürdürme Teminatının altına indiğinde tetiklenir.",
                    "Varantlarda zarar ödenen primle sınırlıdır; teminat tamamlama çağrısı yoktur."
                ],
                "exam_traps": [
                    "⚠️ DİKKAT: Margin call geldiğinde bakiye 'sürdürme teminatı'na kadar değil, 'BAŞLANGIÇ TEMİNATI' seviyesine kadar tamamlanmak zorundadır."
                ],'''

repl_sec_06 = '''                "key_takeaways": [
                    "Futures (Vadeli İşlem): Her iki taraf için de ileri tarihte sabit fiyattan işlem yapma ZORUNLULUĞUDUR; iki taraf da yükümlüdür, iki taraf da teminat yatırır, vazgeçilemez.",
                    "Opsiyon Alıcısı (Long): Hak sahibidir, prim öder, azami riski ödediği primle sınırlıdır, teminat yatırmaz ve piyasa ters giderse vazgeçebilir.",
                    "Opsiyon Satıcısı (Short / Yazıcı): Yükümlüdür, primi peşin alır, riski sınırsızdır ve sözleşme yükümlülüğünü garanti etmek için teminat yatırır.",
                    "Varant (Warrant): Menkul kıymetleştirilmiş banka opsiyonudur; BIST Pay Piyasasında işlem görür, sadece prim ödenir, margin call yoktur.",
                    "Margin Call: Hesap bakiyesi Sürdürme Teminatı seviyesinin altına indiğinde bakiye tekrar BAŞLANGIÇ TEMİNATI seviyesine tamamlanır."
                ],
                "exam_traps": [
                    "⚠️ DİKKAT: 'Opsiyon alıcısı için margin call gelir veya teminat yatırmalıdır' öncülü YANLIŞTIR. Opsiyon alıcısı sadece peşin prim öder; teminatı satıcı (yazıcı) yatırır.",
                    "⚠️ DİKKAT: 'Futures sözleşmesinde yatırımcı kâr etmezse işlemden vazgeçebilir' öncülü YANLIŞTIR. Futures'ta vazgeçme hakkı yoktur; her iki taraf da zorunlu yükümlüdür.",
                    "⚠️ DİKKAT: Margin call geldiğinde bakiye 'sürdürme teminatı'na kadar değil, 'BAŞLANGIÇ TEMİNATI' seviyesine kadar tamamlanmak zorundadır."
                ],
                "exam_tips": [
                    "Öncüllü sorularda; sözleşmeden cayma/vazgeçme hakkı veriliyorsa OPSİYON, iki tarafa da zorunlu bağlayıcılık getiriyorsa FUTURES, hisse senedi pazarında alınıp satılan ve sadece prim ödenen araç soruluyorsa VARANT işaretlenmelidir."
                ],'''

if target_sec_06 in code:
    code = code.replace(target_sec_06, repl_sec_06)
    print("Enriched sec_1003_06 takeaways, traps, tips")
else:
    print("target_sec_06 not found")

with open('scripts/generate_master_topic_notes.py', 'w', encoding='utf-8') as f:
    f.write(code)

print("Updated generate_master_topic_notes.py successfully")
