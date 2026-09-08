# -*- coding: utf-8 -*-
"""
expand_cheatsheet.py
Expands CheatSheetPage.tsx with:
- 8 new durations (dur_17 to dur_24 -> Total 24)
- 7 new ratios (rat_16 to rat_22 -> Total 22)
- 4 new comparisons (comp_7 to comp_10 -> Total 10)
- 6 new traps (trap_10 to trap_15 -> Total 15)
- Updates banner description and badge texts.
"""

import sys

sys.stdout.reconfigure(encoding='utf-8')

NEW_DURATIONS = """  {
    id: 'dur_17',
    moduleId: '1001',
    moduleName: 'Mevzuat',
    duration: '2 - 30 İş Günü',
    title: 'Halka Arzda Talep Toplama Süresi',
    description: 'Sermaye piyasası araçlarının halka arz yoluyla satışında talep toplama süresi en az 2 iş günü, en fazla 30 iş günüdür.',
    trap: 'Sınavda alt sınır 1 gün veya üst sınır 3 ay gibi şıklar konulur; yasal sınır 2 ila 30 iş günüdür.'
  },
  {
    id: 'dur_18',
    moduleId: '1001',
    moduleName: 'Mevzuat',
    duration: 'En Az 3 Hafta Önce',
    title: 'Halka Açık Ortaklıklarda Genel Kurul Toplantı Çağrısı',
    description: 'Halka açık anonim ortaklıklarda genel kurul toplantıya çağrı ilanı, toplantı gününden en az 3 hafta önce KAP\\'ta ve şirket web sitesinde yayımlanır.',
    trap: 'TTK\\'daki kapalı şirketler için geçerli olan 2 haftalık süreyle karıştırmayın; halka açık şirketlerde en az 3 haftadır.'
  },
  {
    id: 'dur_19',
    moduleId: '1001',
    moduleName: 'Mevzuat',
    duration: '5 Yıl',
    title: 'SPK İdari Para Cezalarında Zamanaşımı',
    description: 'SPK\\'nın idari para cezası verme yetkisi, kabahate konu fiilin işlendiği tarihten itibaren 5 yıl geçmekle zamanaşımına uğrar.',
    trap: 'Süre 5 yıldır; 10 veya 20 yıllık adli zamanaşımlarıyla karıştırmayın.'
  },
  {
    id: 'dur_20',
    moduleId: '1001',
    moduleName: 'Mevzuat',
    duration: '2 Yıl / 5 Yıl',
    title: 'TSPB Disiplin Cezası Zamanaşımı Süreleri',
    description: 'Disiplin cezasını gerektiren fiilin öğrenilmesinden itibaren 2 yıl ve her halükarda fiilin işlendiği tarihten itibaren 5 yıl geçmekle ceza verme yetkisi zamanaşımına uğrar.',
    trap: 'Öğrenmeden itibaren 2 yıl, mutlak fiil süresi 5 yıldır.'
  },
  {
    id: 'dur_21',
    moduleId: '1003',
    moduleName: 'SP Araçları',
    duration: '30 Gün - 365 Gün',
    title: 'Finansman Bonoları Vade Sınırları',
    description: 'Finansman bonolarının vadesi 30 günden az, 365 günden (1 yıldan) fazla olamaz. Kural olarak iskontolu ihraç edilir.',
    trap: 'Bononun vadesi 1 yılı aşamaz; 1 yıl ve üzeri borçlanma senetleri tahvildir.'
  },
  {
    id: 'dur_22',
    moduleId: '1005',
    moduleName: 'Yatırım Kur.',
    duration: 'T+1 İş Günü',
    title: 'Kredili İşlemlerde Özkaynak Tamamlama Süresi',
    description: 'Özkaynak oranı %20 sürdürme sınırının altına düşen müşteriye derhal çağrı yapılır; müşteri en geç T+1 iş günü içinde özkaynağı %35 başlangıç seviyesine tamamlamak zorundadır.',
    trap: 'Süre 1 hafta değildir; T+1 iş günüdür. Tamamlanmazsa kurum re\\'sen satar.'
  },
  {
    id: 'dur_23',
    moduleId: '1005',
    moduleName: 'Yatırım Kur.',
    duration: 'En Az 30 Gün',
    title: 'Aracı Kurum Personelinin Hisse Senedi Elde Tutma Süresi',
    description: 'Aracı kurum çalışanları kendi kurumlarındaki hesaplarından aldıkları hisse senetlerini asgari 30 gün boyunca satamaz ve hesaplarında tutmak zorundadır.',
    trap: 'Personel için günlük al-sat (day-trading) kesinlikle yasaktır; asgari elde tutma süresi 30 gündür.'
  },
  {
    id: 'dur_24',
    moduleId: '1012',
    moduleName: 'Takas & Saklama',
    duration: 'T+1 Sabahı',
    title: 'VİOP Nakit Kâr/Zarar Uzlaşma Süresi',
    description: 'VİOP\\'ta gerçekleşen vadeli işlem ve opsiyon sözleşmelerinin günlük kâr/zarar nakit hesabı ve teminat çağrıları T+1 iş günü sabahında gerçekleştirilir.',
    trap: 'Pay Piyasası takası T+2 iken VİOP nakit uzlaşması T+1\\'dir.'
  }
];"""

