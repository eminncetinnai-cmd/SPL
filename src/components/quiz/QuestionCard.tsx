import React, { useState, useMemo } from 'react';
import { Star, Flag, CheckCircle, XCircle, Calculator } from 'lucide-react';
import { Question, UserAnswer, QuizMode } from '../../types/exam';
import { useProgressStore } from '../../stores/progressStore';
import { FormulaDrawer } from './FormulaDrawer';

interface QuestionCardProps {
  question: Question;
  userAnswer?: UserAnswer | null;
  mode: QuizMode;
  isLocked: boolean;
  questionIndex: number;
  totalQuestions: number;
  onSelectOption: (key: 'A' | 'B' | 'C' | 'D' | 'E') => void;
  onToggleReviewFlag?: () => void;
}

export const QuestionCard: React.FC<QuestionCardProps> = React.memo(({
  question,
  userAnswer,
  mode,
  isLocked,
  questionIndex,
  totalQuestions,
  onSelectOption,
  onToggleReviewFlag,
}) => {
  const { toggleBookmark, isBookmarked } = useProgressStore();
  const [showFormulaDrawer, setShowFormulaDrawer] = useState(false);

  const bookmarked = isBookmarked(question.id);
  const selectedKey = userAnswer?.selected_option;
  const isCorrectAnswer = question.correct_answer;

  const isNumericalQuestion = useMemo(() => {
    const text = (question.text + ' ' + (question.topic || '')).toLowerCase();
    return (
      text.includes('hesaplay') ||
      text.includes('bedelli') ||
      text.includes('rüçhan') ||
      text.includes('temettü') ||
      text.includes('margin call') ||
      text.includes('özkaynak') ||
      text.includes('özsermaye') ||
      text.includes('kirli fiyat') ||
      text.includes('tahvil') ||
      text.includes('kupon') ||
      text.includes('başlangıç teminat') ||
      text.includes('tl') ||
      text.includes('%')
    );
  }, [question]);

  const handleKeySelect = (key: 'A' | 'B' | 'C' | 'D' | 'E') => {
    if (mode === 'practice' && isLocked) return;

    // Web Haptic vibration feedback
    if (typeof navigator !== 'undefined' && 'vibrate' in navigator) {
      try {
        if (mode === 'practice') {
          const isCorrect = key === isCorrectAnswer;
          navigator.vibrate(isCorrect ? [15, 25, 20] : 30);
        } else {
          navigator.vibrate(15);
        }
      } catch (e) {}
    }

    onSelectOption(key);
  };

  return (
    <div className="w-full bg-white dark:bg-fintech-surface rounded-2xl sm:rounded-3xl border border-slate-200 dark:border-fintech-border shadow-xs sm:shadow-sm p-4 sm:p-6 space-y-4 sm:space-y-5">
      {/* Formula Drawer Bottom Sheet */}
      <FormulaDrawer
        isOpen={showFormulaDrawer}
        onClose={() => setShowFormulaDrawer(false)}
      />
      {/* Compact iOS-style Header Info */}
      <div className="flex items-center justify-between gap-2 border-b border-slate-100 dark:border-fintech-border/70 pb-3">
        <div className="flex items-center gap-2">
          <span className="px-2.5 py-1 rounded-xl bg-teal-500/10 text-teal-800 dark:text-teal-300 border border-teal-500/20 font-mono text-xs font-bold">
            Soru {questionIndex + 1}
          </span>
          <span className="px-2.5 py-1 rounded-xl bg-slate-100 text-slate-700 font-mono text-xs font-semibold border border-slate-200 dark:bg-slate-800 dark:text-slate-300 dark:border-slate-700">
            Modül {question.module_id}
          </span>
          {isLocked && question.topic && (
            <span className="text-[11px] text-slate-600 dark:text-slate-400 font-mono px-2 py-0.5 rounded-lg bg-slate-100 dark:bg-slate-800 truncate max-w-[150px] sm:max-w-xs">
              {question.topic}
            </span>
          )}
        </div>

        {/* Action Buttons: Formula, Star and Review Flag */}
        <div className="flex items-center gap-1.5 shrink-0">
          <button
            onClick={() => setShowFormulaDrawer(true)}
            className={`flex items-center gap-1 px-2.5 py-1.5 rounded-xl text-xs font-bold transition-all border ${
              isNumericalQuestion
                ? 'bg-amber-500/15 text-amber-700 dark:text-amber-300 border-amber-500/40 shadow-xs'
                : 'bg-slate-100 text-slate-600 hover:text-slate-900 border-slate-200 dark:bg-slate-800/80 dark:text-slate-400 dark:border-slate-700'
            }`}
            title="Sayısal Formül Çekmecesini Aç"
          >
            <Calculator className={`w-3.5 h-3.5 ${isNumericalQuestion ? 'text-amber-500' : ''}`} />
            <span className="text-[11px]">Formül</span>
          </button>

          {mode === 'simulation' && onToggleReviewFlag && (
            <button
              onClick={onToggleReviewFlag}
              className={`flex items-center gap-1 px-3 py-1.5 rounded-xl text-xs font-bold transition-all ${
                userAnswer?.marked_for_review
                  ? 'bg-amber-100 text-amber-900 border border-amber-300 shadow-sm dark:bg-amber-500/20 dark:text-amber-300 dark:border-amber-500/40'
                  : 'bg-slate-100 text-slate-600 hover:text-slate-900 border border-slate-200 dark:bg-slate-800/80 dark:text-slate-400 dark:border-slate-700'
              }`}
              title="Daha sonra tekrar incelemek üzere bayrakla"
            >
              <Flag className={`w-3.5 h-3.5 ${userAnswer?.marked_for_review ? 'fill-amber-500 text-amber-500' : ''}`} />
              <span className="hidden sm:inline">Gözden Geçir</span>
            </button>
          )}

          <button
            onClick={() => toggleBookmark(question.id)}
            className={`p-2 rounded-xl transition-all border ${
              bookmarked
                ? 'bg-amber-100 text-amber-600 border-amber-300 dark:bg-amber-500/15 dark:text-amber-400 dark:border-amber-500/30 shadow-xs'
                : 'bg-slate-100 text-slate-500 hover:text-amber-600 border-slate-200 dark:bg-slate-800/80 dark:text-slate-400 dark:border-slate-700'
            }`}
            title={bookmarked ? 'Yıldızı Kaldır' : 'Soruya Yıldız Ekle'}
          >
            <Star className={`w-4 h-4 ${bookmarked ? 'fill-amber-500 text-amber-500' : ''}`} />
          </button>
        </div>
      </div>

      {/* Question Text with comfortable typography for 6.9" OLED */}
      <div className="text-slate-900 dark:text-slate-100 text-base sm:text-lg leading-relaxed font-semibold whitespace-pre-line select-text">
        {question.text}
      </div>

      {/* Options List - Large, Thumb-Friendly Tap Targets */}
      <div className="space-y-3 pt-1">
        {question.options.map((opt) => {
          const isSelected = selectedKey === opt.key;
          const isCorrect = opt.key === isCorrectAnswer;
          const isPracticeMode = mode === 'practice';

          let buttonStyle =
            'bg-white hover:bg-slate-50 border-slate-200 text-slate-800 hover:border-slate-300 shadow-xs dark:bg-fintech-card dark:hover:bg-fintech-cardHover dark:border-fintech-border dark:text-slate-200';
          let badgeStyle =
            'bg-slate-100 text-slate-800 border-slate-300 font-bold dark:bg-slate-800 dark:text-slate-200 dark:border-slate-600';

          if (isPracticeMode && isLocked) {
            if (isCorrect) {
              buttonStyle =
                'bg-emerald-50/90 border-emerald-500 text-emerald-950 shadow-xs ring-2 ring-emerald-500/30 font-medium dark:bg-emerald-950/50 dark:border-emerald-500 dark:text-emerald-100';
              badgeStyle =
                'bg-emerald-600 text-white border-emerald-700 font-bold dark:bg-emerald-500 dark:text-slate-950 dark:border-emerald-400';
            } else if (isSelected && !isCorrect) {
              buttonStyle =
                'bg-rose-50/90 border-rose-500 text-rose-950 shadow-xs ring-2 ring-rose-500/30 font-medium dark:bg-rose-950/50 dark:border-rose-500 dark:text-rose-100';
              badgeStyle =
                'bg-rose-600 text-white border-rose-700 font-bold dark:bg-rose-500 dark:text-white dark:border-rose-400';
            } else {
              buttonStyle =
                'bg-slate-50/50 border-slate-200 text-slate-400 opacity-50 dark:bg-slate-900/40 dark:border-slate-800/80 dark:text-slate-500';
              badgeStyle =
                'bg-slate-100 text-slate-400 border-slate-200 dark:bg-slate-900 dark:text-slate-600 dark:border-slate-800';
            }
          } else if (isSelected) {
            buttonStyle =
              'bg-teal-50/95 border-teal-500 text-teal-950 shadow-xs ring-2 ring-teal-500/40 font-medium dark:bg-teal-950/60 dark:border-teal-500 dark:text-teal-100';
            badgeStyle =
              'bg-teal-600 text-white border-teal-700 font-bold dark:bg-teal-500 dark:text-slate-950 dark:border-teal-400';
          }

          return (
            <button
              key={opt.key}
              onClick={() => handleKeySelect(opt.key)}
              disabled={isPracticeMode && isLocked}
              className={`w-full min-h-[56px] sm:min-h-[60px] flex items-start gap-3.5 p-3.5 sm:p-4 rounded-2xl border text-left transition-all relative group cursor-pointer ${buttonStyle} ${
                isPracticeMode && isLocked ? 'cursor-default' : 'active:scale-[0.985]'
              }`}
            >
              {/* Option Letter Badge */}
              <div
                className={`w-8 h-8 sm:w-9 sm:h-9 rounded-xl flex items-center justify-center font-mono text-xs sm:text-sm shrink-0 border transition-all ${badgeStyle}`}
              >
                {opt.key}
              </div>

              {/* Option Text */}
              <div className="flex-1 text-sm sm:text-base pt-0.5 leading-snug">
                {opt.text}
              </div>

              {/* Status Icons in Practice Mode */}
              {isPracticeMode && isLocked && (
                <div className="shrink-0 pt-0.5">
                  {isCorrect && (
                    <CheckCircle className="w-5 h-5 text-emerald-500 fill-emerald-500/20" />
                  )}
                  {isSelected && !isCorrect && (
                    <XCircle className="w-5 h-5 text-rose-500 fill-rose-500/20" />
                  )}
                </div>
              )}
            </button>
          );
        })}
      </div>
    </div>
  );
});
