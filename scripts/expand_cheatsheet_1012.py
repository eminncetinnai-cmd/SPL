# -*- coding: utf-8 -*-
import re

with open("src/pages/CheatSheetPage.tsx", "r", encoding="utf-8") as f:
    content = f.read()

# 1. Update dur_13
dur_13_old = """  {
    id: 'dur_13',
    moduleId: '1012',
    moduleName: 'Takas & Saklama',
    duration: 'T+2 (15:00)',
    title: 'BIST Pay Piyasası Takas Valörü ve Son Temerrüt Saati',
    description: 'Pay Piyasası hisse işlemlerinin standart takası T+2 günüdür. Takas borçlarının tamamlanması gereken yasal son saat 15:00\'tir.',
    trap: 'Cuma yapılan işlemin takası Salı günüdür (hafta sonu iş günü sayılmaz).'
  },"""

dur_13_new = """  {
    id: 'dur_13',
    moduleId: '1012',
    moduleName: 'Takas & Saklama',
    duration: 'T+2 (16:45)',
    title: 'BIST Pay Piyasası Takas Valörü ve Borç Kapama Son Saati',
    description: 'Pay Piyasası hisse işlemlerinin standart takas valörü T+2 günüdür. Takas borçlarının kapatılması gereken yasal son saat 16:45\'tir; bu saatten sonra üye ihbarsız temerrüde düşer.',
    trap: 'Takas borç kapama son saati 15:00 değil, 16:45\'tir (15:00 teminat tamamlama son saatidir).'
  },"""

if dur_13_old in content:
    content = content.replace(dur_13_old, dur_13_new)
    print("dur_13 updated successfully.")
else:
    print("Warning: dur_13_old not matched exactly, checking regex...")
    content = re.sub(
        r"id:\s*'dur_13',[\s\S]*?trap:\s*'[^']*'",
        """id: 'dur_13',
    moduleId: '1012',
    moduleName: 'Takas & Saklama',
    duration: 'T+2 (16:45)',
    title: 'BIST Pay Piyasası Takas Valörü ve Borç Kapama Son Saati',
    description: 'Pay Piyasası hisse işlemlerinin standart takas valörü T+2 günüdür. Takas borçlarının kapatılması gereken yasal son saat 16:45\\'tir; bu saatten sonra üye ihbarsız temerrüde düşer.',
    trap: 'Takas borç kapama son saati 15:00 değil, 16:45\\'tir (15:00 teminat tamamlama son saatidir).'""",
        content
    )
    print("dur_13 regex replaced.")

# 2. Update trap_7 to have exact 7-tier hierarchy of Madde 36
trap_7_old = """  {
    id: 'trap_7',
    moduleId: '1012',
    moduleName: 'Takas & Saklama',
    myth: 'Bir aracı kurum temerrüde düştüğünde Takasbank doğrudan diğer masum aracı kurumların Garanti Fonu paralarını kullanır.',
    reality: 'Temerrüt şelalesinde diğer masum üyelerin fonları EN SON ÇARE olarak kullanılır. Sıra: 1. Borçlu üyenin teminatı -> 2. Borçlu üyenin Garanti Fonu payı -> 3. Takasbank SITG özkaynağı -> 4. Diğer üyelerin Garanti Fonu payları.',
    whyImportant: 'Temerrüt şelalesi öncelik sırası sınavda her dönem garanti sorudur.'
  },"""

trap_7_new = """  {
    id: 'trap_7',
    moduleId: '1012',
    moduleName: 'Takas & Saklama',
    myth: 'Bir aracı kurum temerrüde düştüğünde Takasbank doğrudan diğer masum aracı kurumların Garanti Fonu paralarını kullanır.',
    reality: 'Temerrüt şelalesinde (MKT Yönetmeliği m.36) 7 aşamalı kesin öncelik sırası uygulanır: 1. Temerrüt eden üyenin teminatları -> 2. Temerrüt eden üyenin yatırılmış garanti fonu katkısı -> 3. Varsa sigorta tazminleri -> 4. Takasbank tahsisli sermayesi -> 5. Diğer MKT üyelerinin yatırılmış garanti fonu katkıları -> 6. Üyelerden talep edilecek ilave garanti fonu katkıları -> 7. Takasbank taahhütlü sermayesi.',
    whyImportant: 'MKT Madde 36 kaynak kullanım sırası SPL 1012 sınavının en banko ve ayırt edici sorusudur.'
  },"""

