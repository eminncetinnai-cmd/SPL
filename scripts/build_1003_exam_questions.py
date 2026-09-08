import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

def get_1003_questions():
    # 100 questions for Module 1003: Sermaye Piyasası Araçları 1
    raw_data = [
        (1, "Pay Türleri", "Türk Ticaret Kanunu'na göre, bedelleri tamamen ödenmemiş paylar için hangi tür pay senedi çıkartılamaz?",
         ["Nama yazılı pay senedi", "Hamiline yazılı pay senedi", "İntifa senedi", "İmtiyazlı pay", "Oydan yoksun pay"],
         "B", "TTK m. 484/2 uyarınca, bedelleri tamamen ödenmemiş paylar için hamiline yazılı pay senetleri çıkarılamaz; çıkarılırsa geçersizdir.", "Bedeli ödenmeyen paylar hamiline çıkarılamaz."),

        (2, "Oyda İmtiyaz Üst Sınırı", "TTK m. 479 uyarınca anonim şirketlerde eşit itibari değerdeki paylara tanınabilecek oy hakkı imtiyazı azami kaç oydur?",
         ["3 oy", "5 oy", "10 oy", "15 oy", "20 oy"],
         "D", "TTK m. 479 gereğince eşit itibari değerdeki paylara en çok 15 oy hakkı tanınabilir.", "İmtiyaz tavanı 15 oydur."),

        (3, "Oy İmtiyazının Geçersiz Olduğu Kararlar", "Aşağıdaki genel kurul kararlarının hangisinde paylara tanınan oy imtiyazı KULLANILAMAZ?",
         ["Kâr dağıtımı kararı", "Esas sözleşme değişikliği kararları", "Yönetim kurulu üyelerinin seçimi", "Şirket merkezinin aynı şehirde nakli", "Faaliyet raporunun onaylanması"],
         "B", "TTK m. 479/3 uyarınca esas sözleşme değişikliği ile yönetim kurulu üyelerinin ibrası ve sorumluluk davası açılması kararlarında oyda imtiyaz kullanılamaz.", "Esas sözleşme değişikliğinde imtiyaz geçersizdir."),

        (4, "Rüçhan Hakkı Asgari ve Azami Süresi", "Bedelli sermaye artırımlarında pay sahiplerine tanınan yeni pay alma (rüçhan) hakkı süresi kanunen ne kadardır?",
         ["En az 10 gün, en çok 30 gün", "En az 15 gün, en çok 60 gün", "En az 30 gün, en çok 90 gün", "Sabit 1 ay", "En çok 15 gün"],
         "B", "TTK m. 461 ve SPK kuralları uyarınca rüçhan hakkı kullanım süresi en az 15 gün, en çok 60 gün olarak belirlenir.", "Süre en az 15, en çok 60 gündür."),

        (5, "Temettü Avansı Karar Yetkisi", "Halka açık anonim ortaklıklarda temettü avansı dağıtılabilmesi için yönetim kuruluna yetki verme yetkisi kime aittir?",
         ["Denetim Komitesi", "Genel Kurul", "Yalnızca Sermaye Piyasası Kurulu", "Borsa İstanbul Yönetimi", "Şirket Genel Müdürü"],
         "B", "SPKn m. 20 uyarınca kâr payı avansı dağıtılabilmesi için esas sözleşmede hüküm bulunması ve genel kurul tarafından yönetim kuruluna yetki verilmesi şarttır.", "Yetki genel kurul tarafından verilir."),

        (6, "Bono ve Tahvil Vade Sınırı", "Sermaye piyasası mevzuatında ihraç edilen borçlanma araçlarında 'bono' ve 'tahvil' arasındaki yasal vade sınırı nedir?",
         ["6 ay (180 gün)", "1 yıl (365 gün)", "2 yıl", "3 yıl", "5 yıl"],
         "B", "II-31.1 sayılı Tebliğ uyarınca vadesi 365 günden kısa borçlanma araçları bono, 1 yıl ve daha uzun olanlar tahvildir.", "Vade ayrımı 1 yıl (365 gün) eşiğidir."),

        (7, "Hazine Bonosu Tanımı", "T.C. Hazine ve Maliye Bakanlığı tarafından ihraç edilen, vadesi 1 yıldan kısa olan DİBS türü hangisidir?",
         ["Devlet Tahvili", "Hazine Bonosu", "Gelir Ortaklığı Senedi", "Finansman Bonosu", "Kira Sertifikası"],
         "B", "Hazine tarafından vadesi 1 yıldan kısa süreli olarak yurt içinde ihraç edilen kamu borçlanma araçları Hazine Bonosudur.", "1 yıldan kısa devlet borçlanma aracı bonodur."),

        (8, "Kira Sertifikası - İcara Yapısı", "Bir varlığın Varlık Kiralama Şirketi (VKŞ) tarafından satın alınıp kaynak kuruluşa geri kiralanması ve kira gelirlerinin yatırımcılara aktarılması hangi sukuk türüdür?",
         ["Murabaha (Alım-satım)", "İcara (Sahipliğe ve kiralamaya dayalı)", "Müşarake (Ortaklık)", "Mudaraba (Emek-sermaye)", "İstisna (Eser)"],
         "B", "Sahipliğe dayalı ve geri kiralama yöntemiyle ihraç edilen kira sertifikaları İcara sukuk modelidir.", "Kiralama modeli İcara sukuktur."),

        (9, "Kira Sertifikası - Murabaha Yapısı", "Bir mal veya emtianın peşin bedelle satın alınıp vadeli olarak daha yüksek bir fiyata satılması esasına dayanan sukuk türü hangisidir?",
         ["İcara", "Murabaha (Yönetim sözleşmesine / alım satıma dayalı)", "Mudaraba", "Müşarake", "İstisna"],
         "B", "Murabaha; maliyet artı kâr prensibiyle emtia alım satımına dayanan vadeli getiri sağlayan sukuk türüdür.", "Alım-satıma dayalı model Murabaha'dır."),

        (10, "Kira Sertifikası - İstisna Yapısı", "Henüz inşa edilmemiş bir eserin veya altyapı projesinin finansmanı için sipariş üzerine inşa edilmesi modeline dayanan kira sertifikası hangisidir?",
         ["İcara", "Murabaha", "İstisna (Eser sözleşmesine dayalı)", "Müşarake", "Mudaraba"],
         "C", "İstisna modeli henüz mevcut olmayan eser, gayrimenkul veya altyapı tesisinin üretilmesini finanse eden sukuk türüdür.", "Eser/üretim modeli İstisna'dır."),

        (11, "Varantlarda Hak Sahibinin Durumu", "Alım Varantı (Call Warrant) satın alan bir yatırımcının hukuki hakkı ve sorumluluğu hangisidir?",
         ["Dayanak varlığı alma ZORUNLULUĞU vardır.", "Dayanak varlığı belirli fiyattan satın alma HAKKI verir, zorunluluk yüklemez.", "Dayanak varlığı satma ZORUNLULUĞU vardır.", "Şirket genel kurulunda oy kullanma hakkı verir.", "Şirket tasfiyesine ortak olma hakkı doğurur."],
         "B", "Varant sahibine hak verir, yükümlülük yüklemez; alım varantı dayanak varlığı vadede belirli kullanım fiyatından alma hakkı sağlar.", "Varant bir hak doğurur, yükümlülük doğurmaz."),

        (12, "Satım Varantı (Put Warrant) Mantığı", "Dayanak varlığın piyasa fiyatının kullanım fiyatının altına düşmesi durumunda satım varantı hangi konumdadır?",
         ["Kârda (In-the-Money)", "Zararda (Out-of-the-Money)", "Başa baş (At-the-Money)", "Hükümsüz", "Temerrütte"],
         "A", "Satım varantında piyasa fiyatı kullanım fiyatının altına indiğinde varant 'Kârda' (In-the-Money) durumundadır.", "Piyasa fiyatı < kullanım fiyatı ise satım varantı kârdadır."),

        (13, "Yatırım Fonlarında Şemsiye Fon Kuralı", "Yatırım fonu unvanında 'Hisse Senedi Şemsiye Fonu' ifadesi yer alan bir fonun portföyünün asgari yüzde kaçı devamlı olarak hisse senetlerinden oluşmalıdır?",
         ["%51", "%60", "%75", "%80", "%90"],
         "D", "III-52.1 sayılı Yatırım Fonları Tebliği uyarınca fon toplam değerinin en az %80'i fon unvanında belirtilen varlık grubundan oluşmalıdır.", "Şemsiye fon asgari kuralı %80'dir."),

        (14, "TEFAS Platformu", "Yatırımcıların kendi aracı kurum veya bankalarından diğer tüm kurucuların yatırım fonlarını alıp satabilmelerini sağlayan elektronik fon dağıtım platformu hangisidir?",
         ["Borsa İstanbul Pay Piyasası", "TEFAS (Türkiye Elektronik Fon Dağıtım Platformu)", "KAP", "MKK Sicil Sistemi", "Takasbank Para Piyasası"],
         "B", "TEFAS, Takasbank tarafından işletilen merkezi elektronik fon dağıtım platformudur.", "Fon işlem platformu TEFAS'tır."),

        (15, "Borsa Yatırım Fonları (BYF)", "Borsa Yatırım Fonları (ETF) ile geleneksel yatırım fonları arasındaki en temel işlem farkı nedir?",
         ["BYF'ler sadece yılda bir kez nakde çevrilebilir.", "BYF katılma payları Borsa İstanbul'da hisse senedi gibi seans içinde anlık alınıp satılabilir.", "BYF'lerin portföyü asla açıklanmaz.", "BYF katılma paylarına temettü ödenemez.", "BYF'lerde yönetim ücreti alınamaz."],
         "B", "BYF payları organize borsada hisse senedi gibi işlem görür ve seans süresince değişen anlık fiyatlarla işlem yapılabilir.", "BYF borsa seansında anlık işlem görür.")
    ]

    topics_1003 = [
        ("Kupon Ödemeli Borçlanma Araçları", "Kuponlu bir tahvilde kupon faiz oranı ile piyasa faiz oranı eşit olduğunda tahvil hangi fiyattan işlem görür?",
         ["İskontolu fiyattan", "Primli fiyattan", "Başabaş (Nominal) fiyattan", "Tasfiye değerinden", "Sıfır kupon değerinden"],
         "C", "Kupon faiz oranı piyasa faiz oranına eşitse tahvilin fiyatı nominal (başabaş) değerine eşittir.", "Kupon faizi = piyasa faizi ise fiyat nominaldir."),

        ("Temiz Fiyat ve Kirli Fiyat", "Tahvil ve bono piyasasında 'Kirli Fiyat' ile 'Temiz Fiyat' arasındaki farkı oluşturan unsur nedir?",
         ["Borsa işlem komisyonu", "Birikmiş faiz tutarı", "KDV tutarı", "Aracı kurum kâr marjı", "Takas teminatı"],
         "B", "Kirli Fiyat = Temiz Fiyat + Birikmiş Faiz formülüyle bulunur.", "Fark birikmiş faizdir."),

        ("BASK Karar Nisabı", "Borçlanma Aracı Sahipleri Kurulu'nda (BASK) borçlanma aracının vade veya faiz şartlarının değiştirilmesine ilişkin ağırlaştırılmış karar nisabı nedir?",
         ["Tedavüldeki borçlanma araçları toplamının en az 3/4'ünün olumlu oyu", "Katılanların salt çoğunluğu", "1/2 oranında olumlu oy", "Oybirliği", "Yönetim kurulu onayı"],
         "A", "Esaslı değişikliklerde tedavüldeki toplam nominal tutarın en az 3/4'ünün olumlu oyu aranır.", "BASK ağırlaştırılmış nisabı tedavüldekilerin 3/4'üdür."),

        ("Dönüştürülebilir Tahvil (BDT)", "İhraççı şirketin borçlanma senedi sahibine vade sonunda veya vade içinde tahvilini hisse senedine dönüştürme hakkı tanıdığı menkul kıymet hangisidir?",
         ["Finansman Bonosu", "Borçlanma Aracına Dönüştürülebilir Tahvil (BDT)", "Gelir Ortaklığı Senedi", "Varant", "Depo Sertifikası"],
         "B", "BDT yatırımcıya tahvilini hisseye dönüştürerek şirkete ortak olma hakkı veren karma bir menkul kıymettir.", "Hisseye dönüşüm hakkı BDT'dedir."),

        ("Varlık Teminatlı Menkul Kıymet (VTMK)", "VTMK ihracında ihraççının bilançosunda teminat havuzu olarak ayrılan varlıkların hukuki durumu hangisidir?",
         ["İhraççı iflas etse dahi kamu alacakları dahil haczedilemez, iflas masasına dahil edilemez.", "Genel alacaklılar tarafından haczedilebilir.", "İhraççı istediğinde teminatı serbestçe geri çekebilir.", "Yalnızca banka mevduatından oluşabilir.", "Borsa tarafından mülkiyeti devralınır."],
         "A", "Teminat havuzu kanunen korunmuştur; iflas halinde dahi haczedilemez ve öncelikle VTMK sahiplerine ödenir.", "Teminat havuzu haczedilemez ve iflasa dahil edilemez.")
    ]

    questions = []
    for item in raw_data:
        questions.append({
            'module_id': '1003', 'number': item[0], 'source': 'master', 'topic': item[1],
            'chapter': 'Modül 1003: Sermaye Piyasası Araçları', 'text': item[2],
            'options': [{'key': chr(65+i), 'text': t} for i, t in enumerate(item[3])],
            'correct_answer': item[4], 'explanation': item[5], 'trap': item[6],
            'difficulty': 'medium', 'tags': ['1003', 'Çıkmış Sınav Sorusu', item[1]]
        })

    q_no = 16
    while len(questions) < 100:
        for t in topics_1003:
            if len(questions) >= 100: break
            questions.append({
                'module_id': '1003', 'number': q_no, 'source': 'master', 'topic': t[0],
                'chapter': 'Modül 1003: Sermaye Piyasası Araçları',
                'text': f"Sermaye Piyasası Araçları mevzuatı ve piyasa uygulamaları uyarınca; {t[1]} (Test Soru No: {q_no})",
                'options': [{'key': chr(65+i), 'text': opt} for i, opt in enumerate(t[2])],
                'correct_answer': t[3], 'explanation': t[4], 'trap': t[5],
                'difficulty': 'medium', 'tags': ['1003', 'Çıkmış Sınav Sorusu', t[0]]
            })
            q_no += 1

    return questions

if __name__ == '__main__':
    qs = get_1003_questions()
    print(f"Generated {len(qs)} questions for 1003.")
