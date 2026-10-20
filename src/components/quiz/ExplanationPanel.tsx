import React, { useRef, useEffect } from 'react';
import { 
  Lightbulb, 
  AlertTriangle, 
  CheckCircle2, 
  XCircle, 
  ArrowRight, 
  BookOpen, 
  Brain, 
  Scale, 
  FileText,
  HelpCircle,
  Sparkles
} from 'lucide-react';
import { Question } from '../../types/exam';

interface ExplanationPanelProps {
  question: Question;
  isCorrect: boolean;
  selectedOption: string | null;
  onScrolledToBottom?: () => void;
  onNextQuestion?: () => void;
  isLastQuestion?: boolean;
}

export const ExplanationPanel: React.FC<ExplanationPanelProps> = React.memo(({
  question,
  isCorrect,
  selectedOption,
  onScrolledToBottom,
  onNextQuestion,
  isLastQuestion = false,
}) => {
  const panelRef = useRef<HTMLDivElement>(null);

  // Auto scroll this panel into view smoothly when it appears
  useEffect(() => {
    if (panelRef.current) {
      panelRef.current.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
    }
  }, [question.id]);

  const handleScroll = () => {
    if (!panelRef.current || !onScrolledToBottom) return;
    const { scrollTop, scrollHeight, clientHeight } = panelRef.current;
    if (scrollTop + clientHeight >= scrollHeight - 20) {
      onScrolledToBottom();
    }
  };

  const correctOptionObj = question.options?.find((o) => o.key === question.correct_answer);

  // Maarif Cognitive Skill Metadata
  const cognitiveMeta = {
    KB3_Vaka: {
      badge: '🧠 Maarif Düzeyi: KB3 (Vaka / Senaryo Tabanlı Hukuki Teşhis)',
      subtitle: 'Gerçek hayattaki bir finansal vaka / eylem analiz edilerek ilgili sermaye piyasası normu ve hukuki sonucu teşhis edilmektedir.',
      bg: 'bg-indigo-50/80 dark:bg-indigo-950/30',
      border: 'border-indigo-200 dark:border-indigo-500/30',
      text: 'text-indigo-900 dark:text-indigo-300',
      icon: Brain
    },
    KB2_Muhakeme: {
      badge: '⚖️ Maarif Düzeyi: KB2 (Hukuki Muhakeme & Karşılaştırma)',
      subtitle: 'İki farklı kurum, tebliğ, kural veya istisna arasındaki ince hukuki ayrımlar ve kümülatif/seçimlik şartlar değerlendirilmektedir.',
      bg: 'bg-sky-50/80 dark:bg-sky-950/30',
      border: 'border-sky-200 dark:border-sky-500/30',
      text: 'text-sky-900 dark:text-sky-300',
      icon: Scale
    },
    KB1_Kavramsal: {
      badge: '📚 Maarif Düzeyi: KB1 (Kavramsal Bilgi & Temel Norm)',
      subtitle: 'Doğrudan kanuni tanım, süre, oran, asgari sermaye tutarı ve yetkili organ bilgisi ölçülmektedir.',
      bg: 'bg-emerald-50/80 dark:bg-emerald-950/30',
      border: 'border-emerald-200 dark:border-emerald-500/30',
      text: 'text-emerald-900 dark:text-emerald-300',
      icon: FileText
    }
  }[question.cognitive_skill || 'KB1_Kavramsal'];

  const CognitiveIcon = cognitiveMeta.icon;

  return (
    <div 
      ref={panelRef} 
      className="w-full bg-white dark:bg-fintech-surface rounded-3xl border border-slate-200 dark:border-fintech-border shadow-sm overflow-hidden animate-slide-up space-y-0"
    >
      {/* Header Banner */}
      <div
        className={`px-4 sm:px-6 py-3.5 sm:py-4 flex items-center justify-between border-b ${
          isCorrect
            ? 'bg-emerald-50 border-emerald-200 text-emerald-950 dark:bg-emerald-950/40 dark:border-emerald-500/30 dark:text-emerald-300'
            : 'bg-rose-50 border-rose-200 text-rose-950 dark:bg-rose-950/40 dark:border-rose-500/30 dark:text-rose-300'
        }`}
      >
        <div className="flex items-center gap-3">
          {isCorrect ? (
            <div className="p-2 rounded-xl bg-emerald-100 dark:bg-emerald-500/20 text-emerald-700 dark:text-emerald-400">
              <CheckCircle2 className="w-5 h-5" />
            </div>
          ) : (
            <div className="p-2 rounded-xl bg-rose-100 dark:bg-rose-500/20 text-rose-700 dark:text-rose-400">
              <XCircle className="w-5 h-5" />
            </div>
          )}
          <div className="space-y-1">
            <h4 className="font-extrabold text-sm sm:text-base">
              {isCorrect ? 'Tebrikler, Doğru Cevap!' : 'Hatalı Cevap!'}
            </h4>
            <div className="text-xs opacity-90 flex flex-wrap items-center gap-1.5 font-sans">
              <span>Doğru Seçenek:</span>
              <span className="font-black font-mono text-slate-900 dark:text-white px-2 py-0.5 rounded bg-white dark:bg-black/40 border border-slate-300 dark:border-white/20 shadow-xs">
                {question.correct_answer}
              </span>
              {selectedOption && selectedOption !== question.correct_answer && (
                <span className="text-rose-700 dark:text-rose-300 font-semibold font-mono">
                  (Sizin Seçiminiz: <span className="font-bold">{selectedOption}</span>)
                </span>
              )}
            </div>
            {correctOptionObj && (
              <div className="text-xs font-semibold text-emerald-900 dark:text-emerald-200 bg-emerald-100/90 dark:bg-emerald-900/50 px-2.5 py-1 rounded-lg border border-emerald-300/70 dark:border-emerald-700/50 mt-1 max-w-2xl">
                <span className="font-bold mr-1.5">{question.correct_answer}:</span>
                <span>{correctOptionObj.text}</span>
              </div>
            )}
          </div>
        </div>

        {/* Next Question Top Button for Instant Click */}
        {onNextQuestion && (
          <button
            onClick={onNextQuestion}
            className="min-h-[44px] flex items-center gap-1.5 px-4 py-2 rounded-xl bg-gradient-to-r from-teal-600 to-emerald-600 hover:from-teal-500 hover:to-emerald-500 text-white font-bold text-xs shadow-sm active:scale-95 transition-all cursor-pointer"
          >
            <span>{isLastQuestion ? 'Sonuçlar' : 'Sonraki'}</span>
            <ArrowRight className="w-4 h-4" />
          </button>
        )}
      </div>

      {/* Content Body */}
      <div
        onScroll={handleScroll}
        className="p-4 sm:p-6 space-y-4 sm:space-y-5 text-slate-800 dark:text-slate-200 text-sm sm:text-base leading-relaxed"
      >
        {/* Solution & Glossary Section */}
        {question.explanation && (() => {
          const parts = question.explanation.split('📌 Soruda Geçen Kısaltmalar & Terimler:');
          const mainExplanation = parts[0].trim();
          const abbreviations = parts[1] ? parts[1].trim() : null;

          return (
            <div className="space-y-4">
              <div className="space-y-2">
                <div className="flex items-center justify-between gap-2 flex-wrap">
                  <div className="flex items-center gap-2 text-teal-700 dark:text-teal-400 font-bold text-xs tracking-wider uppercase font-mono">
                    <Lightbulb className="w-4 h-4 text-amber-500" />
                    <span>Formatif Çözüm & Kanuni Gerekçe</span>
                  </div>
                  <span className={`inline-flex items-center gap-1.5 px-2.5 py-0.5 rounded-lg border text-[11px] font-mono font-bold ${cognitiveMeta.bg} ${cognitiveMeta.border} ${cognitiveMeta.text}`}>
                    <CognitiveIcon className="w-3.5 h-3.5" />
                    <span>{question.cognitive_skill === 'KB3_Vaka' ? 'Vaka Sorusu' : question.cognitive_skill === 'KB2_Muhakeme' ? 'Öncüllü Muhakeme' : 'Kavramsal Norm'}</span>
                  </span>
                </div>
                <div className="bg-slate-50 dark:bg-fintech-card/80 p-4 sm:p-5 rounded-2xl border border-slate-200 dark:border-fintech-border/80 text-slate-800 dark:text-slate-200 text-sm whitespace-pre-line leading-relaxed">
                  {mainExplanation}
                </div>
              </div>

              {abbreviations && (
                <div className="space-y-2">
                  <div className="flex items-center gap-2 text-cyan-700 dark:text-cyan-400 font-bold text-xs tracking-wider uppercase font-mono">
                    <BookOpen className="w-4 h-4 text-cyan-600 dark:text-cyan-400" />
                    <span>Soruda Geçen Kısaltmalar ve Açılımları</span>
                  </div>
                  <div className="bg-cyan-50/70 dark:bg-cyan-950/20 p-4 rounded-2xl border border-cyan-200 dark:border-cyan-500/30 text-cyan-950 dark:text-cyan-100 text-xs sm:text-sm space-y-2 leading-relaxed">
                    {abbreviations.split('\n').filter(Boolean).map((line, idx) => {
                      const cleanLine = line.replace(/^[•\-\*]\s*/, '').trim();
                      const colonIdx = cleanLine.indexOf(':');
                      if (colonIdx === -1) return null;
                      const abbr = cleanLine.substring(0, colonIdx).trim();
                      const desc = cleanLine.substring(colonIdx + 1).trim();
                      return (
                        <div key={idx} className="flex items-start gap-2.5">
                          <span className="font-mono font-bold text-cyan-900 dark:text-cyan-300 shrink-0 bg-cyan-100 dark:bg-cyan-500/20 px-2 py-0.5 rounded border border-cyan-300 dark:border-cyan-500/40 text-[11px]">
                            {abbr}
                          </span>
                          <span className="text-slate-700 dark:text-slate-300 text-xs sm:text-sm">
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

        {/* Exam Trap Section (if available) */}
        {question.trap && (
          <div className="space-y-2 pt-1">
            <div className="flex items-center gap-2 text-amber-700 dark:text-amber-400 font-bold text-xs tracking-wider uppercase font-mono">
              <AlertTriangle className="w-4 h-4 text-amber-500" />
              <span>Sınavda Çeldirici & Tuzak Noktası (Komisyon Hilesi)</span>
            </div>
            <div className="bg-amber-50/70 dark:bg-amber-950/20 p-4 rounded-2xl border border-amber-200 dark:border-amber-500/30 text-amber-950 dark:text-amber-200/90 text-sm leading-relaxed">
              {question.trap}
            </div>
          </div>
        )}

        {/* Chapter Context & Bottom Action Button */}
        <div className="pt-4 border-t border-slate-200 dark:border-fintech-border/60 flex flex-col sm:flex-row items-center justify-between gap-4">
          <div className="text-xs text-slate-500 dark:text-slate-400 truncate max-w-sm">
            {question.chapter && (
              <span>Bölüm: <strong className="text-slate-700 dark:text-slate-300 font-medium">{question.chapter}</strong></span>
            )}
          </div>

          {onNextQuestion && (
            <button
              onClick={onNextQuestion}
              className="w-full sm:w-auto min-h-[48px] flex items-center justify-center gap-2.5 px-6 py-3.5 rounded-2xl font-black text-xs shadow-md bg-gradient-to-r from-teal-600 to-emerald-600 hover:from-teal-500 hover:to-emerald-500 text-white active:scale-95 transition-all cursor-pointer"
            >
              <span>{isLastQuestion ? 'Testi Tamamla & Bilişsel Karneni Gör' : 'Sonraki Soruya Geç (Enter / →)'}</span>
              <ArrowRight className="w-4 h-4" />
            </button>
          )}
        </div>
      </div>
    </div>
  );
});
