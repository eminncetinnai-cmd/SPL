import React from 'react';
import { useProgressStore } from '../../stores/progressStore';
import { ShieldCheck, AlertCircle, Award, TrendingUp } from 'lucide-react';
import { ModuleId } from '../../types/exam';

export const ReadinessGauge: React.FC = () => {
  const { moduleStats, history } = useProgressStore();

  // Calculate readiness score
  const moduleIds: ModuleId[] = ['1001', '1003', '1005', '1012'];
  let attemptedModulesCount = 0;
  let totalAccuracySum = 0;

  moduleIds.forEach((id) => {
    const s = moduleStats[id];
    if (s.totalQuestions > 0) {
      attemptedModulesCount += 1;
      totalAccuracySum += s.averageAccuracy;
    }
  });

  const avgAttemptedAccuracy = attemptedModulesCount > 0 ? totalAccuracySum / attemptedModulesCount : 0;
  const coverageRatio = attemptedModulesCount / 4;
  const examReadinessScore = attemptedModulesCount > 0 
    ? Math.min(100, Math.round(avgAttemptedAccuracy * 0.6 + (coverageRatio * 100) * 0.4))
    : 0;

  let statusText = 'Henüz Test Çözülmedi (Sınava Başlayın)';
  let statusColor = 'text-slate-500 dark:text-slate-400';
  let badgeColor = 'bg-slate-100 border-slate-200 text-slate-700 dark:bg-slate-800 dark:border-slate-700 dark:text-slate-300';
  let strokeColor = '#E2E8F0';

  if (attemptedModulesCount === 0) {
    statusText = 'Henüz Test Çözülmedi (Sınava Başlayın)';
    statusColor = 'text-slate-500 dark:text-slate-400';
    badgeColor = 'bg-slate-100 border-slate-200 text-slate-700 dark:bg-slate-800 dark:border-slate-700 dark:text-slate-300';
    strokeColor = '#E2E8F0';
  } else if (examReadinessScore >= 75 && attemptedModulesCount === 4) {
    statusText = 'SINAVA HAZIR (Yüksek Başarı Beklentisi)';
    statusColor = 'text-emerald-700 dark:text-emerald-400 font-bold';
    badgeColor = 'bg-emerald-50 border-emerald-200 text-emerald-800 dark:bg-emerald-500/20 dark:border-emerald-500/40 dark:text-emerald-300';
    strokeColor = '#059669';
  } else if (examReadinessScore >= 55 && attemptedModulesCount >= 2) {
    statusText = 'GEÇME SEVİYESİNDE (Tekrar Önerilir)';
    statusColor = 'text-teal-700 dark:text-teal-400 font-bold';
    badgeColor = 'bg-teal-50 border-teal-200 text-teal-800 dark:bg-teal-500/20 dark:border-teal-500/40 dark:text-teal-300';
    strokeColor = '#0D9488';
  } else {
    statusText = 'GELİŞTİRİLMESİ GEREKİYOR';
    statusColor = 'text-amber-700 dark:text-amber-400 font-bold';
    badgeColor = 'bg-amber-50 border-amber-200 text-amber-800 dark:bg-amber-500/20 dark:border-amber-500/40 dark:text-amber-300';
    strokeColor = '#D97706';
  }

  // Circular gauge calculations
  const radius = 56;
  const circumference = 2 * Math.PI * radius;
  const strokeDashoffset = circumference - (examReadinessScore / 100) * circumference;

  return (
    <div className="w-full bg-white dark:bg-fintech-surface rounded-2xl border border-slate-200 dark:border-fintech-border p-5 flex flex-col justify-between space-y-4 shadow-sm">
      <div className="flex items-center justify-between">
        <h3 className="text-sm font-bold text-slate-900 dark:text-white tracking-wide">
          Sınav Hazırbulunuşluk Skoru
        </h3>
        <span className={`text-[11px] font-mono font-bold px-2.5 py-0.5 rounded-full border ${badgeColor}`}>
          {attemptedModulesCount}/4 Modül
        </span>
      </div>

      <div className="flex items-center gap-6 justify-around py-2">
        {/* Circular Progress Gauge */}
        <div className="relative w-32 h-32 flex items-center justify-center shrink-0">
          <svg className="w-full h-full transform -rotate-90" viewBox="0 0 130 130">
            <circle
              cx="65"
              cy="65"
              r={radius}
              stroke="#F1F5F9"
              strokeWidth="10"
              fill="transparent"
            />
            <circle
              cx="65"
              cy="65"
              r={radius}
              stroke={strokeColor}
              strokeWidth="10"
              strokeDasharray={circumference}
              strokeDashoffset={strokeDashoffset}
              strokeLinecap="round"
              fill="transparent"
              className="transition-all duration-1000 ease-out"
            />
          </svg>
          <div className="absolute inset-0 flex flex-col items-center justify-center">
            <span className="font-mono text-2xl font-black text-slate-900 dark:text-white">
              %{examReadinessScore}
            </span>
            <span className="text-[10px] uppercase font-bold text-slate-500 dark:text-slate-400">
              Hazırlık
            </span>
          </div>
        </div>

        {/* Status & Highlights */}
        <div className="space-y-2 text-left">
          <div className="space-y-0.5">
            <span className="text-[11px] uppercase tracking-wider text-slate-500 dark:text-slate-400 font-bold">
              Tahmini Durum:
            </span>
            <p className={`text-xs sm:text-sm font-bold leading-snug ${statusColor}`}>
              {statusText}
            </p>
          </div>

          <div className="text-xs text-slate-400 space-y-1 pt-1">
            <p className="flex items-center gap-1.5">
              <ShieldCheck className="w-3.5 h-3.5 text-teal-400" />
              <span>SPK Barajı: 60/100 Puan</span>
            </p>
            <p className="flex items-center gap-1.5">
              <TrendingUp className="w-3.5 h-3.5 text-emerald-400" />
              <span>Tamamlanan Test: {history.length} Adet</span>
            </p>
          </div>
        </div>
      </div>

      <div className="pt-2 border-t border-fintech-border/60 flex items-center justify-between text-xs text-slate-400">
        <span>Tüm derslerden min 50 & Ort. 60 gereklidir.</span>
      </div>
    </div>
  );
};
