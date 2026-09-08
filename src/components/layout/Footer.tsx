import React from 'react';
import { ShieldCheck, Award, Sparkles } from 'lucide-react';

interface FooterProps {
  onNavigate?: (page: string, params?: any) => void;
}

export const Footer: React.FC<FooterProps> = ({ onNavigate }) => {
  return (
    <footer className="w-full mt-16 pt-8 pb-12 border-t border-slate-200 dark:border-fintech-border text-slate-500 dark:text-slate-400 text-xs no-print">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 space-y-8">
        {/* Main Info Grid */}
        <div className="grid grid-cols-1 md:grid-cols-3 gap-8 items-start">
          {/* Brand & Mission */}
          <div className="space-y-3">
            <div className="flex items-center gap-2.5">
              <div className="w-8 h-8 rounded-xl bg-gradient-to-tr from-teal-600 to-emerald-500 flex items-center justify-center text-white font-black text-xs shadow-sm">
                SPK
              </div>
              <div>
                <span className="text-sm font-black text-slate-900 dark:text-white tracking-tight block">
                  SPK SPL DÜZEY 1 PRO EXAM
                </span>
                <span className="text-[10px] text-slate-500 dark:text-slate-400">
                  Lisanslama Sınavı Hazırlık Platformu
                </span>
              </div>
            </div>
            <p className="text-xs text-slate-600 dark:text-slate-400 leading-relaxed">
              Sermaye Piyasası Kurulu (SPK) Lisanslama Sınavlarına hazırlanan adaylar için geliştirilmiş yeni nesil soru çözüm, analitik ölçme ve sınav simülasyon platformu.
            </p>
            <div className="flex flex-wrap items-center gap-2 pt-1">
              <span className="inline-flex items-center gap-1 px-2.5 py-1 rounded-lg bg-teal-50 dark:bg-teal-500/10 text-teal-800 dark:text-teal-300 border border-teal-200 dark:border-teal-500/20 text-[10px] font-mono font-bold">
                <ShieldCheck className="w-3 h-3 text-teal-600 dark:text-teal-400" />
                Müfredat: Temmuz 2026
              </span>
              <span className="inline-flex items-center gap-1 px-2.5 py-1 rounded-lg bg-amber-50 dark:bg-amber-500/10 text-amber-900 dark:text-amber-300 border border-amber-200 dark:border-amber-500/20 text-[10px] font-mono font-bold">
                <Award className="w-3 h-3 text-amber-500" />
                860 Soru • 400 Kart • 115 Eşik
              </span>
            </div>
          </div>

          {/* Quick Nav Links */}
          <div className="space-y-3 md:pl-6">
            <h4 className="text-xs font-mono font-bold uppercase tracking-wider text-slate-900 dark:text-slate-200">
              Hızlı Erişim & Çalışma Alanları
            </h4>
            <ul className="space-y-2 text-xs">
              <li>
                <button
                  onClick={() => onNavigate?.('practice')}
                  className="hover:text-teal-600 dark:hover:text-teal-400 transition-colors flex items-center gap-2 text-left"
                >
                  <span className="w-1.5 h-1.5 rounded-full bg-teal-500 shrink-0"></span>
                  <span>Soru Çözüm Merkezi (860 Soru)</span>
                </button>
              </li>
              <li>
                <button
                  onClick={() => onNavigate?.('cheat-sheet')}
                  className="hover:text-teal-600 dark:hover:text-teal-400 transition-colors flex items-center gap-2 text-left"
                >
                  <span className="w-1.5 h-1.5 rounded-full bg-amber-500 shrink-0"></span>
                  <span>Sınav Hap Bilgileri (115 Eşik & Süre)</span>
                </button>
              </li>
              <li>
                <button
                  onClick={() => onNavigate?.('flashcards')}
                  className="hover:text-teal-600 dark:hover:text-teal-400 transition-colors flex items-center gap-2 text-left"
                >
                  <span className="w-1.5 h-1.5 rounded-full bg-purple-500 shrink-0"></span>
                  <span>Öğrenme Kartları (400 Flashcard)</span>
                </button>
              </li>
              <li>
                <button
                  onClick={() => onNavigate?.('study-notes')}
                  className="hover:text-teal-600 dark:hover:text-teal-400 transition-colors flex items-center gap-2 text-left"
                >
                  <span className="w-1.5 h-1.5 rounded-full bg-cyan-500 shrink-0"></span>
                  <span>Resmi Konu Anlatımları (32 Bölüm)</span>
                </button>
              </li>
              <li>
                <button
                  onClick={() => onNavigate?.('settings')}
                  className="hover:text-teal-600 dark:hover:text-teal-400 transition-colors flex items-center gap-2 text-left"
                >
                  <span className="w-1.5 h-1.5 rounded-full bg-slate-400 shrink-0"></span>
                  <span>Uygulama Tercihleri & Telif Bilgisi</span>
                </button>
              </li>
            </ul>
          </div>

          {/* Legal Ownership & Creator Attribution Card */}
          <div className="space-y-3 bg-slate-50 dark:bg-fintech-card/60 p-4 rounded-2xl border border-slate-200 dark:border-fintech-border shadow-xs">
            <div className="flex items-center justify-between">
              <span className="text-[11px] font-mono uppercase tracking-wider text-slate-500 dark:text-slate-400 font-bold">
                Fikri Mülkiyet & Telif
              </span>
              <span className="px-2 py-0.5 rounded-full bg-emerald-100 text-emerald-800 dark:bg-emerald-500/20 dark:text-emerald-300 text-[10px] font-bold">
                Telif Korumalı
              </span>
            </div>

            <div className="space-y-1">
              <p className="text-xs text-slate-600 dark:text-slate-300">
                Tasarım, Yazılım Mimarisi ve İçerik Kürasyonu:
              </p>
              <div className="flex items-center gap-2 pt-0.5">
                <div className="w-7 h-7 rounded-lg bg-gradient-to-tr from-teal-500 to-emerald-500 flex items-center justify-center text-slate-950 font-black text-xs shadow-xs">
                  EÇ
                </div>
                <span className="text-sm font-black text-slate-900 dark:text-white tracking-wide">
                  Emin ÇETİN
                </span>
              </div>
            </div>

            <p className="text-[11px] text-slate-500 dark:text-slate-400 leading-relaxed pt-1 border-t border-slate-200 dark:border-fintech-border/60">
              Bu yazılım, soru havuzu, psikometrik algoritmalar ve eğitim içerikleri <strong>Emin ÇETİN</strong> tarafından hazırlanmıştır. 5846 sayılı Fikir ve Sanat Eserleri Kanunu uyarınca <strong>tüm hakları saklıdır</strong>. İzinsiz kopyalanamaz, çoğaltılamaz veya dağıtılamaz.
            </p>
          </div>
        </div>

        {/* Bottom Bar */}
        <div className="pt-6 border-t border-slate-200 dark:border-fintech-border/70 flex flex-col sm:flex-row items-center justify-between gap-3 text-[11px] text-slate-500 dark:text-slate-400">
          <div>
            © 2026 <strong className="text-slate-800 dark:text-slate-200 font-bold">Emin ÇETİN</strong>. Tüm Hakları Saklıdır.
          </div>
          <div className="flex flex-wrap items-center gap-3 sm:gap-4 text-[11px] font-mono">
            <span>SPK SPL 1 PRO v2.5.0</span>
            <span className="hidden sm:inline">•</span>
            <span>Müfredat: Temmuz 2026</span>
            <span className="hidden sm:inline">•</span>
            <span>Türkiye Sermaye Piyasaları</span>
          </div>
        </div>
      </div>
    </footer>
  );
};