if trap_7_old in content:
    content = content.replace(trap_7_old, trap_7_new)
    print("trap_7 updated.")
else:
    print("Warning: trap_7_old not matched exactly, replacing with regex...")
    content = re.sub(
        r"id:\s*'trap_7',[\s\S]*?whyImportant:\s*'[^']*'",
        """id: 'trap_7',
    moduleId: '1012',
    moduleName: 'Takas & Saklama',
    myth: 'Bir aracı kurum temerrüde düştüğünde Takasbank doğrudan diğer masum aracı kurumların Garanti Fonu paralarını kullanır.',
    reality: 'Temerrüt şelalesinde (MKT Yönetmeliği m.36) 7 aşamalı kesin öncelik sırası uygulanır: 1. Temerrüt eden üyenin teminatları -> 2. Temerrüt eden üyenin yatırılmış garanti fonu katkısı -> 3. Varsa sigorta tazminleri -> 4. Takasbank tahsisli sermayesi -> 5. Diğer MKT üyelerinin yatırılmış garanti fonu katkıları -> 6. Üyelerden talep edilecek ilave garanti fonu katkıları -> 7. Takasbank taahhütlü sermayesi.',
    whyImportant: 'MKT Madde 36 kaynak kullanım sırası SPL 1012 sınavının en banko ve ayırt edici sorusudur.'""",
        content
    )

# 3. Add new Durations: dur_43 to dur_50 before the closing bracket of DURATIONS
new_durations = """  {
    id: 'dur_43',
    moduleId: '1012',
    moduleName: 'Takas & Saklama',
    duration: '16:45',
    title: 'Pay ve Borçlanma Araçları Takas Borç Kapama Son Saati',
    description: 'Borsa İstanbul Pay Piyasası ve Borçlanma Araçları Piyasası\\'nda takas günü nakit ve menkul kıymet borçlarının temerrütsüz son kapatılma saati 16:45\\'tir.',
    trap: '16:45\\'ten sonra borcunu kapatmayan üye herhangi bir ihtara gerek kalmaksızın kendiliğinden temerrüde düşer.'
  },
  {
    id: 'dur_44',
    moduleId: '1012',
    moduleName: 'Takas & Saklama',
    duration: '15:00 (Ertesi Gün)',
    title: 'Pay Piyasası ve BAP Gün Sonu Teminat Tamamlama Son Saati',
    description: 'İşlem günü sonunda teminat açığı oluşan üyeler teminat tamamlama yükümlülüklerini bir sonraki iş günü en geç saat 15:00\\'e kadar yerine getirmek zorundadır (Yarım günlerde Pay 11:00, BAP 10:00).',
    trap: 'Gün sonu çağrısı aynı gün değil, ertesi iş günü saat 15:00\\'e kadar tamamlanır.'
  },
  {
    id: 'dur_45',
    moduleId: '1012',
    moduleName: 'Takas & Saklama',
    duration: '16:46 – 17:00',
    title: 'BAP Ön Temerrüt Süresi ve İndirimli Katsayı (0.25)',
    description: 'Borçlanma Araçları Piyasası\\'nda 16:46-17:00 arası kapatılan borçlar ön temerrüt sayılır ve katsayı sadece 0.25 olarak uygulanır (17:01-18:45 arası 0.50, 18:46 sonrası ve ertesi günler katsayı 3).',
    trap: 'Pay Piyasası\\'nda ön temerrüt yoktur (16:46-17:30 arası katsayı 1\\'dir); ön temerrüt (0.25) sadece Borçlanma Araçları Piyasası\\'nda vardır.'
  },
  {
    id: 'dur_46',
    moduleId: '1012',
    moduleName: 'Takas & Saklama',
    duration: '2 Saat',
    title: 'Gün İçi Teminat Tamamlama Çağrısı Yatırma Süresi',
    description: 'Seans içinde teminat açığı oluşması halinde Takasbank tarafından yapılan gün içi teminat tamamlama çağrısına konu tutarlar en geç 2 saat içinde yatırılmak zorundadır.',
    trap: 'Gün içi teminat çağrısı gün sonuna kadar beklenemez; 2 saat içinde yatırılmazsa derhal temerrüt hükümleri işletilir.'
  },
  {
    id: 'dur_47',
    moduleId: '1012',
    moduleName: 'Takas & Saklama',
    duration: '3 İş Günü',
    title: 'Tahakkuk Eden Temerrüt Cezası ve Garanti Fonu İkame Süresi',
    description: 'Temerrüt faizi ve cezası tahakkuk tarihinden itibaren 3 iş günü içinde ödenir. Benzer şekilde temerrüt nedeniyle kullanılan yatırılmış Garanti Fonu katkı payları da 3 iş günü içinde tamamlanmalıdır.',
    trap: 'Süre 3 takvim günü değil, 3 İŞ GÜNÜDÜR; süresinde ödenmezse Takasbank serbest hesaptan re\\'sen tahsil eder.'
  },
  {
    id: 'dur_48',
    moduleId: '1012',
    moduleName: 'Takas & Saklama',
    duration: 'T+3 (11:00)',
    title: 'Pay Piyasası Re\\'sen Borç Kapama ve Temerrüt Sırası',
    description: 'Pay Piyasası\\'nda T+3 günü saat 11:00\\'e kadar menkul kıymet veya nakit borcunu kapatamayan aracı kurumlar adına Borsa İstanbul\\'da Temerrüt Sırası (Buy-in) açılarak aynı gün valörle re\\'sen alım/satım yapılır.',
    trap: 'Borsa temerrüt sırası takas günü değil, takası izleyen iş günü (T+3) saat 11:00\\'de devreye girer.'
  },
  {
    id: 'dur_49',
    moduleId: '1012',
    moduleName: 'Takas & Saklama',
    duration: '90 Gün',
    title: 'Portföy Saklama Sözleşmesi Fesih İhbar Süresi',
    description: 'Portföy yönetim şirketi (PYŞ) veya yatırım ortaklığı, sözleşmeli portföy saklayıcısını değiştirmek veya saklayıcı sözleşmeyi sona erdirmek isterse, bu durumu en az 90 gün önceden karşı tarafa ve SPK\\'ya gerekçeleriyle bildirmek zorundadır.',
    trap: 'İhbar süresi 30 gün veya 60 gün değil, tam 90 gündür; yeni saklayıcı göreve başlayana kadar eski saklayıcının yasal sorumluluğu devam eder.'
  },
  {
    id: 'dur_50',
    moduleId: '1012',
    moduleName: 'Takas & Saklama',
    duration: '1 Ay / 4. Ayın İlk İş Günü',
    title: 'Takasbank MKT Tahsis ve Taahhüt Sermaye Takvimi',
    description: 'Takasbank MKT karşılanmış riskler tahsis ve taahhüt sermayesini yılda bir kez en geç 4. ayın (Nisan) ilk iş günü günceller ve ilan eder. Temerrütte kullanılan tahsisli sermaye ise 1 ay içinde tamamlanır.',
    trap: 'Yıllık güncelleme yılbaşı değil Nisan başıdır; eksilen sermayenin ikame süresi 1 aydır.'
  }
];"""

