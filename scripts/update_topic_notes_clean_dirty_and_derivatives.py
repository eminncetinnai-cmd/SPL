import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('scripts/generate_master_topic_notes.py', 'r', encoding='utf-8') as f:
    code = f.read()

# 1. Update sec_1003_02 to include Clean vs Dirty Price
old_sec_02_content = '''                    "Tasfiyede Öncelik: Şirket iflas ettiğinde veya tasfiyeye girdiğinde tahvil sahipleri alacaklı sıfatıyla pay sahiplerinden (hisse senedi sahiplerinden) çok daha önce tasfiye masasından alacaklarını tahsil ederler."
                ],'''

new_sec_02_content = '''                    "Tasfiyede Öncelik: Şirket iflas ettiğinde veya tasfiyeye girdiğinde tahvil sahipleri alacaklı sıfatıyla pay sahiplerinden (hisse senedi sahiplerinden) çok daha önce tasfiye masasından alacaklarını tahsil ederler.",
                    "Temiz Fiyat (Clean Price) vs Kirli Fiyat (Dirty Price) ve İşlemiş Faiz:\\n• Temiz Fiyat (Clean Price): Tahvilin son kupon ödeme tarihinden bugüne kadar birikmiş/işlemiş faizi HARİÇ piyasa fiyatıdır. Borsa İstanbul Borçlanma Araçları Piyasası ekranlarında kote edilen ve işlem gören fiyat daima TEMİZ FİYATTIR. Temiz fiyat kullanılmasının sebebi, kupon gününe yaklaştıkça faizin yapay olarak fiyatı şişirmesini önlemek ve sadece piyasa faiz oranlarındaki saf getiri dalgalanmalarını izlemektir.\\n• İşlemiş Faiz (Accrued Interest): Son kupon ödeme tarihinden takas (satış) gününe kadar geçen gün sayısı için tahvilin hak ettiği faizdir. Formül: İşlemiş Faiz = Nominal Değer × Yıllık Kupon Oranı × (Geçen Gün Sayısı / 365).\\n• Kirli Fiyat (Dirty Price): Temiz Fiyata İşlemiş Faizin eklenmesiyle oluşan toplam bedeldir. Formül: Kirli Fiyat = Temiz Fiyat + İşlemiş Faiz.\\n• En Kritik Sınav Kuralı: Borsa ekranında Temiz Fiyat kote edilirken; alıcı takas gününde satıcıya cebinden çıkarıp FİİLEN KİRLİ FİYATI öder. Kupon ödeme gününde (veya hemen ertesi günü) işlemiş faiz sıfırlandığı için Temiz Fiyat = Kirli Fiyat olur."
                ],'''

if old_sec_02_content in code:
    code = code.replace(old_sec_02_content, new_sec_02_content)
    print("Injected Clean/Dirty price content into sec_1003_02")
else:
    print("old_sec_02_content not found")

# Add example to sec_1003_02
old_sec_02_example = '''                "concrete_examples": [
                    "Piyasa Örneği: 1.000 TL nominal değerli, 2 yıl vadeli ve 6 ayda bir %20 kupon ödemeli bir şirket tahvili alan yatırımcı; şirket zarar etse dahi her 6 ayda bir 200 TL faiz alır, vade sonunda ise 1.000 TL anaparasını eksiksiz geri alır."
                ],'''

new_sec_02_example = '''                "concrete_examples": [
                    "Piyasa Örneği (Kuponlu Tahvil): 1.000 TL nominal değerli, 2 yıl vadeli ve 6 ayda bir %20 kupon ödemeli bir şirket tahvili alan yatırımcı; şirket zarar etse dahi her 6 ayda bir 200 TL faiz alır, vade sonunda ise 1.000 TL anaparasını eksiksiz geri alır.",
                    "Piyasa Örneği (Temiz vs Kirli Fiyat Hesabı): 1.000 TL nominal değerli, yıllık %20 kupon ödemeli bir tahvilin son kupon ödemesinden 182 gün geçmiştir. Tahvilin borsadaki temiz fiyatı 950 TL'dir. İşlemiş Faiz: 1.000 × %20 × (182 / 365) = 99,7 TL (yaklaşık 100 TL) bulunur. Alıcının takas gününde satıcıya fiilen ödeyeceği Kirli Fiyat: 950 TL (Temiz) + 100 TL (Faiz) = 1.050 TL'dir."
                ],'''

