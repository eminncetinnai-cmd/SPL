import React, { useState } from 'react';
import { 
  Star, 
  Play, 
  Search, 
  Trash2, 
  ChevronDown, 
  ChevronUp, 
  CheckCircle,
  Lightbulb
} from 'lucide-react';
import { useProgressStore } from '../stores/progressStore';
import { useQuizStore } from '../stores/quizStore';
import allQuestionsData from '../data/all_questions.json';
import { Question } from '../types/exam';

interface BookmarksPageProps {
  onNavigate: (page: string, params?: any) => void;
}

export const BookmarksPage: React.FC<BookmarksPageProps> = ({ onNavigate }) => {
  const { bookmarks, toggleBookmark } = useProgressStore();
  const { startQuiz } = useQuizStore();

  const [searchQuery, setSearchQuery] = useState('');
  const [expandedItems, setExpandedItems] = useState<Record<string, boolean>>({});

  const allQuestions = allQuestionsData as Question[];
  const bookmarkedQuestions = allQuestions.filter((q) => bookmarks.includes(q.id));

  const filtered = bookmarkedQuestions.filter((q) => {
    if (!searchQuery.trim()) return true;
    const query = searchQuery.toLowerCase();
    return (
      q.text.toLowerCase().includes(query) ||
      (q.topic || '').toLowerCase().includes(query) ||
      (q.explanation || '').toLowerCase().includes(query)
    );
  });

  const toggleExpand = (id: string) => {
    setExpandedItems((prev) => ({ ...prev, [id]: !prev[id] }));
  };

  const handleStartBookmarkQuiz = () => {
    if (filtered.length === 0) return;
    startQuiz({
      mode: 'bookmarks',
      customQuestions: filtered,
      title: `Yıldızlı Sorular Çalışma Testi (${filtered.length} Soru)`,
    });
    onNavigate('practice');
  };

  return (
    <div className="max-w-5xl mx-auto space-y-6 animate-fade-in pb-16">
      {/* Header Banner */}
      <div className="bg-white dark:bg-fintech-surface rounded-3xl border border-amber-500/30 p-6 sm:p-8 space-y-4 shadow-sm">
        <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-4">
          <div className="flex items-center gap-3.5">
            <div className="p-3 rounded-2xl bg-amber-500/20 text-amber-500 dark:text-amber-400">
              <Star className="w-6 h-6 fill-amber-500 dark:fill-amber-400" />
            </div>
            <div>
              <h1 className="text-xl sm:text-2xl font-black text-slate-900 dark:text-white tracking-tight">
                Yıldızlı / Favori Sorular
              </h1>
              <p className="text-xs sm:text-sm text-slate-600 dark:text-slate-400">
                Sınava hazırlık sürecinde önemli gördüğünüz ve yıldızladığınız kritik sorular.
              </p>
            </div>
          </div>

          {bookmarkedQuestions.length > 0 && (
            <button
              onClick={handleStartBookmarkQuiz}
              className="flex items-center gap-2 px-5 py-2.5 rounded-xl bg-gradient-to-r from-amber-500 to-teal-500 hover:from-amber-400 hover:to-teal-400 text-slate-950 font-black text-xs shadow-md shadow-amber-500/20 active:scale-95 transition-all"
            >
              <Play className="w-4 h-4 fill-slate-950" />
              <span>Yıldızlı Sorulardan Test Çöz ({filtered.length})</span>
            </button>
          )}
        </div>

        {/* Search */}
        <div className="relative pt-2">
          <Search className="absolute left-3.5 top-5 w-4 h-4 text-slate-400" />
          <input
            type="text"
            value={searchQuery}
            onChange={(e) => setSearchQuery(e.target.value)}
            placeholder="Yıldızlı sorular içinde ara..."
            className="w-full bg-slate-50 dark:bg-fintech-card border border-slate-200 dark:border-fintech-border rounded-xl pl-10 pr-4 py-2.5 text-xs text-slate-900 dark:text-slate-200 placeholder-slate-400 focus:outline-none focus:border-amber-500 transition-colors"
          />
        </div>
      </div>

      {/* Bookmarked Questions List */}
      {filtered.length === 0 ? (
        <div className="bg-white dark:bg-fintech-surface rounded-2xl border border-slate-200 dark:border-fintech-border p-12 text-center space-y-3 shadow-sm">
          <div className="w-12 h-12 rounded-full bg-amber-500/10 text-amber-500 dark:text-amber-400 flex items-center justify-center mx-auto">
            <Star className="w-6 h-6" />
          </div>
          <h3 className="text-base font-bold text-slate-900 dark:text-white">Yıldızlı Soru Bulunmuyor</h3>
          <p className="text-xs text-slate-600 dark:text-slate-400 max-w-sm mx-auto">
            Test çözerken veya soru bankasını incelerken soru kartlarının sağ üstündeki yıldız ikonuna tıklayarak buraya kaydedebilirsiniz.
          </p>
        </div>
      ) : (
        <div className="space-y-4">
          <div className="text-xs text-slate-500 dark:text-slate-400 px-2 font-mono">
            <span>{filtered.length} Yıldızlı Soru Listeleniyor</span>
          </div>

          {filtered.map((q, idx) => {
            const isExpanded = expandedItems[q.id] !== false;

            return (
              <div
                key={q.id}
                className="bg-white dark:bg-fintech-surface rounded-2xl border border-slate-200 dark:border-fintech-border shadow-sm overflow-hidden transition-all"
              >
                <div
                  onClick={() => toggleExpand(q.id)}
                  className="p-5 flex items-center justify-between gap-4 cursor-pointer hover:bg-slate-50 dark:hover:bg-fintech-card/40 transition-colors"
                >
                  <div className="flex items-center gap-3 flex-1 min-w-0">
                    <span className="w-7 h-7 rounded-lg bg-amber-500/20 text-amber-600 dark:text-amber-300 font-mono text-xs font-bold flex items-center justify-center shrink-0">
                      {idx + 1}
                    </span>

                    <div className="min-w-0 flex-1">
                      <div className="flex items-center gap-2 flex-wrap text-xs">
                        <span className="font-mono px-2 py-0.5 rounded bg-slate-100 dark:bg-slate-800 text-teal-700 dark:text-teal-400 border border-slate-200 dark:border-slate-700 font-bold">
                          Modül {q.module_id}
                        </span>
                        {q.topic && (
                          <span className="text-slate-500 dark:text-slate-400 truncate max-w-xs">{q.topic}</span>
                        )}
                      </div>
                      <p className="text-sm font-medium text-slate-900 dark:text-slate-200 truncate mt-1">
                        {q.text}
                      </p>
                    </div>
                  </div>

                  <div className="flex items-center gap-2 shrink-0">
                    <button
                      onClick={(e) => {
                        e.stopPropagation();
                        toggleBookmark(q.id);
                      }}
                      className="p-2 rounded-lg bg-amber-500/20 text-amber-500 dark:text-amber-400 border border-amber-500/40 hover:bg-rose-500/20 hover:text-rose-500 dark:hover:text-rose-400 transition-colors"
                      title="Yıldızı Kaldır"
                    >
                      <Trash2 className="w-4 h-4" />
                    </button>

                    {isExpanded ? (
                      <ChevronUp className="w-5 h-5 text-slate-400" />
                    ) : (
                      <ChevronDown className="w-5 h-5 text-slate-400" />
                    )}
                  </div>
                </div>

                {isExpanded && (
                  <div className="px-6 pb-6 pt-2 border-t border-slate-200 dark:border-fintech-border/60 space-y-4">
                    <p className="text-sm text-slate-900 dark:text-slate-100 whitespace-pre-line leading-relaxed">
                      {q.text}
                    </p>

                    <div className="grid grid-cols-1 gap-2">
                      {q.options.map((opt) => {
                        const isCorrect = opt.key === q.correct_answer;
                        return (
                          <div
                            key={opt.key}
                            className={`p-3 rounded-xl border text-xs sm:text-sm flex items-start gap-3 ${
                              isCorrect
                                ? 'bg-emerald-50 dark:bg-emerald-950/40 border-emerald-500 text-emerald-900 dark:text-emerald-200 font-semibold'
                                : 'bg-slate-50 dark:bg-fintech-card/50 border-slate-200 dark:border-fintech-border text-slate-700 dark:text-slate-300'
                            }`}
                          >
                            <span className="font-mono font-bold w-5 shrink-0">{opt.key})</span>
                            <span className="flex-1">{opt.text}</span>
                            {isCorrect && (
                              <span className="text-[11px] font-mono text-emerald-600 dark:text-emerald-400 font-bold shrink-0">
                                Doğru Seçenek ✓
                              </span>
                            )}
                          </div>
                        );
                      })}
                    </div>

                    {q.explanation && (
                      <div className="bg-slate-50 dark:bg-fintech-card/80 p-4 rounded-xl border border-slate-200 dark:border-fintech-border space-y-1 text-xs text-slate-700 dark:text-slate-300">
                        <span className="font-bold text-teal-600 dark:text-teal-400 uppercase tracking-wider block">
                          💡 Çözüm & Analiz:
                        </span>
                        <p className="whitespace-pre-line leading-relaxed">{q.explanation}</p>
                      </div>
                    )}

                    {q.trap && (
                      <div className="bg-amber-50 dark:bg-amber-950/30 p-3.5 rounded-xl border border-amber-300 dark:border-amber-500/40 text-xs text-amber-900 dark:text-amber-200/90 leading-relaxed">
                        <strong className="text-amber-600 dark:text-amber-400 block font-mono uppercase mb-1">
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
      )}
    </div>
  );
};
