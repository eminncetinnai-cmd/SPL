import React, { useState, useMemo } from 'react';
import { 
  Zap,
  Brain, 
  Clock, 
  Percent, 
  Scale, 
  AlertTriangle, 
  Search, 
  Printer, 
  Play, 
  CheckCircle2, 
  HelpCircle,
  Download,
  Loader2
} from 'lucide-react';
import { ModuleId } from '../types/exam';

interface CheatSheetPageProps {
  onNavigate: (page: string, params?: any) => void;
}

interface DurationItem {
  id: string;
  moduleId: ModuleId;
  moduleName: string;
  duration: string;
  title: string;
  description: string;
  trap: string;
}

interface RatioItem {
  id: string;
  moduleId: ModuleId;
  moduleName: string;
  value: string;
  title: string;
  description: string;
  trap: string;
}

interface ComparisonItem {
  id: string;
  moduleId: ModuleId;
  moduleName: string;
  conceptA: { title: string; desc: string; keyPoint: string };
  conceptB: { title: string; desc: string; keyPoint: string };
  differenceRule: string;
}

interface DiagnosisItem {
  id: string;
  moduleId: ModuleId;
  moduleName: string;
  scenarioEvent: string;
  legalDiagnosis: string;
  applicableLaw: string;
  consequenceOrPenalty: string;
  examTrap: string;
}

interface TrapItem {
  id: string;
  moduleId: ModuleId;
  moduleName: string;
  myth: string;
  reality: string;
  whyImportant: string;
}

const DURATIONS: DurationItem[] = [
  {
    id: 'dur_1',
    moduleId: '1001',
    moduleName: 'Mevzuat',
    duration: '12 Ay',
    title: 'İzahnamenin Kanuni Geçerlilik Süresi',
    description: 'SPK onayından itibaren izahname ek ve değişikliklerin Kurulca onaylanması kaydıyla tam 12 ay boyunca geçerlidir.',
    trap: 'Sınavda 30 gün veya 6 ay şıkları konulur; süre kesinlikle 12 aydır.'
  },
  {
    id: 'dur_2',
    moduleId: '1001',
    moduleName: 'Mevzuat',
    duration: '15 - 60 Gün',
    title: 'Rüçhan Hakkı (Yeni Pay Alma) Kullanım Süresi',
    description: 'Bedelli sermaye artırımlarında pay sahiplerine tanınan rüçhan hakkı kullanım süresi en az 15 gün, en fazla 60 gün olarak belirlenir.',
    trap: 'Ayrılma hakkı süresiyle (10-20 iş günü) karıştırmayın.'
  },
  {
    id: 'dur_3',
    moduleId: '1001',
    moduleName: 'Mevzuat',
    duration: '10 - 20 İş Günü',
    title: 'Ayrılma Hakkı Başvuru Süresi',
    description: 'Önemli nitelikteki işlemlere muhalif kalan pay sahiplerinin ortaklığa başvuru süresi en az 10, en fazla 20 iş günüdür.',
    trap: 'Takvim günü değil, KANUNEN İŞ GÜNÜDÜR.'
  },
  {
    id: 'dur_4',
    moduleId: '1001',
    moduleName: 'Mevzuat',
    duration: '20 İş Günü',
    title: 'İlk Halka Arz İzahname Onay Süresi',
    description: 'Payları ilk defa halka arz edilecek ortaklıkların başvuruları belgelerin eksiksiz tesliminden itibaren 20 iş gününde karara bağlanır (Halka açık ortaklıklar için 10 iş günüdür).',
    trap: 'İlk halka arz 20 iş günü, kayıtlı ortaklık 10 iş günüdür.'
  },
  {
    id: 'dur_5',
    moduleId: '1001',
    moduleName: 'Mevzuat',
    duration: '2 İş Günü',
    title: 'İzahname Değişikliğinde Talep Geri Alma Süresi',
    description: 'İzahnamede satış sürecinde yeni bir husus ortaya çıkması durumunda, ek yayımlanmadan önce talepte bulunan yatırımcılar taleplerini en geç 2 iş günü içinde geri alabilir.',
    trap: 'Süre 2 iş günüdür; 1 hafta değildir.'
  },
  {
    id: 'dur_6',
    moduleId: '1001',
    moduleName: 'Mevzuat',
    duration: 'Son 10 Yılda 6 Yıl',
    title: 'Bağımsız Yönetim Kurulu Üyesi Azami Görev Süresi',
    description: 'Bir bağımsız yönetim kurulu üyesi, aynı şirkette son 10 yıl içinde toplamda en fazla 6 yıl görev yapabilir.',
    trap: 'Ömür boyu veya kesintisiz 10 yıl görev yapamaz.'
  },
  {
    id: 'dur_7',
    moduleId: '1001',
    moduleName: 'Mevzuat',
    duration: 'Azami 5 Yıl',
    title: 'Kayıtlı Sermaye Sistemi Tavan Yetki Süresi',
    description: 'Genel kurul tarafından yönetim kuruluna verilen kayıtlı sermaye tavanı içinde sermaye artırma yetkisi en fazla 5 yıl için geçerlidir.',
    trap: '5 yıl dolduğunda tavan yenilenmezse yönetim kurulu sermaye artıramaz.'
  },
  {
    id: 'dur_8',
    moduleId: '1001',
    moduleName: 'Mevzuat',
    duration: 'En Fazla 7 Yıl',
    title: 'Bağımsız Denetim Kuruluşu Rotasyon Süresi',
    description: 'Halka açık ortaklıklar aynı bağımsız denetim firmasından kesintisiz en fazla 7 yıl denetim alabilir (3 yıl ara vermeden tekrar seçilemez).',
    trap: 'Rotasyon süresi 5 yıl değil, 7 yıldır.'
  },
  {
    id: 'dur_9',
    moduleId: '1003',
    moduleName: 'SP Araçları',
    duration: 'En Az 1 Yıl (365 Gün)',
    title: 'Tahvil Asgari Vadesi',
    description: 'Özel sektör ve kamu tahvillerinin asgari vadesi en az 1 yıl (365 gün) olmak zorundadır.',
    trap: '1 yıldan kısa borçlanma araçları Finansman Bonosudur (30-364 gün).'
  },
  {
    id: 'dur_10',
    moduleId: '1003',
    moduleName: 'SP Araçları',
    duration: '30 - 364 Gün',
    title: 'Finansman Bonosu Vade Aralığı',
    description: 'Finansman bonolarının vadesi en az 30 gün, en fazla 364 gün (1 yıldan kısa) olarak ihraç edilir.',
    trap: 'Vadesi 1 yıl veya daha uzun olan bono ihraç edilemez.'
  },
  {
    id: 'dur_11',
    moduleId: '1003',
    moduleName: 'SP Araçları',
    duration: 'Azami 45 Gün',
    title: 'Para Piyasası Fonları Portföy Ağırlıklı Ortalama Vadesi',
    description: 'Para piyasası fonlarının portföyündeki varlıkların ağırlıklı ortalama vadesi en fazla 45 gün olabilir.',
    trap: 'Vadesine en fazla 184 gün kalmış varlıklar fona alınabilir.'
  },
  {
    id: 'dur_12',
    moduleId: '1005',
    moduleName: 'Yatırım Kur.',
    duration: '10 Yıl',
    title: 'Yatırım Kuruluşlarında Belge ve Kayıt Saklama Süresi',
    description: 'Yatırım Hizmetleri Belge ve Kayıt Tebliği (III-45.1) m. 27 ve TTK m. 82 uyarınca, müşteri emir formları, ses ve elektronik log kayıtları ile uzaktan kimlik tespitine ilişkin video görüntüleri 10 yıl saklanır.',
    trap: 'İhtilaflı belgeler 10 yıllık süreyle sınırlı olmaksızın ihtilaf kesin sonuçlanıncaya kadar saklanmak zorundadır.'
  },
  {
    id: 'dur_13',
    moduleId: '1012',
    moduleName: 'Takas & Saklama',
    duration: 'T+2 (16:45)',
    title: 'BIST Pay Piyasası Takas Valörü ve Borç Kapama Son Saati',
    description: 'Pay Piyasası hisse işlemlerinin standart takas valörü T+2 günüdür. Takas borçlarının kapatılması gereken yasal son saat 16:45\'tir; bu saatten sonra üye ihbarsız temerrüde düşer.',
    trap: 'Takas borç kapama son saati 15:00 değil, 16:45\'tir (15:00 teminat tamamlama son saatidir).'
  },
  {
    id: 'dur_14',
    moduleId: '1012',
    moduleName: 'Takas & Saklama',
    duration: 'T+0 veya T+1',
    title: 'Borçlanma Araçları Piyasası Takas Valörü',
    description: 'Tahvil ve bono kesin alım-satım işlemleri kural olarak aynı gün (T+0) veya ertesi gün (T+1) valörle takas edilir.',
    trap: 'Hisse senetleri gibi zorunlu T+2 değildir.'
  },
  {
    id: 'dur_15',
    moduleId: '1012',
    moduleName: 'Takas & Saklama',
    duration: 'T+1 (11:00)',
    title: 'VİOP Teminat Tamamlama (Margin Call) Süresi',
    description: 'VİOP nakit uzlaşması T+1 sabahı yapılır. Normal günlerde 14:30/15:00, yarım işlem günlerinde ise en geç 11:00\'e kadar teminat açığı kapatılmalıdır.',
    trap: 'Yarım günlerde saat 11:00 kuralını unutmayın.'
  },
  {
    id: 'dur_16',
    moduleId: '1012',
    moduleName: 'Takas & Saklama',
    duration: '10 Yıl',
    title: 'Sermaye Piyasası Zamanaşımı Süresi',
    description: 'Yatırım kuruluşlarında 10 yıl boyunca işlem görmeyen ve aranmayan nakit ve hisse senetleri zamanaşımına uğrayarak doğrudan YTM\'ye intikal eder.',
    trap: 'Zamanaşımı süresi 5 yıl veya 20 yıl değil, kesin olarak 10 yıldır.'
  },
  {
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
    description: 'Halka açık anonim ortaklıklarda genel kurul toplantıya çağrı ilanı, toplantı gününden en az 3 hafta önce KAP\'ta ve şirket web sitesinde yayımlanır.',
    trap: 'TTK\'daki kapalı şirketler için geçerli olan 2 haftalık süreyle karıştırmayın; halka açık şirketlerde en az 3 haftadır.'
  },
  {
    id: 'dur_19',
    moduleId: '1001',
    moduleName: 'Mevzuat',
    duration: '5 Yıl',
    title: 'SPK İdari Para Cezalarında Zamanaşımı',
    description: 'SPK\'nın idari para cezası verme yetkisi, kabahate konu fiilin işlendiği tarihten itibaren 5 yıl geçmekle zamanaşımına uğrar.',
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
    duration: 'En Geç 2 İş Günü',
    title: 'Kredili İşlemlerde Özkaynak Tamamlama Süresi',
    description: 'Seri: V, No: 65 sayılı Tebliğ m. 18 uyarınca özkaynak oranı %35 sürdürme sınırının altına düşen müşteriye bildirim yapılır; müşteri bildirimi takip eden 2 iş gününü geçmeyecek sürede özkaynağı %50 başlangıç seviyesine tamamlamak zorundadır.',
    trap: 'Özkaynak tamamlanırken sürdürme sınırına (%35) değil, başlangıç seviyesine (%50) tamamlanır; süre en geç 2 iş günüdür.'
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
    description: 'VİOP\'ta gerçekleşen vadeli işlem ve opsiyon sözleşmelerinin günlük kâr/zarar nakit hesabı ve teminat çağrıları T+1 iş günü sabahında gerçekleştirilir.',
    trap: 'Pay Piyasası takası T+2 iken VİOP nakit uzlaşması T+1\'dir.'
  },
{
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
    description: 'Borsada işlem gören ihraççıların sermaye ve oy hakkı eşik (%5, 10, 15, 20, 25, 33, 50, 67, 95) değişim açıklamaları en geç işlemi izleyen 3. iş günü saat 09.00\'a kadar yapılır (Doğrudan payları MKK otomatik duyurur).',
    trap: 'İşlemin yapıldığı gün veya 2 iş günü değil; izleyen 3. iş günü saat 09:00\'dur.'
  },
  {
    id: 'dur_27',
    moduleId: '1001',
    moduleName: 'Mevzuat',
    duration: '6 İş Günü / En Geç 3 Ay',
    title: 'Şemsiye Fon İçtüzük Tescil ve İlk Katılma Payı İhraç Süresi',
    description: 'SPK onaylı şemsiye fon içtüzüğü 6 iş günü içinde ticaret siciline tescil ettirilir. Tescilden itibaren en geç 3 ay içinde ilk fon katılma payı ihracı için Kurul\'a başvurulmalıdır (1 defa 3 ay uzatılabilir).',
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
    duration: '1 Yıl Faaliyetsizlik',
    title: 'Sermaye Piyasası Faaliyet İzinlerinin İptal Süresi',
    description: 'SPKn md. 41/1-a uyarınca faaliyet izninin verildiği tarihten itibaren 1 yıl süreyle ilgili izin kapsamında herhangi bir faaliyette bulunulmaması, faaliyet izninin iptali nedenidir.',
    trap: "Faaliyete başlamama veya ilgili izin kapsamında faaliyet yürütmeme süresi 2 yıl değil 1 yıldır; dayanak madde SPKn md. 41/1-a'dır."
  },
  {
    id: 'dur_30',
    moduleId: '1001',
    moduleName: 'Mevzuat',
    duration: '3 Ay / 3 Yıl (5 Yıl Butlan)',
    title: 'Örtülü Kazanç ve Malvarlığı Azaltıcı İşlemlerde İptal Dava Süresi',
    description: 'SPKn md. 92 uyarınca ihraççıların malvarlığını azaltıcı hukuka aykırı işlemlerinin Kurulca tespiti tarihinden itibaren 3 ay ve her halde işlemden itibaren 3 yıl içinde iptal, 5 yıl içinde butlan davası açılabilir.',
    trap: 'Öğrenmeden/tespitten itibaren 3 ay, mutlak işlem tarihinden itibaren 3 yıldır.'
  },
  {
    id: 'dur_31',
    moduleId: '1003',
    moduleName: 'SP Araçları',
    duration: '1 Yıl / 180 Gün / 90 Gün',
    title: 'Halka Arz ve Tahsisli Artırım Sonrası Pay Satmama / Kısıtlama Süreleri',
    description: 'Pay Tebliği (VII-128.1) m. 8 uyarınca halka arzda %10+ pay sahibi ortaklar ve yönetim kontrolündekiler ile ihraççı 1 YIL boyunca borsada pay satamaz/sermaye artıramaz ve halka arz fiyatının altında satamaz. Tahsisli sermaye artırımında ihraç edilen paylar da edinimden itibaren 1 YIL süreyle borsada satılamaz (MKK kilitli statü). 19/09/2024 Kurul Kararıyla bireysel dağıtım payları 90 gün borsa dışı satılamaz/virmanlanamaz; ortaklar 180 gün borsa içi dahil satış yapamaz.',
    trap: 'Tahsisli artırımda borsada satılamazlık süresi ve halka arzda %10+ ortakların satmama taahhüdü 1 yıldır (12 ay). Dağıtım alan bireysel yatırımcının borsa dışı virman yasağı ise 90 gündür; süreler karıştırılmamalıdır.'
  },
  {
    id: 'dur_32',
    moduleId: '1003',
    moduleName: 'SP Araçları',
    duration: 'En Çok 30 Gün',
    title: 'Fiyat İstikrarını Sağlayıcı İşlemler Azami Süresi',
    description: 'Payların borsada işlem görmeye başlamasından itibaren en çok 30 gün süreyle fiyat istikrarı işlemleri yapılabilir. Bu işlemler halka arz fiyatının üzerinde emir verilerek yapılamaz.',
    trap: 'Fiyat istikrarı süresi 60 gün veya 15 gün değil; kanunen en çok 30 gündür ve asla halka arz fiyatının üstüne çıkılamaz.'
  },
  {
    id: 'dur_33',
    moduleId: '1003',
    moduleName: 'SP Araçları',
    duration: 'En Az 3 Gün Önce / En Az 2 Rapor',
    title: 'Fiyat Tespit ve Halka Arz Değerlendirme Raporları Süreleri',
    description: 'Fiyat tespit raporu halka arzdan en az 3 gün önce KAP\'ta ilan edilir. Konsorsiyum liderinin son 12 ayda en az 3 analist raporu hazırlamış olması gerekir. Halka arzı takip eden 1 yıl içinde ise ilki 6 ay sonra ve aralarında en az 4 ay olmak üzere en az 2 değerlendirme raporu hazırlanır.',
    trap: 'FTR halka arzdan 1 gün önce değil en az 3 gün önce açıklanır; ilk yıl en az 2 değerlendirme raporu zorunludur.'
  },
  {
    id: 'dur_34',
    moduleId: '1003',
    moduleName: 'SP Araçları',
    duration: '5 İş Günü / En Erken 3. İş Günü',
    title: 'Pay Satış Bilgi Formu İlan ve Satış Takvimi',
    description: 'Sermayenin %3\'ünü aşan pay satışlarında onaylanan pay satış bilgi formu satıştan en az 5 iş günü önce KAP\'ta ilan edilir. Satış en erken ilandan sonraki 3. iş günü başlar, günlük işlem hacmi sermayenin %10\'unu geçemez ve form 1 yıl geçerlidir.',
    trap: 'Satış ilan günü veya ertesi gün başlayamaz; en erken ilan tarihini izleyen 3. iş günü başlayabilir.'
  },
  {
    id: 'dur_35',
    moduleId: '1003',
    moduleName: 'SP Araçları',
    duration: '3 İş Günü',
    title: 'Yurt Dışında Borçlanma Aracı İhracında MKK Bildirimi',
    description: 'Borçlanma Araçları Tebliği (VII-128.8) uyarınca, yurt dışında ihraç edilen borçlanma araçlarının ihraç tutarı, tarihi, ISIN kodu, faiz oranı ve vadesi ihraç tarihini izleyen 3 iş günü içinde MKK\'ya bildirilir.',
    trap: 'Bildirim süresi 10 veya 15 gün değil; 3 iş günüdür. Yurt dışı ihraçlar MKK nezdinde bilgi amaçlı kaydedilir.'
  },
  {
    id: 'dur_36',
    moduleId: '1003',
    moduleName: 'SP Araçları',
    duration: 'En Erken 365 Gün Sonra',
    title: 'PDT ve DET Pay Dönüştürme/Değiştirme Süresi',
    description: 'Paya Dönüştürülebilir Tahviller (PDT) ve Değiştirilebilir Tahvillerde (DET) vadeden önce paya dönüştürme/değiştirme hakkı en erken tahvilin ihraç tarihini izleyen 365 gün (1 yıl) sonra kullanılabilir.',
    trap: 'Dönüştürme hakkı ilk günden itibaren değil, kanunen en erken ihraçtan itibaren 365 gün sonra kullanılabilir.'
  },
  {
    id: 'dur_37',
    moduleId: '1005',
    moduleName: 'Yatırım Kur.',
    duration: '48 Saat',
    title: 'Kitle Fonlamasında Yatırımcı Cayma Hakkı Süresi',
    description: 'Kitle Fonlaması Tebliği (III-35/A.2) m. 18 uyarınca yatırımcılar, fon sağlamaya ilişkin ödeme emrinin verildiği andan itibaren 48 saat içinde hiçbir sebep göstermeksizin cayma hakkına sahiptir.',
    trap: 'Cayma hakkı bildirimi emanet yetkilisine iletildikten sonra en geç ertesi iş günü içinde fon tutarı iade edilir.'
  },
  {
    id: 'dur_38',
    moduleId: '1005',
    moduleName: 'Yatırım Kur.',
    duration: 'Azami 60 Gün',
    title: 'Kitle Fonlaması Kampanya Süresi',
    description: 'Kitle Fonlaması Tebliği (III-35/A.2) m. 18 uyarınca kampanya süresi, onaylı bilgi formunun kampanya sayfasında yayımlandığı tarihte başlar ve bu süre hiçbir şekilde altmış (60) günü geçemez.',
    trap: 'Sınavda 30 veya 90 gün çeldiricisi verilir; yasal azami süre 60 gündür.'
  },
  {
    id: 'dur_39',
    moduleId: '1005',
    moduleName: 'Yatırım Kur.',
    duration: '90 Gün / 30 İş Günü',
    title: 'Kitle Fonlamasında Şirketleşme ve Sermaye Artırımı',
    description: 'Fon toplama tamamlandığında girişimci kampanya bitiminden itibaren 90 gün içinde anonim şirket kurmakla yükümlüdür; şirket kurulduktan sonra ticaret sicili tescilini izleyen 30 iş günü içinde toplanan fon kadar sermaye artırımı tamamlanır.',
    trap: 'Limited şirket olan girişim şirketleri de kampanya bitimini izleyen 90 gün içinde A.Ş.\'ye dönüşmek zorundadır.'
  },
  {
    id: 'dur_40',
    moduleId: '1005',
    moduleName: 'Yatırım Kur.',
    duration: '3 Yıl',
    title: 'Kitle Fonlamasında Girişimci Pay Devri Yasağı',
    description: 'Fonlanan şirkette önemli etkiye sahip olacak ortaklar kampanya başlangıcını takip eden 3 yıl içinde fonlanan şirketteki paylarını devredemezler (miras, eşler arası mal rejimi ve cebri icra hariç).',
    trap: 'Pay devri yasağı 1 yıl veya 5 yıl değil; kanunen tam 3 yıldır.'
  },
  {
    id: 'dur_41',
    moduleId: '1005',
    moduleName: 'Yatırım Kur.',
    duration: '10 İş Günü',
    title: 'TSPB Promosyon Kampanyası Başvuru ve Sonuç Bildirimi',
    description: 'TSPB Promosyon Yönergesi m. 6 uyarınca aracı kurumlar herhangi bir promosyon kampanyası başlatmadan en az 10 iş günü önce Birliğe başvurur. Kampanyadan faydalananlara ilişkin gerçekleşen veriler de kampanya bitiminden sonra en geç 10 iş günü içinde Birliğe bildirilir.',
    trap: 'İnceleme Birlikçe 10 iş gününde sonuçlandırılır ve kampanya uygulama süresi azami 1 yıldır.'
  },
  {
    id: 'dur_42',
    moduleId: '1005',
    moduleName: 'Yatırım Kur.',
    duration: '30 İş Günü / 10 İş Günü',
    title: 'Aracı Kurum Şube ve İrtibat Bürosu İzin ve Tescil Süresi',
    description: 'Yatırım Kuruluşları Tebliği (III-39.1) m. 45 uyarınca şube veya irtibat bürosu açılış izin başvuruları Kurulca 30 iş günü içinde sonuçlandırılır. İznin tebliğini takiben 10 iş günü içinde ticaret siciline tescil ve ilan ettirilir.',
    trap: 'İrtibat bürosunun kapatılması halinde de Kurulca tebliği izleyen 10 iş günü içinde ticaret sicilinden terkin ettirilir.'
  },
  {
    id: 'dur_43',
    moduleId: '1012',
    moduleName: 'Takas & Saklama',
    duration: '16:45',
    title: 'Pay ve Borçlanma Araçları Takas Borç Kapama Son Saati',
    description: 'Borsa İstanbul Pay Piyasası ve Borçlanma Araçları Piyasası\'nda takas günü nakit ve menkul kıymet borçlarının temerrütsüz son kapatılma saati 16:45\'tir.',
    trap: '16:45\'ten sonra borcunu kapatmayan üye herhangi bir ihtara gerek kalmaksızın kendiliğinden temerrüde düşer.'
  },
  {
    id: 'dur_44',
    moduleId: '1012',
    moduleName: 'Takas & Saklama',
    duration: '15:00 (Ertesi Gün)',
    title: 'Pay Piyasası ve BAP Gün Sonu Teminat Tamamlama Son Saati',
    description: 'İşlem günü sonunda teminat açığı oluşan üyeler teminat tamamlama yükümlülüklerini bir sonraki iş günü en geç saat 15:00\'e kadar yerine getirmek zorundadır (Yarım günlerde Pay 11:00, BAP 10:00).',
    trap: 'Gün sonu çağrısı aynı gün değil, ertesi iş günü saat 15:00\'e kadar tamamlanır.'
  },
  {
    id: 'dur_45',
    moduleId: '1012',
    moduleName: 'Takas & Saklama',
    duration: '16:46 – 17:00',
    title: 'BAP Ön Temerrüt Süresi ve İndirimli Katsayı (0.25)',
    description: 'Borçlanma Araçları Piyasası\'nda 16:46-17:00 arası kapatılan borçlar ön temerrüt sayılır ve katsayı sadece 0.25 olarak uygulanır (17:01-18:45 arası 0.50, 18:46 sonrası ve ertesi günler katsayı 3).',
    trap: 'Pay Piyasası\'nda ön temerrüt yoktur (16:46-17:30 arası katsayı 1\'dir); ön temerrüt (0.25) sadece Borçlanma Araçları Piyasası\'nda vardır.'
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
    trap: 'Süre 3 takvim günü değil, 3 İŞ GÜNÜDÜR; süresinde ödenmezse Takasbank serbest hesaptan re\'sen tahsil eder.'
  },
  {
    id: 'dur_48',
    moduleId: '1012',
    moduleName: 'Takas & Saklama',
    duration: 'T+3 (11:00)',
    title: 'Pay Piyasası Re\'sen Borç Kapama ve Temerrüt Sırası',
    description: 'Pay Piyasası\'nda T+3 günü saat 11:00\'e kadar menkul kıymet veya nakit borcunu kapatamayan aracı kurumlar adına Borsa İstanbul\'da Temerrüt Sırası (Buy-in) açılarak aynı gün valörle re\'sen alım/satım yapılır.',
    trap: 'Borsa temerrüt sırası takas günü değil, takası izleyen iş günü (T+3) saat 11:00\'de devreye girer.'
  },
  {
    id: 'dur_49',
    moduleId: '1012',
    moduleName: 'Takas & Saklama',
    duration: '90 Gün',
    title: 'Portföy Saklama Sözleşmesi Fesih İhbar Süresi',
    description: 'Portföy yönetim şirketi (PYŞ) veya yatırım ortaklığı, sözleşmeli portföy saklayıcısını değiştirmek veya saklayıcı sözleşmeyi sona erdirmek isterse, bu durumu en az 90 gün önceden karşı tarafa ve SPK\'ya gerekçeleriyle bildirmek zorundadır.',
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
  },
  {
    id: 'dur_51',
    moduleId: '1001',
    moduleName: 'Mevzuat',
    duration: '1 Yıl (İhraççı & %10+ Ortak) / 6 Ay (Aracı Kurum)',
    title: 'Halka Arzda İhraççı, Ortaklar ve Aracı Kurumun Pay Satmama Taahhütleri',
    description: 'Pay Tebliği (VII-128.1) m. 8 uyarınca izahname onayındaki %10+ pay sahipleri ve yönetim kontrolündeki ortaklar 1 yıl süreyle borsada pay satamaz ve halka arz fiyatı altından satmama taahhüdü verir. İhraççı 1 yıl süreyle sermaye artıramaz. Yetkili aracı kurum ise yüklenim kapsamında aldığı satılamayan payları 6 ay süreyle halka arz fiyatı altında satamaz.',
    trap: 'Ortakların ve ihraççının taahhüdü 1 yıl (12 ay) iken, yetkili aracı kurumun yüklenim paylarını halka arz fiyatının altında satmama taahhüdü 6 aydır.'
  },
  {
    id: 'dur_52',
    moduleId: '1001',
    moduleName: 'Mevzuat',
    duration: 'Şirket Onayı / 24 Ay',
    title: 'Halka Açık Olmayan A.Ş.\'de Sermaye Artırımı Sonrası Pay Devri ve Bedel Ödeme Süresi',
    description: 'TTK m. 491 uyarınca bedeli tamamen ödenmemiş nama yazılı paylar şirket onayı olmadıkça devredilemez. Nakdi sermaye artırımında taahhüt edilen pay bedellerinin en az %25\'i tescilden önce, kalanı tescili izleyen 24 ay içinde ödenir. Esas sözleşmeye bağlam konularak pay devri haklı sebeplerle şirket onayına bağlanabilir (TTK m. 492-493).',
    trap: 'Halka açık olmayan şirketlerde pay devri kural olarak serbesttir; ancak bedeli tam ödenmemiş paylar şirket onayı olmadan asla devredilemez.'
  },
  {
    id: 'dur_53',
    moduleId: '1001',
    moduleName: 'Mevzuat',
    duration: '60 Gün (Solo) / 70 Gün (Konsolide)',
    title: 'Yıllık Finansal Raporların Kamuya Açıklanma Yasal Süresi',
    description: 'Sermaye Piyasasında Finansal Raporlamaya İlişkin Esaslar Tebliği (II-14.1) m. 10 uyarınca, yıllık tam bağımsız denetimden geçmiş finansal raporların solo ortaklıklarda hesap dönemini izleyen 60 gün, konsolide ortaklıklarda ise en geç 70 gün içinde KAP\'ta açıklanması zorunludur.',
    trap: 'Solo ile konsolide arasındaki 10 günlük farkı unutmayın; 6 aylık raporlarda süre solo için 40, konsolide için 50 gündür.'
  },
  {
    id: 'dur_54',
    moduleId: '1003',
    moduleName: 'SP Araçları',
    duration: 'En Az 30 Gün Önce',
    title: 'Yatırım Fonu Birleşme İlanı ve Komisyonsuz Çıkış Süresi',
    description: 'Yatırım Fonlarına İlişkin Esaslar Tebliği (III-52.1) m. 27 uyarınca fon birleşme kararı birleşme tarihinden en az 30 gün önce KAP\'ta ilan edilir. Katılma payı sahipleri bu 30 günlük süre içinde hiçbir komisyon ödemeksizin paylarını fona iade etme hakkına sahiptir.',
    trap: 'İlan ve ayrılma süresi 15 gün veya 1 ay değil, kanunen en az 30 gündür.'
  },
  {
    id: 'dur_55',
    moduleId: '1001',
    moduleName: 'Mevzuat',
    duration: '6 İş Günü / 45 İş Günü',
    title: 'Zorunlu Pay Alım Teklifi (Çağrı) Başvuru ve Fiili Başlama Süresi',
    description: 'Pay Alım Teklifi Tebliği (II-26.1) uyarınca ortaklıkta %50 üzeri oy hakkı veya yönetim kontrolü kazanıldığında en geç 6 iş günü içinde SPK\'ya başvurulur. Kurul onayından sonra en geç 45 iş günü içinde fiili teklif başlar ve talep toplama 10 - 20 iş günü sürer.',
    trap: 'Başvuru süresi 30 gün değil 6 iş günüdür; fiili teklif süresi ise en az 10 iş günü, en fazla 20 iş günüdür.'
  },
  {
    id: 'dur_56',
    moduleId: '1005',
    moduleName: 'Yatırım Kur.',
    duration: 'En Geç 2 İş Günü (T+2)',
    title: 'Kredili İşlemlerde Özkaynak Tamamlama ve 2 Kat Hisse Senedi Kuralı',
    description: 'Özkaynak oranı %35\'in altına düştüğünde aracı kurum çağrı yapar ve özkaynak başlangıç oranı olan %50\'ye tamamlanır. Süre en geç 2 iş günüdür. Nakit yerine hisse senedi getirilirse %50 katsayı uygulandığından nakit açığının tam 2 KATI değerinde hisse getirilmelidir.',
    trap: 'Özkaynak %35\'e değil %50\'ye tamamlanır; hisse senedi getirilirse nakit açığının 1 katı değil 2 katı hisse piyasa değeri gerekir.'
  },
  {
    id: 'dur_57',
    moduleId: '1001',
    moduleName: 'Mevzuat',
    duration: '3 Ay (Hak Düşürücü Süre)',
    title: 'Ortaklıktan Çıkarma ve Satma Hakkı Kullanım Süresi (II-27.2)',
    description: 'Ortaklığın oy haklarının en az %98\'ine ulaşarak Hâkim Ortak konumunun kazanıldığının KAP\'ta ilan edildiği tarihten itibaren 3 aylık hak düşürücü süre içinde azınlık pay sahipleri satma hakkını, hâkim ortak ise çıkarma hakkını kullanabilir. Değerleme raporu zorunludur.',
    trap: 'Eşik %95 değil %98\'dir; kullanım süresi ise 1 ay veya 6 iş günü değil, KAP ilanından itibaren 3 aydır.'
  },
  {
    id: 'dur_58',
    moduleId: '1012',
    moduleName: 'Takas & Saklama',
    duration: 'T+1 Saat 15:00 (Yarım Gün 11:00)',
    title: 'VİOP Teminat Tamamlama Çağrısı (Margin Call) ve Başlangıç Teminatına Çıkma',
    description: 'Gün sonu değerlemesi sonrası teminatı Sürdürme Teminatının altına düşen pozisyonlar için T+1 günü en geç saat 15:00\'e kadar (yarım günlerde 11:00) teminatın Sürdürme seviyesine değil, BAŞLANGIÇ TEMİNATI seviyesine tamamlanması zorunludur.',
    trap: 'Sayısal sorularda mevcut teminatı sürdürme teminatından değil, DAİMA BAŞLANGIÇ TEMİNATINDAN çıkararak tamamlama tutarını hesaplayın!'
  }
];

