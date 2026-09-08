import React from 'react';
import { 
  Scale, 
  Coins, 
  Building2, 
  ShieldCheck, 
  Play, 
  BookOpen, 
  Layers,
  TrendingUp, 
  CheckCircle,
  Sparkles
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
      case 'Scale': return Scale;
      case 'Coins': return Coins;
      case 'Building2': return Building2;
      case 'ShieldCheck': return ShieldCheck;
      default: return Scale;
    }
  };

  return (
    <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-5">
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

        const totalQuestionsInMod = (allQuestionsData as any[]).filter(q => q.module_id === mod.id).length;
        const seenInMod = getSeenCountByModule(mod.id as ModuleId);
        const unseenInMod = Math.max(0, totalQuestionsInMod - seenInMod);
        const percentSolved = totalQuestionsInMod > 0 ? Math.round((seenInMod / totalQuestionsInMod) * 100) : 0;

        const isPassed = stats.bestScore >= 50;

        return (
          <div
            key={mod.id}
            className={`group bg-white dark:bg-fintech-surface rounded-2xl border border-slate-200 dark:border-fintech-border hover:border-teal-500/50 p-5 space-y-4 shadow-sm hover:shadow-md transition-all duration-200 hover:-translate-y-1 relative flex flex-col justify-between`}
          >
            {/* Top Info */}
            <div className="space-y-3">
              <div className="flex items-center justify-between">
                <div className="flex items-center gap-2">
                  <div className={`p-2.5 rounded-xl bg-teal-50 dark:bg-slate-800 text-teal-700 dark:text-teal-400`}>
                    <Icon className="w-5 h-5" />
                  </div>
                  <span className="font-mono text-xs font-bold px-2 py-0.5 rounded-md bg-slate-100 dark:bg-fintech-card border border-slate-200 dark:border-fintech-border text-slate-700 dark:text-slate-300">
                    Modül {mod.code}
                  </span>
                </div>

                {stats.totalQuestions > 0 ? (
                  <span className={`text-[11px] font-mono font-bold px-2 py-0.5 rounded-full ${
                    isPassed ? 'bg-emerald-50 text-emerald-800 border border-emerald-200 dark:bg-emerald-500/15 dark:text-emerald-300 dark:border-emerald-500/30' : 'bg-amber-50 text-amber-800 border border-amber-200 dark:bg-amber-500/15 dark:text-amber-300 dark:border-amber-500/30'
                  }`}>
                    {isPassed ? 'BARAJI GEÇTİ' : `ÇALIŞILIYOR (%${stats.averageAccuracy})`}
                  </span>
                ) : (
                  <span className="text-[10px] font-mono text-slate-500 dark:text-slate-400 px-2 py-0.5 rounded bg-slate-100 dark:bg-slate-800/60 border border-slate-200 dark:border-slate-700/50 font-semibold">
                    TEST BEKLENİYOR
                  </span>
                )}
              </div>

              <div>
                <h4 className="font-black text-slate-900 dark:text-slate-100 text-sm sm:text-base group-hover:text-teal-700 dark:group-hover:text-teal-300 transition-colors leading-snug">
                  {mod.short_name}
                </h4>
                <p className="text-xs text-slate-600 dark:text-slate-400 mt-1 line-clamp-2 leading-relaxed">
                  {mod.description}
                </p>
              </div>

              {/* Soru Havuzu & Çözülmemiş Soru Durumu */}
              <div className="p-2.5 rounded-xl bg-slate-50 dark:bg-fintech-card/80 border border-slate-200 dark:border-fintech-border space-y-1.5">
                <div className="flex items-center justify-between text-[11px] font-mono">
                  <span className="text-slate-600 dark:text-slate-400 font-medium">Soru Havuzu:</span>
                  <span className="font-bold text-teal-800 dark:text-teal-300">{seenInMod} / {totalQuestionsInMod} Çözüldü</span>
                </div>

                <div className="w-full h-1.5 bg-slate-200 dark:bg-slate-800 rounded-full overflow-hidden">
                  <div 
                    className="h-full bg-gradient-to-r from-teal-600 to-emerald-500 rounded-full transition-all duration-500" 
                    style={{ width: `${percentSolved}%` }}
                  />
                </div>

                <div className="flex items-center justify-between text-[10px] pt-0.5">
                  <span className={unseenInMod > 0 ? 'text-amber-800 dark:text-amber-400 font-mono font-bold' : 'text-emerald-800 dark:text-emerald-400 font-mono font-bold'}>
                    {unseenInMod > 0 ? `✨ ${unseenInMod} Çözülmemiş Taze Soru` : `🏆 ${totalQuestionsInMod}/${totalQuestionsInMod} Tamamlandı`}
                  </span>
                  {onNavigate && unseenInMod > 0 && (
                    <button
                      type="button"
                      onClick={() => onNavigate('explorer', { moduleId: mod.id, status: 'unseen' })}
                      className="text-teal-700 dark:text-teal-400 hover:text-teal-900 dark:hover:text-teal-300 hover:underline font-bold"
                    >
                      Gör &rarr;
                    </button>
                  )}
                </div>
              </div>

              {/* Progress Stats */}
              <div className="pt-1 border-t border-slate-200 dark:border-fintech-border/60 grid grid-cols-2 gap-2 text-xs">
                <div className="bg-slate-50 dark:bg-fintech-card/60 p-2 rounded-xl border border-slate-200 dark:border-fintech-border">
                  <span className="text-[10px] text-slate-500 dark:text-slate-400 block uppercase font-mono font-semibold">Ort. Başarı</span>
                  <span className={`font-mono font-bold text-sm ${
                    stats.totalQuestions > 0 
                      ? stats.averageAccuracy >= 50 ? 'text-teal-700 dark:text-teal-300' : 'text-amber-700 dark:text-amber-400' 
                      : 'text-slate-400'
                  }`}>
                    {stats.totalQuestions > 0 ? `%${stats.averageAccuracy}` : '-'}
                  </span>
                </div>
                <div className="bg-slate-50 dark:bg-fintech-card/60 p-2 rounded-xl border border-slate-200 dark:border-fintech-border">
                  <span className="text-[10px] text-slate-500 dark:text-slate-400 block uppercase font-mono font-semibold">En İyi Skor</span>
                  <span className="font-mono font-bold text-sm text-emerald-700 dark:text-emerald-400">
                    {stats.bestScore > 0 ? `${stats.bestScore} / 100` : '-'}
                  </span>
                </div>
              </div>
            </div>

            {/* Actions */}
            <div className="pt-2 space-y-2">
              <button
                onClick={() => handleStart(mod.id as ModuleId)}
                className="w-full flex items-center justify-center gap-2 py-2.5 px-4 rounded-xl bg-gradient-to-r from-teal-600 to-emerald-600 hover:from-teal-500 hover:to-emerald-500 text-white font-bold text-xs shadow-xs active:scale-95 transition-all"
              >
                <Play className="w-3.5 h-3.5 fill-white" />
                <span>Pratik Testi Başlat</span>
              </button>

              <div className="grid grid-cols-2 gap-2">
                <button
                  onClick={() => handleFlashcards(mod.id as ModuleId)}
                  className="flex items-center justify-center gap-1.5 py-2 px-3 rounded-xl bg-teal-50 hover:bg-teal-100 dark:bg-teal-500/10 dark:hover:bg-teal-500/20 text-teal-800 dark:text-teal-300 border border-teal-200 dark:border-teal-500/30 text-xs font-bold transition-all"
                >
                  <Layers className="w-3.5 h-3.5" />
                  <span>100 Kart</span>
                </button>

                <button
                  onClick={() => handleNotes(mod.id as ModuleId)}
                  className="flex items-center justify-center gap-1.5 py-2 px-3 rounded-xl bg-slate-100 hover:bg-slate-200 text-slate-700 hover:text-slate-900 border border-slate-200 dark:bg-fintech-card dark:hover:bg-fintech-cardHover dark:text-slate-300 dark:hover:text-white dark:border-fintech-border text-xs font-bold transition-all"
                >
                  <BookOpen className="w-3.5 h-3.5 text-slate-500 dark:text-slate-400" />
                  <span>Ders Notu</span>
                </button>
              </div>
            </div>
          </div>
        );
      })}
    </div>
  );
};