# 4. Add new Ratios: rat_45 to rat_54 before closing bracket of RATIOS
new_ratios = """  {
    id: 'rat_45',
    moduleId: '1012',
    moduleName: 'Takas & Saklama',
    value: '%64.9 / %30.1 / %5.0',
    title: 'Merkezi Kayıt Kuruluşu (MKK) Güncel Ortaklık Yapısı',
    description: 'MKK sermayesi 100 Milyon TL olup fiili ortaklık payları: İstanbul Takas ve Saklama Bankası A.Ş. %64.9, Borsa İstanbul A.Ş. %30.1 ve Türkiye Sermaye Piyasaları Birliği (TSPB) %5.0\\'dir.',
    trap: 'MKK\\'da çoğunluk hisse Borsa İstanbul\\'un değil, %64.9 ile Takasbank\\'ındır.'
  },
  {
    id: 'rat_46',
    moduleId: '1012',
    moduleName: 'Takas & Saklama',
    value: '%75 / %50 / %10 / %5',
    title: 'MKK Esas Sözleşmesi Azami Pay Sahipliği Tavanları',
    description: 'MKK esas sözleşmesine göre; Takasbank payı %75\\'i, Borsa İstanbul payı %50\\'yi, TSPB payı %10\\'u ve diğer ortakların her birinin payı %5\\'i geçemez.',
    trap: 'Fiili oranlar (%64.9 / %30.1 / %5) ile esas sözleşme tavanları (%75 / %50 / %10 / %5) sınavda birbirinin çeldiricisidir.'
  },
  {
    id: 'rat_47',
    moduleId: '1012',
    moduleName: 'Takas & Saklama',
    value: '2/3 (%66.7)',
    title: 'Temerrüt Mağduriyet Ödemesi Oranı',
    description: 'Temerrüt nedeniyle nakit veya menkul kıymet alacağını valör gününde alamayan hak sahibi üyeye, temerrüt eden üyeden tahsil edilen temerrüt faiz ve cezasının 2/3\\'ü mağduriyet ödemesi olarak aktarılır.',
    trap: 'Tahsil edilen cezanın tamamı Takasbank\\'a kalmaz; 2/3\\'ü alacaklı mağdur üyeye ödenir, 1/3\\'ü Takasbank\\'ta kalır.'
  },
  {
    id: 'rat_48',
    moduleId: '1012',
    moduleName: 'Takas & Saklama',
    value: '%10 / %50 / %30',
    title: 'Asgari Nakit Türk Lirası Teminat Kompozisyon Oranları',
    description: 'Pay Piyasası işlem teminatında en az %10 Nakit TL; VİOP işlem teminatında en az %50 Nakit TL; VİOP Garanti Fonu katkı payında en az %30 Nakit TL zorunludur. BAP ve BİAŞ Para Piyasası\\'nda asgari TL şartı yoktur.',
    trap: 'Tüm piyasalarda nakit TL şartı aynı değildir; VİOP işlem teminatında %50 iken Pay Piyasası\\'nda %10\\'dur; BAP\\'ta ise minimum TL şartı aranmaz.'
  },
  {
    id: 'rat_49',
    moduleId: '1012',
    moduleName: 'Takas & Saklama',
    value: '200K / 700K / 3.575M / 2.875M TL',
    title: 'MKT Piyasalarında Sabit Garanti Fonu Katkı Payları',
    description: 'MKT üyelerinin yatırması gereken maktu asgari Garanti Fonu katkı payları: Pay Piyasası: 200.000 TL, Borçlanma Araçları Piyasası (BAP): 700.000 TL, VİOP: 3.575.000 TL, SWAP Piyasası: 2.875.000 TL, OTC Türev: 500.000 TL, BİAŞ Para Piyasası: 50.000 TL.',
    trap: 'En yüksek sabit katkı payı 3.575.000 TL ile VİOP\\'tadır.'
  },
  {
    id: 'rat_50',
    moduleId: '1012',
    moduleName: 'Takas & Saklama',
    value: '%25',
    title: 'Tek Bir İhraççı/Banka Teminat Konsantrasyon Limiti',
    description: 'Tek bir ihraççı veya banka ya da aynı gruba ait kurumların ihraç ettiği menkul kıymetler/garantiler toplamı (Hazine ve kamu bankaları hariç), ilgili piyasada kabul edilen toplam teminatların %25\\'ini geçemez.',
    trap: 'Hazine ihraçları ve kamu bankası menkul kıymetleri %25 konsantrasyon sınırından muaftır.'
  },
  {
    id: 'rat_51',
    moduleId: '1012',
    moduleName: 'Takas & Saklama',
    value: '%3 / %25 / %100',
    title: 'VİOP Pozisyon Limitleri Eşikleri',
    description: 'Pay vadeli ve opsiyon sözleşmelerinde: Sicil bazında fiili dolaşımın azami %3\\'ü; Piyasa bazında fiili dolaşımın azami %25\\'i (vade sonlarında %35\\'e çıkarılabilir); ELÜS sözleşmelerinde lisanslı depo kapasitesinin %100\\'ü.',
    trap: 'Sicil limiti %3, piyasa limiti %25\\'tir; birbirine karıştırmayın.'
  },
  {
    id: 'rat_52',
    moduleId: '1012',
    moduleName: 'Takas & Saklama',
    value: '%200',
    title: 'BISTECH Risk/Limit Aşımında Emir İptal Eşiği',
    description: 'Üyenin toplam teminat gereksiniminin risk limitine oranı %200\\'ü aşarsa, teminat bakiyesine bakılmaksızın üyenin yeni emir iletimi derhal durdurulur ve BISTECH\\'teki tüm pasif emirleri otomatik olarak iptal edilir.',
    trap: 'Emir iptal eşiği %100 veya %150 değil, tam %200\\'dür.'
  },
  {
    id: 'rat_53',
    moduleId: '1012',
    moduleName: 'Takas & Saklama',
    value: '%80',
    title: 'VİOP Gün İçi Sürdürme Seviyesi Oranı',
    description: 'VİOP\\'ta gün sonlarında sürdürme teminatı uygulanmaz; ancak seans içinde gün içi sürdürme seviyesi oranı %80 olarak uygulanır. Hesabın teminatı %80 altına inerse pasif emirleri iptal edilir.',
    trap: 'VİOP\\'ta gün sonunda sürdürme teminatı yoktur (gün sonu daima %100 başlangıç teminatına tamamlanır); %80 seviyesi sadece seans içi gün içi kontroller içindir.'
  },
  {
    id: 'rat_54',
    moduleId: '1012',
    moduleName: 'Takas & Saklama',
    value: '5.000 TL',
    title: 'Takasbank Nezdinde Nemalandırma Alt Sınırı',
    description: 'Takasbank nezdinde saat 15:40 itibarıyla işlem ve garanti fonu nakit TL bakiyeleri nemalandırılır. Bakiyesi 5.000 TL\\'nin altında kalan hesaplara nema ödenmez.',
    trap: '15:40\\'tan sonra yatırılan nakitler o gün için nemalanmaz; ayrıca 5.000 TL altı bakiyeler nema kapsamı dışındadır.'
  }
];"""

