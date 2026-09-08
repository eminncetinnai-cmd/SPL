import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

print("Starting to add 10 new questions to reach 210 for Module 1001...")

with open('src/data/all_questions.json', 'r', encoding='utf-8') as f:
    all_qs = json.load(f)

# Verify count before
q1001_before = [q for q in all_qs if str(q.get('module_id', '')) == '1001']
print(f"Current 1001 questions count: {len(q1001_before)}")
assert len(q1001_before) == 200, f"Expected 200, found {len(q1001_before)}"

ten_new_questions = [
    # Q131
    {
        "id": "q_1001_master_131",
        "module_id": "1001",
        "number": 131,
        "source": "master",
        "topic": "Katılım Fonu Portföy Sınırlamaları ve Katılma Hesabı İstisnası",
        "chapter": "BÖLÜM 4: YATIRIM FONLARI VE KOLEKTİF YATIRIM KURULUŞLARI",
        "difficulty": "zor",
        "tags": ["III-52.1", "Katılım Fonu", "Katılma Hesabı Limiti", "Portföy Sınırlamaları"],
        "text": "III-52.1 sayılı Yatırım Fonlarına İlişkin Esaslar Tebliği uyarınca, genel yatırım fonlarında vadeli mevduat/katılma hesabı yatırımları fon toplam değerinin en fazla %10'u ve tek bir bankada en fazla %3'ü olabilecekken; KATILIM FONLARI için bu oranlar sırasıyla nasıl uygulanır?",
        "options": [
            {"key": "A", "text": "Fon toplam değerinin en fazla %25'i ve tek bir bankada en fazla %10'u"},
            {"key": "B", "text": "Fon toplam değerinin en fazla %15'i ve tek bir bankada en fazla %5'i"},
            {"key": "C", "text": "Fon toplam değerinin en fazla %20'si ve tek bir bankada en fazla %7'si"},
            {"key": "D", "text": "Fon toplam değerinin en fazla %35'i ve tek bir bankada en fazla %15'i"},
            {"key": "E", "text": "Fon toplam değerinin en fazla %50'si ve tek bir bankada en fazla %20'si"}
        ],
        "correct_answer": "A",
        "trap": "Genel fonlarda %10 ve %3 olan limitler, katılım fonlarının faizsiz enstrüman ihtiyacı sebebiyle %25 ve %10 olarak genişletilmiştir.",
        "explanation": "III-52.1 sayılı Tebliğ m. 1.2.3.15 fıkra 5 (sayfa 123) uyarınca: Fon toplam değerinin en fazla %10'u bankalar nezdinde açılan mevduat/katılma hesaplarında değerlendirilebilir ve tek bir bankada değerlendirilebilecek tutar %3'ü aşamaz. Ancak katılım fonlarında bu oranlar birinci cümle için %25, ikinci cümle için %10 olarak uygulanır."
    },
    # Q132
    {
        "id": "q_1001_master_132",
        "module_id": "1001",
        "number": 132,
        "source": "master",
        "topic": "YTM Tedrici Tasfiyesinde Varlıkların Tahsis ve Garameten Ödeme Sırası",
        "chapter": "BÖLÜM 6: YATIRIM KURULUŞLARI, MÜŞTERİ TESTLERİ VE YATIRIMCI TAZMİN MERKEZİ",
        "difficulty": "zor",
        "tags": ["SPKn md. 84-85", "YTM", "Tedrici Tasfiye", "Garameten Ödeme"],
        "text": "6362 sayılı Sermaye Piyasası Kanunu md. 85 uyarınca hakkında tedricî tasfiye kararı verilen bir yatırım kuruluşunun aktiflerinin paraya çevrilmesiyle elde edilen bedellerin alacaklılara tahsisinde ve garameten ödenmesinde geçerli yasal öncelik sıralaması aşağıdakilerden hangisidir?",
        "options": [
            {"key": "A", "text": "1. Kamu alacakları — 2. Müşteri alacakları — 3. YTM alacakları — 4. Diğer alacaklar"},
            {"key": "B", "text": "1. Müşteri alacakları — 2. Kamu alacakları — 3. YTM alacakları ve tasfiye giderleri — 4. Diğer alacaklar"},
            {"key": "C", "text": "1. YTM alacakları — 2. Müşteri alacakları — 3. Diğer alacaklar — 4. Kamu alacakları"},
            {"key": "D", "text": "1. Müşteri alacakları — 2. Diğer alacaklar — 3. YTM alacakları — 4. Kamu alacakları"},
            {"key": "E", "text": "1. Takasbank temerrüt alacakları — 2. Kamu alacakları — 3. Müşteri alacakları — 4. YTM alacakları"}
        ],
        "correct_answer": "B",
        "trap": "İcra İflas Hukukundaki genel kamu alacağı önceliğinin aksine, SPKn tedrici tasfiyesinde 1. sırada MÜŞTERİ ALACAKLARI yer alır!",
        "explanation": "6362 sayılı SPKn md. 85 ve resmi ders notu sayfa 50 uyarınca tedrici tasfiyede aktiflerden yapılacak ödemelerdeki kesin sıralama şöyledir: 1) Müşteri alacakları tamamen, karşılanamazsa garameten; 2) Kamu alacakları garameten; 3) YTM'nin müşterilere yaptığı ödemeler ve tasfiye giderlerinden doğan alacakları garameten; 4) Diğer alacaklar. Bir gruba ödeme yapılabilmesi için önceki grubun alacağının tamamen karşılanması zorunludur."
    },
    # Q133
    {
        "id": "q_1001_master_133",
        "module_id": "1001",
        "number": 133,
        "source": "master",
        "topic": "SPK Tarafından Bağımsız Denetim Zorunluluğu Getirilebilecek Özel Haller",
        "chapter": "BÖLÜM 1: 6362 SAYILI SERMAYE PİYASASI KANUNU VE GENEL ESASLAR",
        "difficulty": "orta",
        "tags": ["SPKn md. 14/4", "Bağımsız Denetim", "SPK Yetkisi", "Önemli İşlemler"],
        "text": "6362 sayılı Sermaye Piyasası Kanunu md. 14/4 uyarınca periyodik finansal raporlar dışında Kurul'un (SPK) şirketlere özel olarak bağımsız denetim yaptırma yükümlülüğü getirebileceği haller arasında aşağıdakilerden hangisi YER ALMAZ?",
        "options": [
            {"key": "A", "text": "Sermaye piyasası araçlarının ilk halka arzında"},
            {"key": "B", "text": "Sermaye piyasası araçlarının borsada işlem görme başvurusunda"},
            {"key": "C", "text": "Şirketin yıllık olağan kâr payı avansı dağıtım kararında"},
            {"key": "D", "text": "SPKn md. 23'te tanımlanan önemli nitelikteki işlemlerde"},
            {"key": "E", "text": "Ortaklığın faaliyetlerini ve finansal durumunu önemli derecede etkileyen olay ve gelişmelerde"}
        ],
        "correct_answer": "C",
        "trap": "Kâr payı avansı şirket içi ara dönem finansal tablolara dayanır; SPKn 14/4'teki 4 özel bağımsız denetim hali arasında kâr payı avansı yoktur.",
        "explanation": "SPKn md. 14/4 (resmi not sayfa 15) uyarınca Kurul'un bağımsız denetim yükümlülüğü getirebileceği haller kanunda 4 bent halinde tahdidi olarak sayılmıştır: 1) Halka arzda, 2) Borsada işlem görme başvurusunda, 3) SPKn md. 23'te tanımlanan önemli nitelikteki işlemlerde, 4) Ortaklığın faaliyetlerini ve finansal durumunu önemli derecede etkileyen olay ve gelişmelerde."
    },
    # Q134
    {
        "id": "q_1001_master_134",
        "module_id": "1001",
        "number": 134,
        "source": "master",
        "topic": "Yeşil Borçlanma Aracı ve Kira Sertifikası Rehberi Esasları",
        "chapter": "BÖLÜM 5: KURUMSAL YÖNETİM İLKELERİ (II-17.1) VE YÖNETİM KURULU KOMİTELERİ",
        "difficulty": "orta",
        "tags": ["i-SPK 128.18", "Yeşil Borçlanma Aracı", "İkinci Taraf Görüşü", "Etki Raporu"],
        "text": "SPK Karar Organı'nın i-SPK 128.18 sayılı İlke Kararı ile yayımlanan 'Yeşil Borçlanma Aracı, Sürdürülebilir Borçlanma Aracı, Yeşil Kira Sertifikası, Sürdürülebilir Kira Sertifikası Rehberi' uyarınca aşağıdakilerden hangisi ihraççılar için ZORUNLU bir yükümlülüktür?",
        "options": [
            {"key": "A", "text": "İhraçtan elde edilen fonun tamamının yalnızca kamu bankalarında vadeli mevduatta değerlendirilmesi"},
            {"key": "B", "text": "Çevresel etkilerin her ay Borsa İstanbul tarafından ölçülerek kamuya açıklanması"},
            {"key": "C", "text": "İhraç edilen tahvillerin yalnızca yabancı kurumsal yatırımcılara tahsisli satılması"},
            {"key": "D", "text": "Yeşil borçlanma aracı çerçeve belgesinin Rehber ile uyumlu olduğunun yetkili bir dış değerlendirme kuruluşunca hazırlanan 'ikinci taraf görüşü' ile incelenip teyit edilmesi"},
            {"key": "E", "text": "İhraççının yönetim kurulundaki tüm üyelerin bağımsız üyelerden oluşturulması"}
        ],
        "correct_answer": "D",
        "trap": "Yeşil ve sürdürülebilir ihraçlarda en kritik yasal gereklilik bağımsız bir dış değerlendirme kuruluşundan 'ikinci taraf görüşü' (second party opinion) alınmasıdır.",
        "explanation": "Resmi ders notu sayfa 96 uyarınca Rehber kapsamında; yeşil borçlanma aracı çerçeve belgesinin Rehber ile uyumlu olduğunun 'ikinci taraf görüşü' ile incelenmesi ve değerlendirilmesi zorunludur. Ayrıca ihraçtan elde edilen fonun kullanımı yılda bir ve tamamı harcandığında fon kullanım ve etki raporu ile KAP'ta açıklanmalıdır."
    },
    # Q135
    {
        "id": "q_1001_master_135",
        "module_id": "1001",
        "number": 135,
        "source": "master",
        "topic": "Halka Açık Ortaklıkların Kendi Paylarını İktisabı ve Kısıtlanmış Yedekler",
        "chapter": "BÖLÜM 1: 6362 SAYILI SERMAYE PİYASASI KANUNU VE GENEL ESASLAR",
        "difficulty": "zor",
        "tags": ["SPKn md. 22", "Kendi Paylarını İktisap", "Kısıtlanmış Yedek", "Özkaynaklar"],
        "text": "6362 sayılı SPKn md. 22 uyarınca halka açık anonim ortaklıkların kendi paylarını geri satın almaları (hisse geri alımı) durumunda, şirketin malvarlıksal dengesini ve alacaklıları korumak amacıyla muhasebe ve özkaynak düzeni bakımından hangi yasal zorunluluk getirilmiştir?",
        "options": [
            {"key": "A", "text": "Geri alınan payların alım bedeli kadar yedek akçe ayrılır ve bu ayrılan tutar özkaynaklar altında 'kısıtlanmış yedek' olarak sınıflandırılır."},
            {"key": "B", "text": "Geri alınan payların satın alma bedeli kadar genel kurulca nakit temettü dağıtılması şarttır."},
            {"key": "C", "text": "Geri alınan payların tamamının satın alındığı gün derhal imha edilerek sermayenin azaltılması zorunludur."},
            {"key": "D", "text": "Geri alınan paylar doğrudan Borsa İstanbul Takasbank Garanti Fonu hesabına bloke olarak devredilir."},
            {"key": "E", "text": "Şirketin geri aldığı paylar karşılığında bankalardan eşdeğer tutarda kredi limiti açtırması zorunludur."}
        ],
        "correct_answer": "A",
        "trap": "Geri alınan paylar derhal imha edilmez; portföyde tutulabilir ancak geri alım bedeli kadar özkaynaklarda 'kısıtlanmış yedek' ayrılmak zorundadır.",
        "explanation": "6362 sayılı SPKn md. 22/1 son cümlesi ve resmi SPL ders notu sayfa 30 uyarınca: 'Geri alınan payların geri alım bedeli kadar yedek akçe ayrılır ve bu ayrılan yedek akçe özkaynaklar altında kısıtlanmış yedek olarak sınıflandırılır.'"
    },
    # Q136
    {
        "id": "q_1001_master_136",
        "module_id": "1001",
        "number": 136,
        "source": "master",
        "topic": "Borsa İşlemlerinden Doğan Uyuşmazlıklarda SPK'ya İtiraz ve YTM Eşiği",
        "chapter": "BÖLÜM 1: 6362 SAYILI SERMAYE PİYASASI KANUNU VE GENEL ESASLAR",
        "difficulty": "zor",
        "tags": ["SPKn md. 84/5", "Borsa Uyuşmazlıkları", "SPK İtiraz", "Borsa Yönetim Kurulu"],
        "text": "6362 sayılı Sermaye Piyasası Kanunu uyarınca, yatırım kuruluşlarının kendi aralarında veya müşterileri ile borsa işlemlerinden doğan uyuşmazlıkların çözümünde borsa yönetim kurulu kararlarına karşı tarafların Sermaye Piyasası Kurulu nezdinde itirazda bulunabilmeleri hangi şartın varlığına bağlıdır?",
        "options": [
            {"key": "A", "text": "Uyuşmazlığın mutlaka en az 10 farklı yatırımcıyı ilgilendirmesi şartına"},
            {"key": "B", "text": "Uyuşmazlık konusunun sadece açığa satış işlemlerinden kaynaklanması şartına"},
            {"key": "C", "text": "Borsa yönetim kurulunun itiraz hakkını açıkça esas sözleşmeyle saklı tutmuş olması şartına"},
            {"key": "D", "text": "Uyuşmazlık tarafı aracı kurumun faaliyet izninin geçici olarak durdurulmuş olması şartına"},
            {"key": "E", "text": "Uyuşmazlık konusu tutarın, yatırımcıları tazmin kapsamında hak sahiplerine ödenecek azami tutarı gösteren SPKn md. 84/5'teki azami tazmin tutarından fazla olması şartına"}
        ],
        "correct_answer": "E",
        "trap": "Her borsa uyuşmazlığı Kurul'a taşınamaz; Kurul'a itiraz edebilmek için tutarın YTM azami tazmin limitinden fazla olması kanuni şarttır.",
        "explanation": "6362 sayılı SPKn ve resmi ders notu sayfa 46 uyarınca: Borsa işlemlerinden doğan uyuşmazlıkların çözümlenmesine ilişkin usul ve esaslar borsa yönetim kurulunca belirlenir. Uyuşmazlık konusu tutarın yatırımcıları tazmin kapsamında ödenecek azami tutarı gösteren SPKn md. 84/5 hükmündeki tutardan fazla olması halinde söz konusu borsa yönetim kurulu kararına karşı taraflar Kurul nezdinde itirazda bulunabilirler."
    },
    # Q137
    {
        "id": "q_1001_master_137",
        "module_id": "1001",
        "number": 137,
        "source": "master",
        "topic": "Yatırım Hizmet ve Faaliyet İzinlerinin Kurulca İptal Nedenleri",
        "chapter": "BÖLÜM 1: 6362 SAYILI SERMAYE PİYASASI KANUNU VE GENEL ESASLAR",
        "difficulty": "orta",
        "tags": ["SPKn md. 44", "Faaliyet İzni İptali", "2 Yıl Faaliyetsizlik", "3 Ay Süre"],
        "text": "6362 sayılı Sermaye Piyasası Kanunu md. 44 uyarınca, Sermaye Piyasası Kurulu tarafından verilmiş yetki belgesi ve faaliyet izinlerinin iptal edilmesine ilişkin aşağıdaki hallerden hangisi KANUNA UYGUN DEĞİLDİR?",
        "options": [
            {"key": "A", "text": "Faaliyette bulunma yetkisinden açıkça feragat edilmesi"},
            {"key": "B", "text": "Faaliyet izninin verildiği tarihten itibaren iki yıl süreyle ilgili izin kapsamında herhangi bir faaliyette bulunulmaması"},
            {"key": "C", "text": "Faaliyet izninin yanlış veya yanıltıcı beyanlarda bulunularak alınmış olması"},
            {"key": "D", "text": "İzin sırasında aranan şartların kaybedildiğinin tespitinden itibaren üç ay içinde bu şartların yeniden sağlanamaması"},
            {"key": "E", "text": "Ortaklığın son üç aylık dönemde borsa endeksinin altında getiri sağlaması"}
        ],
        "correct_answer": "E",
        "trap": "Piyasa getirisi veya borsa performansı faaliyet izninin iptali sebebi olamaz; yasal şartlar 2 yıl faaliyetsizlik, yanıltıcı beyan ve 3 ayda şartları geri kazanamamadır.",
        "explanation": "SPKn md. 44 ve resmi SPL notu sayfa 35 uyarınca yetki belgesi ve faaliyet izinleri: 1) Açık feragat veya 2 yıl süreyle faaliyette bulunulmaması, 2) Yanlış/yanıltıcı beyanla alınması, 3) Aranan şartların kaybedilmesinden itibaren 3 ay içinde yeniden sağlanamaması hallerinde iptal edilir. Ticari performans veya endeks getirisi iptal nedeni değildir."
    },
    # Q138
    {
        "id": "q_1001_master_138",
        "module_id": "1001",
        "number": 138,
        "source": "master",
        "topic": "Portföy Saklama Hizmetinde Bağımsızlık ve Yasaklar",
        "chapter": "BÖLÜM 1: 6362 SAYILI SERMAYE PİYASASI KANUNU VE GENEL ESASLAR",
        "difficulty": "zor",
        "tags": ["SPKn md. 56", "Portföy Saklayıcısı", "PYŞ İlişkisi", "Yönetici Yasakları"],
        "text": "6362 sayılı SPKn ve ilgili tebliğler uyarınca portföy saklama hizmetini yürüten kuruluş ile portföy yönetim şirketi (PYŞ) arasındaki bağımsızlık ilkeleri ve yasaklar hakkında aşağıdaki ifadelerden hangisi DOĞRUDUR?",
        "options": [
            {"key": "A", "text": "Portföy saklama hizmetini yürüten kuruluş ile portföy yönetim şirketi aynı tüzel kişi olabilir; ayrı tüzel kişilik şartı aranmaz."},
            {"key": "B", "text": "Saklama kuruluşu ve PYŞ yöneticileri karşılıklı olarak birbirlerinin şirketlerinde yönetim kurulu üyesi veya yönetici olarak görev alabilirler."},
            {"key": "C", "text": "Portföy saklama hizmetini yürüten kuruluş ile portföy yönetim şirketi aynı tüzel kişi olamaz; birinin yöneticileri ve temsilcileri diğerinde ortak, yönetici veya temsilci olamaz."},
            {"key": "D", "text": "Portföy saklama hizmetini yürüten kuruluş katılma payı sahiplerine karşı sorumlu değildir; tüm mali sorumluluk sadece kurucuya aittir."},
            {"key": "E", "text": "Saklama kuruluşu saklamasındaki varlıkları Kurul izni olsa dahi hiçbir şekilde başka bir saklama kuruluşu nezdinde alt saklamaya veremez."}
        ],
        "correct_answer": "C",
        "trap": "Saklayıcı ile PYŞ kesinlikle AYNI TÜZEL KİŞİ OLAMAZ ve yöneticileri birbirinde görev alamaz; çıkar çatışmasını önlemek kanuni amir hükümdür.",
        "explanation": "SPKn md. 56 ve resmi not sayfa 42 uyarınca: 'Portföy saklama hizmetini yürüten kuruluş ile portföy yönetim şirketi aynı tüzel kişi olamaz. Portföy saklama kuruluşu yetkilileri PYŞ'de ortak veya yönetici olamaz; PYŞ ortak ve yöneticileri de saklama kuruluşunda yönetici veya temsilci olamaz.' Ayrıca saklayıcı katılma payı sahiplerine karşı doğrudan müteselsilen sorumludur."
    },
    # Q139
    {
        "id": "q_1001_master_139",
        "module_id": "1001",
        "number": 139,
        "source": "master",
        "topic": "Örtülü Kazanç ve Malvarlığını Azaltıcı İşlemlerde İptal ve Butlan Dava Süreleri",
        "chapter": "BÖLÜM 2: SPK'NIN GÖREV/YETKİLERİ, TEDBİRLER, SUÇLAR VE YAPTIRIMLAR",
        "difficulty": "zor",
        "tags": ["SPKn md. 92", "SPKn md. 94", "Dava Süreleri", "İptal ve Butlan"],
        "text": "6362 sayılı Sermaye Piyasası Kanunu md. 92 uyarınca ihraççıların hukuka aykırı işlemleriyle sermayesinin veya malvarlığının azalmasına yol açılması (ve örtülü kazanç aktarımı) halinde Kurul'un açabileceği iptal ve butlan davalarının zamanaşımı süreleri hangisinde doğru verilmiştir?",
        "options": [
            {"key": "A", "text": "Tespitten itibaren 1 ay, işlemden itibaren 1 yıl içinde iptal davası; 2 yıl içinde butlan davası"},
            {"key": "B", "text": "Tespitten itibaren 6 ay, işlemden itibaren 2 yıl içinde iptal davası; 3 yıl içinde butlan davası"},
            {"key": "C", "text": "Tespitten itibaren 1 yıl, işlemden itibaren 5 yıl içinde iptal davası; 10 yıl içinde butlan davası"},
            {"key": "D", "text": "Kurulca tespiti tarihinden itibaren üç ay ve her hâlde işlemin vukuu tarihinden itibaren üç yıl içinde iptal davası; beş yıl içinde butlan veya yokluğun tespiti davası"},
            {"key": "E", "text": "Her zaman açılabilir; sermaye piyasasında malvarlığını azaltıcı işlemlerde zamanaşımı uygulanmaz"}
        ],
        "correct_answer": "D",
        "trap": "İptal davası süresi tespitten 3 ay / işlemden 3 yıldır; butlan veya yokluk tespiti davası süresi ise 5 yıldır.",
        "explanation": "6362 sayılı SPKn md. 92/1-b ve resmi ders notu sayfa 53 uyarınca: İhraççıların hukuka aykırı işlemleri sebebiyle sermayesinin yahut malvarlığının azalmasına veya kaybına yol açıldığının tespiti halinde Kurul: 'Bu durum ve işlemlerin hukuka aykırılığının Kurulca tespiti tarihinden itibaren üç ay ve her hâlde durum ve işlemin vukuu tarihinden itibaren üç yıl içinde iptal davası ve beş yıl içinde butlan veya yokluğun tespiti davası açmaya' yetkilidir."
    },
    # Q140
    {
        "id": "q_1001_master_140",
        "module_id": "1001",
        "number": 140,
        "source": "master",
        "topic": "TSPB Disiplin Yönetmeliğinde Zamanaşımı ve Sicilden Silinme Hükümleri",
        "chapter": "BÖLÜM 7: TSPB MESLEK KURALLARI, ETİK İLKELER, ÇIKAR ÇATIŞMALARI VE DİSİPLİN HÜKÜMLERİ",
        "difficulty": "orta",
        "tags": ["TSPB Disiplin Yönetmeliği", "Soruşturma Zamanaşımı", "Sicilden Silinme", "Tekerrür"],
        "text": "Türkiye Sermaye Piyasaları Birliği (TSPB) Disiplin Yönetmeliği uyarınca disiplin cezalarında soruşturma zamanaşımı, ceza zamanaşımı ve sicilden silinme süreleri hakkında aşağıdaki ifadelerden hangisi DOĞRUDUR?",
        "options": [
            {"key": "A", "text": "Soruşturmaya başlanabilmesi için fiilin işlendiği tarihten itibaren 3 yıl geçmemiş olmalı; sicil kayıtları 10 yıl sonra silinmelidir."},
            {"key": "B", "text": "Soruşturmaya başlanabilmesi için fiilin işlendiği tarihten itibaren bir yıldan fazla süre geçmemiş olması gerekir; kesinleşen cezanın iki yıl içinde uygulanamaması halinde ceza zamanaşımına uğrar ve sicil kayıtları beşinci yılın sonunda silinir."},
            {"key": "C", "text": "Kesinleşen disiplin cezasının sicilden silinmesi için 20 yıl geçmesi şarttır ve tekerrür süresiz olarak uygulanır."},
            {"key": "D", "text": "Ceza kovuşturması bulunsa dahi disiplin soruşturması her halükarda 6 ay içinde düşer."},
            {"key": "E", "text": "Birlik disiplin cezaları üye siciline işlenmez, yalnızca internet sitesinde süresiz duyurulur."}
        ],
        "correct_answer": "B",
        "trap": "Soruşturma zamanaşımı 1 yıl, cezanın infaz zamanaşımı 2 yıl, sicilden silinme 5 yıl ve tekerrüre esas alınmama süresi ise 1 yıldır!",
        "explanation": "TSPB Disiplin Yönetmeliği md. 1.3.3.2.8 ve md. 1.3.3.3.1 (sayfa 176) uyarınca: Soruşturmaya başlanabilmesi için fiilin işlendiği tarihten itibaren 1 yıldan fazla süre geçmemiş olması gerekir (ceza zamanaşımı daha uzunsa o süre uygulanır). Kesinleşen ceza 2 yıl içinde uygulanamazsa zamanaşımına uğrar. Karar ve belgeler 5 yıl saklanır ve 5. yılın sonunda sicilden silinir. Üye 1 yıl içinde yeni fiil işlemezse önceki ceza tekerrüre esas alınmaz."
    }
]

# Append the 10 questions
all_qs.extend(ten_new_questions)

q1001_after = [q for q in all_qs if str(q.get('module_id', '')) == '1001']
print(f"New 1001 questions count: {len(q1001_after)}")
assert len(q1001_after) == 210, f"Expected 210, found {len(q1001_after)}"
print(f"Total all questions count: {len(all_qs)}")
assert len(all_qs) == 760, f"Expected 760, found {len(all_qs)}"

# Save all_questions.json
with open('src/data/all_questions.json', 'w', encoding='utf-8') as f:
    json.dump(all_qs, f, ensure_ascii=False, indent=2)
print("Saved src/data/all_questions.json")

# Save questions_master.json
with open('src/data/questions_master.json', 'w', encoding='utf-8') as f:
    json.dump(all_qs, f, ensure_ascii=False, indent=2)
print("Saved src/data/questions_master.json")

print("\n--- Answer Key Distribution of the 10 New Questions ---")
ans_counts = {}
for q in ten_new_questions:
    a = q['correct_answer']
    ans_counts[a] = ans_counts.get(a, 0) + 1
print("Distribution:", sorted(ans_counts.items()))
print("All tasks completed successfully!")
