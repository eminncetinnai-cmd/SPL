import React from 'react';
import { ShieldCheck, AlertTriangle, CheckCircle, ArrowRight, TrendingUp, Sparkles, AlertCircle } from 'lucide-react';
import { useProgressStore } from '../../stores/progressStore';
import { calculateSpkDiagnostics } from '../../utils/spkDiagnostics';
import { ModuleId } from '../../types/exam';

interface SpkBarrierCardProps {
  onNavigate: (page: string, params?: any) => void;
}

export const SpkBarrierCard: React.FC<SpkBarrierCardProps> = ({ onNavigate }) => {
  const { moduleStats } = useProgressStore();
  const diag = calculateSpkDiagnostics(moduleStats);

  const getStatusBadge = () => {
    switch (diag.overallStatus) {
      case 'passed':
        return {
          bg: 'bg-emerald-500/10 text-emerald-800 dark:text-emerald-300 border-emerald-500/20',
          dot: 'bg-emerald-500',
          title: 'SPK LİSANSI KAZANMA DÜZEYİNDE',
          icon: ShieldCheck,
        };
      case 'failed_module':
        return {
          bg: 'bg-rose-500/10 text-rose-800 dark:text-rose-300 border-rose-500/20',
          dot: 'bg-rose-500',
          title: 'RİSKLİ: MODÜL BARAJI ALTINDA',
          icon: AlertTriangle,
        };
      case 'failed_average':
        return {
          bg: 'bg-amber-500/10 text-amber-800 dark:text-amber-300 border-amber-500/20',
          dot: 'bg-amber-500',
          title: 'DİKKAT: ORTALAMA BARAJI (60) EKSİK',
          icon: TrendingUp,
        };
      default:
        return {
          bg: 'bg-teal-500/10 text-teal-800 dark:text-teal-300 border-teal-500/20',
          dot: 'bg-teal-500',
          title: 'TEŞHİS: VERİ TOPLANIYOR',
          icon: Sparkles,
        };
    }
  };

  const badge = getStatusBadge();
  const StatusIcon = badge.icon;

  return (
    <div className="bg-white dark:bg-fintech-surface rounded-2xl sm:rounded-3xl border border-slate-200 dark:border-fintech-border p-4 sm:p-5 shadow-xs space-y-4">
      {/* Header */}
      <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-3">
        <div className="flex items-center gap-3">
          <div className="p-2.5 rounded-2xl bg-teal-50 dark:bg-slate-800 text-teal-600 dark:text-teal-400">
            <StatusIcon className="w-5 h-5" />
          </div>
          <div>
            <div className="flex items-center gap-2">
              <span className={`px-2 py-0.5 rounded-full text-[10px] font-mono font-bold border flex items-center gap-1.5 ${badge.bg}`}>
                <span className={`w-1.5 h-1.5 rounded-full ${badge.dot}`} />
                {badge.title}
              </span>
              <span className="text-xs text-slate-500 dark:text-slate-400 font-mono">
                SPL Çift Baraj Kuralı
              </span>
            </div>
            <h3 className="text-base sm:text-lg font-black text-slate-900 dark:text-white mt-0.5">
              SPK Baraj Teşhisi & Risk Analizi
            </h3>
          </div>
        </div>

        {/* Global Average Display */}
        <div className="flex items-center gap-3 self-start sm:self-auto bg-slate-50 dark:bg-fintech-card px-3.5 py-2 rounded-xl border border-slate-200/80 dark:border-fintech-border">
          <div className="text-right">
            <span className="text-[10px] text-slate-500 dark:text-slate-400 font-medium block">
              Genel Not Ortalamanız
            </span>
            <span className="text-xs font-mono text-slate-600 dark:text-slate-400">
              Baraj: ≥ 60
            </span>
          </div>
          <div className={`text-xl sm:text-2xl font-black font-mono ${
            diag.overallScore >= 60 
              ? 'text-emerald-800 dark:text-emerald-400' 
              : diag.overallScore >= 50 
              ? 'text-amber-800 dark:text-amber-400' 
              : 'text-rose-800 dark:text-rose-400'
          }`}>
            %{diag.overallScore}
          </div>
        </div>
      </div>

      {/* 4 Module Barrier Micro-Cards */}
      <div className="grid grid-cols-2 lg:grid-cols-4 gap-2.5">
        {Object.values(diag.moduleStatuses).map((m) => {
          const isPassed = m.status === 'passed' || m.status === 'warning';
          const isFailed = m.status === 'failed';
          const isUntested = m.status === 'untested';

          return (
            <div
              key={m.moduleId}
              className={`p-3 rounded-xl border flex flex-col justify-between transition-all ${
                isFailed
                  ? 'bg-rose-50/50 dark:bg-rose-950/20 border-rose-300 dark:border-rose-900/60'
                  : isPassed
                  ? 'bg-emerald-50/40 dark:bg-emerald-950/20 border-emerald-300 dark:border-emerald-900/60'
                  : 'bg-slate-50/60 dark:bg-fintech-card/60 border-slate-200 dark:border-fintech-border'
              }`}
            >
              <div className="space-y-1">
                <div className="flex items-center justify-between">
                  <span className="font-mono text-xs font-bold text-slate-700 dark:text-slate-300">
                    {m.code}
                  </span>
                  <span
                    className={`text-[10px] font-mono font-bold px-1.5 py-0.5 rounded ${
                      isFailed
                        ? 'bg-rose-100 text-rose-700 dark:bg-rose-500/20 dark:text-rose-400'
                        : isPassed
                        ? 'bg-emerald-100 text-emerald-700 dark:bg-emerald-500/20 dark:text-emerald-400'
                        : 'bg-slate-200/70 text-slate-600 dark:bg-slate-800 dark:text-slate-400'
                    }`}
                  >
                    {isUntested ? 'Veri Yok' : `%${m.score}`}
                  </span>
                </div>
                <h5 className="font-bold text-xs text-slate-900 dark:text-white truncate" title={m.shortName}>
                  {m.shortName}
                </h5>
              </div>

              <div className="mt-2 pt-2 border-t border-slate-200/60 dark:border-slate-800 text-[11px] font-mono">
                {isFailed ? (
                  <span className="text-rose-600 dark:text-rose-400 font-bold flex items-center gap-1">
                    <AlertCircle className="w-3 h-3 shrink-0" />
                    +{m.missingNetToPass} net gerek
                  </span>
                ) : isPassed ? (
                  <span className="text-emerald-600 dark:text-emerald-400 font-semibold flex items-center gap-1">
                    <CheckCircle className="w-3 h-3 shrink-0" />
                    Baraj Aşıldı (≥50)
                  </span>
                ) : (
                  <span className="text-slate-400">
                    {m.solvedQuestions}/25 çözüldü
                  </span>
                )}
              </div>
            </div>
          );
        })}
      </div>

      {/* Action Advice Banner */}
      <div className="p-3 rounded-xl bg-slate-50 dark:bg-fintech-card border border-slate-200/80 dark:border-fintech-border flex flex-col sm:flex-row sm:items-center justify-between gap-3 text-xs">
        <div className="flex items-start sm:items-center gap-2 text-slate-700 dark:text-slate-300">
          <span className="font-bold text-teal-600 dark:text-teal-400 shrink-0">🎯 Sınav Stratejisi:</span>
          <span>{diag.actionAdvice}</span>
        </div>

        {diag.weakestModule && diag.weakestModule.status === 'failed' && (
          <button
            onClick={() => onNavigate('practice', { moduleId: diag.weakestModule!.moduleId, filterMode: 'unseen' })}
            className="flex items-center justify-center gap-1.5 px-3.5 py-1.5 rounded-lg bg-rose-600 hover:bg-rose-700 text-white font-bold text-xs shrink-0 active:scale-95 transition-all cursor-pointer shadow-xs"
          >
            <span>{diag.weakestModule.code} Testini Çöz</span>
            <ArrowRight className="w-3.5 h-3.5" />
          </button>
        )}
      </div>
    </div>
  );
};
