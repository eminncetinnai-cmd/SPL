import React, { useState } from 'react';
import { 
  AlertTriangle, 
  RotateCcw, 
  Trash2, 
  Search, 
  CheckCircle, 
  ChevronDown, 
  ChevronUp, 
  Download, 
  Play,
  Star
} from 'lucide-react';
import { useProgressStore } from '../stores/progressStore';
import { useQuizStore } from '../stores/quizStore';
import { exportMistakesToCSV } from '../utils/csvExport';
import { ModuleId, Question } from '../types/exam';
import allQuestionsData from '../data/all_questions.json';

const canonicalMap = new Map<string, Question>(
  (allQuestionsData as Question[]).map((q) => [q.id, q])
);

interface MistakeNotebookPageProps {
  onNavigate: (page: string, params?: any) => void;
}

export const MistakeNotebookPage: React.FC<MistakeNotebookPageProps> = ({ onNavigate }) => {
  const { 
    mistakes, 
    removeMistake, 
    resolveMistake, 
    unresolveMistake, 
    toggleBookmark, 
    isBookmarked, 
    clearMistakes 
  } = useProgressStore();
  const { startQuiz } = useQuizStore();

  const [activeTab, setActiveTab] = useState<'active' | 'resolved'>('active');
  const [selectedModule, setSelectedModule] = useState<string>('all');
  const [searchQuery, setSearchQuery] = useState<string>('');
  const [expandedItems, setExpandedItems] = useState<Record<string, boolean>>({});

  const allMistakesList = Object.values(mistakes);
  const activeMistakes = allMistakesList.filter((m) => !m.resolved);
  const resolvedMistakes = allMistakesList.filter((m) => m.resolved);

  const currentTabList = activeTab === 'active' ? activeMistakes : resolvedMistakes;

  const filteredMistakes = currentTabList.filter((m) => {
    if (selectedModule !== 'all' && m.question.module_id !== selectedModule) return false;
    if (searchQuery.trim()) {
      const q = searchQuery.toLowerCase();
      return (
        m.question.text.toLowerCase().includes(q) ||
        (m.question.topic || '').toLowerCase().includes(q) ||
        (m.question.explanation || '').toLowerCase().includes(q)
      );
    }
    return true;
  });

  const toggleExpand = (id: string) => {
    setExpandedItems((prev) => ({ ...prev, [id]: !prev[id] }));
  };

  const handleStartMistakeQuiz = () => {
    if (filteredMistakes.length === 0) return;
    const questions = filteredMistakes.map((m) => canonicalMap.get(m.question.id) || m.question);

    startQuiz({
      mode: 'practice',
      customQuestions: questions,
      title: `Yanlışlar Tekrar Testi (${questions.length} Soru)`,
    });
    onNavigate('practice');
  };

  return (
    <div className="max-w-5xl mx-auto space-y-6 animate-fade-in pb-16">
      {/* Header Banner */}
      <div className="bg-white dark:bg-fintech-surface rounded-3xl border border-rose-200 dark:border-rose-500/30 p-6 sm:p-8 space-y-4 shadow-sm dark:shadow-xl">
        <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-4">
          <div className="flex items-center gap-3.5">
            <div className="p-3 rounded-2xl bg-rose-100 dark:bg-rose-500/20 text-rose-600 dark:text-rose-400">
              <AlertTriangle className="w-6 h-6" />
            </div>
            <div>
              <h1 className="text-xl sm:text-2xl font-black text-slate-900 dark:text-white tracking-tight">
                Yanlışlarım & Tekrar Defteri
              </h1>
              <p className="text-xs sm:text-sm text-slate-600 dark:text-slate-400">
                Daha önce çözdüğünüz testlerde yanlış yaptığınız sorular burada toplanır.
              </p>
            </div>
          </div>

          {activeMistakes.length > 0 && activeTab === 'active' && (
            <div className="flex items-center gap-3">
              <button
                onClick={() => exportMistakesToCSV(activeMistakes)}
                className="flex items-center gap-1.5 px-3.5 py-2 rounded-xl bg-slate-50 hover:bg-slate-100 dark:bg-fintech-card dark:hover:bg-fintech-cardHover text-slate-700 dark:text-slate-300 text-xs font-semibold border border-slate-200 dark:border-fintech-border shadow-sm transition-colors"
              >
                <Download className="w-4 h-4 text-teal-600 dark:text-teal-400" />
                <span>CSV İndir</span>
              </button>

              <button
                onClick={handleStartMistakeQuiz}
                className="flex items-center gap-2 px-5 py-2.5 rounded-xl bg-gradient-to-r from-rose-500 to-amber-500 hover:from-rose-400 hover:to-amber-400 text-slate-950 font-black text-xs shadow-md shadow-rose-500/20 active:scale-95 transition-all"
              >
                <Play className="w-4 h-4 fill-slate-950" />
                <span>Yanlışlardan Test Başlat ({filteredMistakes.length})</span>
              </button>
            </div>
          )}
        </div>

        {/* Active vs Resolved Tabs */}
        <div className="flex items-center gap-2 border-t border-slate-100 dark:border-fintech-border/60 pt-3">
          <button
            onClick={() => setActiveTab('active')}
            className={`flex items-center gap-2 px-3.5 py-2 rounded-xl text-xs font-bold transition-all ${
              activeTab === 'active'
                ? 'bg-rose-500 text-white shadow-xs'
                : 'bg-slate-100 dark:bg-fintech-card text-slate-600 dark:text-slate-400 hover:bg-slate-200 dark:hover:bg-fintech-cardHover'
            }`}
          >
            <AlertTriangle className="w-4 h-4" />
            <span>Aktif Hatalar ({activeMistakes.length})</span>
          </button>

          <button
            onClick={() => setActiveTab('resolved')}
            className={`flex items-center gap-2 px-3.5 py-2 rounded-xl text-xs font-bold transition-all ${
              activeTab === 'resolved'
                ? 'bg-emerald-600 text-white shadow-xs'
                : 'bg-slate-100 dark:bg-fintech-card text-slate-600 dark:text-slate-400 hover:bg-slate-200 dark:hover:bg-fintech-cardHover'
            }`}
          >
            <CheckCircle className="w-4 h-4" />
            <span>Eritilenler / Öğrenilenler ({resolvedMistakes.length})</span>
          </button>
        </div>

        {/* Filter and Search Bar */}
        <div className="grid grid-cols-1 sm:grid-cols-12 gap-3 pt-1">
          <div className="sm:col-span-8 relative">
            <Search className="absolute left-3.5 top-3 w-4 h-4 text-slate-400" />
            <input
              type="text"
              value={searchQuery}
              onChange={(e) => setSearchQuery(e.target.value)}
              placeholder="Hatalı sorular içinde metin veya konu ara..."
              className="w-full bg-slate-50 dark:bg-fintech-card border border-slate-200 dark:border-fintech-border rounded-xl pl-10 pr-4 py-2.5 text-xs text-slate-900 dark:text-slate-200 placeholder-slate-400 dark:placeholder-slate-500 focus:outline-none focus:border-rose-500 transition-colors shadow-xs"
            />
          </div>

          <div className="sm:col-span-4">
            <select
              value={selectedModule}
              onChange={(e) => setSelectedModule(e.target.value)}
              className="w-full bg-slate-50 dark:bg-fintech-card border border-slate-200 dark:border-fintech-border rounded-xl px-3 py-2.5 text-xs text-slate-900 dark:text-slate-200 focus:outline-none focus:border-rose-500 transition-colors shadow-xs"
            >
              <option value="all">Tüm Modüller ({currentTabList.length})</option>
              <option value="1001">Modül 1001 Mevzuat</option>
              <option value="1003">Modül 1003 Araçlar</option>
              <option value="1005">Modül 1005 Yatırım Kuruluşları</option>
              <option value="1012">Modül 1012 Takas & Saklama</option>
            </select>
          </div>
        </div>
      </div>

      {/* Mistake List */}
      {filteredMistakes.length === 0 ? (
        <div className="bg-white dark:bg-fintech-surface rounded-2xl border border-slate-200 dark:border-fintech-border p-12 text-center space-y-3 shadow-sm">
          <div className="w-12 h-12 rounded-full bg-emerald-100 dark:bg-emerald-500/20 text-emerald-600 dark:text-emerald-400 flex items-center justify-center mx-auto">
            <CheckCircle className="w-6 h-6" />
          </div>
          <h3 className="text-base font-bold text-slate-900 dark:text-white">
            {activeTab === 'active' ? 'Harika! Aktif Hatalı Soru Bulunmuyor' : 'Henüz Eritilen Soru Yok'}
          </h3>
          <p className="text-xs text-slate-500 dark:text-slate-400 max-w-sm mx-auto">
            {activeTab === 'active'
              ? 'Çözdüğünüz testlerde yanlış yaptığınız sorular burada listelenecek ve doğru çözdükçe otomatik eritilecektir.'
              : 'Aktif hatalarınızdan birini doğru çözdüğünüzde veya "Erit" butonuna bastığınızda burada listelenir.'}
          </p>
        </div>
      ) : (
        <div className="space-y-4">
          <div className="flex items-center justify-between text-xs text-slate-500 dark:text-slate-400 px-2 font-mono">
            <span>{filteredMistakes.length} {activeTab === 'active' ? 'Aktif Hatalı Soru' : 'Eritilen/Öğrenilen Soru'} Listeleniyor</span>
            {currentTabList.length > 0 && activeTab === 'active' && (
              <button
                onClick={() => {
                  if (confirm('Tüm aktif hatalı soru geçmişi temizlensin mi?')) {
                    clearMistakes();
                  }
                }}
                className="text-rose-600 dark:text-rose-400 hover:text-rose-700 dark:hover:text-rose-300 transition-colors flex items-center gap-1 font-semibold"
              >
                <Trash2 className="w-3.5 h-3.5" />
                <span>Tümünü Temizle</span>
              </button>
            )}
          </div>

          {filteredMistakes.map((item, idx) => {
            const rawQ = item.question;
            const q = canonicalMap.get(rawQ.id) || rawQ;
            const isExpanded = expandedItems[q.id] !== false;
            const bookmarked = isBookmarked(q.id);

            // Resolve selected option key to canonical question options
            let canonicalSelectedKey = item.last_selected_option;
            if (rawQ.options && q.options) {
              const selectedOpt = rawQ.options.find((o) => o.key === item.last_selected_option);
              if (selectedOpt) {
                const matchedInCanonical = q.options.find((o) => o.text.trim() === selectedOpt.text.trim());
                if (matchedInCanonical) {
                  canonicalSelectedKey = matchedInCanonical.key;
                }
              }
            }

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
                    <span className="w-7 h-7 rounded-lg bg-rose-100 dark:bg-rose-500/20 text-rose-800 dark:text-rose-300 font-mono text-xs font-bold flex items-center justify-center shrink-0">
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
                        <span className="text-[11px] font-mono text-rose-700 dark:text-rose-400 bg-rose-50 dark:bg-rose-500/10 px-2 py-0.5 rounded font-semibold">
                          {item.wrong_count} Kez Yanlış Yapıldı
                        </span>
                        {(item.correct_streak || 0) > 0 && (
                          <span className="text-[11px] font-mono text-emerald-700 dark:text-emerald-400 bg-emerald-50 dark:bg-emerald-500/10 px-2 py-0.5 rounded font-semibold">
                            {item.correct_streak}/2 Doğru
                          </span>
                        )}
                      </div>
                      <p className="text-sm font-semibold text-slate-900 dark:text-slate-200 truncate mt-1">
                        {q.text}
                      </p>
                    </div>
                  </div>

                  <div className="flex items-center gap-2 shrink-0">
                    {activeTab === 'active' ? (
                      <button
                        onClick={(e) => {
                          e.stopPropagation();
                          resolveMistake(q.id);
                        }}
                        className="flex items-center gap-1 px-2.5 py-1.5 rounded-lg bg-emerald-50 hover:bg-emerald-100 dark:bg-emerald-950/40 dark:hover:bg-emerald-900/40 text-emerald-700 dark:text-emerald-300 border border-emerald-300 dark:border-emerald-600 text-xs font-bold transition-all shadow-xs cursor-pointer"
                        title="Bu soruyu kavradım, eritilenlere taşı"
                      >
                        <CheckCircle className="w-3.5 h-3.5" />
                        <span className="hidden sm:inline">Erit</span>
                      </button>
                    ) : (
                      <button
                        onClick={(e) => {
                          e.stopPropagation();
                          unresolveMistake(q.id);
                        }}
                        className="flex items-center gap-1 px-2.5 py-1.5 rounded-lg bg-slate-100 hover:bg-slate-200 dark:bg-slate-800 dark:hover:bg-slate-700 text-slate-600 dark:text-slate-300 border border-slate-300 dark:border-slate-600 text-xs font-bold transition-all shadow-xs cursor-pointer"
                        title="Bu soruyu aktif hatalara geri taşı"
                      >
                        <RotateCcw className="w-3.5 h-3.5" />
                        <span className="hidden sm:inline">Geri Al</span>
                      </button>
                    )}

                    <button
                      onClick={(e) => {
                        e.stopPropagation();
                        toggleBookmark(q.id);
                      }}
                      className={`p-2 rounded-lg border ${
                        bookmarked
                          ? 'bg-amber-100 dark:bg-amber-500/20 text-amber-600 dark:text-amber-400 border-amber-300 dark:border-amber-500/40'
                          : 'bg-slate-100 dark:bg-slate-800 text-slate-400 hover:text-amber-500 border-slate-200 dark:border-slate-700'
                      }`}
                    >
                      <Star className={`w-4 h-4 ${bookmarked ? 'fill-amber-500 text-amber-500 dark:fill-amber-400 dark:text-amber-400' : ''}`} />
                    </button>

                    <button
                      onClick={(e) => {
                        e.stopPropagation();
                        removeMistake(q.id);
                      }}
                      className="p-2 rounded-lg bg-slate-100 hover:bg-rose-50 dark:bg-slate-800 dark:hover:bg-rose-500/20 text-slate-500 hover:text-rose-600 dark:text-slate-400 dark:hover:text-rose-300 border border-slate-200 dark:border-slate-700 transition-colors"
                      title="Defterden Kaldır"
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
                  <div className="px-6 pb-6 pt-2 border-t border-slate-100 dark:border-fintech-border/60 space-y-4">
                    <p className="text-sm text-slate-900 dark:text-slate-100 whitespace-pre-line leading-relaxed">
                      {q.text}
                    </p>

                    {/* Options list */}
                    <div className="grid grid-cols-1 gap-2">
                      {q.options.map((opt) => {
                        const isCorrect = opt.key === q.correct_answer;
                        const wasSelected = canonicalSelectedKey === opt.key;

                        let style = 'bg-slate-50 dark:bg-fintech-card/50 border-slate-200 dark:border-fintech-border text-slate-700 dark:text-slate-300';
                        if (isCorrect) {
                          style = 'bg-emerald-50 dark:bg-emerald-950/40 border-emerald-300 dark:border-emerald-500 text-emerald-900 dark:text-emerald-200 font-semibold';
                        } else if (wasSelected) {
                          style = 'bg-rose-50 dark:bg-rose-950/40 border-rose-300 dark:border-rose-500 text-rose-900 dark:text-rose-200';
                        }

                        return (
                          <div
                            key={opt.key}
                            className={`p-3 rounded-xl border text-xs sm:text-sm flex items-start gap-3 ${style}`}
                          >
                            <span className="font-mono font-bold w-5 shrink-0">{opt.key})</span>
                            <span className="flex-1">{opt.text}</span>
                            {isCorrect && (
                              <span className="text-[11px] font-mono text-emerald-700 dark:text-emerald-400 font-bold shrink-0">
                                Doğru Seçenek ✓
                              </span>
                            )}
                            {wasSelected && (
                              <span className="text-[11px] font-mono text-rose-700 dark:text-rose-400 font-bold shrink-0">
                                Yanlış Seçiminiz ✗
                              </span>
                            )}
                          </div>
                        );
                      })}
                    </div>

                    {/* Solution */}
                    {q.explanation && (
                      <div className="bg-slate-50 dark:bg-fintech-card/80 p-4 rounded-xl border border-slate-200 dark:border-fintech-border space-y-1 text-xs text-slate-700 dark:text-slate-300">
                        <span className="font-bold text-teal-700 dark:text-teal-400 uppercase tracking-wider block">
                          💡 Çözüm Analizi:
                        </span>
                        <p className="whitespace-pre-line leading-relaxed">{q.explanation}</p>
                      </div>
                    )}

                    {/* Trap */}
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
      )}
    </div>
  );
};
