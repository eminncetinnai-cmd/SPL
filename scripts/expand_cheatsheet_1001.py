import json
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

print("Starting execution of CheatSheet expansion...")

with open('src/pages/CheatSheetPage.tsx', 'r', encoding='utf-8') as f:
    cs_content = f.read()

# 1. Add 6 new durations (dur_25 to dur_30)
new_durations_code = """  {
    id: 'dur_25',
    moduleId: '1001',
    moduleName: 'Mevzuat',
    duration: 'Altı Ayı Aşmamak Üzere',
    title: 'TSPB Birlik Üyeliğinden Geçici Çıkarma Azami Süresi',
    description: 'TSPB Disiplin Yönetmeliği uyarınca Birlik üyesine verilen geçici çıkarma cezası fiilin mahiyetine göre altı ayı aşmamak üzere belirlenir (SPKn m. 106, 107, 109 suçlarında mahkeme kararı şarttır).',
    trap: 'Süre 1-2 yıl veya 3 ay değildir; kanuni azami üst sınır 6 aydır.'
  },
  {
    id: 'dur_26',
    moduleId: '1001',
    moduleName: 'Mevzuat',
    duration: '3. İş Günü Saat 09:00',
    title: 'Sermaye Yapısı ve Oy Hakkı Değişiklik Bildirim Süresi',
    description: 'Borsada işlem gören ihraççıların sermaye ve oy hakkı eşik (%5, 10, 15, 20, 25, 33, 50, 67, 95) değişim açıklamaları en geç işlemi izleyen 3. iş günü saat 09.00\\'a kadar yapılır (Doğrudan payları MKK otomatik duyurur).',
    trap: 'İşlemin yapıldığı gün veya 2 iş günü değil; izleyen 3. iş günü saat 09:00\\'dur.'
  },
  {
    id: 'dur_27',
    moduleId: '1001',
    moduleName: 'Mevzuat',
    duration: '6 İş Günü / En Geç 3 Ay',
    title: 'Şemsiye Fon İçtüzük Tescil ve İlk Katılma Payı İhraç Süresi',
    description: 'SPK onaylı şemsiye fon içtüzüğü 6 iş günü içinde ticaret siciline tescil ettirilir. Tescilden itibaren en geç 3 ay içinde ilk fon katılma payı ihracı için Kurul\\'a başvurulmalıdır (1 defa 3 ay uzatılabilir).',
    trap: 'İlk fon başvuru süresi 3 aydır; yapılmazsa içtüzük ticaret sicilinden terkin edilir.'
  },
  {
    id: 'dur_28',
    moduleId: '1001',
    moduleName: 'Mevzuat',
    duration: '10 İş Günü (Mazeretle 20 İş Günü)',
    title: 'TSPB Disiplin Soruşturmasında Yazılı Savunma Süresi',
    description: 'Hakkında disiplin soruşturması başlatılan üyenin tebliğden itibaren yazılı savunma verme süresi 10 iş günüdür (Mazeretle 20 iş günü). Birlik kararına SPK nezdinde itiraz süresi de tebliğden 10 iş günüdür.',
    trap: 'Savunma ve itiraz süreleri takvim günü değil, KANUNEN İŞ GÜNÜDÜR (10 iş günü).'
  },
  {
    id: 'dur_29',
    moduleId: '1001',
    moduleName: 'Mevzuat',
    duration: '2 Yıl Faaliyetsizlik / 3 Ay',
    title: 'Sermaye Piyasası Faaliyet İzinlerinin İptal Süresi',
    description: 'SPKn md. 44 uyarınca izin tarihinden itibaren 2 yıl süreyle faaliyette bulunulmaması veya şartların kaybedildiğinin tespitinden itibaren 3 ay içinde şartların sağlanamaması halinde yetki belgesi iptal edilir.',
    trap: 'Faaliyetsizlik süresi 1 yıl değil 2 yıldır; şartların düzeltilmesi süresi 3 aydır.'
  },
  {
    id: 'dur_30',
    moduleId: '1001',
    moduleName: 'Mevzuat',
    duration: '3 Ay / 3 Yıl (5 Yıl Butlan)',
    title: 'Örtülü Kazanç ve Malvarlığı Azaltıcı İşlemlerde İptal Dava Süresi',
    description: 'SPKn md. 92 uyarınca ihraççıların malvarlığını azaltıcı hukuka aykırı işlemlerinin Kurulca tespiti tarihinden itibaren 3 ay ve her halde işlemden itibaren 3 yıl içinde iptal, 5 yıl içinde butlan davası açılabilir.',
    trap: 'Öğrenmeden/tespitten itibaren 3 ay, mutlak işlem tarihinden itibaren 3 yıldır.'
  }
];"""