NEW_RATIOS = """  {
    id: 'rat_16',
    moduleId: '1001',
    moduleName: 'Mevzuat',
    value: '%10 Yıllık Net Gelir',
    title: 'Kitle Fonlaması Bireysel Yatırım Sınırı',
    description: 'Kitle fonlamasında nitelikli yatırımcı olmayan gerçek kişiler, bir takvim yılında beyan ettikleri yıllık net gelirlerinin en fazla %10\\'u kadar yatırım yapabilirler. Nitelikli yatırımcılara ise sınır uygulanmaz.',
    trap: 'Nitelikli yatırımcılar için üst sınır yoktur; %10 sınırı genel bireysel yatırımcılar içindir.'
  },
  {
    id: 'rat_17',
    moduleId: '1001',
    moduleName: 'Mevzuat',
    value: '%5 Değerleme / %10 Genel Kurul',
    title: 'İlişkili Taraf İşlemleri Eşikleri',
    description: 'Halka açık ortaklıkların ilişkili taraflarla yapacağı varlık veya hizmet devirlerinde işlem tutarı aktif toplamı veya hasılatın %5\\'ini aşarsa değerleme raporu; %10\\'unu aşarsa genel kurul kararı zorunludur.',
    trap: '%5\\'te sadece değerleme raporu şarttır; %10\\'da ise genel kurul onayı ve bağımsız üyelerin çoğunluğu aranır.'
  },
  {
    id: 'rat_18',
    moduleId: '1001',
    moduleName: 'Mevzuat',
    value: 'Yıldız 1 Ay / Diğerleri 6 Ay',
    title: 'Ayrılma Hakkı Fiyat Belirleme Süresi',
    description: 'Önemli nitelikteki işlemlerde ayrılma hakkı kullanım fiyatı, işlemin ilk açıklandığı tarihten önceki; Yıldız Pazar\\'da son 1 aylık, diğer pazarlarda son 6 aylık borsa düzeltilmiş ağırlıklı ortalama fiyatıdır.',
    trap: 'Fiyat nominal değer veya defter değeri değil, borsada oluşan ağırlıklı ortalama fiyattır.'
  },
  {
    id: 'rat_19',
    moduleId: '1003',
    moduleName: 'SP Araçları',
    value: 'Ortalama 45 Gün / Max 184 Gün',
    title: 'Para Piyasası Fonları Portföy Kısıtlamaları',
    description: 'Para Piyasası Fonlarının günlük olarak hesaplanan ağırlıklı ortalama vadesi en fazla 45 gün olup, portföye vadesine 184 günden uzun kalan sermaye piyasası aracı dahil edilemez.',
    trap: 'Ortalama vade 90 gün değil, azami 45 gündür.'
  },
  {
    id: 'rat_20',
    moduleId: '1005',
    moduleName: 'Yatırım Kur.',
    value: 'Başlangıç %50 / Sürdürme %20',
    title: 'Açığa Satış İşlemleri Özkaynak Oranları',
    description: 'Borsa İstanbul\\'da açığa satış işlemlerinde müşterinin pozisyon açılışında bulundurması gereken başlangıç özkaynak oranı en az %50, sürdürme özkaynak oranı ise %20\\'dir.',
    trap: 'Kredili alımda başlangıç %35 iken, açığa satışta risk daha yüksek olduğu için başlangıç %50\\'dir.'
  },
  {
    id: 'rat_21',
    moduleId: '1001',
    moduleName: 'Mevzuat',
    value: 'En Az %25 Nakit & 24 Ay',
    title: 'Anonim Şirket Sermaye Taahhüdü Ödeme Kuralı',
    description: 'Anonim şirketlerin nakdi sermaye taahhüdünün en az %25\\'i tescilden önce bankada bloke edilerek ödenmeli; kalan %75\\'i ise tescili izleyen 24 ay içinde ödenmelidir.',
    trap: 'Tamamının tescilden önce ödenmesi şart değildir; en az %25\\'i yeterlidir.'
  },
  {
    id: 'rat_22',
    moduleId: '1003',
    moduleName: 'SP Araçları',
    value: 'Asli Değer = Max(0, S - K) x Çarpan',
    title: 'Alım Varantı Asli Değer (Intrinsic Value) Formülü',
    description: 'Alım varantlarında Asli Değer = (Spot Fiyat - Kullanım Fiyatı) x Çarpan formülüyle hesaplanır. Spot fiyat kullanım fiyatının altındaysa Asli Değer KESİNLİKLE SIFIRDIR; asla negatif olamaz.',
    trap: 'Varantlarda asli değer hiçbir zaman eksi çıkmaz; minimum sıfırdır.'
  }
];"""

