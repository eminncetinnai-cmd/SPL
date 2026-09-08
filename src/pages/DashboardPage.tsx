import React from 'react';
import { 
  BarChart3, 
  Download, 
  TrendingUp, 
  CheckCircle2, 
  Award, 
  Clock, 
  Trash2, 
  Flame,
  Layers,
  ArrowRight
} from 'lucide-react';
import { useProgressStore } from '../stores/progressStore';
import { SubjectAccuracyChart } from '../components/dashboard/SubjectAccuracyChart';
import { PerformanceTrendChart } from '../components/dashboard/PerformanceTrendChart';
import { ReadinessGauge } from '../components/dashboard/ReadinessGauge';
import { exportQuizHistoryToCSV } from '../utils/csvExport';
import { formatDuration } from '../utils/spkScoring';

interface DashboardPageProps {
  onNavigate: (page: string, params?: any) => void;
}

export const DashboardPage: React.FC<DashboardPageProps> = ({ onNavigate }) => {
  const { history, moduleStats, clearHistory } = useProgressStore();

  const totalQuizzes = history.length;
  const totalQuestionsFromModules = Object.values(moduleStats).reduce((acc, m) => acc + m.totalQuestions, 0);
  const totalCorrectFromModules = Object.values(moduleStats).reduce((acc, m) => acc + m.totalCorrect, 0);

  const totalQuestionsSolved = Math.max(totalQuestionsFromModules, history.reduce((acc, h) => acc + h.total_questions, 0));
  const totalCorrect = Math.max(totalCorrectFromModules, history.reduce((acc, h) => acc + h.correct_count, 0));
  const overallAccuracy = totalQuestionsSolved > 0 ? Math.round((totalCorrect / totalQuestionsSolved) * 100) : null;
  const bestScore = history.length > 0 ? Math.max(...history.map((h) => h.score)) : Math.max(0, ...Object.values(moduleStats).map(m => m.bestScore));
  const passedQuizzes = history.filter((h) => h.overall_passed).length;

  return (
    <div className="max-w-6xl mx-auto space-y-8 animate-fade-in pb-16">
      {/* Top Header */}
      <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-4 border-b border-slate-200 dark:border-fintech-border/70 pb-5">
        <div>
          <span className="text-xs font-mono text-teal-600 dark:text-teal-400 font-bold uppercase tracking-wider block">
            Fintech Analitik & Performans
          </span>
          <h1 className="text-xl sm:text-2xl font-black text-slate-900 dark:text-white tracking-tight">
            Sınav Hazırlık İstatistikleri & Gelişim Grafikleri
          </h1>
        </div>

        <div className="flex items-center gap-3">
          {history.length > 0 && (
            <button
              onClick={() => exportQuizHistoryToCSV(history)}
              className="flex items-center gap-1.5 px-4 py-2 rounded-xl bg-white hover:bg-slate-50 dark:bg-fintech-card dark:hover:bg-fintech-cardHover text-slate-700 dark:text-slate-200 hover:text-slate-900 dark:hover:text-white text-xs font-bold border border-slate-200 dark:border-fintech-border shadow-sm transition-all"
            >
              <Download className="w-4 h-4 text-teal-600 dark:text-teal-400" />
              <span>Sınav Geçmişini CSV İndir</span>
            </button>
          )}

          <button
            onClick={() => onNavigate('simulation-prep')}
            className="flex items-center gap-2 px-5 py-2 rounded-xl bg-teal-500 hover:bg-teal-400 text-slate-950 font-black text-xs shadow-md shadow-teal-500/20 active:scale-95 transition-all"
          >
            <span>Yeni Deneme Başlat</span>
            <ArrowRight className="w-3.5 h-3.5" />
          </button>
        </div>
      </div>

      {/* KPI Cards Grid */}
      <div className="grid grid-cols-2 lg:grid-cols-4 gap-4">
        <div className="bg-white dark:bg-fintech-surface p-5 rounded-2xl border border-slate-200 dark:border-fintech-border space-y-2 shadow-sm">
          <div className="flex items-center justify-between text-slate-500 dark:text-slate-400 text-xs font-mono">
            <span>Çözülen Sınav</span>
            <Flame className="w-4 h-4 text-amber-500 dark:text-amber-400" />
          </div>
          <span className="text-2xl sm:text-3xl font-black font-mono text-slate-900 dark:text-white block">
            {totalQuizzes}
          </span>
          <span className="text-[11px] text-slate-500 dark:text-slate-400 block font-sans">
            {totalQuestionsSolved} Soru Çözüldü
          </span>
        </div>

        <div className="bg-white dark:bg-fintech-surface p-5 rounded-2xl border border-slate-200 dark:border-fintech-border space-y-2 shadow-sm">
          <div className="flex items-center justify-between text-slate-500 dark:text-slate-400 text-xs font-mono">
            <span>Genel Doğruluk</span>
            <CheckCircle2 className="w-4 h-4 text-teal-600 dark:text-teal-400" />
          </div>
          <span className={`text-2xl sm:text-3xl font-black font-mono block ${
            overallAccuracy !== null ? (overallAccuracy >= 60 ? 'text-emerald-600 dark:text-emerald-400' : 'text-amber-600 dark:text-amber-400') : 'text-slate-400'
          }`}>
            {overallAccuracy !== null ? `%${overallAccuracy}` : '-'}
          </span>
          <span className="text-[11px] text-slate-500 dark:text-slate-400 block font-sans">
            {overallAccuracy !== null ? `${totalCorrect} Doğru / ${totalQuestionsSolved - totalCorrect} Yanlış` : 'Henüz test çözülmedi'}
          </span>
        </div>

        <div className="bg-white dark:bg-fintech-surface p-5 rounded-2xl border border-slate-200 dark:border-fintech-border space-y-2 shadow-sm">
          <div className="flex items-center justify-between text-slate-500 dark:text-slate-400 text-xs font-mono">
            <span>En Yüksek Skor</span>
            <Award className="w-4 h-4 text-emerald-600 dark:text-emerald-400" />
          </div>
          <span className="text-2xl sm:text-3xl font-black font-mono text-emerald-600 dark:text-emerald-400 block">
            {bestScore} / 100
          </span>
          <span className="text-[11px] text-slate-500 dark:text-slate-400 block font-sans">
            SPK Barajı: 60 Puan
          </span>
        </div>

        <div className="bg-white dark:bg-fintech-surface p-5 rounded-2xl border border-slate-200 dark:border-fintech-border space-y-2 shadow-sm">
          <div className="flex items-center justify-between text-slate-500 dark:text-slate-400 text-xs font-mono">
            <span>Başarılı Sınavlar</span>
            <TrendingUp className="w-4 h-4 text-cyan-600 dark:text-cyan-400" />
          </div>
          <span className="text-2xl sm:text-3xl font-black font-mono text-cyan-600 dark:text-cyan-300 block">
            {passedQuizzes} / {totalQuizzes}
          </span>
          <span className="text-[11px] text-slate-500 dark:text-slate-400 block font-sans">
            Baraj Üstü Denemeler
          </span>
        </div>
      </div>

      {/* Analytics Charts */}
      <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
        <div className="lg:col-span-1">
          <ReadinessGauge />
        </div>
        <div className="lg:col-span-2">
          <SubjectAccuracyChart />
        </div>
      </div>

      <div>
        <PerformanceTrendChart />
      </div>

      {/* Past Quiz History Table */}
      <div className="bg-white dark:bg-fintech-surface rounded-2xl border border-slate-200 dark:border-fintech-border p-6 space-y-4 shadow-sm">
        <div className="flex items-center justify-between">
          <div>
            <h3 className="text-base font-bold text-slate-900 dark:text-white tracking-wide">
              Sınav Geçmişi Günlüğü
            </h3>
            <p className="text-xs text-slate-500 dark:text-slate-400">
              Çözülen tüm deneme sınavları ve modül testlerinin kronolojik kaydı.
            </p>
          </div>

          {history.length > 0 && (
            <button
              onClick={() => {
                if (confirm('Tüm sınav geçmişi silinsin mi? Bu işlem geri alınamaz.')) {
                  clearHistory();
                }
              }}
              className="text-xs text-rose-500 dark:text-rose-400 hover:text-rose-600 dark:hover:text-rose-300 transition-colors flex items-center gap-1"
            >
              <Trash2 className="w-3.5 h-3.5" />
              <span>Geçmişi Temizle</span>
            </button>
          )}
        </div>

        {history.length === 0 ? (
          <div className="p-8 text-center text-slate-400 text-xs font-mono">
            Henüz tamamlanmış bir sınav kaydı bulunmuyor.
          </div>
        ) : (
          <div className="overflow-x-auto">
            <table className="w-full text-left text-xs font-sans">
              <thead className="border-b border-slate-200 dark:border-fintech-border text-slate-500 dark:text-slate-400 font-mono uppercase text-[10px]">
                <tr>
                  <th className="py-3 px-3">Tarih</th>
                  <th className="py-3 px-3">Sınav Adı</th>
                  <th className="py-3 px-3 text-center">Soru</th>
                  <th className="py-3 px-3 text-center">D / Y / B</th>
                  <th className="py-3 px-3 text-center">Skor</th>
                  <th className="py-3 px-3 text-center">Başarı (%)</th>
                  <th className="py-3 px-3 text-center">Süre</th>
                  <th className="py-3 px-3 text-right">Durum</th>
                </tr>
              </thead>
              <tbody className="divide-y divide-slate-100 dark:divide-fintech-border/60 text-slate-700 dark:text-slate-300">
                {history.map((h) => (
                  <tr key={h.id} className="hover:bg-slate-50 dark:hover:bg-fintech-card/40 transition-colors">
                    <td className="py-3.5 px-3 font-mono text-slate-500 dark:text-slate-400">{h.date}</td>
                    <td className="py-3.5 px-3 font-semibold text-slate-900 dark:text-slate-200">{h.title}</td>
                    <td className="py-3.5 px-3 font-mono text-center">{h.total_questions}</td>
                    <td className="py-3.5 px-3 font-mono text-center text-slate-500 dark:text-slate-400">
                      <span className="text-emerald-600 dark:text-emerald-400 font-bold">{h.correct_count}D</span> /{' '}
                      <span className="text-rose-500 dark:text-rose-400">{h.wrong_count}Y</span> / {h.empty_count}B
                    </td>
                    <td className="py-3.5 px-3 font-mono text-center font-bold text-slate-900 dark:text-white text-sm">
                      {h.score}
                    </td>
                    <td className="py-3.5 px-3 font-mono text-center font-bold text-teal-600 dark:text-teal-400">
                      %{h.accuracy_pct}
                    </td>
                    <td className="py-3.5 px-3 font-mono text-center text-slate-500 dark:text-slate-400">
                      {formatDuration(h.duration_seconds)}
                    </td>
                    <td className="py-3.5 px-3 text-right">
                      <span
                        className={`font-mono text-[10px] font-bold px-2 py-0.5 rounded-full ${
                          h.overall_passed
                            ? 'bg-emerald-500/20 text-emerald-700 dark:text-emerald-300 border border-emerald-500/40'
                            : 'bg-rose-500/20 text-rose-700 dark:text-rose-300 border border-rose-500/40'
                        }`}
                      >
                        {h.overall_passed ? 'GEÇTİ' : 'KALDI'}
                      </span>
                    </td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        )}
      </div>
    </div>
  );
};