target_dur_end = "    trap: 'Pay Piyasası takası T+2 iken VİOP nakit uzlaşması T+1\\'dir.'\n  }\n];"
assert target_dur_end in cs_content, "target_dur_end not found"
cs_content = cs_content.replace(
    target_dur_end,
    "    trap: 'Pay Piyasası takası T+2 iken VİOP nakit uzlaşması T+1\\'dir.'\n  },\n" + new_durations_code[2:]
)

# 2. Add 6 new ratios (rat_23 to rat_28)
new_ratios_code = """  {
    id: 'rat_23',
    moduleId: '1001',
    moduleName: 'Mevzuat',
    value: '15.000.000 TL',
    title: 'İdari Sorumlular ve Ana Ortak İşlem Bildirim Eşiği (2026)',
    description: 'Özel Durumlar Tebliği (II-15.1) m. 11 uyarınca idari sorumluların veya ana ortağın bir takvim yılı içindeki pay işlemlerinin toplam tutarı 2026 yılı için belirlenen 15.000.000 TL\\'ye ulaşmadıkça açıklama yapılmaz; aşan tüm işlemler açıklanır.',
    trap: 'Eski yıllardaki 5 veya 10 milyon TL değil; resmi ders notundaki güncel Kurul eşiği 15.000.000 TL\\'dir.'
  },
  {
    id: 'rat_24',
    moduleId: '1001',
    moduleName: 'Mevzuat',
    value: '3 Mr TL PD & 750 Mn TL FD',
    title: 'Kurumsal Yönetim 1. Grup Ortaklık Eşiği',
    description: 'II-17.1 Tebliği uyarınca 1. Grup şirketler ortalama PD\\'si 3 Milyar TL ve fiili dolaşım PD\\'si 750 Milyon TL üzerinde olanlardır. 2. Grup için 1 Milyar TL ve 250 Milyon TL aranır. Bu eşikler yeniden değerlemeye tabi tutulmaz!',
    trap: 'Eşikler her yıl yeniden değerleme katsayısıyla ARTMAZ, sabit maktudur.'
  },
  {
    id: 'rat_25',
    moduleId: '1001',
    moduleName: 'Mevzuat',
    value: '%25 & %10',
    title: 'Katılım Fonu Katılma Hesabı Portföy Sınırları',
    description: 'III-52.1 Fon Tebliği\\'ne göre normal fonlarda vadeli mevduat portföyün max %10\\'u ve tek bankada max %3\\'ü olabilirken; Katılım Fonlarında katılma hesapları portföyün en fazla %25\\'i, tek katılım bankasında ise en fazla %10\\'u olabilir.',
    trap: 'Genel fonlardaki %10/%3 kuralı, katılım fonlarında faizsiz enstrüman yapısı gereği %25/%10 olarak uygulanır.'
  },
  {
    id: 'rat_26',
    moduleId: '1001',
    moduleName: 'Mevzuat',
    value: '%1,65 (Min) - %4,38 (Max)',
    title: 'Azami Fon Toplam Gider Oranları (FTGK Tavanı)',
    description: 'Fon Tebliği tablosunda yıllık azami toplam gider tavanı Para Piyasası Fonları için %1,65 (en düşük), Fon Sepeti Fonları için %4,38 (en yüksek) olarak belirlenmiştir.',
    trap: 'Serbest fonlar toplam gider tavanına tabi DEĞİLDİR.'
  },
  {
    id: 'rat_27',
    moduleId: '1001',
    moduleName: 'Mevzuat',
    value: '8 - 14 Yıl (Hileli: 14 - 20 Yıl)',
    title: 'Kripto Varlık Hizmet Sağlayıcıda Zimmet Suçu Cezası (m.110/A)',
    description: 'KVHS mensuplarının zimmet cezası 8-14 yıl hapistir. Suç hileli davranışlarla gizlenirse ceza 14-20 yıl hapis olup adli para cezası meydana gelen zararın 3 katından az olamaz!',
    trap: 'Hileli nitelikli zimmette APC cezası zararın 1 veya 2 katı değil, en az 3 katıdır.'
  },
  {
    id: 'rat_28',
    moduleId: '1001',
    moduleName: 'Mevzuat',
    value: '7 Üye',
    title: 'TSPB Disiplin Komitesi Üye Sayısı (Güncel Reform)',
    description: '7518 sayılı Kanun sonrası TSPB Disiplin Komitesi 7 üyeden oluşur: 2 aracı kurum, 1 banka, 1 PYŞ, 1 borsa YO, 1 kripto varlık hizmet sağlayıcı, 1 kitle fonlama platformu temsilcisi. Görev süresi 2 yıldır; raportör Birlik Hukuk İşleri Müdürüdür.',
    trap: 'Eski 5 üyeli yapı değişmiştir; kripto ve kitle fonlama temsilcileri eklenerek 7 üye olmuştur.'
  }
];"""