NEW_COMPARISONS = """  {
    id: 'comp_7',
    moduleId: '1003',
    moduleName: 'SP Araçları',
    conceptA: {
      title: 'İstisna Sukuku (Eser Sözleşmesine Dayalı)',
      desc: 'VKŞ işveren, kaynak kuruluş yüklenicidir.',
      keyPoint: 'İnşaat, fabrika yapımı veya endüstriyel üretim sözleşmesine dayanır.'
    },
    conceptB: {
      title: 'Murabaha Sukuku (Alım-Satıma Dayalı)',
      desc: 'VKŞ varlığı peşin alır, vadeli olarak kâr payı ekleyerek satar.',
      keyPoint: 'Maliyet artı kâr marjıyla vadeli ticari mal satışına dayanır.'
    },
    differenceRule: 'İstisna = Eser/üretim sözleşmesi (inşaat); Murabaha = Maliyet+kâr ile vadeli alım-satımdır.'
  },
  {
    id: 'comp_8',
    moduleId: '1003',
    moduleName: 'SP Araçları',
    conceptA: {
      title: 'Varlık Teminatlı Menkul Kıymet (VTMK - Bilanço İçi)',
      desc: 'Teminat havuzu ihraççı bankanın kendi bilançosunda kalır.',
      keyPoint: 'İhraççının tüm malvarlığı sorumludur; teminat havuzu kamu koruması altındadır.'
    },
    conceptB: {
      title: 'Varlığa Dayalı Menkul Kıymet (VDMK - Bilanço Dışı)',
      desc: 'Alacaklar bilançodan tamamen çıkarılarak Fon\\'a (VFF) devredilir.',
      keyPoint: 'İhraççı iflas etse bile fon portföyü ayrı tüzel kişilik gibi korunur.'
    },
    differenceRule: 'VTMK ihraççının bilançosundadır (On-balance sheet); VDMK ise fon mülkiyetindedir (Off-balance sheet).'
  },
  {
    id: 'comp_9',
    moduleId: '1003',
    moduleName: 'SP Araçları',
    conceptA: {
      title: 'Nama Yazılı Paylar',
      desc: 'Belirli bir kişinin adına yazılı olan pay senetleridir.',
      keyPoint: 'Şirkete karşı devir pay defterine kayıtla hüküm ifade eder; halka açık paylar MKK kaydında hak sahibi adına izlenir.'
    },
    conceptB: {
      title: 'Hamiline Yazılı Paylar',
      desc: 'Senedi elinde bulunduranın hak sahibi sayıldığı pay senetleridir.',
      keyPoint: 'Bedeli tamamen ödenmedikçe hamiline pay çıkarılamaz; MKK\\'ya bildirilmeden devredilemez.'
    },
    differenceRule: 'Nama yazılı paylar bedeli ödenmeden de çıkarılabilir; hamiline paylar ise bedeli TAMAMEN ÖDENMEDİKÇE çıkarılamaz.'
  },
  {
    id: 'comp_10',
    moduleId: '1005',
    moduleName: 'Yatırım Kur.',
    conceptA: {
      title: 'Kredili Pay Alımı (Uzun / Long Pozisyon)',
      desc: 'Hisse senedinin YÜKSELECEĞİ beklentisiyle aracı kurumdan borç nakit alarak hisse almaktır.',
      keyPoint: 'Yükselişten kâr sağlar. Başlangıç özkaynağı %35\\'tir.'
    },
    conceptB: {
      title: 'Açığa Satış (Kısa / Short Pozisyon)',
      desc: 'Hisse senedinin DÜŞECEĞİ beklentisiyle sahip olunmayan hisseyi ödünç alıp satmaktır.',
      keyPoint: 'Düşüşten kâr sağlar. Başlangıç özkaynağı %50\\'dir.'
    },
    differenceRule: 'Kredili alım nakit borçlanarak yükselişe oynar (%35 özkaynak); açığa satış hisse ödünç alarak düşüşe oynar (%50 özkaynak).'
  }
];"""

