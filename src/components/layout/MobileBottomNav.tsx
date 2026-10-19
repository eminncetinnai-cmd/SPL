import React from 'react';
import { Home, Sparkles, Zap, FileText, Layers } from 'lucide-react';

interface MobileBottomNavProps {
  currentPage: string;
  onNavigate: (page: string, params?: any) => void;
}

export const MobileBottomNav: React.FC<MobileBottomNavProps> = ({ currentPage, onNavigate }) => {
  const tabs = [
    { id: 'home', label: 'Ana Sayfa', icon: Home },
    { id: 'practice', label: 'Test Çöz', icon: Sparkles },
    { id: 'cheat-sheet', label: 'Hap Bilgi', icon: Zap },
    { id: 'study-notes', label: 'Ders Notu', icon: FileText },
    { id: 'flashcards', label: 'Kartlar', icon: Layers },
  ];

  return (
    <nav className="md:hidden fixed bottom-0 inset-x-0 z-40 bg-white/95 dark:bg-fintech-surface/95 backdrop-blur-md border-t border-slate-200 dark:border-fintech-border px-1 py-1.5 no-print shadow-lg">
      <div className="grid grid-cols-5 gap-0.5 max-w-md mx-auto">
        {tabs.map((tab) => {
          const Icon = tab.icon;
          const isActive =
            currentPage === tab.id ||
            (tab.id === 'practice' && (currentPage === 'module-quiz-prep' || currentPage === 'past-exams'));

          return (
            <button
              key={tab.id}
              onClick={() => onNavigate(tab.id)}
              className={`flex flex-col items-center justify-center py-1.5 px-1 rounded-xl transition-all cursor-pointer ${
                isActive
                  ? 'text-teal-600 dark:text-teal-400 bg-teal-50/80 dark:bg-teal-500/15 font-bold'
                  : 'text-slate-500 dark:text-slate-400 hover:text-slate-900 dark:hover:text-slate-200 font-medium'
              }`}
            >
              <Icon className={`w-4 h-4 mb-0.5 ${isActive ? 'stroke-[2.5]' : ''}`} />
              <span className="text-[10px] leading-tight tracking-tight truncate max-w-full">
                {tab.label}
              </span>
            </button>
          );
        })}
      </div>
    </nav>
  );
};