target_ratio_end = "    trap: 'Varantlarda asli değer hiçbir zaman eksi çıkmaz; minimum sıfırdır.'\n  }\n];"
assert target_ratio_end in cs_content, "target_ratio_end not found"
cs_content = cs_content.replace(
    target_ratio_end,
    "    trap: 'Varantlarda asli değer hiçbir zaman eksi çıkmaz; minimum sıfırdır.'\n  },\n" + new_ratios_code[2:]
)

# 3. Add 4 new comparisons (comp_11 to comp_14)
new_comparisons_code = """  {
    id: 'comp_11',
    moduleId: '1001',
    moduleName: 'Mevzuat',
    conceptA: {
      title: 'İzinsiz Sermaye Piyasası Faaliyeti (SPKn m.109/2)',
      desc: 'SPK\\'dan izin almaksızın yatırım hizmet ve faaliyeti yürütmek.',
      keyPoint: '2 yıldan 5 yıla kadar hapis ve 5.000 - 10.000 gün adli para cezası.'
    },
    conceptB: {
      title: 'İzinsiz Kripto Varlık Hizmet Sağlayıcılığı (SPKn m.109/A)',
      desc: 'SPK\\'dan izin almaksızın kripto platformu veya saklama faaliyeti yürütmek.',
      keyPoint: '3 yıldan 5 yıla kadar hapis ve 5.000 - 10.000 gün adli para cezası.'
    },
    differenceRule: 'İzinsiz genel sermaye piyasası faaliyetinde ceza alt sınırı 2 yıl iken, izinsiz kripto varlık hizmet sağlayıcılığında alt sınır 3 yıldır!'
  },
  {
    id: 'comp_12',
    moduleId: '1001',
    moduleName: 'Mevzuat',
    conceptA: {
      title: 'Normal Yatırım Fonu Mevduat Sınırları',
      desc: 'Fon portföyünün faizli banka mevduatında değerlendirilmesi.',
      keyPoint: 'Fon toplam değerinin en fazla %10\\'u; tek bankada en fazla %3\\'ü.'
    },
    conceptB: {
      title: 'Katılım Yatırım Fonu Katılma Hesabı Sınırları',
      desc: 'Fon portföyünün katılım bankası katılma hesaplarında değerlendirilmesi.',
      keyPoint: 'Fon toplam değerinin en fazla %25\\'i; tek katılım bankasında en fazla %10\\'u.'
    },
    differenceRule: 'Normal fonlarda mevduat sınırı %10 (tek banka %3) iken; Katılım fonlarında katılma hesabı sınırı %25 (tek banka %10) olarak uygulanır.'
  },
  {
    id: 'comp_13',
    moduleId: '1001',
    moduleName: 'Mevzuat',
    conceptA: {
      title: 'TSPB Disiplin Cezaları',
      desc: 'Meslek Birliği (TSPB) tarafından üyelere uygulanan mesleki cezalar.',
      keyPoint: 'Uyarı, Kınama, İdari Para Cezası, Birlik üyeliğinden geçici çıkarma (max 6 ay), Birlik üyeliğinden sürekli çıkarma.'
    },
    conceptB: {
      title: 'SPK İdari Tedbirleri (SPKn m.96)',
      desc: 'Düzenleyici otorite olan SPK tarafından kamu düzeni için uygulanan tedbirler.',
      keyPoint: 'Faaliyetlerin geçici durdurulması, yetki belgesi iptali, lisans iptali, imza yetkisinin kaldırılması.'
    },
    differenceRule: 'Faaliyetlerin geçici durdurulması bir Birlik disiplin cezası DEĞİL, SPK\\'nın Kanun m. 96 idari tedbiridir.'
  },
  {
    id: 'comp_14',
    moduleId: '1001',
    moduleName: 'Mevzuat',
    conceptA: {
      title: 'Sermaye Piyasası Teminat Sözleşmesi (SPKn m.47)',
      desc: 'Kayden izlenen sermaye piyasası araçlarının teminat gösterilmesi.',
      keyPoint: 'Mülkiyet devirli veya rehinli olabilir; iflas ve icra takiplerinden etkilenmez.'
    },
    conceptB: {
      title: 'Teminat Yöneticisi ve Sözleşmesi (SPKn m.31/B)',
      desc: 'Borçlanma araçları vb. ihraç yükümlülüklerinin yatırım kuruluşu güvencesine bağlanması.',
      keyPoint: 'Genel saklama yetkili yatırım kuruluşu teminat yöneticisi olur; temerrütte mahkeme veya ihbar şartı olmaksızın teminatları re\\'sen satıp paylaştırır.'
    },
    differenceRule: 'SPKn m.47 doğrudan iki taraf arasındaki menkul kıymet teminatıdır; SPKn m.31/B ise genel saklama yetkili bağımsız teminat yöneticisinin atandığı kamusal ihraç teminat mekanizmasıdır.'
  }
];"""