const RATIOS: RatioItem[] = [
  {
    id: 'rat_1',
    moduleId: '1001',
    moduleName: 'Mevzuat',
    value: '%98',
    title: 'Ortaklıktan Çıkarma ve Satma Hakkı Eşiği',
    description: 'Hâkim ortaklık payı %98 oy oranına ulaştığında azınlığı şirketten çıkarma hakkı ve azınlığın paylarını satma hakkı doğar.',
    trap: 'Eşik %50 veya %75 değil, kesinlikle %98\'dir.'
  },
  {
    id: 'rat_2',
    moduleId: '1001',
    moduleName: 'Mevzuat',
    value: '1/3 & En Az 2 Üye',
    title: 'Bağımsız Yönetim Kurulu Üye Kuralı',
    description: 'Halka açık ortaklıklarda bağımsız yönetim kurulu üye sayısı toplam üye sayısının en az üçte biri (1/3) ve asgari 2 üye olmalıdır. Küsuratlar yukarı yuvarlanır.',
    trap: 'Örn: 7 kişilik YK için 7/3 = 2.33 -> En az 3 bağımsız üye zorunludur.'
  },
  {
    id: 'rat_3',
    moduleId: '1001',
    moduleName: 'Mevzuat',
    value: '500 Ortak',
    title: 'Halka Açık Sayılma Eşiği (SPKn m.16)',
    description: 'Payları borsada işlem görmeyen anonim şirketlerin ortak sayısı 500\'ü aştığında şirket kanunen halka açık sayılır ve SPK\'ya tabi olur.',
    trap: 'Sınavda 250 veya 1.000 çeldiricisi konur; eşik 500\'dür.'
  },
  {
    id: 'rat_4',
    moduleId: '1001',
    moduleName: 'Mevzuat',
    value: '3 - 5 Yıl Hapis & 2 Katı',
    title: 'Piyasa Dolandırıcılığı (Manipülasyon) ve Etkin Pişmanlık',
    description: 'İşlem ve bilgi bazlı manipülasyonun cezası 3 yıldan 5 yıla kadar hapis ve adli para cezasıdır. İnceleme öncesi elde edilen menfaatin 2 KATI Hazineye ödenirse ceza verilmez.',
    trap: 'Bilgi bazlı manipülasyonda (yalan haber) etkin pişmanlık uygulanmaz!'
  },
  {
    id: 'rat_5',
    moduleId: '1001',
    moduleName: 'Mevzuat',
    value: '1/4 (%25)',
    title: 'TTK Olağan Genel Kurul Toplantı Nisabı',
    description: 'Anonim ortaklıklarda olağan genel kurul sermayenin en az dörtte biriyle (%25) toplanır; kararlar katılanların çoğunluğuyla alınır.',
    trap: 'İkinci toplantıda asgari toplantı nisabı aranmaz.'
  },
  {
    id: 'rat_6',
    moduleId: '1003',
    moduleName: 'SP Araçları',
    value: 'En Fazla 15 Oy',
    title: 'Oyda İmtiyaz Sınırı (SPKn m.18)',
    description: 'Halka açık ortaklıklarda 1 paya tanınabilecek azami oy hakkı sayısı kural olarak en fazla 15 oydur.',
    trap: 'Esas sözleşme değişikliği ve YK ibra oylamasında imtiyaz kullanılamaz.'
  },
  {
    id: 'rat_7',
    moduleId: '1003',
    moduleName: 'SP Araçları',
    value: 'En Az %95',
    title: 'Borsa Yatırım Fonu (BYF) Endeks Takip Korelasyonu',
    description: 'BYF portföy değeri ile takip ettiği baz endeks arasındaki korelasyon katsayısının en az %95 (0,95) olması yasal zorunluluktur.',
    trap: 'Oran %90 değil, en az %95\'tir.'
  },
  {
    id: 'rat_8',
    moduleId: '1003',
    moduleName: 'SP Araçları',
    value: 'En Az %51',
    title: 'GYO Asgari Gayrimenkul Portföy Oranı',
    description: 'GYO portföy değerinin en az %51\'i gayrimenkul, gayrimenkul projesi ve gayrimenkule dayalı haklardan oluşmak zorundadır.',
    trap: 'GYO\'lar kurumlar vergisinden muaftır (%0) ancak İNŞAAT YAPAMAZLAR.'
  },
  {
    id: 'rat_9',
    moduleId: '1003',
    moduleName: 'SP Araçları',
    value: 'En Az %80',
    title: 'Hisse Senedi Yoğun Fon Portföy Sınırı',
    description: 'Bir yatırım fonunun hisse senedi yoğun fon sayılabilmesi için portföyünün en az %80\'inin sürekli BIST paylarından oluşması şarttır.',
    trap: 'Fon Sepeti Fonunda da en az %80 fon katılma payı şartı vardır.'
  },
  {
    id: 'rat_greeks',
    moduleId: '1003',
    moduleName: 'SP Araçları',
    value: 'Delta • Gamma • Teta • Vega • Rho',
    title: 'Varant Greeks — Hızlı Ezber',
    description: 'Delta (Δ): dayanak varlık fiyatındaki değişimin varant fiyatına etkisi. Gamma (Γ): Delta\'nın değişim hızı. Teta (Θ): zaman geçtikçe varant değerindeki değişim ve zaman erimesi. Vega (ν): oynaklık değişiminin varant fiyatına etkisi. Rho (ρ): faiz oranındaki değişimin varant fiyatına etkisi.',
    trap: 'Delta = fiyat, Gamma = Delta değişimi, Teta = zaman, Vega = volatilite, Rho = faiz.'
  },
  {
    id: 'rat_10',
    moduleId: '1005',
    moduleName: 'Yatırım Kur.',
    value: '45M / 190M / 380M TL',
    title: 'Aracı Kurum Asgari Özsermaye Tabanları (2026)',
    description: '2026 yılı için asgari özsermaye şartları: Dar Yetkili 45.000.000 TL, Kısmi Yetkili 190.000.000 TL, Geniş Yetkili 380.000.000 TL\'dir. Yeni kurulacak aracı kurumlarda 2026 asgari kuruluş sermayesi ise 440.000.000 TL\'dir.',
    trap: 'Sınavda eski yılların tutarları (25M/75M/150M veya 300M) çeldirici olarak verilir; 2026 tutarları 45M / 190M / 380M ve kuruluş için 440M TL\'dir.'
  },
  {
    id: 'rat_11',
    moduleId: '1005',
    moduleName: 'Yatırım Kur.',
    value: 'Başlangıç %50 / Sürdürme %35',
    title: 'Kredili Menkul Kıymet ve Açığa Satış Özkaynak Oranları',
    description: 'Seri: V, No: 65 sayılı Tebliğ m. 17 ve 25 uyarınca; hem kredili alımda hem açığa satışta başlangıç özkaynak oranı asgari %50, işlemler devam ederken sürdürme özkaynak oranı asgari %35\'tir.',
    trap: 'Özkaynak tamamlanırken %35\'e değil, başlangıç seviyesine (%50) yükseltilmek zorundadır.'
  },
  {
    id: 'rat_12',
    moduleId: '1005',
    moduleName: 'Yatırım Kur.',
    value: '1:10 & 50.000 TL',
    title: 'Forex (Kaldıraçlı İşlemler) Yasal Sınırları',
    description: 'Yurt içi yerleşik bireysel müşteriler için azami kaldıraç 1:10, asgari başlangıç teminatı ise 50.000 TL veya muadili dövizdir.',
    trap: 'Yurt dışındaki 1:100 veya 1:400 gibi kaldıraçlar Türkiye\'de kanunen yasaktır.'
  },
  {
    id: 'rat_13',
    moduleId: '1005',
    moduleName: 'Yatırım Kur.',
    value: 'Aktif 500M / Satış 1 Mr / Özkaynak 50M',
    title: 'Kurumsal Profesyonel Müşteri Eşikleri (18.12.2025 SPK Kararı)',
    description: '19.12.2025 tarihinden itibaren ilk kez profesyonel müşteri sınıfına girecek şirketlerde: Aktif toplamının 500 Milyon TL, Yıllık net hasılatının 1 Milyar TL, Özsermayesinin 50 Milyon TL üzerinde olması kıstaslarından EN AZ İKİSİNİ sağlaması şarttır.',
    trap: 'Eski 50M / 90M / 5M (veya 4.5M) eşikleri güncellenmiştir; yeni eşikler 500M / 1 Mr / 50M TL\'dir.'
  },
  {
    id: 'rat_14',
    moduleId: '1003',
    moduleName: 'SP Araçları',
    value: 'Kirli = Temiz + İşlemiş Faiz',
    title: 'Tahvil Fiyatlama ve Takas Ödeme Eşitliği',
    description: 'Borsa ekranında Temiz Fiyat kote edilir. İşlemiş Faiz = Nominal × Kupon Oranı × (Geçen Gün / 365). Alıcı satıcıya takasta Kirli Fiyat üzerinden ödeme yapar.',
    trap: 'Kupon ödeme gününde İşlemiş Faiz = 0 olduğu için Temiz Fiyat ile Kirli Fiyat birbirine EŞİTTİR.'
  },
  {
    id: 'rat_15',
    moduleId: '1005',
    moduleName: 'Yatırım Kur.',
    value: '10 Milyon TL Finansal Varlık',
    title: 'Bireysel Nitelikli Yatırımcı & Serbest Fon Eşiği (GÜNCEL)',
    description: 'Bireysel yatırımcıların talep üzerine Profesyonel Müşteri / Nitelikli Yatırımcı sayılabilmesi için gereken finansal varlık tutarı 1.000.000 TL\'den 10.000.000 TL\'ye yükseltilmiştir. Serbest Yatırım Fonları (Hedge Fund) katılma payları yalnızca bu eşiği aşan Nitelikli Yatırımcılara satılabilir.',
    trap: 'Eski 1 Milyon TL kuralı kaldırılmıştır! Güncel eşik kesinlikle 10 MİLYON TL\'dir.'
  },
  {
    id: 'rat_16',
    moduleId: '1001',
    moduleName: 'Mevzuat',
    value: '%10 Yıllık Net Gelir',
    title: 'Kitle Fonlaması Bireysel Yatırım Sınırı',
    description: 'Kitle fonlamasında nitelikli yatırımcı olmayan gerçek kişiler, bir takvim yılında beyan ettikleri yıllık net gelirlerinin en fazla %10\'u kadar yatırım yapabilirler. Nitelikli yatırımcılara ise sınır uygulanmaz.',
    trap: 'Nitelikli yatırımcılar için üst sınır yoktur; %10 sınırı genel bireysel yatırımcılar içindir.'
  },
  {
    id: 'rat_17',
    moduleId: '1001',
    moduleName: 'Mevzuat',
    value: '%5 Değerleme / %10 Genel Kurul',
    title: 'İlişkili Taraf İşlemleri Eşikleri',
    description: 'Halka açık ortaklıkların ilişkili taraflarla yapacağı varlık veya hizmet devirlerinde işlem tutarı aktif toplamı veya hasılatın %5\'ini aşarsa değerleme raporu; %10\'unu aşarsa genel kurul kararı zorunludur.',
    trap: '%5\'te sadece değerleme raporu şarttır; %10\'da ise genel kurul onayı ve bağımsız üyelerin çoğunluğu aranır.'
  },
  {
    id: 'rat_18',
    moduleId: '1001',
    moduleName: 'Mevzuat',
    value: 'Yıldız 1 Ay / Diğerleri 6 Ay',
    title: 'Ayrılma Hakkı Fiyat Belirleme Süresi',
    description: 'Önemli nitelikteki işlemlerde ayrılma hakkı kullanım fiyatı, işlemin ilk açıklandığı tarihten önceki; Yıldız Pazar\'da son 1 aylık, diğer pazarlarda son 6 aylık borsa düzeltilmiş ağırlıklı ortalama fiyatıdır.',
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
    description: 'Borsa İstanbul\'da açığa satış işlemlerinde müşterinin pozisyon açılışında bulundurması gereken başlangıç özkaynak oranı en az %50, sürdürme özkaynak oranı ise %20\'dir.',
    trap: 'Kredili alımda başlangıç %35 iken, açığa satışta risk daha yüksek olduğu için başlangıç %50\'dir.'
  },
  {
    id: 'rat_21',
    moduleId: '1001',
    moduleName: 'Mevzuat',
    value: 'En Az %25 Nakit & 24 Ay',
    title: 'Anonim Şirket Sermaye Taahhüdü Ödeme Kuralı',
    description: 'Anonim şirketlerin nakdi sermaye taahhüdünün en az %25\'i tescilden önce bankada bloke edilerek ödenmeli; kalan %75\'i ise tescili izleyen 24 ay içinde ödenmelidir.',
    trap: 'Tamamının tescilden önce ödenmesi şart değildir; en az %25\'i yeterlidir.'
  },
  {
    id: 'rat_22',
    moduleId: '1003',
    moduleName: 'SP Araçları',
    value: 'Asli Değer = Max(0, S - K) x Çarpan',
    title: 'Alım Varantı Asli Değer (Intrinsic Value) Formülü',
    description: 'Alım varantlarında Asli Değer = (Spot Fiyat - Kullanım Fiyatı) x Çarpan formülüyle hesaplanır. Spot fiyat kullanım fiyatının altındaysa Asli Değer KESİNLİKLE SIFIRDIR; asla negatif olamaz.',
    trap: 'Varantlarda asli değer hiçbir zaman eksi çıkmaz; minimum sıfırdır.'
  },
{
    id: 'rat_23',
    moduleId: '1001',
    moduleName: 'Mevzuat',
    value: '15.000.000 TL',
    title: 'İdari Sorumlular ve Ana Ortak İşlem Bildirim Eşiği (2026)',
    description: 'Özel Durumlar Tebliği (II-15.1) m. 11 uyarınca idari sorumluların veya ana ortağın bir takvim yılı içindeki pay işlemlerinin toplam tutarı 2026 yılı için belirlenen 15.000.000 TL\'ye ulaşmadıkça açıklama yapılmaz; aşan tüm işlemler açıklanır.',
    trap: 'Eski yıllardaki 5 veya 10 milyon TL değil; resmi ders notundaki güncel Kurul eşiği 15.000.000 TL\'dir.'
  },
  {
    id: 'rat_24',
    moduleId: '1001',
    moduleName: 'Mevzuat',
    value: '3 Mr TL PD & 750 Mn TL FD',
    title: 'Kurumsal Yönetim 1. Grup Ortaklık Eşiği',
    description: 'II-17.1 Tebliği uyarınca 1. Grup şirketler ortalama PD\'si 3 Milyar TL ve fiili dolaşım PD\'si 750 Milyon TL üzerinde olanlardır. 2. Grup için 1 Milyar TL ve 250 Milyon TL aranır. Bu eşikler yeniden değerlemeye tabi tutulmaz!',
    trap: 'Eşikler her yıl yeniden değerleme katsayısıyla ARTMAZ, sabit maktudur.'
  },
  {
    id: 'rat_25',
    moduleId: '1001',
    moduleName: 'Mevzuat',
    value: '%25 & %10',
    title: 'Katılım Fonu Katılma Hesabı Portföy Sınırları',
    description: 'III-52.1 Fon Tebliği\'ne göre normal fonlarda vadeli mevduat portföyün max %10\'u ve tek bankada max %3\'ü olabilirken; Katılım Fonlarında katılma hesapları portföyün en fazla %25\'i, tek katılım bankasında ise en fazla %10\'u olabilir.',
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
  },
{
    id: 'rat_29',
    moduleId: '1003',
    moduleName: 'SP Araçları',
    value: '750 Mn TL & 1.5 Mr TL',
    title: 'Payların İlk Halka Arzında Yüklenim Zorunluluğu 2026 Eşikleri',
    description: 'Pay Tebliği m. 5 ve 2026 Kurul Bülteni uyarınca halka arz edilen payların piyasa değeri 750 Milyon TL\'ye kadar olan kısım için satılamayan payların tamamı; 750 Milyon TL ile 1.5 Milyar TL arası için 750 Mn TL\'nin tamamı ve aşan kısmın yarısı bakiye yüklenim zorunludur. 1.5 Milyar TL üzerinde yüklenim zorunluluğu yoktur.',
    trap: 'Eski 20 Mn / 40 Mn veya 150 Mn / 300 Mn TL tutarları yürürlükten kalkmıştır; güncel 2026 eşikleri 750 Mn TL ve 1.5 Mr TL\'dir.'
  },
  {
    id: 'rat_30',
    moduleId: '1003',
    moduleName: 'SP Araçları',
    value: '950.000.000 TL',
    title: 'Satışa Hazır Bekletilen Paylar 2026 Piyasa Değeri Eşiği',
    description: 'Halka arz edilen payların piyasa değeri 950 Milyon TL\'nin altında olan şirketlerde, halka arz edilen payların nominal değerinin %25\'ine tekabül eden paylar 1 yıl süreyle satışa hazır bekletilmek zorundadır. Bu paylar 1 yıl boyunca halka arz fiyatının en az %25 üzerinde olmadan satılamaz.',
    trap: '2026 yeniden değerleme eşiği tam 950.000.000 TL\'dir (Eski 370 Mn veya 400 Mn TL değildir).'
  },
  {
    id: 'rat_31',
    moduleId: '1003',
    moduleName: 'SP Araçları',
    value: '50 Mn / 25 Mn / 25 Mn TL',
    title: 'Girişim Sermayesi Pazarı (GSP) 2026 Finansal Şartları',
    description: 'GSP\'de nitelikli yatırımcılara sermaye artırımı yoluyla pay ihraç edecek şirketlerin 2026 yılı için aktif toplamı en az 50 Milyon TL, net satış hasılatı en az 25 Milyon TL ve tescilli sermayesi en az 25 Milyon TL olmalıdır. Ek pay satışı yapılamaz, satış 2 iş günüdür.',
    trap: 'GSP\'de mevcut ortak pay satışı veya ek pay satışı yapılamaz; sadece sermaye artırımı yoluyla pay satılabilir.'
  },
  {
    id: 'rat_32',
    moduleId: '1003',
    moduleName: 'SP Araçları',
    value: '5 Kat / 3 Kat',
    title: 'Borçlanma Araçları Genel İhraç Tavanı Limiti',
    description: 'Borçlanma Araçları Tebliği (VII-128.8) uyarınca ihraç tavanı halka açık ortaklıklarda yetkili organ karar tarihli finansal tablolardaki özkaynakların 5 katını, halka açık olmayanlarda ise 3 katını geçemez. Yatırım yapılabilir en yüksek ilk 3 kademe derecelendirme notuna sahip bankalarda bu oranlar %100 artırılır (10 kat / 6 kat).',
    trap: 'Tavan sermayenin değil, ÖZKAYNAKLARIN katı olarak hesaplanır. İpotek finansmanı kuruluşlarında ise bu limit uygulanmaz.'
  },
  {
    id: 'rat_33',
    moduleId: '1003',
    moduleName: 'SP Araçları',
    value: 'On Binde 5 – On Binde 15',
    title: 'Borçlanma Araçlarında SPK Kurul Ücreti Kademeleri',
    description: 'Yurt içi borçlanma aracı ihraçlarında SPK ücreti vadeye göre kademelidir: 179 güne kadar on binde 5; 180-364 gün arası on binde 7; 365-730 gün arası binde 1; 730 günden uzun vadelerde on binde 15\'tir (Halka açık olmayan ortaklıklarda bu oranların %75\'i uygulanır; Yeşil borçlanma araçlarında ise %50 indirimlidir).',
    trap: 'Kurul ücreti tek bir maktu oran değildir; vade uzadıkça on binde 5\'ten on binde 15\'e doğru kademeli olarak artar.'
  },
  {
    id: 'rat_34',
    moduleId: '1003',
    moduleName: 'SP Araçları',
    value: '%50',
    title: 'Katılma İntifa Senetleri (KİS) Azami İhraç Limiti',
    description: 'Pay Tebliği m. 36 uyarınca ihraç edilecek Katılma İntifa Senetlerinin (KİS) toplam tutarı, ihraççı şirketin ödenmiş veya çıkarılmış sermayesinin en çok %50\'si kadar olabilir. KİS sahiplerine yeni pay alma hakkı verilemez.',
    trap: 'Limit sermayenin tamamı veya 2 katı değil, en fazla %50\'sidir.'
  },
  {
    id: 'rat_35',
    moduleId: '1003',
    moduleName: 'SP Araçları',
    value: '2/3 Çoğunluk',
    title: 'BASK (Borçlanma Aracı Sahipleri Kurulu) Karar Nisabı',
    description: 'Tebliğ II-31/A.1 uyarınca Tertip BASK ve Genel BASK, ihraç şartlarında yapılacak değişiklikleri ve hak feragatlerini toplantıya katılan veya temsil edilen tedavüldeki nominal tutarın en az 2/3 çoğunluğunun olumlu oyu ile karara bağlar.',
    trap: 'Karar nisabı basit çoğunluk (%51) değil; nitelikli 2/3 (üçte iki) çoğunluktur.'
  },
  {
    id: 'rat_36',
    moduleId: '1003',
    moduleName: 'SP Araçları',
    value: '±%10 (Akşam ±%3)',
    title: 'VİOP BIST 30 Endeks VİS Fiyat Değişim Sınırı',
    description: 'VİOP BIST 30 Endeks vadeli işlem sözleşmelerinde bir seans boyunca fiyatlar önceki uzlaşma fiyatının en fazla %10 yukarısına veya aşağısına gelebilir (günlük limit ±%10). Akşam seansında ise uygulanacak fiyat değişim limiti baz fiyatın en çok ±%3\'üdür.',
    trap: 'Normal seans tavan/taban limiti ±%10 iken, akşam seansı limiti çok daha dardır (±%3).'
  },
  {
    id: 'rat_37',
    moduleId: '1005',
    moduleName: 'Yatırım Kur.',
    value: '15.000.000 TL',
    title: 'Kitle Fonlama Platformu Asgari Sermaye Şartı',
    description: 'Kitle Fonlaması Tebliği (III-35/A.2) m. 5 uyarınca platformların asgari 15.000.000 TL nakden ödenmiş sermayeye ve özsermayeye sahip olması şarttır. Kuruluş özsermaye şartı listeye alınmayı takip eden ilk 2 yıl yarı oranında uygulanır.',
    trap: 'Platformlar münhasıran paya ve/veya borçlanmaya dayalı kitle fonlaması yapabilir; gayrimenkul kitle fonlaması yapamaz.'
  },
  {
    id: 'rat_38',
    moduleId: '1005',
    moduleName: 'Yatırım Kur.',
    value: '500.000 TL (Max 2.000.000 TL)',
    title: 'Kitle Fonlamasında Bireysel Yatırım Sınırları',
    description: 'Kitle Fonlaması Tebliği (III-35/A.2) m. 16 uyarınca nitelikli olmayan gerçek kişiler bir takvim yılında paya dayalı kitle fonlamasında azami 500.000 TL yatırım yapabilir; beyan edilen yıllık net gelirin %10\'u oranında uygulanırsa bu üst sınır en fazla 2.000.000 TL\'dir.',
    trap: 'Nitelikli yatırımcılar bu yatırım sınırlarına tabi değildir; istedikleri tutarda yatırım yapabilirler.'
  },
  {
    id: 'rat_39',
    moduleId: '1005',
    moduleName: 'Yatırım Kur.',
    value: '200.000 TL',
    title: 'Borçlanmaya Dayalı Kitle Fonlamasında Tek Proje Sınırı',
    description: 'Kitle Fonlaması Tebliği (III-35/A.2) m. 20 uyarınca nitelikli yatırımcı olmayan gerçek kişiler, borçlanmaya dayalı kitle fonlaması yoluyla tek bir projeye en fazla 200.000 TL yatırım yapabilir.',
    trap: 'Takvim yılı genel toplamı 500.000 TL (veya max 2M TL) iken, tek bir projeye azami sınır 200.000 TL\'dir.'
  },
  {
    id: 'rat_40',
    moduleId: '1005',
    moduleName: 'Yatırım Kur.',
    value: 'DİBS + %50 & Azami 5 Yıl',
    title: 'Borçlanmaya Dayalı Kitle Fonlaması Faiz ve Vade Tavanı',
    description: 'Kitle Fonlaması Tebliği (III-35/A.2) m. 20 uyarınca borçlanma aracının faiz oranı en yakın iki DİBS faiz ortalamasının %50 fazlasını aşamaz. Azami vade 5 yıldır ve geri ödeme tek seferde yapılamaz (kademeli itfa kuralı).',
    trap: 'Vadesi 1-2 yıl olanlarda son 3 ayda en fazla %15, vadesi 2-3 yıl olanlarda son 6 ayda en fazla %25 itfa yapılabilir.'
  },
  {
    id: 'rat_41',
    moduleId: '1005',
    moduleName: 'Yatırım Kur.',
    value: '%20 / %50 / %100',
    title: 'Açık Takas Pozisyonu Asgari Net Varlık Oranları',
    description: 'Kredili İşlemler Tebliği (Seri: V, No: 65) m. 9 uyarınca takası henüz gerçekleşmemiş pay alımlarında müşterinin bulundurması gereken net varlık oranı: Yıldız Pazar için %20, Ana Pazar için %50, Alt Pazar/YİP/PÖİP için %100\'dür.',
    trap: 'Yıldız pazarda müşteri 20 TL varlıkla 100 TL alım yapabilir; risk azami %21 günlük marj ile dengelenir.'
  },
  {
    id: 'rat_42',
    moduleId: '1005',
    moduleName: 'Yatırım Kur.',
    value: '403.359 TL (veya %5)',
    title: 'Kredili ve Ödünç İşlemlerde Temerrüt Bildirim Muafiyeti (2026)',
    description: 'Kredili İşlemler Tebliği (Seri: V, No: 65) m. 35 uyarınca üç ayda ikiden fazla takas veya özkaynak yükümlülüğünü yerine getirmeyenler Borsaya bildirilir; ancak temerrüt tutarı 2026 yılı itibarıyla 403.359 TL altında kalan veya müşterinin net varlığının %5\'ini aşmayanlar bildirilmez.',
    trap: 'Bildirilen müşterilerin alım emirleri hiçbir aracı kurumca 6 ay süreyle kabul edilmez.'
  },
  {
    id: 'rat_43',
    moduleId: '1005',
    moduleName: 'Yatırım Kur.',
    value: 'Binde 5 (‰5)',
    title: 'Aracı Kurumların Bir Mali Yılda Yapabileceği Azami Bağış',
    description: 'Yatırım Kuruluşları Tebliği (III-39.1) m. 56/1-k uyarınca aracı kurumlar bir mali yılda kendi özsermayelerinin binde beşini (‰5) aşacak miktarda bağış yapamazlar.',
    trap: 'Sınavda yüzde beş (%5) veya yüzde bir (%1) çeldiricisi verilir; sınır BİNDE BEŞTİR (‰5).'
  },
  {
    id: 'rat_44',
    moduleId: '1005',
    moduleName: 'Yatırım Kur.',
    value: '%25 (Geniş Yetkilide %50)',
    title: 'Aracı Kurumların Finansal Olmayan Ortaklıklara İştirak Sınırı',
    description: 'Yatırım Kuruluşları Tebliği (III-39.1) m. 40 uyarınca aracı kurumların sermaye piyasası ve finans kuruluşları dışındaki şirketlere yapabilecekleri iştirakler toplamı özsermayelerinin %25\'ini (Geniş yetkili kurumlarda %50\'sini) aşamaz.',
    trap: 'Finansal kuruluşlara, borsalara ve MKK\'ya iştirakte sınır yoktur; sınır finans dışı ortaklıklar içindir.'
  },
  {
    id: 'rat_45',
    moduleId: '1012',
    moduleName: 'Takas & Saklama',
    value: '%64.9 / %30.1 / %5.0',
    title: 'Merkezi Kayıt Kuruluşu (MKK) Güncel Ortaklık Yapısı',
    description: 'MKK sermayesi 100 Milyon TL olup fiili ortaklık payları: İstanbul Takas ve Saklama Bankası A.Ş. %64.9, Borsa İstanbul A.Ş. %30.1 ve Türkiye Sermaye Piyasaları Birliği (TSPB) %5.0\'dir.',
    trap: 'MKK\'da çoğunluk hisse Borsa İstanbul\'un değil, %64.9 ile Takasbank\'ındır.'
  },
  {
    id: 'rat_46',
    moduleId: '1012',
    moduleName: 'Takas & Saklama',
    value: '%75 / %50 / %10 / %5',
    title: 'MKK Esas Sözleşmesi Azami Pay Sahipliği Tavanları',
    description: 'MKK esas sözleşmesine göre; Takasbank payı %75\'i, Borsa İstanbul payı %50\'yi, TSPB payı %10\'u ve diğer ortakların her birinin payı %5\'i geçemez.',
    trap: 'Fiili oranlar (%64.9 / %30.1 / %5) ile esas sözleşme tavanları (%75 / %50 / %10 / %5) sınavda birbirinin çeldiricisidir.'
  },
  {
    id: 'rat_47',
    moduleId: '1012',
    moduleName: 'Takas & Saklama',
    value: '2/3 (%66.7)',
    title: 'Temerrüt Mağduriyet Ödemesi Oranı',
    description: 'Temerrüt nedeniyle nakit veya menkul kıymet alacağını valör gününde alamayan hak sahibi üyeye, temerrüt eden üyeden tahsil edilen temerrüt faiz ve cezasının 2/3\'ü mağduriyet ödemesi olarak aktarılır.',
    trap: 'Tahsil edilen cezanın tamamı Takasbank\'a kalmaz; 2/3\'ü alacaklı mağdur üyeye ödenir, 1/3\'ü Takasbank\'ta kalır.'
  },
  {
    id: 'rat_48',
    moduleId: '1012',
    moduleName: 'Takas & Saklama',
    value: '%10 / %50 / %30',
    title: 'Asgari Nakit Türk Lirası Teminat Kompozisyon Oranları',
    description: 'Pay Piyasası işlem teminatında en az %10 Nakit TL; VİOP işlem teminatında en az %50 Nakit TL; VİOP Garanti Fonu katkı payında en az %30 Nakit TL zorunludur. BAP ve BİAŞ Para Piyasası\'nda asgari TL şartı yoktur.',
    trap: 'Tüm piyasalarda nakit TL şartı aynı değildir; VİOP işlem teminatında %50 iken Pay Piyasası\'nda %10\'dur; BAP\'ta ise minimum TL şartı aranmaz.'
  },
  {
    id: 'rat_49',
    moduleId: '1012',
    moduleName: 'Takas & Saklama',
    value: '200K / 700K / 3.575M / 2.875M TL',
    title: 'MKT Piyasalarında Sabit Garanti Fonu Katkı Payları',
    description: 'MKT üyelerinin yatırması gereken maktu asgari Garanti Fonu katkı payları: Pay Piyasası: 200.000 TL, Borçlanma Araçları Piyasası (BAP): 700.000 TL, VİOP: 3.575.000 TL, SWAP Piyasası: 2.875.000 TL, OTC Türev: 500.000 TL, BİAŞ Para Piyasası: 50.000 TL.',
    trap: 'En yüksek sabit katkı payı 3.575.000 TL ile VİOP\'tadır.'
  },
  {
    id: 'rat_50',
    moduleId: '1012',
    moduleName: 'Takas & Saklama',
    value: '%25',
    title: 'Tek Bir İhraççı/Banka Teminat Konsantrasyon Limiti',
    description: 'Tek bir ihraççı veya banka ya da aynı gruba ait kurumların ihraç ettiği menkul kıymetler/garantiler toplamı (Hazine ve kamu bankaları hariç), ilgili piyasada kabul edilen toplam teminatların %25\'ini geçemez.',
    trap: 'Hazine ihraçları ve kamu bankası menkul kıymetleri %25 konsantrasyon sınırından muaftır.'
  },
  {
    id: 'rat_51',
    moduleId: '1012',
    moduleName: 'Takas & Saklama',
    value: '%3 / %25 / %100',
    title: 'VİOP Pozisyon Limitleri Eşikleri',
    description: 'Pay vadeli ve opsiyon sözleşmelerinde: Sicil bazında fiili dolaşımın azami %3\'ü; Piyasa bazında fiili dolaşımın azami %25\'i (vade sonlarında %35\'e çıkarılabilir); ELÜS sözleşmelerinde lisanslı depo kapasitesinin %100\'ü.',
    trap: 'Sicil limiti %3, piyasa limiti %25\'tir; birbirine karıştırmayın.'
  },
  {
    id: 'rat_52',
    moduleId: '1012',
    moduleName: 'Takas & Saklama',
    value: '%200',
    title: 'BISTECH Risk/Limit Aşımında Emir İptal Eşiği',
    description: 'Üyenin toplam teminat gereksiniminin risk limitine oranı %200\'ü aşarsa, teminat bakiyesine bakılmaksızın üyenin yeni emir iletimi derhal durdurulur ve BISTECH\'teki tüm pasif emirleri otomatik olarak iptal edilir.',
    trap: 'Emir iptal eşiği %100 veya %150 değil, tam %200\'dür.'
  },
  {
    id: 'rat_53',
    moduleId: '1012',
    moduleName: 'Takas & Saklama',
    value: '%80',
    title: 'VİOP Gün İçi Sürdürme Seviyesi Oranı',
    description: 'VİOP\'ta gün sonlarında sürdürme teminatı uygulanmaz; ancak seans içinde gün içi sürdürme seviyesi oranı %80 olarak uygulanır. Hesabın teminatı %80 altına inerse pasif emirleri iptal edilir.',
    trap: 'VİOP\'ta gün sonunda sürdürme teminatı yoktur (gün sonu daima %100 başlangıç teminatına tamamlanır); %80 seviyesi sadece seans içi gün içi kontroller içindir.'
  },
  {
    id: 'rat_54',
    moduleId: '1012',
    moduleName: 'Takas & Saklama',
    value: '5.000 TL',
    title: 'Takasbank Nezdinde Nemalandırma Alt Sınırı',
    description: 'Takasbank nezdinde saat 15:40 itibarıyla işlem ve garanti fonu nakit TL bakiyeleri nemalandırılır. Bakiyesi 5.000 TL\'nin altında kalan hesaplara nema ödenmez.',
    trap: '15:40\'tan sonra yatırılan nakitler o gün için nemalanmaz; ayrıca 5.000 TL altı bakiyeler nema kapsamı dışındadır.'
  },
  {
    id: 'rat_isin',
    moduleId: '1012',
    moduleName: 'Takas & Saklama',
    value: '12 Hane',
    title: 'ISIN Kodu — Menkul Kıymetin Kimliği',
    description: 'ISIN (International Securities Identification Number), menkul kıymetleri tanımlayan 12 haneli alfanümerik koddur. 1-2. haneler ülke kodunu (TR), 3. hane menkul kıymet türünü, 4-9. haneler vade/itfa tarihini, 10. hane para birimi veya ödeme niteliğini, 11. hane aynı vadedeki kıymetleri ayıran sıra numarasını, 12. hane ise kontrol hanesini gösterir.',
    trap: 'Sınavda en kritik bölüm 3. hanedir: DİBS örneklerinde T = Devlet Tahvili, B = Hazine Bonosu; finansman bonolarında piyasa örneklerinde F harfi görülebilir. 12. hane ise kontrol hanesidir.'
  }
];

