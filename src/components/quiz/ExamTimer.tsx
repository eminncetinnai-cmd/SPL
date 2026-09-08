import React, { useEffect, useState } from 'react';
import { Timer, AlertCircle } from 'lucide-react';

interface ExamTimerProps {
  timeLimitSeconds?: number;
  onTimeUp?: () => void;
  onTick?: (seconds: number) => void;
  isPaused?: boolean;
}

export const ExamTimer: React.FC<ExamTimerProps> = ({
  timeLimitSeconds,
  onTimeUp,
  onTick,
  isPaused = false,
}) => {
  const isCountdown = typeof timeLimitSeconds === 'number' && timeLimitSeconds > 0;
  const [seconds, setSeconds] = useState(isCountdown ? timeLimitSeconds : 0);

  useEffect(() => {
    if (isPaused) return;

    const interval = setInterval(() => {
      setSeconds((prev) => {
        if (isCountdown) {
          if (prev <= 1) {
            clearInterval(interval);
            if (onTimeUp) onTimeUp();
            return 0;
          }
          const next = prev - 1;
          if (onTick) onTick(timeLimitSeconds - next);
          return next;
        } else {
          const next = prev + 1;
          if (onTick) onTick(next);
          return next;
        }
      });
    }, 1000);

    return () => clearInterval(interval);
  }, [isCountdown, timeLimitSeconds, isPaused, onTimeUp, onTick]);

  const formatTime = (totalSecs: number) => {
    const hours = Math.floor(totalSecs / 3600);
    const mins = Math.floor((totalSecs % 3600) / 60);
    const secs = totalSecs % 60;

    if (hours > 0) {
      return `${hours.toString().padStart(2, '0')}:${mins.toString().padStart(2, '0')}:${secs.toString().padStart(2, '0')}`;
    }
    return `${mins.toString().padStart(2, '0')}:${secs.toString().padStart(2, '0')}`;
  };

  const isLowTime = isCountdown && seconds < 300; // Under 5 mins

  return (
    <div
      className={`flex items-center gap-2 px-4 py-2 rounded-xl font-mono text-sm font-bold border transition-all ${
        isLowTime
          ? 'bg-rose-50 text-rose-700 border-rose-300 dark:bg-rose-500/20 dark:text-rose-300 dark:border-rose-500/50 animate-pulse'
          : 'bg-slate-50 text-teal-800 border-slate-200 dark:bg-fintech-card dark:text-teal-400 dark:border-fintech-border shadow-xs'
      }`}
    >
      <Timer className={`w-4 h-4 ${isLowTime ? 'text-rose-600 dark:text-rose-400' : 'text-teal-600 dark:text-teal-400'}`} />
      <span>{formatTime(seconds)}</span>
      {isLowTime && (
        <span className="text-[11px] text-rose-600 dark:text-rose-400 font-sans font-normal hidden sm:inline">
          (Az Zaman Kaldı!)
        </span>
      )}
    </div>
  );
};