target_comp_end = "    differenceRule: 'Kredili alım nakit borçlanarak yükselişe oynar (%35 özkaynak); açığa satış hisse ödünç alarak düşüşe oynar (%50 özkaynak).'\n  }\n];"
assert target_comp_end in cs_content, "target_comp_end not found"
cs_content = cs_content.replace(
    target_comp_end,
    "    differenceRule: 'Kredili alım nakit borçlanarak yükselişe oynar (%35 özkaynak); açığa satış hisse ödünç alarak düşüşe oynar (%50 özkaynak).'\n  },\n" + new_comparisons_code[2:]
)

# 4. Add 5 new traps (trap_16 to trap_20)
new_traps_code = """  {
    id: 'trap_16',
    moduleId: '1001',
    moduleName: 'Mevzuat',
    myth: 'Kripto varlık hizmet sağlayıcılarının bilgi sistemleri ve teknolojik altyapı kriterlerini Bilgi Teknolojileri ve İletişim Kurumu (BTK) belirler.',
    reality: 'BTK değil, 6362 sayılı Kanun m. 35/B açıkça Türkiye Bilimsel ve Teknolojik Araştırma Kurumu\\'nun (TÜBİTAK) belirleyeceği kriterlere uygunluk şartı getirmiştir.',
    whyImportant: 'Sınavda BTK veya BDDK seçenekleri en kuvvetli çeldiricilerdir; kanunen doğru kurum TÜBİTAK\\'tır.'
  },
  {
    id: 'trap_17',
    moduleId: '1001',
    moduleName: 'Mevzuat',
    myth: 'Yatırım fonları portföyü koruma (hedge) veya arbitraj amacıyla fon toplam değerinin %10\\'una kadar açığa satış veya kredili menkul kıymet işlemi yapabilir.',
    reality: 'Yatırım fonlarının açığa satış ve kredili menkul kıymet işlemi yapması KESİNLİKLE VE HİÇBİR İSTİSNASI OLMAKSIZIN YASAKTIR (Tebliğ III-52.1 m.23).',
    whyImportant: 'Fon portföyünde türev araç bulunabilir ancak açığa satış ve kredili hisse alımı asla yapılamaz.'
  },
  {
    id: 'trap_18',
    moduleId: '1001',
    moduleName: 'Mevzuat',
    myth: 'Kripto platformunda yöneticilerin zimmet suçu işlemesi halinde şirket anonim şirket olduğu için sadece şirketin iflası istenebilir, yöneticilerin şahsen iflası istenemez.',
    reality: 'SPKn m. 110/B uyarınca müşterilere verilen zararlarla sınırlı olarak Kurulun talebi üzerine mahkemece doğrudan ortak ve yöneticilerin ŞAHSEN İFLASLARINA karar verilebilir.',
    whyImportant: 'Sermaye piyasası hukukunda tüzel kişilik perdesini aralayıp doğrudan şahsen iflas öngören istisnai maddedir.'
  },
  {
    id: 'trap_19',
    moduleId: '1001',
    moduleName: 'Mevzuat',
    myth: 'Kurumsal Yönetim Tebliği\\'ndeki şirket gruplandırma eşikleri (1. Grup: 3 Mr TL / 750 Mn TL) her yıl Maliye\\'nin yeniden değerleme katsayısı oranında artırılır.',
    reality: 'Kurumsal Yönetim Tebliği II-17.1 açık hükmü gereğince gruplandırmada kullanılan rakamsal eşikler YENİDEN DEĞERLEMEYE TABİ TUTULMAZ.',
    whyImportant: 'İdari para cezaları yeniden değerlemeyle artarken, kurumsal yönetim grup eşikleri sabit maktu kalır.'
  },
  {
    id: 'trap_20',
    moduleId: '1001',
    moduleName: 'Mevzuat',
    myth: 'Yatırımcı Tazmin Merkezi (YTM) tedrici tasfiyesinde aktiflerden öncelikle Hazine ve vergi gibi kamu alacakları ödenir.',
    reality: 'İcra İflas Kanunu\\'ndaki genel kuralın aksine SPKn m. 85 uyarınca tedrici tasfiyede 1. SIRADA MÜŞTERİ ALACAKLARI ödenir; kamu alacakları 2. sıradadır.',
    whyImportant: 'Tedrici tasfiye sıra cetveli sınavda garanti soru olup 1. sıra daima Müşteri Alacaklarıdır.'
  }
];"""

target_trap_end = "    whyImportant: 'Devir kurumu Maliye/Hazine değil, kanunen YTM\\'dir.'\n  }\n];"
assert target_trap_end in cs_content, "target_trap_end not found"
cs_content = cs_content.replace(
    target_trap_end,
    "    whyImportant: 'Devir kurumu Maliye/Hazine değil, kanunen YTM\\'dir.'\n  },\n" + new_traps_code[2:]
)

# 5. Update banner text description
cs_content = cs_content.replace(
    "24 kanuni süre, 22 kritik oran/sayı, 10 ikili kavram ayrımı ve 15 ölümcül sınav tuzağı",
    "30 kanuni süre, 28 kritik oran/sayı, 14 ikili kavram ayrımı ve 20 ölümcül sınav tuzağı (Temmuz 2026 SPL Düzey 1 Sınavına %100 Uyumlu)"
)

with open('src/pages/CheatSheetPage.tsx', 'w', encoding='utf-8') as f:
    f.write(cs_content)

print("CheatSheetPage.tsx successfully updated!")