NEW_TRAPS = """  {
    id: 'trap_10',
    moduleId: '1003',
    moduleName: 'SP Araçları',
    myth: 'Varantlarda dayanak hisse fiyatı kullanım fiyatının altına düşerse varantın asli değeri negatif (-5 TL gibi) olur.',
    reality: 'Varantlarda Asli Değer ASLA EKSİ (NEGATİF) OLAMAZ! Dayanak fiyat kullanım fiyatının altına düşerse asli değer SIFIR (0 TL) olur.',
    whyImportant: 'Sınav hesaplama sorularında formül Max(0, S-K) şeklindedir; eksi sonuç çıkarsa sıfır alınır.'
  },
  {
    id: 'trap_11',
    moduleId: '1003',
    moduleName: 'SP Araçları',
    myth: 'Kira sertifikalarını (Sukuk) yalnızca katılım bankaları ihraç edebilir.',
    reality: 'Kira sertifikalarını Hazine ve SPK onaylı tüm anonim ortaklıklar bünyesinde kurulan Varlık Kiralama Şirketleri (VKŞ) ihraç edebilir.',
    whyImportant: 'İhraççı sadece faizsiz finans kuruluşları değildir; her türlü büyük sanayi şirketi ve Hazine VKŞ kurabilir.'
  },
  {
    id: 'trap_12',
    moduleId: '1001',
    moduleName: 'Mevzuat',
    myth: 'Halka açık anonim ortaklıklarda imtiyazlı pay sahipleri genel kurulun tüm kararlarında imtiyazlı oy (örneğin 15 oy) kullanabilir.',
    reality: 'Esas sözleşme değişikliklerinde ve yönetim kurulunun ibrası oylamalarında OYDA İMTİYAZ KESİNLİKLE KULLANILAMAZ; her pay 1 oy sayılır.',
    whyImportant: 'Sınavda \\'Hâkim ortak imtiyazlı oyuyla şirketin faaliyet konusunu değiştirdi\\' seçeneği YANLIŞTIR.'
  },
  {
    id: 'trap_13',
    moduleId: '1001',
    moduleName: 'Mevzuat',
    myth: 'Bedelsiz sermaye artırımı şirketin kasasına nakit sokar ve şirketin toplam piyasa değerini doğrudan artırır.',
    reality: 'Bedelsiz artırımda şirketin kasasına 1 KURUŞ BİLE GİRMEZ; sadece iç kaynaklar sermayeye eklenir, hisse fiyatı oransal düşer ve piyasa değeri değişmez.',
    whyImportant: 'Sınavda \\'Bedelsiz sermaye artırımı şirketin likiditesini güçlendirir\\' ifadesi YANLIŞTIR.'
  },
  {
    id: 'trap_14',
    moduleId: '1001',
    moduleName: 'Mevzuat',
    myth: 'İçsel bilgiye dayalı ticaret (insider trading) yapan bir kişi sonradan pişman olup elde ettiği kazancı Hazineye öderse ceza almaz.',
    reality: 'Bilgi suistimali suçunda (SPKn m.106) ETKİN PİŞMANLIK HÜKMÜ KESİNLİKLE YOKTUR. Etkin pişmanlık sadece işlem bazlı manipülasyonda (m.107) geçerlidir.',
    whyImportant: 'Sınavda içeriden öğrenen için \\'Hazineye 2 katını öderse ceza almaz\\' çeldiricisi konur; YANLIŞTIR, sadece manipülasyonda geçerlidir.'
  },
  {
    id: 'trap_15',
    moduleId: '1012',
    moduleName: 'Takas & Saklama',
    myth: 'Aracı kurumdaki hesabında 10 yıl boyunca işlem görmeyen hisse senetleri aracı kuruma kâr olarak kalır veya Hazineye gider.',
    reality: '10 yıl boyunca işlem görmeyen ve talep edilmeyen tüm nakit ve sermaye piyasası araçları doğrudan YATIRIMCI TAZMİN MERKEZİ\\'NE (YTM) devredilir.',
    whyImportant: 'Devir kurumu Maliye/Hazine değil, kanunen YTM\\'dir.'
  }
];"""

