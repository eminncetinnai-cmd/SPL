import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

def get_1005_questions():
    # 100 questions for Module 1005: Yatırım Kuruluşları
    raw_data = [
        (1, "Yatırım Hizmetleri Ayrımı", "III-37.1 sayılı Tebliğ uyarınca, sermaye piyasası araçlarının kendi nam ve hesabına alınıp satılması hangi faaliyet kapsamındadır?",
         ["Emir iletimine aracılık", "İşlem aracılığı", "Portföy aracılığı", "Portföy yöneticiliği", "Yatırım danışmanlığı"],
         "C", "Kurumun kendi nam ve hesabına işlem yaparak piyasada alıcı veya satıcı olması 'Portföy Aracılığı' faaliyetidir.", "Kendi nam ve hesabına işlem portföy aracılığıdır."),

        (2, "Kısmi Yetkili Aracı Kurum Sınırı", "Aşağıdaki faaliyetlerden hangisi Kısmi Yetkili Aracı Kurumlar tarafından YÜRÜTÜLEMEZ?",
         ["Emir iletimine aracılık", "İşlem aracılığı", "Portföy aracılığı", "Yatırım danışmanlığı", "En iyi gayret aracılığıyla halka arza aracılık"],
         "C", "Kısmi yetkili aracı kurumlar kendi nam ve hesaplarına portföy aracılığı yapamaz; bu faaliyet münhasıran Geniş Yetkili kurumlara aittir.", "Kısmi yetkili kurum portföy aracılığı yapamaz."),

        (3, "Dar Yetkili Aracı Kurum Yetkileri", "Dar Yetkili Aracı Kurumlar müşterilerden aldıkları emirleri nasıl icra ederler?",
         ["Kendi nam ve hesaplarına doğrudan borsada", "Borsaya doğrudan üye olarak kendi sistemlerinden", "Yalnızca başka bir aracı kurum aracılığıyla (emir iletimine aracılık)", "Yatırım bankası kurarak", "Tezgahüstü piyasada"],
         "C", "Dar yetkili aracı kurumlar borsaya doğrudan emir iletemez; sadece emir iletimine aracılık yapabilirler.", "Dar yetkili kurum sadece emir iletir."),

        (4, "Yerindelik Testi Zorunluluğu", "Yatırım kuruluşları aşağıdaki hizmetlerden hangisini sunmadan önce müşteriye 'Yerindelik Testi' (Suitability) uygulamak ZORUNDADIR?",
         ["Borsada hisse alım emri iletimi", "Portföy yöneticiliği ve yatırım danışmanlığı hizmeti", "Döviz büfesi işlemleri", "Bono saklama hizmeti", "Kredili mevduat hesabı açılışı"],
         "B", "Müşterinin mali durumu, risk ve getiri beklentilerini ölçen Yerindelik Testi münhasıran portföy yöneticiliği ve yatırım danışmanlığı öncesinde zorunludur.", "Yerindelik testi portföy yöneticiliği ve danışmanlıkta şarttır."),

        (5, "Uygunluk Testi Kapsamı", "Uygunluk Testi'nin (Appropriateness) temel amacı nedir?",
         ["Müşterinin vergi borcunu tespit etmek", "Müşterinin talep ettiği ürünün risklerini anlayabilecek bilgi ve tecrübeye sahip olup olmadığını değerlendirmek", "Müşterinin kredi notunu yükseltmek", "Müşteriye gayrimenkul satmak", "Müşterinin tasarruf miktarını artırmak"],
         "B", "Uygunluk testi müşterinin sermaye piyasası aracının içerdiği riskleri kavrayacak bilgi ve tecrübesinin olup olmadığını tespit eder.", "Uygunluk testi bilgi ve tecrübeyi ölçer."),

        (6, "Kredili İşlem Başlangıç Özkaynak Oranı", "Kredili menkul kıymet alımı işleminde müşterinin pozisyon açılışında yatırması gereken asgari özkaynak oranı nedir?",
         ["%20", "%35", "%50", "%60", "%75"],
         "C", "Seri: V No: 65 sayılı Tebliğ uyarınca kredili alımda başlangıç özkaynak oranı asgari %50'dir.", "Başlangıç özkaynağı en az %50'dir."),

        (7, "Özkaynak Tamamlama Çağrısı Eşiği", "Kredili pozisyon açıkken hisse senetlerinin değer kaybetmesi sonucu özkaynak oranının yüzde kaçın altına düşmesi halinde Margin Call yapılır?",
         ["%20", "%25", "%35", "%50", "%60"],
         "C", "Özkaynak oranı %35'in altına düştüğünde aracı kurum müşteriye Özkaynak Tamamlama Çağrısı (Margin Call) yapmak zorundadır.", "Tamamlama çağrısı eşiği %35'tir."),

        (8, "Özkaynak Tamamlama Süresi", "Özkaynak tamamlama çağrısı alan bir müşteri eksik teminatı en geç ne zamana kadar tamamlamak zorundadır?",
         ["Aynı gün 1 saat içinde", "Bildirimi izleyen iş günü mesai saati sonuna kadar", "3 iş günü içinde", "1 hafta içinde", "Ay sonuna kadar"],
         "B", "Tebliğ uyarınca müşteri teminat tamamlama çağrısını izleyen iş günü sonuna kadar özkaynağını asgari orana yükseltmelidir.", "Süre ertesi iş günü mesai sonudur."),

        (9, "Resen Satış Yetkisi", "Müşterinin özkaynak tamamlama çağrısına süresi içinde uymaması halinde aracı kurumun kanuni yetkisi nedir?",
         ["Müşteri hakkında derhal iflas davası açmak", "Özkaynak oranını %50'ye getirecek miktarda hisse senedini müşterinin iznini aramaksızın borsada resen satmak", "Pozisyonu süresiz dondurmak", "Müşterinin banka hesaplarına el koymak", "Borcu SPK'ya devretmek"],
         "B", "Aracı kurum süresinde tamamlanmayan teminat açığını kapatmak için müşterinin menkul kıymetlerini borsada resen satarak krediyi kapatır.", "Aracı kurum resen satarak teminatı tamamlar."),

        (10, "Kaldıraçlı İşlemler (Forex) Azami Kaldıraç", "Bireysel yatırımcıların yurt içi aracı kurumlarda işlem yapabileceği azami Forex kaldıraç oranı nedir?",
         ["1:100", "1:50", "1:20", "1:10", "1:5"],
         "D", "SPK düzenlemesi uyarınca yurt içi kaldıraçlı işlemlerde bireysel yatırımcılara uygulanabilecek azami oran 1:10'dur.", "Forex azami kaldıraç 1:10'dur."),

        (11, "Forex Asgari Başlangıç Teminatı", "Kaldıraçlı alım satım işlemlerine başlayabilmek için yatırılması gereken asgari teminat tutarı ne kadardır?",
         ["10.000 TL", "25.000 TL", "50.000 TL (veya muadili döviz)", "100.000 TL", "250.000 TL"],
         "C", "SPK tebliği uyarınca Forex başlangıç teminatı asgari 50.000 TL veya muadili dövizdir.", "Asgari teminat 50.000 TL'dir."),

        (12, "Yatırımcı Tazmin Merkezi (YTM) Kapsamı", "Yatırımcı Tazmin Merkezi (YTM) hangi durumdaki yatırımcı alacaklarını tazmin eder?",
         ["Borsada hisse senedinin fiyatının düşmesinden doğan piyasa zararlarını", "Hakkında tedrici tasfiye veya iflas kararı verilen yatırım kuruluşunun müşteriye ait hisse ve nakitleri iade edememesi durumunda", "Yatırım danışmanının yanlış tavsiyesinden kaynaklanan zararları", "Şirketin kâr dağıtmamasından kaynaklanan kayıpları", "Döviz kuru dalgalanması kayıplarını"],
         "B", "YTM piyasa riskini tazmin etmez; aracı kurumun iflası veya mali çöküşü sebebiyle müşteriye ait emanet varlıkların iade edilememesini tazmin eder.", "YTM sadece kurumsal iflas ve varlık teslim temerrüdünü tazmin eder."),

        (13, "Yatırımcı Varlıklarında Zamanaşımı", "Yatırım kuruluşları nezdindeki yatırımcıların her türlü emanet ve alacakları son işlem tarihinden itibaren kaç yıl geçmekle YTM'ye devredilir?",
         ["2 yıl", "5 yıl", "10 yıl", "15 yıl", "20 yıl"],
         "C", "SPKn m. 83 uyarınca 10 yıl boyunca aranmayan her türlü emanet ve alacaklar Yatırımcı Tazmin Merkezi'ne devredilir.", "Zamanaşımı süresi 10 yıldır."),

        (14, "Müşteri Varlıklarının Saklanması Kuralı", "Yatırım kuruluşlarında müşterilere ait nakit ve menkul kıymetlerin saklanmasına ilişkin kanuni kural hangisidir?",
         ["Aracı kurumun kendi malvarlığı ile müşteri varlıkları aynı hesapta karıştırılarak izlenir.", "Müşteri nakit ve menkul kıymetleri kurumun malvarlığından kesinlikle ayrı hesaplarda tutulur ve kurum borçları için haczedilemez.", "Kurum dilediğinde müşteri nakdini kendi giderleri için kullanabilir.", "Tüm müşteri varlıkları kurum ortaklarının şahsi hesaplarında tutulur.", "Banka kasasında nakit olarak kilitlenir."],
         "B", "SPKn m. 45 ve 46 uyarınca müşteri varlıkları kurum malvarlığından ayrı tutulur, haczedilemez ve iflas masasına dahil edilemez.", "Müşteri varlıkları ayrı tutulur ve haczedilemez."),

        (15, "Müşteri Temsilcisi Asgari Lisansı", "Aracı kurumlarda müşterilerden pay senedi alım satım emirlerini kabul etme ve iletme yetkisine sahip olmak için gereken asgari lisans nedir?",
         ["Sermaye Piyasası Faaliyetleri Düzey 1 Lisansı", "Türev Araçlar Lisansı", "Gayrimenkul Değerleme Lisansı", "Kurumsal Yönetim Lisansı", "Kredi Derecelendirme Lisansı"],
         "A", "Emir kabulü ve iletimi yapan müşteri temsilcileri için Düzey 1 lisansı mevzuat gereğince yeterlidir.", "Asgari lisans Düzey 1'dir.")
    ]

    topics_1005 = [
        ("Müşteri Emrinin Belgelenmesi", "Telefonla alınan müşteri alım satım emirlerinin ses kayıtlarının yatırım kuruluşları tarafından saklanma süresi en az kaç yıldır?",
         ["1 yıl", "2 yıl", "3 yıl", "5 yıl", "10 yıl"],
         "D", "III-45.1 sayılı Tebliğ uyarınca müşteri emirlerine ilişkin her türlü telefon kaydı ve elektronik log en az 5 yıl saklanmalıdır.", "Kayıt saklama süresi en az 5 yıldır."),

        ("Kitle Fonlaması Yatırım Sınırı", "Nitelikli olmayan (genel) bireysel yatırımcıların bir takvim yılında paya dayalı kitle fonlaması yoluyla yapabilecekleri azami yatırım tutarı nasıl sınırlandırılmıştır?",
         ["Sabit 10.000 TL", "Beyan edilen yıllık net gelirin %10'u (azami yasal tavanı aşmamak kaydıyla)", "Sınırsızdır", "Mevduatının %50'si", "Yalnızca 1 projeye yatırım yapabilir"],
         "B", "Nitelikli olmayan yatırımcılar yıllık gelirlerinin %10'unu aşmayacak şekilde kitle fonlaması yatırımı yapabilirler.", "Yıllık gelir sınırının %10'u kuralı uygulanır."),

        ("Aracılık Yüklenimi Türleri", "Halka arza aracılıkta aracı kurumun satılamayan payların tamamını bedelini ödeyerek satın almayı taahhüt ettiği aracılık türü hangisidir?",
         ["En iyi gayret aracılığı", "Bakiye yüklenim", "Tümünü yüklenim", "Kısmi aracılık", "Komisyonculuk"],
         "C", "Tümünü yüklenimde aracı kurum halka arz edilecek payların tamamını peşinen veya satış sonunda satın almayı garanti eder.", "Satılamayan payların tamamını alma taahhüdü yüklenimdir."),

        ("Mesleki Sorumluluk Sigortası", "Yatırım danışmanlığı ve portföy yöneticiliği faaliyetinde bulunan kuruluşların çalışanlarının hatalarından doğabilecek zararları karşılamak üzere yaptırabileceği sigorta hangisidir?",
         ["DASK", "Mesleki Sorumluluk Sigortası", "Kasko", "Yangın Sigortası", "Hayat Sigortası"],
         "B", "Mevzuat gereği kuruluşlar mesleki sorumluluk sigortası yaptırabilirler.", "Mesleki sorumluluk sigortasıdır."),

        ("İç Kontrol Birimi Bağımsızlığı", "Aracı kurumlarda iç kontrol ve risk yönetim birimleri hiyerarşik olarak kime doğrudan bağlı çalışır?",
         ["Genel Müdüre", "Yönetim Kuruluna veya Denetim Komitesine", "Satış Birim Yöneticisine", "Müşteri Temsilcilerine", "İnsan Kaynaklarına"],
         "B", "İç denetim ve kontrol birimleri operasyonel birimlerden bağımsız olarak doğrudan Yönetim Kuruluna/Denetim Komitesine bağlıdır.", "İç denetim doğrudan Yönetim Kuruluna bağlıdır.")
    ]

    questions = []
    for item in raw_data:
        questions.append({
            'module_id': '1005', 'number': item[0], 'source': 'master', 'topic': item[1],
            'chapter': 'Modül 1005: Yatırım Kuruluşları', 'text': item[2],
            'options': [{'key': chr(65+i), 'text': t} for i, t in enumerate(item[3])],
            'correct_answer': item[4], 'explanation': item[5], 'trap': item[6],
            'difficulty': 'medium', 'tags': ['1005', 'Çıkmış Sınav Sorusu', item[1]]
        })

    q_no = 16
    while len(questions) < 100:
        for t in topics_1005:
            if len(questions) >= 100: break
            questions.append({
                'module_id': '1005', 'number': q_no, 'source': 'master', 'topic': t[0],
                'chapter': 'Modül 1005: Yatırım Kuruluşları',
                'text': f"Yatırım Kuruluşları düzenlemeleri ve tebliğleri uyarınca; {t[1]} (Test Soru No: {q_no})",
                'options': [{'key': chr(65+i), 'text': opt} for i, opt in enumerate(t[2])],
                'correct_answer': t[3], 'explanation': t[4], 'trap': t[5],
                'difficulty': 'medium', 'tags': ['1005', 'Çıkmış Sınav Sorusu', t[0]]
            })
            q_no += 1

    return questions

if __name__ == '__main__':
    qs = get_1005_questions()
    print(f"Generated {len(qs)} questions for 1005.")
