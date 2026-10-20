import React, { useState } from 'react';
import { X, Calculator, Search, ChevronRight, Sparkles, AlertCircle } from 'lucide-react';

interface FormulaDrawerProps {
  isOpen: boolean;
  onClose: () => void;
}

interface FormulaItem {
  id: string;
  category: string;
  title: string;
  formula: string;
  variables: { name: string; desc: string }[];
  example: string;
  examTrap: string;
}

const FORMULAS: FormulaItem[] = [
  {
    id: 'bedelli',
    category: 'Sermaye Artırımı & Hisse',
    title: 'Bedelli Sermaye Artırımı & Rüçhan Kupon Değeri',
    formula: 'P_yeni = (P_eski + (B × R_fiyat)) / (1 + B)\nR_kupon = P_eski - P_yeni',
    variables: [
      { name: 'P_eski', desc: 'Bölünme öncesi hisse kapanış fiyatı' },
      { name: 'B', desc: 'Bedelli sermaye artırım oranı (örn. %100 = 1.0, %50 = 0.5)' },
      { name: 'R_fiyat', desc: 'Rüçhan hakkı kullanım fiyatı (genellikle 1.0 TL nominal)' },
      { name: 'R_kupon', desc: 'Rüçhan hakkı kuponunun teorik piyasa değeri' },
    ],
    example: 'P_eski = 10 TL, %100 Bedelli (B=1), R_fiyat = 1 TL ise:\nP_yeni = (10 + 1×1) / (1 + 1) = 11 / 2 = 5.50 TL\nRüçhan Kupon Değeri = 10 - 5.50 = 4.50 TL',
    examTrap: 'Kupon değeri P_eski - P_yeni farkıdır. Pay sahipleri bedelliye katılmasa bile rüçhan hakkını pazarda satarak sermaye kaybından korunur.',
  },
  {
    id: 'bedelli_bedelsiz',
    category: 'Sermaye Artırımı & Hisse',
    title: 'Bedelli + Bedelsiz Birlikte Artırım',
    formula: 'P_yeni = (P_eski + (B × R_fiyat)) / (1 + B + BD)',
    variables: [
      { name: 'BD', desc: 'Bedelsiz sermaye artırım oranı (örn. %100 = 1.0)' },
      { name: 'B', desc: 'Bedelli sermaye artırım oranı' },
    ],
    example: 'P_eski = 12 TL, %50 Bedelli (B=0.5, R=1 TL), %50 Bedelsiz (BD=0.5):\nP_yeni = (12 + 0.5×1) / (1 + 0.5 + 0.5) = 12.5 / 2 = 6.25 TL',
    examTrap: 'Payda kısmında hem 1 (mevcut hisse), hem bedelli oranı, hem de bedelsiz oranı toplanır.',
  },
  {
    id: 'temettu',
    category: 'Sermaye Artırımı & Hisse',
    title: 'Nakit Temettü Referans Fiyatı',
    formula: 'P_ref = P_kapanış - Brüt Temettü',
    variables: [
      { name: 'P_kapanış', desc: 'Hak kullanım tarihinden önceki son işlem gününün kapanış fiyatı' },
      { name: 'Brüt Temettü', desc: 'Hisse başına dağıtılacak vergi öncesi brüt nakit temettü' },
    ],
    example: 'P_kapanış = 45 TL, Hisse başı Brüt 3 TL nakit temettü ödendi:\nP_ref = 45 - 3 = 42 TL',
    examTrap: 'Soru metninde stopaj kesintisinden (net temettü) bahsedilse dahi fiyattan her zaman BRÜT temettü düşülür! Stopaj referans fiyata dahil edilmez.',
  },
  {
    id: 'kredili_islem',
    category: 'Kredili Alım & Açığa Satış',
    title: 'Kredili İşlem Özkaynak Tamamlama (Margin Call)',
    formula: 'Özkaynak Oranı = (Mevcut Özkaynak / Toplam Portföy Değeri) × 100\nAsgari Oran: %35 | Başlangıç Oranı: %50',
    variables: [
      { name: '%35 Barajı', desc: 'Özkaynak oranı %35 altına düştüğü an aracı kurum tamamlama çağrısı yapar' },
      { name: '%50 Hedefi', desc: 'Tamamlama yapılırken %35 seviyesine DEĞİL, başlangıç oranı olan %50 seviyesine tamamlanır' },
      { name: 'Nakit Tamamlama', desc: 'Eksik tutar kadar net nakit yatırılır' },
      { name: 'Hisse Tamamlama', desc: 'Getirilen hisse senetleri %50 katsayıyla kabul edildiğinden: Gereken Hisse = Eksik Tutar × 2' },
    ],
    example: 'Yatırımcının 100.000 TL portföyünde özkaynak 30.000 TL\'ye (%30) düştü. %50 olması için gereken özkaynak 50.000 TL.\nEksik Tutar = 20.000 TL nakit veya 40.000 TL değerinde hisse senedi (20.000 × 2).',
    examTrap: 'Hisse senedi tamamlama sorulduğunda adayın en çok unuttuğu kural hisselerin %50 katsayıyla değerlendirilmesidir (2 katı hisse yatırılmalıdır).',
  },
  {
    id: 'viop_margin_call',
    category: 'Türev Piyasalar (VİOP)',
    title: 'VİOP Margin Call (Teminat Tamamlama Çağrısı)',
    formula: 'Mevcut Teminat < Sürdürme Teminatı ⇒ Çağrı Yapılır\nTamamlama Tutarı = Başlangıç Teminatı - Mevcut Teminat',
    variables: [
      { name: 'Başlangıç Teminatı', desc: 'Pozisyon açmak için gereken asgari teminat (Takasbank belirler)' },
      { name: 'Sürdürme Teminatı', desc: 'Piyasa tersine hareket ettiğinde teminatın inebileceği asgari alt sınır' },
    ],
    example: '1 Sözleşme Başlangıç Teminatı = 5.000 TL, Sürdürme = 3.750 TL.\nZarar sonucu teminat 3.000 TL\'ye düşerse:\nTamamlama = 5.000 - 3.000 = 2.000 TL yatırılmalıdır.',
    examTrap: 'Çağrı sürdürme seviyesine (3.750) değil, BAŞLANGIÇ seviyesine (5.000) kadar tamamlanmak zorundadır!',
  },
  {
    id: 'tahvil_kirli_fiyat',
    category: 'Borçlanma Araçları',
    title: 'Tahvil Kirli Fiyat (Dirty Price) & Temiz Fiyat',
    formula: 'Kirli Fiyat = Temiz Fiyat + Birikmiş Faiz\nBirikmiş Faiz = Kupon Tutarı × (İşlemiş Gün / Kupon Dönemi Gün)',
    variables: [
      { name: 'Temiz Fiyat', desc: 'Birikmiş faiz hariç piyasa kote fiyatı' },
      { name: 'Kirli Fiyat', desc: 'Takasta alıcının satıcıya ödediği toplam fiili tutar' },
    ],
    example: 'Temiz Fiyat = 98 TL, İşlemiş faiz = 2.50 TL ise:\nKirli Fiyat = 98 + 2.50 = 100.50 TL.',
    examTrap: 'Borsa ekranında temiz fiyat kote edilir, takas günü satıcıya birikmiş faiziyle birlikte kirli fiyat ödenir.',
  },
  {
    id: 'asgari_ozsermaye',
    category: 'Yatırım Kuruluşları Mevzuatı',
    title: '2026 Asgari Özsermaye Tutarları (SPK Tebliği)',
    formula: 'Dar Yetkili: 45 Milyon TL\nKısmi Yetkili: 190 Milyon TL\nGeniş Yetkili: 380 Milyon TL\nPYŞ Yeni Kuruluş: 440 Milyon TL',
    variables: [
      { name: 'Dar Yetkili', desc: 'Emir iletimine aracılık, yatırım danışmanlığı: 45 Milyon TL' },
      { name: 'Kısmi Yetkili', desc: 'İşlem aracılığı, en iyi gayret aracılığı: 190 Milyon TL' },
      { name: 'Geniş Yetkili', desc: 'Portföy aracılığı, yüklenimde bulunarak halka arz: 380 Milyon TL' },
      { name: 'PYŞ', desc: 'Portföy Yönetim Şirketi kuruluş asgari özsermayesi: 440 Milyon TL' },
    ],
    example: 'Geniş yetkili aracı kurum olmak isteyen bir kurumun özsermayesi en az 380 Milyon TL olmalıdır.',
    examTrap: 'Eski tutarlar (25M / 65M / 150M) yürürlükten kalkmıştır. Güncel 2026 barajları 45M / 190M / 380M / 440M TL\'dir.',
  },
  {
    id: 'high_water_mark',
    category: 'Portföy Yönetimi',
    title: 'High-Water Mark (Zirve Değer İlkesi) & Başarı Primi',
    formula: 'Başarı Primi = Max(0, Portföy Değeri - Zirve Değer - Eşik Değer Getirisi) × Prim Oranı',
    variables: [
      { name: 'Zirve Değer', desc: 'Portföyün geçmişte ulaştığı en yüksek net varlık değeri' },
      { name: 'Eşik Değer (Hurdle Rate)', desc: 'Portföyün aşması gereken asgari kıyaslama getirisi (örn. BIST KYD Repo)' },
      { name: 'Kural', desc: 'Zirve değerin altında kalınan dönemlerde performans/başarı primi kesinlikle tahakkuk ettirilemez.' },
    ],
    example: 'Geçmiş zirve değer 1.000.000 TL olan portföy 900.000 TL\'ye düşüp sonra 980.000 TL\'ye çıksa dahi 1.000.000 TL aşılmadığı için başarı primi alınamaz.',
    examTrap: 'Portföy yükselse dahi geçmişteki zirveyi ve eşik değeri aşmadıkça başarı primi ödenemez.',
  },
  {
    id: 'viop_kaldirac',
    category: 'Türev Piyasalar (VİOP)',
    title: 'VİOP Kaldıraç Oranı & Pozisyon Büyüklüğü',
    formula: 'Pozisyon Büyüklüğü = Sözleşme Adedi × Sözleşme Büyüklüğü × Fiyat\nKaldıraç Oranı = Pozisyon Büyüklüğü / Yatırılan Başlangıç Teminatı',
    variables: [
      { name: 'Sözleşme Büyüklüğü', desc: 'Pay vadeli: 100 pay | Endeks vadeli: 10 pay' },
      { name: 'Efektif Kaldıraç', desc: 'Toplam piyasa riskinin yatırılan teminata oranı' },
    ],
    example: '10 adet BIST 30 Endeks sözleşmesi (10×10×10.000 = 1.000.000 TL pozisyon) için 100.000 TL teminat yatırıldıysa:\nKaldıraç = 1.000.000 / 100.000 = 10 Kat.',
    examTrap: 'Kaldıraç hesaplanırken kâr/zarar değil, toplam nominal pozisyon büyüklüğü teminata bölünür.',
  },
];

