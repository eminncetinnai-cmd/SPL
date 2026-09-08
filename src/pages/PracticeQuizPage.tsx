import React, { useState, useEffect, useRef } from 'react';
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
  Pause
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

interface PracticeQuizPageProps {
  initialModuleId?: ModuleId;
  initialSourceFilter?: 'all' | 'master' | 'cikmis' | 'ogretici' | 'genel';
  onNavigate: (page: string, params?: any) => void;
}

export const PracticeQuizPage: React.FC<PracticeQuizPageProps> = ({
  initialModuleId,
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
  const { seenQuestionIds, avoidQuestionRepetition, setAvoidRepetition, resetSeenQuestions } = useProgressStore();

  // Setup state for configuration: Default to 'genel' (540 questions) or passed initialSourceFilter
  const [selectedModule, setSelectedModule] = useState<ModuleId | 'all'>(initialModuleId || '1001');
  const [questionCount, setQuestionCount] = useState<number>(25);
  const [sourceFilter, setSourceFilter] = useState<'all' | 'master' | 'cikmis' | 'ogretici' | 'genel'>(
    initialSourceFilter === 'cikmis' ? 'cikmis' : 'genel'
  );
  const [showExitConfirm, setShowExitConfirm] = useState(false);

  const allQs = allQuestionsData as Question[];
  const candidatePool = allQs.filter((q) => {
    if (selectedModule !== 'all' && q.module_id !== selectedModule) return false;
    if (sourceFilter === 'cikmis' && q.source !== 'cikmis') return false;
    if (sourceFilter === 'genel' && q.source === 'cikmis') return false;
    return true;
  });

  const totalModulePool = candidatePool.length;
  const seenCount = candidatePool.filter((q) => seenQuestionIds.includes(q.id)).length;
  const unseenCount = Math.max(0, totalModulePool - seenCount);
  const [autoAdvance, setAutoAdvance] = useState(false);
  const [autoAdvanceTimer, setAutoAdvanceTimer] = useState<number | null>(null);

  const autoAdvanceTimeoutRef = useRef<any>(null);

  useEffect(() => {
    if (initialModuleId) {
      setSelectedModule(initialModuleId);
    }
  }, [initialModuleId]);

  useEffect(() => {
    if (initialSourceFilter) {
      setSourceFilter(initialSourceFilter);
    }
  }, [initialSourceFilter]);

  // Clean up auto advance timer on unmount or question change
  useEffect(() => {
    return () => {
      if (autoAdvanceTimeoutRef.current) {
        clearTimeout(autoAdvanceTimeoutRef.current);
      }
    };
  }, [currentSession?.current_index]);

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

    // Auto Advance logic
    if (autoAdvance && currentSession && currentSession.current_index < currentSession.questions.length - 1) {
      setAutoAdvanceTimer(1.5);
      if (autoAdvanceTimeoutRef.current) clearTimeout(autoAdvanceTimeoutRef.current);

      autoAdvanceTimeoutRef.current = setTimeout(() => {
        setAutoAdvanceTimer(null);
        nextQuestion();
      }, 1500);
    }
  };

  const handleCancelAutoAdvance = () => {
    if (autoAdvanceTimeoutRef.current) {
      clearTimeout(autoAdvanceTimeoutRef.current);
      setAutoAdvanceTimer(null);
    }
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
    handleCancelAutoAdvance();
    if (!currentSession) return;
    if (currentSession.current_index === currentSession.questions.length - 1) {
      handleFinish();
    } else {
      nextQuestion();
    }
  };

  const handleStart = () => {
    startQuiz({
      mode: 'practice',
      moduleId: selectedModule,
      questionCount,
      sourceFilter,
    });
  };

  const handleFinish = () => {
    handleCancelAutoAdvance();
    const completed = finishQuiz();
    if (completed) {
      onNavigate('results');
    }
  };

  // If no active session, show setup configuration
  if (!currentSession || currentSession.is_completed) {
    return (
      <div className="max-w-4xl mx-auto space-y-8 animate-fade-in py-4">
        {/* Header */}
        <div className="flex items-center gap-4">
          <button
            onClick={() => onNavigate('home')}
            className="p-2.5 rounded-xl bg-white dark:bg-fintech-surface hover:bg-slate-100 dark:hover:bg-fintech-card border border-slate-200 dark:border-fintech-border text-slate-700 dark:text-slate-300 hover:text-slate-900 dark:hover:text-white shadow-sm transition-all"
          >
            <ArrowLeft className="w-5 h-5" />
          </button>
          <div>
            <h1 className="text-2xl font-black text-slate-900 dark:text-white tracking-tight">
              Modül Pratik Testi Hazırla
            </h1>
            <p className="text-xs sm:text-sm text-slate-600 dark:text-slate-400">
              Anında açıklamalı, soru kilit mekanizmalı ve analitik çözümlü çalışma testi.
            </p>
          </div>
        </div>

        {/* Configuration Card */}
        <div className="bg-white dark:bg-fintech-surface rounded-3xl border border-slate-200 dark:border-fintech-border p-6 sm:p-8 space-y-8 shadow-sm dark:shadow-2xl">
          {/* Step 1: Select Module */}
          <div className="space-y-3">
            <label className="text-xs font-mono uppercase tracking-wider text-slate-700 dark:text-slate-300 font-bold block">
              1. ÇALIŞILACAK DERS / MODÜLÜ SEÇİN
            </label>
            <div className="grid grid-cols-1 sm:grid-cols-2 gap-3">
              <button
                onClick={() => setSelectedModule('all')}
                className={`p-4 rounded-2xl border text-left transition-all flex items-center justify-between ${
                  selectedModule === 'all'
                    ? 'bg-teal-50 dark:bg-teal-500/15 border-teal-500 text-teal-900 dark:text-teal-300 shadow-sm ring-1 ring-teal-500/30'
                    : 'bg-slate-50 dark:bg-fintech-card border-slate-200 dark:border-fintech-border text-slate-700 dark:text-slate-300 hover:border-slate-300 dark:hover:border-slate-600'
                }`}
              >
                <div>
                  <span className="font-bold text-sm block text-slate-900 dark:text-white">Tüm Modüller Karışık</span>
                  <span className="text-xs text-slate-500 dark:text-slate-400">1001, 1003, 1005, 1012 ortak havuz ({allQs.length} Benzersiz Soru)</span>
                </div>
                <Sparkles className="w-5 h-5 text-teal-600 dark:text-teal-400" />
              </button>

              {modulesData.map((m) => (
                <button
                  key={m.id}
                  onClick={() => setSelectedModule(m.id as ModuleId)}
                  className={`p-4 rounded-2xl border text-left transition-all flex items-center justify-between ${
                    selectedModule === m.id
                      ? 'bg-teal-50 dark:bg-teal-500/15 border-teal-500 text-teal-900 dark:text-teal-300 shadow-sm ring-1 ring-teal-500/30'
                      : 'bg-slate-50 dark:bg-fintech-card border-slate-200 dark:border-fintech-border text-slate-700 dark:text-slate-300 hover:border-slate-300 dark:hover:border-slate-600'
                  }`}
                >
                  <div>
                    <span className="font-mono text-xs font-bold text-teal-600 dark:text-teal-400 block">Modül {m.code}</span>
                    <span className="font-bold text-sm text-slate-900 dark:text-white block truncate">{m.short_name}</span>
                  </div>
                  <span className="text-xs font-mono text-slate-500 dark:text-slate-400">{allQs.filter((q) => q.module_id === m.id).length} Soru</span>
                </button>
              ))}
            </div>
          </div>

          {/* Step 2: Question Count */}
          <div className="space-y-3">
            <label className="text-xs font-mono uppercase tracking-wider text-slate-700 dark:text-slate-300 font-bold block">
              2. TESTTEKİ SORU SAYISI
            </label>
            <div className="grid grid-cols-4 gap-3">
              {[10, 25, 50, 100].map((count) => (
                <button
                  key={count}
                  onClick={() => setQuestionCount(count)}
                  className={`py-3 rounded-xl border font-mono font-bold text-sm transition-all ${
                    questionCount === count
                      ? 'bg-teal-500 text-slate-950 border-teal-400 shadow-sm shadow-teal-500/20'
                      : 'bg-slate-50 dark:bg-fintech-card text-slate-700 dark:text-slate-300 border-slate-200 dark:border-fintech-border hover:border-slate-300 dark:hover:border-slate-600'
                  }`}
                >
                  {count} Soru
                </button>
              ))}
            </div>
          </div>

          {/* Step 3: Question Source Filter */}
          <div className="space-y-3">
            <div className="flex items-center justify-between">
              <label className="text-xs font-mono uppercase tracking-wider text-slate-700 dark:text-slate-300 font-bold block">
                3. SORU KAYNAĞI FİLTRESİ
              </label>
              <span className="text-[11px] font-mono text-teal-600 dark:text-teal-400 font-bold">
                Aktif Havuz: {totalModulePool} Soru
              </span>
            </div>

            <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
              {[
                { 
                  id: 'cikmis', 
                  label: '🎯 Çıkmış Sınav Soruları', 
                  badge: '110 Soru',
                  tag: 'RESMİ SINAV ARŞİVİ',
                  desc: 'SPK lisanslama sınavlarında bizzat sorulmuş gerçek ve özgün çıkmış sınav soruları.' 
                },
                { 
                  id: 'genel', 
                  label: '📚 Genel Soru Havuzu (Çıkmış Hariç)', 
                  badge: '540 Soru',
                  tag: 'ÖNCÜLLÜ & MEVZUAT EŞİKLERİ',
                  desc: 'Çıkmış soruları içermeyen; öncüllü (I-II-III) soruları, tüm kanun maddelerini ve sayısal eşikleri kapsayan ana hazırlık bankası.' 
                },
              ].map((src) => (
                <button
                  key={src.id}
                  onClick={() => setSourceFilter(src.id as any)}
                  className={`p-5 rounded-2xl border text-left transition-all relative overflow-hidden ${
                    sourceFilter === src.id
                      ? src.id === 'cikmis'
                        ? 'bg-amber-50 dark:bg-amber-500/15 border-amber-400 text-amber-950 dark:text-amber-200 ring-2 ring-amber-400/40 shadow-sm'
                        : 'bg-teal-50 dark:bg-teal-500/15 border-teal-400 text-teal-950 dark:text-teal-200 ring-2 ring-teal-400/40 shadow-sm'
                      : 'bg-slate-50 dark:bg-fintech-card border-slate-200 dark:border-fintech-border text-slate-600 dark:text-slate-400 hover:text-slate-900 dark:hover:text-slate-200 hover:border-slate-300 dark:hover:border-slate-600'
                  }`}
                >
                  <div className="flex items-center justify-between gap-2 mb-2">
                    <span className="font-bold text-sm block text-slate-900 dark:text-white">{src.label}</span>
                    <span className={`text-[11px] font-mono px-2.5 py-0.5 rounded-full font-bold ${
                      src.id === 'cikmis'
                        ? 'bg-amber-100 dark:bg-amber-500/20 text-amber-800 dark:text-amber-300 border border-amber-300 dark:border-amber-500/40'
                        : 'bg-teal-100 dark:bg-teal-500/20 text-teal-800 dark:text-teal-300 border border-teal-300 dark:border-teal-500/40'
                    }`}>
                      {src.badge}
                    </span>
                  </div>
                  <span className="text-xs text-slate-600 dark:text-slate-300 block leading-relaxed">{src.desc}</span>
                  <div className="mt-3 inline-flex items-center gap-1 text-[10px] font-mono font-bold uppercase tracking-wider text-slate-500 dark:text-slate-400">
                    <span className={`w-1.5 h-1.5 rounded-full ${src.id === 'cikmis' ? 'bg-amber-500' : 'bg-teal-500'}`} />
                    <span>{src.tag}</span>
                  </div>
                </button>
              ))}
            </div>

            {sourceFilter === 'cikmis' ? (
              <div className="flex items-center gap-3 p-4 rounded-2xl bg-amber-50 dark:bg-amber-500/10 border border-amber-200 dark:border-amber-500/30 text-amber-900 dark:text-amber-300 text-xs">
                <span className="text-xl shrink-0">🎯</span>
                <div>
                  <span className="font-bold">Özel Çıkmış Sınav Grubu Seçildi:</span>
                  <span className="text-amber-800 dark:text-amber-200/90 ml-1">
                    Bu modda testinize yalnızca SPK lisanslama sınavlarında bizzat sorulan kanun maddeleri, tebliğler ve çıkmış sınav soruları (110 Soru) dahil edilir.
                  </span>
                </div>
              </div>
            ) : (
              <div className="flex items-center gap-3 p-4 rounded-2xl bg-teal-50 dark:bg-teal-500/10 border border-teal-200 dark:border-teal-500/30 text-teal-900 dark:text-teal-300 text-xs">
                <span className="text-xl shrink-0">📚</span>
                <div>
                  <span className="font-bold">Genel Soru Havuzu (Çıkmış Hariç) Seçildi:</span>
                  <span className="text-teal-800 dark:text-teal-200/90 ml-1">
                    Bu modda testinize çıkmış sorular dahil edilmez; öncüllü (I-II-III) sorular, 15 kritik sayısal/oransal eşik ve müfredatın tüm detaylarını içeren 540 soruluk kapsamlı soru havuzu sunulur.
                  </span>
                </div>
              </div>
            )}
          </div>

          {/* Anti-Repeat Smart Pool Status Banner */}
          <div className="bg-teal-50/70 dark:bg-slate-900/90 rounded-2xl border border-teal-200 dark:border-teal-500/30 p-5 space-y-3">
            <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-3">
              <div className="flex items-center gap-2.5">
                <div className="w-9 h-9 rounded-xl bg-teal-500/15 border border-teal-500/30 flex items-center justify-center shrink-0">
                  <ShieldCheck className="w-5 h-5 text-teal-600 dark:text-teal-400" />
                </div>
                <div>
                  <span className="font-bold text-xs sm:text-sm text-slate-900 dark:text-white block">
                    🛡️ Akıllı Soru Rotasyonu & Tekrarsız Havuz
                  </span>
                  <span className="text-xs text-slate-600 dark:text-slate-300 block">
                    {unseenCount} / {totalModulePool} çözülmemiş yeni soru mevcut
                  </span>
                </div>
              </div>

              <div className="flex items-center gap-2 flex-wrap">
                <button
                  type="button"
                  onClick={() => setAvoidRepetition(!avoidQuestionRepetition)}
                  className={`px-3 py-1.5 rounded-xl text-xs font-mono font-bold transition-all border ${
                    avoidQuestionRepetition
                      ? 'bg-teal-100 dark:bg-teal-500/20 text-teal-800 dark:text-teal-300 border-teal-300 dark:border-teal-500/40'
                      : 'bg-white dark:bg-slate-800 text-slate-600 dark:text-slate-400 border-slate-200 dark:border-slate-700'
                  }`}
                  title="Açık olduğunda çözdüğünüz sorular havuza tekrar girmez"
                >
                  Tekrarsız Havuz: {avoidQuestionRepetition ? 'AÇIK' : 'KAPALI'}
                </button>

                {seenCount > 0 && (
                  <button
                    type="button"
                    onClick={() => {
                      if (confirm('Bu modüle ait çözülmüş soru geçmişi sıfırlanacak ve tüm sorular taze havuza dönecek. Onaylıyor musunuz?')) {
                        resetSeenQuestions(selectedModule);
                      }
                    }}
                    className="px-2.5 py-1.5 rounded-xl text-xs font-mono bg-white dark:bg-slate-800 hover:bg-rose-50 text-slate-600 dark:text-slate-300 hover:text-rose-600 dark:hover:text-rose-300 border border-slate-200 dark:border-slate-700 transition-all"
                    title="Döngüyü baştan başlat"
                  >
                    Döngüyü Sıfırla
                  </button>
                )}
              </div>
            </div>

            {/* Progress bar of pool coverage */}
            <div className="space-y-1">
              <div className="w-full h-2 bg-slate-200 dark:bg-slate-800 rounded-full overflow-hidden">
                <div 
                  className="h-full bg-gradient-to-r from-teal-500 to-emerald-400 transition-all duration-300"
                  style={{ width: `${Math.round((seenCount / totalModulePool) * 100)}%` }}
                />
              </div>
              <div className="flex justify-between text-[11px] font-mono text-slate-500 dark:text-slate-400">
                <span>Çözülen Havuz Kapsamı: %{Math.round((seenCount / totalModulePool) * 100)}</span>
                <span>{unseenCount > 0 ? `${unseenCount} taze soru sırada` : 'Tüm havuz çözüldü! Yeni döngü hazır.'}</span>
              </div>
            </div>
          </div>

          {/* Start CTA */}
          <button
            onClick={handleStart}
            className="w-full flex items-center justify-center gap-3 py-4 rounded-2xl bg-gradient-to-r from-teal-500 to-emerald-500 hover:from-teal-400 hover:to-emerald-400 text-slate-950 font-black text-base shadow-lg shadow-teal-500/25 active:scale-95 transition-all"
          >
            <Play className="w-5 h-5 fill-slate-950" />
            <span>Pratik Testini Başlat</span>
          </button>
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
    <div className="max-w-6xl mx-auto space-y-6 animate-fade-in pb-12">
      {/* Top Header Bar */}
      <div className="bg-white dark:bg-fintech-surface rounded-2xl border border-slate-200 dark:border-fintech-border p-4 flex flex-col sm:flex-row sm:items-center justify-between gap-4 shadow-sm dark:shadow-lg">
        <div className="flex items-center gap-3">
          <button
            onClick={() => setShowExitConfirm(true)}
            className="p-2 rounded-xl bg-slate-50 dark:bg-fintech-card hover:bg-rose-50 text-slate-500 hover:text-rose-600 border border-slate-200 dark:border-fintech-border transition-all shadow-sm"
            title="Testten Çık"
          >
            <ArrowLeft className="w-5 h-5" />
          </button>
          <div>
            <h2 className="font-black text-slate-900 dark:text-white text-sm sm:text-base tracking-tight truncate max-w-xs sm:max-w-md">
              {currentSession.title}
            </h2>
            <div className="flex items-center gap-3 text-xs text-slate-600 dark:text-slate-400 font-mono">
              <span>{answeredCount} / {total} Tamamlandı</span>
              <span>•</span>
              <span className="text-teal-600 dark:text-teal-400 font-semibold">
                %{Math.round((answeredCount / total) * 100)} İlerleme
              </span>
            </div>
          </div>
        </div>

        <div className="flex items-center gap-3 self-end sm:self-auto flex-wrap">
          {/* Auto Advance Toggle */}
          <button
            onClick={() => setAutoAdvance(!autoAdvance)}
            className={`flex items-center gap-1.5 px-3 py-1.5 rounded-xl border text-xs font-mono font-semibold transition-all ${
              autoAdvance
                ? 'bg-amber-100 dark:bg-amber-500/20 text-amber-800 dark:text-amber-300 border-amber-300 dark:border-amber-500/40 shadow-sm'
                : 'bg-slate-50 dark:bg-fintech-card text-slate-600 dark:text-slate-400 border-slate-200 dark:border-fintech-border hover:text-slate-900 dark:hover:text-white'
            }`}
            title="Şık seçildiğinde 1.5 saniye sonra sonraki soruya otomatik geçiş yapar"
          >
            <Zap className={`w-3.5 h-3.5 ${autoAdvance ? 'text-amber-500 fill-amber-500 dark:text-amber-400 dark:fill-amber-400' : ''}`} />
            <span>Otomatik İlerle: {autoAdvance ? 'AÇIK' : 'KAPALI'}</span>
          </button>

          <ExamTimer onTick={updateTimer} />

          <button
            onClick={handleFinish}
            className="px-4 py-2 rounded-xl bg-emerald-50 dark:bg-emerald-500/20 hover:bg-emerald-100 dark:hover:bg-emerald-500/30 text-emerald-800 dark:text-emerald-300 border border-emerald-200 dark:border-emerald-500/40 text-xs font-bold transition-all shadow-sm"
          >
            Testi Bitir
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

      {/* Auto Advance Countdown Bar (if active) */}
      {autoAdvanceTimer !== null && (
        <div className="bg-amber-50 dark:bg-amber-950/30 border border-amber-200 dark:border-amber-500/40 rounded-2xl p-3 flex items-center justify-between gap-4 animate-slide-up shadow-sm">
          <div className="flex items-center gap-2 text-amber-800 dark:text-amber-300 text-xs font-semibold">
            <Zap className="w-4 h-4 text-amber-600 dark:text-amber-400 animate-pulse" />
            <span>1.5 saniye sonra sonraki soruya geçiliyor...</span>
          </div>
          <button
            onClick={handleCancelAutoAdvance}
            className="flex items-center gap-1.5 px-3 py-1 rounded-xl bg-amber-100 hover:bg-amber-200 dark:bg-amber-500/20 dark:hover:bg-amber-500/30 text-amber-900 dark:text-amber-200 text-xs font-bold border border-amber-300 dark:border-amber-500/40"
          >
            <Pause className="w-3.5 h-3.5" />
            <span>Durdur & Oku</span>
          </button>
        </div>
      )}

      {/* Main Layout: Question on left, Optical Form on right */}
      <div className="grid grid-cols-1 lg:grid-cols-12 gap-6">
        {/* Left / Center: Question & Explanation */}
        <div className="lg:col-span-8 space-y-6">
          <QuestionCard
            question={currentQ}
            userAnswer={currentAns}
            mode="practice"
            isLocked={isAnswerLocked}
            questionIndex={currentIndex}
            totalQuestions={total}
            onSelectOption={handleSelectOptionWithSound}
          />

          {/* Explanation Panel (Revealed when answered) */}
          {isAnswerLocked && currentAns && currentAns.selected_option !== null && (
            <ExplanationPanel
              question={currentQ}
              isCorrect={currentAns.is_correct}
              selectedOption={currentAns.selected_option}
              onScrolledToBottom={() => setExplanationRead(true)}
              onNextQuestion={handleNextOrFinish}
              isLastQuestion={isLastQuestion}
            />
          )}

          {/* Bottom Navigation Buttons */}
          <div className="flex items-center justify-between pt-2">
            <button
              onClick={prevQuestion}
              disabled={currentIndex === 0}
              className={`flex items-center gap-2 px-5 py-3 rounded-2xl border text-xs font-bold transition-all ${
                currentIndex === 0
                  ? 'opacity-40 cursor-not-allowed bg-slate-100 dark:bg-fintech-surface border-slate-200 dark:border-fintech-border text-slate-400'
                  : 'bg-white dark:bg-fintech-surface hover:bg-slate-50 dark:hover:bg-fintech-card border border-slate-200 dark:border-fintech-border text-slate-700 dark:text-slate-200 hover:text-slate-900 dark:hover:text-white shadow-sm'
              }`}
            >
              <ArrowLeft className="w-4 h-4" />
              <span>Önceki Soru</span>
            </button>

            {isLastQuestion ? (
              <button
                onClick={handleFinish}
                className="flex items-center gap-2 px-6 py-3.5 rounded-2xl bg-emerald-500 hover:bg-emerald-400 text-slate-950 font-black text-xs shadow-md shadow-emerald-500/25 active:scale-95 transition-all"
              >
                <CheckCircle2 className="w-4 h-4" />
                <span>Testi Tamamla & Sonuçları Gör</span>
              </button>
            ) : (
              <button
                onClick={handleNextOrFinish}
                className={`flex items-center gap-2 px-6 py-3.5 rounded-2xl font-black text-xs transition-all ${
                  isAnswerLocked
                    ? 'bg-gradient-to-r from-teal-500 to-emerald-500 hover:from-teal-400 hover:to-emerald-400 text-slate-950 shadow-md shadow-teal-500/25 active:scale-95'
                    : 'bg-slate-100 hover:bg-slate-200 dark:bg-fintech-card text-slate-700 dark:text-slate-300 hover:text-slate-900 dark:hover:text-white border border-slate-200 dark:border-fintech-border'
                }`}
              >
                <span>Sonraki Soru (Enter / →)</span>
                <ArrowRight className="w-4 h-4" />
              </button>
            )}
          </div>
        </div>

        {/* Right Column: Optical Form & Keyboard Hints */}
        <div className="lg:col-span-4 space-y-6">
          <OpticalForm
            questions={currentSession.questions}
            userAnswers={currentSession.user_answers}
            currentIndex={currentIndex}
            mode="practice"
            onSelectQuestion={goToQuestion}
          />

          {/* Shortcut Keys Box */}
          <div className="bg-white dark:bg-fintech-surface rounded-2xl border border-slate-200 dark:border-fintech-border p-4 space-y-2 text-xs text-slate-600 dark:text-slate-400 shadow-sm">
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
                className="px-4 py-2 rounded-xl bg-teal-500 hover:bg-teal-400 text-slate-950 text-xs font-bold shadow-md shadow-teal-500/25 transition-all"
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
