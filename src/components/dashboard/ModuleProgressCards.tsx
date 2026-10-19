import React from 'react';
import {
  Scale,
  Coins,
  Building2,
  ShieldCheck,
  Play,
  BookOpen,
  Layers,
} from 'lucide-react';
import modulesData from '../../data/modules.json';
import { useProgressStore } from '../../stores/progressStore';
import { ModuleId, ModuleInfo } from '../../types/exam';
import allQuestionsData from '../../data/all_questions.json';

interface ModuleProgressCardsProps {
  onNavigate?: (page: string, params?: any) => void;
  onStartQuiz?: (moduleId: ModuleId) => void;
  onReadNotes?: (moduleId: ModuleId) => void;
  onOpenFlashcards?: (moduleId: ModuleId) => void;
}

const MODULE_TOTAL_COUNTS: Record<string, number> = (allQuestionsData as any[]).reduce(
  (acc, q) => {
    acc[q.module_id] = (acc[q.module_id] || 0) + 1;
    return acc;
  },
  {} as Record<string, number>
);

export const ModuleProgressCards: React.FC<ModuleProgressCardsProps> = ({
  onNavigate,
  onStartQuiz,
  onReadNotes,
  onOpenFlashcards,
}) => {
  const { moduleStats, getSeenCountByModule } = useProgressStore();
  const modules = modulesData as ModuleInfo[];

  const handleStart = (id: ModuleId) => {
    if (onStartQuiz) onStartQuiz(id);
    else if (onNavigate) onNavigate('module-quiz-prep', { moduleId: id });
  };

  const handleNotes = (id: ModuleId) => {
    if (onReadNotes) onReadNotes(id);
    else if (onNavigate) onNavigate('study-notes', { moduleId: id });
  };

  const handleFlashcards = (id: ModuleId) => {
    if (onOpenFlashcards) onOpenFlashcards(id);
    else if (onNavigate) onNavigate('flashcards', { moduleId: id });
  };

  const getIcon = (iconName: string) => {
    switch (iconName) {
      case 'Scale':
        return Scale;
      case 'Coins':
        return Coins;
      case 'Building2':
        return Building2;
      case 'ShieldCheck':
        return ShieldCheck;
      default:
        return Scale;
    }
  };

  return (
    <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-3.5 sm:gap-4">
      {modules.map((mod) => {
        const Icon = getIcon(mod.icon);
        const stats = moduleStats[mod.id as ModuleId] || {
          attempts: 0,
          totalQuestions: 0,
          totalCorrect: 0,
          averageAccuracy: 0,
          bestScore: 0,
          lastScore: null,
        };

        const totalQuestionsInMod = MODULE_TOTAL_COUNTS[mod.id] || 0;
        const seenInMod = getSeenCountByModule(mod.id as ModuleId);
        const unseenInMod = Math.max(0, totalQuestionsInMod - seenInMod);
        const percentSolved =
          totalQuestionsInMod > 0 ? Math.round((seenInMod / totalQuestionsInMod) * 100) : 0;

        const isPassed = stats.averageAccuracy >= 50 && stats.totalQuestions > 0;

        return (
          <div
            key={mod.id}
            className="group bg-white dark:bg-fintech-surface rounded-2xl border border-slate-200 dark:border-fintech-border hover:border-teal-500/50 p-4 space-y-3 shadow-xs hover:shadow-md transition-all flex flex-col justify-between"
          >
            {/* Top Info */}
            <div className="space-y-2.5">
              <div className="flex items-center justify-between gap-2">
                <div className="flex items-center gap-2">
                  <div className="p-2 rounded-xl bg-teal-50 dark:bg-slate-800 text-teal-700 dark:text-teal-400">
                    <Icon className="w-4 h-4" />
                  </div>
                  <span className="font-mono text-xs font-bold px-2 py-0.5 rounded-md bg-slate-100 dark:bg-fintech-card border border-slate-200 dark:border-fintech-border text-slate-700 dark:text-slate-300">
                    {mod.code}
                  </span>
                </div>

                {stats.totalQuestions > 0 ? (
                  <span
                    className={`text-[10px] font-mono font-bold px-2 py-0.5 rounded-full ${
                      isPassed
                        ? 'bg-emerald-50 text-emerald-800 border border-emerald-200 dark:bg-emerald-500/15 dark:text-emerald-300 dark:border-emerald-500/30'
                        : 'bg-amber-50 text-amber-800 border border-amber-200 dark:bg-amber-500/15 dark:text-amber-300 dark:border-amber-500/30'
                    }`}
                  >
                    Başarı: %{stats.averageAccuracy}
                  </span>
                ) : (
                  <span className="text-[10px] font-mono text-slate-500 dark:text-slate-400 px-2 py-0.5 rounded bg-slate-100 dark:bg-slate-800/60">
                    {totalQuestionsInMod} Soru
                  </span>
                )}
              </div>

              <div>
                <h4 className="font-black text-slate-900 dark:text-slate-100 text-sm sm:text-base leading-snug">
                  {mod.short_name}
                </h4>
                <p className="text-[11px] text-slate-500 dark:text-slate-400 mt-0.5 line-clamp-1">
                  {mod.description}
                </p>
              </div>

              {/* Compact Progress Bar */}
              <div className="p-2.5 rounded-xl bg-slate-50 dark:bg-fintech-card/80 border border-slate-200/80 dark:border-fintech-border space-y-1.5">
                <div className="flex items-center justify-between text-[11px] font-mono">
                  <span className="text-slate-500 dark:text-slate-400">
                    {unseenInMod > 0 ? `${unseenInMod} taze soru` : 'Tamamlandı'}
                  </span>
                  <span className="font-bold text-teal-800 dark:text-teal-300">
                    {seenInMod}/{totalQuestionsInMod}
                  </span>
                </div>

                <div className="w-full h-1.5 bg-slate-200 dark:bg-slate-800 rounded-full overflow-hidden">
                  <div
                    className="h-full bg-gradient-to-r from-teal-600 to-emerald-500 rounded-full transition-all duration-500"
                    style={{ width: `${percentSolved}%` }}
                  />
                </div>
              </div>
            </div>

            {/* Actions */}
            <div className="pt-1 space-y-2">
              <button
                onClick={() => handleStart(mod.id as ModuleId)}
                className="w-full flex items-center justify-center gap-1.5 py-2.5 px-3 rounded-xl bg-teal-600 hover:bg-teal-700 text-white font-bold text-xs shadow-xs active:scale-95 transition-all cursor-pointer"
              >
                <Play className="w-3.5 h-3.5 fill-white" />
                <span>Test Çöz</span>
              </button>

              <div className="grid grid-cols-2 gap-1.5">
                <button
                  onClick={() => handleNotes(mod.id as ModuleId)}
                  className="flex items-center justify-center gap-1 py-2 px-2.5 rounded-xl bg-slate-100 hover:bg-slate-200 text-slate-700 dark:bg-fintech-card dark:hover:bg-fintech-cardHover dark:text-slate-300 border border-slate-200 dark:border-fintech-border text-xs font-bold transition-all cursor-pointer"
                >
                  <BookOpen className="w-3.5 h-3.5 text-cyan-600 dark:text-cyan-400" />
                  <span>Ders Notu</span>
                </button>

                <button
                  onClick={() => handleFlashcards(mod.id as ModuleId)}
                  className="flex items-center justify-center gap-1 py-2 px-2.5 rounded-xl bg-slate-100 hover:bg-slate-200 text-slate-700 dark:bg-fintech-card dark:hover:bg-fintech-cardHover dark:text-slate-300 border border-slate-200 dark:border-fintech-border text-xs font-bold transition-all cursor-pointer"
                >
                  <Layers className="w-3.5 h-3.5 text-teal-600 dark:text-teal-400" />
                  <span>100 Kart</span>
                </button>
              </div>
            </div>
          </div>
        );
      })}
    </div>
  );
};
