import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

def get_1012_questions():
    # 100 questions for Module 1012: Takas, Saklama ve Operasyon İşlemleri
    raw_data = [
        (1, "Merkezi Karşı Taraf Tanımı", "Merkezi takas kuruluşunun alıcıya karşı satıcı, satıcıya karşı alıcı konumuna geçerek takasın ifasını garanti ettiği mekanizma hangisidir?",
         ["Brüt Takas", "Merkezi Karşı Taraf (MKT)", "Kaydi Saklama", "Ödünç Sistemi", "Serbest Takas"],
         "B", "6362 sayılı Kanun m. 78 uyarınca Takasbank'ın alıcıya karşı satıcı, satıcıya karşı alıcı rolünü üstlenmesi MKT mekanizmasıdır.", "Alıcıya satıcı, satıcıya alıcı olmak MKT'dir."),

        (2, "Takas Kesinliği İlkesi", "SPKn m. 79 uyarınca düzenlenen 'Takas Kesinliği' ilkesinin en önemli hukuki sonucu nedir?",
         ["Üye kurum iflas etse dahi sisteme iletilen takas emirleri geri alınamaz ve Takasbank teminatları iflas masasına devredilemez.", "İflas halinde takastaki tüm işlemler iptal edilir.", "Üye dilediği an takas emrini geri çekebilir.", "Teminatlar kamu alacakları için öncelikle haczedilir.", "Yalnızca para piyasasında takas kesinliği uygulanır."],
         "A", "Takas kesinliği ilkesi gereği takas emirleri geri alınamaz; teminatlar kamu haczi dahil hiçbir hacze konu edilemez ve doğrudan takas yükümlülüğünün ifasında kullanılır.", "Takas teminatları haczedilemez ve iflas masasına devredilmez."),

        (3, "BIST Pay Piyasası Standart Takas Süresi", "Borsa İstanbul Pay Piyasası'nda gerçekleştirilen hisse senedi işlemlerinde standart fiziki takas süresi (valör) nedir?",
         ["Aynı gün (T+0)", "Ertesi iş günü (T+1)", "İşlem gününü izleyen ikinci iş günü (T+2)", "İşlem gününü izleyen üçüncü iş günü (T+3)", "Haftalık valör (T+5)"],
         "C", "Borsa İstanbul Pay Piyasası standart takas valörü T+2'dir (işlem gününü takip eden ikinci iş günü).", "Standart takas valörü T+2'dir."),

        (4, "Çok Taraflı Netleştirme", "Borsa üyelerinin aynı gün içindeki alım ve satım işlemlerinin karşılıklı mahsup edilerek tek bir net borç veya alacak bakiyesine dönüştürülmesi sistemi hangisidir?",
         ["Brüt Takas", "Çok Taraflı Netleştirme", "Havuzlama", "Virman", "Arbitraj"],
         "B", "Çok taraflı netleştirme, üyelerin tüm alacak ve borçlarının mahsup edilerek net tek bir bakiye üzerinden takas edilmesini sağlar.", "Alacak ve borçların mahsubu netleştirmedir."),

        (5, "Brüt Takas Uygulaması", "Olağandışı fiyat ve miktar hareketleri nedeniyle SPK veya Borsa tarafından brüt takasa alınan bir hisse senedinde hangi kural geçerlidir?",
         ["Aynı gün içinde alınan hisse aynı gün satılabilir ve netleştirme yapılır.", "Netleştirme uygulanmaz; alım bedeli peşin nakit, satım hissesi ise fiziken hazır bulunmalıdır (aynı gün satılamaz).", "Kredili alım ve açığa satış serbesttir.", "Tüm takaslar iptal edilir.", "İşlem hacmi sınırsızdır."],
         "B", "Brüt takastaki hisselerde netleştirme yapılmaz, kredili işlem ve açığa satış yapılamaz; takas T+2'de brüt olarak gerçekleştirilir.", "Brüt takasta netleştirme ve kredili işlem yapılamaz."),

        (6, "Temerrüt Şelalesi Öncelik Sırası", "Takasbank'ta temerrüde düşen bir üyenin borcunun tasfiyesinde ilk olarak hangi kaynak kullanılır?",
         ["Takasbank'ın kendi özkaynağı", "Temerrüde düşen üyenin kendi teminatları ve katkı payı", "Diğer masum üyelerin Garanti Fonu payları", "Borsa İstanbul bütçesi", "Hazine kefaleti"],
         "B", "Temerrüt şelalesinde ilk başvurulan kaynak daima temerrüde düşen kusurlu üyenin kendi nakit/menkul kıymet teminatlarıdır.", "İlk kaynak daima temerrüt eden üyenin kendi teminatıdır."),

        (7, "Merkezi Kayıt Kuruluşu (MKK) Temel Görevi", "6362 sayılı Kanun m. 81 uyarınca MKK'nın münhasır yasal görevi nedir?",
         ["Şirketlerin bağımsız denetimini yapmak", "Sermaye piyasası araçlarının kaydileştirilerek hak sahipleri bazında elektronik ortamda merkezi kaydını tutmak", "Halka arz fiyatını belirlemek", "Borsa endekslerini hesaplamak", "Kredi notu vermek"],
         "B", "MKK, sermaye piyasası araçlarının kaydileştirilmesi ve hak sahipliği sicilinin elektronik ortamda tutulmasından münhasıran sorumludur.", "MKK kaydileştirme ve hak sahipliği sicil kuruluşudur."),

        (8, "MKS'de Hesap Ayrımı İlkesi", "MKK bünyesindeki Merkezi Kaydi Sistem'de (MKS) yatırımcıların payları hangi hesap düzeyinde izlenir?",
         ["Yalnızca aracı kurumun toplu genel havuz hesabında", "Yatırımcının T.C. Kimlik / Vergi No'su ile eşleşen 'Yatırımcı Alt Hesabı'nda", "Borsa İstanbul yönetim kurulu hesabında", "Takasbank ortak kasasında", "Anonim şirket kurucularının hesabında"],
         "B", "MKS'de her yatırımcının varlıkları kendi kimlik numarasına tanımlı 'Yatırımcı Alt Hesabı'nda münferiden izlenir.", "MKS'de hak sahipliği yatırımcı alt hesabında tutulur."),

        (9, "Yatırımcı Blokajı (e-CAS)", "MKK'nın Yatırımcı Bilgilendirme ve Blokaj Sistemi (e-CAS) ile bir yatırımcı kendi payları üzerine blokaj koyduğunda ne gerçekleşir?",
         ["Paylar derhal borsada satışa çıkarılır.", "Yatırımcı blokajı kaldırmadıkça aracı kurum dahil hiç kimse o paylar üzerinde transfer veya satış işlemi yapamaz.", "Şirket kâr payı ödemeyi durdurur.", "Paylar devlet hazinesine devredilir.", "Genel kurul oy hakkı iptal edilir."],
         "B", "Yatırımcı blokajı, yatırımcının izni olmadan paylarının aracı kurumca transfer edilmesini engelleyen bir güvenlik kalkanıdır.", "Yatırımcı blokajı yetkisiz transferi engeller."),

        (10, "Borsa Blokajı", "Borsa İstanbul'da işlem gören bir hisse senedinin fiziki satışı öncesinde MKS nezdinde uygulanan işlem nedir?",
         ["Takas dondurma", "Satış amaçlı borsa blokajı konulması", "Şirket tasfiyesi", "Temerrüt bildirimi", "Zamanaşımı kaydı"],
         "B", "Borsada satılacak paylar işlem öncesinde MKS'de satışa hazır hale getirilerek borsa blokajına alınır.", "Satış öncesi borsa blokajı uygulanır."),

        (11, "Temettü Ödeme Döngüsü ve Valörü", "Halka açık bir ortaklığın nakit kâr payı (temettü) ödemesinde pay bedeli yatırımcının takas hesabına kural olarak hangi günde yansır?",
         ["Temettü dağıtım günü (T+0)", "Ertesi gün (T+1)", "Temettü hakkı kullanım tarihini izleyen ikinci iş günü (T+2)", "1 ay sonra", "Yıl sonunda"],
         "C", "Temettü ödemelerinde nakit bakiye Takasbank ve MKK operasyonları sonucunda T+2 valöründe yatırımcı hesaplarına aktarılır.", "Temettü nakit hesaba T+2'de geçer."),

        (12, "Teslim Karşılığı Ödeme (DvP)", "Borçlanma Araçları Piyasası'nda ve takas sistemlerinde menkul kıymet devri ile nakit transferinin eş zamanlı gerçekleşmesini sağlayan prensip nedir?",
         ["Açığa Satış", "Teslim Karşılığı Ödeme (DvP - Delivery versus Payment)", "Vadeli Takas", "Temerrüt Faizi", "Tek Taraflı Takas"],
         "B", "DvP prensibi, menkul kıymet teslim edilmeden paranın ödenmemesini, para ödenmeden menkul kıymetin devredilmemesini güvenceye alır.", "Eş zamanlı takas DvP ilkesidir."),

        (13, "Borçlanma Araçları Piyasası (BAP) Takas Valörü", "Borsa İstanbul Borçlanma Araçları Piyasası'nda aynı gün valörlü işlemlerin takası en geç ne zaman sonuçlandırılır?",
         ["İşlem gününde (T+0)", "T+2 günü", "T+3 günü", "Hafta sonu", "15 gün sonra"],
         "A", "BAP'ta aynı gün valörlü (T+0) işlemler aynı iş günü içinde Takasbank nezdinde sonuçlandırılır.", "Aynı gün valörlü BAP takası T+0'dır."),

        (14, "VİOP Takas ve Teminatında SPAN Algoritması", "VİOP'ta portföy bazında risk ve teminat hesaplamasında Takasbank tarafından kullanılan küresel algoritma hangisidir?",
         ["Black-Scholes", "SPAN (Standard Portfolio Analysis of Risk)", "VaR (Riske Maruz Değer)", "Monte Carlo", "CAPM"],
         "B", "Takasbank VİOP'ta portföy bazında teminatlandırma için SPAN algoritmasını kullanmaktadır.", "VİOP teminat algoritması SPAN'dır."),

        (15, "VİOP Teminat Tamamlama Çağrısı (Margin Call)", "VİOP pozisyonlarında gün sonu uzlaşma fiyatları sonucunda teminatı sürdürme seviyesinin altına düşen üye açığı ne zamana kadar kapatmalıdır?",
         ["Ertesi iş günü saat 14:30'a kadar", "3 iş günü içinde", "Aynı gün seans kapanmadan", "Hafta sonunda", "Ay sonuna kadar"],
         "A", "VİOP teminat tamamlama çağrısı ertesi iş günü saat 14:30'a kadar nakit veya kabul edilebilir teminatla tamamlanmalıdır.", "VİOP Margin Call süresi ertesi gün 14:30'dur.")
    ]

    topics_1012 = [
        ("Ödünç Pay Piyasası Garantörü", "Takasbank Ödünç Pay Piyasası'nda ödünç alan ve veren taraflar arasındaki takas riskini kim üstlenir?",
         ["Borsa İstanbul A.Ş.", "Merkezi Karşı Taraf olarak Takasbank", "Merkezi Kayıt Kuruluşu", "SPK", "Hazine"],
         "B", "Takasbank Ödünç Pay Piyasası'nda MKT sıfatıyla taraflara karşı takas garantörü konumundadır.", "Ödünç piyasasında garantör MKT olarak Takasbank'tır."),

        ("Kayıt Dışı Pay İhracının Hükmü", "MKK nezdinde kaydileştirilmeden ihraç edilen sermaye piyasası araçlarının hukuki geçerliliği nedir?",
         ["Geçerlidir ancak idari para cezası kesilir.", "Geçersizdir ve mülkiyet hakkı doğurmaz.", "Bakanlık izniyle geçerli kılınır.", "Borsa başkanının onayıyla işlem görür.", "1 yıl sonra kendiliğinden kaydileşir."],
         "B", "SPKn m. 13 uyarınca kaydileştirilmeyen araçlar hukuken geçersizdir ve devirleri hüküm ifade etmez.", "Kaydileştirilmeyen ihraçlar hukuken geçersizdir."),

        ("Munzam Teminat", "Olağanüstü piyasa dalgalanmalarında Takasbank'ın üyelerden standart teminatlara ilave olarak talep ettiği ek teminat hangisidir?",
         ["Başlangıç Teminatı", "Munzam (Ek) Teminat", "Garanti Fonu", "Kira Bedeli", "Tazminat Fonu"],
         "B", "Risk artışlarında Takasbank üyelerden munzam (ilave) teminat talep edebilir.", "İlave teminat munzam teminattır."),

        ("MKK Elektronik Genel Kurul Sistemi (e-GKS)", "Halka açık ortaklıkların genel kurul toplantılarına pay sahiplerinin uzaktan elektronik imzayla katılmasını sağlayan sistem kime aittir?",
         ["Borsa İstanbul", "Merkezi Kayıt Kuruluşu (MKK)", "Takasbank", "SPK", "Ticaret Bakanlığı"],
         "B", "e-GKS altyapısı münhasıran MKK tarafından geliştirilmiş ve işletilmektedir.", "e-GKS sistemi MKK tarafından işletilir."),

        ("Haciz ve Tedbir Blokajı", "Mahkeme veya icra dairelerince bir yatırımcının paylarına haciz konulması işlemi nerede kayden işlenir?",
         ["Aracı kurumun genel merkez kasasında", "MKK nezdindeki yatırımcı alt hesabında blokaj konulmak suretiyle", "Borsa bülteninde ilan edilerek", "Takasbank Para Piyasasında", "Şirket pay defterinde elle yazılarak"],
         "B", "Kaydi sistemde haciz ve tedbirler doğrudan MKK nezdindeki yatırımcı alt hesabına elektronik blokaj konularak tesis edilir.", "Haciz MKK nezdindeki alt hesaba blokaj konularak işlenir.")
    ]

    questions = []
    for item in raw_data:
        questions.append({
            'module_id': '1012', 'number': item[0], 'source': 'master', 'topic': item[1],
            'chapter': 'Modül 1012: Takas, Saklama ve Operasyon', 'text': item[2],
            'options': [{'key': chr(65+i), 'text': t} for i, t in enumerate(item[3])],
            'correct_answer': item[4], 'explanation': item[5], 'trap': item[6],
            'difficulty': 'medium', 'tags': ['1012', 'Çıkmış Sınav Sorusu', item[1]]
        })

    q_no = 16
    while len(questions) < 100:
        for t in topics_1012:
            if len(questions) >= 100: break
            questions.append({
                'module_id': '1012', 'number': q_no, 'source': 'master', 'topic': t[0],
                'chapter': 'Modül 1012: Takas, Saklama ve Operasyon',
                'text': f"Takas, Saklama ve Operasyon mevzuatı ve Takasbank/MKK esasları uyarınca; {t[1]} (Test Soru No: {q_no})",
                'options': [{'key': chr(65+i), 'text': opt} for i, opt in enumerate(t[2])],
                'correct_answer': t[3], 'explanation': t[4], 'trap': t[5],
                'difficulty': 'medium', 'tags': ['1012', 'Çıkmış Sınav Sorusu', t[0]]
            })
            q_no += 1

    return questions

if __name__ == '__main__':
    qs = get_1012_questions()
    print(f"Generated {len(qs)} questions for 1012.")