const COMPARISONS: ComparisonItem[] = [
  {
    id: 'comp_1',
    moduleId: '1005',
    moduleName: 'Yatırım Kur.',
    conceptA: {
      title: 'Uygunluk Testi (Suitability)',
      desc: 'Genel Alım-Satım Aracılığı hizmetinde uygulanır.',
      keyPoint: 'Yatırımcının yalnızca BİLGİ VE TECRÜBESİNİ ölçer.'
    },
    conceptB: {
      title: 'Yerindelik Testi (Appropriateness)',
      desc: 'Portföy Yöneticiliği ve Yatırım Danışmanlığında zorunludur.',
      keyPoint: 'Bilgi + MALİ GÜÇ + YATIRIM AMACINI ölçer.'
    },
    differenceRule: 'Yerindelik testinde müşteri mali gücünü açıklamazsa kuruma portföy yöneticiliği veya danışmanlık hizmeti KESİNLİKLE VERİLEMEZ. Uygunluk testinde ise yazılı risk uyarısı verilerek işlem yapılabilir.'
  },
  {
    id: 'comp_2',
    moduleId: '1012',
    moduleName: 'Takas & Saklama',
    conceptA: {
      title: 'Merkezi Kayıt Kuruluşu (MKK)',
      desc: 'Türkiye\'nin Merkezi Saklama Kuruluşudur.',
      keyPoint: 'Kaydileştirme yapar, mülkiyet hak sahipliği sicilini tutar, e-YATIRIMCI ve e-GKS sistemlerini işletir.'
    },
    conceptB: {
      title: 'Takasbank (İstanbul Takas ve Saklama Bankası)',
      desc: 'Türkiye\'nin Merkezi Takas Kuruluşudur.',
      keyPoint: 'Merkezi Karşı Taraf (CCP) sıfatıyla nakit ve menkul kıymet takasını sonuçlandırır, temerrüt şelalesini yönetir.'
    },
    differenceRule: 'MKK saklama ve mülkiyet sicilidir; Takasbank ise organize takas ve merkezi karşı taraf (garantör) bankasıdır.'
  },
  {
    id: 'comp_3',
    moduleId: '1003',
    moduleName: 'SP Araçları',
    conceptA: {
      title: 'Paya Dönüştürülebilir Tahvil (PDT)',
      desc: 'Borçlanma aracı sahibine hisse senedi alma hakkı verir.',
      keyPoint: 'Vadesinde tahvili ihraç eden şirketin KENDİ PAYLARINA dönüşür.'
    },
    conceptB: {
      title: 'Değiştirilebilir Tahvil (DET)',
      desc: 'Borçlanma aracı sahibine hisse senedi alma hakkı verir.',
      keyPoint: 'İhraççı dışındaki BAŞKA BİR ŞİRKETİN (örneğin iştirakinin) paylarına dönüşür.'
    },
    differenceRule: 'PDT = Kendi payı; DET = Başka şirketin payı.'
  },
  {
    id: 'comp_4',
    moduleId: '1003',
    moduleName: 'SP Araçları',
    conceptA: {
      title: 'Vadeli İşlem Sözleşmesi (Futures - İki Taraflı Zorunlu Sözleşme)',
      desc: 'İleri bir tarihte, bugünden sabitlenen fiyattan dayanak varlığı alma veya satma ZORUNLULUĞUDUR. Tıpkı çiftçi ile fırıncının 3 ay sonra 1 ton buğdayı kilosu 10 TL\'den alıp satmak üzere bağlayıcı sözleşme imzalaması gibidir.',
      keyPoint: 'Her iki taraf da kanunen YÜKÜMLÜDÜR (Piyasa düşse de yükselse de vazgeçemez). İki taraf da Takasbank\'a teminat yatırır, günlük fiyat değişimlerinde zarar büyürse Margin Call uygulanır, zarar teorik olarak sınırsızdır.'
    },
    conceptB: {
      title: 'Opsiyon Sözleşmesi (Options) & Varant (Ev Kaporası / Sigorta Mantığı)',
      desc: 'Alıcıya ileri tarihte belirli fiyattan alma hakkı (Call Option) veya satma hakkı (Put Option) verir. Tıpkı beğendiğiniz 5 Milyon TL\'lik bir ev için ev sahibine 100.000 TL \'kapora (prim)\' ödeyip 1 ay bu fiyattan alma hakkı satın almak gibidir.',
      keyPoint: 'ALICI İÇİN HAKTIR (Ev değer kaybederse evi almaktan vazgeçer; zararı sadece baştaki 100.000 TL kapora/primle sınırlıdır, teminat yatırmaz). SATICI İÇİN YÜKÜMLÜLÜKTÜR (Primi peşin alır ama alıcı isterse evi o fiyattan teslim etmek zorundadır, teminat yatırır). Varant ise menkul kıymetleştirilmiş opsiyondur; sadece prim ödenir, margin call yoktur.'
    },
    differenceRule: 'Futures = İki taraf da zorunlu yükümlüdür (Çift taraflı bağlayıcıdır, vazgeçilemez, iki taraf da teminat yatırır). Opsiyon/Varant = Alıcı hak sahibidir (İsterse hakkından vazgeçer, zararı sadece ödediği primdir); Satıcı ise primi peşin alıp tüm riski üstlenen taraftır (Teminat yatırır).'
  },
  {
    id: 'comp_5',
    moduleId: '1001',
    moduleName: 'Mevzuat',
    conceptA: {
      title: 'İçsel Bilgiye Dayalı Ticaret (m.106)',
      desc: 'Henüz kamuya açıklanmamış gizli bilgiye dayanarak menfaat sağlama suçu.',
      keyPoint: 'Cezası 3-5 yıl hapis. Kanunda ETKİN PİŞMANLIK HÜKMÜ YOKTUR.'
    },
    conceptB: {
      title: 'Piyasa Dolandırıcılığı / Manipülasyon (m.107)',
      desc: 'Yapay piyasa ve fiyat hareketleri oluşturma suçu.',
      keyPoint: 'Cezası 3-5 yıl hapis. İşlem bazlı olanda inceleme öncesi 2 KATINI ödeyerek ETKİN PİŞMANLIK MÜMKÜNDÜR.'
    },
    differenceRule: 'İçsel bilgide etkin pişmanlık yoktur; işlem bazlı manipülasyonda Hazineye 2 katı ödeyerek etkin pişmanlıktan yararlanılabilir.'
  },
  {
    id: 'comp_6',
    moduleId: '1003',
    moduleName: 'SP Araçları',
    conceptA: {
      title: 'Temiz Fiyat (Clean Price - Borsa Ekran Fiyatı)',
      desc: 'Tahvilin son kupon ödeme tarihinden bugüne kadar geçen sürede birikmiş/işlemiş faizi HARİÇ piyasa fiyatıdır. Borsa İstanbul Borçlanma Araçları Piyasası ekranlarında ve finans bültenlerinde kote edilen fiyattır.',
      keyPoint: 'Kote Edilen Fiyattır. Kupon faizinin gün geçtikçe birikmesinden kaynaklanan yapay şişmeyi arındırır, piyasa faizlerindeki saf hareketleri gösterir.'
    },
    conceptB: {
      title: 'Kirli Fiyat (Dirty Price - Takasta Fiilen Ödenen Fiyat)',
      desc: 'Temiz fiyata, son kupon gününden takas gününe kadar hak edilmiş \'İşlemiş Faizin\' eklenmesiyle bulunan toplam fiyattır. Alıcının satıcıya takas günü cebinden çıkarıp FİİLEN ÖDEDİĞİ NAKİT BEDELDİR.',
      keyPoint: 'Fiili Ödeme Tutarıdır. Formül: Kirli Fiyat = Temiz Fiyat + İşlemiş Faiz. (İşlemiş Faiz = Nominal × Kupon Oranı × Geçen Gün / 365).'
    },
    differenceRule: 'Borsa ekranında işlem gören ve kote edilen fiyat TEMİZ FİYAT\'tır; ancak alıcının satıcıya takas gününde fiilen ödediği para KİRLİ FİYAT\'tır. Kupon ödemesinin yapıldığı gün işlemiş faiz sıfırlandığı için Temiz Fiyat = Kirli Fiyat olur; kupon gününe yaklaştıkça Kirli Fiyat yükselir.'
  },
  {
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
      desc: 'Alacaklar bilançodan tamamen çıkarılarak Fon\'a (VFF) devredilir.',
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
      keyPoint: 'Bedeli tamamen ödenmedikçe hamiline pay çıkarılamaz; MKK\'ya bildirilmeden devredilemez.'
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
      keyPoint: 'Yükselişten kâr sağlar. Başlangıç özkaynağı %35\'tir.'
    },
    conceptB: {
      title: 'Açığa Satış (Kısa / Short Pozisyon)',
      desc: 'Hisse senedinin DÜŞECEĞİ beklentisiyle sahip olunmayan hisseyi ödünç alıp satmaktır.',
      keyPoint: 'Düşüşten kâr sağlar. Başlangıç özkaynağı %50\'dir.'
    },
    differenceRule: 'Kredili alım nakit borçlanarak yükselişe oynar (%35 özkaynak); açığa satış hisse ödünç alarak düşüşe oynar (%50 özkaynak).'
  },
{
    id: 'comp_11',
    moduleId: '1001',
    moduleName: 'Mevzuat',
    conceptA: {
      title: 'İzinsiz Sermaye Piyasası Faaliyeti (SPKn m.109/2)',
      desc: 'SPK\'dan izin almaksızın yatırım hizmet ve faaliyeti yürütmek.',
      keyPoint: '2 yıldan 5 yıla kadar hapis ve 5.000 - 10.000 gün adli para cezası.'
    },
    conceptB: {
      title: 'İzinsiz Kripto Varlık Hizmet Sağlayıcılığı (SPKn m.109/A)',
      desc: 'SPK\'dan izin almaksızın kripto platformu veya saklama faaliyeti yürütmek.',
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
      keyPoint: 'Fon toplam değerinin en fazla %10\'u; tek bankada en fazla %3\'ü.'
    },
    conceptB: {
      title: 'Katılım Yatırım Fonu Katılma Hesabı Sınırları',
      desc: 'Fon portföyünün katılım bankası katılma hesaplarında değerlendirilmesi.',
      keyPoint: 'Fon toplam değerinin en fazla %25\'i; tek katılım bankasında en fazla %10\'u.'
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
    differenceRule: 'Faaliyetlerin geçici durdurulması bir Birlik disiplin cezası DEĞİL, SPK\'nın Kanun m. 96 idari tedbiridir.'
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
      keyPoint: 'Genel saklama yetkili yatırım kuruluşu teminat yöneticisi olur; temerrütte mahkeme veya ihbar şartı olmaksızın teminatları re\'sen satıp paylaştırır.'
    },
    differenceRule: 'SPKn m.47 doğrudan iki taraf arasındaki menkul kıymet teminatıdır; SPKn m.31/B ise genel saklama yetkili bağımsız teminat yöneticisinin atandığı kamusal ihraç teminat mekanizmasıdır.'
  },
{
    id: 'comp_15',
    moduleId: '1003',
    moduleName: 'SP Araçları',
    conceptA: {
      title: 'Çoklu Fiyat İhalesi (Amerikan Tipi - DİBS)',
      desc: 'Hazine ihalelerinde en yüksek fiyat teklifinden başlayarak borçlanma tutarına kadar teklifler kabul edilir.',
      keyPoint: 'Her kazanan katılımcı BİZZAT KENDİ TEKLİF ETTİĞİ FİYATTAN (farklı fiyatlardan) senedi satın alır.'
    },
    conceptB: {
      title: 'Tek Fiyat İhalesi (Hollanda Tipi - DİBS)',
      desc: 'Yine en yüksek fiyattan başlanarak hedeflenen tutar karşılanana kadar teklifler sıralanır.',
      keyPoint: 'İhalede oluşan EN DÜŞÜK KABUL EDİLEN FİYAT (marjinal fiyat), kazanan TÜM KATILIMCILARA TEK FİYAT olarak uygulanır.'
    },
    differenceRule: 'Çoklu fiyatta herkes kendi verdiği fiyattan alır (fiyatlar farklılaşır); tek fiyatta ise kazanan herkes kesme fiyatından (tek fiyattan) DİBS alır.'
  },
  {
    id: 'comp_16',
    moduleId: '1003',
    moduleName: 'SP Araçları',
    conceptA: {
      title: 'VİOP Nakdi Uzlaşma (Cash Settlement)',
      desc: 'Vade sonunda taraflar arasında herhangi bir fiziksel mal, hisse veya emtia el değiştirmez.',
      keyPoint: 'Sözleşme fiyatı ile vade sonu uzlaşma fiyatı arasındaki fark hesaplanarak kâr/zarar nakit olarak hesaba aktarılır (Örn: BIST 30 Endeks VİS, Altın VİS).'
    },
    conceptB: {
      title: 'VİOP Fiziki Teslimat (Physical Delivery)',
      desc: 'Vade sonunda sözleşmeye konu dayanak varlık fiilen alıcıya teslim edilir, bedeli satıcıya ödenir.',
      keyPoint: 'Sözleşme büyüklüğü kadar hisse senedi (Pay VİS), DİBS veya ELÜS Takasbank/MKK üzerinden takas edilir (Örn: Pay VİS, DİBS VİS, DolarTL VİS, ELÜS VİS).'
    },
    differenceRule: 'BIST 30 Endeks ve Altın vadeli sözleşmeleri nakdi uzlaşmalıdır; Pay Vadeli ve Dolar/TL vadeli sözleşmeleri ise fiziki teslimatlıdır.'
  },
  {
    id: 'comp_17',
    moduleId: '1003',
    moduleName: 'SP Araçları',
    conceptA: {
      title: 'Hazine Bonosu & Devlet Tahvili (DİBS)',
      desc: 'Hazine ve Maliye Bakanlığı tarafından bütçe finansmanı amacıyla ihraç edilen faizli borçlanma senetleridir.',
      keyPoint: 'Kurumsal ve bireysel tüm yatırımcılara açıktır; ihale, doğrudan satış ve halka arz yöntemleriyle satılır.'
    },
    conceptB: {
      title: 'Altın Tahvili & Altına Dayalı Kira Sertifikası',
      desc: 'Hazinece yastık altındaki altınları ekonomiye kazandırmak amacıyla ihraç edilen 1000/1000 saflıkta altına dayalı senetlerdir.',
      keyPoint: 'YALNIZCA YURT İÇİ GERÇEK KİŞİLERE (bireysel yatırımcılara) ihraç edilir; kurumsal yatırımcılar satın alamaz.'
    },
    differenceRule: 'Standart DİBS ihalelerine kurumsal yatırımcılar katılırken, Altın Tahvili ve Altına Dayalı Kira Sertifikasını yalnızca bireysel (gerçek kişi) yatırımcılar alabilir.'
  },
  {
    id: 'comp_18',
    moduleId: '1003',
    moduleName: 'SP Araçları',
    conceptA: {
      title: 'Halka Arzda Bakiye Yüklenimi (Underwriting)',
      desc: 'Yatırım kuruluşunun satılamayan payları satın alma taahhüdüdür.',
      keyPoint: 'Satış süresi sonunda satılamayan pay kalırsa, yetkili aracı kurum bedelini tam ödeyerek payları KENDİ PORTFÖYÜNE ALMAK ZORUNDADIR.'
    },
    conceptB: {
      title: 'En İyi Gayret Aracılığı (Best Efforts)',
      desc: 'Yatırım kuruluşunun payları satmak için azami çabayı gösterme taahhüdüdür.',
      keyPoint: 'Satış süresi sonunda satılamayan paylar kalırsa aracı kurumun satın alma yükümlülüğü YOKTUR; kalan paylar ihraççı şirkete iade edilir veya iptal edilir.'
    },
    differenceRule: 'Yüklenimde risk aracı kurumdadır (satılamayanı kendi alır); En İyi Gayret aracılığında ise satılamama riski tamamen ihraççı şirkettedir.'
  },
  {
    id: 'comp_19',
    moduleId: '1005',
    moduleName: 'Yatırım Kur.',
    conceptA: {
      title: 'Uygunluk Testi (Appropriateness)',
      desc: 'Alım Satıma Aracılık ve Halka Arza Aracılıkta zorunludur.',
      keyPoint: 'Yatırımcının yalnızca BİLGİ VE TECRÜBESİNİ ölçer; mali durumu sorulmaz. Müşteri uygun olmayan ürünü ısrarla talep ederse yazılı uyarıyla kurum hizmet vermekte serbesttir.'
    },
    conceptB: {
      title: 'Yerindelik Testi (Suitability)',
      desc: 'Bireysel Portföy Yöneticiliği ve Yatırım Danışmanlığında zorunludur.',
      keyPoint: 'Yatırımcının BİLGİ + MALİ DURUM + YATIRIM AMACINI birlikte ölçer. Test sonucuna uygun olmayan ürün veya hizmet MÜŞTERİ İSTESE DAHİ KESİNLİKLE VERİLEMEZ.'
    },
    differenceRule: 'Uygunlukta müşterinin ısrarıyla işlem yapılabilir (özgür irade); Yerindelik testinde ise müşteri istese dahi uygunsuz portföy yönetimi veya yatırım danışmanlığı sunulamaz (katı yasak).'
  },
  {
    id: 'comp_20',
    moduleId: '1005',
    moduleName: 'Yatırım Kur.',
    conceptA: {
      title: 'Aracı Kurum Şubesi',
      desc: 'Aracı kurumun yetkili olduğu tüm faaliyetleri gerçekleştirebilen merkez dışı örgüttür.',
      keyPoint: 'Müşterilerden nakit ve sermaye piyasası aracı tahsilat ve tediye işlemleri YAPABİLİR; lisanslı bir şube müdürü atanması zorunludur.'
    },
    conceptB: {
      title: 'Aracı Kurum İrtibat Bürosu',
      desc: 'Yalnızca aracı kurumu ve hizmetlerini tanıtmak amacıyla kurulur.',
      keyPoint: 'Müşteri emirlerini aracı kuruma iletebilir; ancak NAKİT VE MENKUL KIYMET TAHSİLAT VE TEDİYESİ YAPMASI KANUNEN KESİNLİKLE YASAKTIR. En az 2 yıllık ön lisans mezunu bir büro sorumlusu görev yapar.'
    },
    differenceRule: 'Şube nakit para ve kıymet tahsilatı yapabilirken; irtibat bürosunun nakit veya menkul kıymet tahsil ve tediye işlemi yapması kesinlikle yasaktır.'
  },
  {
    id: 'comp_21',
    moduleId: '1005',
    moduleName: 'Yatırım Kur.',
    conceptA: {
      title: 'Sınırlı Saklama Hizmeti',
      desc: 'Yatırım kuruluşunun yetkili olduğu faaliyetler dolayısıyla kendi müşterilerine sunduğu saklamadır.',
      keyPoint: 'İşlem/portföy aracılığı, portföy yöneticiliği veya halka arza aracılık kapsamındaki kendi müşterilerinin varlıklarını saklar. Emir iletimine aracılıkta saklama yetkisi yoktur.'
    },
    conceptB: {
      title: 'Genel Saklama Hizmeti',
      desc: 'Yetkili olunan faaliyetlerden bağımsız olarak sunulan saklamadır.',
      keyPoint: 'BAŞKA YATIRIM KURULUŞLARININ MÜŞTERİLERİNE ve bağımsız portföylere saklama hizmeti sunulmasını sağlar. Bankalar ve geniş yetkili aracı kurumlarca yürütülür.'
    },
    differenceRule: 'Sınırlı saklama sadece kendi müşterisinin varlığına hizmet verirken, Genel saklama diğer aracı kurumların müşterilerine de bağımsız saklama hizmeti verir.'
  },
  {
    id: 'comp_22',
    moduleId: '1005',
    moduleName: 'Yatırım Kur.',
    conceptA: {
      title: 'Yatırım Danışmanlığı Faaliyeti',
      desc: 'SPK iznine tabi ana yatırım hizmetidir.',
      keyPoint: 'Belli bir kişiye veya risk/getiri tercihi benzer bir gruba yönelik yönlendirici yorum ve tavsiye verilir. Çerçeve sözleşme ve Yerindelik Testi ZORUNLUDUR.'
    },
    conceptB: {
      title: 'Genel Yatırım Tavsiyesi',
      desc: 'Kurula bildirimle sunulabilen bir yan hizmettir.',
      keyPoint: 'Kişisel özellikler dikkate alınmaksızın kamuya veya dağıtım kanallarına sunulan genel araştırma ve bültenlerdir. Yasal standart uyarı notunun bulunması zorunludur.'
    },
    differenceRule: 'Yatırım danışmanlığı kişiye özeldir ve yerindelik testi gerektirir; genel yatırım tavsiyesi ise geniş kitleye yöneliktir ve standart uyarı metniyle sunulur.'
  },
  {
    id: 'comp_23',
    moduleId: '1005',
    moduleName: 'Yatırım Kur.',
    conceptA: {
      title: 'Paya Dayalı Kitle Fonlaması',
      desc: 'Ortaklık payı karşılığında platform aracılığıyla halktan sermaye toplanmasıdır.',
      keyPoint: 'Girişimcinin fonlama sonrası 90 gün içinde anonim şirket kurması zorunludur. Fonlanan şirketin bilgileri 5 yıl boyunca kampanya sayfasında yayımlanır.'
    },
    conceptB: {
      title: 'Borçlanmaya Dayalı Kitle Fonlaması',
      desc: 'Borçlanma aracı karşılığında platform aracılığıyla halktan fon toplanmasıdır.',
      keyPoint: 'Faiz oranı en yakın iki DİBS faizinin %50 fazlasını aşamaz, azami vade 5 yıldır. Tek projeye bireysel yatırım sınırı 200.000 TL\'dir ve geri ödeme tek seferde yapılamaz.'
    },
    differenceRule: 'Paya dayalıda yatırımcı şirkete ortak olur; borçlanmaya dayalıda ise faizli alacaklı olur (DİBS+%50 tavanı ve tek projeye 200 bin TL sınırı uygulanır).'
  },
  {
    id: 'comp_24',
    moduleId: '1005',
    moduleName: 'Yatırım Kur.',
    conceptA: {
      title: 'NFC ile Çip Doğrulama (Temassız Kimlik)',
      desc: 'Uzaktan kimlik tespitinde yakın alan iletişimiyle çipin kriptografik okunmasıdır.',
      keyPoint: 'Kimlik belgesi temassız yongası üzerindeki biyometrik fotoğraf ve veriler güvenli anahtarla doğrulanır; tam ve güvenli eşleşme sağlar.'
    },
    conceptB: {
      title: 'Görsel Güvenlik Unsurları Doğrulaması',
      desc: 'NFC bulunmayan durumlarda uygulanan alternatif doğrulama yöntemidir.',
      keyPoint: 'Beyaz ışık altında en az DÖRT (4) adet görsel güvenlik unsuru doğrulanır ve İLAVE OLARAK ilk finansal hareketin başka bir finansal kuruluş üzerinden yapılması zorunludur.'
    },
    differenceRule: 'NFC çip okuma yapılamadığında en az 4 görsel güvenlik ögesi kontrol edilir ve ilk para transferinin müşterinin başka bir banka hesabından gelmesi şart koşulur.'
  },
  {
    id: 'comp_25',
    moduleId: '1012',
    moduleName: 'Takas & Saklama',
    conceptA: {
      title: 'Açık Teklif Yöntemi (Open Offer)',
      desc: 'İşlemin eşleştiği anda Takasbank\'ın otomatik olarak tarafların arasına girmesidir.',
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
      keyPoint: 'İşlemci kuruluşla birlikte Takasbank\'a karşı müşterek borçlu ve müteselsil kefil sorumluluğu taşır.'
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
      desc: 'Pay Piyasası ve VİOP\'ta kullanılan portföy bazlı parametrik risk yönetimi algoritmasıdır.',
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
      desc: 'Türkiye\'deki yerli yatırımcıların hisse senetlerinin doğrudan kendi ad ve TC/Vergi kimlik numaralarıyla açılan hesaplarda izlenmesidir.',
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
      keyPoint: 'Fon malvarlığını PYŞ\'den korur; harcamaların, birim pay değerinin ve kaldıraç limitlerinin gözetimini yapar.'
    },
    differenceRule: 'Genel saklama müşteri varlığını korur; Portföy saklama ise kolektif fon malvarlığını PYŞ\'nin usulsüz işlemlerine karşı gözetler ve denetler.'
  },
  {
    id: 'comp_33',
    moduleId: '1012',
    moduleName: 'Takas & Saklama',
    conceptA: {
      title: 'Repo (Ters Repo Yapan Tarafın Karşıtı)',
      desc: 'Menkul kıymetin nakit karşılığında geçici olarak satılması ve vade sonunda geri alınması işlemidir.',
      keyPoint: 'Repo yapan taraf menkul kıymeti verir, nakdi alır; vade sonunda nakdi faiziyle ödeyerek menkul kıymeti geri alır.'
    },
    conceptB: {
      title: 'Ters Repo',
      desc: 'Nakit verilerek karşılığında menkul kıymetin teminat olarak alınması ve vade sonunda iade edilmesi işlemidir.',
      keyPoint: 'Ters repo yapan taraf nakdi verir, menkul kıymeti alır; vade sonunda menkul kıymeti iade ederek nakdi faiziyle geri alır.'
    },
    differenceRule: 'Repo = nakit alan ve menkul kıymeti geçici olarak satan taraf; ters repo = nakit veren ve menkul kıymeti teminat olarak alan taraf. Kısa ezber: Repo nakit alır, ters repo nakit verir.'  },
  {
    id: 'comp_28',
    moduleId: '1001',
    moduleName: 'Mevzuat',
    conceptA: {
      title: 'Aktif Fiille Örtülü Kazanç Aktarımı (SPKn m.110/1-b)',
      desc: 'İlişkili tarafla emsaline bariz aykırı fiyatla gayrimenkul veya malvarlığı devrederek kârı eksiltmek.',
      keyPoint: '3 yıldan 5 yıla kadar hapis ve 5.000 günden 10.000 güne kadar adli para cezası gerektiren ADLİ SUÇTUR.'
    },
    conceptB: {
      title: 'İhmali/Pasif Fiille Örtülü Kazanç Aktarımı (SPKn m.103/6)',
      desc: 'Kârlı bir patent, lisans veya ticari fırsatı bilerek değerlendirmeyip malvarlığı artışına engel olmak.',
      keyPoint: 'Adli bir suç oluşturmaz; kabahat niteliğinde olup İDARİ PARA CEZASI yaptırımına tabidir.'
    },
    differenceRule: 'Aktif malvarlığı eksiltme adli suç (hapis) iken; ticari fırsatı şirkete kazandırmayı ihmal etme adli suç değil, idari para cezasıdır.'
  },
  {
    id: 'comp_29',
    moduleId: '1001',
    moduleName: 'Mevzuat',
    conceptA: {
      title: 'İçsel Bilginin Ertelenmesi (II-15.1 m.6)',
      desc: 'İhraççının meşru çıkarlarının zarar görmemesi için KAP açıklamasını kendi sorumluluğunda ertelemesi.',
      keyPoint: 'Yatırımcıların yanıltılmaması ve gizliliğin korunabilmesi ön koşuldur; sebepler kalkınca derhal açıklanır.'
    },
    conceptB: {
      title: 'Söylenti Halinde Doğrulama Yükümlülüğü (II-15.1 m.9)',
      desc: 'Erteleme devam ederken basında veya internette hisse fiyatını etkileyecek haber çıkması hali.',
      keyPoint: 'SPK veya Borsa uyarısı beklenmeksizin DERHAL VE RE\'SEN KAP\'ta özel durum açıklaması yapılması ZORUNLUDUR.'
    },
    differenceRule: 'Erteleme kararı olsa dahi piyasada söylenti veya haber çıkarsa gizlilik kaybolur ve SPK/Borsa talebi beklenmeden derhal açıklama yapılır.'
  },
  {
    id: 'comp_30',
    moduleId: '1001',
    moduleName: 'Mevzuat',
    conceptA: {
      title: 'Yaygın Olmayan İlişkili Taraf Varlık Alımı (II-17.1 m.9)',
      desc: 'İlişkili taraftan tek seferlik veya yaygın olmayan gayrimenkul, tesis veya hisse devralınması.',
      keyPoint: 'İşlem tutarı aktif toplamı veya hasılatın %5\'ini aşarsa LİSANSLI DEĞERLEME RAPORU ve Bağımsız YK Onayı şarttır.'
    },
    conceptB: {
      title: 'Yaygın ve Süreklilik Arz Eden İşlemler (II-17.1 m.10)',
      desc: 'İlişkili tarafla ticari faaliyet gereği devamlı yapılan hammadde veya mamul alış-satışları.',
      keyPoint: 'Bir dönemdeki tutar hasılat veya maliyetin %10\'unu aşarsa Yönetim Kurulu Raporu hazırlanıp KAP\'ta açıklanır.'
    },
    differenceRule: 'Tekil varlık alımında değerleme eşiği %5\'tir; yaygın ve sürekli ticari işlemlerde yönetim kurulu raporu eşiği %10\'dur.'
  },
  {
    id: 'comp_31',
    moduleId: '1005',
    moduleName: 'Yatırım Kur.',
    conceptA: {
      title: 'Şube Yetkileri (III-39.1 m.43)',
      desc: 'Yatırım kuruluşunun merkeze bağlı bağımsız hizmet ve işlem birimidir.',
      keyPoint: 'Müşteri emri alabilir, hesap açabilir, sözleşme akdedebilir, nakit ve menkul kıymet teslim alabilir.'
    },
    conceptB: {
      title: 'İrtibat Bürosu Kesin Yasakları (III-39.1 m.44)',
      desc: 'Yalnızca yatırım kuruluşunun ve sunduğu hizmetlerin tanıtım ve pazarlamasını yapar.',
      keyPoint: 'Müşteri emri alamaz, sözleşme imzalayamaz, hesap açamaz, hiçbir suretle nakit veya kıymet kabul edemez.'
    },
    differenceRule: 'Şube tam yetkili işlem birimidir; İrtibat Bürosu ise sadece tanıtım yapabilir, asla emir ve para kabul edemez.'
  },
  {
    id: 'comp_32',
    moduleId: '1005',
    moduleName: 'Yatırım Kur.',
    conceptA: {
      title: 'Dar Yetkili Aracı Kurum (Asgari 45M TL)',
      desc: 'Sermaye piyasasında en sınırlı faaliyet iznine sahip aracı kurum kategorisidir.',
      keyPoint: 'Yalnızca emir iletimine aracılık ve en iyi gayret halka arza yetkilidir; KENDİ NAMINA İŞLEM YAPAMAZ, kredi veremez.'
    },
    conceptB: {
      title: 'Kısmi ve Geniş Yetkili Aracı Kurum (190M / 380M TL)',
      desc: 'Kendi nam ve hesabına işlem (portföy aracılığı) yapabilen yetkili kategorilerdir.',
      keyPoint: 'İşlem aracılığı, portföy aracılığı, kredili alım, açığa satış, genel saklama ve türev araç işlemlerine yetkilidir.'
    },
    differenceRule: 'Dar yetkili kurumlar sadece müşteri emirlerini iletir, kendi portföyüne alım-satım yapamaz; Kısmi ve Geniş yetkililer portföy aracılığı yapabilir.'
  },
  {
    id: 'comp_33',
    moduleId: '1012',
    moduleName: 'Takas & Saklama',
    conceptA: {
      title: 'Doğrudan Takas Üyesi (MKT m.9)',
      desc: 'Takasbank MKT sistemine doğrudan bağlanan takas üyesidir.',
      keyPoint: 'Yalnızca KENDİ PORTFÖYÜ ve KENDİ MÜŞTERİLERİ ad ve hesabına gerçekleştirilen işlemlerin takasını yapar.'
    },
    conceptB: {
      title: 'Genel Takas Üyesi (MKT m.10)',
      desc: 'Genişletilmiş takas yetkisine ve yüksek sermaye taahhüdüne sahip MKT üyesidir.',
      keyPoint: 'Kendi ve müşterilerinin yanı sıra, TAKAS ÜYESİ OLMAYAN DİĞER YATIRIM KURULUŞLARININ işlemlerini de takas eder.'
    },
    differenceRule: 'Doğrudan üye sadece kendi ve müşterisinin takasını yapar; Genel takas üyesi ise üye olmayan üçüncü kuruluşların takasını da üstlenir.'
  },
  {
    id: 'comp_34',
    moduleId: '1003',
    moduleName: 'SP Araçları',
    conceptA: {
      title: 'Halka Açık Ortaklıkta Sermaye Artırımı (Halka Arz & Tahsisli)',
      desc: 'SPKn ve Pay Tebliği (VII-128.1) hükümleri uygulanır.',
      keyPoint: 'Tahsisli artırımda paylar 1 YIL borsada satılamaz; halka arzda %10+ ortaklar 1 YIL satamaz ve fiyat altı satmama taahhüdü verir.'
    },
    conceptB: {
      title: 'Halka Açık Olmayan A.Ş.\'de Sermaye Artırımı',
      desc: 'TTK m. 456 vd. ve m. 490-493 hükümleri uygulanır.',
      keyPoint: 'Devir serbesttir; ancak bedeli ödenmemiş paylar şirket onayı olmadan devredilemez (TTK m. 491) ve bağlam kuralı geçerlidir.'
    },
    differenceRule: 'Halka açık ortaklıklarda tahsisli paylar MKK nezdinde kilitlenerek 1 yıl borsada satış yasağı uygulanırken; halka kapalı ortaklıklarda kanuni borsa yasağı yoktur, pay devri şirket onayı veya esas sözleşmedeki bağlam hükümleriyle (TTK m. 491-493) sınırlandırılır.'
  },
  {
    id: 'comp_35',
    moduleId: '1003',
    moduleName: 'SP Araçları',
    conceptA: {
      title: 'Garantili Yatırım Fonu (III-52.1 m.25)',
      desc: 'Anapara ve/veya getiri üçüncü bir kuruluş tarafından garanti edilir.',
      keyPoint: 'GARANTİ VEREN KURULUŞ (yetkili banka/finans kurumu) taahhütte bulunur; maliyet fondan karşılanamaz.'
    },
    conceptB: {
      title: 'Koruma Amaçlı Yatırım Fonu (III-52.1 m.25)',
      desc: 'Anaparanın korunması türev ve finansal tekniklerle hedeflenir.',
      keyPoint: 'ÜÇÜNCÜ TARAF GARANTİSİ KESİNLİKLE YOKTUR; anapara korunması EN İYİ GAYRET (best effort) esasına dayanır.'
    },
    differenceRule: 'Garantili fonda garantörün kesin hukuki ve mali garantisi vardır; koruma amaçlı fonda ise portföy yöneticisi en iyi gayretle koruma hedefler, üçüncü taraf garantisi kesinlikle bulunmaz ve fon unvanında garanti kelimesi kullanılamaz.'
  },
  {
    id: 'comp_36',
    moduleId: '1001',
    moduleName: 'Mevzuat',
    conceptA: {
      title: 'Şartlı (Sınırlı Olumlu) Görüş (BDS 705)',
      desc: 'Finansal tablolarda belirli kalemlerde hata/kanıt yetersizliği vardır.',
      keyPoint: 'Aykırılık veya kısıtlama ÖNEMLİDİR ancak tablonun geneline sirayet edecek kadar YAYGIN DEĞİLDİR.'
    },
    conceptB: {
      title: 'Olumsuz Görüş vs Kaçınma (BDS 705)',
      desc: 'Finansal tabloların bütününe yansıyan ağır kusurlar.',
      keyPoint: 'Kanıt var ve yaygın yanlışlık varsa OLUMSUZ GÖRÜŞ; kanıt toplanamıyor ve olası etki yaygınsa GÖRÜŞ BİLDİRMEKTEN KAÇINMA verilir.'
    },
    differenceRule: 'Hata önemli fakat yaygın değilse Şartlı Görüş; hata hem önemli hem yaygınsa Olumsuz Görüş; denetim kanıtı toplanamamış ve olası etki hem önemli hem yaygınsa Görüş Bildirmekten Kaçınma kararı verilir.'
  },
  {
    id: 'comp_37',
    moduleId: '1001',
    moduleName: 'Mevzuat',
    conceptA: {
      title: 'Konsolide Finansal Rapor (TFRS 10)',
      desc: 'Ana ortaklık ve kontrol ettiği bağlı ortaklıkların tek bilançosudur.',
      keyPoint: '%50 üzeri veya fiili yönetim kontrolü olan bağlı ortaklıklar TAM KONSOLİDASYON ile birleştirilir.'
    },
    conceptB: {
      title: 'Solo Finansal Rapor & İştirakler',
      desc: 'Tek başına tüzel kişiliğin bireysel finansal tablosudur.',
      keyPoint: '%20-%50 arası oy hakkı bulunan iştirakler konsolide tablolarda ÖZKAYNAK YÖNTEMİYLE gösterilir.'
    },
    differenceRule: 'Kontrol gücü (>%50) olanlar tam konsolidasyona tabi tutulup azınlık payları özkaynak altında ayrılır; önemli etki (%20-%50) olan iştirakler ise özkaynak yöntemiyle konsolide edilir.'
  },
  {
    id: 'comp_38',
    moduleId: '1003',
    moduleName: 'SP Araçları',
    conceptA: {
      title: 'VİOP Pay Vadeli Sözleşmeleri (Tek Hisse)',
      desc: 'Dayanak varlığı BIST Pay Piyasası hisse senedi olan vadeli sözleşmeler.',
      keyPoint: 'Vade sonunda FİZİKİ UZLAŞMA uygulanır; Takasbank Pay Piyasası T+2 takasında hisse teslim edilir.'
    },
    conceptB: {
      title: 'VİOP Endeks Vadeli Sözleşmeleri (BIST 30)',
      desc: 'Dayanak varlığı hisse senedi sepeti/endeksi olan vadeli sözleşmeler.',
      keyPoint: 'Vade sonunda NAKDİ UZLAŞMA uygulanır; son 30 dakika ve kapanış ortalamasıyla kâr/zarar nakit hesaba yansır.'
    },
    differenceRule: 'Pay vadeli sözleşmelerde fiziki teslimat (hisse senedi transferi T+2) zorunludur; Endeks vadeli sözleşmelerde ise fiziki teslimat imkânsız olduğundan nakdi uzlaşma yapılır.'
  },
  {
    id: 'comp_39',
    moduleId: '1012',
    moduleName: 'Takas & Saklama',
    conceptA: {
      title: 'Açığa Satışta Yukarı Adım Kuralı (Up-Tick)',
      desc: 'Piyasa düşüş yönlüyken panik satışları durdurmak için uygulanan kural.',
      keyPoint: 'Emir son işlem fiyatının ÜZERİNDE girilmek zorundadır (son işlem bir önceki fiyattan yüksekse son fiyattan da girilebilir).'
    },
    conceptB: {
      title: 'Borsa Temerrüt Sırası (Buy-in Pazarı)',
      desc: 'T+2 saat 16:45\'te menkul kıymet borcunu kapatamayan aracı kurumlar için açılır.',
      keyPoint: 'T+3 günü saat 11:00\'de Borsa İstanbul bünyesinde açılarak T+0 valörle re\'sen hisse alımı yapılır.'
    },
    differenceRule: 'Yukarı adım kuralı işlem anında emir fiyatını kısıtlar; Temerrüt sırası ise takas günü teslim edilemeyen hisse açığını T+3 saat 11:00\'de piyasadan re\'sen kapatır.'
  },
  {
    id: 'comp_40',
    moduleId: '1003',
    moduleName: 'SP Araçları',
    conceptA: {
      title: 'Tahvil Temiz Fiyat (Clean Price)',
      desc: 'Son kupon ödeme tarihinden itibaren biriken faizi içermeyen çıplak anapara piyasa fiyatı.',
      keyPoint: 'Borsa İstanbul BAP ekranlarında DAİMA TEMİZ FİYAT kote edilir ve emirler temiz fiyat üzerinden girilir.'
    },
    conceptB: {
      title: 'Tahvil Kirli Fiyat (Dirty Price)',
      desc: 'Temiz fiyata son kupondan takas gününe kadar geçen sürenin birikmiş faizinin eklenmiş hali (Temiz + Birikmiş Faiz).',
      keyPoint: 'Takas gününde alıcının satıcıya FİİLEN ÖDEDİĞİ nakit tutar daima KİRLİ FİYATTIR.'
    },
    differenceRule: 'Borsa ekranında görünen fiyat Temiz Fiyat, takasta cepten çıkan para ise Kirli Fiyattır (Kirli = Temiz + Dönemsel Kupon × t/T). Kupon ödeme gününde birikmiş faiz sıfırlandığından ikisi birbirine eşitlenir.'
  },
  {
    id: 'comp_41',
    moduleId: '1003',
    moduleName: 'SP Araçları',
    conceptA: {
      title: 'Eşzamanlı Bedelli + Bedelsiz Artırım Referans Fiyatı',
      desc: 'Hem nakit girişi (bedelli) hem iç kaynak aktarımı (bedelsiz) aynı anda yapıldığında oluşan açılış fiyatı.',
      keyPoint: 'Formül: P_yeni = [P_eski + (B × R_fiyat)] / (1 + B + BD). Şirkete sadece bedelli kısmından nakit girer.'
    },
    conceptB: {
      title: 'Rüçhan Hakkı Kupon Pazarı Teorik Değeri',
      desc: 'Eski pay sahibinin yeni pay alma hakkını (kuponunu) borsada satmak istemesi halinde oluşan referans değer.',
      keyPoint: 'Formül: R_kupon = P_eski - P_yeni. Kullanılmayan rüçhan payları Birincil Piyasa\'da 2 iş günü satılır.'
    },
    differenceRule: 'Yeni referans fiyat hesaplanırken paydaya hem bedelli (B) hem bedelsiz (BD) oranı eklenir; rüçhan kupon değeri ise doğrudan eski fiyat ile yeni fiyat arasındaki farktır (P_eski - P_yeni).'
  },
  {
    id: 'comp_42',
    moduleId: '1012',
    moduleName: 'Takas & Saklama',
    conceptA: {
      title: 'MKT Şelalesi İlk 3 Aşama (Kusurlu Üye + Takasbank İlk Kayıp)',
      desc: 'Temerrüde düşmeyen masum üyelere dokunulmadan önce kullanılan birincil kaynaklar.',
      keyPoint: '1) Kusurlu üyenin işlem teminatı -> 2) Kusurlu üyenin Garanti Fonu payı -> 3) Takasbank Tahsisli Özkaynağı (First-Loss Capital).'
    },
    conceptB: {
      title: 'MKT Şelalesi 4. ve Sonraki Aşamalar (Masum Üyeler & Kalan Sermaye)',
      desc: 'İlk 3 aşama zararı kapatmaya yetmediğinde devreye giren müteselsil kaynaklar.',
      keyPoint: '4) Diğer masum üyelerin Garanti Fonu katkı payları -> 5) Takasbank kalan özkaynağı -> 6) Ek garanti fonu katkısı.'
    },
    differenceRule: 'Takasbank\'ın tahsis ettiği özkaynak (First-loss capital) en sonda değil, masum üyelerin Garanti Fonu paylarından ÖNCE tam 3. SIRADA kullanılır!'
  }
];

