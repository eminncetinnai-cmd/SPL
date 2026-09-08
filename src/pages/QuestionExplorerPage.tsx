import React, { useState, useMemo } from 'react';
import { 
  Search, 
  Filter, 
  Play, 
  Star, 
  ChevronDown, 
  ChevronUp, 
  BookOpen, 
  CheckCircle,
  Sparkles,
  Layers
} from 'lucide-react';
import allQuestionsData from '../data/all_questions.json';
import { Question, ModuleId } from '../types/exam';
import { useProgressStore } from '../stores/progressStore';
import { useQuizStore } from '../stores/quizStore';
import { formatQuestionId } from '../utils/questionSelector';

interface QuestionExplorerPageProps {
  initialModuleId?: string;
  initialStatus?: 'all' | 'unseen' | 'seen';
  onNavigate: (page: string, params?: any) => void;
}

export const QuestionExplorerPage: React.FC<QuestionExplorerPageProps> = ({ 
  initialModuleId,
  initialStatus,
  onNavigate 
}) => {
  const { toggleBookmark, isBookmarked, isQuestionSeen, seenQuestionIds } = useProgressStore();
  const { startQuiz } = useQuizStore();

  const [searchQuery, setSearchQuery] = useState('');
  const [selectedModule, setSelectedModule] = useState<string>(initialModuleId || 'all');
  const [selectedSource, setSelectedSource] = useState<string>('all');
  const [selectedStatus, setSelectedStatus] = useState<'all' | 'unseen' | 'seen'>(initialStatus || 'all');
  const [page, setPage] = useState(1);
  const [expandedItems, setExpandedItems] = useState<Record<string, boolean>>({});

  // Sync if initial params change
  React.useEffect(() => {
    if (initialModuleId) setSelectedModule(initialModuleId);
    if (initialStatus) setSelectedStatus(initialStatus);
  }, [initialModuleId, initialStatus]);

  const pageSize = 20;
  const allQuestions = allQuestionsData as Question[];

  // Calculate pool metrics
  const modulePool = useMemo(() => {
    return selectedModule === 'all' 
      ? allQuestions 
      : allQuestions.filter((q) => q.module_id === selectedModule);
  }, [allQuestions, selectedModule]);

  const seenInModule = useMemo(() => {
    return modulePool.filter((q) => isQuestionSeen(q.id)).length;
  }, [modulePool, isQuestionSeen, seenQuestionIds]);

  const unseenInModule = modulePool.length - seenInModule;

  const filteredQuestions = useMemo(() => {
    return allQuestions.filter((q) => {
      if (selectedModule !== 'all' && q.module_id !== selectedModule) return false;
      
      if (selectedSource !== 'all') {
        if (selectedSource === 'cikmis') {
          if (q.source !== 'cikmis') return false;
        } else if (selectedSource === 'genel') {
          if (q.source === 'cikmis') return false;
        } else if (q.source !== selectedSource) {
          return false;
        }
      }

      const isSeen = isQuestionSeen(q.id);
      if (selectedStatus === 'unseen' && isSeen) return false;
      if (selectedStatus === 'seen' && !isSeen) return false;

      if (searchQuery.trim()) {
        const query = searchQuery.toLowerCase();
        return (
          q.text.toLowerCase().includes(query) ||
          (q.topic || '').toLowerCase().includes(query) ||
          (q.chapter || '').toLowerCase().includes(query) ||
          (q.explanation || '').toLowerCase().includes(query) ||
          (q.trap || '').toLowerCase().includes(query) ||
          q.id.toLowerCase().includes(query)
        );
      }
      return true;
    });
  }, [allQuestions, selectedModule, selectedSource, selectedStatus, searchQuery, isQuestionSeen, seenQuestionIds]);

  const totalPages = Math.ceil(filteredQuestions.length / pageSize) || 1;
  const paginatedQuestions = filteredQuestions.slice((page - 1) * pageSize, page * pageSize);

  const toggleExpand = (id: string) => {
    setExpandedItems((prev) => ({ ...prev, [id]: !prev[id] }));
  };

  const handleStartCustomQuiz = () => {
    if (filteredQuestions.length === 0) return;
    const questionsToUse = filteredQuestions.slice(0, 50);

    const titlePrefix = selectedStatus === 'unseen' 
      ? 'Çözülmemiş Taze Sorular Testi' 
      : 'Özel Soru Testi';

    startQuiz({
      mode: 'practice',
      customQuestions: questionsToUse,
      title: `${titlePrefix} (${questionsToUse.length} Soru)`,
    });
    onNavigate('practice');
  };

  return (
    <div className="max-w-6xl mx-auto space-y-6 animate-fade-in pb-16">
      {/* Header Banner */}
      <div className="bg-white dark:bg-fintech-surface rounded-3xl border border-slate-200 dark:border-fintech-border p-6 sm:p-8 space-y-5 shadow-sm">
        <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-4">
          <div>
            <div className="flex items-center gap-2 text-xs font-mono text-teal-600 dark:text-teal-400 font-bold uppercase tracking-wider mb-1">
              <Layers className="w-4 h-4" />
              <span>SPK SPL DÜZEY 1 TAM SORU BANKASI</span>
            </div>
            <h1 className="text-xl sm:text-2xl font-black text-slate-900 dark:text-white tracking-tight">
              {allQuestions.length} Soru Bankası Arama & Keşif Motoru
            </h1>
            <p className="text-xs sm:text-sm text-slate-600 dark:text-slate-400">
              Tüm 4 modüldeki master, öğretici ve konu anlatımı çözümlü soruları filtreleyin, çözmediğiniz soruları bulun veya test başlatın.
            </p>
          </div>

          {filteredQuestions.length > 0 && (
            <button
              onClick={handleStartCustomQuiz}
              className="flex items-center gap-2 px-5 py-2.5 rounded-xl bg-gradient-to-r from-teal-500 to-emerald-500 hover:from-teal-400 hover:to-emerald-400 text-slate-950 font-black text-xs shadow-md shadow-teal-500/20 active:scale-95 transition-all self-start sm:self-auto shrink-0"
            >
              <Play className="w-4 h-4 fill-slate-950" />
              <span>{selectedStatus === 'unseen' ? 'Bu Çözülmemiş Sorulardan Test Başlat' : 'Bu Filtreden Test Başlat'}</span>
            </button>
          )}
        </div>

        {/* Status Filter Tabs */}
        <div className="flex items-center gap-2 flex-wrap pt-1 border-t border-slate-200 dark:border-fintech-border/60">
          <span className="text-xs font-mono text-slate-500 dark:text-slate-400 uppercase font-bold mr-1">Durum:</span>
          <button
            onClick={() => { setSelectedStatus('all'); setPage(1); }}
            className={`px-3 py-1.5 rounded-xl text-xs font-bold transition-all ${
              selectedStatus === 'all'
                ? 'bg-teal-500 text-slate-950 shadow-sm font-black'
                : 'bg-slate-100 dark:bg-fintech-card text-slate-600 dark:text-slate-400 hover:text-slate-900 dark:hover:text-white border border-slate-200 dark:border-fintech-border'
            }`}
          >
            Tüm Sorular ({modulePool.length})
          </button>
          <button
            onClick={() => { setSelectedStatus('unseen'); setPage(1); }}
            className={`flex items-center gap-1.5 px-3 py-1.5 rounded-xl text-xs font-bold transition-all ${
              selectedStatus === 'unseen'
                ? 'bg-amber-500 text-slate-950 shadow-sm font-black'
                : 'bg-slate-100 dark:bg-fintech-card text-amber-700 dark:text-amber-300/80 hover:text-amber-800 dark:hover:text-amber-200 border border-amber-300 dark:border-amber-500/30'
            }`}
          >
            <Sparkles className="w-3.5 h-3.5" />
            <span>✨ Henüz Çözülmemiş ({unseenInModule})</span>
          </button>
          <button
            onClick={() => { setSelectedStatus('seen'); setPage(1); }}
            className={`flex items-center gap-1.5 px-3 py-1.5 rounded-xl text-xs font-bold transition-all ${
              selectedStatus === 'seen'
                ? 'bg-emerald-500 text-slate-950 shadow-sm font-black'
                : 'bg-slate-100 dark:bg-fintech-card text-emerald-700 dark:text-emerald-400/80 hover:text-emerald-800 dark:hover:text-emerald-300 border border-emerald-300 dark:border-emerald-500/30'
            }`}
          >
            <CheckCircle className="w-3.5 h-3.5" />
            <span>✅ Çözülmüş Sorular ({seenInModule})</span>
          </button>
        </div>

        {/* Detailed Filters */}
        <div className="grid grid-cols-1 sm:grid-cols-12 gap-3 pt-2">
          <div className="sm:col-span-6 relative">
            <Search className="absolute left-3.5 top-3 w-4 h-4 text-slate-400" />
            <input
              type="text"
              value={searchQuery}
              onChange={(e) => {
                setSearchQuery(e.target.value);
                setPage(1);
              }}
              placeholder="Soru metni, #1001-M042, rüçhan, sukuk, takasbank..."
              className="w-full bg-slate-50 dark:bg-fintech-card border border-slate-200 dark:border-fintech-border rounded-xl pl-10 pr-4 py-2.5 text-xs text-slate-900 dark:text-slate-200 placeholder-slate-400 focus:outline-none focus:border-teal-500 transition-colors"
            />
          </div>

          <div className="sm:col-span-3">
            <select
              value={selectedModule}
              onChange={(e) => {
                setSelectedModule(e.target.value);
                setPage(1);
              }}
              className="w-full bg-slate-50 dark:bg-fintech-card border border-slate-200 dark:border-fintech-border rounded-xl px-3 py-2.5 text-xs text-slate-900 dark:text-slate-200 focus:outline-none focus:border-teal-500 transition-colors"
            >
              <option value="all">Tüm Dersler ({allQuestions.length} Soru)</option>
              <option value="1001">Modül 1001: Mevzuat & Meslek</option>
              <option value="1003">Modül 1003: SP Araçları 1</option>
              <option value="1005">Modül 1005: Yatırım Kuruluşları</option>
              <option value="1012">Modül 1012: Takas & Saklama</option>
            </select>
          </div>

          <div className="sm:col-span-3">
            <select
              value={selectedSource}
              onChange={(e) => {
                setSelectedSource(e.target.value);
                setPage(1);
              }}
              className="w-full bg-slate-50 dark:bg-fintech-card border border-slate-200 dark:border-fintech-border rounded-xl px-3 py-2.5 text-xs text-slate-900 dark:text-slate-200 focus:outline-none focus:border-teal-500 transition-colors"
            >
              <option value="all">Tüm Soru Havuzu ({allQuestions.length} Soru)</option>
              <option value="cikmis">🎯 Çıkmış Sınav Soruları (110 Soru)</option>
              <option value="genel">📚 Genel Soru Havuzu (540 Soru - Çıkmış Hariç)</option>
            </select>
          </div>
        </div>
      </div>

      {/* Results Header */}
      <div className="flex items-center justify-between text-xs text-slate-500 dark:text-slate-400 px-2 font-mono">
        <span>Toplam {filteredQuestions.length} Soru Eşleşti</span>
        <span>Sayfa {page} / {totalPages}</span>
      </div>

      {/* Question Cards List */}
      <div className="space-y-4">
        {paginatedQuestions.map((q, idx) => {
          const globalIndex = (page - 1) * pageSize + idx + 1;
          const isExpanded = expandedItems[q.id] !== false;
          const bookmarked = isBookmarked(q.id);
          const isSeen = isQuestionSeen(q.id);

          return (
            <div
              key={q.id}
              className={`bg-white dark:bg-fintech-surface rounded-2xl border shadow-sm overflow-hidden transition-all ${
                isSeen ? 'border-slate-200 dark:border-fintech-border' : 'border-amber-300 dark:border-amber-500/30'
              }`}
            >
              <div
                onClick={() => toggleExpand(q.id)}
                className="p-5 flex items-center justify-between gap-4 cursor-pointer hover:bg-slate-50 dark:hover:bg-fintech-card/40 transition-colors"
              >
                <div className="flex items-center gap-3 flex-1 min-w-0">
                  <span className="w-7 h-7 rounded-lg bg-teal-500/15 text-teal-700 dark:text-teal-300 font-mono text-xs font-bold flex items-center justify-center shrink-0">
                    {globalIndex}
                  </span>

                  <div className="min-w-0 flex-1">
                    <div className="flex items-center gap-2 flex-wrap text-xs">
                      <span className="font-mono px-2 py-0.5 rounded bg-slate-100 dark:bg-slate-800 text-teal-700 dark:text-teal-400 border border-slate-200 dark:border-slate-700 font-bold">
                        Modül {q.module_id}
                      </span>
                      <span className="font-mono text-xs px-2 py-0.5 rounded bg-teal-500/10 text-teal-700 dark:text-teal-300 border border-teal-500/30 font-bold">
                        {formatQuestionId(q.id)}
                      </span>
                      <span className={`text-[10px] font-mono px-2 py-0.5 rounded font-bold ${
                        isSeen 
                          ? 'bg-emerald-50 dark:bg-emerald-500/15 text-emerald-700 dark:text-emerald-300 border border-emerald-300 dark:border-emerald-500/30' 
                          : 'bg-amber-50 dark:bg-amber-500/20 text-amber-700 dark:text-amber-300 border border-amber-300 dark:border-amber-500/40'
                      }`}>
                        {isSeen ? '✅ Çözüldü' : '✨ Henüz Çözülmedi'}
                      </span>
                      {q.topic && (
                        <span className="text-slate-500 dark:text-slate-400 truncate max-w-xs">{q.topic}</span>
                      )}
                      <span className="text-[10px] font-mono px-2 py-0.5 rounded bg-slate-100 dark:bg-slate-900 border border-slate-200 dark:border-slate-800 text-slate-600 dark:text-slate-400">
                        {q.id.includes('konu') ? 'Konu Anlatımı Çözümlü' : q.source === 'master' ? 'Master Soru' : 'Öğretici Soru'}
                      </span>
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
                    className={`p-2 rounded-lg border ${
                      bookmarked
                        ? 'bg-amber-500/20 text-amber-500 dark:text-amber-400 border-amber-500/40'
                        : 'bg-slate-100 dark:bg-slate-800 text-slate-400 hover:text-amber-500 dark:hover:text-amber-300 border-slate-200 dark:border-slate-700'
                    }`}
                  >
                    <Star className={`w-4 h-4 ${bookmarked ? 'fill-amber-500 dark:fill-amber-400' : ''}`} />
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

                  {/* Options */}
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
                              Doğru Cevap ✓
                            </span>
                          )}
                        </div>
                      );
                    })}
                  </div>

                  {/* Explanation & Glossary */}
                  {q.explanation && (() => {
                    const parts = q.explanation.split('📌 Soruda Geçen Kısaltmalar & Terimler:');
                    const mainExplanation = parts[0].trim();
                    const abbreviations = parts[1] ? parts[1].trim() : null;

                    return (
                      <div className="space-y-3">
                        <div className="bg-slate-50 dark:bg-fintech-card/80 p-4 rounded-xl border border-slate-200 dark:border-fintech-border space-y-1 text-xs text-slate-700 dark:text-slate-300">
                          <span className="font-bold text-teal-600 dark:text-teal-400 uppercase tracking-wider block">
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
                                    <span className="font-mono font-bold text-cyan-800 dark:text-cyan-300 shrink-0 bg-cyan-100 dark:bg-cyan-500/20 px-1.5 py-0.5 rounded border border-cyan-300 dark:border-cyan-500/40 text-[10px]">
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

                  {/* Trap */}
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

      {/* Pagination Controls */}
      {totalPages > 1 && (
        <div className="flex items-center justify-center gap-2 pt-4">
          <button
            onClick={() => setPage((p) => Math.max(1, p - 1))}
            disabled={page === 1}
            className="px-4 py-2 rounded-xl bg-white hover:bg-slate-50 dark:bg-fintech-surface dark:hover:bg-fintech-card border border-slate-200 dark:border-fintech-border text-xs font-bold text-slate-700 dark:text-slate-300 disabled:opacity-40 disabled:cursor-not-allowed shadow-sm"
          >
            ← Önceki Sayfa
          </button>
          <span className="px-4 py-2 font-mono text-xs text-slate-500 dark:text-slate-400">
            {page} / {totalPages}
          </span>
          <button
            onClick={() => setPage((p) => Math.min(totalPages, p + 1))}
            disabled={page === totalPages}
            className="px-4 py-2 rounded-xl bg-white hover:bg-slate-50 dark:bg-fintech-surface dark:hover:bg-fintech-card border border-slate-200 dark:border-fintech-border text-xs font-bold text-slate-700 dark:text-slate-300 disabled:opacity-40 disabled:cursor-not-allowed shadow-sm"
          >
            Sonraki Sayfa →
          </button>
        </div>
      )}
    </div>
  );
};
