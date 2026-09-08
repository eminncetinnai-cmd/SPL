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
  Home,
  FileText,
  AlertTriangle,
  Star,
  Search,
  BarChart3,
  Settings,
  Scale,
  Coins,
  Building2,
  ShieldCheck,
  Zap
} from 'lucide-react';
import { useSettingsStore } from '../../stores/settingsStore';
import { useProgressStore } from '../../stores/progressStore';

interface NavbarProps {
  onNavigate: (page: string, params?: any) => void;
  currentPage: string;
}

export const Navbar: React.FC<NavbarProps> = ({ onNavigate, currentPage }) => {
  const { theme, toggleTheme, soundEnabled, setSoundEnabled } = useSettingsStore();
  const { history, bookmarks, mistakes } = useProgressStore();
  const [mobileMenuOpen, setMobileMenuOpen] = useState(false);

  const totalQuizzes = history.length;
  const mistakeCount = Object.values(mistakes).filter(m => !m.resolved).length;
  const bookmarkCount = bookmarks.length;

  const totalScore = history.reduce((acc, h) => acc + h.score, 0);
  const avgScore = totalQuizzes > 0 ? Math.round(totalScore / totalQuizzes) : 0;

  const handleMobileNav = (page: string, params?: any) => {
    setMobileMenuOpen(false);
    onNavigate(page, params);
  };

  return (
    <header className="sticky top-0 z-40 w-full border-b border-fintech-border bg-fintech-dark/95 backdrop-blur-md px-4 sm:px-6 py-3">
      <div className="flex items-center justify-between">
        {/* Brand & Logo */}
        <div 
          onClick={() => onNavigate('home')} 
          className="flex items-center gap-3 cursor-pointer group select-none"
        >
          <div className="w-10 h-10 rounded-xl bg-gradient-to-tr from-teal-600 to-emerald-500 p-[1px] shadow-sm group-hover:shadow-md transition-all">
            <div className="w-full h-full bg-white dark:bg-fintech-surface rounded-xl flex items-center justify-center">
              <Award className="w-5 h-5 text-teal-600 dark:text-teal-400 group-hover:scale-110 transition-transform" />
            </div>
          </div>
          <div>
            <div className="flex items-center gap-2">
              <span className="text-lg font-black tracking-tight text-slate-900 dark:text-white group-hover:text-teal-600 transition-colors">
                SPK SPL 1
              </span>
              <span className="text-[10px] uppercase font-mono tracking-widest px-2 py-0.5 rounded-full bg-teal-50 dark:bg-teal-500/10 text-teal-700 dark:text-teal-400 border border-teal-200 dark:border-teal-500/30 font-bold">
                PRO EXAM
              </span>
            </div>
            <p className="text-xs text-slate-500 dark:text-slate-400 hidden sm:block">
              Sermaye Piyasası Lisanslama Sınavı Hazırlık Platformu
            </p>
          </div>
        </div>

        {/* Quick KPI stats in Navbar */}
        <div className="hidden lg:flex items-center gap-4">
          <div className="flex items-center gap-2 px-3 py-1.5 rounded-lg bg-slate-50 dark:bg-fintech-card border border-slate-200 dark:border-fintech-border">
            <Flame className="w-4 h-4 text-amber-500" />
            <span className="text-xs text-slate-500 dark:text-slate-400">Çözülen Sınav:</span>
            <span className="text-xs font-mono font-bold text-slate-900 dark:text-slate-200">{totalQuizzes}</span>
          </div>

          <div className="flex items-center gap-2 px-3 py-1.5 rounded-lg bg-slate-50 dark:bg-fintech-card border border-slate-200 dark:border-fintech-border">
            <CheckCircle2 className="w-4 h-4 text-emerald-600 dark:text-emerald-400" />
            <span className="text-xs text-slate-500 dark:text-slate-400">Ort. Başarı:</span>
            <span className="text-xs font-mono font-bold text-emerald-600 dark:text-emerald-400">%{avgScore}</span>
          </div>

          {mistakeCount > 0 && (
            <button 
              onClick={() => onNavigate('mistakes')}
              className="flex items-center gap-2 px-3 py-1.5 rounded-lg bg-rose-50 dark:bg-rose-500/10 border border-rose-200 dark:border-rose-500/30 text-rose-700 dark:text-rose-400 hover:bg-rose-100 dark:hover:bg-rose-500/20 transition-all text-xs font-semibold"
            >
              <span>{mistakeCount} Hatalı Soru</span>
            </button>
          )}

          {bookmarkCount > 0 && (
            <button 
              onClick={() => onNavigate('bookmarks')}
              className="flex items-center gap-2 px-3 py-1.5 rounded-lg bg-amber-50 dark:bg-amber-500/10 border border-amber-200 dark:border-amber-500/30 text-amber-700 dark:text-amber-400 hover:bg-amber-100 dark:hover:bg-amber-500/20 transition-all text-xs font-semibold"
            >
              <BookMarked className="w-3.5 h-3.5" />
              <span>{bookmarkCount} Yıldızlı</span>
            </button>
          )}
        </div>

        {/* Action Controls */}
        <div className="flex items-center gap-2">
          {/* Sınav Hapları CTA */}
          <button
            onClick={() => onNavigate('cheat-sheet')}
            className="hidden xl:flex items-center gap-2 px-3 py-1.5 rounded-lg bg-amber-50 dark:bg-amber-500/10 border border-amber-200 dark:border-amber-500/30 text-amber-800 dark:text-amber-300 hover:bg-amber-100 dark:hover:bg-amber-500/20 text-xs font-bold transition-all"
          >
            <Zap className="w-3.5 h-3.5 fill-amber-500 text-amber-500" />
            <span>⚡ Sınav Hapları (10 Dk)</span>
          </button>

          {/* Sound Toggle */}
          <button
            onClick={() => setSoundEnabled(!soundEnabled)}
            className="p-2 rounded-lg bg-slate-100 hover:bg-slate-200 dark:bg-fintech-card dark:hover:bg-fintech-cardHover border border-slate-200 dark:border-fintech-border text-slate-600 hover:text-slate-900 dark:text-slate-300 dark:hover:text-white transition-colors"
            title={soundEnabled ? "Ses Efektleri Açık" : "Ses Efektleri Kapalı"}
          >
            {soundEnabled ? <Volume2 className="w-4 h-4 text-teal-600 dark:text-teal-400" /> : <VolumeX className="w-4 h-4 text-slate-400" />}
          </button>

          {/* Theme Toggle */}
          <button
            onClick={toggleTheme}
            className="p-2 rounded-lg bg-slate-100 hover:bg-slate-200 dark:bg-fintech-card dark:hover:bg-fintech-cardHover border border-slate-200 dark:border-fintech-border text-slate-600 hover:text-slate-900 dark:text-slate-300 dark:hover:text-white transition-colors"
            title="Tema Değiştir"
          >
            {theme === 'dark' ? <Sun className="w-4 h-4 text-amber-400" /> : <Moon className="w-4 h-4 text-slate-600" />}
          </button>

          {/* Quick Simulation CTA */}
          <button
            onClick={() => onNavigate('simulation-prep')}
            className="hidden sm:flex items-center gap-2 px-4 py-2 rounded-xl bg-gradient-to-r from-teal-600 to-emerald-600 hover:from-teal-500 hover:to-emerald-500 text-white font-bold text-xs tracking-wide shadow-sm hover:shadow transition-all active:scale-95"
          >
            <Sparkles className="w-3.5 h-3.5 text-white" />
            <span>Deneme Sınavı Başlat</span>
          </button>

          {/* Mobile Hamburger Toggle */}
          <button
            onClick={() => setMobileMenuOpen(!mobileMenuOpen)}
            className="p-2 rounded-lg bg-slate-100 hover:bg-slate-200 dark:bg-fintech-card dark:hover:bg-fintech-cardHover border border-slate-200 dark:border-fintech-border text-slate-600 hover:text-slate-900 dark:text-slate-300 md:hidden transition-colors"
            title="Menüyü Aç"
          >
            {mobileMenuOpen ? <X className="w-5 h-5" /> : <Menu className="w-5 h-5" />}
          </button>
        </div>
      </div>

      {/* Mobile Drawer Menu */}
      {mobileMenuOpen && (
        <div className="md:hidden pt-4 pb-2 border-t border-fintech-border mt-3 space-y-3 animate-slide-up">
          <div className="grid grid-cols-2 gap-2 text-xs font-medium">
            <button
              onClick={() => handleMobileNav('home')}
              className="flex items-center gap-2 p-2.5 rounded-xl bg-fintech-card text-teal-300 text-left font-bold"
            >
              <Home className="w-4 h-4 text-teal-400" />
              <span>Ana Sayfa</span>
            </button>
            <button
              onClick={() => handleMobileNav('cheat-sheet')}
              className="flex items-center gap-2 p-2.5 rounded-xl bg-amber-500/20 border border-amber-500/40 text-amber-300 text-left font-bold"
            >
              <Zap className="w-4 h-4 text-amber-400 fill-amber-400" />
              <span>⚡ Sınav Hapları (10 Dk)</span>
            </button>
            <button
              onClick={() => handleMobileNav('past-exams')}
              className="flex items-center gap-2 p-2.5 rounded-xl bg-amber-500/15 border border-amber-500/30 text-amber-300 text-left font-bold"
            >
              <Award className="w-4 h-4 text-amber-400" />
              <span>🎯 Çıkmış Sınav Grubu</span>
            </button>
            <button
              onClick={() => handleMobileNav('simulation-prep')}
              className="flex items-center gap-2 p-2.5 rounded-xl bg-fintech-card text-teal-300 text-left font-bold"
            >
              <Sparkles className="w-4 h-4 text-teal-400" />
              <span>Sınav Simülasyonu</span>
            </button>
            <button
              onClick={() => handleMobileNav('flashcards')}
              className="flex items-center gap-2 p-2.5 rounded-xl bg-fintech-card text-teal-300 text-left font-bold"
            >
              <Sparkles className="w-4 h-4 text-teal-400" />
              <span>Öğrenme Kartları (400)</span>
            </button>
            <button
              onClick={() => handleMobileNav('study-notes')}
              className="flex items-center gap-2 p-2.5 rounded-xl bg-fintech-card text-slate-200 text-left"
            >
              <FileText className="w-4 h-4 text-cyan-400" />
              <span>Konu Anlatımları</span>
            </button>
            <button
              onClick={() => handleMobileNav('mistakes')}
              className="flex items-center gap-2 p-2.5 rounded-xl bg-fintech-card text-rose-300 text-left"
            >
              <AlertTriangle className="w-4 h-4 text-rose-400" />
              <span>Yanlışlarım ({mistakeCount})</span>
            </button>
            <button
              onClick={() => handleMobileNav('bookmarks')}
              className="flex items-center gap-2 p-2.5 rounded-xl bg-fintech-card text-amber-300 text-left"
            >
              <Star className="w-4 h-4 text-amber-400" />
              <span>Yıldızlılar ({bookmarkCount})</span>
            </button>
            <button
              onClick={() => handleMobileNav('explorer')}
              className="flex items-center gap-2 p-2.5 rounded-xl bg-fintech-card text-slate-200 text-left"
            >
              <Search className="w-4 h-4 text-purple-400" />
              <span>540 Soru Bankası</span>
            </button>
            <button
              onClick={() => handleMobileNav('dashboard')}
              className="flex items-center gap-2 p-2.5 rounded-xl bg-fintech-card text-slate-200 text-left"
            >
              <BarChart3 className="w-4 h-4 text-emerald-400" />
              <span>İstatistik & Grafik</span>
            </button>
            <button
              onClick={() => handleMobileNav('settings')}
              className="flex items-center gap-2 p-2.5 rounded-xl bg-fintech-card text-slate-200 text-left"
            >
              <Settings className="w-4 h-4 text-slate-400" />
              <span>Ayarlar</span>
            </button>
          </div>

          <div className="pt-2 border-t border-fintech-border/60">
            <p className="text-[10px] font-mono uppercase tracking-wider text-slate-400 font-bold mb-2">
              Ders Pratik Testleri
            </p>
            <div className="grid grid-cols-2 gap-2 text-xs">
              <button
                onClick={() => handleMobileNav('module-quiz-prep', { moduleId: '1001' })}
                className="flex items-center gap-1.5 p-2 rounded-lg bg-emerald-500/10 text-emerald-300 text-left"
              >
                <Scale className="w-3.5 h-3.5" />
                <span>1001 Mevzuat</span>
              </button>
              <button
                onClick={() => handleMobileNav('module-quiz-prep', { moduleId: '1003' })}
                className="flex items-center gap-1.5 p-2 rounded-lg bg-cyan-500/10 text-cyan-300 text-left"
              >
                <Coins className="w-3.5 h-3.5" />
                <span>1003 Araçlar</span>
              </button>
              <button
                onClick={() => handleMobileNav('module-quiz-prep', { moduleId: '1005' })}
                className="flex items-center gap-1.5 p-2 rounded-lg bg-purple-500/10 text-purple-300 text-left"
              >
                <Building2 className="w-3.5 h-3.5" />
                <span>1005 Yatırım Kur.</span>
              </button>
              <button
                onClick={() => handleMobileNav('module-quiz-prep', { moduleId: '1012' })}
                className="flex items-center gap-1.5 p-2 rounded-lg bg-amber-500/10 text-amber-300 text-left"
              >
                <ShieldCheck className="w-3.5 h-3.5" />
                <span>1012 Takas/Saklama</span>
              </button>
            </div>
          </div>
        </div>
      )}
    </header>
  );
};