const TRAPS: TrapItem[] = [
  {
    id: 'trap_1',
    moduleId: '1001',
    moduleName: 'Mevzuat',
    myth: 'SPK bir şirketin izahnamesini onaylarsa, o şirketin mali durumu Kurul tarafından garantilenmiş sayılır.',
    reality: 'SPK onayı kesinlikle DEVLET VEYA KURUL GARANTİSİ anlamına GELMEZ; yalnızca kamuyu aydınlatma belgelerinin tam ve doğru olduğunu gösterir.',
    whyImportant: 'Sınavda \'SPK izahnameyi onaylayarak hissenin prim yapacağını garanti eder\' şeklindeki seçenekler her zaman YANLIŞTIR.'
  },
  {
    id: 'trap_2',
    moduleId: '1003',
    moduleName: 'SP Araçları',
    myth: 'Tahvil sahipleri genel kurulda söz alıp yönetim kurulu kararlarına karşı oy kullanabilirler.',
    reality: 'Tahvil sahipleri şirketin ortağı değil, ALACAKLISIDIR; genel kurulda hiçbir OY HAKLARI YOKTUR.',
    whyImportant: 'Tahvil sahibi tasfiyede pay sahiplerinden önce alacağını tahsil eder ancak şirketin idaresine katılamaz.'
  },
  {
    id: 'trap_3',
    moduleId: '1003',
    moduleName: 'SP Araçları',
    myth: 'Gayrimenkul Yatırım Ortaklıkları (GYO) inşaat ruhsatı alıp bizzat taşeron çalıştırmadan bina inşa edebilir.',
    reality: 'GYO\'ların bizzat İNŞAAT MÜTEAHHİTLİĞİ YAPMASI KANUNEN YASAKTIR; işi mutlaka üçüncü taraf müteahhit firmalara ihale etmek zorundadırlar.',
    whyImportant: 'GYO kurumlar vergisinden muaftır (%0) ancak inşaat yapamaz.'
  },
  {
    id: 'trap_4',
    moduleId: '1003',
    moduleName: 'SP Araçları',
    myth: 'Katılma İntifa Senetleri (KİS) şirketin sermaye payını temsil eder ve sahibine genel kurulda oy hakkı verir.',
    reality: 'KİS pay temsil etmez, sermaye artırımı sağlamaz ve ASLA OY HAKKI VERMEZ; yalnızca kârdan ve tasfiye artığından pay verir.',
    whyImportant: 'Sınavda KİS\'in oy hakkı olduğu öncülü en popüler çeldiricidir.'
  },
  {
    id: 'trap_5',
    moduleId: '1005',
    moduleName: 'Yatırım Kur.',
    myth: 'Borsada hisse senetleri taban yapıp büyük para kaybeden yatırımcı Yatırımcı Tazmin Merkezi\'ne (YTM) başvurarak zararını tahsil eder.',
    reality: 'YTM piyasa ve fiyat hareketlerinden doğan zararları TAZMİN ETMEZ; sadece aracı kurumun iflası veya personelin zimmeti sonucu teslim edilemeyen hisse ve nakitleri yasal üst limit dahilinde öder.',
    whyImportant: 'Piyasa riski tamamen yatırımcıya aittir.'
  },
  {
    id: 'trap_6',
    moduleId: '1005',
    moduleName: 'Yatırım Kur.',
    myth: 'Kredili işlemlerde özkaynak %20\'nin altına düşerse müşteri hesabını %20\'ye tamamlamakla yükümlüdür.',
    reality: 'Özkaynak tamamlama çağrısı geldiğinde hedef oran sürdürme (%20) değil, en baştaki BAŞLANGIÇ SEVİYESİ (%35) olmak zorundadır.',
    whyImportant: 'Hesaplama sorularında formülü daima %35 başlangıç teminatına göre kurun.'
  },
  {
    id: 'trap_7',
    moduleId: '1012',
    moduleName: 'Takas & Saklama',
    myth: 'Bir aracı kurum temerrüde düştüğünde Takasbank doğrudan diğer masum aracı kurumların Garanti Fonu paralarını kullanır.',
    reality: 'Temerrüt şelalesinde (MKT Yönetmeliği m.36) 7 aşamalı kesin öncelik sırası uygulanır: 1. Temerrüt eden üyenin teminatları -> 2. Temerrüt eden üyenin yatırılmış garanti fonu katkısı -> 3. Varsa sigorta tazminleri -> 4. Takasbank tahsisli sermayesi -> 5. Diğer MKT üyelerinin yatırılmış garanti fonu katkıları -> 6. Üyelerden talep edilecek ilave garanti fonu katkıları -> 7. Takasbank taahhütlü sermayesi.',
    whyImportant: 'MKT Madde 36 kaynak kullanım sırası SPL 1012 sınavının en banko ve ayırt edici sorusudur.'
  },
  {
    id: 'trap_7b',
    moduleId: '1012',
    moduleName: 'Takas & Saklama',
    myth: 'Temerrüt halinde önce Takasbank’ın diğer üyelerin katkılarını kullanır; mütemerrit üyenin kaynakları daha sonra gelir.',
    reality: 'Sorudaki kısaltılmış ve doğru sırada önce mütemerrit üyenin işlem teminatları ve Garanti Fonu katkısı kullanılır; sonra Takasbank tahsisli sermayesi; en nihayet temerrüt etmeyen diğer üyelerin Garanti Fonu katkıları devreye girer. Tam MKT sıralaması 7 aşamalıdır: teminat -> mütemerrit GF -> sigorta -> Takasbank tahsisli sermayesi -> diğer üyeler GF -> ilave GF -> Takasbank taahhütlü sermayesi.',
    whyImportant: 'Bu sırayı karıştıran soruların doğru cevabı çoğu zaman “mütemerrit üye önce, Takasbank sonra, diğer üyeler en son” şeklindedir.'
  },
  {
    id: 'trap_8',
    moduleId: '1003',
    moduleName: 'SP Araçları',
    myth: 'Tahvil alıcısı takas gününde satıcıya sadece borsa ekranında kote edilen Temiz Fiyatı öder.',
    reality: 'Alıcı satıcıya takasta TEMİZ FİYATI DEĞİL, temiz fiyata o güne kadarki işlemiş faizin eklendiği KİRLİ FİYATI (Dirty Price) öder.',
    whyImportant: 'Sınavda \'Alıcının cebinden çıkan fiili nakit tutar\' sorulduğunda Kirli Fiyat = Temiz Fiyat + İşlemiş Faiz formülü kullanılır.'
  },
  {
    id: 'trap_9',
    moduleId: '1005',
    moduleName: 'Yatırım Kur.',
    myth: 'Bireysel bir yatırımcının Serbest Fon alabilmesi veya Nitelikli Yatırımcı sayılabilmesi için 1 Milyon TL nakit/menkul kıymet yeterlidir.',
    reality: '1 Milyon TL kuralı ESKİ MEVZUATTIR! SPK\'nın güncel Kurul İlke Kararı (i-SPK.37.7) ile bireysel talebe bağlı profesyonel müşteri/nitelikli yatırımcı finansal varlık alt sınırı 10 MİLYON TL\'ye yükseltilmiştir.',
    whyImportant: 'Sınavda 1.000.000 TL çeldirici olarak verilir; doğru güncel cevap 10.000.000 TL\'dir.'
  },
  {
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
    whyImportant: 'Sınavda \'Hâkim ortak imtiyazlı oyuyla şirketin faaliyet konusunu değiştirdi\' seçeneği YANLIŞTIR.'
  },
  {
    id: 'trap_13',
    moduleId: '1001',
    moduleName: 'Mevzuat',
    myth: 'Bedelsiz sermaye artırımı şirketin kasasına nakit sokar ve şirketin toplam piyasa değerini doğrudan artırır.',
    reality: 'Bedelsiz artırımda şirketin kasasına 1 KURUŞ BİLE GİRMEZ; sadece iç kaynaklar sermayeye eklenir, hisse fiyatı oransal düşer ve piyasa değeri değişmez.',
    whyImportant: 'Sınavda \'Bedelsiz sermaye artırımı şirketin likiditesini güçlendirir\' ifadesi YANLIŞTIR.'
  },
  {
    id: 'trap_14',
    moduleId: '1001',
    moduleName: 'Mevzuat',
    myth: 'İçsel bilgiye dayalı ticaret (insider trading) yapan bir kişi sonradan pişman olup elde ettiği kazancı Hazineye öderse ceza almaz.',
    reality: 'Bilgi suistimali suçunda (SPKn m.106) ETKİN PİŞMANLIK HÜKMÜ KESİNLİKLE YOKTUR. Etkin pişmanlık sadece işlem bazlı manipülasyonda (m.107) geçerlidir.',
    whyImportant: 'Sınavda içeriden öğrenen için \'Hazineye 2 katını öderse ceza almaz\' çeldiricisi konur; YANLIŞTIR, sadece manipülasyonda geçerlidir.'
  },
  {
    id: 'trap_15',
    moduleId: '1012',
    moduleName: 'Takas & Saklama',
    myth: 'Aracı kurumdaki hesabında 10 yıl boyunca işlem görmeyen hisse senetleri aracı kuruma kâr olarak kalır veya Hazineye gider.',
    reality: '10 yıl boyunca işlem görmeyen ve talep edilmeyen tüm nakit ve sermaye piyasası araçları doğrudan YATIRIMCI TAZMİN MERKEZİ\'NE (YTM) devredilir.',
    whyImportant: 'Devir kurumu Maliye/Hazine değil, kanunen YTM\'dir.'
  },
{
    id: 'trap_16',
    moduleId: '1001',
    moduleName: 'Mevzuat',
    myth: 'Kripto varlık hizmet sağlayıcılarının bilgi sistemleri ve teknolojik altyapı kriterlerini Bilgi Teknolojileri ve İletişim Kurumu (BTK) belirler.',
    reality: 'BTK değil, 6362 sayılı Kanun m. 35/B açıkça Türkiye Bilimsel ve Teknolojik Araştırma Kurumu\'nun (TÜBİTAK) belirleyeceği kriterlere uygunluk şartı getirmiştir.',
    whyImportant: 'Sınavda BTK veya BDDK seçenekleri en kuvvetli çeldiricilerdir; kanunen doğru kurum TÜBİTAK\'tır.'
  },
  {
    id: 'trap_17',
    moduleId: '1001',
    moduleName: 'Mevzuat',
    myth: 'Yatırım fonları portföyü koruma (hedge) veya arbitraj amacıyla fon toplam değerinin %10\'una kadar açığa satış veya kredili menkul kıymet işlemi yapabilir.',
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
    myth: 'Kurumsal Yönetim Tebliği\'ndeki şirket gruplandırma eşikleri (1. Grup: 3 Mr TL / 750 Mn TL) her yıl Maliye\'nin yeniden değerleme katsayısı oranında artırılır.',
    reality: 'Kurumsal Yönetim Tebliği II-17.1 açık hükmü gereğince gruplandırmada kullanılan rakamsal eşikler YENİDEN DEĞERLEMEYE TABİ TUTULMAZ.',
    whyImportant: 'İdari para cezaları yeniden değerlemeyle artarken, kurumsal yönetim grup eşikleri sabit maktu kalır.'
  },
  {
    id: 'trap_20',
    moduleId: '1001',
    moduleName: 'Mevzuat',
    myth: 'Yatırımcı Tazmin Merkezi (YTM) tedrici tasfiyesinde aktiflerden öncelikle Hazine ve vergi gibi kamu alacakları ödenir.',
    reality: 'İcra İflas Kanunu\'ndaki genel kuralın aksine SPKn m. 85 uyarınca tedrici tasfiyede 1. SIRADA MÜŞTERİ ALACAKLARI ödenir; kamu alacakları 2. sıradadır.',
    whyImportant: 'Tedrici tasfiye sıra cetveli sınavda garanti soru olup 1. sıra daima Müşteri Alacaklarıdır.'
  },
{
    id: 'trap_21',
    moduleId: '1003',
    moduleName: 'SP Araçları',
    myth: 'Aracı kurumlar fiyat istikrarı sürecinde hisse fiyatını yükseltmek amacıyla halka arz fiyatının üzerinde de alım emri verebilirler.',
    reality: 'Fiyat istikrarı işlemlerinde halka arz fiyatının ÜZERİNDE ALIM EMRİ VERİLMESİ KANUNEN KESİNLİKLE YASAKTIR; amaç fiyatı şişirmek değil, halka arz fiyatının altına düşmesini frenlemektir.',
    whyImportant: 'Fiyat istikrarı işlemlerinde halka arz fiyatı tavan fiyattır; üstünde emir verilemeyeceği sınavda en sık sorulan tuzaktır.'
  },
  {
    id: 'trap_22',
    moduleId: '1003',
    moduleName: 'SP Araçları',
    myth: 'Hazine tarafından ihraç edilen Altın Tahvili ve Altına Dayalı Kira Sertifikalarını kurumsal portföylerine getiri sağlamak için emeklilik ve yatırım fonları da satın alabilir.',
    reality: 'Hazine ihraç duyurularında açıkça belirtildiği üzere Altın Tahvili ve Altına Dayalı Kira Sertifikaları YALNIZCA GERÇEK KİŞİLERE (bireysel yatırımcılara) satılır; tüzel kişiler ve kurumsal fonlar alamaz.',
    whyImportant: 'Sınavda \'kurumsal yatırımcılar portföy çeşitlendirmesi için satın alabilir\' çeldiricisi konulur; sadece gerçek kişiler alabilir.'
  },
  {
    id: 'trap_23',
    moduleId: '1003',
    moduleName: 'SP Araçları',
    myth: 'Girişim Sermayesi Pazarı\'nda (GSP) yüksek talep gelmesi durumunda şirket ortakları ek pay satışı (greenshoe) yaparak paylarını nitelikli yatırımcılara satabilir.',
    reality: 'Tebliğ II-16.3 uyarınca Girişim Sermayesi Pazarı\'nda mevcut ortakların pay satışı veya EK PAY SATIŞI YAPILMASI KESİNLİKLE YASAKTIR; ihraç yalnızca sermaye artırımı yoluyla yapılabilir.',
    whyImportant: 'GSP\'nin temel felsefesi şirkete yeni taze sermaye girişidir; ortakların para çıkışına veya ek pay satışına izin verilmez.'
  },
  {
    id: 'trap_24',
    moduleId: '1003',
    moduleName: 'SP Araçları',
    myth: 'Bir şirketin ihraç edebileceği borçlanma aracı üst limiti (ihraç tavanı), şirketin ticaret sicilinde kayıtlı ödenmiş sermayesinin katları olarak hesaplanır.',
    reality: 'Borçlanma Araçları Tebliği\'nde ihraç tavanı sermayenin değil, son onaylı finansal tablolardaki ÖZKAYNAK TOPLAMININ 5 katı (halka kapalıda 3 katı) olarak hesaplanır.',
    whyImportant: 'Sınav sorularında sermaye ile özkaynak kavramları yer değiştirilerek tuzak kurulur; doğru baz ÖZKAYNAKTIR.'
  },
  {
    id: 'trap_25',
    moduleId: '1003',
    moduleName: 'SP Araçları',
    myth: 'DİBS ihalelerinde rekabetçi olmayan teklif (ROT) yöntemiyle her yatırım kuruluşu ve bireysel yatırımcı ihale öncesi teminatsız alım yapabilir.',
    reality: 'DİBS ihalelerinde ROT (Rekabetçi Olmayan Teklif) verme hakkı yalnızca KAMU KURUMLARI ile Hazinece seçilmiş PİYASA YAPICI (Market Maker) BANKALARA tanınmıştır.',
    whyImportant: 'Diğer tüm banka ve aracı kurumlar ile yatırımcılar ihaleye doğrudan teklif veremez veya ROT hakkından faydalanamaz.'
  },
  {
    id: 'trap_26',
    moduleId: '1005',
    moduleName: 'Yatırım Kur.',
    myth: 'Kredili işlemlerde özkaynak oranı %35 sürdürme sınırının altına gerilediğinde müşteri hesabını tekrar %35 seviyesine tamamlamak zorundadır.',
    reality: 'Özkaynak tamamlama çağrısı yapıldığında hedef oran %35 sürdürme sınırı DEĞİL, BAŞLANGIÇ ÖZKAYNAK ORANI OLAN %50\'DİR.',
    whyImportant: 'Sınavdaki formül ve hesaplama sorularında tamamlama tutarı daima başlangıç özkaynak oranı olan %50\'ye göre hesaplanır.'
  },
  {
    id: 'trap_27',
    moduleId: '1005',
    moduleName: 'Yatırım Kur.',
    myth: 'Aracı kurum irtibat büroları sadece tanıtım yapar; kesinlikle müşteri emri alamaz ve borsaya iletemez.',
    reality: 'Yatırım Kuruluşları Tebliği (III-39.1) m. 44 uyarınca irtibat büroları MÜŞTERİ EMİRLERİNİ ARACI KURUMA İLETEBİLİR. Yasak olan tek şey nakit ve menkul kıymet tahsilat ve tediye işlemleridir.',
    whyImportant: 'Sınavda irtibat bürolarının hiçbir şekilde emir alamayacağı söylenerek tuzak kurulur; aracı kuruma emir iletimi serbesttir.'
  },
  {
    id: 'trap_28',
    moduleId: '1005',
    moduleName: 'Yatırım Kur.',
    myth: 'Bir müşteri borsada işlem gören herhangi bir menkul kıymeti veya yatırım fonunu satın almak istediğinde istisnasız her üründe uygunluk testi zorunludur.',
    reality: 'Müşterinin kendi talebi olması şartıyla; Yatırım Fonu Katılma Payları ile Borsada işlem gören DİBS (Devlet Tahvili/Hazine Bonosu) alımlarında UYGUNLUK TESTİ YAPILMASI ZORUNLU DEĞİLDİR.',
    whyImportant: 'Yatırım fonları ve kamu borçlanma araçları düşük riskli standart ürünler sayıldığından müşteri bilgilendirilerek uygunluk testinden muaf tutulur.'
  },
  {
    id: 'trap_29',
    moduleId: '1005',
    moduleName: 'Yatırım Kur.',
    myth: 'Aracı kurumlar müşteri çekmek ve işlem hacmini artırmak için kaldıraçlı işlemlerde (Forex) ve CFD\'lerde promosyon kampanyası veya hacim iadesi düzenleyebilir.',
    reality: 'SPK\'nın 15.07.2016 tarihli İlke Kararı ve TSPB Yönergesi uyarınca kaldıraçlı alım satım işlemleri (Forex) ve fark kontratları (CFD) için promosyon kampanyası düzenlenmesi KESİNLİKLE YASAKTIR.',
    whyImportant: 'Kaldıraçlı işlemlerde deneme hesabı bonusları, nakit hediyeler veya işlem hacmine bağlı maliyet iadesi gibi hiçbir promosyona izin verilmez.'
  },
  {
    id: 'trap_30',
    moduleId: '1005',
    moduleName: 'Yatırım Kur.',
    myth: 'Kitle fonlaması platformları gayrimenkul projeleri, konut üretimi ve arsa alım satımı gibi projeler için halktan fon toplayabilir.',
    reality: 'Kitle Fonlaması Tebliği (III-35/A.2) m. 15 uyarınca platformlar GAYRİMENKUL ve gayrimenkule dayalı hakların alım satımı ile gayrimenkul geliştirme projelerine ilişkin KESİNLİKLE KİTLE FONLAMASI YÜRÜTEMEZ.',
    whyImportant: 'Kitle fonlaması yalnızca teknoloji ve üretim faaliyeti odaklı yenilikçi girişim şirketleri içindir; gayrimenkul projeleri kanunen yasaktır.'
  },
  {
    id: 'trap_31',
    moduleId: '1005',
    moduleName: 'Yatırım Kur.',
    myth: 'Halka açık bir şirketin yönetim kurulu üyeleri veya hakim ortakları şirket hisselerinde düşüş beklediklerinde diledikleri gibi açığa satış yapabilirler.',
    reality: 'Kredili İşlemler Tebliği (Seri: V, No: 65) m. 30 uyarınca ihraççı şirketin yönetim kurulu üyeleri, üst düzey personeli ve %10 veya daha fazla paya sahip ortakları ile bunların eş ve çocukları KENDİ ŞİRKETLERİNİN PAYLARINDA AÇIĞA SATIŞ YAPAMAZLAR.',
    whyImportant: 'İçeriden öğrenenlerin kendi hisselerinde açığa satış yapması mutlak işlem yasağı kapsamındadır.'
  },
  {
    id: 'trap_32',
    moduleId: '1012',
    moduleName: 'Takas & Saklama',
    myth: 'Merkezi Karşı Taraf (MKT) rolünü üstlenen Takasbank, temerrüt halinde doğrudan aracı kurumun müşterisiyle muhatap olur ve müşteriye dava açar.',
    reality: 'MKT uygulamasında Takasbank\'ın yasal muhatabı KESİNLİKLE VE SADECE ÜYEDİR (Aracı Kurum/Banka). Takasbank müşterilere karşı sorumlu olmadığı gibi, müşterilerle de doğrudan muhatap olmaz.',
    whyImportant: 'Sınavda "Takasbank temerrüt eden müşteriye doğrudan ihbarname gönderir" çeldiricisi konur; KESİNLİKLE YANLIŞTIR.'
  },
  {
    id: 'trap_33',
    moduleId: '1012',
    moduleName: 'Takas & Saklama',
    myth: 'Tüm yatırım ortaklıkları ve tüm fonlar Portföy Saklama Tebliği (III-56.1) kapsamında saklayıcı tutmak zorundadır.',
    reality: 'GYO, Altyapı GYO, GSYO ve Emeklilik Yatırım Fonları Tebliğ hükümleri çerçevesinde portföy saklama zorunluluğunda DEĞİLDİR! Ancak Gayrimenkul Yatırım Fonları (GYF) ve Girişim Sermayesi Yatırım Fonları (GSYF) TEBLİĞ KAPSAMINDADIR.',
    whyImportant: 'Sınavda "Emeklilik fonları ve GYO\'lar saklayıcı tutmak zorundadır" ifadesi YANLIŞTIR; GYF ve GSYF ise ZORUNLUDUR.'
  },
  {
    id: 'trap_34',
    moduleId: '1012',
    moduleName: 'Takas & Saklama',
    myth: 'Takasbank\'ın MKT olduğu tüm piyasalarda üyelerden maktu üyelik teminatı alınır.',
    reality: 'Ödünç Pay Piyasası\'nda (ÖPP) ÜYELİK TEMİNATI UYGULAMASI BULUNMAMAKTADIR! Üyelik teminatı Pay, BAP ve VİOP\'ta nakit TL olarak alınır.',
    whyImportant: 'Sınavda "Ödünç Pay Piyasasında üyelik teminatı zorunludur" seçeneği YANLIŞTIR.'
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
    myth: 'Üyelerin MKT hizmeti kapsamında Takasbank\'a verdikleri teminatların mülkiyeti daima üyede kalır, Takasbank sadece rehin hakkına sahiptir.',
    reality: '6362 sayılı SPKn m.78 uyarınca, MKT çerçevesinde takas kuruluşları tarafından alınan teminatların MÜLKİYETİ TAKAS KURULUŞUNA (Takasbank) GEÇER; Takasbank teminatları tevdi amaçları doğrultusunda kullanabilir.',
    whyImportant: 'Teminatların mülkiyetinin Takasbank\'a geçmesi ve kamu alacakları dahil haczedilememesi SPKn 78\'in en temel kuralıdır.'
  },
  {
    id: 'trap_37',
    moduleId: '1012',
    moduleName: 'Takas & Saklama',
    myth: 'VİOP\'ta açık pozisyonunda artış olmamasına rağmen diğer işlemlerin azalmasıyla oluşan pasif limit aşımlarında üyeye derhal pozisyon kapatma cezası uygulanır.',
    reality: 'Pasif aşımda olan siciller için derhal re\'sen kapatma uygulanmaz; ancak piyasadaki ilgili dayanak varlığa bağlı toplam açık pozisyonun %12\'si aşılırsa kapatma ve tedbir hükümleri işletilir.',
    whyImportant: 'Sınavda pasif aşım tolerans eşiği %12 olarak sorulmaktadır.'
  },
  {
    id: 'trap_38',
    moduleId: '1012',
    moduleName: 'Takas & Saklama',
    myth: 'Borçlanma Araçları Piyasası\'ndaki (BAP) tüm pazarlarda çok taraflı netleştirme yapılır.',
    reality: 'Taahhütlü İşlemler Pazarı ve Uluslararası Tahvil Pazarı\'ndaki (Eurotahvil) işlemler NETLEŞTİRMEYE DAHİL EDİLMEZ; takasları işlem bazında (brüt) gerçekleştirilir.',
    whyImportant: 'BAP\'ta netleştirme dışı kalan pazarlar sınavda sıkça sorulur: Taahhütlü İşlemler ve Uluslararası Tahvil Pazarı.'
  }
];