# 5. Add new Comparisons: comp_25 to comp_32
new_comparisons = """  {
    id: 'comp_25',
    moduleId: '1012',
    moduleName: 'Takas & Saklama',
    conceptA: {
      title: 'Açık Teklif Yöntemi (Open Offer)',
      desc: 'İşlemin eşleştiği anda Takasbank\\'ın otomatik olarak tarafların arasına girmesidir.',
      keyPoint: 'Taraflar arasında sözleşme doğmadan, eşleşme anında alıcıya karşı satıcı, satıcıya karşı alıcı konumuna geçer.'
    },
    conceptB: {
      title: 'Sözleşme Yenileme Yöntemi (Novation)',
      desc: 'Taraflar arasında kurulan orijinal sözleşmenin iptal edilerek Takasbank ile ayrı sözleşmeler yapılmasıdır.',
      keyPoint: 'Orijinal sözleşme fesholur; Takasbank alıcı ve satıcı ile ayrı ayrı iki yeni sözleşme akdeder.'
    },
    differenceRule: 'Açık teklifte orijinal sözleşme hiç doğmaz, eşleşme anında MKT araya girer; Sözleşme yenilemede ise önce taraflar arası sözleşme kurulur, ardından iptal edilip yenilenir.'
  },
  {
    id: 'comp_26',
    moduleId: '1012',
    moduleName: 'Takas & Saklama',
    conceptA: {
      title: 'Doğrudan Takas Üyesi (Direct Clearing Member)',
      desc: 'Yalnızca kendi portföyü ve/veya müşterilerinin takas işlemlerini yürütmeye yetkili üyedir.',
      keyPoint: 'Başka piyasa üyelerinin veya işlemci kuruluşların takasını gerçekleştiremez.'
    },
    conceptB: {
      title: 'Genel Takas Üyesi (General Clearing Member)',
      desc: 'Kendisi ve müşterilerinin yanı sıra diğer işlemci kuruluşların da takasını üstlenen üyedir.',
      keyPoint: 'İşlemci kuruluşla birlikte Takasbank\\'a karşı müşterek borçlu ve müteselsil kefil sorumluluğu taşır.'
    },
    differenceRule: 'Doğrudan üye sadece kendi ve müşteri işlemlerini takas eder; Genel üye üçüncü taraf işlemci kuruluşların da takasını yapar ve müteselsilen kefildir.'
  },
  {
    id: 'comp_27',
    moduleId: '1012',
    moduleName: 'Takas & Saklama',
    conceptA: {
      title: 'Çok Taraflı Netleştirme (Multilateral Netting)',
      desc: 'Aynı valörlü işlemlerde alış ve satışların mahsup edilerek tek bir net nakit ve kıymet borcu/alacağı çıkarılmasıdır.',
      keyPoint: 'Likidite ihtiyacını ve takas riskini dramatik ölçüde düşürür.'
    },
    conceptB: {
      title: 'Brüt Takas (Gross Settlement)',
      desc: 'Her işlemin alım ve satımının birbirine mahsup edilmeksizin ayrı ayrı ve tam tutarları üzerinden takas edilmesidir.',
      keyPoint: 'Netleştirme yapılmaz; üye toplam satış kadar menkul kıymet borçlu, toplam nakit kadar borçludur.'
    },
    differenceRule: 'Netleştirmede sadece net bakiye el değiştirirken, brüt takasta işlem tutarlarının tamamı mahsup edilmeden birebir takasa tabi tutulur.'
  },
  {
    id: 'comp_28',
    moduleId: '1012',
    moduleName: 'Takas & Saklama',
    conceptA: {
      title: 'Başlangıç Teminatı (Initial Margin)',
      desc: 'Pozisyon ilk açıldığında gelecekteki temerrüt riskine karşı alınan teminattır.',
      keyPoint: 'Portföyün olası fiyat dalgalanmalarına karşı güvencedir (VİOP güven düzeyi %99-%99.75, BAP %99.50).'
    },
    conceptB: {
      title: 'Değişim Teminatı (Variation Margin)',
      desc: 'Mevcut açık pozisyonların cari piyasa fiyatları ile değerlenmesi sonucu doğan kar/zarar farkıdır.',
      keyPoint: 'Gün içi ve gün sonu fiyat hareketlerine göre hesaplanır, zarar edenden tahsil edilir, kar edene aktarılır.'
    },
    differenceRule: 'Başlangıç teminatı gelecekteki potansiyel riski karşılar; Değişim teminatı ise gerçekleşen güncel piyasa fiyat farkını (kar/zarar) yansıtır.'
  },
  {
    id: 'comp_29',
    moduleId: '1012',
    moduleName: 'Takas & Saklama',
    conceptA: {
      title: 'BISTECH Marjin Yöntemi',
      desc: 'Pay Piyasası ve VİOP\\'ta kullanılan portföy bazlı parametrik risk yönetimi algoritmasıdır.',
      keyPoint: '5 adımlı analiz: Ürün grubu riski, gruplar arası risk, marjin risk değeri, başlangıç teminatı, bulunması gereken teminat.'
    },
    conceptB: {
      title: 'Nakit Akım Teminatlandırma (NAT) Yöntemi',
      desc: 'Borçlanma Araçları Piyasası (BAP) ve OTC Türevler için verim eğrilerine şok uygulayan modeldir.',
      keyPoint: 'Temel 3 bileşen şoku kullanır: Paralel kayma, Eğim değişmesi, Eğrilik (curvature) değişmesi.'
    },
    differenceRule: 'BISTECH Marjin hisse ve türev sözleşmelerini ürün gruplarına ayırır; NAT ise tahvil ve swapları nakit akımlarına ve verim eğrilerine göre şoklar.'
  },
  {
    id: 'comp_30',
    moduleId: '1012',
    moduleName: 'Takas & Saklama',
    conceptA: {
      title: 'Serbest Virman',
      desc: 'Bir hesaptaki menkul kıymetin herhangi bir nakit veya karşı edim şartı aranmaksızın başka bir hesaba aktarılmasıdır.',
      keyPoint: 'Tek taraflı transferdir; karşı taraftan nakit beklenmez.'
    },
    conceptB: {
      title: 'Şartlı Virman (DvP - Teslim Karşılığı Ödeme)',
      desc: 'Menkul kıymet transferinin ancak karşı taraftan belirlenen nakdin eşanlı olarak hesaba geçmesi şartıyla yapılmasıdır.',
      keyPoint: 'Eşanlı transfer mekanizmasıdır; nakit gelmezse kıymet transferi gerçekleşmez.'
    },
    differenceRule: 'Serbest virman şartsız kıymet aktarımıdır; Şartlı virman anapara riskini sıfırlayan Teslim Karşılığı Ödeme (DvP) güvencesidir.'
  },
  {
    id: 'comp_31',
    moduleId: '1012',
    moduleName: 'Takas & Saklama',
    conceptA: {
      title: 'MKK Doğrudan Hak Sahipliği (Direct Holding)',
      desc: 'Türkiye\\'deki yerli yatırımcıların hisse senetlerinin doğrudan kendi ad ve TC/Vergi kimlik numaralarıyla açılan hesaplarda izlenmesidir.',
      keyPoint: 'Aracı kurum iflas etse dahi mülkiyet MKK sicilinde doğrudan yatırımcıya aittir.'
    },
    conceptB: {
      title: 'YMSK Global Saklama (Omnibus Holding)',
      desc: 'Yurt dışı merkezi saklama kuruluşları nezdinde yabancı yatırımcıların toplu havuz hesaplarda izlenmesidir.',
      keyPoint: 'MKK nezdinde hak sahibi adına tekil açılmaz; atanan sicil doğrudan hak sahipliğini ispatlamaz.'
    },
    differenceRule: 'Doğrudan saklamada MKK mülkiyet sicilidir; YMSK global hesapta ise alt hak sahiplerinin detay kayıtları yurt dışı saklayıcı nezdinde tutulur.'
  },
  {
    id: 'comp_32',
    moduleId: '1012',
    moduleName: 'Takas & Saklama',
    conceptA: {
      title: 'Genel Saklama Hizmeti (Tebliğ III-37.1)',
      desc: 'Yatırım kuruluşlarının müşterilerine ait sermaye piyasası araçlarını kayden izleme ve saklama faaliyetidir.',
      keyPoint: 'Bireysel ve kurumsal yatırımcıların standart hisse/tahvil saklama hesabıdır.'
    },
    conceptB: {
      title: 'Portföy Saklama Hizmeti (Tebliğ III-56.1)',
      desc: 'Kolektif yatırım kuruluşlarının (Yatırım Fonları ve Yatırım Ortaklıkları) portföylerinin saklanması ve gözetimidir.',
      keyPoint: 'Fon malvarlığını PYŞ\\'den korur; harcamaların, birim pay değerinin ve kaldıraç limitlerinin gözetimini yapar.'
    },
    differenceRule: 'Genel saklama müşteri varlığını korur; Portföy saklama ise kolektif fon malvarlığını PYŞ\\'nin usulsüz işlemlerine karşı gözetler ve denetler.'
  }
];"""

