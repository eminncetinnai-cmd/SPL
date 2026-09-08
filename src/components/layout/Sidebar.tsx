import React from 'react';
import { 
  Home, 
  BookOpen, 
  Sparkles, 
  Layers, 
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
  ChevronRight,
  Zap,
  Award
} from 'lucide-react';
import { useProgressStore } from '../../stores/progressStore';

interface SidebarProps {
  currentPage: string;
  onNavigate: (page: string, params?: any) => void;
}

export const Sidebar: React.FC<SidebarProps> = ({ currentPage, onNavigate }) => {
  const { mistakes, bookmarks, learnedCards } = useProgressStore();
  const mistakeCount = Object.values(mistakes).filter(m => !m.resolved).length;
  const bookmarkCount = bookmarks.length;
  const learnedCardsCount = learnedCards.length;

  const navItems = [
    { id: 'home', label: 'Ana Sayfa', icon: Home },
    { id: 'practice', label: 'Test Çöz', icon: Sparkles, badge: '860 Soru', color: 'text-teal-600 dark:text-teal-400' },
    { id: 'cheat-sheet', label: '⚡ Sınav Hapları (10 Dk)', icon: Zap, badge: 'Hızlı Tekrar', color: 'text-amber-600 dark:text-amber-400' },
    { id: 'flashcards', label: 'Öğrenme Kartları', icon: Layers, badge: '400 Kart' },
    { id: 'study-notes', label: 'Konu Anlatımları', icon: FileText, badge: '32 Bölüm' },
    { id: 'mistakes', label: 'Yanlışlarım Defteri', icon: AlertTriangle, count: mistakeCount, color: 'text-rose-500 dark:text-rose-400' },
    { id: 'bookmarks', label: 'Yıldızlı Sorular', icon: Star, count: bookmarkCount, color: 'text-amber-500 dark:text-amber-400' },
    { id: 'dashboard', label: 'Analitik & İstatistik', icon: BarChart3 },
    { id: 'settings', label: 'Ayarlar & Yedek', icon: Settings },
  ];

  const modules = [
    { id: '1001', code: '1001', name: 'Mevzuat & Meslek', icon: Scale, color: 'text-emerald-700 dark:text-emerald-400', bg: 'bg-emerald-50 dark:bg-emerald-500/10' },
    { id: '1003', code: '1003', name: 'Sermaye Piyasası Araçları', icon: Coins, color: 'text-cyan-700 dark:text-cyan-400', bg: 'bg-cyan-50 dark:bg-cyan-500/10' },
    { id: '1005', code: '1005', name: 'Yatırım Kuruluşları', icon: Building2, color: 'text-purple-700 dark:text-purple-400', bg: 'bg-purple-50 dark:bg-purple-500/10' },
    { id: '1012', code: '1012', name: 'Takas, Saklama & Op.', icon: ShieldCheck, color: 'text-amber-700 dark:text-amber-400', bg: 'bg-amber-50 dark:bg-amber-500/10' },
  ];

  return (
    <aside className="w-64 shrink-0 border-r border-slate-200 dark:border-fintech-border bg-white dark:bg-fintech-surface/90 min-h-[calc(100vh-61px)] p-4 flex flex-col justify-between hidden md:flex">
      <div className="space-y-6">
        {/* Main Navigation */}
        <div className="space-y-1">
          <p className="px-3 text-[11px] font-mono uppercase tracking-wider text-slate-500 dark:text-slate-400 font-bold mb-2">
            Platform Menüsü
          </p>
          {navItems.map((item) => {
            const Icon = item.icon;
            const isActive = currentPage === item.id;
            return (
              <button
                key={item.id}
                onClick={() => onNavigate(item.id)}
                className={`w-full flex items-center justify-between px-3 py-2.5 rounded-xl text-sm font-medium transition-all ${
                  isActive
                    ? 'bg-teal-50 text-teal-900 border border-teal-200 font-bold dark:bg-teal-500/15 dark:text-teal-300 dark:border-teal-500/30'
                    : 'text-slate-700 hover:text-slate-900 hover:bg-slate-100 dark:text-slate-300 dark:hover:text-white dark:hover:bg-fintech-card'
                }`}
              >
                <div className="flex items-center gap-3">
                  <Icon className={`w-4 h-4 ${isActive ? 'text-teal-600 dark:text-teal-400' : item.color || 'text-slate-500 dark:text-slate-400'}`} />
                  <span>{item.label}</span>
                </div>
                {item.badge && (
                  <span className="text-[10px] font-mono px-2 py-0.5 rounded-full bg-teal-50 text-teal-700 border border-teal-200 dark:bg-teal-500/10 dark:text-teal-400 dark:border-teal-500/20 font-bold">
                    {item.badge}
                  </span>
                )}
                {typeof item.count === 'number' && item.count > 0 && (
                  <span className="text-[11px] font-mono px-2 py-0.5 rounded-full bg-rose-50 text-rose-700 border border-rose-200 dark:bg-rose-500/20 dark:text-rose-300 dark:border-rose-500/30 font-bold">
                    {item.count}
                  </span>
                )}
              </button>
            );
          })}
        </div>

        {/* Modules Section */}
        <div className="space-y-1 pt-2 border-t border-slate-200 dark:border-fintech-border/60">
          <p className="px-3 text-[11px] font-mono uppercase tracking-wider text-slate-500 dark:text-slate-400 font-bold mb-2">
            Modül Soru Çözümü
          </p>
          {modules.map((m) => {
            const Icon = m.icon;
            return (
              <button
                key={m.id}
                onClick={() => onNavigate('practice', { moduleId: m.id })}
                className="w-full flex items-center justify-between px-3 py-2 rounded-xl text-xs text-slate-700 hover:text-slate-900 hover:bg-slate-100 dark:text-slate-300 dark:hover:text-white dark:hover:bg-fintech-card transition-all group"
              >
                <div className="flex items-center gap-2.5">
                  <div className={`p-1.5 rounded-lg ${m.bg} ${m.color}`}>
                    <Icon className="w-3.5 h-3.5" />
                  </div>
                  <div className="text-left">
                    <span className="font-mono text-[10px] text-slate-500 dark:text-slate-400 block">{m.code}</span>
                    <span className="font-bold truncate block max-w-[140px]">{m.name}</span>
                  </div>
                </div>
                <ChevronRight className="w-3.5 h-3.5 text-slate-400 group-hover:text-slate-700 dark:text-slate-600 dark:group-hover:text-slate-300 group-hover:translate-x-0.5 transition-all" />
              </button>
            );
          })}
        </div>
      </div>

      {/* Footer Info Box */}
      <div className="p-3 rounded-2xl bg-slate-50 dark:bg-fintech-card/80 border border-slate-200 dark:border-fintech-border text-xs space-y-2">
        <div className="flex items-center justify-between font-mono text-[10px] text-slate-500 dark:text-slate-400">
          <span className="font-bold text-slate-700 dark:text-slate-300">SPK SPL 1 PRO</span>
          <span className="text-emerald-600 dark:text-emerald-400 font-bold">ONLINE</span>
        </div>
        <div className="text-[11px] text-slate-600 dark:text-slate-300 leading-tight">
          860 Soru • 400 Flashcard • 32 Ders Notu
        </div>
        <div className="pt-2 border-t border-slate-200 dark:border-fintech-border/60 text-[10px] space-y-0.5">
          <div className="flex items-center justify-between">
            <span className="text-slate-500 dark:text-slate-400">Geliştirici & Küratör:</span>
            <span className="font-bold text-slate-800 dark:text-slate-200">Emin ÇETİN</span>
          </div>
          <p className="text-[9px] text-slate-400 dark:text-slate-500 font-mono">
            © 2026 Tüm Hakları Saklıdır
          </p>
        </div>
      </div>
    </aside>
  );
};