const DIAGNOSES: DiagnosisItem[] = [
  {
    id: 'diag_1',
    moduleId: '1001',
    moduleName: 'Mevzuat',
    scenarioEvent: 'Şirket yönetim kurulu üyesinin henüz KAP\'ta açıklanmamış rekor kâr/ihale bilgisini kullanarak pay alması ve haksız menfaat sağlaması.',
    legalDiagnosis: 'Bilgi Suistimali (Insider Trading)',
    applicableLaw: '6362 sayılı SPKn m. 106',
    consequenceOrPenalty: '3 yıldan 8 yıla kadar hapis veya adli para cezası (menfaatin 2 katından az olamaz)',
    examTrap: 'Etkin pişmanlık (m. 107/3) YALNIZCA işlem bazlı piyasa dolandırıcılığında geçerlidir; Bilgi Suistimalinde (m. 106) etkin pişmanlık KESİNLİKLE YOKTUR.'
  },
  {
    id: 'diag_2',
    moduleId: '1001',
    moduleName: 'Mevzuat',
    scenarioEvent: 'Halka açık ortaklığın 40 Milyon TL değerindeki gayrimenkulünü ilişkili tarafın şahsi şirketine emsaline bariz aykırı şekilde 15 Milyon TL bedelle satması.',
    legalDiagnosis: 'Aktif Yolla Örtülü Kazanç Aktarımı (Güveni Kötüye Kullanma)',
    applicableLaw: 'SPKn m. 21 ve m. 110/1-b',
    consequenceOrPenalty: 'Nitelikli Güveni Kötüye Kullanma Suçu (Hapis Cezası ve Zararın İadesi)',
    examTrap: 'Pasif/ihmali yolla kazanç kaybında idari para cezası (m. 103/6) verilirken; aktif fiille malvarlığını eksiltmede m. 110/1-b adli hapis cezası uygulanır.'
  },
  {
    id: 'diag_3',
    moduleId: '1001',
    moduleName: 'Mevzuat',
    scenarioEvent: 'Şirket hakkında geçerli ertelenmiş içsel bir satın alma bilgisi varken basında haber çıkması ve Başkanın \'SPK sormadıkça açıklama yapmayız\' demesi.',
    legalDiagnosis: 'Özel Durum Açıklaması Derhal Doğrulama / Tekzip Yükümlülüğü İhlali',
    applicableLaw: 'II-15.1 Özel Durumlar Tebliği m. 9',
    consequenceOrPenalty: 'Kurul veya Borsa talebi beklenmeksizin DERHAL KAP\'ta açıklama zorunluluğu',
    examTrap: 'Kurulun veya Borsa\'nın yazı göndermesi beklenmez; basında haber veya söylenti çıktığı anda erteleme düşer ve derhal KAP açıklaması şarttır.'
  },
  {
    id: 'diag_4',
    moduleId: '1001',
    moduleName: 'Mevzuat',
    scenarioEvent: 'Sosyal medyada organize olarak hisse tavsiyesi verip takipçiler alırken kendi paylarını el altından satan grubun durumu (Pump & Dump).',
    legalDiagnosis: 'Bilgi Bazlı ve İşlem Bazlı Piyasa Dolandırıcılığı (Manipülasyon)',
    applicableLaw: '6362 sayılı SPKn m. 107/1 ve 107/2',
    consequenceOrPenalty: '3 yıldan 5 yıla kadar hapis ve 5.000 güne kadar adli para cezası',
    examTrap: 'Bilgi bazlı manipülasyonda (m. 107/2) Etkin Pişmanlık uygulanmaz; Etkin Pişmanlık yalnızca işlem bazlı manipülasyonda (m. 107/1) geçerlidir.'
  },
  {
    id: 'diag_5',
    moduleId: '1001',
    moduleName: 'Mevzuat',
    scenarioEvent: 'Halka açık şirketin tüm malvarlığını devretme kararına genel kurulda muhalefet eden ortağın ayrılma hakkını kullanmak istemesi.',
    legalDiagnosis: 'Önemli Nitelikteki İşlem ve Ayrılma Hakkı Kullanımı',
    applicableLaw: 'SPKn m. 23 ve 24; II-23.3 sayılı Tebliğ',
    consequenceOrPenalty: 'Ortaklık payları kamuya açıklama tarihindeki borsa düzeltilmiş fiyatından satın almakla yükümlüdür',
    examTrap: 'Ayrılma hakkı genel kurul toplantısına bizzat katılıp muhalif oy kullanarak tutanağa muhalefet şerhi işleten ortaklara tanınır.'
  },
  {
    id: 'diag_6',
    moduleId: '1001',
    moduleName: 'Mevzuat',
    scenarioEvent: 'BIST 1. Grup halka açık şirketin Bağımsız Yönetim Kurulu üyesinin son 3 yılda şirkette danışmanlık yaptığının anlaşılması.',
    legalDiagnosis: 'Bağımsız Yönetim Kurulu Üyeliği Kriteri İhlali (Bağımsızlığın Kaybı)',
    applicableLaw: 'Kurumsal Yönetim Tebliği (II-17.1) m. 4.3.4',
    consequenceOrPenalty: 'Üyelik sıfatı derhal düşer; yerine en geç yapılacak ilk genel kurulda yeni bağımsız üye seçilir',
    examTrap: 'Bağımsız üyenin şirket, hâkim ortak veya iştiraklerle son 5 YIL içinde istihdam veya ticari ilişkisinin bulunmaması şarttır.'
  },
  {
    id: 'diag_7',
    moduleId: '1001',
    moduleName: 'Mevzuat',
    scenarioEvent: 'SPK tarafından aracı kuruma kesilen 5 milyon TL idari para cezasına karşı yönetim kurulunun dava açmak istemesi.',
    legalDiagnosis: 'İdari Yaptırım Kararlarına Karşı Yargı Yolu ve Görevli Mahkeme',
    applicableLaw: '6362 sayılı SPKn m. 105 ve 2577 sayılı İYUK',
    consequenceOrPenalty: 'Tebliğden itibaren 30 GÜN içinde yetkili İDARE MAHKEMESİNDE iptal davası açılır',
    examTrap: 'SPK para cezalarına karşı Sulh Ceza Hakimliği değil; İDARE MAHKEMESİ yetkilidir (Süre 30 gündür).'
  },
  {
    id: 'diag_8',
    moduleId: '1001',
    moduleName: 'Mevzuat',
    scenarioEvent: 'Anonim şirket genel kurulunda kanuna aykırı olarak pay sahiplerinin bilgi alma ve genel kurula katılma hakkının engellenmesi.',
    legalDiagnosis: 'Genel Kurul Kararının İptali ve Butlan Davası',
    applicableLaw: '6102 sayılı TTK m. 445 ve 447',
    consequenceOrPenalty: 'Karar tarihinden itibaren 3 AY içinde şirket merkezinin bulunduğu Asliye Ticaret Mahkemesinde iptal davası açılır',
    examTrap: 'İptal davası açma süresi 30 gün değil, 3 AYDIR; butlan hallerinde ise süre aranmaksızın her zaman tespit istenebilir.'
  },
  {
    id: 'diag_9',
    moduleId: '1001',
    moduleName: 'Mevzuat',
    scenarioEvent: 'Brokerın kurumsal müşteriden gelen 1 milyon lotluk alım emrini borsaya iletmeden önce şahsi hesabına alım emri girmesi (Front-Running).',
    legalDiagnosis: 'Müşteri Emrine Öncelik Kuralı ve Sadakat Yükümlülüğünün Ağır İhlali',
    applicableLaw: 'TSPB Meslek Kuralları m. 14 ve SPKn m. 106',
    consequenceOrPenalty: 'Disiplin cezası, meslekten geçici/sürekli men ve Bilgi Suistimali kapsamında adli kovuşturma',
    examTrap: 'Front-Running sadece şirket içi bir kusur değil; haksız menfaat sağlayan doğrudan bir sermaye piyasası suçudur.'
  },
  {
    id: 'diag_10',
    moduleId: '1001',
    moduleName: 'Mevzuat',
    scenarioEvent: 'Yatırım fonu kurucusu olan Portföy Yönetim Şirketi\'nin iflas etmesi ve alacaklıların fon malvarlığına haciz koydurmak istemesi.',
    legalDiagnosis: 'Yatırım Fonu Malvarlığının Mutlak Korunması ve Ayrılığı',
    applicableLaw: '6362 sayılı SPKn m. 53',
    consequenceOrPenalty: 'Fon malvarlığı kamu alacakları için dahi haczedilemez, iflas masasına dahil edilemez',
    examTrap: 'Vergi ve SGK gibi kamu alacakları dahi fon malvarlığını haczedemez; portföy başka bir saklayıcıya devredilir.'
  },
  {
    id: 'diag_11',
    moduleId: '1001',
    moduleName: 'Mevzuat',
    scenarioEvent: 'Halka arz izahnamesi onaylandıktan sonra şirketin en büyük üretim tesisinde yangın çıkması ve üretimin durması.',
    legalDiagnosis: 'İzahnamede Önemli Yeni Gelişme ve Ek/Tadil Yükümlülüğü',
    applicableLaw: 'II-5.1 İzahname Tebliği m. 11',
    consequenceOrPenalty: 'Gelişmeden itibaren 7 iş gününde Kurula başvurulur; Kurul 7 iş gününde onaylar; yatırımcılara 3 iş günü cayma hakkı doğar',
    examTrap: 'İzahname onaylanmış olsa dahi halka arz tamamlanana kadar meydana gelen yeni gelişmeler izahname ekiyle onaylatılmak zorundadır.'
  },
  {
    id: 'diag_12',
    moduleId: '1001',
    moduleName: 'Mevzuat',
    scenarioEvent: 'Kayıtlı sermaye tavanı 500 Milyon TL olan şirkette genel kurulca verilen 5 yıllık sürenin dolması ve YK\'nın tavan dahilinde sermaye artırmak istemesi.',
    legalDiagnosis: 'Kayıtlı Sermaye Sistemi Yetki Süresinin Sona Ermesi',
    applicableLaw: 'SPKn m. 18 ve II-18.1 Tebliği m. 6',
    consequenceOrPenalty: 'Genel kuruldan yeni bir 5 yıllık yetki alınmadıkça yönetim kurulu kararıyla sermaye artırımı yapılamaz',
    examTrap: 'Süre dolduğunda şirket kayıtlı sermaye sisteminden çıkmış sayılmaz; ancak yönetim kurulu sermaye artıramaz (yetki genel kurula döner).'
  },
  {
    id: 'diag_13',
    moduleId: '1003',
    moduleName: 'SP Araçları',
    scenarioEvent: 'Şirketin ihraç ettiği tahvillerin kupon faiz ödemesini vadesinde yapamaması ve temerrüde düşmesi.',
    legalDiagnosis: 'Borçlanma Araçları Sahipleri Kurulu (BASK) Toplantı ve Karar Süreci',
    applicableLaw: 'Borçlanma Araçları Tebliği (VII-128.8) m. 25-28',
    consequenceOrPenalty: 'Tedavüldeki tahvillerin en az %10\'una sahip yatırımcılar BASK\'ı çağırır; kararlar 2/3 sermaye çoğunluğuyla alınır',
    examTrap: 'BASK toplantı çağrısı için tedavüldeki tahvil nominal tutarının en az %10\'u, karar için ise en az 2/3 (üçte iki) çoğunluk aranır.'
  },
  {
    id: 'diag_14',
    moduleId: '1003',
    moduleName: 'SP Araçları',
    scenarioEvent: 'Bedelli sermaye artırımında yönetim kurulunun mevcut ortakların rüçhan haklarını kısıtlayarak tahsisli hisse ihraç etmesi.',
    legalDiagnosis: 'Rüçhan Hakkının Sınırlandırılması ve Esas Sözleşme Yetkisi',
    applicableLaw: '6102 sayılı TTK m. 461 ve Pay Tebliği (VII-128.1)',
    consequenceOrPenalty: 'Esas sözleşmede açık yetki bulunması ve YK gerekçe raporunun KAP\'ta ilanı şarttır',
    examTrap: 'Rüçhan hakkı kısıtlaması için esas sözleşmede yönetim kuruluna açıkça yetki verilmiş olması ve YK raporunun KAP\'ta ilanı zorunludur.'
  },
  {
    id: 'diag_15',
    moduleId: '1003',
    moduleName: 'SP Araçları',
    scenarioEvent: 'Şirket genel kurulunda esas sözleşme değişikliği ve yönetim kurulunun ibrası oylanırken imtiyazlı pay sahiplerinin 15 oy kullanmak istemesi.',
    legalDiagnosis: 'Oyda İmtiyazın Kullanılamayacağı Emredici Kanuni Haller',
    applicableLaw: 'SPKn m. 28 ve 6102 sayılı TTK m. 479',
    consequenceOrPenalty: 'Esas sözleşme değişikliği ve ibra oylamalarında her pay sahibi yalnızca TEK OY (1 pay = 1 oy) kullanabilir',
    examTrap: 'Esas sözleşme değişikliği, yönetim kurulu üyelerinin ibrası ve sorumluluk davası açılmasında oyda imtiyaz KESİNLİKLE KULLANILAMAZ.'
  },
  {
    id: 'diag_16',
    moduleId: '1003',
    moduleName: 'SP Araçları',
    scenarioEvent: 'Enflasyonun yükseldiği dönemde TÜFE\'ye endeksli devlet tahvili alan kurumsal yatırımcının dönemsel getiri hesabı.',
    legalDiagnosis: 'Enflasyona Endeksli Borçlanma Aracı Anapara ve Kupon Güncellemesi',
    applicableLaw: 'Hazine Finansman Kanunu ve Borçlanma Araçları Tebliği',
    consequenceOrPenalty: 'Hem dönemsel kupon ödemeleri hem de vade sonu anapara enflasyon endeks katsayısıyla çarpılarak ödenir',
    examTrap: 'TÜFE tahvilinde enflasyon artışı sadece kuponu değil, tahvilin anapara nominal değerini de doğrudan artırır.'
  },
  {
    id: 'diag_17',
    moduleId: '1003',
    moduleName: 'SP Araçları',
    scenarioEvent: 'VKŞ tarafından ihraç edilen yönetim sözleşmesine dayalı kira sertifikasında kaynak kuruluşun kâr payını ödeyememesi.',
    legalDiagnosis: 'Yönetim Sözleşmesine Dayalı Kira Sertifikası (Vekâlet Sukuk) Temerrüdü',
    applicableLaw: 'III-61.1 Kira Sertifikaları Tebliği',
    consequenceOrPenalty: 'Kaynak kuruluş taahhüt ettiği getiri ve anaparanın tamamından VKŞ\'ye ve yatırımcılara karşı doğrudan müteselsilen sorumludur',
    examTrap: 'Kira sertifikalarında kaynak kuruluş iflas etse dahi dayanak varlıklar VKŞ nezdinde ayrı bir malvarlığı olarak güvence altındadır.'
  },
  {
    id: 'diag_18',
    moduleId: '1003',
    moduleName: 'SP Araçları',
    scenarioEvent: 'VİOP vadeli sözleşmesinde yatırımcının teminatının sürdürme seviyesinin altına düşmesi üzerine aracı kurumun çağrı yapması.',
    legalDiagnosis: 'Margin Call ve Başlangıç Teminatına Tamamlama Kuralı',
    applicableLaw: 'VİOP İşleyiş Esasları ve Takasbank Prosedürleri',
    consequenceOrPenalty: 'Yatırımcı ertesi iş günü (T+1) saat 15:00\'e kadar teminatını tekrar BAŞLANGIÇ seviyesine tamamlamak zorundadır',
    examTrap: 'Teminat sürdürme seviyesine kadar değil; TEKRAR BAŞLANGIÇ TEMİNATI DÜZEYİNE tamamlanmak zorundadır.'
  },
  {
    id: 'diag_19',
    moduleId: '1003',
    moduleName: 'SP Araçları',
    scenarioEvent: 'Alım (Call) opsiyonu alan yatırımcının hisse fiyatının kullanım fiyatının altında kalması üzerine zarara uğraması.',
    legalDiagnosis: 'Opsiyon Alıcısının Hukuki Durumu ve Zararın Sınırlandırılması',
    applicableLaw: 'Türev Araçlar İlkeleri',
    consequenceOrPenalty: 'Alıcı opsiyon hakkını kullanmaz; azami zararı ödediği primle sınırlı kalır',
    examTrap: 'Opsiyon alıcısının teslim yükümlülüğü yoktur; aleyhine olan durumda hakkını kullanmaktan vazgeçebilir ve zararı prim kadardır.'
  },
  {
    id: 'diag_20',
    moduleId: '1003',
    moduleName: 'SP Araçları',
    scenarioEvent: 'Varant ihraç eden aracı kurumun iflas etmesi durumunda varant sahiplerinin Takasbank\'a başvurması.',
    legalDiagnosis: 'Varantlarda İhraççı Kredi Riski ve MKT Garantisinin Olmaması',
    applicableLaw: 'VII-128.3 Varantlar Tebliği',
    consequenceOrPenalty: 'Varant ihraççının menkul kıymetidir; Takasbank MKT garantisi ihraççı iflasını kapsamaz, yatırımcı genel masaya başvurur',
    examTrap: 'Varantlarda teminat tamamlama çağrısı yoktur ancak İHRAÇÇI KREDİ RİSKİ vardır; Takasbank CCP garantisi varant ihraççısının batmasını ödemez.'
  },
  {
    id: 'diag_21',
    moduleId: '1003',
    moduleName: 'SP Araçları',
    scenarioEvent: 'GYO\'nun portföyündeki nakit fazlasıyla bizzat inşaat makineleri alıp yüklenici sıfatıyla inşaat yapmaya başlaması.',
    legalDiagnosis: 'GYO Faaliyet Yasakları (Bizzat Müteahhitlik Yapma Yasağı)',
    applicableLaw: 'III-48.1 GYO Tebliği m. 22',
    consequenceOrPenalty: 'GYO bizzat inşaat yapamaz; inşaat işlerini müteahhitlik şirketlerine ihale etmek zorundadır',
    examTrap: 'GYO inşaat yapamaz, arsa geliştirip projeyi taşerona yaptırır; kazançları Kurumlar Vergisinden tamamen istisnadır (%0 KV).'
  },
  {
    id: 'diag_22',
    moduleId: '1003',
    moduleName: 'SP Araçları',
    scenarioEvent: 'VDMK ihraç eden fonun teminat havuzuna vadesi geçmiş ve icra takibine uğramış batık tüketici kredilerinin devredilmesi.',
    legalDiagnosis: 'VDMK Teminat Havuzuna Kabul Edilemeyecek Varlık Yasağı',
    applicableLaw: 'III-58.1 VDMK Tebliği m. 7',
    consequenceOrPenalty: 'Batık/şüpheli alacaklar teminat havuzuna devredilemez; ihraç belgesi Kurulca onaylanmaz',
    examTrap: 'VDMK teminat havuzuna vadesi gelmemiş ve tahsilatında gecikme olmayan standart sağlam alacaklar devredilebilir.'
  },
  {
    id: 'diag_23',
    moduleId: '1003',
    moduleName: 'SP Araçları',
    scenarioEvent: 'Borsa Yatırım Fonu (BYF) katılma paylarının seans içinde işlem görmesi ve fon payı yaratma/bozdurma mekanizması.',
    legalDiagnosis: 'Yetkilendirilmiş Katılımcı ve Ayni Pay Yaratma/Bozdurma (Creation/Redemption)',
    applicableLaw: 'III-52.2 BYF Tebliği',
    consequenceOrPenalty: 'BYF borsada hisse gibi işlem görür; yetkilendirilmiş katılımcı baz varlık sepeti teslim ederek anlık pay yaratır/bozar',
    examTrap: 'BYF katılma payları TEFAS\'ta tek fiyattan değil; seans boyunca Borsa İstanbul Pay Piyasası\'nda sürekli işlem görür.'
  },
  {
    id: 'diag_24',
    moduleId: '1003',
    moduleName: 'SP Araçları',
    scenarioEvent: 'Halka açık şirkette hâkim ortağın pay oranının %98\'e ulaşması üzerine azınlık ortakların durumdan rahatsız olması.',
    legalDiagnosis: 'Ortaklıktan Çıkarma Hakkı ve Satma Hakkı Eşiği',
    applicableLaw: 'II-27.3 Ortaklıktan Çıkarma ve Satma Hakları Tebliği',
    consequenceOrPenalty: 'Hâkim ortak azınlığı şirketten çıkarabilir; azınlık pay sahipleri de paylarını hâkim ortağa satmaya zorlayabilir',
    examTrap: 'Ortaklıktan çıkarma ve satma hakkı eşiği %50 veya %75 değil, KESİNLİKLE %98 OY HAKKI EŞİĞİDİR.'
  },
  {
    id: 'diag_25',
    moduleId: '1005',
    moduleName: 'Yatırım Kur.',
    scenarioEvent: 'Dar yetkili aracı kurumun Borsa İstanbul Pay Piyasası terminallerinden bizzat hisse alım satım emri icra etmesi.',
    legalDiagnosis: 'Dar Yetkili Aracı Kurum Faaliyet Yetki Aşımı (İşlem Aracılığı Yasağı)',
    applicableLaw: 'Yatırım Kuruluşları Tebliği (III-39.1) m. 5',
    consequenceOrPenalty: 'Dar yetkili kurum borsada doğrudan işlem yapamaz; emirleri kısmi/geniş yetkili kuruma iletmek zorundadır',
    examTrap: 'Dar yetkili aracı kurumlar emir iletimi yapabilir; ancak borsa terminallerinde bizzat emir icra edemez (işlem aracılığı yapamaz).'
  },
  {
    id: 'diag_26',
    moduleId: '1005',
    moduleName: 'Yatırım Kur.',
    scenarioEvent: 'Aracı kurum irtibat bürosu çalışanının müşteriden elden 500.000 TL nakit tahsil ederek hisse alım sözleşmesi imzalatması.',
    legalDiagnosis: 'İrtibat Bürosu Ağır Yetki Aşımı ve Nakit Tahsilat Yasağı',
    applicableLaw: 'Yatırım Kuruluşları Tebliği (III-39.1) m. 44',
    consequenceOrPenalty: 'İrtibat bürosu hesap açamaz, sözleşme imzalayamaz, nakit/kıymet teslim alamaz ve ödeme yapamaz',
    examTrap: 'Şubeler nakit/sözleşme işlemi yapabilir; irtibat büroları ise yalnızca tanıtım yapabilir ve emirleri merkeze iletebilir.'
  },
  {
    id: 'diag_27',
    moduleId: '1005',
    moduleName: 'Yatırım Kur.',
    scenarioEvent: 'Müşteri temsilcisinin belirli bir müşterinin mali gücünü analiz ederek şahsa özel hisse portföy sepeti önermesi.',
    legalDiagnosis: 'Yatırım Danışmanlığı Hizmeti ve Yazılı Çerçeve Sözleşme Zorunluluğu',
    applicableLaw: 'Yatırım Hizmetleri Tebliği (III-37.1) m. 11',
    consequenceOrPenalty: 'Kişiye özel yönlendirici tavsiye Yatırım Danışmanlığıdır; SPK yetki belgesi, Düzey 3 Lisansı ve sözleşme şarttır',
    examTrap: 'Web sitesinde herkese açık sabah bülteni Genel Tavsiyedir; müşterinin mali durumuna özel hazırlanan öneri Yatırım Danışmanlığıdır.'
  },
  {
    id: 'diag_28',
    moduleId: '1005',
    moduleName: 'Yatırım Kur.',
    scenarioEvent: 'Bireysel portföy yönetiminde piyasa krizi sebebiyle müşterinin 10 Milyon TL\'lik portföyünün 8 Milyon TL\'ye gerilemesi ve müşterinin zararı istemesi.',
    legalDiagnosis: 'Vekâlet Sözleşmesi Sorumluluk Sınırı ve Getiri Garantisi Yasağı',
    applicableLaw: 'TBK m. 502 ve III-55.1 Tebliği',
    consequenceOrPenalty: 'Yönetici basiretli vekil gibi davrandığı sürece piyasa kaybından sorumlu tutulamaz; getiri taahhüdü kanunen yasaktır',
    examTrap: 'Portföy yöneticiliği vekâlet akdidir; yönetici kâr garantisi veremez, kusuru olmaksızın oluşan piyasa kaybını tazmin etmez.'
  },
  {
    id: 'diag_29',
    moduleId: '1005',
    moduleName: 'Yatırım Kur.',
    scenarioEvent: 'Hisse hesabı olan müşterinin Uygunluk Testi sonucunda VİOP için \'uygun değildir\' uyarısı almasına rağmen işlem yapmak istemesi.',
    legalDiagnosis: 'Uygunluk Testinde Müşteri Israrı ve Yazılı Beyanla İşlem İcrası',
    applicableLaw: 'Yatırım Hizmetleri Tebliği (III-37.1) m. 33',
    consequenceOrPenalty: 'Kurum yazılı risk uyarısı yapar; müşteri riski üstlendiğini yazılı beyan ederse işlem gerçekleştirilebilir',
    examTrap: 'Uygunluk testinde müşteri ısrar ederse yazılı beyanla işlem yapılabilir; ancak Yerindelik Testinde (danışmanlık/portföy) ısrar etse dahi hizmet verilemez!'
  },
  {
    id: 'diag_30',
    moduleId: '1005',
    moduleName: 'Yatırım Kur.',
    scenarioEvent: 'Aracı kurumun hesabında 50 milyon TL bulunan bireysel fabrikatör müşteriyi doğrudan profesyonel müşteri sınıfına alması.',
    legalDiagnosis: 'Müşteri Sınıflandırma Hatası (Gerçek Kişilerin Kendiliğinden Profesyonel Olamaması)',
    applicableLaw: 'III-37.1 Tebliği m. 31 ve 32',
    consequenceOrPenalty: 'Gerçek kişiler doğrudan profesyonel müşteri olamaz; yazılı talep ve 3 şarttan en az 2\'sini sağlaması zorunludur',
    examTrap: 'Gerçek kişi ne kadar zengin olursa olsun doğrudan profesyonel müşteri DEĞİLDİR; sadece yazılı taleple Talebe Dayalı Profesyonel Müşteri olabilir.'
  },
  {
    id: 'diag_31',
    moduleId: '1005',
    moduleName: 'Yatırım Kur.',
    scenarioEvent: 'Kısmi yetkili bir aracı kurumun özsermayesinin 2026 yılı yasal eşiği olan 190 Milyon TL\'nin altına (150 Milyon TL\'ye) inmesi.',
    legalDiagnosis: 'Asgari Özsermaye Yükümlülüğü Açığı ve Tamamlama Süreci',
    applicableLaw: 'Yatırım Kuruluşları Tebliği (III-39.1)',
    consequenceOrPenalty: 'Kurum derhal Kurula bildirir ve eksilen özsermayeyi mevzuatta tanınan yasal sürede tamamlamak zorundadır',
    examTrap: '2026 Asgari Özsermaye Eşikleri: Dar Yetkili: 45M TL, Kısmi Yetkili: 190M TL, Geniş Yetkili: 380M TL\'dir.'
  },
  {
    id: 'diag_32',
    moduleId: '1005',
    moduleName: 'Yatırım Kur.',
    scenarioEvent: 'Kredili işlemde hisse düşüşüyle müşterinin özkaynak oranının %30\'a gerilemesi üzerine kurumun müşteriyi araması.',
    legalDiagnosis: 'Sürdürme Özkaynak Oranı İhlali ve Tamamlama Süresi',
    applicableLaw: 'Seri: V, No: 65 sayılı Tebliğ m. 13-17',
    consequenceOrPenalty: 'Müşteri bildirimi izleyen 2 İŞ GÜNÜ içinde özkaynağını tekrar asgari %50 (Başlangıç) seviyesine tamamlamalıdır',
    examTrap: 'Tamamlama süresi 2 takvim günü değil 2 İŞ GÜNÜDÜR; tamamlanması gereken oran %35 değil, BAŞLANGIÇ ORANI olan asgari %50\'dir.'
  },
  {
    id: 'diag_33',
    moduleId: '1005',
    moduleName: 'Yatırım Kur.',
    scenarioEvent: 'Açığa satış yasağı olmayan bir BIST hissesinde yatırımcının en son işlem fiyatı olan 100 TL\'den açığa satış emri girmesi (Up-tick Kuralı).',
    legalDiagnosis: 'Yukarı Adım (Up-Tick) Kuralı Uygulama Zorunluluğu',
    applicableLaw: 'Borsa İstanbul Açığa Satış Yönergesi',
    consequenceOrPenalty: 'Fiyat düşüşünü engellemek için açığa satış son fiyattan daha yüksek bir fiyattan (en az 100,10 TL) yapılmalıdır',
    examTrap: 'Yukarı adım kuralı geçerliyken son gerçekleşen fiyattan daha düşük fiyata açığa satış emri girilemez; en az son fiyattan yüksek girilmelidir.'
  },
  {
    id: 'diag_34',
    moduleId: '1005',
    moduleName: 'Yatırım Kur.',
    scenarioEvent: 'Görüntülü görüşmeyle uzaktan hesap açan müşterinin ilk para transferini şirket ortağının banka hesabından yapması.',
    legalDiagnosis: 'Uzaktan Müşteri Ediniminde İlk Para Transferi Kuralı İhlali',
    applicableLaw: 'Sermaye Piyasasında Uzaktan Kimlik Tespiti Tebliği',
    consequenceOrPenalty: 'Hesap aktifleşmez; ilk EFT/Havale MUTLAKA müşterinin kendi adına açılmış banka hesabından gelmelidir',
    examTrap: 'Uzaktan edinimde ilk para transferi eş, ortak veya akraba hesabından yapılamaz; bizzat müşterinin kendi ad ve soyadına kayıtlı olmalıdır.'
  },
  {
    id: 'diag_35',
    moduleId: '1005',
    moduleName: 'Yatırım Kur.',
    scenarioEvent: 'Aracı kurumun yer darlığı nedeniyle 3 yıl önceki müşteri emir formlarını ve telefon ses kayıtlarını imha etmesi.',
    legalDiagnosis: 'Belge ve Kayıt Düzeni Saklama Süresi İhlali',
    applicableLaw: 'III-45.1 Belge ve Kayıt Düzeni Tebliği m. 28',
    consequenceOrPenalty: 'Müşteri sözleşmeleri, emir kayıtları ve telefon ses kayıtları EN AZ 5 YIL saklanmak zorundadır',
    examTrap: 'TTK genel ticari defter saklama süresi 10 yıldır; ancak SPK Belge ve Kayıt Düzeni Tebliği uyarınca müşteri kayıtları EN AZ 5 YIL saklanır.'
  },
  {
    id: 'diag_36',
    moduleId: '1005',
    moduleName: 'Yatırım Kur.',
    scenarioEvent: 'Aracı kurum organizasyon şemasında İç Denetim Birimi yöneticisinin doğrudan Şirket Genel Müdürüne bağlanması.',
    legalDiagnosis: 'İç Denetimin Bağımsızlığı İlkesi İhlali',
    applicableLaw: 'Yatırım Kuruluşları Tebliği (III-39.1) m. 18',
    consequenceOrPenalty: 'İç denetim icraya (Genel Müdüre) bağlanamaz; doğrudan Yönetim Kurulu veya Denetim Komitesine bağlı olmalıdır',
    examTrap: 'İç Denetim ve İç Kontrol birimleri Genel Müdüre DEĞİL, doğrudan Yönetim Kurulu\'na veya Denetim Komitesi\'ne bağlı çalışır.'
  },
  {
    id: 'diag_37',
    moduleId: '1012',
    moduleName: 'Takas & Saklama',
    scenarioEvent: 'Pay Piyasasında T+2 takas günü saat 16:45 itibarıyla nakit takas borcunu kapatamayan aracı kurumun durumu.',
    legalDiagnosis: 'Takas Borcu Temerrüdü ve 16:45 Kesin Takas Kapanış Saati',
    applicableLaw: 'Takasbank Merkezi Karşı Taraf Yönergesi',
    consequenceOrPenalty: '16:45\'te borç kapatılmazsa temerrüt başlar; teminatlar ve garanti fonu şelale sırasıyla devreye girer',
    examTrap: 'Pay Piyasası takas kapanış saati 17:30 veya 18:00 değil, tam olarak 16:45\'tir. Teminat tamamlama çağrısı son saati ise 15:00\'tir.'
  },
  {
    id: 'diag_38',
    moduleId: '1012',
    moduleName: 'Takas & Saklama',
    scenarioEvent: 'Borçlanma Araçları Piyasası (BAP) takasında üyenin nakit borcunu saat 16:48\'de Takasbank hesabına yatırması.',
    legalDiagnosis: 'BAP Ön Temerrüt Süreci ve 0.25 İndirimli Gecikme Katsayısı',
    applicableLaw: 'Takasbank BAP Takas ve Temerrüt Esasları',
    consequenceOrPenalty: '16:46 - 17:00 arası ön temerrüttür; üye 0.25 gecikme katsayısıyla faiz ödeyerek temerrütsüz borcunu kapatır',
    examTrap: 'Ön temerrüt (16:46-17:00 arası 0.25 katsayı) SADECE Borçlanma Araçları Piyasası\'nda vardır; Pay Piyasası\'nda ön temerrüt yoktur.'
  },
  {
    id: 'diag_39',
    moduleId: '1012',
    moduleName: 'Takas & Saklama',
    scenarioEvent: 'Takasbank MKT temerrüt şelalesinde temerrüde düşen üyenin teminatları ve garanti fonu katkı payı yetersiz kaldığında devreye giren kaynak.',
    legalDiagnosis: 'Takasbank Taahhütlü MKT Özkaynak Payı (3. Sıra Sermaye Katkısı)',
    applicableLaw: 'Takasbank MKT Yönergesi m. 36',
    consequenceOrPenalty: 'Masum diğer üyelerin Garanti Fonuna geçilmeden ÖNCE Takasbank kendi taahhüt ettiği sermaye katkısını harcar',
    examTrap: 'Takasbank özkaynağı en sona bırakılmaz; 3. sırada Takasbank taahhütlü özkaynağı devreye girer, 4. sırada diğer üyelerin fonu kullanılır.'
  },
  {
    id: 'diag_40',
    moduleId: '1012',
    moduleName: 'Takas & Saklama',
    scenarioEvent: 'MKK doğrudan hak sahipliği sisteminde işlem yapan bir aracı kurumun iflas etmesi halinde müşteri hisselerinin hukuki durumu.',
    legalDiagnosis: 'Doğrudan Hak Sahipliği ve Mülkiyetin Ayrılığı İlkesi',
    applicableLaw: '6362 sayılı SPKn m. 13 ve 81',
    consequenceOrPenalty: 'Paylar aracı kurum havuzunda değil müşteri TCKN alt hesabında olduğundan iflas masasına devredilemez',
    examTrap: 'Türkiye\'de Omnibus saklama değil Doğrudan Hak Sahipliği geçerlidir; kurum batsa dahi müşterinin hisseleri eksiksiz korunur.'
  },
  {
    id: 'diag_41',
    moduleId: '1012',
    moduleName: 'Takas & Saklama',
    scenarioEvent: 'Yatırımcının e-YATIRIMCI uygulamasından hisselerine \'Yatırımcı Blokajı\' koyması sonrasında kurumun hisseyi virmanlamak istemesi.',
    legalDiagnosis: 'MKK Yatırımcı Blokajı Güvenlik Modülü ve Virman Engeli',
    applicableLaw: 'MKK Hak Sahipliği ve e-YATIRIMCI Yönergesi',
    consequenceOrPenalty: 'Blokajı yalnızca yatırımcı kaldırabilir; aracı kurum veya çalışanları hisse üzerinde hiçbir işlem yapamaz',
    examTrap: 'Yatırımcı blokajı Takasbank nezdinde değil; Merkezi Kayıt Kuruluşu (MKK) e-YATIRIMCI uygulaması üzerinden konulur.'
  },
  {
    id: 'diag_42',
    moduleId: '1012',
    moduleName: 'Takas & Saklama',
    scenarioEvent: 'Borsada hisseleri %70 düşen yatırımcının uğradığı sermaye kaybını Yatırımcı Tazmin Merkezi\'nden (YTM) talep etmesi.',
    legalDiagnosis: 'YTM Kanuni Tazmin Kapsamı Dışılık (Piyasa Fiyat Düşüşü Zararları)',
    applicableLaw: '6362 sayılı SPKn m. 82-84',
    consequenceOrPenalty: 'Tazmin talebi reddedilir; YTM borsa fiyat düşüşü ve yatırım risklerini KESİNLİKLE TAZMİN ETMEZ',
    examTrap: 'YTM piyasa kaybını ödemez; yalnızca aracı kurumun iflası/tasfiyesi nedeniyle müşteriye emanet kıymet ve nakdi verememesi halinde devreye girer.'
  },
  {
    id: 'diag_43',
    moduleId: '1012',
    moduleName: 'Takas & Saklama',
    scenarioEvent: 'BAP Kesin Alım Satım Pazarında saat 11:30\'da aynı gün valörlü (T+0) gerçekleşen DİBS alım satımının takas saati.',
    legalDiagnosis: 'BAP T+0 Kesin Takas Kapanış Saati',
    applicableLaw: 'Borsa İstanbul BAP Yönergesi ve Takas Esasları',
    consequenceOrPenalty: 'İşlem T+0 günü en geç saat 16:45 itibarıyla nakit ve kıymet takası tamamlanmak zorundadır',
    examTrap: 'Aynı gün valörlü (T+0) DİBS işlemlerinde de takas borcu kapama son saati 16:45\'tir.'
  },
  {
    id: 'diag_44',
    moduleId: '1012',
    moduleName: 'Takas & Saklama',
    scenarioEvent: 'Satış yapan üyenin T+2\'de hisseyi teslim edememesi ve ÖPP\'den de ödünç hisse bulunamaması üzerine Takasbank\'ın harekete geçmesi.',
    legalDiagnosis: 'Takasbank Temerrüt İkame Alımı (Borsa Temerrüt Sırası / Buy-in)',
    applicableLaw: 'Takasbank Ödünç Pay Piyasası ve Temerrüt Yönergesi',
    consequenceOrPenalty: 'Takasbank T+3 günü saat 11:00\'e kadar açık piyasadan re\'sen ikame alım yapar; oluşan maliyeti temerrüt eden üyeden tahsil eder',
    examTrap: 'Takasbank açık piyasadan re\'sen alımı takas günü değil; takası izleyen iş günü olan T+3 saat 11:00\'e kadar Borsa Temerrüt Sırasında yapar.'
  },
  {
    id: 'diag_45',
    moduleId: '1012',
    moduleName: 'Takas & Saklama',
    scenarioEvent: 'Portföy saklayıcısı bankanın portföy yönetim şirketi ile yaptığı saklama sözleşmesini feshetmek istemesi.',
    legalDiagnosis: 'Portföy Saklama Sözleşmesi Fesih İhbar Süresi Zorunluluğu',
    applicableLaw: 'Portföy Saklama Tebliği (III-56.1) m. 14',
    consequenceOrPenalty: 'Fesih ihbarı en az 90 GÜN önceden karşı tarafa ve SPK\'ya yazılı olarak bildirilmek zorundadır',
    examTrap: 'Saklama sözleşmesi fesih ihbar süresi 30 gün veya 60 gün değil; tam olarak 90 GÜNDÜR.'
  },
  {
    id: 'diag_46',
    moduleId: '1012',
    moduleName: 'Takas & Saklama',
    scenarioEvent: 'BISTECH risk algoritmasında üyenin teminat olarak sunduğu BIST 30 hisseleri ve DİBS\'lerin değerlemesi.',
    legalDiagnosis: 'Nakit Dışı Teminatlarda Saç Tıraşı (Haircut / İskonto) ve Asgari Nakit TL Kuralı',
    applicableLaw: 'Takasbank MKT Teminat Yönetmeliği',
    consequenceOrPenalty: 'Kıymetlere risk katsayısı (iskonto) uygulanır ve VİOP pozisyonlarında asgari %50 nakit TL teminat oranı aranır',
    examTrap: 'Nakit dışı teminatlar piyasa fiyatından %100 kabul edilmez; likidite ve fiyat riskine göre iskonto (haircut) kesilerek kabul edilir.'
  },
  {
    id: 'diag_47',
    moduleId: '1012',
    moduleName: 'Takas & Saklama',
    scenarioEvent: '2012 yılında kaydileştirilmeyen fiziki pay senetlerinin 10 yıl sonra mülkiyetinin YTM\'ye devredilmek istenmesi.',
    legalDiagnosis: 'Kaydileştirilmeyen Paylarda Zamanaşımı Mülkiyet Devrinin AYM Tarafından İptali',
    applicableLaw: 'Anayasa Mahkemesi İptal Kararı (2012/100 E., 2015/18 K.)',
    consequenceOrPenalty: 'Payların mülkiyeti 10 yıl geçse dahi devlete geçmez; yönetim hakları donar, kâr payları YTM hesabında saklanır',
    examTrap: 'Eski SPKn m. 13\'teki 10 yıllık zamanaşımıyla mülkiyetin devlete geçmesi hükmü AYM tarafından İPTAL EDİLMİŞTİR; mülkiyet hakkı zamanaşımına uğramaz.'
  },
  {
    id: 'diag_48',
    moduleId: '1012',
    moduleName: 'Takas & Saklama',
    scenarioEvent: 'Borsa İstanbul Kıymetli Madenler ve Taşlar Piyasası\'nda (KMTP) gerçekleşen altın ve gümüş işlemlerinin takas güvencesi.',
    legalDiagnosis: 'Takasbank\'ın Merkezi Karşı Taraf OLMADIĞI Piyasa Statüsü',
    applicableLaw: 'Takasbank MKT Yönergesi m. 3',
    consequenceOrPenalty: 'Takasbank KMTP\'de takas bankasıdır ancak Merkezi Karşı Taraf (CCP) garantisi VERMEZ',
    examTrap: 'Takasbank Pay, VİOP, BAP, TPP ve SWAP piyasalarında MKT\'dir; ancak Kıymetli Madenler ve Taşlar Piyasası\'nda (KMTP) MKT DEĞİLDİR!'
  }
];