# 6. Add new Traps: trap_32 to trap_38
new_traps = """  {
    id: 'trap_32',
    moduleId: '1012',
    moduleName: 'Takas & Saklama',
    myth: 'Merkezi Karşı Taraf (MKT) rolünü üstlenen Takasbank, temerrüt halinde doğrudan aracı kurumun müşterisiyle muhatap olur ve müşteriye dava açar.',
    reality: 'MKT uygulamasında Takasbank\\'ın yasal muhatabı KESİNLİKLE VE SADECE ÜYEDİR (Aracı Kurum/Banka). Takasbank müşterilere karşı sorumlu olmadığı gibi, müşterilerle de doğrudan muhatap olmaz.',
    whyImportant: 'Sınavda \'Takasbank temerrüt eden müşteriye doğrudan ihbarname gönderir\' çeldiricisi konur; KESİNLİKLE YANLIŞTIR.'
  },
  {
    id: 'trap_33',
    moduleId: '1012',
    moduleName: 'Takas & Saklama',
    myth: 'Tüm yatırım ortaklıkları ve tüm fonlar Portföy Saklama Tebliği (III-56.1) kapsamında saklayıcı tutmak zorundadır.',
    reality: 'GYO, Altyapı GYO, GSYO ve Emeklilik Yatırım Fonları Tebliğ hükümleri çerçevesinde portföy saklama zorunluluğunda DEĞİLDİR! Ancak Gayrimenkul Yatırım Fonları (GYF) ve Girişim Sermayesi Yatırım Fonları (GSYF) TEBLİĞ KAPSAMINDADIR.',
    whyImportant: 'Sınavda \'Emeklilik fonları ve GYO\\'lar saklayıcı tutmak zorundadır\' ifadesi YANLIŞTIR; GYF ve GSYF ise ZORUNLUDUR.'
  },
  {
    id: 'trap_34',
    moduleId: '1012',
    moduleName: 'Takas & Saklama',
    myth: 'Takasbank\\'ın MKT olduğu tüm piyasalarda üyelerden maktu üyelik teminatı alınır.',
    reality: 'Ödünç Pay Piyasası\\'nda (ÖPP) ÜYELİK TEMİNATI UYGULAMASI BULUNMAMAKTADIR! Üyelik teminatı Pay, BAP ve VİOP\\'ta nakit TL olarak alınır.',
    whyImportant: 'Sınavda \'Ödünç Pay Piyasasında üyelik teminatı zorunludur\' seçeneği YANLIŞTIR.'
  },
  {
    id: 'trap_35',
    moduleId: '1012',
    moduleName: 'Takas & Saklama',
    myth: 'SPK tarafından kaydileştirilmesine karar verilip süresinde teslim edilmeyen hisse senetleri tamamen imha edilir ve mülkiyeti devlete geçer.',
    reality: 'Teslim edilmeyen payların mülkiyeti son bulmaz! Sadece temettü dışındaki hakları (oy kullanma, genel kurula katılma) donar, borsada işlem göremez ve aracı kurumlarca aracılık edilemez; hak sahipleri başvurduğunda kaydileştirilir.',
    whyImportant: 'Mülkiyet hakkı Anayasal güvence altındadır; haklar yok olmaz, sadece kaydileşene kadar donar.'
  },
  {
    id: 'trap_36',
    moduleId: '1012',
    moduleName: 'Takas & Saklama',
    myth: 'Üyelerin MKT hizmeti kapsamında Takasbank\\'a verdikleri teminatların mülkiyeti daima üyede kalır, Takasbank sadece rehin hakkına sahiptir.',
    reality: '6362 sayılı SPKn m.78 uyarınca, MKT çerçevesinde takas kuruluşları tarafından alınan teminatların MÜLKİYETİ TAKAS KURULUŞUNA (Takasbank) GEÇER; Takasbank teminatları tevdi amaçları doğrultusunda kullanabilir.',
    whyImportant: 'Teminatların mülkiyetinin Takasbank\\'a geçmesi ve kamu alacakları dahil haczedilememesi SPKn 78\\'in en temel kuralıdır.'
  },
  {
    id: 'trap_37',
    moduleId: '1012',
    moduleName: 'Takas & Saklama',
    myth: 'VİOP\\'ta açık pozisyonunda artış olmamasına rağmen diğer işlemlerin azalmasıyla oluşan pasif limit aşımlarında üyeye derhal pozisyon kapatma cezası uygulanır.',
    reality: 'Pasif aşımda olan siciller için derhal re\\'sen kapatma uygulanmaz; ancak piyasadaki ilgili dayanak varlığa bağlı toplam açık pozisyonun %12\\'si aşılırsa kapatma ve tedbir hükümleri işletilir.',
    whyImportant: 'Sınavda pasif aşım tolerans eşiği %12 olarak sorulmaktadır.'
  },
  {
    id: 'trap_38',
    moduleId: '1012',
    moduleName: 'Takas & Saklama',
    myth: 'Borçlanma Araçları Piyasası\\'ndaki (BAP) tüm pazarlarda çok taraflı netleştirme yapılır.',
    reality: 'Taahhütlü İşlemler Pazarı ve Uluslararası Tahvil Pazarı\\'ndaki (Eurotahvil) işlemler NETLEŞTİRMEYE DAHİL EDİLMEZ; takasları işlem bazında (brüt) gerçekleştirilir.',
    whyImportant: 'BAP\\'ta netleştirme dışı kalan pazarlar sınavda sıkça sorulur: Taahhütlü İşlemler ve Uluslararası Tahvil Pazarı.'
  }
];"""

