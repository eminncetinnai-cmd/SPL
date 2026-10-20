import React, { useState } from 'react';
import {
  Sparkles,
  Moon,
  Sun,
  Volume2,
  VolumeX,
  Award,
  CheckCircle2,
  Flame,
  BookMarked,
  Menu,
  X,
  AlertTriangle,
  Star,
  Search,
  BarChart3,
  Settings,
  Zap,
} from 'lucide-react';
import { useSettingsStore } from '../../stores/settingsStore';
import { useProgressStore } from '../../stores/progressStore';

interface NavbarProps {
  onNavigate: (page: string, params?: any) => void;
  currentPage: string;
}

export const Navbar: React.FC<NavbarProps> = ({ onNavigate }) => {
  const { theme, toggleTheme, soundEnabled, setSoundEnabled } = useSettingsStore();
  const { history, bookmarks, mistakes } = useProgressStore();
  const [mobileMenuOpen, setMobileMenuOpen] = useState(false);

  const totalQuizzes = history.length;
  const mistakeCount = Object.values(mistakes).filter((m) => !m.resolved).length;
  const bookmarkCount = bookmarks.length;

  const totalScore = history.reduce((acc, h) => acc + h.score, 0);
  const avgScore = totalQuizzes > 0 ? Math.round(totalScore / totalQuizzes) : 0;

  const handleMobileNav = (page: string, params?: any) => {
    setMobileMenuOpen(false);
    onNavigate(page, params);
  };

  return (
    <header className="sticky top-0 z-40 w-full border-b border-fintech-border bg-fintech-dark/95 backdrop-blur-md px-3 sm:px-6 pt-[calc(0.625rem+env(safe-area-inset-top,0px))] pb-2.5">
      <div className="flex items-center justify-between gap-2">
        {/* Brand & Logo */}
        <div
          onClick={() => onNavigate('home')}
          className="flex items-center gap-2.5 cursor-pointer group select-none min-w-0"
        >
          <div className="w-9 h-9 rounded-xl bg-gradient-to-tr from-teal-600 to-emerald-500 p-[1px] shadow-sm shrink-0">
            <div className="w-full h-full bg-white dark:bg-fintech-surface rounded-xl flex items-center justify-center">
              <Award className="w-4 h-4 text-teal-600 dark:text-teal-400" />
            </div>
          </div>
          <div className="min-w-0">
            <div className="flex items-center gap-1.5">
              <span className="text-base sm:text-lg font-black tracking-tight text-slate-900 dark:text-white truncate">
                SPK SPL 1
              </span>
              <span className="text-[9px] uppercase font-mono tracking-wider px-1.5 py-0.5 rounded-full bg-teal-50 dark:bg-teal-500/10 text-teal-700 dark:text-teal-400 border border-teal-200 dark:border-teal-500/30 font-bold shrink-0">
                PRO
              </span>
            </div>
          </div>
        </div>

        {/* Quick KPI stats in Navbar (Desktop) */}
        <div className="hidden lg:flex items-center gap-3">
          <div className="flex items-center gap-1.5 px-2.5 py-1 rounded-lg bg-slate-50 dark:bg-fintech-card border border-slate-200 dark:border-fintech-border text-xs">
            <Flame className="w-3.5 h-3.5 text-amber-500" />
            <span className="text-slate-500 dark:text-slate-400">Test:</span>
            <span className="font-mono font-bold text-slate-900 dark:text-slate-200">{totalQuizzes}</span>
          </div>

          <div className="flex items-center gap-1.5 px-2.5 py-1 rounded-lg bg-slate-50 dark:bg-fintech-card border border-slate-200 dark:border-fintech-border text-xs">
            <CheckCircle2 className="w-3.5 h-3.5 text-emerald-600 dark:text-emerald-400" />
            <span className="text-slate-500 dark:text-slate-400">Başarı:</span>
            <span className="font-mono font-bold text-emerald-600 dark:text-emerald-400">%{avgScore}</span>
          </div>

          {mistakeCount > 0 && (
            <button
              onClick={() => onNavigate('mistakes')}
              className="flex items-center gap-1.5 px-2.5 py-1 rounded-lg bg-rose-50 dark:bg-rose-500/10 border border-rose-200 dark:border-rose-500/30 text-rose-700 dark:text-rose-400 hover:bg-rose-100 transition-all text-xs font-semibold"
            >
              <span>{mistakeCount} Hatalı</span>
            </button>
          )}

          {bookmarkCount > 0 && (
            <button
              onClick={() => onNavigate('bookmarks')}
              className="flex items-center gap-1.5 px-2.5 py-1 rounded-lg bg-amber-50 dark:bg-amber-500/10 border border-amber-200 dark:border-amber-500/30 text-amber-700 dark:text-amber-400 hover:bg-amber-100 transition-all text-xs font-semibold"
            >
              <BookMarked className="w-3.5 h-3.5" />
              <span>{bookmarkCount}</span>
            </button>
          )}
        </div>

        {/* Action Controls */}
        <div className="flex items-center gap-1.5 sm:gap-2">
          {/* Sınav Sabahı Modu CTA */}
          <button
            onClick={() => onNavigate('exam-morning')}
            className="flex items-center gap-1 px-2.5 py-1.5 rounded-lg bg-gradient-to-r from-amber-500 to-rose-500 hover:from-amber-600 hover:to-rose-600 text-white text-xs font-black tracking-wide shadow-xs transition-all active:scale-95 cursor-pointer"
            title="Sınav Salonuna Girmeden Önceki Son 15 Dakika Hap Bilgileri"
          >
            <Zap className="w-3.5 h-3.5 fill-white text-white" />
            <span className="hidden sm:inline">Sınav Sabahı (15 Dk)</span>
            <span className="sm:hidden">15 Dk</span>
          </button>

          {/* Mobile Mistake Quick Badge */}
          {mistakeCount > 0 && (
            <button
              onClick={() => onNavigate('mistakes')}
              className="lg:hidden flex items-center gap-1 px-2 py-1.5 rounded-lg bg-rose-50 dark:bg-rose-500/15 border border-rose-200 dark:border-rose-500/30 text-rose-700 dark:text-rose-300 text-xs font-bold"
              title="Yanlışlarım Defteri"
            >
              <AlertTriangle className="w-3.5 h-3.5 text-rose-500" />
              <span>{mistakeCount}</span>
            </button>
          )}

          {/* Sound Toggle */}
          <button
            onClick={() => setSoundEnabled(!soundEnabled)}
            className="p-2 rounded-lg bg-slate-100 hover:bg-slate-200 dark:bg-fintech-card dark:hover:bg-fintech-cardHover border border-slate-200 dark:border-fintech-border text-slate-600 dark:text-slate-300 transition-colors"
            title={soundEnabled ? 'Ses Efektleri Açık' : 'Ses Efektleri Kapalı'}
          >
            {soundEnabled ? (
              <Volume2 className="w-4 h-4 text-teal-600 dark:text-teal-400" />
            ) : (
              <VolumeX className="w-4 h-4 text-slate-400" />
            )}
          </button>

          {/* Theme Toggle */}
          <button
            onClick={toggleTheme}
            className="p-2 rounded-lg bg-slate-100 hover:bg-slate-200 dark:bg-fintech-card dark:hover:bg-fintech-cardHover border border-slate-200 dark:border-fintech-border text-slate-600 dark:text-slate-300 transition-colors"
            title="Tema Değiştir"
          >
            {theme === 'dark' ? (
              <Sun className="w-4 h-4 text-amber-400" />
            ) : (
              <Moon className="w-4 h-4 text-slate-600" />
            )}
          </button>

          {/* Quick Quiz CTA (Desktop) */}
          <button
            onClick={() => onNavigate('practice')}
            className="hidden sm:flex items-center gap-1.5 px-3.5 py-1.5 rounded-xl bg-teal-600 hover:bg-teal-700 text-white font-bold text-xs shadow-xs transition-all active:scale-95 cursor-pointer"
          >
            <Sparkles className="w-3.5 h-3.5 text-white" />
            <span>Test Çöz</span>
          </button>

          {/* Mobile Secondary Menu Toggle */}
          <button
            onClick={() => setMobileMenuOpen(!mobileMenuOpen)}
            className="p-2 rounded-lg bg-slate-100 hover:bg-slate-200 dark:bg-fintech-card border border-slate-200 dark:border-fintech-border text-slate-600 dark:text-slate-300 md:hidden transition-colors"
            title="Diğer Araçlar"
          >
            {mobileMenuOpen ? <X className="w-4 h-4" /> : <Menu className="w-4 h-4" />}
          </button>
        </div>
      </div>

      {/* Compact Mobile Drawer (Secondary Tools Only) */}
      {mobileMenuOpen && (
        <div className="md:hidden pt-3 pb-2 border-t border-slate-200 dark:border-fintech-border mt-2.5 animate-slide-up">
          <div className="grid grid-cols-2 gap-2 text-xs font-semibold">
            <button
              onClick={() => handleMobileNav('practice')}
              className="min-h-[44px] flex items-center gap-2 p-2.5 rounded-xl bg-slate-50 dark:bg-fintech-card border border-slate-200 dark:border-fintech-border text-slate-800 dark:text-slate-200 text-left cursor-pointer active:scale-95 transition-all"
            >
              <Award className="w-4 h-4 text-amber-500 shrink-0" />
              <span>Soru Çözümü</span>
            </button>
            <button
              onClick={() => handleMobileNav('study-notes')}
              className="min-h-[44px] flex items-center gap-2 p-2.5 rounded-xl bg-slate-50 dark:bg-fintech-card border border-slate-200 dark:border-fintech-border text-slate-800 dark:text-slate-200 text-left active:scale-95 transition-all"
            >
              <Zap className="w-4 h-4 text-teal-500 shrink-0" />
              <span>Ders Notları</span>
            </button>
            <button
              onClick={() => handleMobileNav('bookmarks')}
              className="min-h-[44px] flex items-center gap-2 p-2.5 rounded-xl bg-slate-50 dark:bg-fintech-card border border-slate-200 dark:border-fintech-border text-amber-700 dark:text-amber-300 text-left active:scale-95 transition-all"
            >
              <Star className="w-4 h-4 text-amber-500 shrink-0" />
              <span>Yıldızlılar ({bookmarkCount})</span>
            </button>
            <button
              onClick={() => handleMobileNav('settings')}
              className="min-h-[44px] flex items-center gap-2 p-2.5 rounded-xl bg-slate-50 dark:bg-fintech-card border border-slate-200 dark:border-fintech-border text-slate-800 dark:text-slate-200 text-left active:scale-95 transition-all"
            >
              <Settings className="w-4 h-4 text-slate-500 shrink-0" />
              <span>Ayarlar & Sıfırla</span>
            </button>
          </div>
        </div>
      )}
    </header>
  );
};
