import React from 'react';
import {
  Sparkles,
  Play,
  AlertTriangle,
  Star,
  CheckCircle,
  BarChart3,
  ArrowRight,
  Zap,
  Layers,
} from 'lucide-react';
import { ModuleProgressCards } from '../components/dashboard/ModuleProgressCards';
import { useProgressStore } from '../stores/progressStore';
import allQuestionsData from '../data/all_questions.json';

interface HomePageProps {
  onNavigate: (page: string, params?: any) => void;
}

export const HomePage: React.FC<HomePageProps> = ({ onNavigate }) => {
  const { history, mistakes, bookmarks, learnedCards, moduleStats, seenQuestionIds } = useProgressStore();

  const mistakeCount = Object.values(mistakes).filter((m) => !m.resolved).length;
  const bookmarkCount = bookmarks.length;
  const learnedCardsCount = learnedCards.length;

  const totalAnsweredFromModules = Object.values(moduleStats).reduce((acc, m) => acc + m.totalQuestions, 0);
  const totalCorrectFromModules = Object.values(moduleStats).reduce((acc, m) => acc + m.totalCorrect, 0);

  const totalAnswered = Math.max(totalAnsweredFromModules, history.reduce((acc, h) => acc + h.total_questions, 0));
  const totalCorrect = Math.max(totalCorrectFromModules, history.reduce((acc, h) => acc + h.correct_count, 0));
  const overallAccuracy = totalAnswered > 0 ? Math.round((totalCorrect / totalAnswered) * 100) : null;

  return (
    <div className="space-y-5 sm:space-y-6 animate-fade-in">
      {/* Compact Hero & Quick Actions */}
      <div className="rounded-2xl sm:rounded-3xl bg-white dark:bg-fintech-surface border border-slate-200 dark:border-teal-500/30 p-4 sm:p-6 shadow-sm space-y-4">
        <div className="flex flex-col lg:flex-row lg:items-center justify-between gap-4">
          <div className="space-y-1.5 max-w-2xl">
            <div className="inline-flex items-center gap-1.5 px-2.5 py-0.5 rounded-full bg-teal-50 dark:bg-teal-500/15 text-teal-800 dark:text-teal-300 border border-teal-200 dark:border-teal-500/30 text-[11px] font-mono font-bold">
              <Sparkles className="w-3 h-3 text-teal-600 dark:text-teal-400" />
              <span>SPK SPL DÜZEY 1 HAZIRLIK PLATFORMU</span>
            </div>
            <h1 className="text-xl sm:text-2xl lg:text-3xl font-black text-slate-900 dark:text-white tracking-tight">
              Sınava Odaklı Çalışma Merkezi
            </h1>
            <div className="flex flex-wrap items-center gap-3 text-xs font-mono text-slate-600 dark:text-slate-400">
              <span className="flex items-center gap-1 text-slate-700 dark:text-slate-300 font-semibold">
                <CheckCircle className="w-3.5 h-3.5 text-emerald-600 dark:text-emerald-400" /> Modül Barajı: ≥ 50
              </span>
              <span className="flex items-center gap-1 text-slate-700 dark:text-slate-300 font-semibold">
                <CheckCircle className="w-3.5 h-3.5 text-teal-600 dark:text-teal-400" /> Ortalama Baraj: ≥ 60
              </span>
            </div>
          </div>

          {/* Primary Action Buttons */}
          <div className="grid grid-cols-1 sm:grid-cols-3 gap-2 w-full lg:w-auto shrink-0">
            <button
              onClick={() => onNavigate('practice', { filterMode: 'unseen' })}
              className="flex items-center justify-center gap-2 px-4 py-3 rounded-xl bg-teal-600 hover:bg-teal-700 active:bg-teal-800 text-white font-black text-xs sm:text-sm shadow-sm active:scale-95 transition-all cursor-pointer"
            >
              <Play className="w-4 h-4 fill-white text-white" />
              <span>Karma Test Başlat</span>
            </button>

            <button
              onClick={() => onNavigate('cheat-sheet')}
              className="flex items-center justify-center gap-1.5 px-4 py-3 rounded-xl bg-amber-400 hover:bg-amber-500 text-slate-950 font-bold text-xs sm:text-sm shadow-xs active:scale-95 transition-all cursor-pointer"
            >
              <Zap className="w-4 h-4 fill-slate-950 text-slate-950" />
              <span>249 Altın Kural</span>
            </button>

            <button
              onClick={() => onNavigate('mistakes')}
              className={`flex items-center justify-center gap-1.5 px-4 py-3 rounded-xl font-bold text-xs sm:text-sm shadow-xs active:scale-95 transition-all cursor-pointer ${
                mistakeCount > 0
                  ? 'bg-rose-500 hover:bg-rose-600 text-white'
                  : 'bg-slate-100 dark:bg-fintech-card text-slate-700 dark:text-slate-300 border border-slate-200 dark:border-fintech-border'
              }`}
            >
              <AlertTriangle className="w-4 h-4" />
              <span>Hata Defterim ({mistakeCount})</span>
            </button>
          </div>
        </div>

        {/* Compact KPI Strip */}
        <div className="grid grid-cols-2 sm:grid-cols-4 gap-2.5 pt-3 border-t border-slate-100 dark:border-fintech-border/60">
          <div className="p-2.5 rounded-xl bg-slate-50 dark:bg-fintech-card border border-slate-200/80 dark:border-fintech-border flex items-center justify-between">
            <span className="text-[11px] text-slate-500 dark:text-slate-400 font-medium">Soru Havuzu</span>
            <span className="text-xs sm:text-sm font-black font-mono text-slate-900 dark:text-white">
              {seenQuestionIds.length} / {(allQuestionsData as any[]).length}
            </span>
          </div>

          <div className="p-2.5 rounded-xl bg-slate-50 dark:bg-fintech-card border border-slate-200/80 dark:border-fintech-border flex items-center justify-between">
            <span className="text-[11px] text-slate-500 dark:text-slate-400 font-medium">Başarı Oranı</span>
            <span className={`text-xs sm:text-sm font-black font-mono ${
              overallAccuracy !== null
                ? overallAccuracy >= 60
                  ? 'text-emerald-600 dark:text-emerald-400'
                  : 'text-amber-600 dark:text-amber-400'
                : 'text-slate-400'
            }`}>
              {overallAccuracy !== null ? `%${overallAccuracy}` : '-'}
            </span>
          </div>

          <div className="p-2.5 rounded-xl bg-slate-50 dark:bg-fintech-card border border-slate-200/80 dark:border-fintech-border flex items-center justify-between">
            <span className="text-[11px] text-slate-500 dark:text-slate-400 font-medium">Flashcard</span>
            <span className="text-xs sm:text-sm font-black font-mono text-teal-700 dark:text-teal-300">
              {learnedCardsCount} / 400
            </span>
          </div>

          <div className="p-2.5 rounded-xl bg-slate-50 dark:bg-fintech-card border border-slate-200/80 dark:border-fintech-border flex items-center justify-between">
            <span className="text-[11px] text-slate-500 dark:text-slate-400 font-medium">Yanlış Defteri</span>
            <span className="text-xs sm:text-sm font-black font-mono text-rose-600 dark:text-rose-400">
              {mistakeCount} Soru
            </span>
          </div>
        </div>
      </div>

      {/* 4 SPL Module Cards Section */}
      <div className="space-y-3">
        <div className="flex items-center justify-between px-1">
          <h2 className="text-base sm:text-lg font-black text-slate-900 dark:text-white tracking-tight">
            Sınav Dersleri (4 Modül)
          </h2>
          <span className="text-xs font-mono text-slate-500 dark:text-slate-400">
            Test • Ders Notu • Kartlar
          </span>
        </div>

        <ModuleProgressCards onNavigate={onNavigate} />
      </div>

      {/* Quick Study Tools Grid (2x2 on Mobile, 4 cols on Desktop) */}
      <div className="grid grid-cols-2 lg:grid-cols-4 gap-3">
        <button
          onClick={() => onNavigate('mistakes')}
          className="p-3.5 sm:p-4 rounded-2xl bg-white dark:bg-fintech-surface hover:bg-slate-50 dark:hover:bg-fintech-card border border-slate-200 dark:border-fintech-border text-left transition-all flex items-center justify-between group shadow-xs cursor-pointer"
        >
          <div className="min-w-0 pr-2">
            <div className="flex items-center gap-1.5 text-rose-600 dark:text-rose-400 font-bold text-xs sm:text-sm">
              <AlertTriangle className="w-4 h-4 shrink-0" />
              <span className="truncate">Yanlışlarım</span>
            </div>
            <span className="text-[11px] text-slate-500 dark:text-slate-400 block mt-0.5">
              {mistakeCount > 0 ? `${mistakeCount} hatalı soru` : 'Hata kaydı yok'}
            </span>
          </div>
          <ArrowRight className="w-4 h-4 text-slate-400 group-hover:text-rose-500 shrink-0" />
        </button>

        <button
          onClick={() => onNavigate('bookmarks')}
          className="p-3.5 sm:p-4 rounded-2xl bg-white dark:bg-fintech-surface hover:bg-slate-50 dark:hover:bg-fintech-card border border-slate-200 dark:border-fintech-border text-left transition-all flex items-center justify-between group shadow-xs cursor-pointer"
        >
          <div className="min-w-0 pr-2">
            <div className="flex items-center gap-1.5 text-amber-600 dark:text-amber-400 font-bold text-xs sm:text-sm">
              <Star className="w-4 h-4 shrink-0" />
              <span className="truncate">Yıldızlı Sorular</span>
            </div>
            <span className="text-[11px] text-slate-500 dark:text-slate-400 block mt-0.5">
              {bookmarkCount} favori soru
            </span>
          </div>
          <ArrowRight className="w-4 h-4 text-slate-400 group-hover:text-amber-500 shrink-0" />
        </button>

        <button
          onClick={() => onNavigate('simulation-prep')}
          className="p-3.5 sm:p-4 rounded-2xl bg-white dark:bg-fintech-surface hover:bg-slate-50 dark:hover:bg-fintech-card border border-slate-200 dark:border-fintech-border text-left transition-all flex items-center justify-between group shadow-xs cursor-pointer"
        >
          <div className="min-w-0 pr-2">
            <div className="flex items-center gap-1.5 text-teal-600 dark:text-teal-400 font-bold text-xs sm:text-sm">
              <Sparkles className="w-4 h-4 shrink-0" />
              <span className="truncate">Deneme Sınavı</span>
            </div>
            <span className="text-[11px] text-slate-500 dark:text-slate-400 block mt-0.5">
              4 Ders Gerçek Prova
            </span>
          </div>
          <ArrowRight className="w-4 h-4 text-slate-400 group-hover:text-teal-500 shrink-0" />
        </button>

        <button
          onClick={() => onNavigate('flashcards')}
          className="p-3.5 sm:p-4 rounded-2xl bg-white dark:bg-fintech-surface hover:bg-slate-50 dark:hover:bg-fintech-card border border-slate-200 dark:border-fintech-border text-left transition-all flex items-center justify-between group shadow-xs cursor-pointer"
        >
          <div className="min-w-0 pr-2">
            <div className="flex items-center gap-1.5 text-emerald-600 dark:text-emerald-400 font-bold text-xs sm:text-sm">
              <Layers className="w-4 h-4 shrink-0" />
              <span className="truncate">Öğrenme Kartları</span>
            </div>
            <span className="text-[11px] text-slate-500 dark:text-slate-400 block mt-0.5">
              400 Kavram & Özet
            </span>
          </div>
          <ArrowRight className="w-4 h-4 text-slate-400 group-hover:text-emerald-500 shrink-0" />
        </button>
      </div>
    </div>
  );
};