# Replace end of DURATIONS array: dur_42's closing bracket
# Search for dur_42 closing:
#   }
# ];
pattern_dur = r"(id:\s*'dur_42',[\s\S]*?\}\s*)\n(\];)"
if re.search(pattern_dur, content):
    content = re.sub(pattern_dur, r"\1,\n" + new_durations, content)
    print("New durations added successfully.")
else:
    print("Error: Could not find dur_42 closing bracket.")

# Replace end of RATIOS array: rat_44
pattern_rat = r"(id:\s*'rat_44',[\s\S]*?\}\s*)\n(\];)"
if re.search(pattern_rat, content):
    content = re.sub(pattern_rat, r"\1,\n" + new_ratios, content)
    print("New ratios added successfully.")
else:
    print("Error: Could not find rat_44 closing bracket.")

# Replace end of COMPARISONS array: comp_24
pattern_comp = r"(id:\s*'comp_24',[\s\S]*?\}\s*)\n(\];)"
if re.search(pattern_comp, content):
    content = re.sub(pattern_comp, r"\1,\n" + new_comparisons, content)
    print("New comparisons added successfully.")
else:
    print("Error: Could not find comp_24 closing bracket.")

# Replace end of TRAPS array: trap_31
pattern_trap = r"(id:\s*'trap_31',[\s\S]*?\}\s*)\n(\];)"
if re.search(pattern_trap, content):
    content = re.sub(pattern_trap, r"\1,\n" + new_traps, content)
    print("New traps added successfully.")
else:
    print("Error: Could not find trap_31 closing bracket.")

with open("src/pages/CheatSheetPage.tsx", "w", encoding="utf-8") as f:
    f.write(content)
print("CheatSheetPage.tsx successfully rewritten.")