export const CheatSheetPage: React.FC<CheatSheetPageProps> = ({ onNavigate }) => {
  const [activeTab, setActiveTab] = useState<'all' | 'durations' | 'ratios' | 'comparisons' | 'traps' | 'diagnoses'>('all');
  const [moduleFilter, setModuleFilter] = useState<ModuleId | 'all'>('all');
  const [searchQuery, setSearchQuery] = useState<string>('');
  const [showAllInAllTab, setShowAllInAllTab] = useState<boolean>(false);

  const normalizedQuery = searchQuery.trim().toLowerCase();

  const filterItem = (text: string, modId: ModuleId) => {
    const matchesModule = moduleFilter === 'all' || moduleFilter === modId;
    const matchesSearch = !normalizedQuery || text.toLowerCase().includes(normalizedQuery);
    return matchesModule && matchesSearch;
  };

  const filteredDurations = useMemo(
    () => DURATIONS.filter((d) => filterItem(`${d.duration} ${d.title} ${d.description} ${d.trap}`, d.moduleId)),
    [moduleFilter, normalizedQuery]
  );

  const filteredRatios = useMemo(
    () => RATIOS.filter((r) => filterItem(`${r.value} ${r.title} ${r.description} ${r.trap}`, r.moduleId)),
    [moduleFilter, normalizedQuery]
  );

  const filteredComparisons = useMemo(
    () => COMPARISONS.filter((c) => filterItem(`${c.conceptA.title} ${c.conceptB.title} ${c.differenceRule}`, c.moduleId)),
    [moduleFilter, normalizedQuery]
  );

  const filteredTraps = useMemo(
    () => TRAPS.filter((t) => filterItem(`${t.myth} ${t.reality} ${t.whyImportant}`, t.moduleId)),
    [moduleFilter, normalizedQuery]
  );

  const filteredDiagnoses = useMemo(
    () => DIAGNOSES.filter((d) => filterItem(`${d.scenarioEvent} ${d.legalDiagnosis} ${d.applicableLaw} ${d.consequenceOrPenalty} ${d.examTrap}`, d.moduleId)),
    [moduleFilter, normalizedQuery]
  );

  const shouldCapAllTab = activeTab === 'all' && !showAllInAllTab && !normalizedQuery && moduleFilter === 'all';
  const visibleDurations = shouldCapAllTab ? filteredDurations.slice(0, 9) : filteredDurations;
  const visibleRatios = shouldCapAllTab ? filteredRatios.slice(0, 9) : filteredRatios;
  const visibleComparisons = shouldCapAllTab ? filteredComparisons.slice(0, 6) : filteredComparisons;
  const visibleTraps = shouldCapAllTab ? filteredTraps.slice(0, 6) : filteredTraps;
  const visibleDiagnoses = shouldCapAllTab ? filteredDiagnoses.slice(0, 6) : filteredDiagnoses;

  const filteredTotal = filteredDurations.length + filteredRatios.length + filteredComparisons.length + filteredTraps.length + filteredDiagnoses.length;
  const [isGeneratingPdf, setIsGeneratingPdf] = useState<boolean>(false);
  const packagedScope = moduleFilter === 'all' ? 'all' : moduleFilter;
  const canUsePackagedPdf = activeTab === 'all' && searchQuery.trim() === '';

  const handleDownloadPdf = async (scope: 'all' | 'filtered' = 'all') => {
    setIsGeneratingPdf(true);
    try {
      const { downloadCheatSheetPdf, downloadPackagedCheatSheetPdf } = await import(
        '../utils/cheatSheetPdfGenerator'
      );
      if (scope === 'all' && canUsePackagedPdf) {
        downloadPackagedCheatSheetPdf(packagedScope);
        return;
      }
      if (scope === 'all') {
        await downloadCheatSheetPdf({
          durations: DURATIONS,
          ratios: RATIOS,
          comparisons: COMPARISONS,
          traps: TRAPS,
          title: 'SPK SERMAYE PİYASASI FAALİYETLERİ DÜZEY 1',
          filterTitle: 'Tüm Müfredat ve 4 Temel Modül (1001, 1003, 1005, 1012) - 249 Altın Hap Bilgi ve Vaka Teşhisi',
        });
      } else {
        const moduleNameMap: Record<string, string> = {
          all: 'Tüm Dersler',
          '1001': '1001 Sermaye Piyasası Mevzuatı',
          '1003': '1003 Sermaye Piyasası Araçları 1',
          '1005': '1005 Yatırım Kuruluşları',
          '1012': '1012 Takas, Saklama ve Operasyon',
        };
        const currentModule = moduleNameMap[moduleFilter] || moduleFilter;
        const searchDesc = searchQuery.trim() ? ` / Arama: "${searchQuery.trim()}"` : '';
        const categoryMap: Record<string, string> = {
          all: 'Tüm Kategoriler',
          durations: 'Kanuni Süreler',
          ratios: 'Kritik Eşikler ve Rakamlar',
          comparisons: 'Karıştırılan İkili Kavramlar',
          traps: 'Ölümcül Sınav Tuzakları',
        };
        const catTitle = categoryMap[activeTab] || activeTab;
        await downloadCheatSheetPdf({
          durations: activeTab === 'all' || activeTab === 'durations' ? filteredDurations : [],
          ratios: activeTab === 'all' || activeTab === 'ratios' ? filteredRatios : [],
          comparisons: activeTab === 'all' || activeTab === 'comparisons' ? filteredComparisons : [],
          traps: activeTab === 'all' || activeTab === 'traps' ? filteredTraps : [],
          title: 'SPK SERMAYE PİYASASI FAALİYETLERİ DÜZEY 1',
          filterTitle: `Özel Filtre: ${currentModule} • ${catTitle}${searchDesc} (${filteredTotal} Madde)`,
        });
      }
    } catch (err) {
      console.error('PDF indirme hatası:', err);
    } finally {
      setIsGeneratingPdf(false);
    }
  };

  const handleOpenPreview = async () => {
    if (canUsePackagedPdf) {
      const { openPackagedCheatSheetPdf } = await import('../utils/cheatSheetPdfGenerator');
      openPackagedCheatSheetPdf(packagedScope);
      return;
    }
    await handleDownloadPdf('filtered');
  };

  return (
    <div className="space-y-8 animate-fadeIn pb-16">
      {/* Header Banner */}
      <div className="relative overflow-hidden rounded-2xl sm:rounded-3xl bg-white dark:bg-fintech-surface border border-amber-200 dark:border-amber-500/30 p-4 sm:p-6 shadow-sm">
        <div className="relative z-10 flex flex-col md:flex-row items-start md:items-center justify-between gap-4">
          <div className="space-y-1.5 max-w-2xl">
            <div className="inline-flex items-center gap-1.5 px-2.5 py-0.5 rounded-full bg-amber-100 dark:bg-amber-500/20 border border-amber-300 dark:border-amber-500/40 text-amber-900 dark:text-amber-300 text-[11px] font-mono font-bold">
              <Zap className="w-3 h-3 fill-amber-500 text-amber-600" />
              <span>HIZLI TEKRAR • 249 ALTIN HAP BİLGİ</span>
            </div>
            <h1 className="text-xl sm:text-2xl font-black text-slate-900 dark:text-white tracking-tight">
              Sınavın Altın Eşikleri, Süreleri ve Karşılaştırmaları
            </h1>
            <p className="hidden sm:block text-xs text-slate-600 dark:text-slate-300 leading-relaxed">
              58 kanuni süre, 56 kritik oran/sayı, 48 ikili kavram ayrımı, 39 sınav tuzağı ve 48 vaka teşhisi.
            </p>
          </div>

          {/* Quick Actions */}
          <div className="flex flex-wrap items-center gap-2 shrink-0 w-full md:w-auto">
            <button
              onClick={() => onNavigate('exam-morning')}
              className="flex-1 md:flex-initial flex items-center justify-center gap-1.5 px-3.5 py-2.5 rounded-xl bg-gradient-to-r from-amber-500 to-rose-500 hover:from-amber-600 hover:to-rose-600 text-white text-xs font-black shadow-xs transition-all active:scale-95 cursor-pointer"
            >
              <Zap className="w-3.5 h-3.5 fill-white text-white" />
              <span>Sınav Sabahı (15 Dk)</span>
            </button>

            <button
              onClick={() => handleDownloadPdf('all')}
              disabled={isGeneratingPdf}
              className="flex-1 md:flex-initial flex items-center justify-center gap-1.5 px-3.5 py-2.5 rounded-xl bg-teal-600 hover:bg-teal-700 text-white text-xs font-bold shadow-xs transition-all active:scale-95 disabled:opacity-60 cursor-pointer"
            >
              {isGeneratingPdf ? (
                <Loader2 className="w-3.5 h-3.5 text-white animate-spin" />
              ) : (
                <Download className="w-3.5 h-3.5 text-white" />
              )}
              <span>{isGeneratingPdf ? 'Hazırlanıyor...' : 'PDF İndir (249)'}</span>
            </button>
          </div>
        </div>
      </div>

      {/* Control Bar: Filters & Search */}
      <div className="bg-white dark:bg-fintech-surface rounded-2xl border border-slate-200 dark:border-fintech-border p-3 sm:p-4 space-y-3 shadow-sm">
        {/* Category Tabs */}
        <div className="flex items-center gap-2 overflow-x-auto pb-2 border-b border-slate-100 dark:border-fintech-border/60">
          <button
            onClick={() => setActiveTab('all')}
            className={`shrink-0 px-3 py-1.5 rounded-xl text-xs font-bold transition-all cursor-pointer ${
              activeTab === 'all'
                ? 'bg-teal-600 text-white shadow-sm'
                : 'text-slate-700 dark:text-slate-300 hover:text-slate-950 dark:hover:text-white hover:bg-slate-100 dark:hover:bg-fintech-card'
            }`}
          >
            Tümü ({DURATIONS.length + RATIOS.length + COMPARISONS.length + TRAPS.length + DIAGNOSES.length})
          </button>
          <button
            onClick={() => setActiveTab('durations')}
            className={`shrink-0 flex items-center gap-1.5 px-3 py-1.5 rounded-xl text-xs font-bold transition-all cursor-pointer ${
              activeTab === 'durations'
                ? 'bg-amber-500 text-slate-950 shadow-sm'
                : 'text-slate-700 dark:text-slate-300 hover:text-slate-950 dark:hover:text-white hover:bg-slate-100 dark:hover:bg-fintech-card'
            }`}
          >
            <Clock className="w-3.5 h-3.5" />
            <span>Süreler ({DURATIONS.length})</span>
          </button>
          <button
            onClick={() => setActiveTab('ratios')}
            className={`shrink-0 flex items-center gap-1.5 px-3 py-1.5 rounded-xl text-xs font-bold transition-all cursor-pointer ${
              activeTab === 'ratios'
                ? 'bg-emerald-600 text-white shadow-sm'
                : 'text-slate-700 dark:text-slate-300 hover:text-slate-950 dark:hover:text-white hover:bg-slate-100 dark:hover:bg-fintech-card'
            }`}
          >
            <Percent className="w-3.5 h-3.5" />
            <span>Oranlar ({RATIOS.length})</span>
          </button>
          <button
            onClick={() => setActiveTab('comparisons')}
            className={`shrink-0 flex items-center gap-1.5 px-3 py-1.5 rounded-xl text-xs font-bold transition-all cursor-pointer ${
              activeTab === 'comparisons'
                ? 'bg-purple-600 text-white shadow-sm'
                : 'text-slate-700 dark:text-slate-300 hover:text-slate-950 dark:hover:text-white hover:bg-slate-100 dark:hover:bg-fintech-card'
            }`}
          >
            <Scale className="w-3.5 h-3.5" />
            <span>Karşılaştırmalar ({COMPARISONS.length})</span>
          </button>
          <button
            onClick={() => setActiveTab('traps')}
            className={`shrink-0 flex items-center gap-1.5 px-3 py-1.5 rounded-xl text-xs font-bold transition-all cursor-pointer ${
              activeTab === 'traps'
                ? 'bg-rose-600 text-white shadow-sm'
                : 'text-slate-700 dark:text-slate-300 hover:text-slate-950 dark:hover:text-white hover:bg-slate-100 dark:hover:bg-fintech-card'
            }`}
          >
            <AlertTriangle className="w-3.5 h-3.5" />
            <span>Tuzaklar ({TRAPS.length})</span>
          </button>
          <button
            onClick={() => setActiveTab('diagnoses')}
            className={`shrink-0 flex items-center gap-1.5 px-3 py-1.5 rounded-xl text-xs font-bold transition-all cursor-pointer ${
              activeTab === 'diagnoses'
                ? 'bg-indigo-600 text-white shadow-sm'
                : 'text-slate-700 dark:text-slate-300 hover:text-slate-950 dark:hover:text-white hover:bg-slate-100 dark:hover:bg-fintech-card'
            }`}
          >
            <Brain className="w-3.5 h-3.5" />
            <span>Vaka Teşhisi ({DIAGNOSES.length})</span>
          </button>
        </div>

        {/* Second Row: Module Select & Search Input */}
        <div className="flex flex-col sm:flex-row items-center justify-between gap-3">
          {/* Module Pills */}
          <div className="flex flex-wrap items-center gap-1.5 w-full sm:w-auto">
            <span className="text-[11px] font-mono text-slate-500 dark:text-slate-400 uppercase mr-1 font-semibold">Ders:</span>
            {[
              { id: 'all', label: 'Tüm Dersler' },
              { id: '1001', label: '1001 Mevzuat' },
              { id: '1003', label: '1003 Araçlar' },
              { id: '1005', label: '1005 Kuruluşlar' },
              { id: '1012', label: '1012 Takas' }
            ].map(m => (
              <button
                key={m.id}
                onClick={() => setModuleFilter(m.id as any)}
                className={`px-2.5 py-1 rounded-lg text-xs font-medium transition-all ${
                  moduleFilter === m.id
                    ? 'bg-teal-50 dark:bg-fintech-border text-teal-900 dark:text-teal-300 font-bold border border-teal-300 dark:border-teal-500/40 shadow-xs'
                    : 'text-slate-600 dark:text-slate-400 hover:text-slate-900 dark:hover:text-slate-200'
                }`}
              >
                {m.label}
              </button>
            ))}
          </div>

          {/* Search Box */}
          <div className="relative w-full sm:w-64">
            <Search className="absolute left-3 top-2.5 w-3.5 h-3.5 text-slate-400" />
            <input
              type="text"
              value={searchQuery}
              onChange={(e) => setSearchQuery(e.target.value)}
              placeholder="Eşik, oran veya süre ara (örn: %98, 15 gün)..."
              className="w-full bg-slate-50 dark:bg-fintech-card border border-slate-200 dark:border-fintech-border rounded-xl pl-9 pr-3 py-1.5 text-xs text-slate-900 dark:text-slate-200 placeholder-slate-400 dark:placeholder-slate-500 focus:outline-none focus:border-teal-500 transition-colors"
            />
          </div>
        </div>
      </div>

      {/* SECTION 1: DURATION CARDS */}
      {(activeTab === 'all' || activeTab === 'durations') && filteredDurations.length > 0 && (
        <div className="space-y-4">
          <div className="flex items-center justify-between border-b border-slate-200 dark:border-fintech-border/70 pb-2">
            <div className="flex items-center gap-2">
              <Clock className="w-5 h-5 text-amber-500 dark:text-amber-400" />
              <h2 className="text-lg font-black text-slate-900 dark:text-white">⏱️ Kanuni Süreler, Günler ve Valörler</h2>
              <span className="text-xs font-mono text-slate-500 dark:text-slate-400">({filteredDurations.length} Eşik)</span>
            </div>
            {shouldCapAllTab && (
              <button
                onClick={() => setActiveTab('durations')}
                className="text-xs font-bold text-amber-600 dark:text-amber-400 hover:underline cursor-pointer"
              >
                Tümünü Gör ({filteredDurations.length}) →
              </button>
            )}
          </div>

          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
            {visibleDurations.map((item) => (
              <div 
                key={item.id}
                className="bg-white dark:bg-fintech-surface rounded-2xl border border-amber-200 dark:border-amber-500/30 p-5 space-y-3 shadow-sm hover:border-amber-400 dark:hover:border-amber-500/60 transition-all flex flex-col justify-between"
              >
                <div className="space-y-2">
                  <div className="flex items-center justify-between gap-2">
                    <span className="px-3 py-1 rounded-xl bg-amber-100 dark:bg-amber-500/20 border border-amber-300 dark:border-amber-500/40 text-amber-900 dark:text-amber-300 font-mono text-sm font-black tracking-wide">
                      {item.duration}
                    </span>
                    <span className="text-[10px] font-mono text-slate-600 dark:text-slate-400 bg-slate-100 dark:bg-fintech-card px-2 py-0.5 rounded-md border border-slate-200 dark:border-fintech-border">
                      Modül {item.moduleId}
                    </span>
                  </div>
                  <h3 className="text-sm font-bold text-slate-900 dark:text-white leading-snug">
                    {item.title}
                  </h3>
                  <p className="text-xs text-slate-600 dark:text-slate-300 leading-relaxed">
                    {item.description}
                  </p>
                </div>

                <div className="p-2.5 rounded-xl bg-amber-50 dark:bg-amber-950/30 border border-amber-200 dark:border-amber-500/20 text-[11px] text-slate-800 dark:text-amber-200/90 leading-relaxed">
                  <span className="font-bold text-amber-700 dark:text-amber-400 block mb-0.5">⚠️ Sınav Notu / Çeldirici:</span>
                  {item.trap}
                </div>
              </div>
            ))}
          </div>
        </div>
      )}

      {/* SECTION 2: RATIOS & THRESHOLDS */}
      {(activeTab === 'all' || activeTab === 'ratios') && filteredRatios.length > 0 && (
        <div className="space-y-4">
          <div className="flex items-center justify-between border-b border-slate-200 dark:border-fintech-border/70 pb-2">
            <div className="flex items-center gap-2">
              <Percent className="w-5 h-5 text-emerald-600 dark:text-emerald-400" />
              <h2 className="text-lg font-black text-slate-900 dark:text-white">📊 Kritik Yüzdeler, Oranlar ve Parasal Eşikler</h2>
              <span className="text-xs font-mono text-slate-500 dark:text-slate-400">({filteredRatios.length} Eşik)</span>
            </div>
            {shouldCapAllTab && (
              <button
                onClick={() => setActiveTab('ratios')}
                className="text-xs font-bold text-emerald-600 dark:text-emerald-400 hover:underline cursor-pointer"
              >
                Tümünü Gör ({filteredRatios.length}) →
              </button>
            )}
          </div>

          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
            {visibleRatios.map((item) => (
              <div 
                key={item.id}
                className="bg-white dark:bg-fintech-surface rounded-2xl border border-emerald-200 dark:border-emerald-500/30 p-5 space-y-3 shadow-sm hover:border-emerald-400 dark:hover:border-emerald-500/60 transition-all flex flex-col justify-between"
              >
                <div className="space-y-2">
                  <div className="flex items-center justify-between gap-2">
                    <span className="px-3 py-1 rounded-xl bg-emerald-100 dark:bg-emerald-500/20 border border-emerald-300 dark:border-emerald-500/40 text-emerald-900 dark:text-emerald-300 font-mono text-sm font-black tracking-wide">
                      {item.value}
                    </span>
                    <span className="text-[10px] font-mono text-slate-600 dark:text-slate-400 bg-slate-100 dark:bg-fintech-card px-2 py-0.5 rounded-md border border-slate-200 dark:border-fintech-border">
                      Modül {item.moduleId}
                    </span>
                  </div>
                  <h3 className="text-sm font-bold text-slate-900 dark:text-white leading-snug">
                    {item.title}
                  </h3>
                  <p className="text-xs text-slate-600 dark:text-slate-300 leading-relaxed">
                    {item.description}
                  </p>
                </div>

                <div className="p-2.5 rounded-xl bg-emerald-50 dark:bg-emerald-950/30 border border-emerald-200 dark:border-emerald-500/20 text-[11px] text-slate-800 dark:text-emerald-200/90 leading-relaxed">
                  <span className="font-bold text-emerald-700 dark:text-emerald-400 block mb-0.5">⚠️ Sınav Notu:</span>
                  {item.trap}
                </div>
              </div>
            ))}
          </div>
        </div>
      )}

      {/* SECTION 3: COMPARISON CARDS */}
      {(activeTab === 'all' || activeTab === 'comparisons') && filteredComparisons.length > 0 && (
        <div className="space-y-4">
          <div className="flex items-center justify-between border-b border-slate-200 dark:border-fintech-border/70 pb-2">
            <div className="flex items-center gap-2">
              <Scale className="w-5 h-5 text-purple-600 dark:text-purple-400" />
              <h2 className="text-lg font-black text-slate-900 dark:text-white">⚖️ Sınavda En Çok Karıştırılan İkili Kavramlar</h2>
              <span className="text-xs font-mono text-slate-500 dark:text-slate-400">({filteredComparisons.length} İkili)</span>
            </div>
            {shouldCapAllTab && (
              <button
                onClick={() => setActiveTab('comparisons')}
                className="text-xs font-bold text-purple-600 dark:text-purple-400 hover:underline cursor-pointer"
              >
                Tümünü Gör ({filteredComparisons.length}) →
              </button>
            )}
          </div>

          <div className="space-y-4">
            {visibleComparisons.map((item) => (
              <div 
                key={item.id}
                className="bg-white dark:bg-fintech-surface rounded-2xl border border-purple-200 dark:border-purple-500/30 p-5 sm:p-6 space-y-4 shadow-sm"
              >
                <div className="flex items-center justify-between">
                  <span className="text-xs font-mono text-purple-800 dark:text-purple-400 font-bold uppercase">
                    Karşılaştırma Analizi • Modül {item.moduleId}
                  </span>
                </div>

                <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
                  {/* Concept A */}
                  <div className="p-4 rounded-xl bg-purple-50/70 dark:bg-purple-950/20 border border-purple-200 dark:border-purple-500/30 space-y-2">
                    <h4 className="text-sm font-black text-purple-950 dark:text-purple-200">{item.conceptA.title}</h4>
                    <p className="text-xs text-slate-700 dark:text-slate-300 leading-relaxed">{item.conceptA.desc}</p>
                    <div className="text-[11px] font-mono text-purple-900 dark:text-purple-300 bg-purple-100/80 dark:bg-purple-950/40 p-2 rounded-lg font-semibold">
                      🔑 {item.conceptA.keyPoint}
                    </div>
                  </div>

                  {/* Concept B */}
                  <div className="p-4 rounded-xl bg-purple-50/70 dark:bg-purple-950/20 border border-purple-200 dark:border-purple-500/30 space-y-2">
                    <h4 className="text-sm font-black text-purple-950 dark:text-purple-200">{item.conceptB.title}</h4>
                    <p className="text-xs text-slate-700 dark:text-slate-300 leading-relaxed">{item.conceptB.desc}</p>
                    <div className="text-[11px] font-mono text-purple-900 dark:text-purple-300 bg-purple-100/80 dark:bg-purple-950/40 p-2 rounded-lg font-semibold">
                      🔑 {item.conceptB.keyPoint}
                    </div>
                  </div>
                </div>

                {/* Golden Difference Rule */}
                <div className="p-3.5 rounded-xl bg-purple-50 dark:bg-gradient-to-r dark:from-purple-900/30 dark:to-slate-900/40 border border-purple-200 dark:border-purple-500/40 text-xs text-purple-950 dark:text-purple-100 flex items-start gap-2.5">
                  <CheckCircle2 className="w-4 h-4 text-purple-600 dark:text-purple-400 shrink-0 mt-0.5" />
                  <div>
                    <span className="font-bold text-purple-900 dark:text-purple-300 block mb-0.5">Altın Ayrım Kuralı:</span>
                    <span className="leading-relaxed">{item.differenceRule}</span>
                  </div>
                </div>
              </div>
            ))}
          </div>
        </div>
      )}

      {/* SECTION 4: EXAM TRAPS */}
      {(activeTab === 'all' || activeTab === 'traps') && filteredTraps.length > 0 && (
        <div className="space-y-4">
          <div className="flex items-center justify-between border-b border-slate-200 dark:border-fintech-border/70 pb-2">
            <div className="flex items-center gap-2">
              <AlertTriangle className="w-5 h-5 text-rose-600 dark:text-rose-400" />
              <h2 className="text-lg font-black text-slate-900 dark:text-white">🚨 Ölümcül Sınav Tuzakları (Doğru Bilinen Yanlışlar)</h2>
              <span className="text-xs font-mono text-slate-500 dark:text-slate-400">({filteredTraps.length} Altın Kural)</span>
            </div>
            {shouldCapAllTab && (
              <button
                onClick={() => setActiveTab('traps')}
                className="text-xs font-bold text-rose-600 dark:text-rose-400 hover:underline cursor-pointer"
              >
                Tümünü Gör ({filteredTraps.length}) →
              </button>
            )}
          </div>

          <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
            {visibleTraps.map((item) => (
              <div 
                key={item.id}
                className="bg-white dark:bg-fintech-surface rounded-2xl border border-rose-200 dark:border-rose-500/30 p-5 space-y-3.5 shadow-sm flex flex-col justify-between"
              >
                <div className="space-y-3">
                  <div className="flex items-center justify-between">
                    <span className="text-[10px] font-mono text-rose-700 dark:text-rose-400 bg-rose-50 dark:bg-rose-950/40 border border-rose-200 dark:border-rose-500/30 px-2 py-0.5 rounded-md font-bold">
                      Tuzak • Modül {item.moduleId}
                    </span>
                  </div>

                  {/* Myth */}
                  <div className="p-3 rounded-xl bg-rose-50 dark:bg-rose-950/30 border border-rose-200 dark:border-rose-500/30 text-xs text-rose-950 dark:text-rose-200">
                    <span className="font-bold text-rose-700 dark:text-rose-400 block mb-1">❌ Sınavda Çeldirici Olarak Yazılan (YANLIŞ):</span>
                    <span className="leading-relaxed">"{item.myth}"</span>
                  </div>

                  {/* Reality */}
                  <div className="p-3 rounded-xl bg-emerald-50 dark:bg-emerald-950/30 border border-emerald-200 dark:border-emerald-500/30 text-xs text-emerald-950 dark:text-emerald-200">
                    <span className="font-bold text-emerald-700 dark:text-emerald-400 block mb-1">✅ Kanuni Gerçek (DOĞRU):</span>
                    <span className="leading-relaxed">{item.reality}</span>
                  </div>
                </div>

                <div className="text-[11px] text-slate-600 dark:text-slate-400 italic">
                  💡 {item.whyImportant}
                </div>
              </div>
            ))}
          </div>
        </div>
      )}

      {/* SECTION 5: SCENARIO DIAGNOSES (MAARİF MODELİ VAKA TEŞHİSİ) */}
      {(activeTab === 'all' || activeTab === 'diagnoses') && filteredDiagnoses.length > 0 && (
        <div className="space-y-4">
          <div className="flex items-center justify-between border-b border-slate-200 dark:border-fintech-border/70 pb-2">
            <div className="flex items-center gap-2">
              <Brain className="w-5 h-5 text-indigo-600 dark:text-indigo-400" />
              <h2 className="text-lg font-black text-slate-900 dark:text-white">🧠 Maarif Modeli: Vaka Teşhis & Hukuki Nitelendirme Matrisi</h2>
              <span className="text-xs font-mono text-slate-500 dark:text-slate-400">({filteredDiagnoses.length} Somut Olay)</span>
            </div>
            {shouldCapAllTab && (
              <button
                onClick={() => setActiveTab('diagnoses')}
                className="text-xs font-bold text-indigo-600 dark:text-indigo-400 hover:underline cursor-pointer"
              >
                Tümünü Gör ({filteredDiagnoses.length}) →
              </button>
            )}
          </div>

          <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
            {visibleDiagnoses.map((item) => (
              <div 
                key={item.id}
                className="bg-white dark:bg-fintech-surface rounded-2xl border border-indigo-200 dark:border-indigo-500/30 p-5 space-y-3.5 shadow-sm hover:border-indigo-400 dark:hover:border-indigo-500/60 transition-all flex flex-col justify-between"
              >
                <div className="space-y-3">
                  <div className="flex items-center justify-between gap-2">
                    <span className="px-2.5 py-1 rounded-xl bg-indigo-100 dark:bg-indigo-500/20 border border-indigo-300 dark:border-indigo-500/40 text-indigo-900 dark:text-indigo-300 font-mono text-xs font-bold">
                      {item.applicableLaw}
                    </span>
                    <span className="text-[10px] font-mono text-slate-600 dark:text-slate-400 bg-slate-100 dark:bg-fintech-card px-2 py-0.5 rounded-md border border-slate-200 dark:border-fintech-border">
                      Modül {item.moduleId}
                    </span>
                  </div>

                  <div className="space-y-1">
                    <span className="text-[10px] font-mono uppercase text-indigo-600 dark:text-indigo-400 font-bold block">
                      📌 Somut Finansal Olay / Senaryo:
                    </span>
                    <p className="text-xs text-slate-800 dark:text-slate-200 font-medium leading-relaxed bg-slate-50 dark:bg-fintech-card/60 p-2.5 rounded-xl border border-slate-200 dark:border-fintech-border/60">
                      {item.scenarioEvent}
                    </p>
                  </div>

                  <div className="grid grid-cols-1 sm:grid-cols-2 gap-2 text-xs">
                    <div className="p-2.5 rounded-xl bg-teal-50 dark:bg-teal-950/20 border border-teal-200 dark:border-teal-500/30">
                      <span className="font-bold text-teal-900 dark:text-teal-300 block text-[11px] mb-0.5">🎯 Hukuki Teşhis:</span>
                      <span className="text-slate-800 dark:text-slate-200 font-semibold">{item.legalDiagnosis}</span>
                    </div>
                    <div className="p-2.5 rounded-xl bg-purple-50 dark:bg-purple-950/20 border border-purple-200 dark:border-purple-500/30">
                      <span className="font-bold text-purple-900 dark:text-purple-300 block text-[11px] mb-0.5">⚖️ Hukuki Sonuç / Yaptırım:</span>
                      <span className="text-slate-800 dark:text-slate-200">{item.consequenceOrPenalty}</span>
                    </div>
                  </div>
                </div>

                <div className="p-2.5 rounded-xl bg-amber-50 dark:bg-amber-950/30 border border-amber-200 dark:border-amber-500/20 text-[11px] text-slate-800 dark:text-amber-200/90 leading-relaxed">
                  <span className="font-bold text-amber-700 dark:text-amber-400 block mb-0.5">⚠️ Sınav Çeldiricisi & Komisyon Hilesi:</span>
                  {item.examTrap}
                </div>
              </div>
            ))}
          </div>
        </div>
      )}

      {shouldCapAllTab && (
        <div className="flex justify-center pt-2">
          <button
            onClick={() => setShowAllInAllTab(true)}
            className="px-6 py-3 rounded-2xl bg-slate-900 dark:bg-white text-white dark:text-slate-950 font-black text-xs sm:text-sm shadow-md hover:opacity-90 active:scale-95 transition-all cursor-pointer"
          >
            Tüm 249 Hap Bilgi Kartını Tek Sayfada Göster
          </button>
        </div>
      )}


      {/* Empty State */}
      {filteredDurations.length === 0 && filteredRatios.length === 0 && filteredComparisons.length === 0 && filteredTraps.length === 0 && filteredDiagnoses.length === 0 && (
        <div className="bg-white dark:bg-fintech-surface rounded-2xl border border-slate-200 dark:border-fintech-border p-12 text-center text-slate-500 dark:text-slate-400 space-y-3 shadow-sm">
          <HelpCircle className="w-8 h-8 text-slate-400 dark:text-slate-500 mx-auto" />
          <p className="text-sm font-medium">Arama kriterinize uygun hap bilgi bulunamadı.</p>
        </div>
      )}

      {/* Bottom Sticky Ready Bar */}
      <div className="rounded-2xl bg-gradient-to-r from-teal-50 via-slate-50 to-white dark:from-teal-500/10 dark:via-fintech-card dark:to-slate-900 border border-teal-200 dark:border-teal-500/30 p-6 flex flex-col sm:flex-row items-center justify-between gap-4 shadow-sm">
        <div>
          <h4 className="text-sm font-black text-slate-900 dark:text-white">Sınav Bilgilerini Tazeledin mi?</h4>
          <p className="text-xs text-slate-600 dark:text-slate-400">249 altın hap bilgiyi PDF olarak saklayabilir veya çözülmemiş sorularla hemen pratik yapabilirsin.</p>
        </div>

        <div className="grid grid-cols-1 sm:grid-cols-2 lg:flex items-center gap-2.5 w-full lg:w-auto">
          <button
            onClick={() => handleDownloadPdf('all')}
            disabled={isGeneratingPdf}
            className="flex-1 sm:flex-initial flex items-center justify-center gap-2 px-4 py-2.5 rounded-xl bg-teal-600 hover:bg-teal-700 active:bg-teal-800 text-white text-xs font-bold transition-all shadow-sm disabled:opacity-60 cursor-pointer"
          >
            {isGeneratingPdf ? <Loader2 className="w-4 h-4 text-white animate-spin" /> : <Download className="w-4 h-4 text-white" />}
            <span className="text-white font-bold">{isGeneratingPdf ? 'PDF Hazırlanıyor...' : 'PDF İndir (249 Madde)'}</span>
          </button>
          <button
            onClick={handleOpenPreview}
            className="flex-1 sm:flex-initial flex items-center justify-center gap-2 px-4 py-2.5 rounded-xl bg-white dark:bg-fintech-surface border border-slate-300 dark:border-fintech-border text-slate-800 dark:text-slate-100 hover:bg-slate-50 dark:hover:bg-fintech-card text-xs font-bold transition-all shadow-sm cursor-pointer"
          >
            <Printer className="w-4 h-4 text-teal-600 dark:text-teal-400" />
            <span>PDF Önizle / İndir</span>
          </button>
          <button
            onClick={() => onNavigate('practice', { filterMode: 'unseen' })}
            className="flex-1 sm:flex-initial flex items-center justify-center gap-2 px-4 py-2.5 rounded-xl bg-amber-500 hover:bg-amber-600 text-slate-950 text-xs font-bold transition-all shadow-sm cursor-pointer"
          >
            <Play className="w-3.5 h-3.5 fill-slate-950 text-slate-950" />
            <span className="text-slate-950 font-bold">Çözülmemiş Soruları Çöz</span>
          </button>
          <button
            onClick={() => onNavigate('practice')}
            className="flex-1 sm:flex-initial flex items-center justify-center gap-2 px-5 py-2.5 rounded-xl bg-teal-600 hover:bg-teal-700 text-white text-xs font-black shadow-md shadow-teal-700/20 transition-all cursor-pointer"
          >
            <span className="text-white font-bold">Rastgele Test Başlat (1.135)</span>
          </button>
        </div>
      </div>
    </div>
  );
};
