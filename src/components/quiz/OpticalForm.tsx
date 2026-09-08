import React from 'react';
import { Flag, Check, X, AlertCircle } from 'lucide-react';
import { Question, UserAnswer, QuizMode } from '../../types/exam';

interface OpticalFormProps {
  questions: Question[];
  userAnswers: Record<string, UserAnswer>;
  currentIndex: number;
  mode: QuizMode;
  isCompleted?: boolean;
  onSelectQuestion: (index: number) => void;
}

export const OpticalForm: React.FC<OpticalFormProps> = ({
  questions,
  userAnswers,
  currentIndex,
  mode,
  isCompleted,
  onSelectQuestion,
}) => {
  const answeredCount = Object.values(userAnswers).filter(a => a.selected_option !== null).length;
  const flaggedCount = Object.values(userAnswers).filter(a => a.marked_for_review).length;
  const total = questions.length;

  return (
    <div className="bg-white dark:bg-fintech-surface rounded-2xl border border-slate-200 dark:border-fintech-border p-5 space-y-4 shadow-sm">
      <div className="flex items-center justify-between border-b border-slate-200 dark:border-fintech-border pb-3">
        <h4 className="font-bold text-sm text-slate-800 dark:text-slate-200">Soru Navigatörü</h4>
        <span className="text-xs font-mono font-bold text-slate-500 dark:text-slate-400">
          {answeredCount} / {total} Cevaplandı
        </span>
      </div>

      {/* Grid of Question Numbers */}
      <div className="grid grid-cols-5 gap-2 max-h-72 overflow-y-auto pr-1">
        {questions.map((q, idx) => {
          const ans = userAnswers[q.id];
          const isAnswered = ans && ans.selected_option !== null;
          const isFlagged = ans?.marked_for_review;
          const isCurrent = currentIndex === idx;

          let btnClass = 'bg-slate-50 text-slate-600 hover:text-slate-900 border-slate-200 hover:bg-slate-100 hover:border-slate-300 dark:bg-fintech-card dark:text-slate-400 dark:hover:text-white dark:border-fintech-border dark:hover:border-slate-600';

          if (isCompleted || (mode === 'practice' && isAnswered)) {
            // Show correct / wrong in completed review or locked practice
            if (ans?.is_correct) {
              btnClass = 'bg-emerald-50 border-emerald-500 text-emerald-900 font-bold dark:bg-emerald-950/60 dark:border-emerald-500/80 dark:text-emerald-300';
            } else if (isAnswered) {
              btnClass = 'bg-rose-50 border-rose-500 text-rose-900 font-bold dark:bg-rose-950/60 dark:border-rose-500/80 dark:text-rose-300';
            }
          } else if (isAnswered) {
            btnClass = 'bg-teal-50 border-teal-500 text-teal-950 font-bold dark:bg-teal-950/60 dark:border-teal-500 dark:text-teal-300';
          }

          if (isCurrent) {
            btnClass += ' ring-2 ring-teal-500 ring-offset-2 ring-offset-white dark:ring-offset-fintech-dark';
          }

          return (
            <button
              key={q.id}
              onClick={() => onSelectQuestion(idx)}
              className={`relative h-10 rounded-xl flex items-center justify-center font-mono text-xs border transition-all ${btnClass}`}
            >
              <span>{idx + 1}</span>

              {/* Review Flag Badge */}
              {isFlagged && (
                <span className="absolute -top-1 -right-1 w-3 h-3 rounded-full bg-amber-400 ring-2 ring-white dark:ring-fintech-dark" />
              )}
            </button>
          );
        })}
      </div>

      {/* Legend */}
      <div className="pt-2 border-t border-slate-200 dark:border-fintech-border/60 text-[11px] text-slate-500 dark:text-slate-400 space-y-1.5 font-medium">
        <div className="flex items-center justify-between">
          <div className="flex items-center gap-1.5">
            <span className="w-2.5 h-2.5 rounded-full bg-teal-500"></span>
            <span>Cevaplanan</span>
          </div>
          <span className="font-mono font-bold text-slate-800 dark:text-slate-300">{answeredCount}</span>
        </div>
        <div className="flex items-center justify-between">
          <div className="flex items-center gap-1.5">
            <span className="w-2.5 h-2.5 rounded-full bg-slate-300 dark:bg-slate-700"></span>
            <span>Boş / Bekleyen</span>
          </div>
          <span className="font-mono font-bold text-slate-800 dark:text-slate-300">{total - answeredCount}</span>
        </div>
        {mode === 'simulation' && (
          <div className="flex items-center justify-between">
            <div className="flex items-center gap-1.5">
              <span className="w-2.5 h-2.5 rounded-full bg-amber-400"></span>
              <span>Gözden Geçirilecek</span>
            </div>
            <span className="font-mono font-bold text-amber-600 dark:text-amber-300">{flaggedCount}</span>
          </div>
        )}
      </div>
    </div>
  );
};