with open('src/pages/CheatSheetPage.tsx', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Replace DURATIONS ending
dur_target = """    trap: 'Zamanaşımı süresi 5 yıl veya 20 yıl değil, kesin olarak 10 yıldır.'
  }
];"""

dur_replacement = """    trap: 'Zamanaşımı süresi 5 yıl veya 20 yıl değil, kesin olarak 10 yıldır.'
  },\n""" + NEW_DURATIONS

if dur_target in content:
    content = content.replace(dur_target, dur_replacement, 1)
    print("DURATIONS başarıyla genişletildi (24 madde).")
else:
    print("HATA: dur_target bulunamadı!")

# 2. Replace RATIOS ending
rat_target = """    trap: 'Eski 1 Milyon TL kuralı kaldırılmıştır! Güncel eşik kesinlikle 10 MİLYON TL\\'dir.'
  }
];"""

rat_replacement = """    trap: 'Eski 1 Milyon TL kuralı kaldırılmıştır! Güncel eşik kesinlikle 10 MİLYON TL\\'dir.'
  },\n""" + NEW_RATIOS

if rat_target in content:
    content = content.replace(rat_target, rat_replacement, 1)
    print("RATIOS başarıyla genişletildi (22 madde).")
else:
    print("HATA: rat_target bulunamadı!")

# 3. Replace COMPARISONS ending
comp_target = """    differenceRule: 'Borsa ekranında işlem gören ve kote edilen fiyat TEMİZ FİYAT\\'tır; ancak alıcının satıcıya takas gününde fiilen ödediği para KİRLİ FİYAT\\'tır. Kupon ödemesinin yapıldığı gün işlemiş faiz sıfırlandığı için Temiz Fiyat = Kirli Fiyat olur; kupon gününe yaklaştıkça Kirli Fiyat yükselir.'
  }
];"""

comp_replacement = """    differenceRule: 'Borsa ekranında işlem gören ve kote edilen fiyat TEMİZ FİYAT\\'tır; ancak alıcının satıcıya takas gününde fiilen ödediği para KİRLİ FİYAT\\'tır. Kupon ödemesinin yapıldığı gün işlemiş faiz sıfırlandığı için Temiz Fiyat = Kirli Fiyat olur; kupon gününe yaklaştıkça Kirli Fiyat yükselir.'
  },\n""" + NEW_COMPARISONS

if comp_target in content:
    content = content.replace(comp_target, comp_replacement, 1)
    print("COMPARISONS başarıyla genişletildi (10 madde).")
else:
    print("HATA: comp_target bulunamadı!")

# 4. Replace TRAPS ending
trap_target = """    whyImportant: 'Sınavda 1.000.000 TL çeldirici olarak verilir; doğru güncel cevap 10.000.000 TL\\'dir.'
  }
];"""

trap_replacement = """    whyImportant: 'Sınavda 1.000.000 TL çeldirici olarak verilir; doğru güncel cevap 10.000.000 TL\\'dir.'
  },\n""" + NEW_TRAPS

if trap_target in content:
    content = content.replace(trap_target, trap_replacement, 1)
    print("TRAPS başarıyla genişletildi (15 madde).")
else:
    print("HATA: trap_target bulunamadı!")

# 5. Replace header text
header_old = "Sınav salonuna girmeden önce göz gezdirerek hata yapma ihtimalini ortadan kaldıran 16 kanuni süre, 13 kritik oran, 5 ikili kavram ayrımı ve 7 ölümcül sınav tuzağı."
header_new = "Sınav salonuna girmeden önce 10 dakikada göz gezdirerek hata yapma ihtimalini ortadan kaldıran 24 kanuni süre, 22 kritik oran/sayı, 10 ikili kavram ayrımı ve 15 ölümcül sınav tuzağı (11 Eylül 2026 SPL Düzey 1 Sınavına %100 Uyumlu)."

if header_old in content:
    content = content.replace(header_old, header_new, 1)
    print("Header metni güncellendi.")
else:
    print("HATA: header_old bulunamadı!")

with open('src/pages/CheatSheetPage.tsx', 'w', encoding='utf-8') as f:
    f.write(content)

print("\n--- CheatSheetPage.tsx Başarıyla Güncellendi ---")
