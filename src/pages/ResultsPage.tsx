import React, { useEffect, useState } from 'react';
import confetti from 'canvas-confetti';
import { 
  Award, 
  CheckCircle2, 
  XCircle, 
  AlertTriangle, 
  Clock, 
  RotateCcw, 
  Home, 
  Download, 
  BookOpen, 
  Filter, 
  ChevronDown, 
  ChevronUp, 
  Star,
  Sparkles,
  HelpCircle
} from 'lucide-react';
import { useQuizStore } from '../stores/quizStore';
import { useProgressStore } from '../stores/progressStore';
import { exportQuizHistoryToCSV } from '../utils/csvExport';
import { formatDuration } from '../utils/spkScoring';
import { ModuleId, Question } from '../types/exam';
import modulesData from '../data/modules.json';

interface ResultsPageProps {
  onNavigate: (page: string, params?: any) => void;
}

export const ResultsPage: React.FC<ResultsPageProps> = ({ onNavigate }) => {
  const { currentSession, startQuiz } = useQuizStore();
  const { history, toggleBookmark, isBookmarked } = useProgressStore();

  const [filterType, setFilterType] = useState<'all' | 'wrong' | 'correct' | 'empty'>('all');
  const [expandedQuestions, setExpandedQuestions] = useState<Record<string, boolean>>({});

  useEffect(() => {
    if (currentSession?.overall_passed) {
      confetti({
        particleCount: 100,
        spread: 70,
        origin: { y: 0.6 },
        colors: ['#14B8A6', '#10B981', '#F59E0B', '#38BDF8'],
      });
    }
  }, [currentSession]);

  if (!currentSession) {
    return (
      <div className="max-w-md mx-auto text-center py-16 space-y-4">
        <h2 className="text-lg font-bold text-white">Görüntülenecek Sınav Sonucu Bulunamadı</h2>
        <button
          onClick={() => onNavigate('home')}
          className="px-6 py-2.5 rounded-xl bg-teal-500 text-slate-950 font-bold text-xs"
        >
          Ana Sayfaya Dön
        </button>
      </div>
    );
  }

  const {
    score = 0,
    accuracy_pct = 0,
    correct_count = 0,
    wrong_count = 0,
    empty_count = 0,
    duration_seconds = 0,
    questions = [],
    user_answers = {},
    module_breakdown = {},
    overall_passed = false,
  } = currentSession;

  const toggleExpand = (qId: string) => {
    setExpandedQuestions((prev) => ({ ...prev, [qId]: !prev[qId] }));
  };

  const filteredQuestions = questions.filter((q) => {
    const ans = user_answers[q.id];
    if (filterType === 'correct') return ans && ans.is_correct;
    if (filterType === 'wrong') return ans && ans.selected_option !== null && !ans.is_correct;
    if (filterType === 'empty') return !ans || ans.selected_option === null;
    return true;
  });

  const handleRetakeMistakes = () => {
    const wrongQuestions = questions.filter((q) => {
      const ans = user_answers[q.id];
      return ans && ans.selected_option !== null && !ans.is_correct;
    });

    if (wrongQuestions.length === 0) return;

    startQuiz({
      mode: 'practice',
      customQuestions: wrongQuestions,
      title: 'Hatalı Soruların Tekrarı',
    });
    onNavigate('practice');
  };

  const handleRetakeFull = () => {
    startQuiz({
      mode: currentSession.mode,
      moduleId: currentSession.module_id,
      customQuestions: currentSession.questions,
      title: currentSession.title,
    });
    onNavigate(currentSession.mode === 'simulation' ? 'simulation' : 'practice');
  };

  return (
    <div className="max-w-5xl mx-auto space-y-8 animate-fade-in pb-16">
      {/* Top Header Card */}
      <div className="bg-white dark:bg-fintech-surface rounded-3xl border border-slate-200 dark:border-fintech-border p-6 sm:p-8 space-y-6 shadow-sm dark:shadow-2xl relative overflow-hidden">
        {overall_passed && (
          <div className="absolute top-0 right-0 -mt-10 -mr-10 w-48 h-48 bg-emerald-500/10 rounded-full blur-2xl"></div>
        )}

        <div className="flex flex-col sm:flex-row items-start sm:items-center justify-between gap-4 border-b border-slate-100 dark:border-fintech-border/70 pb-6">
          <div>
            <span className="text-xs font-mono text-teal-600 dark:text-teal-400 font-bold uppercase tracking-wider block">
              Sınav Tamamlandı Raporu
            </span>
            <h1 className="text-xl sm:text-2xl font-black text-slate-900 dark:text-white tracking-tight">
              {currentSession.title}
            </h1>
          </div>

          <div className="flex items-center gap-3">
            <button
              onClick={() => exportQuizHistoryToCSV(history)}
              className="flex items-center gap-1.5 px-3.5 py-2 rounded-xl bg-slate-50 hover:bg-slate-100 dark:bg-fintech-card dark:hover:bg-fintech-cardHover text-slate-700 dark:text-slate-300 text-xs font-semibold border border-slate-200 dark:border-fintech-border shadow-sm transition-colors"
            >
              <Download className="w-4 h-4 text-teal-600 dark:text-teal-400" />
              <span>CSV İndir</span>
            </button>
            <button
              onClick={() => onNavigate('home')}
              className="flex items-center gap-1.5 px-4 py-2 rounded-xl bg-slate-100 hover:bg-slate-200 dark:bg-fintech-card dark:hover:bg-fintech-cardHover text-slate-900 dark:text-white text-xs font-semibold border border-slate-200 dark:border-fintech-border shadow-sm transition-colors"
            >
              <Home className="w-4 h-4" />
              <span>Ana Sayfa</span>
            </button>
          </div>
        </div>

        {/* Score & KPI Strip */}
        <div className="grid grid-cols-2 sm:grid-cols-5 gap-4">
          <div className="col-span-2 sm:col-span-1 bg-slate-50 dark:bg-fintech-card p-4 rounded-2xl border border-slate-200 dark:border-fintech-border text-center space-y-1 shadow-sm">
            <span className="text-[11px] font-mono text-slate-500 dark:text-slate-400 uppercase block font-semibold">SPK Puanı</span>
            <span className={`text-3xl font-black font-mono ${overall_passed ? 'text-emerald-600 dark:text-emerald-400' : 'text-amber-600 dark:text-amber-400'}`}>
              {score}
            </span>
            <span className="text-[10px] text-slate-500 block">/ 100 Puan</span>
          </div>

          <div className="bg-slate-50 dark:bg-fintech-card p-4 rounded-2xl border border-slate-200 dark:border-fintech-border text-center space-y-1 shadow-sm">
            <span className="text-[11px] font-mono text-slate-500 dark:text-slate-400 uppercase block font-semibold">Başarı Oranı</span>
            <span className="text-2xl font-bold font-mono text-teal-600 dark:text-teal-400">%{accuracy_pct}</span>
            <span className="text-[10px] text-slate-500 block">{correct_count}/{questions.length} Doğru</span>
          </div>

          <div className="bg-slate-50 dark:bg-fintech-card p-4 rounded-2xl border border-slate-200 dark:border-fintech-border text-center space-y-1 shadow-sm">
            <span className="text-[11px] font-mono text-slate-500 dark:text-slate-400 uppercase block font-semibold">Yanlış / Boş</span>
            <div className="flex items-center justify-center gap-2 text-base font-bold font-mono">
              <span className="text-rose-600 dark:text-rose-400">{wrong_count} Y</span>
              <span className="text-slate-400 dark:text-slate-500">•</span>
              <span className="text-slate-600 dark:text-slate-400">{empty_count} B</span>
            </div>
            <span className="text-[10px] text-slate-500 block">Net Düşmez</span>
          </div>

          <div className="bg-slate-50 dark:bg-fintech-card p-4 rounded-2xl border border-slate-200 dark:border-fintech-border text-center space-y-1 shadow-sm">
            <span className="text-[11px] font-mono text-slate-500 dark:text-slate-400 uppercase block font-semibold">Harcanan Süre</span>
            <span className="text-base font-bold font-mono text-slate-800 dark:text-slate-200">
              {formatDuration(duration_seconds)}
            </span>
            <span className="text-[10px] text-slate-500 block">Toplam Süre</span>
          </div>

          <div className="col-span-2 sm:col-span-1 bg-slate-50 dark:bg-fintech-card p-4 rounded-2xl border border-slate-200 dark:border-fintech-border text-center space-y-1 flex flex-col justify-center shadow-sm">
            <span className="text-[11px] font-mono text-slate-500 dark:text-slate-400 uppercase block font-semibold">SPK Durum</span>
            <span
              className={`text-sm font-black font-mono px-2 py-1 rounded-lg inline-block ${
                overall_passed
                  ? 'bg-emerald-100 dark:bg-emerald-500/20 text-emerald-800 dark:text-emerald-300 border border-emerald-300 dark:border-emerald-500/40'
                  : 'bg-rose-100 dark:bg-rose-500/20 text-rose-800 dark:text-rose-300 border border-rose-300 dark:border-rose-500/40'
              }`}
            >
              {overall_passed ? 'BARAJI GEÇTİ ✓' : 'BARAJ ALTI ✗'}
            </span>
          </div>
        </div>

        {/* Status Alert Banner */}
        <div
          className={`p-4 sm:p-5 rounded-2xl border flex items-start gap-3.5 shadow-sm ${
            overall_passed
              ? 'bg-emerald-50 dark:bg-emerald-950/30 border-emerald-200 dark:border-emerald-500/40 text-emerald-900 dark:text-emerald-200'
              : 'bg-rose-50 dark:bg-rose-950/30 border-rose-200 dark:border-rose-500/40 text-rose-900 dark:text-rose-200'
          }`}
        >
          {overall_passed ? (
            <Award className="w-6 h-6 text-emerald-600 dark:text-emerald-400 shrink-0 mt-0.5" />
          ) : (
            <AlertTriangle className="w-6 h-6 text-rose-600 dark:text-rose-400 shrink-0 mt-0.5" />
          )}
          <div className="space-y-1 text-xs sm:text-sm">
            <h4 className="font-black">
              {overall_passed
                ? 'Tebrikler! Sınav Başarı Kriterlerini Sağladınız.'
                : 'Sınav Başarı Kriterleri Sağlanamadı.'}
            </h4>
            <p className="opacity-95 leading-relaxed">
              SPK Düzey 1 lisansı için <strong>her dersten en az 50 puan</strong> ve <strong>tüm derslerin genel ortalamasında en az 60 puan</strong> alınması şarttır.
            </p>
          </div>
        </div>

        {/* Module Breakdown (if multiple modules) */}
        {Object.keys(module_breakdown).length > 0 && (
          <div className="space-y-3 pt-2">
            <h3 className="text-xs font-mono font-bold uppercase tracking-wider text-slate-700 dark:text-slate-300">
              Ders / Modül Bazlı Sonuç Karnesi
            </h3>
            <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-3">
              {(Object.keys(module_breakdown) as ModuleId[]).map((modId) => {
                const bd = (module_breakdown as any)[modId];
                if (!bd) return null;
                const passed = bd.score >= 50;

                return (
                  <div
                    key={modId}
                    className={`p-4 rounded-xl border space-y-2 bg-slate-50 dark:bg-fintech-card/60 shadow-sm ${
                      passed ? 'border-emerald-300 dark:border-emerald-500/40' : 'border-rose-300 dark:border-rose-500/40'
                    }`}
                  >
                    <div className="flex items-center justify-between">
                      <span className="font-mono text-xs font-bold text-slate-800 dark:text-slate-300">
                        Modül {modId}
                      </span>
                      <span
                        className={`text-[10px] font-mono font-bold px-2 py-0.5 rounded ${
                          passed
                            ? 'bg-emerald-100 dark:bg-emerald-500/20 text-emerald-800 dark:text-emerald-300'
                            : 'bg-rose-100 dark:bg-rose-500/20 text-rose-800 dark:text-rose-300'
                        }`}
                      >
                        {passed ? 'GEÇTİ (≥50)' : 'KALDI (<50)'}
                      </span>
                    </div>

                    <div className="flex items-baseline justify-between">
                      <span className="text-lg font-black font-mono text-slate-900 dark:text-white">
                        {bd.score} Puan
                      </span>
                      <span className="text-xs font-mono text-slate-500 dark:text-slate-400">
                        {bd.correct}D / {bd.wrong}Y
                      </span>
                    </div>
                  </div>
                );
              })}
            </div>
          </div>
        )}

        {/* Action Buttons */}
        <div className="flex flex-wrap items-center gap-3 pt-3 border-t border-slate-100 dark:border-fintech-border/70">
          {wrong_count > 0 && (
            <button
              onClick={handleRetakeMistakes}
              className="flex items-center gap-2 px-5 py-3 rounded-xl bg-gradient-to-r from-rose-500 to-amber-500 hover:from-rose-400 hover:to-amber-400 text-slate-950 font-black text-xs shadow-md shadow-rose-500/20 active:scale-95 transition-all"
            >
              <RotateCcw className="w-4 h-4" />
              <span>Yanlış Yapılan {wrong_count} Soruyu Tekrar Çöz</span>
            </button>
          )}

          <button
            onClick={handleRetakeFull}
            className="flex items-center gap-2 px-5 py-3 rounded-xl bg-teal-500 hover:bg-teal-400 text-slate-950 font-bold text-xs shadow-md shadow-teal-500/20 active:scale-95 transition-all"
          >
            <RotateCcw className="w-4 h-4" />
            <span>Tüm Sınavı Yeniden Başlat</span>
          </button>
        </div>
      </div>

      {/* Comprehensive Question Review Section */}
      <div className="space-y-5">
        <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-4">
          <div>
            <h2 className="text-lg font-black text-slate-900 dark:text-white tracking-tight">
              Soru İnceleme ve Analitik Çözümler
            </h2>
            <p className="text-xs text-slate-600 dark:text-slate-400">
              Her sorunun doğru cevabını, seçiminizi ve sınav tuzaklarını inceleyin.
            </p>
          </div>

          {/* Filter Tabs */}
          <div className="flex items-center gap-1.5 p-1 rounded-xl bg-slate-100 dark:bg-fintech-surface border border-slate-200 dark:border-fintech-border text-xs">
            <button
              onClick={() => setFilterType('all')}
              className={`px-3 py-1.5 rounded-lg font-bold transition-all ${
                filterType === 'all'
                  ? 'bg-teal-500 text-slate-950 shadow-sm'
                  : 'text-slate-600 dark:text-slate-400 hover:text-slate-900 dark:hover:text-white'
              }`}
            >
              Tümü ({questions.length})
            </button>
            <button
              onClick={() => setFilterType('wrong')}
              className={`px-3 py-1.5 rounded-lg font-bold transition-all ${
                filterType === 'wrong'
                  ? 'bg-rose-500 text-white shadow-sm'
                  : 'text-slate-600 dark:text-slate-400 hover:text-slate-900 dark:hover:text-white'
              }`}
            >
              Yanlışlar ({wrong_count})
            </button>
            <button
              onClick={() => setFilterType('correct')}
              className={`px-3 py-1.5 rounded-lg font-bold transition-all ${
                filterType === 'correct'
                  ? 'bg-emerald-500 text-slate-950 shadow-sm'
                  : 'text-slate-600 dark:text-slate-400 hover:text-slate-900 dark:hover:text-white'
              }`}
            >
              Doğrular ({correct_count})
            </button>
            {empty_count > 0 && (
              <button
                onClick={() => setFilterType('empty')}
                className={`px-3 py-1.5 rounded-lg font-bold transition-all ${
                  filterType === 'empty'
                    ? 'bg-slate-700 text-white shadow-sm'
                    : 'text-slate-600 dark:text-slate-400 hover:text-slate-900 dark:hover:text-white'
                }`}
              >
                Boşlar ({empty_count})
              </button>
            )}
          </div>
        </div>

        {/* Questions Accordion List */}
        <div className="space-y-4">
          {filteredQuestions.map((q, idx) => {
            const ans = user_answers[q.id];
            const isCorrect = ans?.is_correct;
            const isAnswered = ans && ans.selected_option !== null;
            const isExpanded = expandedQuestions[q.id] !== false; // expanded by default or toggled
            const bookmarked = isBookmarked(q.id);

            return (
              <div
                key={q.id}
                className="bg-white dark:bg-fintech-surface rounded-2xl border border-slate-200 dark:border-fintech-border shadow-sm overflow-hidden transition-all"
              >
                {/* Header Row */}
                <div
                  onClick={() => toggleExpand(q.id)}
                  className="p-4 sm:p-5 flex items-center justify-between gap-3 cursor-pointer hover:bg-slate-50 dark:hover:bg-fintech-card/40 transition-colors"
                >
                  <div className="flex items-center gap-3 flex-1 min-w-0">
                    <div className="shrink-0">
                      {isCorrect ? (
                        <CheckCircle2 className="w-5 h-5 text-emerald-600 dark:text-emerald-400" />
                      ) : isAnswered ? (
                        <XCircle className="w-5 h-5 text-rose-600 dark:text-rose-400" />
                      ) : (
                        <HelpCircle className="w-5 h-5 text-slate-400 dark:text-slate-500" />
                      )}
                    </div>

                    <div className="min-w-0 flex-1">
                      <div className="flex items-center gap-2 flex-wrap text-xs">
                        <span className="font-mono font-bold text-slate-800 dark:text-slate-300">
                          Soru {idx + 1}
                        </span>
                        <span className="font-mono px-2 py-0.5 rounded bg-slate-100 dark:bg-slate-800 text-slate-600 dark:text-slate-400 border border-slate-200 dark:border-slate-700">
                          Modül {q.module_id}
                        </span>
                        {q.topic && (
                          <span className="text-slate-500 dark:text-slate-400 truncate max-w-xs hidden sm:inline">
                            {q.topic}
                          </span>
                        )}
                      </div>
                      <p className="text-sm font-semibold text-slate-900 dark:text-slate-200 truncate mt-1">
                        {q.text}
                      </p>
                    </div>
                  </div>

                  <div className="flex items-center gap-3 shrink-0">
                    <button
                      onClick={(e) => {
                        e.stopPropagation();
                        toggleBookmark(q.id);
                      }}
                      className={`p-1.5 rounded-lg border ${
                        bookmarked
                          ? 'bg-amber-100 dark:bg-amber-500/20 text-amber-600 dark:text-amber-400 border-amber-300 dark:border-amber-500/40'
                          : 'bg-slate-100 dark:bg-slate-800 text-slate-400 hover:text-amber-500 border-slate-200 dark:border-slate-700'
                      }`}
                    >
                      <Star className={`w-4 h-4 ${bookmarked ? 'fill-amber-500 text-amber-500 dark:fill-amber-400 dark:text-amber-400' : ''}`} />
                    </button>

                    {isExpanded ? (
                      <ChevronUp className="w-5 h-5 text-slate-400" />
                    ) : (
                      <ChevronDown className="w-5 h-5 text-slate-400" />
                    )}
                  </div>
                </div>

                {/* Expanded Details */}
                {isExpanded && (
                  <div className="px-5 pb-6 pt-2 border-t border-slate-100 dark:border-fintech-border/60 space-y-4">
                    <p className="text-sm text-slate-900 dark:text-slate-100 whitespace-pre-line leading-relaxed">
                      {q.text}
                    </p>

                    {/* Options list with indicators */}
                    <div className="grid grid-cols-1 gap-2 pt-1">
                      {q.options.map((opt) => {
                        const isCorrectOpt = opt.key === q.correct_answer;
                        const isUserOpt = ans?.selected_option === opt.key;

                        let style = 'bg-slate-50 dark:bg-fintech-card/50 border-slate-200 dark:border-fintech-border text-slate-700 dark:text-slate-300';
                        if (isCorrectOpt) {
                          style = 'bg-emerald-50 dark:bg-emerald-950/40 border-emerald-300 dark:border-emerald-500 text-emerald-900 dark:text-emerald-200 font-medium';
                        } else if (isUserOpt && !isCorrectOpt) {
                          style = 'bg-rose-50 dark:bg-rose-950/40 border-rose-300 dark:border-rose-500 text-rose-900 dark:text-rose-200';
                        }

                        return (
                          <div
                            key={opt.key}
                            className={`p-3 rounded-xl border text-xs sm:text-sm flex items-start gap-3 ${style}`}
                          >
                            <span className="font-mono font-bold w-5 shrink-0">{opt.key})</span>
                            <span className="flex-1">{opt.text}</span>
                            {isCorrectOpt && (
                              <span className="text-[11px] font-mono text-emerald-700 dark:text-emerald-400 font-bold shrink-0">
                                Doğru Cevap ✓
                              </span>
                            )}
                            {isUserOpt && !isCorrectOpt && (
                              <span className="text-[11px] font-mono text-rose-700 dark:text-rose-400 font-bold shrink-0">
                                Sizin Seçiminiz ✗
                              </span>
                            )}
                          </div>
                        );
                      })}
                    </div>

                    {/* Explanation Box & Glossary */}
                    {q.explanation && (() => {
                      const parts = q.explanation.split('📌 Soruda Geçen Kısaltmalar & Terimler:');
                      const mainExplanation = parts[0].trim();
                      const abbreviations = parts[1] ? parts[1].trim() : null;

                      return (
                        <div className="space-y-3">
                          <div className="bg-slate-50 dark:bg-fintech-card/80 p-4 rounded-xl border border-slate-200 dark:border-fintech-border space-y-1.5 text-xs text-slate-700 dark:text-slate-300">
                            <span className="font-bold text-teal-700 dark:text-teal-400 uppercase tracking-wider block">
                              💡 Analitik Çözüm & Sınav İpucu:
                            </span>
                            <p className="whitespace-pre-line leading-relaxed">{mainExplanation}</p>
                          </div>

                          {abbreviations && (
                            <div className="bg-cyan-50 dark:bg-cyan-950/20 p-3.5 rounded-xl border border-cyan-200 dark:border-cyan-500/30 text-xs space-y-2">
                              <span className="font-bold text-cyan-800 dark:text-cyan-300 uppercase tracking-wider block font-mono text-[10px]">
                                📌 Soruda Geçen Kısaltmalar ve Açılımları:
                              </span>
                              <div className="space-y-1.5">
                                {abbreviations.split('\n').filter(Boolean).map((line, aIdx) => {
                                  const cleanLine = line.replace(/^[•\-\*]\s*/, '').trim();
                                  const colonIdx = cleanLine.indexOf(':');
                                  if (colonIdx === -1) return null;
                                  const abbr = cleanLine.substring(0, colonIdx).trim();
                                  const desc = cleanLine.substring(colonIdx + 1).trim();
                                  return (
                                    <div key={aIdx} className="flex items-start gap-2">
                                      <span className="font-mono font-bold text-cyan-800 dark:text-cyan-300 shrink-0 bg-cyan-100 dark:bg-cyan-500/20 px-1.5 py-0.5 rounded border border-cyan-200 dark:border-cyan-500/40 text-[10px]">
                                        {abbr}
                                      </span>
                                      <span className="text-slate-700 dark:text-slate-300 text-xs">
                                        {desc}
                                      </span>
                                    </div>
                                  );
                                })}
                              </div>
                            </div>
                          )}
                        </div>
                      );
                    })()}

                    {/* Exam Trap Box */}
                    {q.trap && (
                      <div className="bg-amber-50 dark:bg-amber-950/30 p-3.5 rounded-xl border border-amber-200 dark:border-amber-500/40 text-xs text-amber-900 dark:text-amber-200/90 leading-relaxed">
                        <strong className="text-amber-700 dark:text-amber-400 block font-mono uppercase mb-1">
                          ⚠️ Sınav Tuzağı:
                        </strong>
                        {q.trap}
                      </div>
                    )}
                  </div>
                )}
              </div>
            );
          })}
        </div>
      </div>
    </div>
  );
};
