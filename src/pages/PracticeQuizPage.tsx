import React, { useState, useEffect, useRef, useMemo } from 'react';
import { 
  ArrowLeft, 
  ArrowRight, 
  CheckCircle2, 
  Sparkles, 
  RotateCcw, 
  Play, 
  BookOpen, 
  Scale, 
  Coins, 
  Building2, 
  ShieldCheck, 
  AlertCircle, 
  Zap, 
  Brain,
  ChevronDown,
  ChevronUp,
  X,
  SlidersHorizontal,
  Flame,
  Star,
  ListOrdered
} from 'lucide-react';
import { useQuizStore } from '../stores/quizStore';
import { useSettingsStore } from '../stores/settingsStore';
import { QuestionCard } from '../components/quiz/QuestionCard';
import { ExplanationPanel } from '../components/quiz/ExplanationPanel';
import { OpticalForm } from '../components/quiz/OpticalForm';
import { ExamTimer } from '../components/quiz/ExamTimer';
import { soundManager } from '../utils/soundEffects';
import { useProgressStore } from '../stores/progressStore';
import { ModuleId, Question } from '../types/exam';
import modulesData from '../data/modules.json';

import allQuestionsData from '../data/all_questions.json';

const ALL_QUESTIONS = allQuestionsData as Question[];
const QUESTION_BY_ID = new Map<string, Question>(ALL_QUESTIONS.map((q) => [q.id, q]));
const MODULE_TOTAL_COUNTS: Record<string, number> = ALL_QUESTIONS.reduce((acc, q) => {
  acc[q.module_id] = (acc[q.module_id] || 0) + 1;
  return acc;
}, {} as Record<string, number>);

interface PracticeQuizPageProps {
  initialModuleId?: ModuleId;
  initialFilterMode?: 'unseen' | 'all' | 'mistakes' | 'bookmarks';
  initialTestMode?: 'practice' | 'simulation';
  initialSourceFilter?: 'all' | 'master' | 'cikmis' | 'ogretici' | 'genel';
  onNavigate: (page: string, params?: any) => void;
}

