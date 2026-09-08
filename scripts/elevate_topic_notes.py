# -*- coding: utf-8 -*-
"""
elevate_topic_notes.py
Enriches and simplifies all 29 sections in src/data/topic_notes.json.
Features:
- Clear, pedagogical language for 11 September 2026 SPL Düzey 1 exam.
- Multiple concrete, realistic real-world market examples (at least 2 per section) with step-by-step numbers.
- Up-to-date 2026 regulations: 10M TL individual qualified investor / hedge fund threshold, Clean/Dirty price formulas, Sukuk breakdown (Istisna, Murabaha, Icara, Mudaraba), warrant moneyness & intrinsic value calculations, etc.
- Crisp exam traps and key takeaways.
"""

import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('src/data/topic_notes.json', 'r', encoding='utf-8') as f:
    tn = json.load(f)

# Define full enriched data for each section
ENRICHMENTS = {
    # =========================================================================
    # MODÜL 1001: SERMAYE PİYASASI MEVZUATI
    # =========================================================================
    "sec_1001_01": {
        "title": "1. Sermaye Piyasası Kanunu'nun (SPKn) Amacı, Kapsamı ve SPK'nın Düzenleme/Denetleme Yetkileri",
        "content": [
            "6362 sayılı Sermaye Piyasası Kanunu'nun (SPKn) temel varlık sebebi; sermaye piyasasının şeffaf, etkin, adil ve rekabetçi bir ortamda işlemesini temin etmek ve en önemlisi tasarruf sahiplerinin (yatırımcıların) hak ve menfaatlerini korumaktır.",
            "Sermaye Piyasası Kurulu (SPK), idari ve mali özerkliğe sahip bir kamu otoritesidir. SPK; ihraççılardan halka açık ortaklıklara, borsalardan aracı kurumlara, Takasbank'tan MKK'ya kadar piyasanın tüm aktörlerini düzenler ve denetler.",
            "Sınavda Kritik Yetki Ayrımı: SPK'nın doğrudan yetkileri ile mahkeme kararı gerektiren halleri kesinlikle karıştırmayın. SPK; idari para cezası kesebilir, borsada işlem yasağı getirebilir ve izinsiz faaliyette bulunan internet sitelerine BTK üzerinden doğrudan erişim engeli aldırabilir. Ancak SPK kişileri hapse atamaz (mahkeme karar verir), doğrudan şirket malvarlığına el koyamaz ve şirket yöneticisini doğrudan azledemez; bunun için Asliye Ticaret Mahkemesi'nden görevden uzaklaştırma ve kayyum atanması talep eder.",
            "SPK Kararlarına İtiraz: SPK kararları idari işlem niteliğinde olduğundan, ilgililer kararın tebliğinden itibaren 30 gün içinde İdare Mahkemelerinde iptal davası açabilirler."
        ],
        "concrete_examples": [
            "Örnek 1 (İzinsiz Faaliyet & Erişim Engeli): Yurt dışında kurulan ve SPK lisansı bulunmayan 'X-Forex' adlı internet sitesi, Türk vatandaşlarına sosyal medyadan kaldıraçlı döviz işlemi yaptırmaya başladığında; SPK m.99 gereğince mahkeme kararı beklemeksizin doğrudan BTK'ya (Bilgi Teknolojileri ve İletişim Kurumu) bildirimde bulunarak siteye Türkiye'den erişimi derhal engeller.",
            "Örnek 2 (SPK Onayı Devlet Garantisi Değildir): ABC Holding, halka arz için izahname hazırlayıp SPK'ya onaylatır. Yatırımcı Kerem Bey bu hisseleri alır ancak şirket kötü yönetildiği için hisseler %40 değer kaybeder. Kerem Bey 'SPK onayladı, paramı devlet ödesin' diyemez; çünkü SPK onayı sadece bilgilerin tam ve doğru olduğunu gösterir, şirketin kâr edeceğine devlet garantisi VERMEZ."
        ],
        "key_takeaways": [
            "SPK'nın nihai ve birincil hedefi tasarruf sahiplerinin (yatırımcıların) haklarını korumaktır.",
            "SPK izahnameyi onaylarken şirketin mali başarısına veya hissenin prim yapacağına asla garanti vermez.",
            "SPK izinsiz sermaye piyasası faaliyeti yürüten siteleri doğrudan BTK aracılığıyla erişime kapatır.",
            "SPK kararlarına karşı yargı yolu açıktır; idare mahkemelerinde 30 gün içinde dava açılabilir."
        ],
        "exam_traps": [
            "⚠️ SINAV TUZAĞI: 'SPK izahnameyi onaylayarak ihraç edilen paylara veya borçlanma senetlerine devlet garantisi sağlar' ifadesi sınavlarda en çok sorulan YANLIŞ öncüldür.",
            "⚠️ DİKKAT: SPK şirket yöneticilerini re'sen görevden alamaz; mahkemeden görevden uzaklaştırma ve kayyum atanmasını talep eder."
        ]
    },
    "sec_1001_02": {
        "title": "2. İzahname, Halka Arz ve Kamuyu Aydınlatma Platformu (KAP) Esasları",
        "content": [
            "Sermaye piyasası araçlarının halka arz edilebilmesi veya borsada işlem görebilmesi için kural olarak 'İzahname' hazırlanması ve Kurulca onaylanması şarttır.",
            "İzahnamenin Geçerlilik Süresi: SPK onayından itibaren izahname tam 12 AY boyunca geçerlidir. Süre içinde yeni ihraç yapılacaksa ek ve değişikliklerin Kurulca onaylanması yeterlidir; 12 ay dolduğunda ise sıfırdan yeni izahname hazırlanır.",
            "Halka Arzda Talep Toplama Süreleri ve Yöntemleri (Tebliğ II-5.2): Payların halka arzında talep toplama süresi en az 2 İŞ GÜNÜ, en fazla 30 İŞ GÜNÜ olabilir. Talep toplama 4 yöntemle yapılır: 1) Sabit Fiyatla, 2) Fiyat Teklifi Alma Yoluyla, 3) Fiyat Aralığı Yoluyla ve 4) Borsada Satış Yöntemi.",
            "İçsel Bilgi ve Erteleme (Tebliğ II-15.1): İçsel bilgi; henüz kamuya açıklanmamış, doğrudan veya dolaylı olarak ihraççıyla ilgili, kesinleşmiş ve açıklandığında fiyatı etkileyebilecek bilgidir. Şirketler meşru menfaatlerini korumak amacıyla içsel bilginin açıklanmasını erteleyebilirler. ANCAK bilginin gizliliği bozulduğu veya basına sızdığı anda şirket ertelemeyi derhal kaldırıp KAP'ta özel durum açıklaması yapmak ZORUNDADIR."
        ],
        "concrete_examples": [
            "Örnek 1 (İçsel Bilginin Ertelenmesi & Sızması): BIST'te işlem gören bir savunma sanayii şirketi, 500 milyon dolarlık dev bir ihracat sözleşmesi imzalamak üzeredir. Sözleşme imzalanana kadar hisse spekülasyonunu önlemek için açıklamayı erteler. Ancak bir internet gazetesinde sözleşmenin detayları sızdırılınca, gizlilik kalktığı için şirket aynı iş günü içinde derhal KAP'ta resmi özel durum açıklaması yapmak zorunda kalır.",
            "Örnek 2 (Talep Toplama Süresi Sınav Sorusu): Bir teknoloji şirketi halka arzında talep toplama tarihlerini Pazartesi ve Salı olarak 2 iş günü belirler (Mevzuata uygundur: asgari 2 iş günü). Şirket talep toplamayı tek bir güne indiremez veya 30 iş gününden uzun tutamaz."
        ],
        "key_takeaways": [
            "İzahnamenin yasal geçerlilik süresi: Kesin olarak 12 AYDIR.",
            "Halka arz talep toplama süresi: En az 2 İŞ GÜNÜ, en fazla 30 İŞ GÜNÜ.",
            "İçsel bilginin ertelenmesi şirketin sorumluluğundadır; bilgi sızarsa derhal KAP açıklaması zorunludur.",
            "İzahnamede değişiklik veya yeni husus çıkarsa, talepte bulunan yatırımcılar taleplerini 2 İŞ GÜNÜ içinde geri alabilir."
        ],
        "exam_traps": [
            "⚠️ SÜRE TUZAĞI: İzahname onay süresi halka açık şirketler için 10 iş günü, ilk defa halka açılacak şirketler için 20 iş günüdür.",
            "⚠️ İÇSEL BİLGİ TUZAĞI: İçsel bilginin suç veya geçerli sayılması için noter tasdikli olması gerekmez; somut ve kamuya duyurulmamış olması yeterlidir."
        ]
    },
    "sec_1001_03": {
        "title": "3. Kurumsal Yönetim İlkeleri ve Bağımsız Yönetim Kurulu Üyeleri",
        "content": [
            "Kurumsal Yönetim İlkeleri dört temel sütun üzerine kuruludur: Adillik, Şeffaflık, Hesap Verebilirlik ve Sorumluluk.",
            "Bağımsız Yönetim Kurulu Üye Sayısı Kuralı: Halka açık anonim ortaklıklarda bağımsız üye sayısı, toplam yönetim kurulu üye sayısının en az üçte birinden (1/3) az olamaz ve her halükarda ASGARİ 2 ÜYE olmak zorundadır. Üçte bir oranı hesaplanırken küsuratlar doğrudan BİR ÜST TAM SAYIYA YUVARLANIR.",
            "Bağımsız Üyelerin Görev Süresi ve Kısıtlamaları: Bir bağımsız yönetim kurulu üyesi aynı şirkette son 10 yıl içinde toplamda en fazla 6 YIL görev yapabilir. Şirketle, iştirakleriyle veya hâkim ortakla son 5 yıl içinde istihdam, sermaye veya ticari bağı bulunmamalıdır.",
            "İlişkili Taraf İşlemleri Eşikleri: Halka açık ortaklıkların ilişkili taraflarıyla yapacakları varlık/hizmet devirlerinde işlem tutarı aktif büyüklüğünün veya hasılatın %5'ini aşıyorsa SPK lisanslı değerleme raporu zorunludur. İşlem tutarı %10'u aşıyorsa genel kurul onayı ve bağımsız üyelerin çoğunluğunun onayı şarttır."
        ],
        "concrete_examples": [
            "Örnek 1 (Bağımsız Üye Yuvarlama Hesabı): X A.Ş.'nin Yönetim Kurulu 7 kişiden oluşmaktadır. Yasal bağımsız üye sayısı: 7 / 3 = 2,33'tür. Kanun gereği küsurat yukarı yuvarlanır; dolayısıyla bu şirkette EN AZ 3 BAĞIMSIZ ÜYE bulunmak zorundadır (2 üye yetersizdir!).",
            "Örnek 2 (İlişkili Taraf Eşiği): Aktif büyüklüğü 1 Milyar TL olan halka açık bir şirket, ana ortağına ait bir fabrikayı 70 Milyon TL'ye satın almak istemektedir. 70M / 1.000M = %7'dir. %5 eşiği aşıldığı için SPK lisanslı gayrimenkul değerleme kuruluşundan resmi değerleme raporu alınması kanuni zorunluluktur."
        ],
        "key_takeaways": [
            "Bağımsız YK üye sayısı: Toplam üyenin en az 1/3'ü ve asgari 2 üye (küsurat yukarı yuvarlanır).",
            "Bağımsız üye azami görev süresi: Son 10 yılda en fazla 6 yıl.",
            "İlişkili taraf değerleme zorunluluğu eşiği: Aktif veya hasılatın %5'i; Genel kurul onay eşiği: %10'u.",
            "Denetimden Sorumlu Komite üyelerinin TAMAMI bağımsız yönetim kurulu üyelerinden oluşmak zorundadır."
        ],
        "exam_traps": [
            "⚠️ YUVARLAMA TUZAĞI: 8 kişilik yönetim kurulunda 8/3 = 2.66'dır, yukarı yuvarlanarak en az 3 üye gerekir; 6 kişilikte 6/3 = 2 üyedir.",
            "⚠️ KOMİTE TUZAĞI: Denetim komitesi üyelerinin en az biri değil, TAMAMI bağımsız yönetim kurulu üyesi olmak zorundadır."
        ]
    },
    "sec_1001_04": {
        "title": "4. Pay Sahipliği Hakları, Sermaye Artırımları ve Önemli Nitelikteki İşlemler",
        "content": [
            "Pay sahipliği hakları ikiye ayrılır: Mali Haklar (Kâr payı/temettü, tasfiye bakiyesi, yeni pay alma/rüçhan hakkı, bedelsiz pay alma hakkı) ve İdari Haklar (Genel kurula katılma, oy kullanma, bilgi alma ve inceleme, iptal davası açma).",
            "Bedelli vs Bedelsiz Sermaye Artırımı: Bedelli artırımda şirketin kasasına ortaklardan yeni nakit para girer, sermaye ve özkaynaklar büyür; rüçhan hakkı kullanım süresi 15 ila 60 gündür. Bedelsiz artırımda ise şirket içi iç kaynaklar (emisyon primi, kâr yedekleri) sermayeye eklenir; şirketin kasasına YENİ NAKİT GİRMEZ, toplam özkaynak değişmez, sadece sermaye kalemi büyür.",
            "Önemli Nitelikteki İşlemler ve Ayrılma Hakkı (Tebliğ II-23.3): Birleşme, bölünme, tür değiştirme veya malvarlığının önemli kısmını devretme gibi işlemlere genel kurulda ret oyu verip muhalefet şerhi düşen pay sahipleri ortaklıktan 'Ayrılma Hakkı'na sahiptir. Başvuru süresi 10 ila 20 İŞ GÜNÜDÜR.",
            "Ayrılma Hakkı Fiyatı Tespiti (2026 Kuralı): İşlemin ilk kez kamuya açıklandığı tarihten önceki; Yıldız Pazar'da işlem gören şirketler için son 1 AYLIK, diğer pazarlarda işlem görenler için son 6 AYLIK düzeltilmiş borsa ağırlıklı ortalama fiyatı uygulanır.",
            "Ortaklıktan Çıkarma ve Satma Hakkı: Hâkim ortak genel kurulda payların ve oy haklarının en az %98'ine ulaştığında, azınlık ortakları şirketten çıkarma hakkına; azınlık ise paylarını hâkim ortağa satma hakkına sahip olur."
        ],
        "concrete_examples": [
            "Örnek 1 (Bedelsiz Sermaye Artırımı Etkisi): Şirket %100 bedelsiz sermaye artırımı yapar. 100 TL fiyatı ve 100 lotu olan yatırımcının elindeki lot sayısı 200'e çıkar, hisse fiyatı ise 50 TL'ye düşer. Yatırımcının toplam portföy değeri 10.000 TL olarak aynı kalır; şirketin kasasına 1 kuruş bile nakit girmez.",
            "Örnek 2 (Ayrılma Hakkı Başvuru Süresi Sınav Sorusu): Halka açık ABC A.Ş. önemli nitelikteki devir işlemi için genel kurul toplar. Muhalif kalan yatırımcı Ayşe Hanım genel kurulda ret oyu verip muhalefetini tutanağa işletir. Şirketin belirlediği ayrılma hakkı kullanım süresi 15 iş günüdür (10-20 iş günü kuralına uygundur). Ayşe Hanım bu süre içinde başvurarak hisselerini şirkete satar."
        ],
        "key_takeaways": [
            "Rüçhan hakkı kullanım süresi: En az 15 gün, en fazla 60 gün.",
            "Ayrılma hakkı başvuru süresi: En az 10 iş günü, en fazla 20 iş günü.",
            "Ayrılma hakkı fiyatı: Yıldız Pazar için son 1 aylık; diğer pazarlar için son 6 aylık borsa ağırlıklı ortalaması.",
            "Ortaklıktan çıkarma ve satma hakkı eşiği: Tam %98 oy hakkıdır."
        ],
        "exam_traps": [
            "⚠️ İŞ GÜNÜ TUZAĞI: Ayrılma hakkı süresi 10-20 takvim günü değil, KANUNEN İŞ GÜNÜDÜR.",
            "⚠️ BEDELSİZ TUZAĞI: 'Bedelsiz sermaye artırımı şirketin likiditesini ve nakit varlıklarını artırır' ifadesi KESİNLİKLE YANLIŞTIR."
        ]
    },
    "sec_1001_05": {
        "title": "5. Sermaye Piyasası Suçları, Cezaları ve Etkin Pişmanlık (m.106 - m.110)",
        "content": [
            "Sermaye piyasasında güveni sarsan en ağır fiiller SPKn m.106-110 arasında adli suç olarak düzenlenmiştir.",
            "Bilgi Suistimali (İçeriden Öğrenenlerin Ticareti - m.106): Henüz kamuya duyurulmamış içsel bilgiyi kullanarak işlem yapıp menfaat temin etmektir. Cezası: 3 YILDAN 5 YILA KADAR HAPİS VE elde edilen menfaatin İKİ KATINDAN AZ OLMAMAK ÜZERE adli para cezasıdır (Hapis 'veya' adli para cezası değil, İKİSİ BİRLİKTE uygulanır!). Bilgi suistimalinde ETKİN PİŞMANLIK HÜKMÜ KANUNEN YOKTUR.",
            "Piyasa Dolandırıcılığı (Manipülasyon - m.107): İki türdür: 1) İşlem Bazlı Manipülasyon (yapay emir verme, kendinden kendine işlem vb.) ve 2) Bilgi Bazlı Manipülasyon (yalan, yanlış, yanıltıcı haber yayma). Cezası: 3 yıldan 5 yıla kadar hapis ve beş bin güne kadar adli para cezasıdır.",
            "İşlem Bazlı Manipülasyonda Etkin Pişmanlık (m.107/3): SPK incelemeye başlamadan önce Kurula ihbarda bulunup elde ettiği menfaatin 2 KATINI Hazineye ödeyen kişi hakkında CEZA VERİLMEZ. İnceleme başladıktan sonra fakat dava açılmadan öderse cezada indirim uygulanır. Bilgi bazlı manipülasyonda ise etkin pişmanlık hükümleri uygulanmaz.",
            "İzinsiz Sermaye Piyasası Faaliyeti (m.109): Kuruldan yetki belgesi almaksızın sermaye piyasasında faaliyette bulunanlar 2 yıldan 5 yıla kadar hapis ve 5.000 günden 10.000 güne kadar adli para cezası ile cezalandırılır.",
            "İdari Para Cezalarında Zamanaşımı: Kurulun idari para cezası verme yetkisi, kabahatin işlendiği tarihten itibaren 5 YIL geçmekle zamanaşımına uğrar."
        ],
        "concrete_examples": [
            "Örnek 1 (İşlem Bazlı Manipülasyonda Etkin Pişmanlık): BIST'te işlem gören sığ bir hissede karşılıklı sahte alım-satım emirleri vererek 2 milyon TL haksız kâr sağlayan bir spekülatör, SPK henüz dosya açıp inceleme başlatmadan önce durumu SPK'ya yazılı itiraf eder ve menfaatin iki katı olan 4 milyon TL'yi Hazineye peşin yatırır. SPKn m.107/3 gereğince hakkında hiçbir adli hapis cezası verilmez.",
            "Örnek 2 (Bilgi Suistimalinde Kümülatif Ceza): Şirketin maden bulduğunu KAP duyurusundan önce öğrenip hisse alan ve 500.000 TL kazanan genel müdür yardımcısı yargılandığında mahkeme; '3 yıl hapis VEYA para cezası' diyemez. Kanun gereği 3 yıldan 5 yıla kadar HAPİS VE en az 1.000.000 TL (menfaatin 2 katı) adli para cezasına BİRLİKTE hükmeder."
        ],
        "key_takeaways": [
            "Bilgi suistimali yaptırımı: 3-5 yıl hapis VE menfaatin en az iki katı adli para cezası (Kümülatiftir).",
            "Bilgi suistimalinde etkin pişmanlık YOKTUR.",
            "İşlem bazlı manipülasyonda SPK incelemesinden önce menfaatin 2 katı ödenirse CEZA VERİLMEZ.",
            "SPK idari para cezalarında zamanaşımı süresi kesin olarak 5 YILDIR."
        ],
        "exam_traps": [
            "⚠️ 'VEYA' TUZAĞI: Şıklarda '3 yıldan 5 yıla kadar hapis veya adli para cezası' yazar; doğrusu 'hapis VE adli para cezası'dır.",
            "⚠️ PİŞMANLIK TUZAĞI: Yalan haber yayarak manipülasyon yapan (bilgi bazlı) kişi parayı ödese dahi etkin pişmanlıktan yararlanamaz; sadece işlem bazlıda geçerlidir."
        ]
    },
    "sec_1001_06": {
        "title": "6. Türkiye Sermaye Piyasaları Birliği (TSPB) ve Disiplin Cezaları Hiyerarşisi",
        "content": [
            "Türkiye Sermaye Piyasaları Birliği (TSPB), kamu kurumu niteliğinde bir meslek kuruluşudur. Bankalar, aracı kurumlar, portföy yönetim şirketleri ve yatırım ortaklıkları Birliğin zorunlu üyesidir.",
            "TSPB Disiplin Cezaları Sıralaması (Hafiften Ağıra): 1. Uyarı -> 2. Kınama -> 3. Para Cezası -> 4. Geçici Olarak Faaliyetten Men -> 5. Sürekli Olarak Faaliyetten Men.",
            "Yetki Ayrımı: Disiplin soruşturmasını TSPB Disiplin Kurulu yürütür ve öneri hazırlar; cezayı verme yetkisi ise TSPB Yönetim Kurulu'na aittir.",
            "Zamanaşımı Hükümleri: Disiplin cezasını gerektiren fiilin öğrenildiği tarihten itibaren 2 YIL ve her halükarda fiilin işlendiği tarihten itibaren 5 YIL içinde soruşturmaya başlanmazsa ceza verme yetkisi zamanaşımına uğrar.",
            "Para Cezalarının Akıbeti: Tahsil edilen disiplin para cezaları Birlik bütçesine irat (gelir) kaydedilir ve mesleki eğitim ile araştırmalarda kullanılır; Hazineye veya müşterilere aktarılmaz."
        ],
        "concrete_examples": [
            "Örnek 1 (Disiplin Cezaları Hiyerarşisi): Görevinde ilk kez usul hatası yaparak müşteri ekstresini geciktiren bir uzmana 'Uyarı' cezası verilirken; güveni kötüye kullanıp müşterinin parasını zimmetine geçiren personel hakkında meslekten ihraç anlamına gelen 'Sürekli Faaliyetten Men' cezası uygulanır.",
            "Örnek 2 (Zamanaşımı Süresi Hesabı): 2020 yılında işlenen bir meslek kuralı ihlali TSPB tarafından 2024 yılında (4 yıl sonra) öğrenilmiştir. Öğrenmeden itibaren 2 yıl süre vardır ancak 2025 yılında fiilin üzerinden 5 yıl geçeceği için mutlak 5 yıllık zamanaşımı dolmadan cezanın kesinleşmesi şarttır."
        ],
        "key_takeaways": [
            "TSPB disiplin cezaları: Uyarı, Kınama, Para Cezası, Geçici Men, Sürekli Men.",
            "Disiplin soruşturmasını Disiplin Kurulu yapar; ceza kararını Yönetim Kurulu verir.",
            "Disiplin zamanaşımı: Öğrenmeden 2 yıl, her halükarda fiilden 5 yıldır.",
            "Disiplin para cezaları Birliğe gelir kaydedilir."
        ],
        "exam_traps": [
            "⚠️ SIRALAMA TUZAĞI: Şıklara 'İdari para cezası' veya 'Hapis cezası' konur; TSPB adli ceza veya SPK idari para cezası veremez; sadece Birlik Disiplin Para Cezası verir.",
            "⚠️ YETKİ TUZAĞI: Disiplin cezalarını Disiplin Kurulu değil, Yönetim Kurulu karara bağlar."
        ]
    },
    "sec_1001_07": {
        "title": "7. TTK Anonim Şirketler: Genel Kurul Toplantı ve Karar Yetersayıları (Nisaplar) ile Kayıtlı Sermaye Sistemi",
        "content": [
            "Türk Ticaret Kanunu (TTK) ve SPKn uyarınca anonim şirketlerin genel kurullarında farklı kararlar için farklı toplantı ve karar nisapları aranır.",
            "Olağan Genel Kurul Toplantı Nisabı: Sermayenin en az dörtte birini (%25) temsil eden pay sahiplerinin katılımıyla toplanır. Kararlar katılanların oy çoğunluğuyla alınır. İlk toplantıda %25 bulunamazsa, ikinci toplantıda asgari bir nisap aranmaksızın mevcut olanlarla toplanılır.",
            "Ağırlaştırılmış Nisaplar: Şirketin işletme konusunun tamamen değiştirilmesi veya sermaye artırımı/azaltımı gibi esas sözleşme değişikliklerinde sermayenin en az %50'si aranır. Bilanço zararlarının kapatılması veya şirket merkezinin yurt dışına taşınmasında ise sermayenin %100'ünün oybirliği şarttır.",
            "Kayıtlı Sermaye Sistemi: Yönetim kuruluna, genel kurul kararına gerek kalmaksızın tavan sınırına kadar sermayeyi artırma yetkisi tanıyan sistemdir. SPK'dan izin alınarak geçilir. Tavan için izin süresi en fazla 5 YILDIR. 5 yıl dolduğunda genel kuruldan ve SPK'dan yeni yetki alınmalıdır; yönetim kurulu tavanı kendiliğinden uzatamaz."
        ],
        "concrete_examples": [
            "Örnek 1 (Olağan Genel Kurul Nisap Hesabı): Sermayesi 100 milyon TL olan bir anonim ortaklığın olağan genel kurul yapabilmesi için ilk toplantıda en az 25 milyon TL'lik (%25) pay sahibinin asaleten veya vekaleten hazır bulunması zorunludur. 24 milyon TL olursa toplantı açılamaz ve ertelenir.",
            "Örnek 2 (Kayıtlı Sermaye Tavan Süresi): ABC A.Ş.'nin 2021 yılında onaylanan 500 Milyon TL kayıtlı sermaye tavanı izni 2026 yılı sonunda dolmaktadır. 2027 yılında yönetim kurulu 'Eski yetkimiz vardı' diyerek tek taraflı sermaye artıramaz; genel kurulu toplayıp yeni bir 5 yıllık yetki süresi almak ve SPK'ya onaylatmak zorundadır."
        ],
        "key_takeaways": [
            "Olağan genel kurul toplantı nisabı: Sermayenin en az %25'idir (Dörtte bir).",
            "Kayıtlı sermaye tavanı izin süresi: En fazla 5 YILDIR.",
            "Tavan süresi dolunca yönetim kurulu yetkiyi re'sen uzatamaz; genel kurul ve SPK onayı şarttır.",
            "Anonim şirket kuruluşunda nakdi sermayenin en az %25'i tescilden önce ödenmeli, kalanı 24 ayda tamamlanmalıdır."
        ],
        "exam_traps": [
            "⚠️ İKİNCİ TOPLANTI TUZAĞI: Olağan genel kurulun ikinci toplantısında %25 nisap aranmaz, katılanlarla karar alınır.",
            "⚠️ TAVAN UZATMA TUZAĞI: 5 yıllık süre dolduğunda şirket sistemden çıkmış sayılmaz; sadece genel kuruldan yetki almadan yönetim kurulu sermaye artıramaz."
        ]
    },

    # =========================================================================
    # MODÜL 1003: SERMAYE PİYASASI ARAÇLARI 1
    # =========================================================================
    "sec_1003_01": {
        "title": "1. Paylar (Hisse Senetleri), Hukuki Haklar ve Oyda İmtiyaz Sınırı (15 Oy)",
        "content": [
            "Hisse senedi (Pay), anonim ortaklığın sermayesinin belirli bir parçasını temsil eden, sahibine ortaklık ve mülkiyet hakları sağlayan kıymetli evraktır.",
            "Oyda İmtiyaz Sınırı (SPKn m.18): Halka açık anonim ortaklıklarda, pay sahiplerine tanınabilecek oy imtiyazı kural olarak 1 paya en fazla 15 OY HAKKI ile sınırlandırılmıştır.",
            "İmtiyazın Geçersiz Olduğu Haller (Sınavın Favori Sorusu): Oyda imtiyaz hakkı; 1) Esas sözleşme değişikliklerinde ve 2) Yönetim kurulunun ibrası ile sorumluluk davası açılması oylamalarında KESİNLİKLE KULLANILAMAZ. Bu oylamalarda her pay yalnızca 1 oy hakkına sahip olur.",
            "Nama ve Hamiline Payların Kaydileştirilmesi: Borsa İstanbul'da işlem gören tüm paylar MKK nezdinde hak sahipleri adına kayden izlenir. Pay devirleri fiziki teslim veya pay defteriyle değil, MKK kaydi hesapları arasında aktarımla tamamlanır."
        ],
        "concrete_examples": [
            "Örnek 1 (Oyda İmtiyaz Sınav Senaryosu): Halka açık bir şirkette (A) grubu payların 1 paya 15 oy hakkı, (B) grubu payların 1 oy hakkı vardır. Genel kurulda yönetim kurulu üyelerinin aklanması (ibrası) oylanırken (A) grubu pay sahibi 15 oy kullanamaz; kanun gereği oyu 1 oy olarak sayılır.",
            "Örnek 2 (Hisse Bölünmesi - Stock Split): 1 hissesi 200 TL olan yatırımcının hissesi 1'e 2 bölündüğünde; hisse sayısı 2 kata çıkar (1'den 2'ye), fiyatı yarıya iner (100 TL). Toplam piyasa değeri ve şirketteki oy gücü oranı KESİNLİKLE DEĞİŞMEZ."
        ],
        "key_takeaways": [
            "Halka açık ortaklıklarda 1 paya tanınabilecek azami oy hakkı: En fazla 15 oydur.",
            "Esas sözleşme değişikliği ve yönetim kurulunun ibrasında imtiyaz kullanılamaz.",
            "Hisse bölünmesinde (Stock split) şirketin toplam piyasa değeri ve özkaynakları değişmez.",
            "Halka açık payların geçerli devri MKK kaydi hesap aktarımıyla gerçekleşir."
        ],
        "exam_traps": [
            "⚠️ İBRA TUZAĞI: Sınavda 'Hâkim ortak imtiyazlı 15 oyuyla kendisini ibra etti' derse bu işlem KANUNEN HUKUKSUZDUR.",
            "⚠️ BÖLÜNME TUZAĞI: Hisse bölünmesi şirketin sermayesini artırmaz veya şirketin kasasına nakit sokmaz."
        ]
    },
    "sec_1003_02": {
        "title": "2. Borçlanma Araçları: Tahviller, Finansman Bonoları, Temiz/Kirli Fiyat ve Birikmiş Faiz Hesabı",
        "content": [
            "Borçlanma araçları, ihraççının borçlu, yatırımcının alacaklı olduğu menkul kıymetlerdir. Tahvil sahibi şirketin ortağı değildir; kâra-zarara katılmaz, genel kurulda oy kullanamaz; sadece faiz ve anaparasını alır.",
            "Vade Sınırları Ayrımı: Finansman Bonoları kısa vadeli borçlanma araçlarıdır; vadeleri en az 30 GÜN, en fazla 365 GÜNDÜR (1 yıl). Tahviller ise vadeleri 1 YIL (365 gün) ve daha uzun olan orta ve uzun vadeli borçlanma araçlarıdır.",
            "Temiz Fiyat vs Kirli Fiyat (Sınavın Altın Formülü):",
            "1) Temiz Fiyat (Clean Price): Tahvilin birikmiş faizi HARİÇ piyasa fiyatıdır. Borsa İstanbul Borçlanma Araçları Piyasası ekranlarında kote edilen fiyattır.",
            "2) Kirli Fiyat (Dirty Price): Takasta alıcının satıcıya cebinden çıkarıp fiilen ödediği tutardır. Formül: Kirli Fiyat = Temiz Fiyat + Birikmiş Faiz.",
            "3) Birikmiş Faiz Formülü: Birikmiş Faiz = Nominal Değer x Kupon Oranı x (Son Kupondan Geçen Gün / 365). Kupon ödeme gününde geçen gün sıfır olduğundan Temiz Fiyat = Kirli Fiyat olur!"
        ],
        "concrete_examples": [
            "Örnek 1 (Adım Adım Kirli Fiyat Hesabı):",
            "Nominal Değeri: 1.000 TL, Yıllık Kupon Oranı: %20, Son kupondan bu yana geçen gün: 90 gün, Borsa Ekranındaki Temiz Fiyat: 1.020 TL.",
            "Adım 1: Birikmiş Faiz = 1.000 x 0,20 x (90 / 365) = 49,31 TL.",
            "Adım 2: Kirli Fiyat = 1.020 + 49,31 = 1.069,31 TL. Alıcı takasta satıcıya tam 1.069,31 TL öder!",
            "Örnek 2 (Bono ile Tahvil Karşılaştırması): Bir banka 6 ay (180 gün) vadeli borçlanmak istediğinde Finansman Bonosu ihraç eder (İskontolu satılır). 3 yıl vadeli borçlanmak istediğinde ise kuponlu Tahvil ihraç eder."
        ],
        "key_takeaways": [
            "Finansman bonosu vadesi: 30 gün ila 365 gün (1 yıldan kısa).",
            "Tahvil vadesi: 1 yıl (365 gün) ve üzeri.",
            "Borsa ekranında kote edilen fiyat: TEMİZ FİYAT.",
            "Takasta fiilen ödenen nakit bedel: KİRLİ FİYAT (Temiz + Birikmiş Faiz).",
            "Kupon gününde Birikmiş Faiz = 0 olduğu için Temiz Fiyat = Kirli Fiyat olur."
        ],
        "exam_traps": [
            "⚠️ FORMÜL TUZAĞI: 'Kirli Fiyat = Temiz Fiyat - Birikmiş Faiz' değildir; BİRİKMİŞ FAİZ DAİMA EKLENİR.",
            "⚠️ OY HAKKI TUZAĞI: Tahvil sahipleri şirketin genel kurulunda söz alıp oy kullanamazlar; sadece alacaklıdırlar."
        ]
    },
    "sec_1003_03": {
        "title": "3. Yatırım Fonları, TEFAS, Borsa Yatırım Fonları (BYF / ETF) ve Serbest Fonlar (10M TL)",
        "content": [
            "Yatırım Fonu, inançlı mülkiyet esasına göre tasarruf sahiplerinden toplanan paralarla oluşturulan portföyü temsil eden malvarlığıdır. Tüzel kişiliği yoktur; Portföy Yönetim Şirketleri (PYŞ) tarafından yönetilir.",
            "Borsa Yatırım Fonları (BYF / ETF - %95 Kuralı): Bir endeksi baz alan, katılma payları Borsa İstanbul Pay Piyasası'nda gün boyu HİSSE SENEDİ GİBİ anlık piyasa fiyatıyla alınıp satılan fonlardır. Portföy değeri ile takip ettiği endeks arasındaki korelasyon en az %95 (0,95) olmak zorundadır.",
            "Geleneksel Fonlar ile BYF Ayrımı: Geleneksel fonlar günde 1 kez açıklanan pay fiyatından TEFAS üzerinden alınıp satılırken; BYF'ler seans içinde borsa emir defterinde sürekli müzayedeyle hisse gibi alınıp satılır.",
            "Para Piyasası Fonları (PPF) Vade Kısıtlamaları: Portföyün günlük hesaplanan ağırlıklı ortalama vadesi en fazla 45 GÜNDÜR. Portföye vadesine 184 günden uzun kalan araç alınamaz.",
            "Serbest Fonlar (Hedge Funds) ve 2026 Nitelikli Yatırımcı Eşiği: Serbest Fon, Gayrimenkul Yatırım Fonu (GYF) ve Girişim Sermayesi Yatırım Fonu (GSYF) katılma payları YALNIZCA Nitelikli Yatırımcılara satılabilir. SPK'nın güncel kararı gereğince bireysel nitelikli yatırımcı finansal varlık eşiği 10 MİLYON TL'DİR (Eski 1 Milyon TL kuralı kaldırılmıştır!)."
        ],
        "concrete_examples": [
            "Örnek 1 (Borsa Yatırım Fonu İşlemi): Yatırımcı Selin Hanım, BIST 30 endeksine yatırım yapmak ister. 30 farklı hisseyi tek tek almak yerine, BIST 30 endeksini izleyen bir BYF payını tıpkı hisse senedi alır gibi saat 14:30'da borsadaki anlık piyasa fiyatından satın alır.",
            "Örnek 2 (Serbest Fon 10 Milyon TL Sınav Senaryosu): Banka şubesine giden bir yatırımcının 4 milyon TL mevduatı vardır. Banka bu müşteriye Serbest Yatırım Fonu satamaz; çünkü müşteri güncel 10 Milyon TL Nitelikli Yatırımcı finansal varlık şartını sağlamamaktadır."
        ],
        "key_takeaways": [
            "BYF (ETF) payları seans boyunca hisse senedi gibi anlık fiyattan işlem görür.",
            "BYF ile baz endeks arasındaki korelasyon katsayısı: En az %95 (0,95).",
            "Para Piyasası Fonu ağırlıklı ortalama vadesi: Azami 45 gün (max vade 184 gün).",
            "Hisse senedi yoğun fon portföy asgari hisse oranı: En az %80.",
            "Serbest Fon satın alma eşiği: Kesinlikle 10 MİLYON TL (Nitelikli Yatırımcı)."
        ],
        "exam_traps": [
            "⚠️ 10 MİLYON TL TUZAĞI: Serbest fon ve nitelikli yatırımcı sorularında şıklarda 1 Milyon TL görürseniz işaretlemeyin; güncel sınır 10 MİLYON TL'dir.",
            "⚠️ KORELASYON TUZAĞI: BYF endeks takip korelasyonu %90 değil, en az %95'tir."
        ]
    },
    "sec_1003_04": {
        "title": "4. Gayrimenkul Yatırım Ortaklıkları (GYO - %51 Kuralı) ve Girişim Sermayesi (GSYF / GSYO)",
        "content": [
            "Gayrimenkul Yatırım Ortaklığı (GYO), gayrimenkullere, gayrimenkul projelerine ve gayrimenkule dayalı haklara yatırım yapan sermaye piyasası kurumudur.",
            "Portföy Sınırlaması (%51 Kuralı): GYO'ların portföy değerinin en az %51'i gayrimenkul, gayrimenkul projeleri ve gayrimenkule dayalı haklardan oluşmak zorundadır.",
            "İnşaat Yapma Yasağı (Sınavın En Popüler Tuzağı): GYO'ların bizzat İNŞAAT YAPMASI, işçi çalıştırıp müteahhitlik üstlenmesi KANUNEN YASAKTIR. GYO arsayı alır, projeyi hazırlar ancak inşaat işini mutlaka üçüncü taraf bağımsız müteahhit firmalara ihale etmek zorundadır.",
            "Vergi Avantajı: GYO'lar kurumlar vergisinden kanunen muaftır (%0 Kurumlar Vergisi öderler).",
            "Girişim Sermayesi (GSYO ve GSYF): Türkiye'de yerleşik, büyüme potansiyeli yüksek ancak sermaye ihtiyacı olan girişim şirketlerine (start-up / KOBİ) özkaynak finansmanı sağlarlar."
        ],
        "concrete_examples": [
            "Örnek 1 (GYO İnşaat Yasağı Sınav Senaryosu): Büyük bir konut projesi geliştirmek isteyen Torunlar GYO, inşaat ruhsatını aldıktan sonra şantiye kurup bizzat duvar öremez veya inşaat işçisi istihdam edemez. İşi sözleşmeyle bir inşaat taahhüt şirketine (müteahhide) anahtar teslim ihale eder.",
            "Örnek 2 (Portföy Oranı Kontrolü): Toplam portföy büyüklüğü 2 Milyar TL olan bir GYO'nun en az 1 Milyar 20 Milyon TL'si (%51) tamamlanmış bina, arsa veya konut projelerinden oluşmalıdır; kalan kısmı repoda veya devlet tahvilinde likidite olarak tutabilir."
        ],
        "key_takeaways": [
            "GYO asgari gayrimenkul portföy oranı: En az %51.",
            "GYO'ların bizzat inşaat müteahhitliği yapması KESİNLİKLE YASAKTIR.",
            "GYO kazançları Kurumlar Vergisinden %100 istisnadır (%0 vergi).",
            "GSYF katılma payları yalnızca Nitelikli Yatırımcılara satılabilir."
        ],
        "exam_traps": [
            "⚠️ İNŞAAT TUZAĞI: 'GYO kendi personeliyle inşaat faaliyetlerini bizzat yürütür' seçeneği HER ZAMAN YANLIŞTIR.",
            "⚠️ VERGİ TUZAĞI: GYO'lar kurumlar vergisi ödemez ancak gayrimenkul alımında tapu harcı ve KDV yükümlülükleri genel hükümlere tabidir."
        ]
    },
    "sec_1003_05": {
        "title": "5. Varlığa Dayalı Menkul Kıymetler (VDMK), İTMK ve Kira Sertifikaları (Sukuk)",
        "content": [
            "Varlığa Dayalı Menkul Kıymetler (VDMK): Kaynak kuruluşun alacakları (tüketici kredileri, leasing alacakları) bilançodan çıkarılarak (Bilanço Dışı - Off Balance Sheet) SPK onaylı Varlık Finansmanı Fonu'na (VFF) devredilir ve menkul kıymetleştirilir.",
            "İpotek Teminatlı Menkul Kıymetler (İTMK) & VTMK: Menkul kıymet ihraççının KENDİ BİLANÇOSUNDA kalmaya devam eder (Bilanço İçi - On Balance Sheet). İhraççının tüm malvarlığı sorumludur; ayrılan teminat havuzu ise kamu koruması altındadır ve ihraççı iflas etse dahi havuz haczedilemez.",
            "Kira Sertifikaları (Sukuk) Tür Ayrımı (2026 Sınavında Kesin Çıkacak Alan):",
            "1) Eser Sözleşmesine Dayalı (İstisna Sukuku): VKŞ'nin işveren, kaynak kuruluşun yüklenici olduğu bir inşaat/üretim eser sözleşmesine dayanır.",
            "2) Alım-Satıma Dayalı (Murabaha Sukuku): Varlığın VKŞ tarafından peşin alınıp vadeli olarak kâr payı eklenerek satılmasına dayanır.",
            "3) Mülkiyete ve Kiralamaya Dayalı (İcara Sukuku): Varlığın satın alınıp kaynak kuruluşa veya üçüncü kişilere kiralanması ve kira gelirinin ödenmesidir.",
            "4) Ortaklığa Dayalı (Mudaraba / Müşareke Sukuku): Emek-sermaye veya sermaye-sermaye kâr-zarar ortaklığına dayanır."
        ],
        "concrete_examples": [
            "Örnek 1 (İstisna Sukuku Örneği): Bir belediye metro veya hastane inşaatı yaptırmak için Varlık Kiralama Şirketi (VKŞ) kurar. VKŞ işveren, belediye ise yüklenici olur; inşaat sözleşmesine dayalı olarak 'Eser Sözleşmesine Dayalı Kira Sertifikası (İstisna)' ihraç edilerek yatırımcılardan fon toplanır.",
            "Örnek 2 (VDMK ile VTMK Ayrımı): Bir banka konut kredisi alacaklarını bilançosundan tamamen çıkartıp Varlık Finansmanı Fonu'na satarsa VDMK ihraç edilmiş olur. Eğer kredileri kendi bilançosunda tutup üzerine teminat şerhi koyarak ihraç yaparsa İTMK ihraç etmiş olur."
        ],
        "key_takeaways": [
            "VDMK = Bilanço dışı (Varlık Finansmanı Fonu mülkiyetindedir).",
            "İTMK / VTMK = Bilanço içi (İhraççının bilançosunda teminat havuzudur).",
            "İstisna Sukuku = Eser ve üretim sözleşmesine dayalıdır.",
            "Murabaha Sukuku = Maliyet artı kâr payı ile vadeli alım-satıma dayalıdır.",
            "İcara Sukuku = Kiralamaya dayalıdır."
        ],
        "exam_traps": [
            "⚠️ SUKUK KARIŞTIRMA TUZAĞI: Eser/inşaat sözleşmesi görünce 'İcara' veya 'Sahipliğe dayalı' değil, kesinlikle 'İSTİSNA' seçeneğini işaretleyin.",
            "⚠️ BİLANÇO TUZAĞI: VDMK fonun mülkiyetindedir (bilanço dışı), İTMK ise ihraççı bankanın bilançosundadır."
        ]
    },
    "sec_1003_06": {
        "title": "6. Türev Araçlar, VİOP, Varantlar (Moneyness ve Asli Değer Hesabı)",
        "content": [
            "Türev Araçlar; değeri başka bir dayanak varlığa (pay, endeks, döviz, emtia) bağlı olan finansal sözleşmelerdir.",
            "Vadeli İşlemler (Futures) vs Opsiyon/Varant (Altın Kural):",
            "- Futures Sözleşmesi: İKİ TARAF İÇİN DE ZORUNLULUKTUR. Alıcı da satıcı da vazgeçemez, her iki taraf da Takasbank'a teminat yatırır ve günlük fiyat değişimlerinde Margin Call uygulanır.",
            "- Opsiyon ve Varant: ALICI İÇİN HAK, SATICI İÇİN YÜKÜMLÜLÜKTÜR. Alıcı prim öder, riski sadece ödediği prim kadardır (teminat yatırmaz). Satıcı ise primi alır ama tüm riski üstlenir ve teminat yatırır.",
            "Varantlarda Durumlar (Moneyness) ve Asli Değer (Intrinsic Value) Formülü:",
            "- Alım Varantı (Call): Asli Değer = Max(0, Dayanak Fiyat - Kullanım Fiyatı) x Çarpan.",
            "  * Kârda (In the Money): Spot Fiyat > Kullanım Fiyatı (Asli değer pozitiftir).",
            "  * Başa Baş (At the Money): Spot Fiyat = Kullanım Fiyatı (Asli değer sıfırdır).",
            "  * Zararda (Out of the Money): Spot Fiyat < Kullanım Fiyatı (Asli değer sıfırdır).",
            "- Satım Varantı (Put): Asli Değer = Max(0, Kullanım Fiyatı - Dayanak Fiyat) x Çarpan.",
            "KRİTİK KURAL: Varantlarda Asli Değer ASLA NEGATİF OLAMAZ! Ya pozitiftir ya da sıfırdır."
        ],
        "concrete_examples": [
            "Örnek 1 (Alım Varantı Asli Değer Hesabı):",
            "Dayanak Hisse Fiyatı: 70 TL, Varantın Kullanım Fiyatı: 60 TL, Çarpan: 0,10.",
            "Spot Fiyat (70) > Kullanım Fiyatı (60) olduğu için varant KÂRDA'dır (In the Money).",
            "Asli Değer = (70 - 60) x 0,10 = 10 x 0,10 = 1,00 TL'dir. Eğer hisse 55 TL olsaydı, varant ZARARDA olacaktı ve Asli Değeri -0,50 değil, KESİNLİKLE SIFIR (0 TL) olacaktı!",
            "Örnek 2 (Futures ile Varant Ayrımı): THYAO vadeli sözleşmesi alan yatırımcı hisse düşerse Takasbank'tan Margin Call (teminat tamamlama) çağrısı alır. THYAO alım varantı alan yatırımcı ise en fazla ödediği primi kaybeder; asla Margin Call almaz."
        ],
        "key_takeaways": [
            "Futures = İki taraf için de kanuni zorunluluk (İki taraf da teminat yatırır, margin call var).",
            "Opsiyon/Varant = Alıcı için HAK, satıcı için YÜKÜMLÜLÜK.",
            "Alım varantında Dayanak Fiyat > Kullanım Fiyatı ise varant KÂRDA'dır (In the money).",
            "Varantlarda Asli Değer hiçbir zaman eksi (negatif) olamaz; minimum değeri sıfırdır.",
            "Varant Piyasa Değeri = Asli Değer + Zaman Değeri."
        ],
        "exam_traps": [
            "⚠️ ASLİ DEĞER TUZAĞI: Şıklarda 'Hisse fiyatı kullanım fiyatının altına düşerse varantın asli değeri negatif olur' der; YANLIŞTIR, asli değer SIFIR olur.",
            "⚠️ MARGİN CALL TUZAĞI: Varant satın alan yatırımcıya asla margin call (teminat tamamlama) gelmez."
        ]
    },
    "sec_1003_07": {
        "title": "7. Pay Benzeri Menkul Kıymetler (PDT, DET, KİS) ve Varant Risk Göstergeleri (Greeks)",
        "content": [
            "Paya Dönüştürülebilir Tahvil (PDT) vs Değiştirilebilir Tahvil (DET):",
            "- PDT (Paya Dönüştürülebilir): Vadesinde veya belirli dönemlerde tahvili çıkaran şirketin KENDİ PAYLARINA dönüşür.",
            "- DET (Değiştirilebilir Tahvil): İhraççı şirketin değil, ihraççının portföyündeki BAŞKA BİR ŞİRKETİN (örneğin iştirakinin) paylarıyla değiştirilir.",
            "Katılma İntifa Senetleri (KİS - Sınavın Favori Sorusudur): Ortaklık esas sermayesini temsil etmez. Sahibine kârdan pay alma, tasfiye artığından pay alma ve rüçhan hakkı verir. ANCAK GENEL KURULDA OY HAKKI VE YÖNETİME KATILMA HAKKI KESİNLİKLE VERMEZ.",
            "Varant Risk Göstergeleri (Greeks):",
            "- Delta: Dayanak varlık fiyatı 1 TL değiştiğinde varant fiyatının kaç TL değişeceğini gösterir (Alım varantında 0 ile +1, satım varantında -1 ile 0 arasındadır).",
            "- Gama: Dayanak varlık fiyatı değiştiğinde Delta'nın ne kadar değişeceğini ölçer.",
            "- Teta: Vadeye kalan gün sayısı azaldıkça varantın her gün uğradığı zaman aşınması (değer kaybı) miktarıdır (Teta daima negatiftir).",
            "- Vega: Dayanak varlığın volatilitesi (oynaklığı) %1 değiştiğinde varant fiyatının duyarlılığıdır."
        ],
        "concrete_examples": [
            "Örnek 1 (PDT vs DET Ayrımı): Koç Holding ihraç ettiği tahvili vadesinde Koç Holding payına dönüştürürse bu PDT'dir. Eğer portföyündeki Yapı Kredi veya Ford Otosan paylarıyla değiştirme hakkı tanırsa bu DET'tir.",
            "Örnek 2 (KİS Oy Hakkı Yasağı): Bir anonim şirket başarılı mühendislerine ödül olarak Katılma İntifa Senedi (KİS) verir. Mühendisler her yıl şirketin kârından temettü alırlar ancak genel kurul toplantısında oy kullanamazlar ve yönetim kuruluna üye seçemezler."
        ],
        "key_takeaways": [
            "PDT = İhraççının KENDİ payına dönüşür.",
            "DET = Başka bir şirketin payıyla değiştirilir.",
            "KİS = Mali hak sağlar (kâr, tasfiye), OY HAKKI KESİNLİKLE YOKTUR.",
            "Delta = Dayanak varlık fiyatındaki 1 birimlik değişime varantın tepkisi.",
            "Teta = Zaman aşınması (vade yaklaştıkça değer kaybı)."
        ],
        "exam_traps": [
            "⚠️ KİS OY TUZAĞI: 'KİS sahipleri genel kurulda 1 oy hakkına sahiptir' ifadesi KESİNLİKLE YANLIŞTIR.",
            "⚠️ DET TUZAĞI: DET kendi payına dönüşmez, portföydeki başka şirketin payına dönüşür."
        ]
    },

    # =========================================================================
    # MODÜL 1005: YATIRIM KURULUŞLARI
    # =========================================================================
    "sec_1005_01": {
        "title": "1. Yatırım Hizmetleri, Faaliyetleri ve Yan Hizmetlerin Hukuki Kapsamı",
        "content": [
            "Yatırım Kuruluşları; aracı kurumlar ile yatırım hizmet ve faaliyetinde bulunmak üzere Kurulca yetkilendirilen bankalardır.",
            "Temel Yatırım Hizmet ve Faaliyetleri (6362 sayılı Kanun m.37):",
            "1. Emir İletimine Aracılık (müşteri emrini başka kuruma aktarma),",
            "2. İşlem Aracılığı (müşteri adına ve hesabına borsada işlem yapma),",
            "3. Portföy Aracılığı (kendi nam ve hesabına borsa işlemlerinde karşı taraf olma),",
            "4. Portföy Yöneticiliği (vekil sıfatıyla portföyü yönetme),",
            "5. Yatırım Danışmanlığı (kişiye özel yönlendirici tavsiye verme),",
            "6. Halka Arza Aracılık (en iyi gayret veya yüklenim),",
            "7. Saklama Hizmeti (sınırlı veya genel saklama).",
            "Yan Hizmetler (m.38): Kredili işlem yaptırma, sermaye piyasası araçları için kredi verme, finansman sağlama, yatırım araştırması ve finansal analiz raporları yayımlama, döviz hizmetleri sunmadır.",
            "Önemli Kural: Bankalar 'Portföy Aracılığı' (kendi nam ve hesabına hisse senedi alım satımı) ve 'Gayrimenkul/Girişim Fonu Kuruculuğu' yapamazlar; bu işlemler aracı kurumlar ve PYŞ'ler tarafından yapılır."
        ],
        "concrete_examples": [
            "Örnek 1 (Banka Şubesinde Emir İletimi): X Bankası'nın Anadolu'daki bir şubesine giden müşteri Borsa İstanbul'dan hisse almak istediğinde, banka şubesi 'Emir İletimine Aracılık' lisansıyla bu emri anlaşmalı olduğu aracı kuruma iletir.",
            "Örnek 2 (Portföy Aracılığı): Bir aracı kurumun Borsa İstanbul'da piyasa yapıcı olarak kendi portföyünden kotasyon vermesi ve hisse alıp satması 'Portföy Aracılığı' faaliyetidir."
        ],
        "key_takeaways": [
            "Yatırım kuruluşları = Aracı kurumlar + Yetkili bankalar.",
            "Temel hizmetler 7 adettir (Emir iletimi, işlem aracılığı, portföy aracılığı, portföy yönetimi, yatırım danışmanlığı, halka arz aracılığı, saklama).",
            "Mevduat bankaları hisse senetlerinde portföy aracılığı (kendi namına alım satım) yapamazlar."
        ],
        "exam_traps": [
            "⚠️ BANKA YETKİSİ TUZAĞI: 'Mevduat bankaları Borsa İstanbul Pay Piyasası'nda kendi nam ve hesaplarına hisse senedi alıp satabilir' ifadesi YANLIŞTIR."
        ]
    },
    "sec_1005_02": {
        "title": "2. Aracı Kurum Sınıflandırması ve Asgari Sermaye Tabanları (25M / 75M / 150M TL)",
        "content": [
            "SPK Tebliği (III-39.1) uyarınca aracı kurumlar yapabilecekleri yetkilere göre 3 sınıfa ayrılır ve sahip olmaları gereken asgari özsermaye tutarları kademelidir:",
            "1. Dar Yetkili Aracı Kurum (Asgari Özkaynak: 25 MİLYON TL): Yalnızca emir iletimine aracılık, en iyi gayretle halka arz ve yatırım danışmanlığı yapabilir. Kendi namına işlem YAPAMAZ, kredili hisse ve açığa satış YAPTIRAMAZ, kaldıraçlı işlem (forex) YAPTIRAMAZ.",
            "2. Kısmi Yetkili Aracı Kurum (Asgari Özkaynak: 75 MİLYON TL): İşlem aracılığı, en iyi gayretle halka arz, sınırlı saklama ve kredili işlem yaptırabilir. Portföy aracılığı ve bakiye yüklenimi YAPAMAZ.",
            "3. Geniş Yetkili Aracı Kurum (Asgari Özkaynak: 150 MİLYON TL): Tüm yatırım hizmet ve faaliyetlerini (portföy aracılığı, tümünü/bakiye yüklenim halka arz, genel saklama, forex) yapmaya tam yetkilidir."
        ],
        "concrete_examples": [
            "Örnek 1 (Dar Yetkili Kurum Kısıtı Sınav Sorusu): Özkaynağı 30 milyon TL olan Dar Yetkili bir aracı kuruma giden müşteri kredili hisse senedi hesabı açmak ister. Kurum bu işlemi yapamaz; çünkü kredili işlem ve açığa satış yaptırabilmek için en az Kısmi Yetkili (75 Milyon TL) olmak şarttır.",
            "Örnek 2 (Yüklenimli Halka Arz): Bir şirketin satılamayan halka arz paylarının tamamını peşin satın alma taahhüdü (Bakiye/Tümünü Yüklenim) verebilmek için aracı kurumun kesinlikle Geniş Yetkili (150 Milyon TL) olması zorunludur."
        ],
        "key_takeaways": [
            "Dar Yetkili Aracı Kurum asgari özkaynak: 25 Milyon TL.",
            "Kısmi Yetkili Aracı Kurum asgari özkaynak: 75 Milyon TL.",
            "Geniş Yetkili Aracı Kurum asgari özkaynak: 150 Milyon TL.",
            "Kendi hesabına hisse alım satımı (portföy aracılığı) yalnızca GENİŞ YETKİLİ aracı kurumlarca yapılabilir."
        ],
        "exam_traps": [
            "⚠️ KREDİLİ İŞLEM TUZAĞI: Dar yetkili aracı kurumlar kredili menkul kıymet işlemi yaptıramaz.",
            "⚠️ YÜKLENİM TUZAĞI: Kısmi yetkili kurumlar sadece 'en iyi gayret' aracılığı yapabilir, yüklenim taahhüdü veremez."
        ]
    },
    "sec_1005_03": {
        "title": "3. Müşteri Sınıflandırması: Genel Müşteri vs Profesyonel Müşteri & 2026 Nitelikli Yatırımcı Eşiği (10 Milyon TL)",
        "content": [
            "Yatırım kuruluşları hizmet vermeden önce müşterilerini iki ana kategoriye ayırmak zorundadır: 1) Genel Müşteri ve 2) Profesyonel Müşteri.",
            "Kendiliğinden Profesyonel Sayılanlar: Bankalar, aracı kurumlar, sigorta şirketleri, emeklilik fonları, yatırım fonları, SPK lisanslı portföy yönetim şirketleri vb.",
            "Kurumsal Müşterilerin Talebe Dayalı Profesyonellik Şartları: Bu 3 kriterden EN AZ İKİSİNİ sağlamalıdır: 1) Aktif toplamı en az 50 Milyon TL, 2) Yıllık net hasılatı en az 90 Milyon TL, 3) Özkaynakları en az 4,5 Milyon TL.",
            "Bireysel Müşterilerin Talebe Dayalı Profesyonellik Şartları (2026 GÜNCEL MEVZUAT): Bireysel bir müşterinin profesyonel müşteri (ve dolayısıyla NİTELİKLİ YATIRIMCI) sayılabilmesi için:",
            "1. Nakit mevduat ve sermaye piyasası araçları toplamının EN AZ 10 MİLYON TL olması KANUNİ ŞARTTIR (Eski 1 Milyon TL kuralı kaldırılmıştır!).",
            "2. Ayrıca şu iki şarttan en az birini sağlamalıdır: Ya son 1 yılda her 3 aylık dönemde en az 500.000 TL hacimli 10 işlem yapmış olmak YA DA finans sektöründe en az 2 yıl tecrübeye sahip olmak.",
            "Serbest Fon Bağlantısı: Serbest Yatırım Fonları (Hedge Funds), Girişim Sermayesi (GSYF) ve Gayrimenkul Yatırım Fonları (GYF) katılma payları YALNIZCA bu 10 Milyon TL eşiğini sağlayan Nitelikli Yatırımcılara satılabilir!"
        ],
        "concrete_examples": [
            "Örnek 1 (Bireysel Profesyonel Müşteri Hesabı): Mehmet Bey'in bankada 12 Milyon TL hisse ve mevduatı vardır. Ayrıca son 1 yılda her çeyrekte 600.000 TL'lik 10 borsa işlemi yapmıştır. Mehmet Bey aracı kuruma yazılı başvurarak 'Profesyonel Müşteri' statüsü alır ve Serbest Fon satın alabilir.",
            "Örnek 2 (Eski Eşik Tuzağı): 2 Milyon TL birikimi olan Can Bey serbest fon almak ister. Bankacı eski bilgiyle '1 Milyon TL'yi geçtiniz alabilirsiniz' diyemez; çünkü güncel Kurul Kararı gereğince bireysel nitelikli yatırımcı eşiği tam 10 MİLYON TL'dir."
        ],
        "key_takeaways": [
            "Bireysel Nitelikli Yatırımcı finansal varlık alt sınırı: Kesinlikle 10 MİLYON TL.",
            "Kurumsal profesyonellik için 3 şarttan (Aktif 50M, Satış 90M, Özkaynak 4.5M) en az 2'si aranır.",
            "Genel müşterilere sağlanan kamusal koruma (risk bildirim formu, sözleşme zorunlulukları) en üst seviyededir.",
            "Serbest Fonlar ve GSYF'ler yalnızca Nitelikli Yatırımcılara ihraç edilebilir."
        ],
        "exam_traps": [
            "⚠️ 10 MİLYON TL TUZAĞI: Sınav komisyonunun bu dönem en çok test edeceği soru 10 Milyon TL Nitelikli Yatırımcı ve Serbest Fon eşiğidir. Asla 1 Milyon TL şıkkını işaretlemeyin.",
            "⚠️ ÜÇ ŞART TUZAĞI: Kurumsal profesyonellikte üç şartın üçü birden değil, en az ikisi yeterlidir."
        ]
    },
    "sec_1005_04": {
        "title": "4. Uygunluk Testi (Suitability) vs Yerindelik Testi (Appropriateness)",
        "content": [
            "Yatırımcıyı korumak ve yanlış ürün satışını engellemek için iki ayrı test mekanizması uygulanır:",
            "1. Uygunluk Testi (Suitability): Alım-satım aracılığı ve halka arza aracılık hizmetlerinde genel müşterilere uygulanır. Yatırımcının YALNIZCA BİLGİ VE TECRÜBESİNİ ölçer. Müşterinin talep ettiği ürünün riskini anlayıp anlayamayacağını tespit eder. Müşteri testte başarısız olsa bile, riskleri yazılı kabul ettiğini beyan ederse işlem yine de yapılabilir.",
            "2. Yerindelik Testi (Appropriateness): Portföy Yöneticiliği ve Yatırım Danışmanlığı hizmetlerinde uygulanması KANUNEN ZORUNLUDUR. Bilgi ve tecrübeye ek olarak; müşterinin MALİ GÜCÜNÜ (gelir düzeyi, malvarlığı) ve YATIRIM AMACINI (risk toleransı, vade tercihi) ölçer.",
            "KRİTİK FARK: Müşteri yerindelik testini doldurmaktan kaçınır veya mali durumunu açıklamazsa, yatırım kuruluşu o müşteriye Portföy Yöneticiliği veya Yatırım Danışmanlığı hizmeti KESİNLİKLE VEREMEZ (Hizmet reddedilir!)."
        ],
        "concrete_examples": [
            "Örnek 1 (Uygunluk Testi): İlk defa borsa hesabı açan Ali Bey VİOP'ta işlem yapmak ister. Yapılan uygunluk testinde türev ürün bilgisi yetersiz çıkar. Aracı kurum Ali Bey'e 'Bu ürün sizin için uygun değildir' uyarısı verir. Ali Bey bu riski yazılı kabul ederse kurum emri piyasaya iletebilir.",
            "Örnek 2 (Yerindelik Testi): Ayşe Hanım 5 milyon TL'sini yönetmesi için bir portföy yönetim şirketine gider ancak 'Aylık gelirimi ve diğer malvarlığımı açıklamam' diyerek formu doldurmaz. Kurum kanun gereği Ayşe Hanım ile Portföy Yönetim Sözleşmesi İMZALAYAMAZ; hizmeti derhal reddetmek zorundadır."
        ],
        "key_takeaways": [
            "Uygunluk Testi = Sadece Bilgi ve Tecrübe ölçer (Alım-satım aracılığında uygulanır).",
            "Yerindelik Testi = Bilgi + Mali Güç + Yatırım Amacı ölçer (Portföy yönetimi ve danışmanlıkta uygulanır).",
            "Yerindelik testi yapılmadan veya bilgi verilmeden portföy yöneticiliği KESİNLİKLE YAPILAMAZ.",
            "Profesyonel müşterilere uygunluk testi yapılması zorunlu değildir."
        ],
        "exam_traps": [
            "⚠️ HİZMET VERME TUZAĞI: 'Müşteri mali durumunu açıklamazsa kurum kendi takdiriyle portföy yönetebilir' seçeneği KESİNLİKLE YANLIŞTIR; hizmet verilemez.",
            "⚠️ KAPSAM TUZAĞI: Uygunluk testi mali gücü ölçmez; mali güç yalnızca yerindelik testinde ölçülür."
        ]
    },
    "sec_1005_05": {
        "title": "5. Kredili Menkul Kıymet Alımı, Açığa Satış ve Özkaynak Oranları (%35 / %20)",
        "content": [
            "Kredili Menkul Kıymet İşlemleri; müşterinin hesabındaki özkaynağın belirli bir katı kadar aracı kurum kredisi kullanarak hisse senedi almasıdır.",
            "Asgari Başlangıç Özkaynak Oranı: Kredili işlem pozisyonu açılırken yatırılması gereken asgari özkaynak oranı KESİN OLARAK %35'TİR (Kaldıraç yaklaşık 1'e 2,85).",
            "Asgari Sürdürme Özkaynak Oranı: Piyasa düşüp portföy değer kaybettiğinde özkaynak oranının inebileceği en alt yasal sınır %20'DİR.",
            "Özkaynak Tamamlama Çağrısı (Margin Call) & HEDEF SEVİYE TUZAĞI:",
            "Müşterinin özkaynak oranı %20'nin altına düşerse aracı kurum T+1 iş günü içinde teminat tamamlama çağrısı yapar. Müşterinin tamamlaması gereken hedef oran %20 değil, en baştaki BAŞLANGIÇ SEVİYESİ (%35)'TİR!",
            "Açığa Satış: Sahip olunmayan hissenin ödünç alınarak satılmasıdır. Başlangıç özkaynağı kural olarak en az %50, sürdürme özkaynağı %20'dir."
        ],
        "concrete_examples": [
            "Örnek 1 (Adım Adım Özkaynak ve Tamamlama Hesabı):",
            "Müşteri 35.000 TL nakit koyar, 65.000 TL kredi çeker ve 100.000 TL'lik hisse alır (Özkaynak Oranı: 35/100 = %35).",
            "Hisselerin değeri düşerek 70.000 TL'ye iner. Kredi borcu 65.000 TL sabit kaldığı için müşterinin kalan özkaynağı: 70.000 - 65.000 = 5.000 TL olur.",
            "Yeni Özkaynak Oranı: 5.000 / 70.000 = %7,14'tür. Bu oran %20 sürdürme sınırının altına indiği için kurum çağrı yapar.",
            "Müşteri hesabını %20'ye (14.000 TL) değil; portföyün %35'i olan 24.500 TL özkaynağa tamamlamak için aradaki 19.500 TL'yi yatırmak zorundadır!",
            "Örnek 2 (Re'sen Tasfiye): Müşteri verilen T+1 iş günü sürede parayı yatırmazsa aracı kurum mahkeme kararı aramaksızın re'sen hisseleri piyasa fiyatından satarak kredi borcunu tahsil eder."
        ],
        "key_takeaways": [
            "Kredili işlem asgari başlangıç özkaynak oranı: %35.",
            "Kredili işlem asgari sürdürme özkaynak oranı: %20.",
            "Özkaynak tamamlama çağrısında hedef seviye: Tekrar %35 başlangıç seviyesidir.",
            "Süresinde tamamlanmayan pozisyonlar aracı kurumca re'sen tasfiye edilir."
        ],
        "exam_traps": [
            "⚠️ HEDEF ORAN TUZAĞI: Sınavda 'Müşteri özkaynağını %20'ye tamamlar' der; KESİNLİKLE YANLIŞTIR, %35'e tamamlar.",
            "⚠️ DAR YETKİLİ TUZAĞI: Dar yetkili aracı kurumlar kredili işlem ve açığa satış yaptıramaz."
        ]
    },
    "sec_1005_06": {
        "title": "6. Kaldıraçlı Alım Satım (Forex / FX) İşlemleri ve Yasal Kaldıraç Sınırı (1:10)",
        "content": [
            "Kaldıraçlı Alım Satım İşlemleri (Forex), döviz, kıymetli maden ve emtiaların belirli bir teminat karşılığında katlarıyla işlem görmesidir.",
            "Yasal Azami Kaldıraç Sınırı: Türkiye'de yerleşik bireysel müşteriler için uygulanabilecek azami yasal kaldıraç oranı 1:10'DUR (Bire ona kadar). Yurt dışındaki 1:100 veya 1:400 gibi kaldıraç oranları Türkiye'de kanunen yasaktır.",
            "Asgari Başlangıç Teminatı: Kaldıraçlı işlemlere başlayabilmek için yatırılması gereken asgari nakit teminat tutarı 50.000 TL veya muadili konvertibl yabancı para birimidir.",
            "Yetki Kuralı: Kaldıraçlı işlem yaptırma yetkisi yalnızca SPK lisanslı GENİŞ YETKİLİ ARACI KURUMLARA aittir; bankalar veya dar yetkili kurumlar forex işletemez.",
            "Kâr Garantisi Yasağı: Aracı kurumların veya çalışanlarının müşteriye kesin kâr garantisi vermesi, zararı tazmin taahhüdünde bulunması kanunen suçtur."
        ],
        "concrete_examples": [
            "Örnek 1 (Kaldıraç Hesabı): Hesabında 50.000 TL başlangıç teminatı olan yatırımcı, 1:10 azami kaldıraç sayesinde en fazla 500.000 TL değerinde döviz pozisyonu açabilir. Eğer pozisyon aleyhe %10 hareket ederse müşterinin tüm teminatı sıfırlanır.",
            "Örnek 2 (İzinsiz Yurt Dışı Forex): Yurt dışındaki bir kurum Türkiye'deki vatandaşa 'Bizde 1:200 kaldıraç var, 100 dolarla başla' diyerek işlem yaptırırsa; SPK bu sitelere doğrudan erişim engeli koyar ve aracılık edenler hakkında izinsiz faaliyet suçu (2-5 yıl hapis) davası açılır."
        ],
        "key_takeaways": [
            "Bireysel müşteriler için azami yasal kaldıraç: 1:10.",
            "Asgari başlangıç teminatı: 50.000 TL veya muadili döviz.",
            "Yalnızca Geniş Yetkili Aracı Kurumlar kaldıraçlı işlem yaptırabilir.",
            "Kaldıraçlı işlemlerde kesin kâr taahhüdü verilmesi yasaktır."
        ],
        "exam_traps": [
            "⚠️ KALDIRAÇ TUZAĞI: Şıklarda 1:20 veya 1:50 yazar; bireyseller için yasal sınır 1:10'dur.",
            "⚠️ TEMİNAT TUZAĞI: Asgari teminat 10.000 TL değil, 50.000 TL'dir."
        ]
    },
    "sec_1005_07": {
        "title": "7. Müşteri Varlıklarının Ayrılığı ve Yatırımcı Tazmin Merkezi (YTM)",
        "content": [
            "Müşteri Varlıklarının Korunması İlkesi: Yatırım kuruluşları müşterilerine ait sermaye piyasası araçlarını MKK nezdinde müşteri adına ve müşteri bazında; nakit varlıkları ise Takasbank nezdinde müşteri adına bloke hesaplarda saklamak zorundadır.",
            "Haciz ve İflas Masasına Dahil Edilememe: Müşteri varlıkları, yatırım kuruluşunun kendi borçları nedeniyle haczedilemez, rehnedilemez ve kurum iflas etse dahi iflas masasına DAHİL EDİLEMEZ.",
            "Yatırımcı Tazmin Merkezi (YTM) Kapsamı (Sınavın Altın Kuralı):",
            "- YTM Neyi Tazmin Eder? Yatırım kuruluşunun iflası, tasfiyesi veya personelin zimmeti nedeniyle müşteriye ait hisse senedi ve nakit teslim yükümlülüğünü yerine getirememesi durumunu kanuni üst limit dahilinde tazmin eder.",
            "- YTM Neyi Tazmin ETMEZ? Yatırımcının borsada işlem yaparken hisse fiyatlarının düşmesi, piyasa dalgalanması veya tahvil ihraç eden şirketin batması sonucu uğradığı PİYASA ZARARLARINI ASLA TAZMİN ETMEZ!"
        ],
        "concrete_examples": [
            "Örnek 1 (Aracı Kurum İflası): X Yatırım Menkul Değerler iflas eder. Yatırımcı Mehmet Bey'in aracı kurumdaki 800.000 TL değerindeki hisseleri MKK'da kendi adına kayıtlı olduğu için iflas masasından etkilenmez ve doğrudan başka bir aracı kuruma aktarılır.",
            "Örnek 2 (YTM Tazmin Kapsamı Tuzağı): Borsada bir hisse senedi taban serisi yaparak %70 değer kaybeder ve yatırımcı 300.000 TL zarar eder. Yatırımcı YTM'ye başvurup 'Zararımı devlet karşılasın' diyemez; çünkü YTM piyasa riskini ve hisse değer kaybını asla tazmin etmez."
        ],
        "key_takeaways": [
            "Müşteri hisseleri MKK'da, nakitleri Takasbank'ta müşteri adına saklanır.",
            "Müşteri varlıkları aracı kurumun borcu için haczedilemez ve iflas masasına girmez.",
            "YTM piyasa zararını tazmin etmez; sadece saklamadaki varlıkların teslim edilememesi halini tazmin eder.",
            "Yatırım kuruluşlarında 10 yıl boyunca aranmayan varlıklar doğrudan YTM'ye aktarılır."
        ],
        "exam_traps": [
            "⚠️ TAZMİN TUZAĞI: 'Hisse senedi fiyatı düşen yatırımcının zararını YTM tazmin eder' ifadesi KESİNLİKLE YANLIŞTIR.",
            "⚠️ TAHVİL BATMASI TUZAĞI: İhraç edilen özel sektör tahvili vadesinde ödenmezse YTM bunu tazmin etmez; bu bir kredi riskidir."
        ]
    },
    "sec_1005_08": {
        "title": "8. İç Sistemler, Uyum Görevlisi (Compliance) ve Müşteri Emirlerinin İcrası (En İyi İcra - Best Execution)",
        "content": [
            "İç Sistemler Teşkilatı: Aracı kurumlar faaliyetlerinin güvenli yürütülmesi için 3 temel iç sistem birimi kurmak zorundadır: 1) İç Denetim (Teftiş), 2) İç Kontrol ve 3) Risk Yönetimi.",
            "Uyum Görevlisi (Compliance): Şirketin tüm işlemlerinin SPK mevzuatına, TSPB meslek kurallarına ve MASAK suç gelirlerinin aklanmasının önlenmesi mevzuatına uygunluğunu gözetir. Doğrudan Yönetim Kurulu'na raporlama yapar.",
            "Müşteri Emirlerinin Önceliği İlkesi: Kurumlar ve çalışanlar, müşterinin emrini piyasaya iletmeden önce kendi adlarına veya ilişkili kişiler adına işlem yapamazlar (Front-running yasağı). Müşteri emri her koşulda kurumun ve çalışanın menfaatinden önceliklidir.",
            "Personelin İşlem Kısıtlaması (30 Gün Kuralı): Aracı kurum çalışanları hisse senedi alım satım işlemlerini yalnızca kendi çalıştıkları aracı kurum nezdindeki hesaplarından yapabilirler. Satın aldıkları hisse senetlerini asgari 30 GÜN süreyle elde tutmak zorundadırlar (30 günden önce satamazlar!)."
        ],
        "concrete_examples": [
            "Örnek 1 (Front-Running Yasağı): Kurumsal bir fon müşterisi aracı kurumu arayıp 5 milyon lotluk dev bir hisse alım emri verir. Bu emrin fiyatı yükselteceğini bilen broker, müşteri emrini sisteme girmeden önce kendi hesabına 10.000 lot hisse alırsa bu durum ağır bir suç ve meslek ihlali (Front-running) oluşturur.",
            "Örnek 2 (30 Gün Elde Tutma Kuralı): Aracı kurumda araştırma uzmanı olan Ahmet Bey, çalıştığı kurumdaki hesabından bir BIST hissesi alır. Hisse 5 gün sonra %25 prim yapar. Ahmet Bey 'Kârı realize edeyim' diyerek hisseyi satamaz; çünkü kanun gereği en az 30 gün hesabında tutmak zorundadır."
        ],
        "key_takeaways": [
            "İç sistemler: İç Denetim, İç Kontrol ve Risk Yönetiminden oluşur.",
            "Müşteri emri daima kurumun ve personelin kendi işleminden önce gelir.",
            "Aracı kurum personeli hisse senetlerini yalnızca kendi kurumundan alabilir ve en az 30 gün satamaz.",
            "En İyi İcra ilkesi: Emirler fiyat, maliyet, hız ve takas olasılığı açısından müşteri lehine en iyi şekilde icra edilir."
        ],
        "exam_traps": [
            "⚠️ 30 GÜN TUZAĞI: Personel hisse aldığında 1 hafta veya 15 gün değil, KESİNLİKLE EN AZ 30 GÜN elde tutmak zorundadır.",
            "⚠️ HESAP AÇMA TUZAĞI: Aracı kurum personeli başka bir aracı kurumda gizlice hesap açamaz."
        ]
    },

    # =========================================================================
    # MODÜL 1012: TAKAS, SAKLAMA VE OPERASYON
    # =========================================================================
    "sec_1012_01": {
        "title": "1. Takas ve Saklamanın Temel Esasları & Teslim Karşılığı Ödeme (DVP İlkesi)",
        "content": [
            "Takas ve Saklama Piyasasının İki Ana Kurumu:",
            "1. Takasbank (İstanbul Takas ve Saklama Bankası A.Ş.): Türkiye'nin Merkezi Takas Kuruluşudur.",
            "2. MKK (Merkezi Kayıt Kuruluşu A.Ş.): Türkiye'nin Merkezi Saklama Kuruluşudur.",
            "Teslim Karşılığı Ödeme İlkesi (Delivery Versus Payment - DVP): Menkul kıymet takasında nakit transferi ile menkul kıymet devrinin EŞANLI (aynı anda) ve birbirine bağlı olarak gerçekleşmesidir. Biri teslim edilmedikçe diğeri serbest bırakılmaz.",
            "DVP'nin Amacı: Takas işlemlerinde 'Anapara / Temerrüt Riskini' (yani satıcının parayı alıp hisseyi vermemesi veya alıcının hisseyi alıp parayı ödememesi riskini) tamamen sıfırlamaktır. DVP hissenin borsada düşmesi anlamına gelen piyasa riskini engellemez, sadece takas teslimat riskini yok eder."
        ],
        "concrete_examples": [
            "Örnek 1 (DVP Mantığı): Pazartesi günü borsada 500.000 TL'lik hisse satan Mehmet Bey'in hisseleri MKK'da bloke edilir; alıcı Can Bey'in 500.000 TL nakdi Takasbank'ta bloke edilir. Takas günü geldiğinde sistem iki işlemi aynı milisaniyede eşzamanlı takaslar; biri olmadan diğeri asla gerçekleşmez.",
            "Örnek 2 (DVP Ne İşe Yaramaz?): Yatırımcı hisseyi 100 TL'den alır, hisse T+2 takas gününe kadar 90 TL'ye düşer. Yatırımcı 'DVP vardı niye zarar ettim' diyemez; çünkü DVP fiyat düşüşünü (piyasa riskini) değil, sadece hissenin hesaba güvenle geçmesini garanti eder."
        ],
        "key_takeaways": [
            "Merkezi Takas Kuruluşu: Takasbank.",
            "Merkezi Saklama Kuruluşu: MKK.",
            "DVP ilkesi nakit ve menkul kıymetin eşanlı takas edilmesidir.",
            "DVP'nin temel amacı 'Anapara / Temerrüt Riskini' tamamen ortadan kaldırmaktır."
        ],
        "exam_traps": [
            "⚠️ RİSK TUZAĞI: 'DVP piyasa riskini ortadan kaldırır' ifadesi YANLIŞTIR; DVP takas teslimat (temerrüt) riskini ortadan kaldırır."
        ]
    },
    "sec_1012_02": {
        "title": "2. Borsa İstanbul Piyasaları Standart Takas Süreleri (Valörleri - T+2 / T+0)",
        "content": [
            "Takas Süresi (Valör), borsada işlemin gerçekleştiği gün (T) ile nakit ve menkul kıymet takasının fiilen sonuçlandığı gün arasındaki süredir:",
            "1. Borsa İstanbul Pay Piyasası (Hisse Senetleri): Takas süresi kural olarak T+2'DİR (İşlem gününü izleyen İKİNCİ İŞ GÜNÜ).",
            "2. Borçlanma Araçları Piyasası (Tahvil ve Bono): Takas süresi kural olarak AYNI GÜN (T+0) veya T+1'dir.",
            "3. VİOP (Vadeli İşlem ve Opsiyon Piyasası): Nakit kâr/zarar uzlaşması T+1 GÜNÜ sabahında tamamlanır.",
            "Hafta Sonu ve Tatil Günleri Kuralı: Takas sürelerinde sadece RESMİ İŞ GÜNLERİ sayılır; cumartesi, pazar ve resmi tatiller hesaba katılmaz!"
        ],
        "concrete_examples": [
            "Örnek 1 (Perşembe Yapılan İşlem): Perşembe günü hisse senedi satan yatırımcının parası ne zaman hesaba geçer?",
            "- T = Perşembe,",
            "- T+1 = Cuma,",
            "- Cumartesi ve Pazar iş günü olmadığı için atlanır,",
            "- T+2 = PAZARTESİ günüdür! Takas Pazartesi gerçekleşir.",
            "Örnek 2 (Cuma Yapılan İşlem): Cuma günü hisse satan yatırımcının takası T+1 Pazartesi, T+2 SALI günüdür! Takas Salı günü hesaba geçer."
        ],
        "key_takeaways": [
            "BIST Pay Piyasası standart takas süresi: T+2 (İkinci iş günü).",
            "Tahvil ve Bono Kesin Alım Satım Pazarı: T+0 (Aynı gün) veya T+1.",
            "VİOP nakit uzlaşma süresi: T+1 iş günü sabahı.",
            "Hafta sonları ve resmi tatiller takas süresi hesabına dahil edilmez."
        ],
        "exam_traps": [
            "⚠️ CUMA GÜNÜ TUZAĞI: Cuma günü yapılan pay alımının takası Pazar değil, SALI günüdür.",
            "⚠️ PERŞEMBE GÜNÜ TUZAĞI: Perşembe yapılan pay işleminin takası Cuma değil, PAZARTESİ günüdür."
        ]
    },
    "sec_1012_03": {
        "title": "3. Takasbank Merkezi Karşı Taraf (CCP) Rolü ve Temerrüt Şelalesi (Default Waterfall)",
        "content": [
            "Merkezi Karşı Taraf (Central Counterparty - CCP): Takasbank'ın alıcıya karşı satıcı, satıcıya karşı alıcı konumuna geçerek takasın sonuçlanmasını kendi tüzel kişiliğiyle GARANTİ ETMESİDİR. Bir aracı kurum batsa dahi Takasbank CCP sıfatıyla diğer tarafa hissesini veya parasını öder.",
            "Temerrüt Şelalesi (Default Waterfall - Sınavın Kesin Çıkacak Sıralama Sorusu):",
            "Bir borsa üyesi takas borcunu ödeyemezse Takasbank zararı şu kesin öncelik sırasıyla kapatır:",
            "1. Basamak: Temerrüde düşen borçlu üyenin verdiği teminatlar (nakit, hisse, teminat mektubu),",
            "2. Basamak: Temerrüde düşen borçlu üyenin Garanti Fonu'ndaki katkı payı,",
            "3. Basamak: Takasbank'ın bu amaçla ayırdığı kendi özkaynağı (SITG - Sermaye İçi Temerrüt Güvencesi),",
            "4. Basamak: Temerrüde düşmeyen DİĞER MASUM ÜYELERİN Garanti Fonu katkı payları (zarar oranında paylaştırılır),",
            "5. Basamak: Kalan zarar için Takasbank'ın genel özkaynakları."
        ],
        "concrete_examples": [
            "Örnek 1 (Temerrüt Şelalesi Uygulaması): X Aracı Kurumu 100 milyon TL takas borcunu ödeyemez. Takasbank ilk olarak X Kurumu'nun kendi teminatlarına el koyar (60 milyon TL). Kalan 40 milyon TL için X Kurumu'nun Garanti Fonu payını (10 milyon TL) bozar. Kalan 30 milyon TL için Takasbank kendi SITG özkaynağını devreye sokar. Asla ilk başta diğer masum üyelerin parasına dokunulmaz!",
            "Örnek 2 (CCP Güvencesi): A Kurumu B Kurumu'na hisse satar. Takas gününden önce B Kurumu iflas etse bile, A Kurumu hisse satış bedelini Takasbank'tan kuruşu kuruşuna tahsil eder; çünkü Takasbank Merkezi Karşı Taraftır."
        ],
        "key_takeaways": [
            "Merkezi Karşı Taraf (CCP) = Takasbank'ın takasın sonuçlanmasını garanti etmesidir.",
            "Temerrüt Şelalesi 1. Sıra: Borçlu üyenin kendi teminatlarıdır.",
            "Temerrüt Şelalesi 2. Sıra: Borçlu üyenin Garanti Fonu katkı payıdır.",
            "Temerrüt Şelalesi 3. Sıra: Takasbank'ın kendi temerrüt özkaynağıdır (SITG).",
            "Diğer masum üyelerin Garanti Fonu paylarına en son çare olarak başvurulur."
        ],
        "exam_traps": [
            "⚠️ SIRALAMA TUZAĞI: 'Temerrüt halinde Takasbank doğrudan diğer üyelerin fonunu kullanır' ifadesi YANLIŞTIR; önce borçlunun teminatı, sonra Takasbank özkaynağı devreye girer."
        ]
    },
    "sec_1012_04": {
        "title": "4. Merkezi Kayıt Kuruluşu (MKK), Kaydileştirme ve Hak Sahipliği Sicili",
        "content": [
            "Merkezi Kayıt Kuruluşu (MKK), Türkiye sermaye piyasasında menkul kıymetlerin kaydileştirilerek elektronik ortamda ihraç edildiği, saklandığı ve hak sahiplerinin izlendiği Merkezi Saklama Kuruluşudur.",
            "Kurucu Hukuki Nitelik: MKK nezdinde tutulan kayıtlar alelade bir saklama kaydı değildir; tapu sicili gibi mülkiyetin ispatında kurucu hukuki sicil niteliğindedir.",
            "Tekil Yatırımcı Sicil Numarası: Türkiye'de kaç farklı aracı kurumda veya bankada hesabı olursa olsun, bir yatırımcıya T.C. Kimlik Numarası / Vergi Numarası ile eşleşen tek bir MKK Sicil Numarası üretilir. Tüm hesaplar bu sicil altında merkezi olarak konsolide edilir.",
            "Fiziki Senet Yasağı: Borsa İstanbul'da işlem gören hisse senetlerinin fiziki kupon şeklinde basılması veya elden alınıp satılması kanunen imkansızdır; tüm sistem %100 dijital ve kaydidir."
        ],
        "concrete_examples": [
            "Örnek 1 (Tek Sicil Numarası): Yatırımcı Murat Bey'in İş Yatırım'da, Garanti Yatırım'da ve Yapı Kredi Yatırım'da 3 ayrı hesabı vardır. Murat Bey e-Devlet veya MKK şifresiyle sisteme girdiğinde tek bir MKK Sicil No altında 3 kurumdaki tüm hisselerini tek ekranda topluca görür.",
            "Örnek 2 (Kaydi Hak Sahipliği): Şirket temettü dağıttığında MKK sisteminde kayıtlı hak sahipleri listesini çıkarır ve para doğrudan Takasbank kanalıyla yatırımcıların yatırım hesaplarına aktarılır; kupon ibraz etmeye gerek yoktur."
        ],
        "key_takeaways": [
            "Türkiye'nin Merkezi Saklama Kuruluşu: MKK.",
            "MKK kayıtları kurucu hukuki hak sahipliği sicilidir.",
            "Her yatırımcıya tek bir benzersiz MKK Sicil Numarası verilir.",
            "Borsada işlem gören paylar %100 kaydileştirilmiştir; fiziki teslimat yapılamaz."
        ],
        "exam_traps": [
            "⚠️ KURUM KARIŞTIRMA TUZAĞI: Hak sahipliği sicilini tutan Takasbank değil, MKK'dır. Takasbank takası yapar, MKK saklar ve kaydeder."
        ]
    },
    "sec_1012_05": {
        "title": "5. MKK e-YATIRIMCI Güvenlik Blokajı ve Zamanaşımı Hükümleri (10 Yıl Kuralı)",
        "content": [
            "e-YATIRIMCI (Yatırımcı Bilgi Merkezi): MKK tarafından yatırımcıların kullanımına sunulan web ve mobil platformdur.",
            "Yatırımcı Güvenlik Blokajı: Yatırımcılar e-YATIRIMCI uygulaması üzerinden istedikleri hisse senetlerine 'Yatırımcı Blokajı' koyabilirler. Bu blokaj kaldırılmadığı sürece aracı kurum dahi ilgili hisseleri satamaz, virmanlayamaz ve transfer edemez; bu sistem yatırımcı varlıklarını kötü niyetli personel işlemlerine karşı %100 korur.",
            "Sermaye Piyasasında Zamanaşımı (Altın Kural: 10 YIL):",
            "SPKn m.83 uyarınca; yatırım kuruluşlarında ve ihraççılarda yatırımcılar adına bulunan ve 10 YIL boyunca işlem görmeyen, aranmayan her türlü nakit, temettü ve sermaye piyasası araçları zamanaşımına uğrar.",
            "Zamanaşımına Uğrayan Varlıkların Akıbeti: Zamanaşımına uğrayan varlıklar aracı kuruma kâr KALMAZ, Hazineye devredilmez; kanun gereği doğrudan YATIRIMCI TAZMİN MERKEZİ'NE (YTM) intikal eder."
        ],
        "concrete_examples": [
            "Örnek 1 (e-YATIRIMCI Blokajı): Uzun vadeli temettü yatırımcısı olan Hakan Bey, aldığı Ereğli hisselerini 5 yıl satmayı düşünmemektedir. e-YATIRIMCI uygulamasına girerek hisselerine 'Yatırımcı Blokajı' koyar. Artık aracı kurum personeli sehven veya kasten bu hisseleri satmaya kalksa bile borsa sistemi 'MKK Blokajı Var' uyarısıyla emri reddeder.",
            "Örnek 2 (10 Yıllık Zamanaşımı Hesabı): 2016 yılında hesabında 50.000 TL nakit ve hisse senedi unutan bir yatırımcı, 10 yıl boyunca (2026 yılı sonuna kadar) hiçbir işlem yapmaz ve aramazsa, bu varlıklar zamanaşımına uğrayarak doğrudan YTM hesaplarına devredilir."
        ],
        "key_takeaways": [
            "e-YATIRIMCI blokajı aracı kurumun müşteri rızası olmadan hisse devretmesini engeller.",
            "Sermaye piyasası araçlarında ve nakitlerde zamanaşımı süresi: Kesinlikle 10 YILDIR.",
            "Zamanaşımına uğrayan tüm varlıklar Yatırımcı Tazmin Merkezi'ne (YTM) devredilir."
        ],
        "exam_traps": [
            "⚠️ SÜRE TUZAĞI: Zamanaşımı süresi 5 yıl veya 20 yıl değil, kesin olarak '10 YIL'dır.",
            "⚠️ DEVİR TUZAĞI: Zamanaşımına uğrayan varlıklar Hazineye veya aracı kuruma değil, YTM'ye aktarılır."
        ]
    },
    "sec_1012_06": {
        "title": "6. Takasbank Para Piyasası (TPP) ve Ödünç Pay Piyasası (ÖPA)",
        "content": [
            "Takasbank Para Piyasası (TPP): Takasbank üyesi bankalar ve aracı kurumların kısa vadeli Türk Lirası likidite fazlalarını değerlendirdikleri veya likidite açıklarını kapattıkları kör havuz (anonim) para piyasasıdır. Takasbank bu piyasada Merkezi Karşı Taraf olarak takası garanti eder. Bireysel yatırımcılar bu piyasada doğrudan işlem yapamaz.",
            "Ödünç Pay Piyasası (ÖPA): Borsa İstanbul bünyesinde işlem gören payların belirli bir komisyon karşılığında ödünç verilip ödünç alındığı piyasadır.",
            "Ödünç Pay Piyasası Ne İşe Yarar?",
            "1. Açığa Satış Yapanlar İçin: Açığa satış yapan yatırımcı takas günü hisseyi teslim edebilmek için ÖPA'dan hisse ödünç alır.",
            "2. Takas Temerrüdünü Önlemek İçin: Takas gününde hisse senedi açığı olan bir aracı kurum ÖPA'dan ödünç alarak temerrüde düşmekten kurtulur.",
            "3. Uzun Vadeli Yatırımcılar İçin: Portföyündeki hisseleri uzun süre satmayacak olan fonlar hisselerini ödünç vererek ek komisyon getirisi elde eder."
        ],
        "concrete_examples": [
            "Örnek 1 (Ödünç Pay ile Takas Açığını Kapatma): X Yatırım müşterisi Salı günü takası olan 10.000 lot hisseyi teslim edemez. X Yatırım temerrüde düşüp ceza yememek için hemen Takasbank Ödünç Pay Piyasası'na girer, yıllık %10 komisyonla 10.000 lot hisseyi ödünç alır ve Takasbank'a teslim ederek takası kapatır.",
            "Örnek 2 (Takasbank Para Piyasası Likidite Yönetimi): Gün sonunda kasasında 100 milyon TL nakit fazlası kalan Garanti Yatırım, parayı TPP'ye gecelik (O/N) borç olarak koyar; nakit açığı olan İş Yatırım ise DİBS teminatı vererek bu parayı borç alır. İki kurum birbirini görmez, Takasbank aradaki garantördür."
        ],
        "key_takeaways": [
            "Takasbank Para Piyasası (TPP) finansal kurumların TL borçlanıp borç verdikleri kör havuzdur.",
            "Ödünç Pay Piyasası (ÖPA) açığa satış ve takas açığını kapatmak için hisse kiralama imkanı sağlar.",
            "Her iki piyasada da Takasbank Merkezi Karşı Taraf (CCP) olarak takası garanti eder."
        ],
        "exam_traps": [
            "⚠️ BİREYSEL TUZAĞI: Bireysel yatırımcılar Takasbank Para Piyasası'nda doğrudan üye olup işlem yapamazlar; aracı kurumları aracılığıyla nemalandırılırlar."
        ]
    },
    "sec_1012_07": {
        "title": "7. MKK Elektronik Platformları (e-GKS, e-ŞİRKET, e-VEDO, e-Ürün) ve Temettü/Bedelli Hak Kullanım Süreçleri",
        "content": [
            "MKK tarafından sermaye piyasasının dijitalleşmesi amacıyla geliştirilen temel elektronik platformlar:",
            "1. e-GKS (Elektronik Genel Kurul Sistemi): Pay sahiplerinin dünyanın her yerinden genel kurula fiziken gitmeksizin elektronik imzayla katılmasını, canlı yayın izlemesini, soru sormasını ve oy kullanmasını sağlayan sistemdir. Halka açık şirketlerde e-GKS kurulması kanunen zorunludur.",
            "2. e-ŞİRKET (Şirketler Bilgi Portalı): Şirketlerin kanunen ilan etmek zorunda olduğu belgelerin yayımlandığı merkezi veri tabanıdır.",
            "3. e-VEDO (Veri Deposu): Türev araç işlemlerinin SPK ve uluslararası düzenlemeler gereği raporlandığı merkezi veri tabanıdır.",
            "4. e-Ürün (Elektronik Ürün Senedi Platformu): Lisanslı depolarda saklanan tarımsal ürünleri (buğday, mısır, pamuk) temsil eden Elektronik Ürün Senetlerinin (ELÜS) MKK nezdinde kayden izlendiği sistemdir.",
            "Temettü Hak Kullanım Süreci: Temettü dağıtım tarihinde (T) hisseye sahip olanlar temettüye hak kazanır. Nakit temettü tutarı T+2 İŞ GÜNÜNDE yatırımcıların hesaplarına Takasbank aracılığıyla net olarak yansır."
        ],
        "concrete_examples": [
            "Örnek 1 (e-GKS ile Evden Oy Kullanma): Ankara'da yaşayan yatırımcı Zeynep Hanım, pay sahibi olduğu ve genel kurulu İstanbul'da yapılan Tüpraş A.Ş.'nin genel kuruluna e-GKS üzerinden güvenli elektronik imzasıyla bağlanır, yönetim kurulu faaliyet raporunu inceler ve gündem maddelerine evinden 'Kabul' oyu verir.",
            "Örnek 2 (Temettü Hesaba Geçiş Süresi): Şirket Pazartesi günü (T) temettü dağıtacağını açıklar. Pazartesi sabahı hisseye sahip olan yatırımcının temettü nakdi T+2 kuralı gereğince ÇARŞAMBA günü öğleden sonra hesabına nakit geçer."
        ],
        "key_takeaways": [
            "e-GKS elektronik ortamda genel kurula katılım ve oy kullanma platformudur (MKK işletir).",
            "e-VEDO türev finansal işlemlerin raporlandığı merkezi veri deposudur.",
            "e-Ürün lisanslı depoculuk tarımsal ürün senetlerinin (ELÜS) kaydi sistemidir.",
            "Nakit temettüler hak kullanım tarihini izleyen ikinci iş gününde (T+2) hesaplara aktarılır."
        ],
        "exam_traps": [
            "⚠️ İŞLETİCİ TUZAĞI: e-GKS ve e-ŞİRKET platformlarını Borsa İstanbul veya Takasbank değil, münhasıran 'MKK' işletmektedir.",
            "⚠️ TEMETTÜ GÜNÜ TUZAĞI: Temettü nakdi genel kurul günü değil, şirketin belirlediği hak kullanım tarihinden 2 iş günü sonra (T+2) hesaba yatar."
        ]
    }
}

def elevate():
    updated_count = 0
    for mod, data in tn.items():
        for s in data.get('sections', []):
            sid = s.get('id')
            if sid in ENRICHMENTS:
                enr = ENRICHMENTS[sid]
                s['title'] = enr['title']
                s['content'] = enr['content']
                s['concrete_examples'] = enr['concrete_examples']
                s['key_takeaways'] = enr['key_takeaways']
                s['exam_traps'] = enr['exam_traps']
                updated_count += 1
                
    with open('src/data/topic_notes.json', 'w', encoding='utf-8') as f:
        json.dump(tn, f, ensure_ascii=False, indent=2)
        
    print(f"Toplam {updated_count} konu anlatım bölümü başarıyla zenginleştirildi ve güncellendi.")

if __name__ == '__main__':
    elevate()
