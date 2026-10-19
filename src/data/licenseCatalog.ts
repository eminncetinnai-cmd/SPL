export interface LicenseCatalogEntry {
  name: string;
  education: string;
  subjects: string[];
  note?: string;
}

const SUBJECTS = {
  mevzuatDar: '1001 DAR KAPSAMLI SERMAYE PİYASASI MEVZUATI VE MESLEK KURALLARI',
  mevzuatGenis: '1001 GENİŞ KAPSAMLI SERMAYE PİYASASI MEVZUATI VE MESLEK KURALLARI',
  araclar1: '1003 SERMAYE PİYASASI ARAÇLARI 1',
  araclar2: '1007 SERMAYE PİYASASI ARAÇLARI 2',
  yatirim: '1005 YATIRIM KURULUŞLARI',
  finansalPiyasalar: '1006 FİNANSAL PİYASALAR',
  takas: '1012 TAKAS SAKLAMA VE OPERASYON İŞLEMLERİ',
  finansalYonetim: '1011 FİNANSAL YÖNETİM VE MALİ ANALİZ',
  ticaret: '1010 TİCARET HUKUKU',
  muhasebe: '1009 MUHASEBE VE FİNANSAL RAPORLAMA',
  ekonomi: '1002 GENEL EKONOMİ',
  finansMatematik: '1004 TEMEL FİNANS MATEMATİĞİ VE DEĞERLEME YÖNTEMLERİ',
  vergilendirme: '1008 KURUMLARDA VE SERMAYE PİYASASINDA VERGİLENDİRME',
  turev: '1013 TÜREV ARAÇLAR PİYASALARI VE RİSK YÖNETİMİ',
} as const;

export const LICENSE_CATALOG: LicenseCatalogEntry[] = [
  {
    name: 'Sermaye Piyasası Faaliyetleri Düzey 1 Lisansı',
    education: 'En az 2 yıllık yükseköğretim mezuniyeti',
    subjects: [SUBJECTS.mevzuatDar, SUBJECTS.araclar1, SUBJECTS.yatirim, SUBJECTS.takas],
  },
  {
    name: 'Sermaye Piyasası Faaliyetleri Düzey 2 Lisansı',
    education: 'En az 4 yıllık yükseköğretim mezuniyeti',
    subjects: [
      SUBJECTS.mevzuatGenis,
      SUBJECTS.araclar1,
      SUBJECTS.araclar2,
      SUBJECTS.yatirim,
      SUBJECTS.finansalPiyasalar,
      SUBJECTS.takas,
      SUBJECTS.finansalYonetim,
      SUBJECTS.ticaret,
      SUBJECTS.muhasebe,
    ],
    note: 'Düzey 2 lisansı, Düzey 1 lisansının gerekli olduğu unvan ve görevlerde çalışabilme imkânı sağlar.',
  },
  {
    name: 'Sermaye Piyasası Faaliyetleri Düzey 3 Lisansı',
    education: 'En az 4 yıllık yükseköğretim mezuniyeti',
    subjects: [
      SUBJECTS.mevzuatGenis,
      SUBJECTS.araclar1,
      SUBJECTS.araclar2,
      SUBJECTS.yatirim,
      SUBJECTS.finansalPiyasalar,
      SUBJECTS.takas,
      SUBJECTS.finansalYonetim,
      SUBJECTS.ticaret,
      SUBJECTS.muhasebe,
      SUBJECTS.ekonomi,
      SUBJECTS.finansMatematik,
      SUBJECTS.vergilendirme,
    ],
    note: 'Düzey 3 lisansı, Düzey 2 ve Düzey 1 lisanslarının gerekli olduğu unvan ve görevleri kapsar.',
  },
  {
    name: 'Türev Araçlar Lisansı',
    education: 'En az 4 yıllık yükseköğretim mezuniyeti',
    subjects: [
      SUBJECTS.mevzuatGenis,
      SUBJECTS.araclar1,
      SUBJECTS.araclar2,
      SUBJECTS.yatirim,
      SUBJECTS.finansalPiyasalar,
      SUBJECTS.finansMatematik,
      SUBJECTS.turev,
      SUBJECTS.vergilendirme,
    ],
  },
  {
    name: 'Kredi Derecelendirme Lisansı',
    education: 'En az 4 yıllık yükseköğretim mezuniyeti',
    subjects: [
      SUBJECTS.mevzuatGenis,
      SUBJECTS.finansMatematik,
      SUBJECTS.ticaret,
      SUBJECTS.muhasebe,
      'Kredi Derecelendirmesi',
    ],
  },
  {
    name: 'Kurumsal Yönetim Derecelendirme Lisansı',
    education: 'En az 4 yıllık yükseköğretim mezuniyeti',
    subjects: [
      SUBJECTS.mevzuatGenis,
      SUBJECTS.finansMatematik,
      SUBJECTS.ticaret,
      SUBJECTS.muhasebe,
      'Kurumsal Yönetim',
    ],
  },
  {
    name: 'Konut Değerleme Lisansı',
    education: 'En az 2 yıllık yükseköğretim mezuniyeti',
    subjects: [SUBJECTS.mevzuatDar, 'Gayrimenkul Değerleme Esasları'],
  },
  {
    name: 'Gayrimenkul Değerleme Lisansı',
    education: 'En az 4 yıllık yükseköğretim mezuniyeti',
    subjects: [
      SUBJECTS.mevzuatDar,
      'Gayrimenkul Değerleme Esasları',
      'İnşaat ve Gayrimenkul Muhasebesi',
      'Gayrimenkul Mevzuatı',
    ],
    note: 'Gayrimenkul Değerleme Lisansı, Konut Değerleme Lisansının gerekli olduğu görevleri de kapsar.',
  },
  {
    name: 'Bilgi Sistemleri Bağımsız Denetim Lisansı',
    education: 'En az 4 yıllık yükseköğretim mezuniyeti',
    subjects: [
      SUBJECTS.mevzuatDar,
      'Bilgi Sistemleri Yönetimi ve Denetimi',
      'Bilgi Sistemleri Geliştirilmesi ve Uygulanması',
      'Bilgi Sistemleri İşletimi',
      'Bilgi Sistemleri Güvenliği',
    ],
  },
];