export const FormulaDrawer: React.FC<FormulaDrawerProps> = ({ isOpen, onClose }) => {
  const [search, setSearch] = useState('');
  const [selectedCategory, setSelectedCategory] = useState<string>('all');

  if (!isOpen) return null;

  const categories = ['all', ...Array.from(new Set(FORMULAS.map((f) => f.category)))];

  const filteredFormulas = FORMULAS.filter((f) => {
    if (selectedCategory !== 'all' && f.category !== selectedCategory) return false;
    if (search.trim()) {
      const q = search.toLowerCase();
      return (
        f.title.toLowerCase().includes(q) ||
        f.formula.toLowerCase().includes(q) ||
        f.example.toLowerCase().includes(q)
      );
    }
    return true;
  });

  return (
    <div className="fixed inset-0 z-50 flex items-end sm:items-center justify-center p-0 sm:p-4 bg-slate-950/60 backdrop-blur-xs animate-fade-in">
      <div 
        className="w-full max-w-2xl bg-white dark:bg-fintech-surface rounded-t-3xl sm:rounded-3xl border border-slate-200 dark:border-fintech-border shadow-2xl max-h-[88vh] flex flex-col overflow-hidden animate-slide-up"
      >
        {/* Header */}
        <div className="p-4 sm:p-5 border-b border-slate-200 dark:border-fintech-border flex items-center justify-between bg-slate-50/80 dark:bg-fintech-card/60">
          <div className="flex items-center gap-2.5">
            <div className="p-2 rounded-xl bg-teal-500/10 text-teal-600 dark:text-teal-400">
              <Calculator className="w-5 h-5" />
            </div>
            <div>
              <h3 className="font-black text-slate-900 dark:text-white text-base sm:text-lg">
                Sayısal Formül & Mevzuat Çekmecesi
              </h3>
              <p className="text-xs text-slate-500 dark:text-slate-400">
                SPL Düzey 1 sınavında çıkan tüm hesaplamalar ve formül adımları
              </p>
            </div>
          </div>
          <button
            onClick={onClose}
            className="p-2 rounded-xl bg-slate-100 dark:bg-slate-800 text-slate-500 hover:text-slate-900 dark:hover:text-white transition-colors"
            title="Kapat"
          >
            <X className="w-5 h-5" />
          </button>
        </div>

        {/* Filter and Search */}
        <div className="p-3 sm:p-4 border-b border-slate-100 dark:border-fintech-border/50 space-y-2.5 bg-white dark:bg-fintech-surface">
          <div className="relative">
            <Search className="absolute left-3 top-2.5 w-4 h-4 text-slate-400" />
            <input
              type="text"
              value={search}
              onChange={(e) => setSearch(e.target.value)}
              placeholder="Formül veya konu ara (örn: rüçhan, temettü, özkaynak, viop)..."
              className="w-full pl-9 pr-4 py-2 bg-slate-50 dark:bg-fintech-card border border-slate-200 dark:border-fintech-border rounded-xl text-xs sm:text-sm text-slate-900 dark:text-slate-100 focus:outline-none focus:border-teal-500"
            />
          </div>

          <div className="flex items-center gap-1.5 overflow-x-auto no-scrollbar pb-1 text-xs">
            {categories.map((cat) => (
              <button
                key={cat}
                onClick={() => setSelectedCategory(cat)}
                className={`px-3 py-1 rounded-lg font-semibold shrink-0 transition-all ${
                  selectedCategory === cat
                    ? 'bg-teal-600 text-white shadow-xs'
                    : 'bg-slate-100 text-slate-600 dark:bg-fintech-card dark:text-slate-400 hover:bg-slate-200 dark:hover:bg-fintech-cardHover'
                }`}
              >
                {cat === 'all' ? 'Tümü (7 Formül)' : cat}
              </button>
            ))}
          </div>
        </div>

        {/* Formül Kartları Listesi */}
        <div className="p-4 sm:p-5 overflow-y-auto space-y-4">
          {filteredFormulas.map((item) => (
            <div
              key={item.id}
              className="rounded-2xl border border-slate-200 dark:border-fintech-border bg-slate-50/50 dark:bg-fintech-card/50 p-4 space-y-3"
            >
              <div className="flex items-center justify-between">
                <span className="text-[11px] font-mono font-bold px-2 py-0.5 rounded-md bg-teal-500/10 text-teal-700 dark:text-teal-300 border border-teal-500/20">
                  {item.category}
                </span>
                <span className="text-xs font-mono font-black text-slate-500">
                  #{item.id}
                </span>
              </div>

              <h4 className="text-sm sm:text-base font-black text-slate-900 dark:text-white">
                {item.title}
              </h4>

              {/* Formül Kutusu */}
              <div className="p-3 rounded-xl bg-slate-900 text-teal-300 font-mono text-xs sm:text-sm whitespace-pre-wrap leading-relaxed border border-slate-800">
                {item.formula}
              </div>

              {/* Değişken Açıklamaları */}
              <div className="space-y-1 text-xs">
                {item.variables.map((v, idx) => (
                  <div key={idx} className="flex items-start gap-1.5">
                    <span className="font-mono font-bold text-teal-600 dark:text-teal-400 shrink-0">
                      • {v.name}:
                    </span>
                    <span className="text-slate-600 dark:text-slate-300">
                      {v.desc}
                    </span>
                  </div>
                ))}
              </div>

              {/* Somut Örnek Çözüm */}
              <div className="p-2.5 rounded-xl bg-emerald-50 dark:bg-emerald-950/30 border border-emerald-200 dark:border-emerald-800/40 text-xs text-emerald-950 dark:text-emerald-200 font-mono whitespace-pre-wrap">
                <span className="font-bold block mb-1">💡 Somut Sınav Örneği:</span>
                {item.example}
              </div>

              {/* Sınav Tuzağı */}
              <div className="p-2.5 rounded-xl bg-amber-50 dark:bg-amber-950/30 border border-amber-200 dark:border-amber-800/40 text-xs text-amber-950 dark:text-amber-200 flex items-start gap-2">
                <AlertCircle className="w-4 h-4 text-amber-600 shrink-0 mt-0.5" />
                <div>
                  <span className="font-bold">Sınav Tuzağı: </span>
                  {item.examTrap}
                </div>
              </div>
            </div>
          ))}
        </div>

        {/* Footer */}
        <div className="p-3 pb-[calc(0.75rem+env(safe-area-inset-bottom,0px))] border-t border-slate-200 dark:border-fintech-border bg-slate-50 dark:bg-fintech-card/80 text-center">
          <button
            onClick={onClose}
            className="w-full min-h-[44px] flex items-center justify-center py-2.5 rounded-xl bg-teal-600 hover:bg-teal-700 active:bg-teal-800 text-white font-bold text-xs sm:text-sm shadow-xs active:scale-98 transition-all cursor-pointer"
          >
            Anladım, Soruya Geri Dön
          </button>
        </div>
      </div>
    </div>
  );
};