if old_sec_02_example in code:
    code = code.replace(old_sec_02_example, new_sec_02_example)
    print("Injected Clean/Dirty example into sec_1003_02")
else:
    print("old_sec_02_example not found")

# Add table to sec_1003_02
old_sec_02_table = '''                        "rows": [
                            ["Tahvil (Özel Sektör / Devlet)", "1 Yıl (365 Gün)", "Sınırsız (5-10-30 yıl)", "Sabit veya Değişken Kuponlu Faiz"],
                            ["Finansman Bonosu", "30 Gün", "364 Gün", "İskontolu Getiri"],
                            ["Hazine Bonosu", "1 Aydan Az Olmamak Üzere", "1 Yıldan Az", "İskontolu Getiri"]
                        ]'''

new_sec_02_table = '''                        "rows": [
                            ["Tahvil (Özel Sektör / Devlet)", "1 Yıl (365 Gün)", "Sınırsız (5-10-30 yıl)", "Sabit veya Değişken Kuponlu Faiz"],
                            ["Finansman Bonosu", "30 Gün", "364 Gün", "İskontolu Getiri"],
                            ["Hazine Bonosu", "1 Aydan Az Olmamak Üzere", "1 Yıldan Az", "İskontolu Getiri"],
                            ["Temiz Fiyat (Clean Price)", "Borsa ekranında kote edilen fiyat", "Kupon faizi hariç fiyat", "Kirli Fiyat - İşlemiş Faiz"],
                            ["Kirli Fiyat (Dirty Price)", "Takasta fiilen ödenen nakit bedel", "Kupon faizi dahil toplam tutar", "Temiz Fiyat + İşlemiş Faiz"]
                        ]'''

if old_sec_02_table in code:
    code = code.replace(old_sec_02_table, new_sec_02_table)
    print("Injected Clean/Dirty table rows into sec_1003_02")
else:
    print("old_sec_02_table not found")

# 2. Update sec_1003_06 (Derivatives, Futures, Options, Warrants)
old_sec_06_content = '''                "content": [
                    "Türev Araçlar; değeri dayanak bir varlığın (hisse senedi, endeks, döviz, emtia, faiz) fiyatına bağlı olan finansal sözleşmelerdir. Borsa İstanbul bünyesinde Vadeli İşlem ve Opsiyon Piyasası'nda (VİOP) işlem görürler.",
                    "Vadeli İşlem Sözleşmesi (Futures): Alıcı ve satıcıya gelecekteki belirli bir tarihte, önceden anlaşılan fiyattan belirli miktarda varlığı alma veya satma YÜKÜMLÜLÜĞÜ getirir.",
                    "Opsiyon Sözleşmesi (Options): Alıcıya belirli bir fiyattan dayanak varlığı alma hakkı (Call Option) veya satma hakkı (Put Option) verir. Alıcı için HAK, satıcı için YÜKÜMLÜLÜKTÜR.",
                    "Teminat Tamamlama Çağrısı (Margin Call): VİOP'ta pozisyon açılırken 'Başlangıç Teminatı' yatırılır. Fiyatlar ters gittiğinde hesap bakiyesi 'Sürdürme Teminatı' seviyesinin altına düşerse, Takasbank aracı kuruma ve yatırımcıya teminatı başlangıç seviyesine tamamlaması için Teminat Tamamlama Çağrısı yapar.",
                    "Varantlar (Warrants): Menkul kıymet niteliğindeki opsiyonlardır. Alıcı sadece ödediği prim kadar risk taşır, margin call bulunmaz ve kaldıraçlı getiri sunar."
                ],'''

