import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

MASTER_TOPIC_NOTES = {
    # =========================================================================
    # MODÜL 1001: SERMAYE PİYASASI MEVZUATI VE İLGİLİ MEVZUAT
    # =========================================================================
    "1001": {
        "module_id": "1001",
        "module_name": "Sermaye Piyasası Mevzuatı ve İlgili Mevzuat",
        "title": "SPK Mevzuatı Kapsamlı Sınav Hazırlık Kılavuzu",
        "total_sections": 7,
        "sections": [
            {
                "id": "sec_1001_01",
                "title": "1. Sermaye Piyasası Kanunu'nun (SPKn) Amacı, Kapsamı ve SPK'nın Düzenleme/Denetleme Yetkileri",
                "content": [
                    "6362 sayılı Sermaye Piyasası Kanunu'nun (SPKn) temel amacı; sermaye piyasasının güvenilir, şeffaf, etkin, istikrarlı, adil ve rekabetçi bir ortamda işleyişinin ve gelişmesinin sağlanması, tasarruf sahiplerinin ve yatırımcıların hak ve menfaatlerinin korunmasıdır.",
                    "Sermaye Piyasası Kurulu (SPK), idari ve mali özerkliğe sahip bir kamu tüzel kişisidir. Kurul; sermaye piyasası araçlarını, ihraççıları, halka arz edenleri, borsaları, teşkilatlanmış diğer pazar yerlerini, takas ve saklama kuruluşlarını, yatırım kuruluşlarını ve diğer sermaye piyasası kurumlarını düzenler ve denetler.",
                    "SPK'nın denetim yetkileri son derece geniştir: İlgili gerçek ve tüzel kişilerden her türlü bilgi ve belgeyi isteme, defter ve kayıtlarını yerinde inceleme, bilgi işlem sistemlerine erişme yetkisine sahiptir. Kanuna aykırı faaliyet tespit edildiğinde Kurul; aykırılıkların giderilmesi için süre verme, idari para cezası kesme, hukuka aykırı internet sitelerine erişimin engellenmesini BTK'dan talep etme ve ilgililer hakkında Cumhuriyet Başsavcılığı'na suç duyurusunda bulunma yetkilerini haizdir."
                ],
                "concrete_examples": [
                    "Piyasa Örneği: Lisanssız bir internet sitesi yurt içindeki yatırımcılara sosyal medya üzerinden izinsiz kaldıraçlı döviz (Forex) işlemi yaptırdığında, SPK m.99 kapsamında mahkemeye gitmeye gerek kalmaksızın doğrudan Bilgi Teknolojileri ve İletişim Kurumu'na (BTK) başvurarak ilgili web sitesine Türkiye'den erişimin engellenmesini sağlar."
                ],
                "key_takeaways": [
                    "SPK'nın nihai hedefi tasarruf sahiplerinin ve yatırımcıların haklarını korumaktır.",
                    "SPK, şirket yöneticilerini doğrudan kamu görevinden azledemez; gerektiğinde görevden uzaklaştırılmaları veya kayyum atanması için asliye ticaret mahkemesinden talepte bulunur.",
                    "Kurul kararlarına karşı yargı yolu açıktır; idari yargıda (İdare Mahkemeleri ve Danıştay) dava açılabilir."
                ],
                "exam_traps": [
                    "⚠️ DİKKAT: 'SPK'nın onayı ihraç edilen menkul kıymetin veya şirketin mali durumuna devlet garantisi verildiği anlamına GELMEZ.' Bu ifade SPK sınavlarında en çok sorulan klasik çeldiricidir."
                ],
                "exam_tips": [
                    "Öncüllü sorularda 'Kurulun doğrudan şirket malvarlığına el koyabileceği' gibi aşırı idari yetkiler genellikle YANLIŞ öncüldür. Kurul mahkemeler aracılığıyla ihtiyati tedbir talep eder."
                ],
                "tables": [
                    {
                        "headers": ["Yetki Alanı", "SPK'nın Doğrudan Yetkisi", "Yargı / Mahkeme Kararı Gereken Haller"],
                        "rows": [
                            ["İnternet Sitesi Erişimi", "BTK'ya doğrudan erişim engeli bildirimi", "Site sahibinin cezai mahkumiyeti"],
                            ["Piyasa İşlemleri", "Borsada geçici veya sürekli işlem yasağı", "Hapis cezası kararı"],
                            ["Şirket Yönetimi", "Yönetim kurulu üyeliğinden istifa çağrısı", "Görevden uzaklaştırma ve kayyum ataması"]
                        ]
                    }
                ]
            },
            {
                "id": "sec_1001_02",
                "title": "2. İzahname, Halka Arz ve Kamuyu Aydınlatma Platformu (KAP) Esasları",
                "content": [
                    "Sermaye piyasası araçlarının halka arz edilebilmesi veya borsada işlem görebilmesi için kural olarak 'İzahname' hazırlanması ve bu izahnamenin Sermaye Piyasası Kurulu tarafından onaylanması zorunludur.",
                    "İzahname; ihraççının ve varsa garantörün finansal durumu, faaliyetleri, geleceğe yönelik beklentileri ve ihraç edilecek sermaye piyasası araçlarının nitelikleri hakkında yatırımcıların bilinçli bir değerlendirme yapmasını sağlayacak bilgileri içerir.",
                    "SPK onayından itibaren izahnamenin kanuni geçerlilik süresi, ek ve değişikliklerin Kurulca onaylanması şartıyla tam 12 AYDIR. Süre bitiminde yeni bir halka arz yapılacaksa sıfırdan yeni bir izahname onaylatılmalıdır.",
                    "Kamuyu Aydınlatma Platformu (KAP); sermaye piyasası ve borsa mevzuatı uyarınca kamuya açıklanması zorunlu bildirimlerin elektronik imzalı olarak iletildiği ve kamuya duyurulduğu merkezi sistemdir. Şirketler meşru menfaatlerinin zarar görmemesi için 'içsel bilginin açıklanmasını erteleyebilirler'; ancak erteleme sebepleri ortadan kalktığı veya bilginin gizliliği korunamadığı (sızdığı) anda derhal KAP açıklaması yapılmak zorundadır."
                ],
                "concrete_examples": [
                    "Piyasa Örneği: ABC Teknoloji A.Ş., büyük bir yabancı ortakla birleşme görüşmesi yürütürken hisse fiyatının spekülatif dalgalanmasını önlemek için açıklamayı erteler. Fakat bir ekonomi gazetesinde bu gizli görüşmenin detayları haber olunca (bilgi sızınca), şirket ertelemeyi derhal sonlandırarak aynı gün KAP'a resmi özel durum açıklaması yapmak zorundadır."
                ],
                "key_takeaways": [
                    "İzahnamenin geçerlilik süresi: Onay tarihinden itibaren 12 AYDIR.",
                    "İzahnamede yer alan yanıltıcı bilgilerden; ihraççı, konsorsiyum lideri aracı kurum ve bağımsız denetim kuruluşu kusurları oranında müteselsilen sorumludur.",
                    "Tasarruf Sahiplerine Satış Duyurusu (TSSD) izahname ile birlikte KAP'ta ilan edilir."
                ],
                "exam_traps": [
                    "⚠️ DİKKAT: İzahnamenin geçerlilik süresi 30 gün veya 6 ay değil, kesin olarak '12 AY'dır.",
                    "⚠️ DİKKAT: İzahnamede eksiklik halinde yatırımcı önce ihraççıya başvurur; ihraççıdan tazmin edemezse konsorsiyum lideri aracı kuruma ve bağımsız denetçiye gider."
                ],
                "tables": [
                    {
                        "headers": ["Belge Türü", "Onay / İlan Yeri", "Kanuni Süre / Geçerlilik"],
                        "rows": [
                            ["İzahname", "SPK Onayı + KAP İlanı", "Onay tarihinden itibaren 12 Ay"],
                            ["Tasarruf Sahiplerine Satış Duyurusu", "KAP + Şirket Web Sitesi", "Halka arz süresince (En az 2 iş günü)"],
                            ["Özel Durum Açıklaması", "KAP Sistemi", "Olay vuku bulduğunda derhal"]
                        ]
                    }
                ]
            },
            {
                "id": "sec_1001_03",
                "title": "3. Kurumsal Yönetim İlkeleri ve Bağımsız Yönetim Kurulu Üyeleri",
                "content": [
                    "SPK Kurumsal Yönetim Tebliği (II-17.1), halka açık anonim ortaklıkların kurumsal yönetim standartlarını belirler. İlkeler dört temel sütun üzerine kuruludur: Pay Sahipleri, Kamuyu Aydınlatma ve Şeffaflık, Menfaat Sahipleri ve Yönetim Kurulu.",
                    "Borsa İstanbul Yıldız Pazar ve Ana Pazar'da işlem gören şirketler piyasa değerleri ve fiili dolaşım oranlarına göre 1., 2. ve 3. Grup olarak sınıflandırılır. 1. Grup ortaklıklarda bağımsız yönetim kurulu üyesi bulundurmak mutlak surette zorunludur.",
                    "Bağımsız Yönetim Kurulu Üye Oranı: Yönetim kurulu içerisindeki bağımsız üye sayısı, toplam üye sayısının üçte birinden (1/3) az olamaz ve her halükarda en az 2 kişi olmak zorundadır. Oran hesaplanırken küsuratlar bir üst tam sayıya yuvarlanır (Örn: 7 kişilik yönetim kurulunda 7 / 3 = 2.33 -> En az 3 bağımsız üye gerekir).",
                    "Bağımsız Üyenin Görev Süresi: Bir bağımsız üye aynı şirkette son 10 yıl içinde en fazla 6 yıl görev yapabilir. Bağımsız üye; şirkette veya iştiraklerinde icracı yönetici olamaz, son 5 yılda çalışmamış olmalı ve 1. dereceye kadar akrabalık bağı bulunmamalıdır."
                ],
                "concrete_examples": [
                    "Piyasa Örneği: BIST 30 endeksinde yer alan 8 kişilik bir banka yönetim kurulunda bağımsız üye hesabı: 8 / 3 = 2,66 eder. Küsurat yukarı yuvarlanarak en az 3 üyenin SPK kriterlerine tam uyan bağımsız üye olması zorunludur."
                ],
                "key_takeaways": [
                    "Bağımsız yönetim kurulu üye oranı: En az 1/3 ve asgari 2 üye.",
                    "Azami bağımsız üyelik görev süresi: Son 10 yıl içinde toplam 6 yıl.",
                    "Denetimden Sorumlu Komite üyelerinin tamamı bağımsız yönetim kurulu üyelerinden oluşmak zorundadır."
                ],
                "exam_traps": [
                    "⚠️ DİKKAT: 'Genel müdür veya murahhas aza bağımsız üye olabilir' ifadesi YANLIŞTIR. İcracı üyeler asla bağımsız üye olamaz.",
                    "⚠️ DİKKAT: Şirket sermayesinde %5 veya daha fazla paya sahip olan kişiler bağımsız üye seçilemez."
                ],
                "tables": [
                    {
                        "headers": ["Kriter", "Kanuni / Tebliğ Eşiği", "Sınav Notu"],
                        "rows": [
                            ["Bağımsız Üye Oranı", "Yönetim kurulu tam sayısının en az 1/3'ü", "Küsuratlar yukarı yuvarlanır"],
                            ["Asgari Bağımsız Üye Sayısı", "En az 2 üye", "Yönetim kurulu 5 kişi olsa dahi en az 2 üye şarttır"],
                            ["Azami Görev Süresi", "Son 10 yıl içinde en fazla 6 yıl", "Bağımsızlığın zedelenmemesi kuralı"],
                            ["Denetim Komitesi Yapısı", "Tamamı (%100) Bağımsız Üye", "İcracı üye komitede yer alamaz"]
                        ]
                    }
                ]
            },
            {
                "id": "sec_1001_04",
                "title": "4. Pay Sahipliği Hakları, Sermaye Artırımları ve Önemli Nitelikteki İşlemler",
                "content": [
                    "Anonim ortaklıklarda sermaye artırımı iki şekilde gerçekleşir: Bedelsiz (İç kaynaklardan veya temettüden karşılanan) ve Bedelli (Ortakların şirkete nakit koymasıyla gerçekleşen).",
                    "Rüçhan Hakkı (Yeni Pay Alma Hakkı): Bedelli sermaye artırımında mevcut pay sahiplerinin şirketteki ortaklık payları oranında yeni payları öncelikle satın alma hakkıdır. Kanunen rüçhan hakkı kullanım süresi en az 15 gün, en fazla 60 gün olarak belirlenir. Kullanılmayan paylar Borsa İstanbul Birincil Piyasa'da nominal değerden düşük olmamak üzere halka arz edilir.",
                    "Ayrılma Hakkı: Birleşme, bölünme, tür değiştirme veya tüm malvarlığının devri gibi 'Önemli Nitelikteki İşlemler' genel kurulda görüşülürken muhalefet şerhi koyan pay sahipleri, paylarını Kurul düzenlemelerine uygun adil bir bedelle şirkete satarak ortaklıktan ayrılabilir.",
                    "Ortaklıktan Çıkarma ve Satma Hakkı (%98 Kuralı): Halka açık ortaklıklarda bir pay sahibinin veya birlikte hareket edenlerin oy hakları oranı %98 eşiğine ulaştığında; hâkim ortak azınlıkta kalanları şirketten çıkarma hakkına sahip olurken, azınlık pay sahipleri de paylarını hâkim ortağa adil bedelle satma hakkı kazanır."
                ],
                "concrete_examples": [
                    "Piyasa Örneği: Holding A.Ş., borsada işlem gören iştirakinin %98 oy hakkını topladığında, kalan %2'lik küçük yatırımcıları mahkeme kararıyla şirketten çıkarabilir ve şirketi borsa kotundan çıkartabilir. Aynı şekilde %2'lik azınlık yatırımcı da paylarını son 1 aylık/6 aylık ağırlıklı ortalama fiyat üzerinden holdinge zorunlu satın aldırma hakkına sahiptir."
                ],
                "key_takeaways": [
                    "Rüçhan hakkı kullanım süresi: En az 15 gün, en fazla 60 gün.",
                    "Hâkim ortaklık / Ortaklıktan çıkarma ve satma hakkı eşiği: Tam %98'dir.",
                    "Ayrılma hakkı bedeli: Genel kurul onayından önceki 30 günlük borsa düzeltilmiş ağırlıklı ortalama fiyatı esas alınır."
                ],
                "exam_traps": [
                    "⚠️ DİKKAT: Ortaklıktan çıkarma eşiği %50 veya %75 değil, kesin olarak '%98'dir.",
                    "⚠️ DİKKAT: Rüçhan hakkı kısıtlanırken sadece yönetim kurulu kararı yetmez; kayıtlı sermaye sisteminde esas sözleşmede açık yetki bulunması zorunludur."
                ],
                "tables": [
                    {
                        "headers": ["İşlem Türü", "Kanuni Eşik / Süre Sınırı", "Hukuki Sonuç"],
                        "rows": [
                            ["Rüçhan Hakkı Kullanımı", "En az 15 gün, en fazla 60 gün", "Pay sahipleri yeni payları nakit ödeyerek alır"],
                            ["Hâkim Ortaklık Eşiği", "%98 Oy Hakkı Oranı", "Çıkarma ve satma hakkı karşılıklı doğar"],
                            ["Kayıtlı Sermaye Tavanı Yetkisi", "Azami 5 yıl", "Süre dolunca genel kuruldan yeni yetki alınır"]
                        ]
                    }
                ]
            },
            {
                "id": "sec_1001_05",
                "title": "5. Sermaye Piyasası Suçları, Cezaları ve Etkin Pişmanlık (m.106 - m.110)",
                "content": [
                    "6362 sayılı Kanun'da sermaye piyasasının dürüstlüğünü ve şeffaflığını korumak amacıyla ağır cezai yaptırımlar öngörülmüştür:",
                    "1. İçsel Bilgiye Dayalı Ticaret (İnsider Trading - m.106): Henüz kamuya açıklanmamış, sermaye piyasası aracının fiyatını etkileyebilecek nitelikteki bilgiye doğrudan veya dolaylı olarak dayanarak menfaat temin edilmesi fiilidir. Cezası 3 yıldan 8 yıla kadar hapis veya adli para cezasıdır.",
                    "2. Piyasa Dolandırıcılığı (Manipülasyon - m.107): İki türlü işlenir: İşlem Bazlı Manipülasyon (Yapay arz-talep yaratmak, kendi kendine emir eşleştirmek) ve Bilgi Bazlı Manipülasyon (Yalan, yanlış, yanıltıcı haber yaymak). Cezası 3 yıldan 5 yıla kadar hapis ve 5.000 günden 10.000 güne kadar adli para cezasıdır. Bilgi bazlı manipülasyonda adli para cezası elde edilen menfaatten az olamaz.",
                    "3. Örtülü Kazanç Aktarımı Suçu (m.21 ve m.110): Halka açık ortaklıkların ilişkili taraflarla emsallerine göre bariz şekilde farklı fiyat, ücret ve bedeller üzerinden işlem yaparak şirket kârını dışarı aktarması suçtur. Cezası 2 yıldan 5 yıla kadar hapis ve 5.000 güne kadar adli para cezasıdır.",
                    "4. Yetkisiz Sermaye Piyasası Faaliyeti (m.109): SPK'dan izin almaksızın sermaye piyasası faaliyeti yürütenlere 2 yıldan 5 yıla kadar hapis ve 5.000 güne kadar adli para cezası verilir.",
                    "Etkin Pişmanlık Hükmü (m.107/3): İşlem bazlı manipülasyon suçunu işleyen kişi, SPK tarafından henüz incelemeye başlanmadan önce durumu Kurul'a ihbar eder ve elde ettiği menfaatin 2 KATINI Hazineye öderse hakkında cezaya hükmolunmaz."
                ],
                "concrete_examples": [
                    "Piyasa Örneği: Halka açık bir gıda şirketinin hâkim ortağı, şirkete ait bir fabrikayı kendi şahsi şirketine piyasa değerinin 1/5 fiyatına satarsa 'Örtülü Kazanç Aktarımı' suçunu işlemiş olur. SPK bu işlemi tespit ettiğinde işlemin iptali ve devredilen kârın faiziyle şirkete iadesi için dava açar, ilgililer hakkında Cumhuriyet Savcılığı'na suç duyurusunda bulunur."
                ],
                "key_takeaways": [
                    "Piyasa Dolandırıcılığı Cezası: 3 yıldan 5 yıla kadar hapis ve 5.000 - 10.000 gün adli para cezası.",
                    "Etkin Pişmanlık: İnceleme öncesinde menfaatin 2 KATI Hazineye ödenmelidir.",
                    "Örtülü kazanç aktarımı ve yetkisiz sermaye piyasası faaliyeti hapis cezası gerektiren adli suçlardır."
                ],
                "exam_traps": [
                    "⚠️ DİKKAT: Bilgi bazlı manipülasyonda (yalan haber yayma) etkin pişmanlık uygulanmaz; etkin pişmanlık sadece 'işlem bazlı manipülasyon' için geçerlidir.",
                    "⚠️ DİKKAT: Hazineye ödenecek tutar kârın kendisi değil, kanunen 'İKİ KATI'dır."
                ],
                "tables": [
                    {
                        "headers": ["Suç Tipi", "Hapis Cezası Sınırı", "Adli Para Cezası", "Etkin Pişmanlık Şartı"],
                        "rows": [
                            ["İçsel Bilgi Ticareti (m.106)", "3 yıl - 8 yıl hapis", "Adli Para Cezası", "Uygulanmaz"],
                            ["İşlem Bazlı Manipülasyon (m.107/1)", "3 yıl - 5 yıl hapis", "5.000 - 10.000 gün", "İnceleme öncesi 2 katı ödeme"],
                            ["Bilgi Bazlı Manipülasyon (m.107/2)", "3 yıl - 5 yıl hapis", "Menfaatten az olamaz", "Uygulanmaz"],
                            ["Örtülü Kazanç Aktarımı (m.21/110)", "2 yıl - 5 yıl hapis", "5.000 güne kadar", "Kazancın şirkete iadesi şartı"],
                            ["Yetkisiz Sermaye Faaliyeti (m.109)", "2 yıl - 5 yıl hapis", "5.000 güne kadar", "Uygulanmaz"]
                        ]
                    }
                ]
            },
            {
                "id": "sec_1001_06",
                "title": "6. Türkiye Sermaye Piyasaları Birliği (TSPB) ve Disiplin Cezaları Hiyerarşisi",
                "content": [
                    "Türkiye Sermaye Piyasaları Birliği (TSPB); kamu kurumu niteliğinde bir meslek kuruluşudur. Sermaye piyasasında faaliyet gösteren tüm aracı kurumlar, bankalar, portföy yönetim şirketleri ve yatırım ortaklıkları TSPB'ye üye olmak zorundadır.",
                    "TSPB'nin temel görevleri: Sermaye piyasası faaliyetlerinin mesleki kurallara, dürüstlük ve güven ilkelerine uygun yürütülmesini gözetmek, haksız rekabeti önlemek, meslek kurallarını belirlemek ve üyelerini denetlemektir.",
                    "TSPB Disiplin Cezaları Hiyerarşisi: Birlik mevzuatına ve meslek kurallarına aykırı hareket eden üye kuruluşlara ve çalışanlarına verilebilecek cezalar hafiften ağıra doğru şöyledir:\n1. Uyarı\n2. Kınama\n3. Para Cezası\n4. Geçici Olarak Faaliyetten Alıkoyma\n5. Birlik Üyeliğinden Çıkarma (İhraç)"
                ],
                "concrete_examples": [
                    "Piyasa Örneği: Bir aracı kurum çalışanının müşteriye yanıltıcı getiri taahhüdünde bulunması halinde TSPB Disiplin Kurulu toplanarak önce kınama veya para cezası uygular. Fiilin tekrarı ve kasıt halinde ise SPK'nın onayına sunulmak üzere birlik üyeliğinden çıkarma kararı alınabilir."
                ],
                "key_takeaways": [
                    "Sermaye piyasasında faaliyet izni alan tüm aracı kurumların TSPB'ye üye olması kanunen mecburidir.",
                    "Disiplin cezaları sıralaması: Uyarı -> Kınama -> Para Cezası -> Geçici Alıkoyma -> Birlik Üyeliğinden Çıkarma.",
                    "Birlik üyeliğinden çıkarma kararı kesinleştiğinde kuruluşun faaliyet izni de SPK tarafından iptal edilir."
                ],
                "exam_traps": [
                    "⚠️ DİKKAT: TSPB hapis cezası veremez; hapis cezası yalnızca bağımsız mahkemelerce verilebilir.",
                    "⚠️ DİKKAT: Disiplin cezalarında 'İhtar' değil mevzuattaki resmi terim olan 'Uyarı' yer alır."
                ],
                "tables": [
                    {
                        "headers": ["Ceza Derecesi", "Ceza Türü", "Uygulama Yetkisi", "Açıklama"],
                        "rows": [
                            ["1. Derece", "Uyarı", "TSPB Disiplin Kurulu", "Mesleğin icrasında dikkatsizlik hali"],
                            ["2. Derece", "Kınama", "TSPB Disiplin Kurulu", "Kusurlu davranışın yazılı kınanması"],
                            ["3. Derece", "Para Cezası", "TSPB Yönetim Kurulu", "Mevzuatta belirlenen parasal ceza"],
                            ["4. Derece", "Geçici Faaliyetten Alıkoyma", "TSPB + SPK Onayı", "Belirli süre işlem yapamama"],
                            ["5. Derece", "Birlik Üyeliğinden Çıkarma", "TSPB Genel Kurulu + SPK", "En ağır mesleki yaptırım (İhraç)"]
                        ]
                    }
                ]
            },
            {
                "id": "sec_1001_07",
                "title": "7. TTK Anonim Şirketler: Genel Kurul Toplantı ve Karar Yetersayıları (Nisaplar) ile Kayıtlı Sermaye Sistemi",
                "content": [
                    "Türk Ticaret Kanunu (TTK) ve Sermaye Piyasası Kanunu, anonim ortaklıkların karar alma organı olan Genel Kurul'un geçerli toplanabilmesi ve karar alabilmesi için asgari yetersayılar (nisaplar) belirlemiştir.",
                    "1. Olağan Genel Kurul Toplantı ve Karar Nisabı: Kanunda veya esas sözleşmede daha ağır bir nisap öngörülmemişse; şirket sermayesinin EN AZ DÖRTTE BİRİNİ (%25) temsil eden pay sahiplerinin hazır bulunmasıyla toplanır. Kararlar toplantıda hazır bulunan oyların ÇOĞUNLUĞUYLA alınır. İlk toplantıda nisap sağlanamazsa ikinci toplantıda nisap aranmaz.",
                    "2. Esas Sözleşme Değişikliği Nisabı: Kural olarak şirket sermayesinin en az YARISINI (%50) temsil eden pay sahiplerinin hazır bulunması gerekir. Kararlar toplantıda temsil edilen oyların çoğunluğuyla alınır. Şirket merkezinin yurt dışına taşınması veya bilanço zararlarının kapatılması için yükümlülük getirilmesinde ise %100 OYBİRLİĞİ şarttır.",
                    "3. Kayıtlı Sermaye Sistemi: Halka açık ortaklıklar SPK izniyle kayıtlı sermaye sistemine geçebilirler. Bu sistemde genel kurul, yönetim kuruluna esas sözleşmede belirlenen tavan içinde sermayeyi artırma yetkisi verir. Yönetim kuruluna verilen bu tavan artırım yetkisinin süresi EN FAZLA 5 YILDIR. 5 yıl dolduğunda genel kuruldan yeni yetki alınmalıdır."
                ],
                "concrete_examples": [
                    "Piyasa Örneği: 100 Milyon TL sermayeli BIST şirketinin olağan genel kurulunun toplanabilmesi için en az 25 Milyon TL sermayeyi temsil eden pay sahiplerinin toplantıda hazır bulunması şarttır. Toplantıya 40 Milyon TL pay sahibi katılmışsa, 20 Milyon TL + 1 oy ile tüm olağan kararlar (faaliyet raporu onayı, yönetim ibra vb.) yasal olarak alınabilir."
                ],
                "key_takeaways": [
                    "Olağan Genel Kurul Toplantı Nisabı: Sermayenin en az 1/4'ü (%25). Karar: Hazır bulunanların çoğunluğu.",
                    "Kayıtlı sermaye sisteminde yönetim kuruluna verilen sermaye artırma yetki süresi: En fazla 5 yıldır.",
                    "İlk toplantıda 1/4 nisap bulunamazsa ikinci toplantıda çağrı usulüne uyulmak kaydıyla asgari nisap aranmaz."
                ],
                "exam_traps": [
                    "⚠️ DİKKAT: Kayıtlı sermaye sisteminde yönetim kurulu tavanı aşarak sermaye artıramaz; tavanı artırmak için Genel Kurul'un esas sözleşme değişikliği yapması şarttır."
                ],
                "tables": [
                    {
                        "headers": ["Genel Kurul Karar Konusu", "Toplantı Yetersayısı (Nisap)", "Karar Yetersayısı", "İkinci Toplantı Kuralı"],
                        "rows": [
                            ["Olağan Kararlar (İbra, Temettü, Seçim)", "Sermayenin en az 1/4'ü (%25)", "Katılanların Çoğunluğu", "Nisap aranmaksızın toplanır"],
                            ["Esas Sözleşme Değişikliği (Genel)", "Sermayenin en az 1/2'si (%50)", "Katılanların Çoğunluğu", "Sermayenin en az 1/3'ü ile toplanır"],
                            ["Şirket Merkezini Yurt Dışına Taşıma", "Sermayenin %100'ü (Tamamı)", "Tam Oybirliği", "İkinci toplantıda da %100 aranır"],
                            ["Kayıtlı Sermaye Tavan Yetki Süresi", "Azami 5 Yıl", "Genel Kurul Onayı", "5 yıl sonra yetki yenilenir"]
                        ]
                    }
                ]
            }
        ]
    },

    # =========================================================================
    # MODÜL 1003: SERMAYE PİYASASI ARAÇLARI 1
    # =========================================================================
    "1003": {
        "module_id": "1003",
        "module_name": "Sermaye Piyasası Araçları 1",
        "title": "Sermaye Piyasası Araçları Kapsamlı Sınav Hazırlık Kılavuzu",
        "total_sections": 7,
        "sections": [
            {
                "id": "sec_1003_01",
                "title": "1. Paylar (Hisse Senetleri), Hukuki Haklar ve Oyda İmtiyaz Sınırı (15 Oy)",
                "content": [
                    "Pay (Hisse Senedi); anonim ortaklıkların sermayesini temsil eden ve sahibine ortaklık sıfatı kazandıran menkul kıymettir. Pay sahibine iki grup hak sağlar: 1) Mali Haklar (Temettü/Kâr payı, Tasfiye bakiyesi, Rüçhan hakkı, Bedelsiz pay alma hakkı), 2) İdari Haklar (Genel kurula katılma, Oy kullanma, Bilgi alma ve inceleme, İptal davası açma).",
                    "Nama ve Hamiline Paylar: Borsa İstanbul'da işlem gören tüm paylar Merkezi Kayıt Kuruluşu (MKK) nezdinde kaydileştirilmiştir; mülkiyet devri fiziki teslimle değil MKK hesapları arasında elektronik tescille gerçekleşir.",
                    "Oyda İmtiyaz Sınırı (SPKn m.18): Halka açık anonim ortaklıklarda paylara esas sözleşmeyle oyda imtiyaz tanınabilir. Ancak mevzuat gereğince bir paya tanınabilecek azami oy hakkı sayısı KURAL OLARAK EN FAZLA 15 OYDUR.",
                    "İmtiyazın Sınırlandırıldığı Haller: Esas sözleşme değişikliği, yönetim kurulu üyelerinin ibra edilmesi veya sorumluluk davası açılması genel kurullarında oyda imtiyaz hükümleri uygulanamaz."
                ],
                "concrete_examples": [
                    "Piyasa Örneği: XYZ A.Ş.'nin A grubu imtiyazlı ve B grubu adi payları vardır. SPKn m.18 uyarınca bir A grubu paya genel kurulda en fazla 15 oy hakkı tanımlanabilir. Şirket esas sözleşmesine 1 paya 50 oy hakkı yazsa dahi, SPK onayından geçemez ve tescil edilemez."
                ],
                "key_takeaways": [
                    "Oyda imtiyaz azami yasal sınırı: 1 paya en fazla 15 oy.",
                    "Tahvil sahibi şirketin alacaklısıdır; pay sahibi ise ortaklığın sahibidir.",
                    "Borsadaki payların devri MKK kayıtlarına tescil ile hüküm ifade eder."
                ],
                "exam_traps": [
                    "⚠️ DİKKAT: Pay sahibinin şirkete karşı borcu sadece taahhüt ettiği sermaye payını ödemektir (Tek Borç İlkesi). Şirket zarara uğrarsa ortaklardan ek para talep edemez."
                ],
                "tables": [
                    {
                        "headers": ["Hak Türü", "Hakkın Niteliği", "İmtiyaz Tanınabilir mi?"],
                        "rows": [
                            ["Kâr Payı (Temettü)", "Mali Hak", "Evet, öncelikli kâr dağıtımı imtiyazı verilebilir"],
                            ["Oy Hakkı", "İdari Hak", "Evet, ancak 1 paya en fazla 15 oy verilebilir"],
                            ["Yönetim Kuruluna Aday Gösterme", "İdari Hak", "Evet, esas sözleşmeyle aday gösterme imtiyazı verilebilir"],
                            ["Bilgi Alma ve İnceleme", "Müktesep Hak", "Hayır, hiçbir pay sahibinin bilgi alma hakkı kısıtlanamaz"]
                        ]
                    }
                ]
            },
            {
                "id": "sec_1003_02",
                "title": "2. Borçlanma Araçları: Tahviller, Finansman Bonoları ve Kupon Türleri",
                "content": [
                    "Borçlanma Araçları; ihraççının borçlu, yatırımcının alacaklı olduğu menkul kıymetlerdir. Yatırımcı şirketin kâr-zarar ortağı değildir; vadesinde anaparasını ve dönemsel faizini (kupon) alma hakkına sahiptir.",
                    "Tahviller (Bonds): Anonim şirketlerin ve kamunun borçlanmak için ihraç ettiği en az 1 YIL (365 GÜN) vadeli orta ve uzun vadeli borçlanma araçlarıdır.",
                    "Finansman Bonoları: Vadesi en az 30 gün, en fazla 364 gün (1 yıldan kısa) olan kısa vadeli iskonto esaslı borçlanma araçlarıdır.",
                    "Kupon Türleri: Sabit kuponlu tahviller (piyasa faizinden etkilenmeksizin sabit oran öder) ve Değişken kuponlu tahviller (TCMB politika faizine veya TÜFE enflasyon oranına endeksli kupon öder).",
                    "Tasfiyede Öncelik: Şirket iflas ettiğinde veya tasfiyeye girdiğinde tahvil sahipleri alacaklı sıfatıyla pay sahiplerinden (hisse senedi sahiplerinden) çok daha önce tasfiye masasından alacaklarını tahsil ederler.",
                    "Temiz Fiyat (Clean Price) vs Kirli Fiyat (Dirty Price) ve İşlemiş Faiz:\n• Temiz Fiyat (Clean Price): Tahvilin son kupon ödeme tarihinden bugüne kadar birikmiş/işlemiş faizi HARİÇ piyasa fiyatıdır. Borsa İstanbul Borçlanma Araçları Piyasası ekranlarında kote edilen ve işlem gören fiyat daima TEMİZ FİYATTIR. Temiz fiyat kullanılmasının sebebi, kupon gününe yaklaştıkça faizin yapay olarak fiyatı şişirmesini önlemek ve sadece piyasa faiz oranlarındaki saf getiri dalgalanmalarını izlemektir.\n• İşlemiş Faiz (Accrued Interest): Son kupon ödeme tarihinden takas (satış) gününe kadar geçen gün sayısı için tahvilin hak ettiği faizdir. Formül: İşlemiş Faiz = Nominal Değer × Yıllık Kupon Oranı × (Geçen Gün Sayısı / 365).\n• Kirli Fiyat (Dirty Price): Temiz Fiyata İşlemiş Faizin eklenmesiyle oluşan toplam bedeldir. Formül: Kirli Fiyat = Temiz Fiyat + İşlemiş Faiz.\n• En Kritik Sınav Kuralı: Borsa ekranında Temiz Fiyat kote edilirken; alıcı takas gününde satıcıya cebinden çıkarıp FİİLEN KİRLİ FİYATI öder. Kupon ödeme gününde (veya hemen ertesi günü) işlemiş faiz sıfırlandığı için Temiz Fiyat = Kirli Fiyat olur."
                ],
                "concrete_examples": [
                    "Piyasa Örneği (Kuponlu Tahvil): 1.000 TL nominal değerli, 2 yıl vadeli ve 6 ayda bir %20 kupon ödemeli bir şirket tahvili alan yatırımcı; şirket zarar etse dahi her 6 ayda bir 200 TL faiz alır, vade sonunda ise 1.000 TL anaparasını eksiksiz geri alır.",
                    "Piyasa Örneği (Temiz vs Kirli Fiyat Hesabı): 1.000 TL nominal değerli, yıllık %20 kupon ödemeli bir tahvilin son kupon ödemesinden 182 gün geçmiştir. Tahvilin borsadaki temiz fiyatı 950 TL'dir. İşlemiş Faiz: 1.000 × %20 × (182 / 365) = 99,7 TL (yaklaşık 100 TL) bulunur. Alıcının takas gününde satıcıya fiilen ödeyeceği Kirli Fiyat: 950 TL (Temiz) + 100 TL (Faiz) = 1.050 TL'dir."
                ],
                "key_takeaways": [
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
                ],
                "tables": [
                    {
                        "headers": ["Borçlanma Aracı", "Asgari Vade", "Azami Vade", "Getiri Yapısı"],
                        "rows": [
                            ["Tahvil (Özel Sektör / Devlet)", "1 Yıl (365 Gün)", "Sınırsız (5-10-30 yıl)", "Sabit veya Değişken Kuponlu Faiz"],
                            ["Finansman Bonosu", "30 Gün", "364 Gün", "İskontolu Getiri"],
                            ["Hazine Bonosu", "1 Aydan Az Olmamak Üzere", "1 Yıldan Az", "İskontolu Getiri"],
                            ["Temiz Fiyat (Clean Price)", "Borsa ekranında kote edilen fiyat", "Kupon faizi hariç fiyat", "Kirli Fiyat - İşlemiş Faiz"],
                            ["Kirli Fiyat (Dirty Price)", "Takasta fiilen ödenen nakit bedel", "Kupon faizi dahil toplam tutar", "Temiz Fiyat + İşlemiş Faiz"]
                        ]
                    }
                ]
            },
            {
                "id": "sec_1003_03",
                "title": "3. Yatırım Fonları, TEFAS ve Borsa Yatırım Fonları (BYF / ETF - %95 Kuralı)",
                "content": [
                    "Yatırım Fonu; tasarruf sahiplerinden toplanan paralarla pay, borçlanma aracı, altın ve para piyasası enstrümanlarından oluşan inançlı mülkiyet esasına dayalı portföydür. Tüzel kişiliği yoktur, portföy yönetim şirketleri (PYŞ) tarafından yönetilir.",
                    "Malvarlığı Ayrılığı: Fon malvarlığı, kurucunun ve portföy saklayıcısının (Takasbank) malvarlığından tamamen ayrıdır. Kurucu iflas etse veya borca batsa dahi fon malvarlığı haczedilemez, rehin edilemez ve iflas masasına dahil edilemez.",
                    "TEFAS (Türkiye Elektronik Fon Alım Satım Platformu): Yatırımcıların kendi banka veya aracı kurum hesapları üzerinden diğer tüm kurucuların fonlarını tek tıkla alıp satabildikleri merkezi Takasbank fon süpermarketidir.",
                    "Borsa Yatırım Fonları (BYF / ETF): Bir endeksi (örneğin BIST 30 veya Altın Endeksi) baz alan ve katılma payları Borsa İstanbul Pay Piyasası'nda tıpkı hisse senedi gibi anlık işlem gören fonlardır.",
                    "Takip Korelasyon Oranı (%95 Kuralı): BYF Tebliği uyarınca, fon portföyünün değeri ile takip ettiği baz endeks arasındaki korelasyon katsayısının EN AZ %95 (0,95) olması kanuni zorunluluktur.",
                    "Özel Fon Türleri ve Asgari Portföy Sınırları: Hisse Senedi Yoğun Fonlarda portföyün EN AZ %80'inin devamlı olarak BIST hisselerinden oluşması zorunludur. Fon Sepeti Fonlarında fon değerinin EN AZ %80'i diğer yatırım fonu paylarından oluşur. Para Piyasası Fonlarında ise portföyün ağırlıklı ortalama vadesi en fazla 45 gün olabilir."
                ],
                "concrete_examples": [
                    "Piyasa Örneği: BIST 30 Endeksini takip eden bir BYF payı satın alan yatırımcı, seans saatleri içinde anlık olarak ekranından hisse senedi gibi işlem yapar. BIST 30 endeksi %3 yükseldiğinde, %95 takip kuralı gereğince BYF'nin fiyatı da neredeyse birebir oranda (%3 civarında) anlık yükselir."
                ],
                "key_takeaways": [
                    "BYF baz endeks takip korelasyon katsayısı: En az %95 (0,95).",
                    "Geleneksel fonlar gün sonu tek fiyatla (NAD) işlem görürken, BYF'ler borsa seansında anlık sürekli müzayedede işlem görür.",
                    "Yatırım fonu malvarlığı kurucunun borçları için asla haczedilemez."
                ],
                "exam_traps": [
                    "⚠️ DİKKAT: BYF'lerde işlem fiyatı gün sonunda belirlenmez; hisse senedi gibi seans boyunca serbest piyasada anlık arz-talebe göre belirlenir."
                ],
                "tables": [
                    {
                        "headers": ["Özellik", "Geleneksel Yatırım Fonu (TEFAS)", "Borsa Yatırım Fonu (BYF / ETF)"],
                        "rows": [
                            ["İşlem Platformu", "TEFAS / Dağıtıcı Kurumlar", "Borsa İstanbul Pay Piyasası"],
                            ["Fiyat Oluşumu", "Gün sonu tek Net Aktif Değeri (NAD)", "Seans boyunca anlık piyasa fiyatı"],
                            ["Yasal Zorunluluk", "Portföy sınırlamaları tebliği", "En az %95 Endeks Takip Korelasyonu"]
                        ]
                    }
                ]
            },
            {
                "id": "sec_1003_04",
                "title": "4. Gayrimenkul Yatırım Ortaklıkları (GYO - %51 Kuralı) ve Girişim Sermayesi (GSYF / GSYO)",
                "content": [
                    "Gayrimenkul Yatırım Ortaklıkları (GYO); gayrimenkuller, gayrimenkul projeleri, gayrimenkule dayalı haklar ve sermaye piyasası araçlarından oluşan portföyü işletmek üzere kurulan sermaye piyasası kurumlarıdır.",
                    "GYO Portföy Oranı (%51 Kuralı): SPK GYO Tebliği uyarınca GYO portföy değerinin EN AZ %51'İNİN gayrimenkuller, gayrimenkule dayalı haklar ve gayrimenkul projelerinden oluşması yasal zorunluluktur.",
                    "Vergisel Avantaj: Kurumlar Vergisi Kanunu m.5/1-d uyarınca GYO'ların kazançları kurumlar vergisinden tamamen istisnadır (Kurumlar Vergisi oranı %0).",
                    "İnşaat Yasağı: GYO'lar inşaat şirketi veya müteahhit değildir; bizzat kendi işçileri ve ekipmanlarıyla inşaat yapamazlar, işi daima üçüncü taraf müteahhitlere ihale etmek zorundadırlar.",
                    "Girişim Sermayesi (GSYF / GSYO): Türkiye'de kurulu veya kurulacak olan, büyüme potansiyeli yüksek ancak sermaye ihtiyacı duyan erken aşama girişim şirketlerine sermaye ve yönetim desteği sağlayan fon ve ortaklıklardır."
                ],
                "concrete_examples": [
                    "Piyasa Örneği: Torunlar GYO veya Emlak Konut GYO büyük bir konut projesi geliştirdiğinde, projeyi bizzat kendi işçileriyle inşa edemez; ihale açarak inşaat işini yüklenici bir müteahhit firmaya devreder. Elde ettiği kâr üzerinden ise kurumlar vergisi ödemez."
                ],
                "key_takeaways": [
                    "GYO portföyünün asgari %51'i gayrimenkul varlıklarından oluşmalıdır.",
                    "GYO'lar kurumlar vergisinden muaftır.",
                    "GYO'ların bizzat inşaat müteahhitliği yapması kanunen yasaktır."
                ],
                "exam_traps": [
                    "⚠️ DİKKAT: 'GYO'lar inşaat ruhsatı alıp bizzat taşeron çalıştırmadan bina yapabilir' ifadesi kesinlikle YANLIŞTIR. Müteahhitlik yapamazlar."
                ],
                "tables": [
                    {
                        "headers": ["Kurum Türü", "Asgari Portföy Şartı", "Vergi Muafiyeti", "Temel Yasak"],
                        "rows": [
                            ["GYO", "En az %51 Gayrimenkul Varlıkları", "Kurumlar Vergisi %0", "Bizzat İnşaat Müteahhitliği Yapma Yasağı"],
                            ["GSYF", "En az %80 Girişim Sermayesi Yatırımı", "Kurumlar Vergisi %0", "Kısa Vadeli Spekülatif Al-Sat Yasağı"]
                        ]
                    }
                ]
            },
            {
                "id": "sec_1003_05",
                "title": "5. Varlığa Dayalı Menkul Kıymetler (VDMK), İTMK ve Kira Sertifikaları (Sukuk)",
                "content": [
                    "Varlığa Dayalı Menkul Kıymetler (VDMK): İhracın teminatını oluşturan alacak havuzlarına (tüketici kredileri, konut kredileri, leasing alacakları) dayanılarak ihraç edilen borçlanma araçlarıdır.",
                    "İpotek Teminatlı Menkul Kıymetler (İTMK): Konut finansmanı kuruluşlarının bilanço içi ipotekli konut kredileri teminat gösterilerek ihraç ettiği yüksek güvenlikli tahvillerdir.",
                    "Kira Sertifikaları (Sukuk) ve Varlık Kiralama Şirketleri (VKŞ): Kira sertifikaları; faizsiz finans ilkelerine uygun olarak varlık veya hakların getirisine ortaklık sağlayan menkul kıymetlerdir. Kira sertifikaları MÜNHASIRAN Sermaye Piyasası Kurulu'ndan izin alınarak kurulan 'Varlık Kiralama Şirketleri' (VKŞ) tarafından ihraç edilir.",
                    "Başlıca Sukuk Türleri: Sahipliğe Dayalı (İcara - Varlık kiralanır), Yönetim Sözleşmesine Dayalı (Vekalet), Ortaklığa Dayalı (Mudaraba / Müşareke) ve Alım-Satıma Dayalı (Murabaha)."
                ],
                "concrete_examples": [
                    "Piyasa Örneği: Hazine ve Maliye Bakanlığı ya da bir katılım bankası sukuk ihraç etmek istediğinde, kamuya ait bir otoyolu veya binayı VKŞ'ye devreder; VKŞ kira sertifikası satıp parayı toplar, varlığı tekrar kiralayarak elde ettiği kira bedelini yatırımcılara kupon ödemesi olarak dağıtır."
                ],
                "key_takeaways": [
                    "Kira sertifikalarını sadece anonim şirket şeklinde kurulan Varlık Kiralama Şirketleri (VKŞ) ihraç edebilir.",
                    "VDMK ve İTMK teminat havuzundaki alacaklar, ihraççı iflas etse dahi kamu alacakları dahil hiçbir borç için haczedilemez."
                ],
                "exam_traps": [
                    "⚠️ DİKKAT: Normal bir ticari şirket kendi doğrudan unvanıyla sukuk ihraç edemez; mutlaka bir VKŞ kurmak zorundadır."
                ],
                "tables": [
                    {
                        "headers": ["Araç", "İhraççı Tüzel Kişilik", "Dayanak Varlık", "Temel Güvence"],
                        "rows": [
                            ["Kira Sertifikası (Sukuk)", "Varlık Kiralama Şirketi (VKŞ)", "Taşınmaz, hak veya gelir akışı", "Mülkiyet veya kira sözleşmesi"],
                            ["VDMK", "Fon Kurucusu / İpotek Finansmanı Kur.", "Tüketici, taşıt, ihracat alacakları", "Teminat havuzunun haczedilemezliği"],
                            ["İTMK", "Konut Finansmanı Kuruluşları", "İpotekli konut kredisi havuzu", "Bilanço içi teminat kütüğü"]
                        ]
                    }
                ]
            },
            {
                "id": "sec_1003_06",
                "title": "6. Türev Araçlar, VİOP İşlemleri ve Varantlar (Margin Call Mekanizması)",
                "content": [
                    "Türev Araçlar; değeri dayanak bir varlığın (hisse senedi, endeks, döviz, emtia, faiz) fiyatına bağlı olan finansal sözleşmelerdir. Borsa İstanbul bünyesinde Vadeli İşlem ve Opsiyon Piyasası'nda (VİOP) işlem görürler.",
                    "1. Vadeli İşlem Sözleşmesi (Futures - İki Taraflı Zorunlu Sözleşme):\n• Alıcı ve satıcıya gelecekteki belirli bir tarihte, önceden sabitlenen fiyattan belirli miktarda varlığı alma veya satma YÜKÜMLÜLÜĞÜ getirir.\n• Benzetme: Çiftçi ile fırıncının 3 ay sonra 1 ton buğdayı kilosu 10 TL'den alıp satmak üzere bağlayıcı sözleşme imzalaması gibidir. 3 ay sonra buğday piyasada 20 TL de olsa 5 TL de olsa İKİ TARAF DA İŞLEMİ 10 TL'DEN YAPMAK ZORUNDADIR. Cayma veya vazgeçme hakkı yoktur.\n• Teminat & Risk: Her iki taraf da Takasbank'a başlangıç teminatı yatırır. Fiyat ters giderse zarar teorik olarak sınırsızdır ve günlük teminat tamamlama çağrısı (Margin Call) uygulanır.",
                    "2. Opsiyon Sözleşmesi (Options - Ev Kaporası & Sigorta Mantığı):\n• Alıcıya belirli bir vadede veya vadeye kadar, önceden belirlenen kullanım fiyatından dayanak varlığı ALMA HAKKI (Call Option) veya SATMA HAKKI (Put Option) veren sözleşmelerdir.\n• Benzetme (Alım Opsiyonu / Call): Beğendiğiniz 5 Milyon TL'lik bir ev için ev sahibine 100.000 TL kapora (prim) verip '1 ay boyunca bu evi 5 Milyona alma hakkı' satın aldınız. 1 ay sonra evin fiyatı 7 Milyona çıkarsa hakkınızı kullanır evi 5 Milyona alırsınız. Ancak evin fiyatı 3 Milyona düşerse evi almaktan VAZGEÇERSİNİZ; tek kaybınız baştaki 100.000 TL kapora (prim) olur.\n• ALICI İÇİN HAKTIR: Alıcı sadece prim öder. Hak sahibidir; piyasa aleyhine giderse hakkını kullanmaktan vazgeçebilir. Riski kesin olarak ödediği primle sınırlıdır; teminat yatırmaz ve Margin Call uygulanmaz.\n• SATICI (YAZICI) İÇİN YÜKÜMLÜLÜKTÜR: Primi peşin tahsil eder ancak alıcı hakkını kullanmak isterse sözleşme şartlarını eksiksiz yerine getirmek ZORUNDADIR. Kazancı aldığı primle sınırlı, zararı teorik olarak sınırsızdır; bu yüzden teminat yatırır ve Margin Call uygulanır.",
                    "3. Varantlar (Warrants - Menkul Kıymetleştirilmiş Banka Opsiyonu):\n• Sahibine belirli bir vadede veya tarihe kadar, önceden belirlenen fiyattan dayanak varlığı alma veya satma hakkı veren 'menkul kıymet niteliğindeki' opsiyonlardır.\n• VİOP opsiyonlarından farkı: Varantlar Borsa İstanbul Pay Piyasası'nda tıpkı bir hisse senedi gibi işlem görür. İhraççısı daima yetkili bir banka veya aracı kurumdur (yatırımcı satıcı/yazıcı olamaz, sadece alıcı olabilir).\n• Varant alan yatırımcı sadece primi öder; teminat yatırmaz, margin call (teminat tamamlama) riski yoktur ve maksimum kaybı ödediği prim tutarı kadardır.",
                    "4. Teminat Tamamlama Çağrısı (Margin Call Mekanizması):\n• Vadeli işlemlerde pozisyon açılırken 'Başlangıç Teminatı' yatırılır. Fiyatlar ters gittiğinde hesap bakiyesi 'Sürdürme Teminatı' seviyesinin altına düşerse, Takasbank aracı kuruma ve yatırımcıya teminatı tekrar BAŞLANGIÇ SEVİYESİNE tamamlaması için Teminat Tamamlama Çağrısı (Margin Call) yapar."
                ],
                "concrete_examples": [
                    "Piyasa Örneği: Yatırımcı VİOP'ta 100.000 TL'lik BIST 30 vadeli kontratı için 15.000 TL başlangıç teminatı yatırır. Sürdürme teminatı 11.000 TL'dir. Endeks düşüp hesap bakiyesi 9.000 TL'ye indiğinde, Takasbank yatırımcıya aynı gün saat 15:00'e kadar hesabını tekrar 15.000 TL'ye tamamlaması için (6.000 TL nakit yatırması için) Margin Call gönderir. Yatırmazsa pozisyonu resen kapatılır."
                ],
                "key_takeaways": [
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
                ],
                "tables": [
                    {
                        "headers": ["Özellik", "Futures (Vadeli İşlem)", "Options (Opsiyon)", "Varant (Warrant)"],
                        "rows": [
                            ["Yükümlülük Durumu", "Her iki taraf da zorunlu yükümlü", "Alıcı hak sahibi, satıcı yükümlü", "Alıcı hak sahibi, ihraççı yükümlü"],
                            ["Zarar Riski", "Teorik olarak sınırsız", "Alıcı için primle sınırlı, satıcı için sınırsız", "Ödenen primle sınırlı"],
                            ["Teminat Mekanizması", "Başlangıç + Sürdürme (Margin Call)", "Opsiyon satıcısı için teminat zorunlu", "Alıcı için teminat yok, sadece peşin prim"]
                        ]
                    }
                ]
            },
            {
                "id": "sec_1003_07",
                "title": "7. Pay Benzeri Menkul Kıymetler (PDT, DET, KİS, OYP) ve Varant Risk Göstergeleri (Greeks)",
                "content": [
                    "Sermaye piyasasında hisse senedi ve klasik tahvillerin dışında hem borç hem ortaklık unsurlarını barındıran melez (hibrit) menkul kıymetler bulunmaktadır:",
                    "1. Paya Dönüştürülebilir Tahvil (PDT): Sahibine vadesinde tahvili ihraç eden şirketin paylarına dönüştürme hakkı verir.",
                    "2. Değiştirilebilir Tahvil (DET): PDT'den farklı olarak ihraççı şirketin değil, başka bir şirketin (genellikle iştirakinin veya borsada işlem gören başka payların) paylarıyla değiştirme hakkı verir.",
                    "3. Katılma İntifa Senetleri (KİS): Şirket sermayesinde pay temsil etmez, oy hakkı ve yönetim hakkı vermez; yalnızca şirket kârından, tasfiye artığından pay alma veya yeni pay alma hakkı tanır.",
                    "4. Oydan Yoksun Paylar (OYP): Genel kurulda oy hakkı bulunmayan ancak kâr dağıtımında imtiyaz sağlanan paylardır.",
                    "Varant ve Opsiyonlarda Risk Göstergeleri (Greeks):\n• Delta: Dayanak varlığın fiyatındaki 1 birimlik değişimin varant fiyatına etkisidir.\n• Gama: Dayanak varlık fiyatı değiştikçe Delta'nın ne hızla değiştiğini gösterir.\n• Teta (Theta): Vadeye yaklaştıkça varant değerindeki günlük zaman erimesini (time decay) ölçer.\n• Vega: Dayanak varlığın zımni volatilitesindeki %1'lik değişimin varant fiyatına etkisidir.\n• Ro (Rho): Faiz oranlarındaki değişimin varant fiyatına etkisidir."
                ],
                "concrete_examples": [
                    "Piyasa Örneği: Bir holding nakit faiz ödemek yerine DET ihraç eder. Vade sonunda yatırımcı tahvilini nakit almak yerine holdingin borsadaki dev iştirakinin hisselerine dönüştürerek yüksek getiri elde edebilir."
                ],
                "key_takeaways": [
                    "PDT ihraççının kendi payına, DET ise başka bir şirketin payına dönüşür.",
                    "KİS sermaye payı temsil etmez ve asla oy hakkı tanımaz.",
                    "Teta (Theta) opsiyon ve varantlarda zaman aşınmasını ölçen en kritik parametredir."
                ],
                "exam_traps": [
                    "⚠️ DİKKAT: 'KİS sahipleri genel kurulda yönetim kurulu üyesi seçebilir' ifadesi kesinlikle YANLIŞTIR. KİS oy hakkı vermez."
                ],
                "tables": [
                    {
                        "headers": ["Parametre (Greek)", "Ölçtüğü Risk Faktörü", "Varant Fiyatına Etkisi"],
                        "rows": [
                            ["Delta", "Dayanak Varlık Fiyat Değişimi", "Alım varantında pozitif (0 ile 1), Satımda negatif (-1 ile 0)"],
                            ["Gama", "Delta'nın Değişim Hızı", "Kullanım fiyatına yaklaştıkça en yüksek seviyeye çıkar"],
                            ["Teta (Theta)", "Zaman Erimesi (Vadeye Kalan Gün)", "Vadeye yaklaştıkça varantın değerini sürekli aşındırır (-)"],
                            ["Vega", "Zımni Oynaklık (Volatilite)", "Volatilite arttıkça varant fiyatı yükselir (+)"],
                            ["Ro (Rho)", "Piyasa Faiz Oranları Değişimi", "Faiz arttıkça alım varantı hafif yükselir, satım düşer"]
                        ]
                    }
                ]
            }
        ]
    },

    # =========================================================================
    # MODÜL 1005: YATIRIM KURULUŞLARI
    # =========================================================================
    "1005": {
        "module_id": "1005",
        "module_name": "Yatırım Kuruluşları",
        "title": "Yatırım Kuruluşları Kapsamlı Sınav Hazırlık Kılavuzu",
        "total_sections": 8,
        "sections": [
            {
                "id": "sec_1005_01",
                "title": "1. Yatırım Hizmetleri, Faaliyetleri ve Yan Hizmetlerin Hukuki Kapsamı",
                "content": [
                    "6362 sayılı Kanun m.37 uyarınca Yatırım Hizmet ve Faaliyetleri; aracı kurumlar ve yetkilendirilmiş bankalar tarafından Sermaye Piyasası Kurulu'ndan yetki belgesi alınarak yürütülen temel finansal faaliyetlerdir.",
                    "Temel Yatırım Hizmet ve Faaliyetleri:\n1. Emir İletimine Aracılık (Müşteri emirlerinin işlem yapılmak üzere başka bir kuruma iletilmesi)\n2. İşlem Aracılığı (Emirlerin müşteri nam ve hesabına borsa pazarında bizzat eşleştirilmesi)\n3. Portföy Aracılığı (Sermaye piyasası araçlarının kendi nam ve hesabına alınıp satılması)\n4. Bireysel Portföy Yöneticiliği (Müşteriyle vekil ilişkisi içinde portföyün yönetilmesi)\n5. Yatırım Danışmanlığı (Yönlendirici nitelikte kişiye özel yatırım tavsiyesi verilmesi)\n6. Halka Arza Aracılık (Yüklenimde bulunarak veya en iyi gayret esasıyla satışa aracılık)\n7. Saklama Hizmeti (Müşterilere ait varlıkların saklanması ve idaresi)",
                    "Yan Hizmetler: Kredi açma, döviz işlemleri, kurumsal finansman danışmanlığı, sermaye piyasası araştırması gibi ek hizmetlerdir; tek başlarına icra edilemezler."
                ],
                "concrete_examples": [
                    "Piyasa Örneği: Bir aracı kurum bir şirketin halka arzında 'Halka arza aracılık - En iyi gayret' yetki belgesiyle çalışıyorsa satılamayan payları satın alma taahhüdü vermez; sadece satışa aracılık eder. 'Bakiye yüklenimi' yapıyorsa satılamayan tüm payları kendi parasıyla satın almak zorundadır."
                ],
                "key_takeaways": [
                    "Yatırım hizmet ve faaliyetleri sadece SPK'dan yetki belgesi alınarak yürütülebilir.",
                    "Portföy aracılığı aracı kurumun kendi nam ve hesabına işlem yapmasıdır.",
                    "Yatırım danışmanlığı kişiye özel tavsiye sunmaktır; genel bülten hazırlamak yatırım danışmanlığı sayılmaz."
                ],
                "exam_traps": [
                    "⚠️ DİKKAT: Bankalar 'Portföy Aracılığı' yetkisi kapsamında Borsa İstanbul Pay Piyasası'nda hisse senetlerinde kendi nam ve hesaplarına işlem yapamazlar; hisse senedi işlemleri münhasıran aracı kurumlarca yapılır."
                ],
                "tables": [
                    {
                        "headers": ["Yatırım Hizmeti", "Tanım", "Yetkili Kuruluşlar"],
                        "rows": [
                            ["Emir İletimine Aracılık", "Emrin başka bir kuruma aktarılması (Acentelik)", "Dar, Kısmi, Geniş Yetkili Aracı Kurumlar"],
                            ["Portföy Aracılığı", "Kendi nam ve hesabına alım satım", "Kısmi ve Geniş Yetkili Aracı Kurumlar"],
                            ["Bireysel Portföy Yöneticiliği", "Vekaletle portföy idaresi", "Portföy Yönetim Şirketleri ve Geniş Yetkililer"],
                            ["Yatırım Danışmanlığı", "Kişiye özel analiz ve tavsiye", "Yetki belgeli Aracı Kurumlar ve PYŞ'ler"]
                        ]
                    }
                ]
            },
            {
                "id": "sec_1005_02",
                "title": "2. Aracı Kurum Sınıflandırması ve Asgari Sermaye Tabanları (25M / 75M / 150M TL)",
                "content": [
                    "Yatırım Kuruluşlarının Kuruluş ve Faaliyet Esasları Tebliği (III-39.1) uyarınca aracı kurumlar faaliyet kapsamlarına ve sermaye yeterliliklerine göre üç gruba ayrılır:",
                    "1. Dar Yetkili Aracı Kurumlar: Sadece emir iletimine aracılık, en iyi gayret halka arzı ve yatırım tavsiyesi sunabilirler. Kendi nam ve hesaplarına işlem yapamaz, kredili alım açamazlar. Asgari Özkaynak Tabanı: 25 MİLYON TL.",
                    "2. Kısmi Yetkili Aracı Kurumlar: Dar yetkililere ek olarak işlem aracılığı, kendi nam ve hesabına portföy aracılığı (hisse hariç veya belirli araçlarda) yapabilirler. Asgari Özkaynak Tabanı: 75 MİLYON TL.",
                    "3. Geniş Yetkili Aracı Kurumlar: Tüm yatırım hizmetlerini (portföy aracılığı, yüklenimli halka arz, kredili işlem, açığa satış, genel saklama) sunabilen tam kapsamlı kurumlardır. Asgari Özkaynak Tabanı: 150 MİLYON TL."
                ],
                "concrete_examples": [
                    "Piyasa Örneği: Yeni kurulan Delta Menkul Değerler A.Ş., müşterilerine kredili hisse senedi aldırmak ve halka arzlarda bakiye yüklenimi taahhüt etmek istiyorsa, kanunen 'Geniş Yetkili Aracı Kurum' olmak ve en az 150 Milyon TL asgari özkaynak tabanını sağlamak zorundadır."
                ],
                "key_takeaways": [
                    "Dar Yetkili Aracı Kurum Asgari Özsermayesi: 25 Milyon TL.",
                    "Kısmi Yetkili Aracı Kurum Asgari Özsermayesi: 75 Milyon TL.",
                    "Geniş Yetkili Aracı Kurum Asgari Özsermayesi: 150 Milyon TL.",
                    "Dar yetkili kurumlar kendi namlarına işlem ve kredili menkul kıymet işlemi yapamaz."
                ],
                "exam_traps": [
                    "⚠️ DİKKAT: Sınav sorularında sermaye tutarları sıklıkla sorulur: Dar: 25M, Kısmi: 75M, Geniş: 150M TL eşiklerini mutlaka ezberleyin."
                ],
                "tables": [
                    {
                        "headers": ["Aracı Kurum Sınıfı", "Asgari Özkaynak Şartı", "Yapabileceği Temel Faaliyetler", "Yasak Olan Faaliyetler"],
                        "rows": [
                            ["Dar Yetkili", "25 Milyon TL", "Emir iletimi, en iyi gayret halka arzı", "Kendi hesabına işlem, kredili işlem, saklama"],
                            ["Kısmi Yetkili", "75 Milyon TL", "İşlem aracılığı, portföy aracılığı", "Bakiye yüklenimi, genel saklama"],
                            ["Geniş Yetkili", "150 Milyon TL", "Tüm faaliyetler, kredili işlem, yüklenim", "Yasak yoktur (Tam Yetkili)"]
                        ]
                    }
                ]
            },
            {
                "id": "sec_1005_03",
                "title": "3. Müşteri Sınıflandırması: Genel Müşteri vs Profesyonel Müşteri",
                "content": [
                    "Yatırım Hizmetleri Tebliği (III-39.1) uyarınca yatırım kuruluşları müşterilerini hizmet sunmadan önce 'Genel Müşteri' veya 'Profesyonel Müşteri' olarak sınıflandırmak zorundadır.",
                    "Profesyonel Müşteri: Kendi yatırım kararlarını verebilecek ve maruz kaldığı riskleri değerlendirebilecek tecrübe, bilgi ve uzmanlığa sahip müşterilerdir. Doğrudan profesyonel sayılanlar: Bankalar, aracı kurumlar, sigorta şirketleri, emeklilik fonları, yatırım fonları, SPK'dan izinli diğer mali kuruluşlar.",
                    "Talep Üzerine Profesyonel Müşteri Olabilecek Kuruluşlar: Aşağıdaki üç şarttan en az ikisini sağlayan şirketler yazılı talepte bulunarak profesyonel müşteri statüsüne geçebilir:\n• Aktif toplamının en az 50 MİLYON TL olması,\n• Yıllık net satış hasılatının en az 90 MİLYON TL olması,\n• Özkaynaklarının en az 4,5 MİLYON TL olması.",
                    "Genel Müşteri: Profesyonel müşteri tanımı dışındaki tüm bireysel ve kurumsal yatırımcılardır. Mevzuatça en yüksek düzeyde korunurlar; kendilerine yazılı çerçeve sözleşmesi, detaylı risk bildirim formu verilmesi ve testlerin uygulanması zorunludur."
                ],
                "concrete_examples": [
                    "Piyasa Örneği: Aktif büyüklüğü 60 Milyon TL ve yıllık cirosu 100 Milyon TL olan bir tekstil şirketi iki kriteri aştığı için aracı kuruma yazılı başvurarak 'Profesyonel Müşteri' olabilir. Böylece kendisine her işlem öncesi uzun risk formları imzalatılması muafiyeti doğar."
                ],
                "key_takeaways": [
                    "Bankalar, aracı kurumlar ve emeklilik fonları doğrudan Profesyonel Müşteridir.",
                    "Şirketler için profesyonellik eşikleri: Aktif 50M TL, Satış Hasılatı 90M TL, Özkaynak 4.5M TL (en az ikisi).",
                    "Genel müşteriler mevzuatça en sıkı korunan yatırımcı grubudur."
                ],
                "exam_traps": [
                    "⚠️ DİKKAT: Bir bireysel yatırımcı çok zengin olsa bile aksini yazılı talep edip şartları sağlamadıkça kanunen 'Genel Müşteri' kabul edilir."
                ],
                "tables": [
                    {
                        "headers": ["Müşteri Grubu", "Hukuki Statü", "Risk Bildirim Seviyesi", "Uygunluk / Yerindelik Testi"],
                        "rows": [
                            ["Genel Müşteri", "Koruma en üst düzeydedir", "Eksiksiz detaylı risk bildirimi zorunlu", "Zorunludur"],
                            ["Profesyonel Müşteri", "Kendi riskini alabilir", "Genel risk bildirimi yeterlidir", "Bilgi seviyesi var kabul edilir"]
                        ]
                    }
                ]
            },
            {
                "id": "sec_1005_04",
                "title": "4. Uygunluk Testi (Suitability) vs Yerindelik Testi (Appropriateness)",
                "content": [
                    "Yatırım kuruluşlarının müşterilerine sundukları ürün ve hizmetlerin risk derecesi ile müşterinin profilini eşleştirmek için iki farklı yasal test uygulanır:",
                    "1. Uygunluk Testi: Genel alım-satım aracılığı hizmetinde uygulanır. Müşterinin sermaye piyasası aracının risklerini anlayabilecek 'bilgi ve tecrübeye' sahip olup olmadığını ölçer. Müşteri testi doldurmak istemezse veya ürün uygun çıkmazsa, kurum müşteriyi yazılı uyararak işlemi müşterinin kendi sorumluluğunda gerçekleştirebilir.",
                    "2. Yerindelik Testi: Portföy Yöneticiliği ve Yatırım Danışmanlığı hizmetlerinde uygulanması KANUNEN ZORUNLUDUR. Uygunluk testinden farklı olarak; müşterinin mali gücünü (mali durumunu, gelirini, portföy büyüklüğünü) ve yatırım amaçlarını (risk toleransı, vade tercihi) da kapsar.",
                    "En Kritik Fark: Yerindelik testinde müşteri mali durumunu ve yatırım amaçlarını açıklamazsa, aracı kurum o müşteriye Portföy Yöneticiliği veya Yatırım Danışmanlığı hizmeti KESİNLİKLE VEREMEZ."
                ],
                "concrete_examples": [
                    "Piyasa Örneği: Mehmet Bey aracı kuruma gidip 'Bana özel portföy yöneticiliği yapın' derse, kurum Yerindelik Testi yapmak zorundadır. Mehmet Bey 'Maaşımı ve malvarlığımı söylemem' derse, kurum kanunen ona portföy yöneticiliği hizmeti sunamaz, sözleşme imzalayamaz."
                ],
                "key_takeaways": [
                    "Uygunluk Testi: Alım-Satım aracılığında bilgi ve tecrübeyi ölçer.",
                    "Yerindelik Testi: Portföy Yöneticiliği ve Yatırım Danışmanlığında zorunludur; bilgi + mali güç + yatırım amacını ölçer.",
                    "Yerindelik testi olmadan portföy yöneticiliği yapılamaz."
                ],
                "exam_traps": [
                    "⚠️ DİKKAT: 'Uygunluk testi portföy yöneticiliğinde yeterlidir' ifadesi YANLIŞTIR. Portföy yöneticiliğinde mutlaka 'Yerindelik Testi' aranır."
                ],
                "tables": [
                    {
                        "headers": ["Test Türü", "Zorunlu Olduğu Hizmet", "Ölçülen Kriterler", "Bilgi Verilmezse Sonuç"],
                        "rows": [
                            ["Uygunluk Testi", "Genel Alım-Satım Aracılığı", "Yatırımcının Bilgi ve Tecrübesi", "Yazılı uyarı ile işlem yapılabilir"],
                            ["Yerindelik Testi", "Portföy Yöneticiliği & Yatırım Danışmanlığı", "Bilgi + Mali Durum + Yatırım Amacı", "Hizmet kesinlikle verilemez"]
                        ]
                    }
                ]
            },
            {
                "id": "sec_1005_05",
                "title": "5. Kredili Menkul Kıymet Alımı, Açığa Satış ve Özkaynak Oranları (%35 / %20)",
                "content": [
                    "Kredili Menkul Kıymet İşlemleri Tebliği (Seri: V, No: 65) uyarınca aracı kurumlar müşterilerine menkul kıymet alımı için kredi kullandırabilir veya açığa satış yaptırabilirler.",
                    "Başlangıç Özkaynak Oranı (%35 Kuralı): Yatırımcının kredili işlem yapabilmesi için emir anında hesabında bulundurması gereken asgari özkaynak oranı EN AZ %35'TİR. (Örn: 100.000 TL'lik hisse alacaksa en az 35.000 TL özkaynak yatırmalı, en fazla 65.000 TL kredi kullanabilir).",
                    "Sürdürme Özkaynak Oranı (%20 Kuralı): Piyasadaki fiyat düşüşleri sonucunda özkaynak oranının düşebileceği asgari yasal sınır %20'DİR.",
                    "Özkaynak Tamamlama Bildirimi ve Resen Satış: Müşterinin özkaynak oranı %20'nin altına düşerse, aracı kurum müşteriye aynı gün bildirimde bulunarak özkaynağını tekrar %35'e tamamlamasını ister. Müşteri bildirilen süre içinde teminatı tamamlamazsa, aracı kurum müşterinin onayını aramaksızın rehinli payları borsada satarak krediyi resen kapatır."
                ],
                "concrete_examples": [
                    "Piyasa Örneği: Can Bey 35.000 TL nakit koyup 65.000 TL krediyle 100.000 TL'lik BIST hissesi alır (Özkaynak %35). Hisse değeri 75.000 TL'ye düşerse: Kredi borcu 65.000 TL bakiye kalır, Can Bey'in özkaynağı 10.000 TL'ye iner. Özkaynak oranı 10.000 / 75.000 = %13.3 olur (%20'nin altına düşer). Kurum Can Bey'e tamamlama çağrısı yapar; para gelmezse hisseleri borsada satar."
                ],
                "key_takeaways": [
                    "Asgari Başlangıç Özkaynak Oranı: Kesin olarak %35.",
                    "Asgari Sürdürme Özkaynak Oranı: Kesin olarak %20.",
                    "Özkaynak oranı %20'nin altına düşerse tamamlanması gereken hedef oran tekrar %35'tir."
                ],
                "exam_traps": [
                    "⚠️ DİKKAT: Özkaynak %20'nin altına indiğinde müşteri sadece %20'ye kadar değil, en baştaki '%35 Başlangıç Seviyesi'ne kadar teminat tamamlamak zorundadır."
                ],
                "tables": [
                    {
                        "headers": ["Aşama", "Yasal Asgari Oran", "Mali Durum", "Uygulanan Prosedür"],
                        "rows": [
                            ["Pozisyon Açılışı", "%35 Başlangıç Özkaynağı", "Portföyün en az %35'i müşterinin kendi parasıdır", "Kredi kullandırılır"],
                            ["Pozisyon Devamı", "%20 Sürdürme Özkaynağı", "Fiyat düşüşlerine karşı asgari tampon", "İşlem serbestçe devam eder"],
                            ["Kritik Eşik Aşımı", "< %20 Kritik Seviye", "Temerrüt ve batık riski", "Özkaynak tamamlama çağrısı ve resen satış"]
                        ]
                    }
                ]
            },
            {
                "id": "sec_1005_06",
                "title": "6. Kaldıraçlı Alım Satım (Forex / FX) İşlemleri ve Yasal Kaldıraç Sınırı (1:10)",
                "content": [
                    "Kaldıraçlı Alım Satım (Forex / FX) İşlemleri; yatırılan teminat tutarının belirli bir katına kadar döviz, emtia ve kıymetli maden paritelerinde iki yönlü alım-satım yapılmasına imkan tanıyan türev işlemlerdir.",
                    "Yasal Kaldıraç Sınırı (1:10 Kuralı): SPK düzenlemeleri uyarınca yurt içi yerleşik bireysel yatırımcılara uygulanabilecek azami yasal kaldıraç oranı 1:10 OLARAK SINIRLANDIRILMIŞTIR. Yatırımcı yatırdığı teminatın en fazla 10 katı büyüklüğünde pozisyon açabilir.",
                    "Asgari Başlangıç Teminatı: Kaldıraçlı işlemlere başlayabilmek için müşterinin yatırması zorunlu asgari başlangıç teminatı tutarı 50.000 TL veya muadili dövizdir.",
                    "Yetki Belgesi Şartı: Forex işlemleri yalnızca SPK'dan 'Kaldıraçlı Alım Satım Yetki Belgesi' almış Geniş Yetkili Aracı Kurumlar tarafından yaptırılabilir. Yurt dışı lisanssız sitelerde işlem yaptırmak suçtur."
                ],
                "concrete_examples": [
                    "Piyasa Örneği: 50.000 TL başlangıç teminatı ile hesap açan bir yatırımcı, 1:10 azami kaldıraç kuralı gereği en fazla 500.000 TL büyüklüğünde Dolar/TL veya Altın/Dolar pozisyonu açabilir. Aracı kurum müşteriye 1:50 veya 1:100 kaldıraç verirse SPK tarafından ağır idari para cezası ve yetki iptali ile cezalandırılır."
                ],
                "key_takeaways": [
                    "Azami yasal kaldıraç sınırı: 1:10.",
                    "Asgari başlangıç teminatı: 50.000 TL veya muadili döviz.",
                    "Kaldıraçlı işlemlerde müşteriye kesin kâr garantisi veya zarar etmeme taahhüdü verilmesi kesinlikle yasaktır."
                ],
                "exam_traps": [
                    "⚠️ DİKKAT: Yurt dışındaki 1:100, 1:400 gibi kaldıraç oranları Türkiye'de kanunen yasaktır; yasal azami sınır kesin olarak '1:10'dur."
                ],
                "tables": [
                    {
                        "headers": ["Parametre", "SPK Yasal Sınırı", "Sınav Notu"],
                        "rows": [
                            ["Azami Kaldıraç", "1:10 (Teminatın 10 Katı)", "Hiçbir kurum 1:10 oranını aşamaz"],
                            ["Asgari Başlangıç Teminatı", "50.000 TL veya muadili döviz", "Hesap açılışında zorunlu asgari bakiye"],
                            ["Yetkili Kurum Türü", "Geniş Yetkili Aracı Kurumlar", "Dar yetkililer forex işlemi yapamaz"]
                        ]
                    }
                ]
            },
            {
                "id": "sec_1005_07",
                "title": "7. Müşteri Varlıklarının Ayrılığı ve Yatırımcı Tazmin Merkezi (YTM)",
                "content": [
                    "Müşteri Varlıklarının Ayrılığı İlkesi (SPKn m.46): Yatırım kuruluşları, müşterilerine ait nakit ve menkul kıymetleri kendi malvarlıklarından kesin olarak ayrı tutmak zorundadır. Müşterilere ait nakitler Takasbank nezdindeki müşteri hesaplarında, sermaye piyasası araçları ise MKK nezdinde hak sahipleri bazında alt hesaplarda izlenir. Kurum mali sıkıntıya düşse dahi müşteri varlıkları haczedilemez ve iflas masasına dahil edilemez.",
                    "Yatırımcı Tazmin Merkezi (YTM): Hakkında tedrici tasfiye veya iflas kararı verilen yatırım kuruluşlarının, yatırım hizmet ve faaliyetlerinden kaynaklanan müşterilerine ait nakit ve menkul kıymet teslim yükümlülüklerini yerine getirememesi halinde devreye giren kamu tüzel kişiliğine haiz teminat kurumudur.",
                    "Tazmin Kapsamı ve Limiti: YTM sadece hırsızlık, suiistimal, iflas ve teslim edememe durumlarını tazmin eder; piyasa fiyatlarındaki düşüşten kaynaklanan borsa zararlarını tazmin etmez. Kanuni tazmin üst limiti her yıl yeniden değerleme oranında artırılır."
                ],
                "concrete_examples": [
                    "Piyasa Örneği: İflas eden bir aracı kurumdaki yatırımcının 500.000 TL değerinde hissesi MKK'da kendi adına kayıtlı olduğu için doğrudan korunur ve başka kuruma virmanlanır. Kurumun zimmetine geçirdiği veya teslim edemediği nakitler ise YTM tarafından yasal limit dahilinde nakden tazmin edilir."
                ],
                "key_takeaways": [
                    "Müşteri hisseleri MKK'da, nakitleri Takasbank'ta müşteri adına ayrı saklanır.",
                    "YTM piyasa zararını değil, aracı kurumun batması sonucu teslim edemediği varlıkları tazmin eder.",
                    "YTM'nin gelirleri üye kurumların ödediği aidatlardan ve zamanaşımına uğrayan hesaplardan oluşur."
                ],
                "exam_traps": [
                    "⚠️ DİKKAT: 'Borsada hisse senetleri değer kaybedip para kaybeden yatırımcı YTM'ye başvurarak zararını tahsil eder' ifadesi sınavda en çok sorulan YANLIŞ çeldiricidir."
                ],
                "tables": [
                    {
                        "headers": ["Risk Türü", "YTM Tazmin Eder mi?", "Hukuki Açıklama"],
                        "rows": [
                            ["Aracı Kurumun İflası", "EVET, Tazmin Eder", "Teslim edilemeyen nakit ve hisseler limit dahilinde ödenir"],
                            ["Kurum Çalışanının Zimmeti", "EVET, Tazmin Eder", "Müşteri hesabından izinsiz çalınan varlıklar karşılanır"],
                            ["Borsa Fiyatının Taban Yapması", "HAYIR, Tazmin Etmez", "Piyasa ve yatırım riski tamamen yatırımcıya aittir"]
                        ]
                    }
                ]
            },
            {
                "id": "sec_1005_08",
                "title": "8. İç Sistemler, Uyum Görevlisi (Compliance) ve Müşteri Emirlerinin İcrası (En İyi İcra - Best Execution)",
                "content": [
                    "Yatırım kuruluşları kurumsal risklerini yönetmek ve sermaye piyasası mevzuatına tam uyumu sağlamak amacıyla bünyelerinde bağımsız 'İç Sistemler' kurmak zorundadır. İç Sistemler; İç Denetim (Teftiş Kurulu), İç Kontrol ve Risk Yönetimi birimlerinden oluşur.",
                    "Uyum Görevlisi (Compliance Officer): Yatırım kuruluşunun tüm faaliyetlerinin SPK mevzuatına, borsa kurallarına, TSPB meslek ilkelerine ve MASAK (Suç Gelirlerinin Aklanmasının Önlenmesi) mevzuatına uygunluğunu izlemek ve raporlamakla yükümlü kilit yöneticidir.",
                    "Müşteri Emirlerine Öncelik ve Zaman Önceliği Kuralı: Yatırım kuruluşları müşteri emirlerini aldıkları an zaman damgasıyla kaydederler. Bir yatırım kuruluşu veya personeli, kendi nam ve hesabına yapacağı işlemler için müşterinin bekleyen aynı yönlü emrinden önce sisteme emir giremez.",
                    "Öncelikli İşlem Yasağı (Front-Running): Müşteriden gelen büyük hacimli bir alım emrini borsaya iletmeden önce, hissenin fiyatının yükseleceğini bilerek kendi şahsi hesabından önceden o hisseden alım yapmak ağır bir piyasa suçudur.",
                    "Personel İşlem Yasakları: Aracı kurum çalışanları sermaye piyasası araçlarında kısa vadeli spekülatif işlem yapamazlar; satın aldıkları payları EN AZ 30 GÜN boyunca ellerinde tutmak zorundadırlar (30 gün elde tutma kuralı)."
                ],
                "concrete_examples": [
                    "Piyasa Örneği: Kurumsal bir fon müşterisi aracı kurumu arayıp 5 milyon lotluk dev bir X hissesi alım emri verdiğinde; aracı kurum brokerı bu emri borsaya girmeden 1 dakika önce kendi şahsi hesabından 10.000 lot X hissesi alırsa 'Front-Running' yapmış olur. SPK bu işlemi tespit ettiğinde işlem yasağı, lisans iptali ve hapis istemiyle savcılığa suç duyurusunda bulunur."
                ],
                "key_takeaways": [
                    "İç Sistemler üç ayaktan oluşur: İç Denetim, İç Kontrol, Risk Yönetimi.",
                    "Müşteri emri daima kurumun ve personelin kendi işleminden önce gelir (Müşteri emrine öncelik).",
                    "Aracı kurum personeli aldığı hisse senedini en az 30 gün satamaz (30 gün elde tutma zorunluluğu)."
                ],
                "exam_traps": [
                    "⚠️ DİKKAT: Aracı kurum çalışanlarının hisse senedi alması tamamen yasak değildir; ancak kendi çalıştıkları kurumda hesap açmak ve aldıkları hisseyi en az 30 gün elde tutmak zorundadırlar."
                ],
                "tables": [
                    {
                        "headers": ["Kural / İlke", "Yasal Düzenleme", "Yasaklanan Eylem"],
                        "rows": [
                            ["Öncelikli İşlem Yasağı (Front-Running)", "SPKn & Yatırım Tebliği", "Müşteri emrinden önce kendi hesabına işlem yapma"],
                            ["Personel İşlem Sınırı", "En az 30 Gün Elde Tutma", "Kısa vadeli spekülatif al-sat yapma yasağı"],
                            ["En İyi İcra (Best Execution)", "Müşteri Lehine En İyi Fiyat", "Emri bilerek kötü fiyattan eşleştirme yasağı"],
                            ["Uyum Birimi Raporlaması", "Doğrudan Yönetim Kuruluna", "İcracı genel müdür yardımcısına bağlanamaz"]
                        ]
                    }
                ]
            }
        ]
    },

    # =========================================================================
    # MODÜL 1012: TAKAS, SAKLAMA VE OPERASYON İŞLEMLERİ
    # =========================================================================
    "1012": {
        "module_id": "1012",
        "module_name": "Takas, Saklama ve Operasyon İşlemleri",
        "title": "Takas ve Saklama Kapsamlı Sınav Hazırlık Kılavuzu",
        "total_sections": 7,
        "sections": [
            {
                "id": "sec_1012_01",
                "title": "1. Takas ve Saklamanın Temel Esasları & Teslim Karşılığı Ödeme (DVP İlkesi)",
                "content": [
                    "Sermaye piyasasında alım-satım emrinin borsada eşleşmesi işlemi başlatır; ancak işlemin nihai olarak tamamlanması 'Takas' ve 'Saklama' operasyonları ile gerçekleşir.",
                    "Merkezi Takas Kuruluşu: Türkiye'deki merkezi takas kuruluşu İstanbul Takas ve Saklama Bankası A.Ş.'dir (Takasbank). Takasbank, borsada gerçekleşen işlemlerin netleştirilmesini, nakit ve menkul kıymet takasını yürütür.",
                    "Teslim Karşılığı Ödeme (Delivery Versus Payment - DVP): Takas sisteminin en temel güvenlik direğidir. Menkul kıymet teslimi ile nakit ödemenin aynı anda, eşzamanlı olarak gerçekleştirilmesini emreder. Nakit ödenmedikçe menkul kıymet devredilmez; menkul kıymet verilmedikçe nakit serbest bırakılmaz.",
                    "DVP'nin Yok Ettiği Risk: DVP mekanizması, karşı tarafın menkul kıymeti alıp parayı ödememesi veya parayı alıp hisseyi teslim etmemesi riskini (Anapara Riski / Principal Risk) tamamen sıfırlar."
                ],
                "concrete_examples": [
                    "Piyasa Örneği: Ali Bey Borsa İstanbul'da 50.000 TL'lik hisse sattığında, Takasbank ve MKK sisteminde hisseler Ali Bey'in hesabından çıkıp alıcının hesabına geçerken, alıcının 50.000 TL nakdi de eşanlı olarak Ali Bey'in hesabına aktarılır. Böylece 'parayı verdim hisse gelmedi' riski ortadan kalkar."
                ],
                "key_takeaways": [
                    "Merkezi Takas Kuruluşu: Takasbank.",
                    "DVP ilkesi nakit ve menkul kıymetin eşanlı takaslanmasıdır.",
                    "DVP'nin temel amacı 'Anapara / Temerrüt Riskini' tamamen yok etmektir."
                ],
                "exam_traps": [
                    "⚠️ DİKKAT: DVP piyasa riskini (hisse fiyatının düşmesini) değil, takas teslimatındaki 'anapara temerrüt riskini' önler."
                ],
                "tables": [
                    {
                        "headers": ["İşlem Adımı", "Gerçekleştiren Kurum", "Operasyonel İşlev"],
                        "rows": [
                            ["İşlem Eşleşmesi", "Borsa İstanbul (BIST)", "Alıcı ve satıcı emirlerinin eşleşmesi"],
                            ["Takas ve Netleştirme", "Takasbank", "Borç ve alacakların netleştirilip takasa bağlanması"],
                            ["Mülkiyet Tescili", "Merkezi Kayıt Kuruluşu (MKK)", "Hak sahipleri adına kaydi pay transferi"]
                        ]
                    }
                ]
            },
            {
                "id": "sec_1012_02",
                "title": "2. Borsa İstanbul Piyasaları Standart Takas Süreleri (Valörleri - T+2 / T+0)",
                "content": [
                    "Borsa İstanbul'daki farklı pazarlarda gerçekleşen işlemlerin takas borç ve alacaklarının tasfiye edildiği kanuni valör süreleri farklıdır:",
                    "1. BIST Pay Piyasası (Hisse Senetleri): Standart takas süresi T+2'DİR (İşlem gününü izleyen İKİNCİ iş günü). Pazartesi günü alınan bir hissenin bedeli ve mülkiyeti Çarşamba günü takas edilir. Cuma günü yapılan işlemin takası ise araya hafta sonu girdiği için Salı günü gerçekleşir. T+2 günü nakit ve menkul kıymet teslim borçlarının tamamlanması gereken yasal son temerrüt saati ise 15:00'tir.",
                    "2. Borçlanma Araçları Piyasası (Tahvil ve Bono): Kesin alım-satım işlemleri kural olarak aynı gün (T+0) veya tarafların tercihine göre ertesi iş günü (T+1) valörle takas edilir.",
                    "3. Eurobond Piyasası: Uluslararası takas standartlarına uygun olarak kural olarak T+2 valörle takas edilir.",
                    "4. VİOP (Vadeli İşlemler): Pozisyon açılış teminatları anlık bloke edilir, günlük kâr/zarar nakit uzlaşması ise ertesi iş günü (T+1) seans açılışından önce hesaba yansıtılır."
                ],
                "concrete_examples": [
                    "Piyasa Örneği: Perşembe günü BIST Pay Piyasası'nda 100.000 TL'lik hisse senedi satan bir yatırımcının satış tutarı T+2 kuralı gereğince; Cuma (T+1), Cumartesi-Pazar (Tatil), Pazartesi (T+2) günü Takasbank nezdinde nakit olarak hesaba geçer."
                ],
                "key_takeaways": [
                    "BIST Pay Piyasası Takas Süresi: Kesin olarak T+2.",
                    "Borçlanma Araçları Piyasası (Tahvil/Bono): T+0 veya T+1.",
                    "VİOP nakit uzlaşması: T+1 günü sabahı."
                ],
                "exam_traps": [
                    "⚠️ DİKKAT: Cuma günü yapılan hisse senedi işleminin takası Pazar günü değil, takip eden 'SALI' günüdür (resmi tatiller iş günü sayılmaz)."
                ],
                "tables": [
                    {
                        "headers": ["Piyasa Türü", "İşlem Gören Araç", "Standart Takas Süresi (Valör)"],
                        "rows": [
                            ["Pay Piyasası", "Hisse Senetleri, BYF, Varant", "T+2 (İkinci İş Günü)"],
                            ["Borçlanma Araçları Piyasası", "Devlet Tahvili, Hazine Bonosu", "T+0 (Aynı Gün) veya T+1"],
                            ["Eurobond Pazarı", "Döviz Cinsinden Kamu/Şirket Tahvili", "T+2"],
                            ["VİOP", "Vadeli İşlem ve Opsiyon Sözleşmeleri", "T+1 (Kâr/Zarar Uzlaşması)"]
                        ]
                    }
                ]
            },
            {
                "id": "sec_1012_03",
                "title": "3. Takasbank Merkezi Karşı Taraf (CCP) Rolü ve Temerrüt Şelalesi (Default Waterfall)",
                "content": [
                    "Merkezi Karşı Taraf (Central Counterparty - CCP / MKT): Takasbank'ın takas işlemlerinde alıcıya karşı satıcı, satıcıya karşı alıcı konumuna geçerek takasın tamamlanmasını mali olarak garanti etmesidir.",
                    "CCP'nin Amacı: Piyasadaki aracı kurumlardan biri iflas etse veya borcunu ödeyemese dahi, diğer masum üyelerin işlemlerinin aksamadan tıkır tıkır gerçekleşmesini sağlamaktır.",
                    "Temerrüt Şelalesi (Default Waterfall) Öncelik Sıralaması: Bir üye aracı kurum takas yükümlülüğünü yerine getiremeyip temerrüde düştüğünde, Takasbank zararı kapatmak için kaynakları sırasıyla şu hiyerarşik sırayla kullanır:\n1. Adım: Temerrüde düşen üyenin yatırmış olduğu teminatlar (Marjinler),\n2. Adım: Temerrüde düşen üyenin Garanti Fonu'na yatırdığı katkı payı,\n3. Adım: Takasbank'ın kendi taahhüt ettiği özkaynak katkı payı (SITG - Skin in the Game),\n4. Adım: Temerrüt etmeyen diğer masum üyelerin Garanti Fonu katkı payları,\n5. Adım: Kalan zararın üyeler arasında oransal paylaştırılması."
                ],
                "concrete_examples": [
                    "Piyasa Örneği: X Yatırım Menkul Değerler 50 milyon TL'lik takas borcunu ödeyemezse, Takasbank önce X Yatırım'ın yatırdığı teminatları bozar. Yetmezse X Yatırım'ın Garanti Fonu payını kullanır. O da yetmezse Takasbank kendi ayırdığı sermaye tamponunu devreye sokar; en son çare olarak diğer üyelerin havuzundaki garanti fonuna başvurulur."
                ],
                "key_takeaways": [
                    "CCP uygulamasında takas odası (Takasbank) karşı taraf riskini üstlenir.",
                    "Temerrüt Şelalesi sıralaması: 1. Üyenin teminatı -> 2. Üyenin garanti fonu payı -> 3. Takasbank özkaynak katkısı -> 4. Diğer üyelerin garanti fonu payları.",
                    "Masum üyelerin garanti fonuna en son çare olarak başvurulur."
                ],
                "exam_traps": [
                    "⚠️ DİKKAT: 'Takasbank temerrüt halinde doğrudan diğer üyelerin parasını kullanır' ifadesi YANLIŞTIR. Önce mutlaka temerrüt eden üyenin kendi teminatları ve garanti fonu payı tüketilir."
                ],
                "tables": [
                    {
                        "headers": ["Şelale Sırası", "Kullanılan Kaynak", "Kimin Kaynağı?", "Öncelik Derecesi"],
                        "rows": [
                            ["1. Sıra", "Temerrüt Eden Üyenin Teminatları", "Borçlu Üyenin", "İlk Başvurulan Kaynak"],
                            ["2. Sıra", "Temerrüt Eden Üyenin Garanti Fonu Payı", "Borçlu Üyenin", "İkinci Başvurulan Kaynak"],
                            ["3. Sıra", "Takasbank Taahhütlü Özkaynak Katkısı", "Takasbank'ın", "Kurumun Kendi Özkaynağı"],
                            ["4. Sıra", "Diğer Üyelerin Garanti Fonu Katkı Payları", "Diğer Masum Üyelerin", "En Son Çare"]
                        ]
                    }
                ]
            },
            {
                "id": "sec_1012_04",
                "title": "4. Merkezi Kayıt Kuruluşu (MKK), Kaydileştirme ve Hak Sahipliği Sicili",
                "content": [
                    "Merkezi Kayıt Kuruluşu A.Ş. (MKK); sermaye piyasası araçlarının kaydileştirilmesine ilişkin işlemleri yürüten, bunların kayden izlendiği merkezi saklama kuruluşudur.",
                    "Kaydileştirme: Menkul kıymetlerin fiziki senet olarak basılmasından vazgeçilerek, bilgisayar ortamında elektronik veri olarak ihraç edilmesi ve hak sahipleri adına hesaplarda izlenmesidir.",
                    "MKK Kayıtlarının Kurucu Niteliği: 6362 sayılı Kanun m.13 uyarınca kaydi sermaye piyasası araçlarına ilişkin haklar MKK nezdindeki elektronik kayıtlara dayanır. Bu kayıtlar hak sahipliğini ispata yarayan tek yetkili kurucu hukuki sicildir.",
                    "Elektronik Hak Kullanımları: MKK sistemi; bedelli sermaye artırımı, bedelsiz sermaye artırımı, nakit kâr payı (temettü) dağıtımı ve kupon ödemesi gibi kurumsal işlemleri ihraççı şirket ile Takasbank arasında entegre ederek doğrudan yatırımcıların aracı kurumlardaki alt hesaplarına otomatik yansıtır."
                ],
                "concrete_examples": [
                    "Piyasa Örneği: Ereğli Demir Çelik A.Ş. temettü dağıttığında, yatırımcının eline çek veya makbuz verilmez; temettü günü MKK hak sahipliği listesini Takasbank'a iletir ve nakit para otomatik olarak yatırımcının aracı kurumdaki cari hesabına yatar."
                ],
                "key_takeaways": [
                    "Türkiye'nin Merkezi Saklama Kuruluşu: MKK.",
                    "MKK kayıtları kurucu hukuki sicil niteliğindedir.",
                    "Borsada işlem gören payların fiziki basımı veya fiziki teslimatı kanunen imkansızdır."
                ],
                "exam_traps": [
                    "⚠️ DİKKAT: MKK takas kuruluşu değildir; MKK 'Merkezi Saklama Kuruluşu'dur. Takas kuruluşu ise 'Takasbank'tır. Bu iki kurumun görevlerini sınavda karıştırmayın."
                ],
                "tables": [
                    {
                        "headers": ["Fonksiyon", "Yetkili Kuruluş", "Temel Görev"],
                        "rows": [
                            ["Merkezi Saklama & Hak Sahipliği Sicili", "Merkezi Kayıt Kuruluşu (MKK)", "Kaydileştirme, üye hesapları, e-YATIRIMCI"],
                            ["Merkezi Takas & Karşı Taraf", "Takasbank", "Netleştirme, nakit takası, temerrüt yönetimi"],
                            ["Organize Borsa İşlemleri", "Borsa İstanbul (BIST)", "Emir eşleştirme ve piyasa işletimi"]
                        ]
                    }
                ]
            },
            {
                "id": "sec_1012_05",
                "title": "5. MKK e-YATIRIMCI Güvenlik Blokajı ve Zamanaşımı Hükümleri (10 Yıl Kuralı)",
                "content": [
                    "MKK e-YATIRIMCI Sistemi: Yatırımcıların MKK nezdindeki hesaplarını e-Devlet veya MKK şifresiyle internet ve mobil uygulama üzerinden anlık takip edebildikleri dijital platformdur.",
                    "Yatırımcı Blokajı Hizmeti: Yatırımcılar e-YATIRIMCI üzerinden portföylerindeki paylara 'Yatırımcı Blokajı' koyabilirler. Blokaj aktifken aracı kurum veya üçüncü şahıslar yatırımcının rızası olmadan hiçbir şekilde hisse transferi veya satışı yapamaz. Yatırımcı satış yapacağı zaman blokajı saniyeler içinde kendisi kaldırır.",
                    "Zamanaşımı Hükümleri (10 Yıl Kuralı - SPKn m.83): Yatırım kuruluşları ve ihraççı ortaklıklar nezdinde 10 YIL BOYUNCA hiçbir işlem görmeyen ve hak sahipleri tarafından aranmayan her türlü sermaye piyasası aracı, nakit temettü ve faiz alacakları zamanaşımına uğrar.",
                    "YTM'ye Devir: 10 yıllık süre sonunda zamanaşımına uğrayan tüm bu varlıklar Yatırımcı Tazmin Merkezi'ne (YTM) intikal eder ve Hazineye gelir kaydedilir. Bu süreden sonra hak sahipleri hak iddia edemezler."
                ],
                "concrete_examples": [
                    "Piyasa Örneği: 2014 yılında dedesinden kalan hisse senetlerini unutan bir mirasçı, 10 yıl boyunca (2024 yılına kadar) hiçbir işlem yapmaz veya temettü talep etmezse, hisseler ve biriken nakit kâr payları kanunen zamanaşımına uğrayarak Yatırımcı Tazmin Merkezi'ne devredilir."
                ],
                "key_takeaways": [
                    "Sermaye piyasası araçlarında ve temettülerde zamanaşımı süresi: Tam 10 YILDIR.",
                    "Zamanaşımına uğrayan varlıklar Yatırımcı Tazmin Merkezi'ne (YTM) devredilir.",
                    "e-YATIRIMCI blokajı aracı kurumun müşteri rızası dışında virman yapmasını engeller."
                ],
                "exam_traps": [
                    "⚠️ DİKKAT: Zamanaşımı süresi 5 yıl veya 20 yıl değil, kesin olarak '10 YIL'dır.",
                    "⚠️ DİKKAT: Zamanaşımına uğrayan paylar aracı kuruma kâr kalmaz; kanunen YTM'ye aktarılır."
                ],
                "tables": [
                    {
                        "headers": ["Güvenlik & Hukuki Süreç", "Geçerli Kural / Süre", "Yasal Dayanak & Sonuç"],
                        "rows": [
                            ["e-YATIRIMCI Blokajı", "Anlık Açma / Kapama", "Müşteri rızası dışı transferleri %100 bloke eder"],
                            ["Zamanaşımı Süresi", "10 Yıl", "SPKn m.83 uyarınca hak düşürücü süre"],
                            ["Devredilen Kurum", "Yatırımcı Tazmin Merkezi (YTM)", "Hazineye gelir kaydedilir"]
                        ]
                    }
                ]
            },
            {
                "id": "sec_1012_06",
                "title": "6. Takasbank Para Piyasası (TPP) ve Ödünç Pay Piyasası (ÖPA)",
                "content": [
                    "Takasbank Para Piyasası (TPP): Takasbank üyelerinin (bankalar ve aracı kurumlar) kısa vadeli Türk Lirası likidite fazlalarını değerlendirdikleri veya likidite açıklarını kapattıkları organize para piyasasıdır.",
                    "TPP'nin İşleyişi: İşlemler 'Çok Taraflı Kör Havuz' sisteminde anonim olarak gerçekleşir; borç alan ve borç veren birbirinin kimliğini bilmez. Takasbank Merkezi Karşı Taraf (CCP) sıfatıyla takası garanti eder. Borçlanabilmek için Takasbank'ın kabul ettiği teminatlar (DİBS, BIST payları, nakit, döviz) rehin verilir.",
                    "Ödünç Pay Piyasası (ÖPA): Takasbank nezdinde pay piyasasında açığa satış yapan veya takas günü hisse teslim yükümlülüğünü yerine getiremeyen üyelerin, belirli bir faiz/komisyon ve teminat karşılığında hisse senedi ödünç alabildikleri organize piyasadır.",
                    "ÖPA'nın Faydası: Açığa satış yapan yatırımcının takas gününde hisseyi teslim edemeyip temerrüde düşmesini engeller ve piyasa likiditesini artırır."
                ],
                "concrete_examples": [
                    "Piyasa Örneği: Pazartesi günü açığa satış yapan bir aracı kurum Çarşamba günü takas saatine kadar hisseyi piyasadan geri alamadıysa, Takasbank Ödünç Pay Piyasası'na (ÖPA) girerek portföyünde o hisse bulunan başka bir kurumdan 3 günlüğüne hisse ödünç alır ve takas açığını kapatır."
                ],
                "key_takeaways": [
                    "Takasbank Para Piyasası (TPP) üyelerin kısa vadeli TL borçlanıp borç verdikleri kör havuz piyasasıdır.",
                    "Ödünç Pay Piyasası (ÖPA) açığa satış veya takas açığı için hisse ödünç alma imkanı sağlar.",
                    "Her iki piyasada da Takasbank Merkezi Karşı Taraf olarak takası garanti eder."
                ],
                "exam_traps": [
                    "⚠️ DİKKAT: TPP'de bireysel yatırımcılar doğrudan işlem yapamaz; sadece Takasbank üyesi bankalar ve aracı kurumlar işlem yapabilir."
                ],
                "tables": [
                    {
                        "headers": ["Piyasa Adı", "İşlem Amacı", "İşlem Gören Varlık", "Teminat Türleri"],
                        "rows": [
                            ["Takasbank Para Piyasası (TPP)", "Kısa vadeli nakit likidite temini", "Türk Lirası Nakit", "DİBS, BIST 30 Payları, Döviz, Eurobond"],
                            ["Ödünç Pay Piyasası (ÖPA)", "Açığa satış ve takas açığını kapatma", "BIST Pay Senetleri", "Nakit, DİBS, BIST Payları"]
                        ]
                    }
                ]
            },
            {
                "id": "sec_1012_07",
                "title": "7. MKK Elektronik Platformları (e-GKS, e-ŞİRKET, e-VEDO, e-Ürün) ve Temettü/Bedelli Hak Kullanım Süreçleri",
                "content": [
                    "Merkezi Kayıt Kuruluşu (MKK), yalnızca bir saklama kuruluşu değil; Türk sermaye piyasasının dijital omurgasını oluşturan tescilli bir Ar-Ge ve teknoloji merkezidir.",
                    "1. e-GKS (Elektronik Genel Kurul Sistemi): Anonim ortaklıkların genel kurullarına dünyanın her yerinden güvenli elektronik imza ile canlı katılma, oy kullanma, önerge verme ve toplantıyı izleme imkanı sunan dünyadaki ilk entegre sistemlerden biridir.",
                    "2. e-ŞİRKET (Şirketler Bilgi Portalı): TTK denetimine tabi sermaye şirketlerinin finansal tablolarını, denetçi raporlarını ve yasal bildirimlerini kamuya açıkladıkları merkezi kurumsal platformdur.",
                    "3. e-VEDO (Elektronik Veri Deposu): SPK düzenlemeleri uyarınca tezgahüstü (OTC) ve organize türev işlemlerin raporlandığı ulusal Veri Depolama Kuruluşu (Trade Repository) platformudur.",
                    "4. e-Ürün (Elektronik Ürün Senedi - ELÜS): Lisanslı depolara teslim edilen tarımsal ürünlerin (buğday, pamuk, mısır vb.) mülkiyetini temsil eden ürün senetlerinin MKK nezdinde kayden ihraç edildiği ve Türkiye Ürün İhtisas Borsası'nda (TÜRİB) işlem gördüğü sistemdir.",
                    "Hak Kullanım Süreçleri Operasyonları: Temettü dağıtımında T günü hak sahibi listesi MKK tarafından dondurulur, T+2 günü Takasbank üzerinden nakit para yatırımcıların hesaplarına net olarak yatırılır. Bedelli sermaye artırımında ise MKK sisteminde pay sahiplerine otomatik rüçhan kuponları tanımlanır."
                ],
                "concrete_examples": [
                    "Piyasa Örneği: Almanya'da yaşayan bir yatırımcı BIST'te pay sahibi olduğu şirketin İstanbul'daki genel kuruluna uçağa binip gelmeksizin; e-GKS sistemi üzerinden e-İmzasıyla online bağlanıp gündem maddelerine 'Ret' oyu verip toplantı tutanağına elektronik muhalefet şerhi koyabilir."
                ],
                "key_takeaways": [
                    "e-GKS elektronik genel kurula katılım ve oy kullanma platformudur.",
                    "e-VEDO türev işlemlerin raporlandığı merkezi veri deposudur.",
                    "Tarımsal ürün senetleri (ELÜS) MKK'nın e-Ürün platformunda kayden tutulur."
                ],
                "exam_traps": [
                    "⚠️ DİKKAT: e-GKS'yi Takasbank veya Borsa İstanbul değil, münhasıran 'MKK' işletmektedir."
                ],
                "tables": [
                    {
                        "headers": ["Platform Adı", "İşleten Kurum", "Temel Fonksiyonu", "Yasal Dayanak"],
                        "rows": [
                            ["e-GKS", "MKK", "Elektronik Genel Kurul ve Canlı Oy Kullanımı", "TTK m.1527"],
                            ["e-ŞİRKET", "MKK", "Şirket Finansal Tablo ve Yasal Bildirimleri", "TTK m.1524"],
                            ["e-VEDO", "MKK", "Türev İşlemler Merkezi Veri Depolama (TR)", "SPKn m.87"],
                            ["e-Ürün (ELÜS)", "MKK", "Lisanslı Depo Tarım Ürün Senetleri Kaydı", "5300 sayılı Kanun"],
                            ["e-YATIRIMCI", "MKK", "Yatırımcı Portföy Takibi ve Güvenlik Blokajı", "SPKn m.13"]
                        ]
                    }
                ]
            }
        ]
    }
}

# Write directly to topic_notes.json
with open('src/data/topic_notes.json', 'w', encoding='utf-8') as f:
    json.dump(MASTER_TOPIC_NOTES, f, ensure_ascii=False, indent=2)

print("Successfully generated master topic_notes.json with 29 comprehensive chapters, concrete examples, and tables!")
