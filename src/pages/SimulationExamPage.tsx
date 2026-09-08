import React, { useState, useEffect } from 'react';
import { 
  ArrowLeft, 
  ArrowRight, 
  Sparkles, 
  AlertTriangle, 
  Timer, 
  CheckCircle2, 
  HelpCircle,
  Flag,
  FileCheck,
  Award
} from 'lucide-react';
import { useQuizStore } from '../stores/quizStore';
import { QuestionCard } from '../components/quiz/QuestionCard';
import { OpticalForm } from '../components/quiz/OpticalForm';
import { ExamTimer } from '../components/quiz/ExamTimer';
import { ModuleId, Question } from '../types/exam';
import allQuestionsData from '../data/all_questions.json';

import { useProgressStore } from '../stores/progressStore';
import { selectSimulationExam100, selectSmartQuestions } from '../utils/questionSelector';

interface SimulationExamPageProps {
  onNavigate: (page: string, params?: any) => void;
}

export const SimulationExamPage: React.FC<SimulationExamPageProps> = ({ onNavigate }) => {
  const {
    currentSession,
    startQuiz,
    selectOption,
    toggleReviewFlag,
    goToQuestion,
    nextQuestion,
    prevQuestion,
    finishQuiz,
    updateTimer,
  } = useQuizStore();

  const { seenQuestionIds, avoidQuestionRepetition, setAvoidRepetition, resetSeenQuestions } = useProgressStore();

  const [examType, setExamType] = useState<'full' | 'single'>('full');
  const [selectedModule, setSelectedModule] = useState<ModuleId>('1001');
  const [showFinishModal, setShowFinishModal] = useState(false);

  const allQs = allQuestionsData as Question[];
  const totalPool = examType === 'full' 
    ? allQs.length 
    : allQs.filter((q) => q.module_id === selectedModule).length;
  const seenPoolCount = examType === 'full'
    ? seenQuestionIds.length
    : seenQuestionIds.filter((id) => id.includes(`_${selectedModule}_`)).length;
  const unseenPoolCount = Math.max(0, totalPool - seenPoolCount);

  // Keyboard shortcut listener
  useEffect(() => {
    const handleKeyDown = (e: KeyboardEvent) => {
      if (!currentSession || currentSession.is_completed) return;

      const key = e.key.toUpperCase();
      if (['A', 'B', 'C', 'D', 'E'].includes(key)) {
        selectOption(key as any);
      } else if (['1', '2', '3', '4', '5'].includes(e.key)) {
        const keyMap: Record<string, any> = { '1': 'A', '2': 'B', '3': 'C', '4': 'D', '5': 'E' };
        selectOption(keyMap[e.key]);
      } else if (e.key === 'ArrowRight') {
        nextQuestion();
      } else if (e.key === 'ArrowLeft') {
        prevQuestion();
      } else if (e.key.toUpperCase() === 'F') {
        if (currentSession.questions[currentSession.current_index]) {
          toggleReviewFlag(currentSession.questions[currentSession.current_index].id);
        }
      }
    };

    window.addEventListener('keydown', handleKeyDown);
    return () => window.removeEventListener('keydown', handleKeyDown);
  }, [currentSession, nextQuestion, prevQuestion, selectOption, toggleReviewFlag]);

  const handleStartExam = () => {
    const allQs = allQuestionsData as Question[];

    if (examType === 'full') {
      const { questions: combined100 } = selectSimulationExam100(
        allQs,
        seenQuestionIds,
        avoidQuestionRepetition
      );

      startQuiz({
        mode: 'simulation',
        moduleId: 'all',
        customQuestions: combined100,
        title: 'SPK SPL Düzey 1 Resmi Sınav Simülasyonu (100 Soru)',
        timeLimitMinutes: 120, // 2 Hours SPK standard
      });
    } else {
      const selection = selectSmartQuestions(allQs, {
        moduleId: selectedModule,
        count: 25,
        sourceFilter: 'all',
        seenQuestionIds,
        avoidRepetition: avoidQuestionRepetition,
      });

      startQuiz({
        mode: 'simulation',
        moduleId: selectedModule,
        customQuestions: selection.questions,
        title: `Modül ${selectedModule} Süreli Deneme Sınavı (25 Soru)`,
        timeLimitMinutes: 30,
      });
    }
  };

  const handleFinishExam = () => {
    setShowFinishModal(false);
    const completed = finishQuiz();
    if (completed) {
      onNavigate('results');
    }
  };

  // Pre-Exam Rules & Setup View
  if (!currentSession || currentSession.is_completed) {
    return (
      <div className="max-w-4xl mx-auto space-y-8 animate-fade-in py-4">
        <div className="flex items-center gap-4">
          <button
            onClick={() => onNavigate('home')}
            className="p-2.5 rounded-xl bg-white dark:bg-fintech-surface hover:bg-slate-100 dark:hover:bg-fintech-card border border-slate-200 dark:border-fintech-border text-slate-700 dark:text-slate-300 hover:text-slate-900 dark:hover:text-white shadow-sm transition-all"
          >
            <ArrowLeft className="w-5 h-5" />
          </button>
          <div>
            <h1 className="text-2xl font-black text-slate-900 dark:text-white tracking-tight">
              SPK SPL Düzey 1 Sınav Simülasyonu
            </h1>
            <p className="text-xs sm:text-sm text-slate-600 dark:text-slate-400">
              Resmi SPK sınav kuralları, optik form sistemi ve süreli karne değerlendirmesi.
            </p>
          </div>
        </div>

        {/* Configuration Card */}
        <div className="bg-white dark:bg-fintech-surface rounded-3xl border border-slate-200 dark:border-teal-500/30 p-6 sm:p-8 space-y-8 shadow-sm dark:shadow-2xl">
          {/* Exam Type Selection */}
          <div className="space-y-3">
            <label className="text-xs font-mono uppercase tracking-wider text-slate-700 dark:text-slate-300 font-bold block">
              1. SINAV TÜRÜNÜ SEÇİN
            </label>
            <div className="grid grid-cols-1 sm:grid-cols-2 gap-4">
              <button
                onClick={() => setExamType('full')}
                className={`p-5 rounded-2xl border text-left transition-all relative ${
                  examType === 'full'
                    ? 'bg-teal-50 dark:bg-teal-500/15 border-teal-500 text-teal-950 dark:text-white shadow-sm ring-1 ring-teal-500/30'
                    : 'bg-slate-50 dark:bg-fintech-card border-slate-200 dark:border-fintech-border text-slate-600 dark:text-slate-400 hover:text-slate-900 dark:hover:text-slate-200 hover:border-slate-300'
                }`}
              >
                <div className="flex items-center justify-between mb-2">
                  <span className="font-bold text-base text-slate-900 dark:text-white">Tam Sınav Simülasyonu</span>
                  <span className="px-2.5 py-0.5 rounded-full bg-teal-500 text-slate-950 text-xs font-mono font-bold">
                    100 Soru
                  </span>
                </div>
                <p className="text-xs text-slate-600 dark:text-slate-300 leading-relaxed">
                  4 Dersin tamamı (1001, 1003, 1005, 1012) x 25'er soru. Süre: <strong>120 Dakika</strong>. Gerçek SPK lisanslama sınav formatı.
                </p>
              </button>

              <button
                onClick={() => setExamType('single')}
                className={`p-5 rounded-2xl border text-left transition-all relative ${
                  examType === 'single'
                    ? 'bg-teal-50 dark:bg-teal-500/15 border-teal-500 text-teal-950 dark:text-white shadow-sm ring-1 ring-teal-500/30'
                    : 'bg-slate-50 dark:bg-fintech-card border-slate-200 dark:border-fintech-border text-slate-600 dark:text-slate-400 hover:text-slate-900 dark:hover:text-slate-200 hover:border-slate-300'
                }`}
              >
                <div className="flex items-center justify-between mb-2">
                  <span className="font-bold text-base text-slate-900 dark:text-white">Tek Modül Denemesi</span>
                  <span className="px-2.5 py-0.5 rounded-full bg-slate-200 dark:bg-slate-800 text-slate-700 dark:text-slate-300 text-xs font-mono font-bold">
                    25 Soru
                  </span>
                </div>
                <p className="text-xs text-slate-600 dark:text-slate-300 leading-relaxed">
                  Seçeceğiniz tek bir ders için 25 soruluk süreli deneme. Süre: <strong>30 Dakika</strong>.
                </p>
              </button>
            </div>
          </div>

          {/* Module Selector if Single Exam */}
          {examType === 'single' && (
            <div className="space-y-3 pt-2">
              <label className="text-xs font-mono uppercase tracking-wider text-slate-700 dark:text-slate-300 font-bold block">
                2. DENENECEK DERSİ SEÇİN
              </label>
              <div className="grid grid-cols-1 sm:grid-cols-2 gap-3">
                {[
                  { id: '1001', name: '1001 - Sermaye Piyasası Mevzuatı' },
                  { id: '1003', name: '1003 - Sermaye Piyasası Araçları 1' },
                  { id: '1005', name: '1005 - Yatırım Kuruluşları' },
                  { id: '1012', name: '1012 - Takas, Saklama ve Operasyon' },
                ].map((m) => (
                  <button
                    key={m.id}
                    onClick={() => setSelectedModule(m.id as ModuleId)}
                    className={`p-3.5 rounded-xl border text-left text-xs font-bold transition-all ${
                      selectedModule === m.id
                        ? 'bg-teal-50 dark:bg-teal-500/20 border-teal-500 text-teal-800 dark:text-teal-300 shadow-sm'
                        : 'bg-slate-50 dark:bg-fintech-card border-slate-200 dark:border-fintech-border text-slate-700 dark:text-slate-400 hover:text-slate-900 dark:hover:text-slate-200'
                    }`}
                  >
                    {m.name}
                  </button>
                ))}
              </div>
            </div>
          )}

          {/* Official SPK Exam Rules Box */}
          <div className="bg-amber-50/70 dark:bg-slate-900/80 rounded-2xl border border-amber-200 dark:border-fintech-border p-5 space-y-3">
            <h4 className="font-bold text-xs font-mono text-amber-800 dark:text-amber-400 uppercase tracking-wider flex items-center gap-2">
              <Award className="w-4 h-4 text-amber-600 dark:text-amber-400" />
              <span>Resmi SPK SPL Düzey 1 Sınav ve Puanlama Kuralları</span>
            </h4>
            <ul className="text-xs text-slate-700 dark:text-slate-300 space-y-2 list-disc list-inside leading-relaxed">
              <li>Sınavda <strong>yanlış cevaplar doğru cevapları götürmez</strong> (Net hesaplanmaz, her doğru soru 4 puandır).</li>
              <li>Lisans almaya hak kazanmak için <strong>tüm derslerin genel aritmetik ortalaması en az 60 puan</strong> olmalıdır.</li>
              <li>Herhangi bir modülden <strong>50 puanın altında kalınırsa</strong> (min 50 barajı), genel ortalama 60 üstü olsa dahi o dersten kalınmış sayılır.</li>
              <li>Sınav sırasında soruları boş bırakabilir, daha sonra gözden geçirmek üzere bayrak ekleyebilir veya değiştirebilirsiniz.</li>
              <li>Sınav sonuçları ve detaylı analitik çözümler sınavı bitirdiğiniz anda karne halinde sunulur.</li>
            </ul>
          </div>

          {/* Anti-Repeat Smart Pool Status Banner */}
          <div className="bg-teal-50/70 dark:bg-slate-900/90 rounded-2xl border border-teal-200 dark:border-teal-500/30 p-5 space-y-3">
            <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-3">
              <div className="flex items-center gap-2.5">
                <div className="w-9 h-9 rounded-xl bg-teal-500/15 border border-teal-500/30 flex items-center justify-center shrink-0">
                  <FileCheck className="w-5 h-5 text-teal-600 dark:text-teal-400" />
                </div>
                <div>
                  <span className="font-bold text-xs sm:text-sm text-slate-900 dark:text-white block">
                    🛡️ Akıllı Soru Rotasyonu & Tekrarsız Havuz
                  </span>
                  <span className="text-xs text-slate-600 dark:text-slate-300 block">
                    {unseenPoolCount} / {totalPool} çözülmemiş taze soru mevcut ({examType === 'full' ? 'Tüm Modüller' : `Modül ${selectedModule}`})
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
                  title="Açık olduğunda çözdüğünüz sorular denemelere tekrar girmez"
                >
                  Tekrarsız Havuz: {avoidQuestionRepetition ? 'AÇIK' : 'KAPALI'}
                </button>

                {seenPoolCount > 0 && (
                  <button
                    type="button"
                    onClick={() => {
                      if (confirm('Soru havuzu geçmişiniz sıfırlanacak ve tüm sorular taze deneme havuzuna dönecektir. Onaylıyor musunuz?')) {
                        resetSeenQuestions(examType === 'full' ? 'all' : selectedModule);
                      }
                    }}
                    className="px-2.5 py-1.5 rounded-xl text-xs font-mono bg-white dark:bg-slate-800 hover:bg-rose-50 text-slate-600 dark:text-slate-300 hover:text-rose-600 dark:hover:text-rose-300 border border-slate-200 dark:border-slate-700 transition-all"
                    title="Havuzu yenile ve baştan başlat"
                  >
                    Döngüyü Sıfırla
                  </button>
                )}
              </div>
            </div>

            {/* Progress bar */}
            <div className="space-y-1">
              <div className="w-full h-2 bg-slate-200 dark:bg-slate-800 rounded-full overflow-hidden">
                <div 
                  className="h-full bg-gradient-to-r from-teal-500 to-emerald-400 transition-all duration-300"
                  style={{ width: `${Math.round((seenPoolCount / totalPool) * 100)}%` }}
                />
              </div>
              <div className="flex justify-between text-[11px] font-mono text-slate-500 dark:text-slate-400">
                <span>Havuz Kapsamı: %{Math.round((seenPoolCount / totalPool) * 100)}</span>
                <span>{unseenPoolCount > 0 ? `${unseenPoolCount} yeni soru sırada` : 'Tüm havuz denendi! Yeni döngü hazır.'}</span>
              </div>
            </div>
          </div>

          {/* Start Exam Button */}
          <button
            onClick={handleStartExam}
            className="w-full flex items-center justify-center gap-3 py-4 rounded-2xl bg-gradient-to-r from-teal-500 to-emerald-500 hover:from-teal-400 hover:to-emerald-400 text-slate-950 font-black text-base shadow-lg shadow-teal-500/25 active:scale-95 transition-all"
          >
            <Sparkles className="w-5 h-5 fill-slate-950" />
            <span>Sınavı Başlat & Sayacı Çalıştır</span>
          </button>
        </div>
      </div>
    );
  }

  // Active Simulation Exam View
  const currentIndex = currentSession.current_index;
  const total = currentSession.questions.length;
  const currentQ = currentSession.questions[currentIndex];
  const currentAns = currentSession.user_answers[currentQ.id];
  const isLastQuestion = currentIndex === total - 1;

  const answeredCount = Object.values(currentSession.user_answers).filter(
    (a) => a.selected_option !== null
  ).length;
  const flaggedCount = Object.values(currentSession.user_answers).filter(
    (a) => a.marked_for_review
  ).length;

  return (
    <div className="max-w-6xl mx-auto space-y-6 animate-fade-in pb-12">
      {/* Top Header Bar */}
      <div className="bg-white dark:bg-fintech-surface rounded-2xl border border-slate-200 dark:border-fintech-border p-4 flex items-center justify-between gap-4 shadow-sm dark:shadow-xl">
        <div>
          <h2 className="font-black text-slate-900 dark:text-white text-sm sm:text-base tracking-tight truncate max-w-xs sm:max-w-md">
            {currentSession.title}
          </h2>
          <div className="flex items-center gap-3 text-xs text-slate-600 dark:text-slate-400 font-mono">
            <span>{answeredCount} / {total} İşaretlendi</span>
            {flaggedCount > 0 && (
              <span className="text-amber-600 dark:text-amber-400 font-semibold">• {flaggedCount} Bayraklı</span>
            )}
          </div>
        </div>

        <div className="flex items-center gap-4">
          <ExamTimer
            timeLimitSeconds={currentSession.time_limit_seconds}
            onTick={updateTimer}
            onTimeUp={handleFinishExam}
          />

          <button
            onClick={() => setShowFinishModal(true)}
            className="px-5 py-2.5 rounded-xl bg-gradient-to-r from-emerald-500 to-teal-500 hover:from-emerald-400 hover:to-teal-400 text-slate-950 font-black text-xs shadow-md shadow-emerald-500/20 active:scale-95 transition-all"
          >
            Sınavı Bitir
          </button>
        </div>
      </div>

      {/* Progress Line */}
      <div className="w-full h-1.5 bg-slate-200 dark:bg-fintech-card rounded-full overflow-hidden">
        <div
          className="h-full bg-gradient-to-r from-teal-500 to-emerald-400 transition-all duration-300"
          style={{ width: `${((currentIndex + 1) / total) * 100}%` }}
        />
      </div>

      {/* Question & Optical Sheet Grid */}
      <div className="grid grid-cols-1 lg:grid-cols-12 gap-6">
        {/* Question Area */}
        <div className="lg:col-span-8 space-y-6">
          <QuestionCard
            question={currentQ}
            userAnswer={currentAns}
            mode="simulation"
            isLocked={false}
            questionIndex={currentIndex}
            totalQuestions={total}
            onSelectOption={selectOption}
            onToggleReviewFlag={() => toggleReviewFlag(currentQ.id)}
          />

          {/* Navigation Controls */}
          <div className="flex items-center justify-between pt-2">
            <button
              onClick={prevQuestion}
              disabled={currentIndex === 0}
              className={`flex items-center gap-2 px-5 py-3 rounded-xl border text-xs font-bold transition-all ${
                currentIndex === 0
                  ? 'opacity-40 cursor-not-allowed bg-slate-100 dark:bg-fintech-surface border-slate-200 dark:border-fintech-border text-slate-400'
                  : 'bg-white dark:bg-fintech-surface hover:bg-slate-50 dark:hover:bg-fintech-card border-slate-200 dark:border-fintech-border text-slate-700 dark:text-slate-200 hover:text-slate-900 dark:hover:text-white shadow-sm'
              }`}
            >
              <ArrowLeft className="w-4 h-4" />
              <span>Önceki Soru</span>
            </button>

            <button
              onClick={() => toggleReviewFlag(currentQ.id)}
              className={`flex items-center gap-1.5 px-4 py-3 rounded-xl text-xs font-semibold border transition-all ${
                currentAns?.marked_for_review
                  ? 'bg-amber-100 dark:bg-amber-500/20 text-amber-800 dark:text-amber-300 border-amber-300 dark:border-amber-500/40 shadow-sm'
                  : 'bg-white dark:bg-fintech-surface text-slate-600 dark:text-slate-400 hover:text-slate-900 dark:hover:text-slate-200 border-slate-200 dark:border-fintech-border shadow-sm'
              }`}
            >
              <Flag className={`w-4 h-4 ${currentAns?.marked_for_review ? 'fill-amber-500 text-amber-500 dark:fill-amber-400 dark:text-amber-400' : ''}`} />
              <span>{currentAns?.marked_for_review ? 'Bayrağı Kaldır' : 'Gözden Geçir (Flag)'}</span>
            </button>

            {isLastQuestion ? (
              <button
                onClick={() => setShowFinishModal(true)}
                className="flex items-center gap-2 px-6 py-3 rounded-xl bg-emerald-500 hover:bg-emerald-400 text-slate-950 font-black text-xs shadow-md shadow-emerald-500/25 active:scale-95 transition-all"
              >
                <CheckCircle2 className="w-4 h-4" />
                <span>Sınavı Bitir</span>
              </button>
            ) : (
              <button
                onClick={nextQuestion}
                className="flex items-center gap-2 px-6 py-3 rounded-xl bg-teal-500 hover:bg-teal-400 text-slate-950 font-extrabold text-xs shadow-md shadow-teal-500/25 active:scale-95 transition-all"
              >
                <span>Sonraki Soru</span>
                <ArrowRight className="w-4 h-4" />
              </button>
            )}
          </div>
        </div>

        {/* Optical Sheet Form on Right */}
        <div className="lg:col-span-4 space-y-6">
          <OpticalForm
            questions={currentSession.questions}
            userAnswers={currentSession.user_answers}
            currentIndex={currentIndex}
            mode="simulation"
            onSelectQuestion={goToQuestion}
          />
        </div>
      </div>

      {/* Confirmation Modal to Finish Exam */}
      {showFinishModal && (
        <div className="fixed inset-0 z-50 bg-slate-950/60 backdrop-blur-sm flex items-center justify-center p-4">
          <div className="bg-white dark:bg-fintech-surface rounded-3xl border border-slate-200 dark:border-fintech-border max-w-md w-full p-6 space-y-5 shadow-2xl animate-slide-up">
            <div className="flex items-center gap-3 text-emerald-600 dark:text-emerald-400">
              <FileCheck className="w-6 h-6" />
              <h3 className="font-black text-lg text-slate-900 dark:text-white">Sınavı Bitirmek İstiyor musunuz?</h3>
            </div>

            <div className="bg-slate-50 dark:bg-fintech-card p-4 rounded-2xl border border-slate-200 dark:border-fintech-border text-xs space-y-2 font-mono">
              <div className="flex justify-between text-slate-600 dark:text-slate-300">
                <span>Toplam Soru:</span>
                <span className="font-bold text-slate-900 dark:text-white">{total}</span>
              </div>
              <div className="flex justify-between text-teal-600 dark:text-teal-400">
                <span>Cevaplanan Soru:</span>
                <span className="font-bold">{answeredCount}</span>
              </div>
              <div className="flex justify-between text-slate-600 dark:text-slate-400">
                <span>Boş Bırakılan:</span>
                <span className="font-bold text-rose-600 dark:text-rose-300">{total - answeredCount}</span>
              </div>
              {flaggedCount > 0 && (
                <div className="flex justify-between text-amber-600 dark:text-amber-400">
                  <span>Gözden Geçirilecek (Bayraklı):</span>
                  <span className="font-bold">{flaggedCount}</span>
                </div>
              )}
            </div>

            <p className="text-xs text-slate-600 dark:text-slate-400 leading-relaxed">
              Sınavı bitirdikten sonra tüm soruların puanlaması SPK standartlarında hesaplanacak ve ayrıntılı çözüm analizleri görüntülenecektir.
            </p>

            <div className="flex items-center justify-end gap-3 pt-2">
              <button
                onClick={() => setShowFinishModal(false)}
                className="px-4 py-2.5 rounded-xl bg-slate-100 hover:bg-slate-200 dark:bg-fintech-card dark:hover:bg-fintech-cardHover text-slate-700 dark:text-slate-300 text-xs font-semibold border border-slate-200 dark:border-fintech-border transition-colors"
              >
                Sınava Devam Et
              </button>
              <button
                onClick={handleFinishExam}
                className="px-5 py-2.5 rounded-xl bg-emerald-500 hover:bg-emerald-400 text-slate-950 text-xs font-black shadow-md shadow-emerald-500/30 active:scale-95 transition-all"
              >
                Evet, Sınavı Bitir
              </button>
            </div>
          </div>
        </div>
      )}
    </div>
  );
};