new_sec_06_content = '''                "content": [
                    "Türev Araçlar; değeri dayanak bir varlığın (hisse senedi, endeks, döviz, emtia, faiz) fiyatına bağlı olan finansal sözleşmelerdir. Borsa İstanbul bünyesinde Vadeli İşlem ve Opsiyon Piyasası'nda (VİOP) işlem görürler.",
                    "1. Vadeli İşlem Sözleşmesi (Futures - İki Taraflı Zorunlu Sözleşme):\\n• Alıcı ve satıcıya gelecekteki belirli bir tarihte, önceden sabitlenen fiyattan belirli miktarda varlığı alma veya satma YÜKÜMLÜLÜĞÜ getirir.\\n• Benzetme: Çiftçi ile fırıncının 3 ay sonra 1 ton buğdayı kilosu 10 TL'den alıp satmak üzere bağlayıcı sözleşme imzalaması gibidir. 3 ay sonra buğday piyasada 20 TL de olsa 5 TL de olsa İKİ TARAF DA İŞLEMİ 10 TL'DEN YAPMAK ZORUNDADIR. Cayma veya vazgeçme hakkı yoktur.\\n• Teminat & Risk: Her iki taraf da Takasbank'a başlangıç teminatı yatırır. Fiyat ters giderse zarar teorik olarak sınırsızdır ve günlük teminat tamamlama çağrısı (Margin Call) uygulanır.",
                    "2. Opsiyon Sözleşmesi (Options - Ev Kaporası & Sigorta Mantığı):\\n• Alıcıya belirli bir vadede veya vadeye kadar, önceden belirlenen kullanım fiyatından dayanak varlığı ALMA HAKKI (Call Option) veya SATMA HAKKI (Put Option) veren sözleşmelerdir.\\n• Benzetme (Alım Opsiyonu / Call): Beğendiğiniz 5 Milyon TL'lik bir ev için ev sahibine 100.000 TL kapora (prim) verip '1 ay boyunca bu evi 5 Milyona alma hakkı' satın aldınız. 1 ay sonra evin fiyatı 7 Milyona çıkarsa hakkınızı kullanır evi 5 Milyona alırsınız. Ancak evin fiyatı 3 Milyona düşerse evi almaktan VAZGEÇERSİNİZ; tek kaybınız baştaki 100.000 TL kapora (prim) olur.\\n• ALICI İÇİN HAKTIR: Alıcı sadece prim öder. Hak sahibidir; piyasa aleyhine giderse hakkını kullanmaktan vazgeçebilir. Riski kesin olarak ödediği primle sınırlıdır; teminat yatırmaz ve Margin Call uygulanmaz.\\n• SATICI (YAZICI) İÇİN YÜKÜMLÜLÜKTÜR: Primi peşin tahsil eder ancak alıcı hakkını kullanmak isterse sözleşme şartlarını eksiksiz yerine getirmek ZORUNDADIR. Kazancı aldığı primle sınırlı, zararı teorik olarak sınırsızdır; bu yüzden teminat yatırır ve Margin Call uygulanır.",
                    "3. Varantlar (Warrants - Menkul Kıymetleştirilmiş Banka Opsiyonu):\\n• Sahibine belirli bir vadede veya tarihe kadar, önceden belirlenen fiyattan dayanak varlığı alma veya satma hakkı veren 'menkul kıymet niteliğindeki' opsiyonlardır.\\n• VİOP opsiyonlarından farkı: Varantlar Borsa İstanbul Pay Piyasası'nda tıpkı bir hisse senedi gibi işlem görür. İhraççısı daima yetkili bir banka veya aracı kurumdur (yatırımcı satıcı/yazıcı olamaz, sadece alıcı olabilir).\\n• Varant alan yatırımcı sadece primi öder; teminat yatırmaz, margin call (teminat tamamlama) riski yoktur ve maksimum kaybı ödediği prim tutarı kadardır.",
                    "4. Teminat Tamamlama Çağrısı (Margin Call Mekanizması):\\n• Vadeli işlemlerde pozisyon açılırken 'Başlangıç Teminatı' yatırılır. Fiyatlar ters gittiğinde hesap bakiyesi 'Sürdürme Teminatı' seviyesinin altına düşerse, Takasbank aracı kuruma ve yatırımcıya teminatı tekrar BAŞLANGIÇ SEVİYESİNE tamamlaması için Teminat Tamamlama Çağrısı (Margin Call) yapar."
                ],'''

if old_sec_06_content in code:
    code = code.replace(old_sec_06_content, new_sec_06_content)
    print("Injected deep Futures/Options/Warrants explanations into sec_1003_06")
else:
    print("old_sec_06_content not found")

with open('scripts/generate_master_topic_notes.py', 'w', encoding='utf-8') as f:
    f.write(code)

print("Finished updating generate_master_topic_notes.py")
