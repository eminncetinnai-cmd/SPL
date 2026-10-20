import React, { useState, useEffect, useMemo } from 'react';
import { 
  Sparkles, 
  RotateCw, 
  CheckCircle2, 
  XCircle, 
  Star, 
  Shuffle, 
  ArrowLeft, 
  ArrowRight, 
  Lightbulb, 
  AlertTriangle, 
  BookOpen, 
  Layers,
  Award,
  Filter
} from 'lucide-react';
import flashcardsData from '../data/flashcards.json';
import modulesData from '../data/modules.json';
import { Flashcard, ModuleId } from '../types/exam';
import { useProgressStore } from '../stores/progressStore';
import { shuffleArray } from '../utils/questionSelector';

interface FlashcardsPageProps {
  initialModuleId?: ModuleId;
  onNavigate: (page: string, params?: any) => void;
}

export const FlashcardsPage: React.FC<FlashcardsPageProps> = ({
  initialModuleId = '1001',
  onNavigate,
}) => {
  const { 
    learnedCards, 
    starredCards, 
    toggleLearnedCard, 
    isCardLearned, 
    toggleStarredCard, 
    isCardStarred 
  } = useProgressStore();

  const [selectedModule, setSelectedModule] = useState<ModuleId | 'all'>(initialModuleId || '1001');
  const [filterMode, setFilterMode] = useState<'all' | 'unlearned' | 'learned' | 'starred'>('all');
  const [currentIndex, setCurrentIndex] = useState(0);
  const [isFlipped, setIsFlipped] = useState(false);
  const [isShuffled, setIsShuffled] = useState(false);

  const allCards = flashcardsData as Flashcard[];

  // Filter cards by module and learning state
  const filteredCards = useMemo(() => {
    let pool = allCards.filter((card) => {
      if (selectedModule !== 'all' && card.module_id !== selectedModule) return false;
      if (filterMode === 'learned') return isCardLearned(card.id);
      if (filterMode === 'unlearned') return !isCardLearned(card.id);
      if (filterMode === 'starred') return isCardStarred(card.id);
      return true;
    });

    if (isShuffled) {
      pool = shuffleArray(pool);
    }
    return pool;
  }, [allCards, selectedModule, filterMode, isShuffled, learnedCards, starredCards]);

  // Reset index and flipped state on filter change
  useEffect(() => {
    setCurrentIndex(0);
    setIsFlipped(false);
  }, [selectedModule, filterMode, isShuffled]);

  // Keyboard navigation
  useEffect(() => {
    const handleKeyDown = (e: KeyboardEvent) => {
      if (e.code === 'Space') {
        e.preventDefault();
        setIsFlipped((prev) => !prev);
      } else if (e.key === 'ArrowRight') {
        handleNext();
      } else if (e.key === 'ArrowLeft') {
        handlePrev();
      } else if (e.key === '1') {
        if (currentCard && isCardLearned(currentCard.id)) {
          toggleLearnedCard(currentCard.id);
        }
      } else if (e.key === '2') {
        if (currentCard && !isCardLearned(currentCard.id)) {
          toggleLearnedCard(currentCard.id);
        }
      } else if (e.key.toLowerCase() === 's') {
        if (currentCard) {
          toggleStarredCard(currentCard.id);
        }
      }
    };

    window.addEventListener('keydown', handleKeyDown);
    return () => window.removeEventListener('keydown', handleKeyDown);
  }, [filteredCards, currentIndex, isCardLearned, isCardStarred]);

  const total = filteredCards.length;
  const currentCard = total > 0 ? filteredCards[currentIndex % total] : null;

  const handleNext = () => {
    setIsFlipped(false);
    setCurrentIndex((prev) => (prev + 1 < total ? prev + 1 : 0));
  };

  const handlePrev = () => {
    setIsFlipped(false);
    setCurrentIndex((prev) => (prev - 1 >= 0 ? prev - 1 : total - 1));
  };

  // Module stats
  const moduleTotal = selectedModule === 'all' ? 400 : 100;
  const moduleLearnedCount = allCards
    .filter((c) => selectedModule === 'all' || c.module_id === selectedModule)
    .filter((c) => isCardLearned(c.id)).length;
  const learnedPercentage = Math.round((moduleLearnedCount / moduleTotal) * 100);

  return (
    <div className="max-w-5xl mx-auto space-y-6 animate-fade-in pb-16">
      {/* Top Header */}
      <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-4 border-b border-slate-200 dark:border-fintech-border/70 pb-5">
        <div>
          <span className="text-xs font-mono text-teal-600 dark:text-teal-400 font-bold uppercase tracking-wider block">
            Hızlı Kavram Tekrarı (Flashcards)
          </span>
          <h1 className="text-xl sm:text-2xl font-black text-slate-900 dark:text-white tracking-tight">
            400 Akılda Kalıcı Öğrenme Kartı
          </h1>
          <p className="text-xs text-slate-600 dark:text-slate-400 mt-0.5">
            Kavram çiftleri, somut finansal örnekler ve sınav tuzaklarıyla hafızanızı tazeleyin.
          </p>
        </div>

        {/* Progress Badge */}
        <div className="flex items-center gap-3 bg-white dark:bg-fintech-surface p-3 rounded-2xl border border-slate-200 dark:border-fintech-border self-start sm:self-auto shadow-sm">
          <div className="text-right">
            <span className="text-[10px] uppercase font-mono text-slate-500 dark:text-slate-400 block font-bold">
              Öğrenilen Kartlar
            </span>
            <span className="text-sm font-mono font-bold text-teal-600 dark:text-teal-300">
              {moduleLearnedCount} / {moduleTotal} (%{learnedPercentage})
            </span>
          </div>
          <div className="w-10 h-10 rounded-xl bg-teal-500/15 border border-teal-500/30 flex items-center justify-center font-mono font-bold text-xs text-teal-600 dark:text-teal-400">
            %{learnedPercentage}
          </div>
        </div>
      </div>

      {/* Module Selector Tabs */}
      <div className="grid grid-cols-2 sm:grid-cols-5 gap-2.5">
        <button
          onClick={() => setSelectedModule('all')}
          className={`p-3 rounded-xl border text-left text-xs font-bold transition-all shadow-sm ${
            selectedModule === 'all'
              ? 'bg-teal-50 dark:bg-teal-500/15 border-teal-500 text-teal-700 dark:text-teal-300 font-black'
              : 'bg-white dark:bg-fintech-surface border-slate-200 dark:border-fintech-border text-slate-600 dark:text-slate-400 hover:text-slate-900 dark:hover:text-white'
          }`}
        >
          <span className="block text-[10px] text-teal-600 dark:text-teal-400 font-mono">Tüm Modüller</span>
          <span>400 Kart</span>
        </button>

        {modulesData.map((m) => (
          <button
            key={m.id}
            onClick={() => setSelectedModule(m.id as ModuleId)}
            className={`p-3 rounded-xl border text-left text-xs font-bold transition-all shadow-sm ${
              selectedModule === m.id
                ? 'bg-teal-50 dark:bg-teal-500/15 border-teal-500 text-teal-700 dark:text-teal-300 font-black'
                : 'bg-white dark:bg-fintech-surface border-slate-200 dark:border-fintech-border text-slate-600 dark:text-slate-400 hover:text-slate-900 dark:hover:text-white'
            }`}
          >
            <span className="block text-[10px] text-teal-600 dark:text-teal-400 font-mono">Modül {m.code}</span>
            <span className="truncate block">{m.short_name}</span>
          </button>
        ))}
      </div>

      {/* Filter and Shuffle Controls */}
      <div className="flex flex-wrap items-center justify-between gap-3 bg-white dark:bg-fintech-surface p-3 rounded-2xl border border-slate-200 dark:border-fintech-border text-xs shadow-sm">
        <div className="flex items-center gap-1.5 flex-wrap">
          <button
            onClick={() => setFilterMode('all')}
            className={`px-3 py-1.5 rounded-lg font-bold transition-all ${
              filterMode === 'all' ? 'bg-teal-600 text-white shadow-sm font-black' : 'text-slate-600 dark:text-slate-400 hover:text-slate-900 dark:hover:text-white'
            }`}
          >
            Tümü ({allCards.filter((c) => selectedModule === 'all' || c.module_id === selectedModule).length})
          </button>
          <button
            onClick={() => setFilterMode('unlearned')}
            className={`px-3 py-1.5 rounded-lg font-bold transition-all ${
              filterMode === 'unlearned' ? 'bg-amber-500 text-slate-950 shadow-sm font-black' : 'text-slate-600 dark:text-slate-400 hover:text-slate-900 dark:hover:text-white'
            }`}
          >
            Öğrenilecekler ({moduleTotal - moduleLearnedCount})
          </button>
          <button
            onClick={() => setFilterMode('learned')}
            className={`px-3 py-1.5 rounded-lg font-bold transition-all ${
              filterMode === 'learned' ? 'bg-emerald-600 text-white shadow-sm font-black' : 'text-slate-600 dark:text-slate-400 hover:text-slate-900 dark:hover:text-white'
            }`}
          >
            Öğrenilenler ({moduleLearnedCount})
          </button>
          <button
            onClick={() => setFilterMode('starred')}
            className={`px-3 py-1.5 rounded-lg font-bold transition-all flex items-center gap-1 ${
              filterMode === 'starred' ? 'bg-amber-400 text-slate-950 shadow-sm font-black' : 'text-slate-600 dark:text-slate-400 hover:text-slate-900 dark:hover:text-white'
            }`}
          >
            <Star className="w-3.5 h-3.5" />
            <span>Yıldızlılar</span>
          </button>
        </div>

        <button
          onClick={() => setIsShuffled(!isShuffled)}
          className={`flex items-center gap-1.5 px-3 py-1.5 rounded-lg font-mono font-bold transition-all border ${
            isShuffled
              ? 'bg-teal-500/20 text-teal-700 dark:text-teal-300 border-teal-500/40'
              : 'bg-slate-50 dark:bg-fintech-card text-slate-600 dark:text-slate-400 border-slate-200 dark:border-fintech-border hover:text-slate-900 dark:hover:text-white'
          }`}
        >
          <Shuffle className="w-3.5 h-3.5" />
          <span>{isShuffled ? 'Karışık Sıra Açık' : 'Sırayla'}</span>
        </button>
      </div>

      {/* Main Flashcard View */}
      {currentCard ? (
        <div className="space-y-6">
          {/* Card Counter and Status */}
          <div className="flex items-center justify-between px-2 text-xs font-mono text-slate-500 dark:text-slate-400">
            <span>Kart {currentIndex + 1} / {total}</span>
            <span className="text-teal-600 dark:text-teal-400 font-semibold">{currentCard.chapter}</span>
          </div>

          {/* 3D Interactive Flip Card Box */}
          <div
            onClick={() => setIsFlipped(!isFlipped)}
            className="w-full min-h-[380px] sm:min-h-[420px] bg-gradient-to-br from-white via-slate-50 to-slate-100 dark:from-slate-900 dark:via-fintech-surface dark:to-slate-900 rounded-3xl border border-slate-200 dark:border-teal-500/30 hover:border-teal-500/60 p-5 sm:p-8 shadow-lg cursor-pointer select-none transition-all duration-300 relative flex flex-col justify-between group hover:shadow-teal-500/10"
          >
            {/* Top Row on Card */}
            <div className="flex items-center justify-between gap-3">
              <div className="flex items-center gap-2">
                <span className="px-3 py-1 rounded-xl bg-teal-500/15 text-teal-700 dark:text-teal-400 border border-teal-500/30 font-mono text-xs font-bold">
                  Modül {currentCard.module_id}
                </span>
                <span className="px-3 py-1 rounded-xl bg-slate-100 dark:bg-slate-800 text-slate-700 dark:text-slate-300 font-mono text-xs border border-slate-200 dark:border-slate-700">
                  Kart #{currentCard.number}
                </span>
                {isCardLearned(currentCard.id) && (
                  <span className="px-2.5 py-1 rounded-xl bg-emerald-500/20 text-emerald-700 dark:text-emerald-300 border border-emerald-500/40 font-mono text-xs font-bold flex items-center gap-1">
                    <CheckCircle2 className="w-3.5 h-3.5" /> Öğrenildi
                  </span>
                )}
              </div>

              <div className="flex items-center gap-2" onClick={(e) => e.stopPropagation()}>
                <button
                  onClick={() => toggleStarredCard(currentCard.id)}
                  className={`p-2.5 rounded-xl border transition-all ${
                    isCardStarred(currentCard.id)
                      ? 'bg-amber-500/20 text-amber-500 dark:text-amber-400 border-amber-500/40'
                      : 'bg-slate-100 dark:bg-slate-800 text-slate-400 hover:text-amber-500 dark:hover:text-amber-300 border-slate-200 dark:border-slate-700'
                  }`}
                  title="Kartı Yıldızla"
                >
                  <Star className={`w-4 h-4 ${isCardStarred(currentCard.id) ? 'fill-amber-400' : ''}`} />
                </button>

                <button
                  onClick={() => setIsFlipped(!isFlipped)}
                  className="flex items-center gap-1.5 px-3 py-2 rounded-xl bg-white dark:bg-fintech-card hover:bg-slate-50 dark:hover:bg-fintech-cardHover text-slate-700 dark:text-slate-300 text-xs border border-slate-200 dark:border-fintech-border shadow-sm"
                >
                  <RotateCw className="w-3.5 h-3.5 text-teal-600 dark:text-teal-400" />
                  <span>{isFlipped ? 'Ön Yüz' : 'Çevir'}</span>
                </button>
              </div>
            </div>

            {/* Middle Content */}
            {!isFlipped ? (
              /* FRONT FACE */
              <div className="text-center py-8 sm:py-12 space-y-4 my-auto">
                <span className="text-xs font-mono text-slate-500 dark:text-slate-400 uppercase tracking-wider block">
                  Kavram / Soru Başlığı
                </span>
                <h2 className="text-xl sm:text-2xl md:text-3xl font-black text-slate-900 dark:text-white tracking-tight leading-snug max-w-2xl mx-auto">
                  {currentCard.title}
                </h2>
                <p className="text-xs text-teal-600 dark:text-teal-400/80 font-mono pt-4 flex items-center justify-center gap-2">
                  <RotateCw className="w-3.5 h-3.5 animate-spin-slow" />
                  <span>Tanım, örnek ve sınav tuzağını görmek için karta tıklayın (veya Space)</span>
                </p>
              </div>
            ) : (
              /* BACK FACE */
              <div className="py-4 space-y-4 my-auto animate-fade-in text-left text-xs sm:text-sm leading-relaxed">
                {/* Definition */}
                {currentCard.definition && (
                  <div className="bg-white/90 dark:bg-fintech-card/80 p-4 rounded-2xl border border-slate-200 dark:border-fintech-border space-y-1 shadow-sm">
                    <span className="font-mono text-[11px] font-bold text-teal-600 dark:text-teal-400 uppercase tracking-wider block flex items-center gap-1.5">
                      <BookOpen className="w-3.5 h-3.5" />
                      <span>Temel Tanım & Mantık</span>
                    </span>
                    <p className="text-slate-800 dark:text-slate-200">{currentCard.definition}</p>
                  </div>
                )}

                {/* Example */}
                {currentCard.example && (
                  <div className="bg-emerald-50 dark:bg-emerald-950/20 p-4 rounded-2xl border border-emerald-200 dark:border-emerald-500/30 space-y-1 shadow-sm">
                    <span className="font-mono text-[11px] font-bold text-emerald-700 dark:text-emerald-400 uppercase tracking-wider block flex items-center gap-1.5">
                      <Lightbulb className="w-3.5 h-3.5 text-amber-500 dark:text-amber-400" />
                      <span>Akılda Kalıcı Somut Örnek</span>
                    </span>
                    <p className="text-emerald-900 dark:text-emerald-100/90">{currentCard.example}</p>
                  </div>
                )}

                {/* Trap */}
                {currentCard.trap && (
                  <div className="bg-amber-50 dark:bg-amber-950/25 p-4 rounded-2xl border border-amber-200 dark:border-amber-500/40 space-y-1 shadow-sm">
                    <span className="font-mono text-[11px] font-bold text-amber-700 dark:text-amber-400 uppercase tracking-wider block flex items-center gap-1.5">
                      <AlertTriangle className="w-3.5 h-3.5 text-amber-500 dark:text-amber-400" />
                      <span>Sınav Tuzağı & Kritik Ayrım</span>
                    </span>
                    <p className="text-amber-900 dark:text-amber-200/90">{currentCard.trap}</p>
                  </div>
                )}
              </div>
            )}

            {/* Bottom Footer on Card */}
            <div className="flex items-center justify-between border-t border-slate-200 dark:border-fintech-border/60 pt-4 text-xs text-slate-500 dark:text-slate-400 font-mono">
              <span>Boşluk (Space): Kartı Çevir</span>
              <span>← / → : Önceki / Sonraki Kart</span>
            </div>
          </div>

          {/* Navigation & Learning Actions Bar */}
          <div className="flex flex-col sm:flex-row items-center justify-between gap-4 pt-2">
            <button
              onClick={handlePrev}
              className="w-full sm:w-auto min-h-[48px] flex items-center justify-center gap-2 px-6 py-3 rounded-2xl bg-white hover:bg-slate-50 dark:bg-fintech-surface dark:hover:bg-fintech-card border border-slate-200 dark:border-fintech-border text-slate-700 dark:text-slate-200 hover:text-slate-900 dark:hover:text-white text-xs font-bold transition-all shadow-sm"
            >
              <ArrowLeft className="w-4 h-4" />
              <span>Önceki Kart</span>
            </button>

            <div className="flex items-center gap-3 w-full sm:w-auto justify-center">
              <button
                onClick={() => {
                  if (isCardLearned(currentCard.id)) {
                    toggleLearnedCard(currentCard.id);
                  }
                  handleNext();
                }}
                className={`flex-1 sm:flex-initial flex items-center justify-center gap-2 px-5 py-3 rounded-2xl border text-xs font-bold transition-all ${
                  !isCardLearned(currentCard.id)
                    ? 'bg-amber-500/15 text-amber-700 dark:text-amber-300 border-amber-500/40'
                    : 'bg-slate-100 dark:bg-fintech-card text-slate-600 dark:text-slate-400 border-slate-200 dark:border-fintech-border hover:text-slate-900 dark:hover:text-white'
                }`}
              >
                <XCircle className="w-4 h-4" />
                <span>Tekrar Et (1)</span>
              </button>

              <button
                onClick={() => {
                  if (!isCardLearned(currentCard.id)) {
                    toggleLearnedCard(currentCard.id);
                  }
                  handleNext();
                }}
                className={`flex-1 sm:flex-initial flex items-center justify-center gap-2 px-6 py-3 rounded-2xl border text-xs font-black transition-all ${
                  isCardLearned(currentCard.id)
                    ? 'bg-emerald-600 text-white border-emerald-700 shadow-md shadow-emerald-700/20'
                    : 'bg-emerald-500/20 text-emerald-700 dark:text-emerald-300 border-emerald-500/40 hover:bg-emerald-500/30'
                }`}
              >
                <CheckCircle2 className="w-4 h-4" />
                <span>Öğrendim (2)</span>
              </button>
            </div>

            <button
              onClick={handleNext}
              className="w-full sm:w-auto min-h-[48px] flex items-center justify-center gap-2 px-6 py-3 rounded-2xl bg-teal-600 hover:bg-teal-700 active:bg-teal-800 text-white text-xs font-black shadow-md shadow-teal-700/20 active:scale-95 transition-all cursor-pointer"
            >
              <span className="text-white font-black">Sonraki Kart</span>
              <ArrowRight className="w-4 h-4 text-white" />
            </button>
          </div>
        </div>
      ) : (
        <div className="bg-white dark:bg-fintech-surface rounded-2xl border border-slate-200 dark:border-fintech-border p-12 text-center space-y-3 shadow-sm">
          <h3 className="text-base font-bold text-slate-900 dark:text-white">Seçili Kriterde Kart Bulunamadı</h3>
          <p className="text-xs text-slate-600 dark:text-slate-400">
            Filtre seçeneklerinizi değiştirerek diğer kartları inceleyebilirsiniz.
          </p>
        </div>
      )}
    </div>
  );
};