export const PracticeQuizPage: React.FC<PracticeQuizPageProps> = ({
  initialModuleId,
  initialFilterMode,
  initialTestMode,
  initialSourceFilter,
  onNavigate,
}) => {
  const {
    currentSession,
    activeQuestion,
    activeAnswer,
    isAnswerLocked,
    explanationRead,
    startQuiz,
    selectOption,
    setExplanationRead,
    goToQuestion,
    nextQuestion,
    prevQuestion,
    finishQuiz,
    resetSession,
    updateTimer,
  } = useQuizStore();

  const { soundEnabled } = useSettingsStore();
  const {
    seenQuestionIds,
    avoidQuestionRepetition,
    setAvoidRepetition,
    resetSeenQuestions,
    isQuestionSeen,
    getSeenCountByModule,
    mistakes,
    bookmarks,
  } = useProgressStore();

  // Setup state for configuration
  const [selectedModule, setSelectedModule] = useState<ModuleId | 'all'>(initialModuleId || 'all');
  const [filterMode, setFilterMode] = useState<'unseen' | 'all' | 'mistakes' | 'bookmarks'>(
    initialFilterMode || 'unseen'
  );
  const [cognitiveFilter, setCognitiveFilter] = useState<'all' | 'KB1_Kavramsal' | 'KB2_Muhakeme' | 'KB3_Vaka'>('all');
  const [questionCount, setQuestionCount] = useState<number>(25);
  const [showExitConfirm, setShowExitConfirm] = useState(false);
  const [showAdvancedFilters, setShowAdvancedFilters] = useState(false);
  const [showMobileOptical, setShowMobileOptical] = useState(false);

  const allQs = ALL_QUESTIONS;

  const candidatePool = useMemo(() => {
    return allQs.filter((q) => {
      if (selectedModule !== 'all' && q.module_id !== selectedModule) return false;
      if (cognitiveFilter !== 'all' && q.cognitive_skill !== cognitiveFilter) return false;
      if (initialSourceFilter === 'cikmis' && q.source !== 'cikmis') return false;
      if (initialSourceFilter === 'genel' && q.source === 'cikmis') return false;
      if (
        initialSourceFilter &&
        initialSourceFilter !== 'all' &&
        initialSourceFilter !== 'genel' &&
        initialSourceFilter !== 'cikmis' &&
        q.source !== initialSourceFilter
      ) {
        return false;
      }
      return true;
    });
  }, [allQs, selectedModule, cognitiveFilter, initialSourceFilter]);

  const kbCounts = useMemo(() => {
    let all = 0;
    let KB3_Vaka = 0;
    let KB2_Muhakeme = 0;
    let KB1_Kavramsal = 0;
    for (let i = 0; i < allQs.length; i++) {
      const q = allQs[i];
      if (selectedModule === 'all' || q.module_id === selectedModule) {
        all++;
        if (q.cognitive_skill === 'KB3_Vaka') KB3_Vaka++;
        else if (q.cognitive_skill === 'KB2_Muhakeme') KB2_Muhakeme++;
        else if (q.cognitive_skill === 'KB1_Kavramsal') KB1_Kavramsal++;
      }
    }
    return { all, KB3_Vaka, KB2_Muhakeme, KB1_Kavramsal };
  }, [allQs, selectedModule]);

  const totalModulePool = candidatePool.length;
  const seenCount = useMemo(
    () => candidatePool.filter((q) => isQuestionSeen(q.id)).length,
    [candidatePool, isQuestionSeen, seenQuestionIds]
  );
  const unseenCount = Math.max(0, totalModulePool - seenCount);

  // Active mistakes and bookmarks in the selected scope
  const mistakeCountInScope = useMemo(
    () =>
      Object.values(mistakes).filter(
        (m) => !m.resolved && (selectedModule === 'all' || m.question.module_id === selectedModule)
      ).length,
    [mistakes, selectedModule]
  );

  const bookmarkCountInScope = useMemo(
    () =>
      bookmarks.filter((bId) => {
        const q = QUESTION_BY_ID.get(bId);
        return q && (selectedModule === 'all' || q.module_id === selectedModule);
      }).length,
    [bookmarks, selectedModule]
  );

  useEffect(() => {
    if (initialModuleId) {
      setSelectedModule(initialModuleId);
    }
  }, [initialModuleId]);

  useEffect(() => {
    if (initialFilterMode) {
      setFilterMode(initialFilterMode);
    }
  }, [initialFilterMode]);

  const handleSelectOptionWithSound = (key: 'A' | 'B' | 'C' | 'D' | 'E') => {
    if (!activeQuestion) return;
    const isCorrect = activeQuestion.correct_answer === key;

    if (soundEnabled) {
      if (isCorrect) {
        soundManager.playCorrect();
      } else {
        soundManager.playWrong();
      }
    }

    selectOption(key);
  };

  // Keyboard shortcut listener
  useEffect(() => {
    const handleKeyDown = (e: KeyboardEvent) => {
      if (!currentSession || currentSession.is_completed) return;

      const key = e.key.toUpperCase();
      if (['A', 'B', 'C', 'D', 'E'].includes(key)) {
        if (!isAnswerLocked) {
          handleSelectOptionWithSound(key as any);
        }
      } else if (['1', '2', '3', '4', '5'].includes(e.key)) {
        const keyMap: Record<string, any> = { '1': 'A', '2': 'B', '3': 'C', '4': 'D', '5': 'E' };
        if (!isAnswerLocked) {
          handleSelectOptionWithSound(keyMap[e.key]);
        }
      } else if (e.key === 'ArrowRight' || e.key === 'Enter' || e.code === 'Space') {
        if (e.target instanceof HTMLInputElement || e.target instanceof HTMLTextAreaElement) return;
        e.preventDefault();
        handleNextOrFinish();
      } else if (e.key === 'ArrowLeft') {
        prevQuestion();
      }
    };

    window.addEventListener('keydown', handleKeyDown);
    return () => window.removeEventListener('keydown', handleKeyDown);
  }, [currentSession, nextQuestion, prevQuestion, isAnswerLocked, activeQuestion, soundEnabled]);

  const handleNextOrFinish = () => {
    if (!currentSession) return;
    if (currentSession.current_index === currentSession.questions.length - 1) {
      handleFinish();
    } else {
      nextQuestion();
    }
  };

  const handleResetSeenPool = () => {
    const scopeText = selectedModule === 'all' 
      ? 'Tüm modüllere ait çözülmüş soru havuzu döngüsü' 
      : `Modül ${selectedModule} dersine ait çözülmüş soru havuzu döngüsü`;
    
    if (window.confirm(`${scopeText} sıfırlanacak ve sorular tekrar taze (çözülmemiş) olarak testlere dahil edilecektir.\n\nSınav geçmişiniz ve başarı karneleriniz korunur.\n\nSıfırlamak istiyor musunuz?`)) {
      resetSeenQuestions(selectedModule);
      alert('Soru havuzu başarıyla sıfırlandı. Tüm sorular taze olarak hazır.');
    }
  };

  const handleStart = () => {
    // Validate question count for specialized filters
    if (filterMode === 'mistakes' && mistakeCountInScope === 0) {
      alert('Seçili kapsamda kayıtlı hatalı sorunuz bulunmamaktadır.');
      return;
    }
    if (filterMode === 'bookmarks' && bookmarkCountInScope === 0) {
      alert('Seçili kapsamda yıldızlanmış sorunuz bulunmamaktadır.');
      return;
    }

    startQuiz({
      mode: 'practice',
      moduleId: selectedModule,
      questionCount,
      filterMode,
      title: selectedModule === 'all'
        ? `Tüm Modüller Soru Çözümü (${questionCount} Soru)`
        : `Modül ${selectedModule} Soru Çözümü (${questionCount} Soru)`,
    });
  };

  const handleQuickStart = (type: 'fresh' | 'mistakes' | 'all_pool') => {
    if (type === 'mistakes') {
      if (mistakeCountInScope === 0) {
        alert('Seçili kapsamda kayıtlı hatalı sorunuz bulunmamaktadır.');
        return;
      }
      const count = Math.min(25, mistakeCountInScope);
      startQuiz({
        mode: 'practice',
        moduleId: selectedModule,
        questionCount: count,
        filterMode: 'mistakes',
        title: selectedModule === 'all'
          ? `Tüm Dersler - Hataları Temizleme (${count} Soru)`
          : `Modül ${selectedModule} - Hataları Temizleme (${count} Soru)`,
      });
      return;
    }

    if (type === 'all_pool') {
      const count = 25;
      startQuiz({
        mode: 'practice',
        moduleId: selectedModule,
        questionCount: count,
        filterMode: 'all',
        title: selectedModule === 'all'
          ? `Tüm Dersler Karma Test (${count} Soru)`
          : `Modül ${selectedModule} Karma Test (${count} Soru)`,
      });
      return;
    }

    // type === 'fresh'
    const targetFilter = unseenCount > 0 ? 'unseen' : 'all';
    const count = 25;
    startQuiz({
      mode: 'practice',
      moduleId: selectedModule,
      questionCount: count,
      filterMode: targetFilter,
      title: selectedModule === 'all'
        ? `Tüm Dersler Çözülmemiş Test (${count} Soru)`
        : `Modül ${selectedModule} Çözülmemiş Test (${count} Soru)`,
    });
  };

  const handleFinish = () => {
    const completed = finishQuiz();
    if (completed) {
      onNavigate('results');
    }
  };

  // If no active session, show setup configuration
  if (!currentSession || currentSession.is_completed) {
    return (
      <div className="max-w-4xl mx-auto space-y-4 sm:space-y-6 animate-fade-in pb-10">
        {/* Header */}
        <div className="flex items-center justify-between gap-3">
          <div className="flex items-center gap-3">
            <button
              onClick={() => onNavigate('home')}
              className="p-2 rounded-xl bg-white dark:bg-fintech-surface hover:bg-slate-100 dark:hover:bg-fintech-card border border-slate-200 dark:border-fintech-border text-slate-700 dark:text-slate-300 shadow-xs transition-all active:scale-95"
            >
              <ArrowLeft className="w-4 h-4 sm:w-5 sm:h-5" />
            </button>
            <div>
              <h1 className="text-lg sm:text-2xl font-black text-slate-900 dark:text-white tracking-tight">
                Test & Soru Çözümü
              </h1>
              <p className="text-xs text-slate-500 dark:text-slate-400">
                1-dokunuş hızlı testler veya modül seçimiyle hemen başlayın
              </p>
            </div>
          </div>

          {seenCount > 0 && (
            <button
              type="button"
              onClick={handleResetSeenPool}
              className="inline-flex items-center gap-1.5 px-2.5 py-1.5 rounded-xl text-xs font-bold text-amber-700 dark:text-amber-300 bg-amber-50 hover:bg-amber-100 dark:bg-amber-500/10 border border-amber-300 dark:border-amber-500/30 transition-all cursor-pointer shrink-0 active:scale-95"
              title="Çözülmüş soruları sıfırlayarak tüm soruları taze yap"
            >
              <RotateCcw className="w-3.5 h-3.5 text-amber-600 dark:text-amber-400" />
              <span>Sıfırla ({seenCount})</span>
            </button>
          )}
        </div>

        {/* 1. Ders / Modül Seçimi */}
        <div className="bg-white dark:bg-fintech-surface rounded-2xl sm:rounded-3xl border border-slate-200 dark:border-fintech-border p-4 sm:p-5 space-y-3 shadow-xs">
          <div className="flex items-center justify-between">
            <label className="text-xs font-mono uppercase tracking-wider text-slate-700 dark:text-slate-300 font-bold flex items-center gap-1.5">
              <BookOpen className="w-3.5 h-3.5 text-teal-600 dark:text-teal-400" />
              <span>Ders Seçimi</span>
            </label>
            <span className="text-[11px] font-mono text-teal-600 dark:text-teal-400 font-bold">
              {candidatePool.length} Soru Hazır
            </span>
          </div>

          <div className="grid grid-cols-2 sm:grid-cols-5 gap-2">
            <button
              onClick={() => setSelectedModule('all')}
              className={`p-3 rounded-2xl border text-left transition-all col-span-2 sm:col-span-1 active:scale-[0.98] ${
                selectedModule === 'all'
                  ? 'bg-teal-50 dark:bg-teal-500/15 border-teal-500 text-teal-900 dark:text-teal-300 ring-2 ring-teal-500/30 shadow-xs'
                  : 'bg-slate-50 dark:bg-fintech-card border-slate-200 dark:border-fintech-border text-slate-700 dark:text-slate-300 hover:border-slate-300'
              }`}
            >
              <div className="flex items-center justify-between mb-1">
                <span className="font-mono text-[10px] font-bold text-teal-600 dark:text-teal-400">KARMA</span>
                <span className="text-[10px] font-mono font-bold text-slate-400">{allQs.length}</span>
              </div>
              <span className="font-bold text-xs sm:text-sm block text-slate-900 dark:text-white truncate">Tüm Dersler</span>
              <span className="text-[10px] text-slate-500 dark:text-slate-400 block mt-0.5">Gerçek Sınav Dağılımı</span>
            </button>

            {modulesData.map((m) => {
              const modTotal = MODULE_TOTAL_COUNTS[m.id] || 0;
              const modSeen = getSeenCountByModule(m.id as ModuleId);
              const modUnseen = Math.max(0, modTotal - modSeen);

              return (
                <button
                  key={m.id}
                  onClick={() => setSelectedModule(m.id as ModuleId)}
                  className={`p-3 rounded-2xl border text-left transition-all active:scale-[0.98] ${
                    selectedModule === m.id
                      ? 'bg-teal-50 dark:bg-teal-500/15 border-teal-500 text-teal-900 dark:text-teal-300 ring-2 ring-teal-500/30 shadow-xs'
                      : 'bg-slate-50 dark:bg-fintech-card border-slate-200 dark:border-fintech-border text-slate-700 dark:text-slate-300 hover:border-slate-300'
                  }`}
                >
                  <div className="flex items-center justify-between mb-1">
                    <span className="font-mono text-[10px] font-bold text-teal-600 dark:text-teal-400">
                      Modül {m.code}
                    </span>
                    <span className="text-[10px] font-mono font-bold text-slate-400">{modTotal}</span>
                  </div>
                  <span className="font-bold text-xs sm:text-sm text-slate-900 dark:text-white block truncate">
                    {m.short_name}
                  </span>
                  <span className="text-[10px] text-teal-600 dark:text-teal-400 font-semibold block mt-0.5">
                    {modUnseen} taze soru
                  </span>
                </button>
              );
            })}
          </div>
        </div>

        {/* 2. ⚡ 1-Dokunuş Hızlı Başlat Kartları (Önerilen) */}
        <div className="space-y-2.5">
          <label className="text-xs font-mono uppercase tracking-wider text-slate-700 dark:text-slate-300 font-bold flex items-center gap-1.5 px-1">
            <Flame className="w-3.5 h-3.5 text-amber-500" />
            <span>Hızlı Başlat (Önerilen)</span>
          </label>

          <div className="grid grid-cols-1 sm:grid-cols-3 gap-3">
            {/* Quick 1: 25 Taze Soru */}
            <button
              onClick={() => handleQuickStart('fresh')}
              className="p-4 rounded-2xl bg-gradient-to-br from-teal-600 to-emerald-600 hover:from-teal-700 hover:to-emerald-700 text-white shadow-md shadow-teal-700/20 text-left transition-all active:scale-[0.98] cursor-pointer flex flex-col justify-between"
            >
              <div>
                <div className="flex items-center justify-between mb-2">
                  <span className="p-2 rounded-xl bg-white/20 backdrop-blur-xs text-white">
                    <Play className="w-4 h-4 fill-white" />
                  </span>
                  <span className="px-2 py-0.5 rounded-full bg-white/25 text-[10px] font-mono font-bold text-white">
                    25 Soru
                  </span>
                </div>
                <h3 className="font-black text-sm sm:text-base text-white">
                  25 Taze Soru Başlat
                </h3>
                <p className="text-xs text-teal-50/90 mt-1">
                  Seçili dersten henüz çözmediğiniz sorularla hemen pratik yapın.
                </p>
              </div>
              <div className="mt-3 pt-2 border-t border-white/20 flex items-center justify-between text-[11px] font-mono text-teal-100">
                <span>{unseenCount} taze soru havuzda</span>
                <span className="font-bold underline">Hemen Çöz →</span>
              </div>
            </button>

            {/* Quick 2: Yanlışlarımı Temizle */}
            <button
              onClick={() => handleQuickStart('mistakes')}
              disabled={mistakeCountInScope === 0}
              className={`p-4 rounded-2xl border text-left transition-all flex flex-col justify-between ${
                mistakeCountInScope > 0
                  ? 'bg-white dark:bg-fintech-surface border-rose-300 dark:border-rose-500/40 hover:border-rose-400 active:scale-[0.98] cursor-pointer shadow-xs'
                  : 'bg-slate-50 dark:bg-fintech-card/50 border-slate-200 dark:border-fintech-border opacity-60 cursor-not-allowed'
              }`}
            >
              <div>
                <div className="flex items-center justify-between mb-2">
                  <span className={`p-2 rounded-xl ${mistakeCountInScope > 0 ? 'bg-rose-100 dark:bg-rose-500/20 text-rose-600 dark:text-rose-400' : 'bg-slate-200 dark:bg-slate-800 text-slate-400'}`}>
                    <RotateCcw className="w-4 h-4" />
                  </span>
                  <span className={`px-2 py-0.5 rounded-full text-[10px] font-mono font-bold ${
                    mistakeCountInScope > 0 ? 'bg-rose-100 dark:bg-rose-500/20 text-rose-700 dark:text-rose-300' : 'bg-slate-200 dark:bg-slate-800 text-slate-500'
                  }`}>
                    {mistakeCountInScope} Hata
                  </span>
                </div>
                <h3 className="font-black text-sm sm:text-base text-slate-900 dark:text-white">
                  Yanlışlarımı Temizle
                </h3>
                <p className="text-xs text-slate-500 dark:text-slate-400 mt-1">
                  {mistakeCountInScope > 0
                    ? 'Daha önce yanlış yaptığınız soruları çözerek eksiklerinizi kapatın.'
                    : 'Tebrikler! Seçili derste çözülmemiş yanlış soru bulunmuyor.'}
                </p>
              </div>
              <div className="mt-3 pt-2 border-t border-slate-100 dark:border-fintech-border flex items-center justify-between text-[11px] font-mono">
                <span className="text-slate-500">{mistakeCountInScope > 0 ? 'Hatalı Sorular' : 'Temiz'}</span>
                <span className="font-bold text-rose-600 dark:text-rose-400">{mistakeCountInScope > 0 ? 'Düzelt →' : 'Tamam'}</span>
              </div>
            </button>

            {/* Quick 3: Tüm Havuzdan Karma Test */}
            <button
              onClick={() => handleQuickStart('all_pool')}
              className="p-4 rounded-2xl bg-white dark:bg-fintech-surface border border-slate-200 dark:border-fintech-border hover:border-teal-500/50 text-left transition-all active:scale-[0.98] cursor-pointer shadow-xs flex flex-col justify-between"
            >
              <div>
                <div className="flex items-center justify-between mb-2">
                  <span className="p-2 rounded-xl bg-teal-100 dark:bg-teal-500/20 text-teal-600 dark:text-teal-400">
                    <Sparkles className="w-4 h-4" />
                  </span>
                  <span className="px-2 py-0.5 rounded-full bg-teal-100 dark:bg-teal-500/20 text-[10px] font-mono font-bold text-teal-700 dark:text-teal-300">
                    25 Soru
                  </span>
                </div>
                <h3 className="font-black text-sm sm:text-base text-slate-900 dark:text-white">
                  Tüm Havuzdan Karma Test
                </h3>
                <p className="text-xs text-slate-500 dark:text-slate-400 mt-1">
                  Seçili dersten veya tüm derslerden rastgele karma 25 soru ile anında açıklamalı test.
                </p>
              </div>
              <div className="mt-3 pt-2 border-t border-slate-100 dark:border-fintech-border flex items-center justify-between text-[11px] font-mono text-teal-600 dark:text-teal-400">
                <span>Karma Test</span>
                <span className="font-bold">Başla →</span>
              </div>
            </button>
          </div>
        </div>

        {/* 3. Gelişmiş Filtreler & Özel Ayarlar (Açılır-Kapanır Accordion) */}
        <div className="bg-white dark:bg-fintech-surface rounded-2xl sm:rounded-3xl border border-slate-200 dark:border-fintech-border overflow-hidden shadow-xs">
          <button
            type="button"
            onClick={() => setShowAdvancedFilters(!showAdvancedFilters)}
            className="w-full p-4 flex items-center justify-between text-left hover:bg-slate-50 dark:hover:bg-fintech-card transition-colors cursor-pointer"
          >
            <div className="flex items-center gap-2">
              <SlidersHorizontal className="w-4 h-4 text-teal-600 dark:text-teal-400" />
              <span className="font-bold text-xs sm:text-sm text-slate-800 dark:text-slate-200">
                Gelişmiş Filtreler ve Soru Sayısı Ayarla
              </span>
            </div>
            <div className="flex items-center gap-2">
              <span className="text-[11px] font-mono text-slate-400 hidden sm:inline">
                {filterMode} • {cognitiveFilter} • {questionCount} Soru
              </span>
              {showAdvancedFilters ? (
                <ChevronUp className="w-4 h-4 text-slate-400" />
              ) : (
                <ChevronDown className="w-4 h-4 text-slate-400" />
              )}
            </div>
          </button>

          {showAdvancedFilters && (
            <div className="p-4 pt-2 border-t border-slate-100 dark:border-fintech-border/60 space-y-4 animate-fade-in">
              {/* Soru Filtresi */}
              <div className="space-y-2">
                <label className="text-xs font-mono uppercase tracking-wider text-slate-700 dark:text-slate-300 font-bold block">
                  Soru Filtresi
                </label>
                <div className="grid grid-cols-2 sm:grid-cols-4 gap-2">
                  {[
                    { id: 'unseen', label: '🟢 Çözülmemiş', sub: `${unseenCount} Taze Soru` },
                    { id: 'all', label: '⚪ Tüm Havuz', sub: `${totalModulePool} Soru` },
                    { id: 'mistakes', label: '🔴 Yanlışlarım', sub: `${mistakeCountInScope} Soru` },
                    { id: 'bookmarks', label: '⭐ Yıldızlılar', sub: `${bookmarkCountInScope} Soru` },
                  ].map((filter) => (
                    <button
                      key={filter.id}
                      onClick={() => setFilterMode(filter.id as any)}
                      className={`p-2.5 rounded-xl border text-left transition-all ${
                        filterMode === filter.id
                          ? 'bg-teal-50 dark:bg-teal-500/15 border-teal-500 text-teal-950 dark:text-teal-200 ring-1 ring-teal-400/40'
                          : 'bg-slate-50 dark:bg-fintech-card border-slate-200 dark:border-fintech-border text-slate-600 dark:text-slate-400'
                      }`}
                    >
                      <span className="font-bold text-xs block text-slate-900 dark:text-white truncate">
                        {filter.label}
                      </span>
                      <span className="text-[10px] font-mono text-slate-500 dark:text-slate-400 block mt-0.5">
                        {filter.sub}
                      </span>
                    </button>
                  ))}
                </div>
              </div>

              {/* Bilişsel Düzey (Maarif) */}
              <div className="space-y-2">
                <label className="text-xs font-mono uppercase tracking-wider text-slate-700 dark:text-slate-300 font-bold flex items-center gap-1.5">
                  <Brain className="w-3.5 h-3.5 text-teal-600 dark:text-teal-400" />
                  <span>Maarif Bilişsel Düzey</span>
                </label>
                <div className="grid grid-cols-2 sm:grid-cols-4 gap-2">
                  {[
                    { id: 'all', label: '🌟 Tümü Karma', count: kbCounts.all },
                    { id: 'KB3_Vaka', label: '🧠 Vaka & Hesap', count: kbCounts.KB3_Vaka },
                    { id: 'KB2_Muhakeme', label: '⚖️ Öncüllü (I-II-III)', count: kbCounts.KB2_Muhakeme },
                    { id: 'KB1_Kavramsal', label: '📚 Mevzuat & Tanım', count: kbCounts.KB1_Kavramsal },
                  ].map((kb) => (
                    <button
                      key={kb.id}
                      type="button"
                      onClick={() => setCognitiveFilter(kb.id as any)}
                      className={`p-2 rounded-xl border text-left transition-all cursor-pointer flex items-center justify-between gap-1 ${
                        cognitiveFilter === kb.id
                          ? 'bg-teal-50 dark:bg-teal-500/15 border-teal-500 text-teal-950 dark:text-teal-200 ring-1 ring-teal-400/40'
                          : 'bg-slate-50 dark:bg-fintech-card border-slate-200 dark:border-fintech-border text-slate-600 dark:text-slate-400'
                      }`}
                    >
                      <span className="font-bold text-xs text-slate-900 dark:text-white truncate">{kb.label}</span>
                      <span className="text-[10px] font-mono font-bold px-1.5 py-0.5 rounded bg-slate-200 dark:bg-slate-800 text-slate-700 dark:text-slate-300 shrink-0">
                        {kb.count}
                      </span>
                    </button>
                  ))}
                </div>
              </div>

              {/* Soru Sayısı */}
              <div className="space-y-1.5 pt-2 border-t border-slate-100 dark:border-fintech-border/60">
                <label className="text-xs font-mono uppercase tracking-wider text-slate-700 dark:text-slate-300 font-bold block">
                  Soru Sayısı
                </label>
                <div className="grid grid-cols-4 gap-2">
                  {[10, 25, 50, 100].map((count) => (
                    <button
                      key={count}
                      type="button"
                      onClick={() => setQuestionCount(count)}
                      className={`py-2 rounded-xl border font-mono font-bold text-xs transition-all ${
                        questionCount === count
                          ? 'bg-teal-600 text-white border-teal-700 shadow-xs'
                          : 'bg-slate-50 dark:bg-fintech-card text-slate-700 dark:text-slate-300 border-slate-200 dark:border-fintech-border'
                      }`}
                    >
                      {count}
                    </button>
                  ))}
                </div>
              </div>

              {/* Start with Custom Filters Button */}
              <button
                onClick={handleStart}
                className="w-full flex items-center justify-center gap-2 py-3 rounded-xl bg-teal-600 hover:bg-teal-700 active:bg-teal-800 text-white font-black text-xs sm:text-sm shadow-md shadow-teal-700/20 active:scale-95 transition-all cursor-pointer"
              >
                <Play className="w-4 h-4 fill-white text-white" />
                <span className="text-white font-black">
                  Özel Ayarlarla Başlat ({questionCount} Soru)
                </span>
              </button>
            </div>
          )}
        </div>
      </div>
    );
  }

  // Active Quiz View
  const currentIndex = currentSession.current_index;
  const total = currentSession.questions.length;
  const currentQ = currentSession.questions[currentIndex];
  const currentAns = currentSession.user_answers[currentQ.id];
  const isLastQuestion = currentIndex === total - 1;

  const answeredCount = Object.values(currentSession.user_answers).filter(
    (a) => a.selected_option !== null
  ).length;

  return (
    <div className="max-w-6xl mx-auto space-y-4 sm:space-y-6 animate-fade-in pb-16 sm:pb-12">
      {/* Top Header Bar */}
      <div className="bg-white dark:bg-fintech-surface rounded-2xl border border-slate-200 dark:border-fintech-border p-3 sm:p-4 flex items-center justify-between gap-2.5 sm:gap-4 shadow-xs">
        <div className="flex items-center gap-2 sm:gap-3 min-w-0">
          <button
            onClick={() => setShowExitConfirm(true)}
            className="p-2 rounded-xl bg-slate-50 dark:bg-fintech-card hover:bg-rose-50 text-slate-500 hover:text-rose-600 border border-slate-200 dark:border-fintech-border transition-all shadow-xs shrink-0 active:scale-95"
            title="Testten Çık"
          >
            <ArrowLeft className="w-4 h-4 sm:w-5 sm:h-5" />
          </button>
          <div className="min-w-0">
            <div className="flex items-center gap-1.5 sm:gap-2">
              <span className="font-black text-slate-900 dark:text-white text-xs sm:text-base tracking-tight truncate">
                Soru {currentIndex + 1} / {total}
              </span>
              <span className="text-[10px] font-mono font-bold px-1.5 py-0.5 rounded-full bg-teal-50 dark:bg-teal-500/15 text-teal-700 dark:text-teal-300 border border-teal-200 dark:border-teal-500/30 shrink-0">
                %{Math.round((answeredCount / total) * 100)}
              </span>
            </div>
            <p className="text-[11px] text-slate-500 dark:text-slate-400 truncate hidden sm:block">
              {currentSession.title}
            </p>
          </div>
        </div>

        <div className="flex items-center gap-1.5 sm:gap-2.5 shrink-0">
          {/* Mobile Optical Form Button */}
          <button
            onClick={() => setShowMobileOptical(true)}
            className="lg:hidden flex items-center gap-1 px-2.5 py-1.5 rounded-xl bg-teal-50 dark:bg-teal-500/15 text-teal-800 dark:text-teal-300 border border-teal-300 dark:border-teal-500/40 text-xs font-bold transition-all active:scale-95 cursor-pointer"
            title="Soru Listesi ve Optik Form"
          >
            <ListOrdered className="w-3.5 h-3.5 text-teal-600 dark:text-teal-400" />
            <span>Optik ({answeredCount}/{total})</span>
          </button>

          <ExamTimer onTick={updateTimer} />

          <button
            onClick={handleFinish}
            className="px-3 sm:px-4 py-1.5 sm:py-2 rounded-xl bg-emerald-50 dark:bg-emerald-500/20 hover:bg-emerald-100 dark:hover:bg-emerald-500/30 text-emerald-800 dark:text-emerald-300 border border-emerald-300 dark:border-emerald-500/40 text-xs font-bold transition-all shadow-xs cursor-pointer active:scale-95"
          >
            Bitir
          </button>
        </div>
      </div>

      {/* Progress Bar */}
      <div className="w-full h-1.5 bg-slate-200 dark:bg-fintech-card rounded-full overflow-hidden">
        <div
          className="h-full bg-gradient-to-r from-teal-500 to-emerald-400 transition-all duration-300"
          style={{ width: `${((currentIndex + 1) / total) * 100}%` }}
        />
      </div>

      {/* Main Layout: Question on left, Optical Form on right (desktop) */}
      <div className="grid grid-cols-1 lg:grid-cols-12 gap-6">
        {/* Left / Center: Question & Explanation */}
        <div className="lg:col-span-8 space-y-5 sm:space-y-6">
          <QuestionCard
            question={currentQ}
            userAnswer={currentAns}
            mode={currentSession.mode}
            isLocked={currentSession.mode === 'practice' ? isAnswerLocked : false}
            questionIndex={currentIndex}
            totalQuestions={total}
            onSelectOption={handleSelectOptionWithSound}
          />

          {/* Explanation Panel (Only shown in practice mode when answered) */}
          {currentSession.mode === 'practice' && isAnswerLocked && currentAns && currentAns.selected_option !== null && (
            <ExplanationPanel
              question={currentQ}
              isCorrect={currentAns.is_correct}
              selectedOption={currentAns.selected_option}
              onScrolledToBottom={() => setExplanationRead(true)}
              onNextQuestion={handleNextOrFinish}
              isLastQuestion={isLastQuestion}
            />
          )}

          {/* Bottom Navigation Buttons (Ergonomic for iPhone 16 Pro Max thumb zones) */}
          <div className="sticky bottom-0 z-20 -mx-4 px-4 py-3 bg-white/95 dark:bg-fintech-surface/95 backdrop-blur-md border-t border-slate-200/80 dark:border-fintech-border/80 sm:static sm:bg-transparent sm:backdrop-blur-none sm:border-0 sm:p-0 sm:mx-0 flex items-center justify-between gap-2.5 pb-[calc(0.75rem+env(safe-area-inset-bottom))] sm:pb-0 shadow-lg sm:shadow-none">
            <button
              onClick={prevQuestion}
              disabled={currentIndex === 0}
              className={`flex-1 sm:flex-initial flex items-center justify-center gap-2 px-4 py-3.5 sm:py-3 rounded-2xl border text-xs sm:text-sm font-bold transition-all active:scale-95 ${
                currentIndex === 0
                  ? 'opacity-40 cursor-not-allowed bg-slate-100 dark:bg-fintech-surface border-slate-200 dark:border-fintech-border text-slate-400'
                  : 'bg-white dark:bg-fintech-surface hover:bg-slate-50 dark:hover:bg-fintech-card border-slate-200 dark:border-fintech-border text-slate-700 dark:text-slate-200 shadow-xs'
              }`}
            >
              <ArrowLeft className="w-4 h-4 shrink-0" />
              <span>Önceki</span>
            </button>

            {/* Mobile quick optical button in bottom bar */}
            <button
              onClick={() => setShowMobileOptical(true)}
              className="lg:hidden px-3.5 py-3.5 rounded-2xl bg-slate-100 dark:bg-fintech-card border border-slate-200 dark:border-fintech-border text-slate-700 dark:text-slate-300 text-xs font-bold flex items-center justify-center gap-1.5 active:scale-95 transition-all"
              title="Optik Form"
            >
              <ListOrdered className="w-4 h-4 text-teal-600 dark:text-teal-400" />
              <span>{answeredCount}/{total}</span>
            </button>

            {isLastQuestion ? (
              <button
                onClick={handleFinish}
                className="flex-1 sm:flex-initial flex items-center justify-center gap-2 px-5 sm:px-6 py-3.5 sm:py-3 rounded-2xl bg-emerald-600 hover:bg-emerald-700 active:bg-emerald-800 text-white font-black text-xs sm:text-sm shadow-md shadow-emerald-700/25 active:scale-95 transition-all cursor-pointer"
              >
                <CheckCircle2 className="w-4 h-4 text-white shrink-0" />
                <span className="text-white font-black">Testi Tamamla</span>
              </button>
            ) : (
              <button
                onClick={handleNextOrFinish}
                className={`flex-1 sm:flex-initial flex items-center justify-center gap-2 px-5 sm:px-6 py-3.5 sm:py-3 rounded-2xl font-black text-xs sm:text-sm transition-all cursor-pointer active:scale-95 ${
                  (currentSession.mode === 'practice' ? isAnswerLocked : currentAns?.selected_option !== null)
                    ? 'bg-teal-600 hover:bg-teal-700 active:bg-teal-800 text-white shadow-md shadow-teal-700/25'
                    : 'bg-slate-100 hover:bg-slate-200 dark:bg-fintech-card text-slate-700 dark:text-slate-300 border border-slate-200 dark:border-fintech-border'
                }`}
              >
                <span className={(currentSession.mode === 'practice' ? isAnswerLocked : currentAns?.selected_option !== null) ? 'text-white font-black' : ''}>
                  Sonraki Soru
                </span>
                <ArrowRight className={`w-4 h-4 ${(currentSession.mode === 'practice' ? isAnswerLocked : currentAns?.selected_option !== null) ? 'text-white' : ''} shrink-0`} />
              </button>
            )}
          </div>
        </div>

        {/* Right Column: Optical Form & Keyboard Hints (Desktop Only) */}
        <div className="hidden lg:block lg:col-span-4 space-y-6">
          <OpticalForm
            questions={currentSession.questions}
            userAnswers={currentSession.user_answers}
            currentIndex={currentIndex}
            mode={currentSession.mode}
            onSelectQuestion={goToQuestion}
          />

          {/* Shortcut Keys Box (Desktop Only) */}
          <div className="bg-white dark:bg-fintech-surface rounded-2xl border border-slate-200 dark:border-fintech-border p-4 space-y-2 text-xs text-slate-600 dark:text-slate-400 shadow-xs">
            <h5 className="font-bold text-slate-800 dark:text-slate-300 uppercase tracking-wider text-[10px] font-mono">
              Klavye Kısayolları
            </h5>
            <div className="grid grid-cols-2 gap-2 text-[11px]">
              <div><kbd className="px-1.5 py-0.5 rounded bg-slate-100 dark:bg-slate-800 border border-slate-200 dark:border-slate-700 font-mono text-teal-700 dark:text-teal-400 font-bold">A - E</kbd> / <kbd className="px-1.5 py-0.5 rounded bg-slate-100 dark:bg-slate-800 border border-slate-200 dark:border-slate-700 font-mono text-teal-700 dark:text-teal-400 font-bold">1 - 5</kbd>: Şık Seç</div>
              <div><kbd className="px-1.5 py-0.5 rounded bg-slate-100 dark:bg-slate-800 border border-slate-200 dark:border-slate-700 font-mono text-teal-700 dark:text-teal-400 font-bold">Enter / → / Space</kbd>: Sonraki Soru</div>
            </div>
          </div>
        </div>
      </div>

      {/* Mobile Optical Form Bottom Sheet Modal */}
      {showMobileOptical && (
        <div className="fixed inset-0 z-50 bg-slate-950/60 backdrop-blur-sm flex flex-col justify-end p-0 sm:p-4">
          <div className="bg-white dark:bg-fintech-surface rounded-t-3xl sm:rounded-3xl border-t sm:border border-slate-200 dark:border-fintech-border max-w-lg w-full mx-auto p-5 space-y-4 shadow-2xl animate-slide-up max-h-[85vh] flex flex-col">
            <div className="flex items-center justify-between pb-3 border-b border-slate-100 dark:border-fintech-border/60">
              <div>
                <h3 className="font-black text-base text-slate-900 dark:text-white">Optik Form & Soru Listesi</h3>
                <p className="text-xs text-slate-500 dark:text-slate-400">{answeredCount} / {total} Tamamlandı</p>
              </div>
              <button
                onClick={() => setShowMobileOptical(false)}
                className="p-2 rounded-full bg-slate-100 dark:bg-fintech-card text-slate-500 hover:text-slate-800 dark:text-slate-300 transition-colors"
              >
                <X className="w-5 h-5" />
              </button>
            </div>
            <div className="overflow-y-auto flex-1 pr-1">
              <OpticalForm
                questions={currentSession.questions}
                userAnswers={currentSession.user_answers}
                currentIndex={currentIndex}
                mode={currentSession.mode}
                onSelectQuestion={(idx) => {
                  goToQuestion(idx);
                  setShowMobileOptical(false);
                }}
              />
            </div>
            <button
              onClick={() => setShowMobileOptical(false)}
              className="w-full py-3 rounded-2xl bg-teal-600 text-white font-bold text-sm shadow-md shadow-teal-700/20 active:scale-95 transition-all"
            >
              Soruyu Çözmeye Dön
            </button>
          </div>
        </div>
      )}

      {/* Exit Confirmation Modal */}
      {showExitConfirm && (
        <div className="fixed inset-0 z-50 bg-slate-950/60 backdrop-blur-sm flex items-center justify-center p-4">
          <div className="bg-white dark:bg-fintech-surface rounded-3xl border border-slate-200 dark:border-fintech-border max-w-md w-full p-6 space-y-5 shadow-2xl animate-slide-up">
            <div className="flex items-center gap-3 text-amber-600 dark:text-amber-400">
              <AlertCircle className="w-6 h-6" />
              <h3 className="font-black text-lg text-slate-900 dark:text-white">Testten Çıkılsın mı?</h3>
            </div>
            <p className="text-sm text-slate-600 dark:text-slate-300">
              Testi sonlandırırsanız şu ana kadarki ilerlemeniz kaydedilip sonuç raporunuz oluşturulacaktır.
            </p>
            <div className="flex items-center justify-end gap-3 pt-2">
              <button
                onClick={() => setShowExitConfirm(false)}
                className="px-4 py-2 rounded-xl bg-slate-100 hover:bg-slate-200 dark:bg-fintech-card dark:hover:bg-fintech-cardHover text-slate-700 dark:text-slate-300 text-xs font-semibold border border-slate-200 dark:border-fintech-border transition-colors"
              >
                Teste Devam Et
              </button>
              <button
                onClick={() => {
                  setShowExitConfirm(false);
                  resetSession();
                  onNavigate('home');
                }}
                className="px-4 py-2 rounded-xl bg-slate-200 hover:bg-slate-300 dark:bg-slate-800 dark:hover:bg-slate-700 text-slate-700 dark:text-slate-300 text-xs font-semibold border border-slate-300 dark:border-slate-700 transition-colors"
              >
                Kaydetmeden Çık
              </button>
              <button
                onClick={() => {
                  setShowExitConfirm(false);
                  handleFinish();
                }}
                className="px-4 py-2 rounded-xl bg-teal-600 hover:bg-teal-700 active:bg-teal-800 text-white text-xs font-bold shadow-md shadow-teal-700/25 transition-all cursor-pointer"
              >
                Sonuçları Gör ve Bitir
              </button>
            </div>
          </div>
        </div>
      )}
    </div>
  );
};
