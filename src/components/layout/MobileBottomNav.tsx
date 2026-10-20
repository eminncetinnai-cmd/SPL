import { Home, Sparkles, Zap, Layers, AlertTriangle } from 'lucide-react';

interface MobileBottomNavProps {
  currentPage: string;
  onNavigate: (page: string, params?: any) => void;
}

export const MobileBottomNav: React.FC<MobileBottomNavProps> = ({ currentPage, onNavigate }) => {
  const tabs = [
    { id: 'home', label: 'Ana Sayfa', icon: Home },
    { id: 'practice', label: 'Test Çöz', icon: Sparkles },
    { id: 'mistakes', label: 'Yanlışlarım', icon: AlertTriangle },
    { id: 'cheat-sheet', label: 'Hap Bilgi', icon: Zap },
    { id: 'flashcards', label: 'Kartlar', icon: Layers },
  ];

  return (
    <nav className="md:hidden fixed bottom-0 inset-x-0 z-40 bg-white/95 dark:bg-fintech-surface/95 backdrop-blur-md border-t border-slate-200 dark:border-fintech-border px-2 pt-1.5 pb-[calc(0.6rem+env(safe-area-inset-bottom,0px))] no-print shadow-lg">
      <div className="grid grid-cols-5 gap-1 max-w-md mx-auto">
        {tabs.map((tab) => {
          const Icon = tab.icon;
          const isActive =
            currentPage === tab.id ||
            (tab.id === 'practice' && (currentPage === 'module-quiz-prep' || currentPage === 'past-exams'));

          return (
            <button
              key={tab.id}
              onClick={() => onNavigate(tab.id)}
              className={`min-h-[48px] flex flex-col items-center justify-center py-1.5 px-1 rounded-xl transition-all cursor-pointer active:scale-95 ${
                isActive
                  ? 'text-teal-600 dark:text-teal-400 bg-teal-50/80 dark:bg-teal-500/15 font-bold shadow-2xs'
                  : 'text-slate-500 dark:text-slate-400 hover:text-slate-900 dark:hover:text-slate-200 font-medium'
              }`}
            >
              <Icon className={`w-5 h-5 mb-0.5 ${isActive ? 'stroke-[2.5]' : ''}`} />
              <span className="text-[10px] leading-tight tracking-tight truncate max-w-full font-medium">
                {tab.label}
              </span>
            </button>
          );
        })}
      </div>
    </nav>
  );
};
