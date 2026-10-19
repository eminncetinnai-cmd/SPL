import React from 'react';

interface FooterProps {
  onNavigate?: (page: string, params?: any) => void;
}

export const Footer: React.FC<FooterProps> = () => {
  return (
    <footer className="w-full mt-8 pt-4 pb-20 md:pb-6 border-t border-slate-200/80 dark:border-fintech-border/70 text-slate-500 dark:text-slate-400 text-[11px] no-print">
      <div className="flex flex-col sm:flex-row items-center justify-between gap-2">
        <div className="flex items-center gap-2 text-center sm:text-left">
          <span className="font-bold text-slate-800 dark:text-slate-200">SPK SPL Düzey 1 PRO</span>
          <span>•</span>
          <span>935 Soru • 249 Hap Bilgi • 400 Kart</span>
        </div>
        <div className="font-mono text-[10px] text-slate-400 dark:text-slate-500">
          © 2026 <strong className="text-slate-700 dark:text-slate-300">Emin ÇETİN</strong> • Temmuz 2026 Müfredatı
        </div>
      </div>
    </footer>
  );
};
