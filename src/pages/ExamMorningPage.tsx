import React, { useState, useEffect, useMemo, useRef } from 'react';
import { 
  Zap, 
  Clock, 
  RotateCw, 
  ArrowLeft, 
  ArrowRight, 
  CheckCircle2, 
  AlertCircle, 
  Headphones, 
  Play, 
  Pause, 
  RotateCcw, 
  Layers, 
  List, 
  Sparkles, 
  BookOpen, 
  ShieldCheck, 
  Coins, 
  Scale, 
  Building2, 
  ChevronRight,
  Filter,
  Volume2,
  VolumeX,
  Star
} from 'lucide-react';
import { EXAM_MORNING_CARDS, ExamMorningCard, ExamMorningCategory } from '../data/examMorningData';
import { ModuleId } from '../types/exam';
import { useAudioStore } from '../stores/audioStore';

interface ExamMorningPageProps {
  onNavigate: (page: string, params?: any) => void;
  initialModuleId?: ModuleId | 'all';
}

export const ExamMorningPage: React.FC<ExamMorningPageProps> = ({ 
  onNavigate, 
  initialModuleId = 'all' 
}) => {
  const [selectedModule, setSelectedModule] = useState<ModuleId | 'all'>(initialModuleId);
  const [selectedCategory, setSelectedCategory] = useState<ExamMorningCategory | 'all'>('all');
  const [viewMode, setViewMode] = useState<'cards' | 'list'>('cards');
  const [currentIndex, setCurrentIndex] = useState(0);
  const [isFlipped, setIsFlipped] = useState(false);
  
  // Progress tracking
  const [rememberedIds, setRememberedIds] = useState<Set<string>>(new Set());
  const [reviewIds, setReviewIds] = useState<Set<string>>(new Set());
  const [onlyReviewFilter, setOnlyReviewFilter] = useState(false);

  // 15-Minute Exam Countdown Timer
  const [timeLeftSeconds, setTimeLeftSeconds] = useState(15 * 60); // 15 minutes
  const [isTimerRunning, setIsTimerRunning] = useState(false);

  // Audio store for hands-free reading
  const { playSection, stop: stopAudio, isPlaying, currentSentenceIndex } = useAudioStore();

  // Timer effect
  useEffect(() => {
    let interval: NodeJS.Timeout | null = null;
    if (isTimerRunning && timeLeftSeconds > 0) {
      interval = setInterval(() => {
        setTimeLeftSeconds((prev) => Math.max(0, prev - 1));
      }, 1000);
    } else if (timeLeftSeconds === 0) {
      setIsTimerRunning(false);
    }
    return () => {
      if (interval) clearInterval(interval);
    };
  }, [isTimerRunning, timeLeftSeconds]);

  const formatTimer = (seconds: number) => {
    const mins = Math.floor(seconds / 60);
    const secs = seconds % 60;
    return `${mins.toString().padStart(2, '0')}:${secs.toString().padStart(2, '0')}`;
  };

  // Filtered Cards
  const filteredCards = useMemo(() => {
    return EXAM_MORNING_CARDS.filter((card) => {
      if (selectedModule !== 'all' && card.moduleId !== selectedModule) return false;
      if (selectedCategory !== 'all' && card.category !== selectedCategory) return false;
      if (onlyReviewFilter && !reviewIds.has(card.id)) return false;
      return true;
    });
  }, [selectedModule, selectedCategory, onlyReviewFilter, reviewIds]);

  const currentCard: ExamMorningCard | undefined = filteredCards[currentIndex];

  // Reset current index when filter changes
  useEffect(() => {
    setCurrentIndex(0);
    setIsFlipped(false);
  }, [selectedModule, selectedCategory, onlyReviewFilter]);

  // Keyboard navigation
  useEffect(() => {
    const handleKeyDown = (e: KeyboardEvent) => {
      // Don't trigger if typing in an input
      if (['INPUT', 'TEXTAREA'].includes((e.target as HTMLElement).tagName)) return;

      if (e.code === 'Space') {
        e.preventDefault();
        setIsFlipped((prev) => !prev);
      } else if (e.key === 'ArrowRight') {
        handleNext();
      } else if (e.key === 'ArrowLeft') {
        handlePrev();
      } else if (e.key === '1') {
        if (currentCard) handleMarkRemembered(currentCard.id);
      } else if (e.key === '2') {
        if (currentCard) handleMarkReview(currentCard.id);
      }
    };

    window.addEventListener('keydown', handleKeyDown);
    return () => window.removeEventListener('keydown', handleKeyDown);
  }, [filteredCards, currentIndex, currentCard]);

  const handleNext = () => {
    if (filteredCards.length === 0) return;
    setIsFlipped(false);
    setCurrentIndex((prev) => (prev + 1) % filteredCards.length);
  };

  const handlePrev = () => {
    if (filteredCards.length === 0) return;
    setIsFlipped(false);
    setCurrentIndex((prev) => (prev - 1 + filteredCards.length) % filteredCards.length);
  };

  const handleMarkRemembered = (id: string) => {
    setRememberedIds((prev) => {
      const next = new Set(prev);
      next.add(id);
      return next;
    });
    setReviewIds((prev) => {
      const next = new Set(prev);
      next.delete(id);
      return next;
    });
    handleNext();
  };

  const handleMarkReview = (id: string) => {
    setReviewIds((prev) => {
      const next = new Set(prev);
      next.add(id);
      return next;
    });
    setRememberedIds((prev) => {
      const next = new Set(prev);
      next.delete(id);
      return next;
    });
    handleNext();
  };

  // Hands-free Audio Walk Mode: Reads the filtered cards out loud in sequence
  const handleStartAudioWalk = () => {
    if (filteredCards.length === 0) return;
    
    // Prepare audio script from cards
    const paragraphs: string[] = [];
    filteredCards.forEach((c, idx) => {
      paragraphs.push(`Kart ${idx + 1}. ${c.frontTitle}. ${c.frontQuestion}`);
      paragraphs.push(`Cevap: ${c.keyHighlight}. ${c.backRule}`);
      if (c.trapNote) {
        paragraphs.push(`Sınav Tuzağı uyarısı: ${c.trapNote}`);
      }
    });

    playSection({
      moduleId: selectedModule === 'all' ? '1001' : selectedModule,
      sectionId: 'exam_morning_walk',
      title: `Sınav Sabahı Sesli Tekrar (${filteredCards.length} Kart)`,
      paragraphs,
    });
  };

  const modulesList: { id: ModuleId | 'all'; name: string; icon: any; count: number }[] = [
    { id: 'all', name: 'Tüm Modüller', icon: Sparkles, count: EXAM_MORNING_CARDS.length },
    { id: '1001', name: '1001 Mevzuat', icon: Scale, count: EXAM_MORNING_CARDS.filter(c => c.moduleId === '1001').length },
    { id: '1003', name: '1003 SP Araçları', icon: Coins, count: EXAM_MORNING_CARDS.filter(c => c.moduleId === '1003').length },
    { id: '1005', name: '1005 Yatırım Kur.', icon: Building2, count: EXAM_MORNING_CARDS.filter(c => c.moduleId === '1005').length },
    { id: '1012', name: '1012 Takas/Saklama', icon: ShieldCheck, count: EXAM_MORNING_CARDS.filter(c => c.moduleId === '1012').length },
  ];

  const categoriesList: { id: ExamMorningCategory | 'all'; label: string }[] = [
    { id: 'all', label: 'Tüm Konular' },
    { id: 'duration', label: '⏱️ Süreler' },
    { id: 'ratio', label: '📊 Oranlar & Eşikler' },
    { id: 'penalty', label: '⚖️ Suçlar & Cezalar' },
    { id: 'comparison', label: '💡 Altın Ayrımlar' },
    { id: 'trap', label: '⚠️ Sınav Tuzakları' },
  ];

  return (
    <div className="space-y-6 animate-fade-in pb-16 max-w-6xl mx-auto">
      {/* Top Banner & 15-Minute Countdown */}
      <div className="relative overflow-hidden rounded-3xl bg-gradient-to-r from-amber-500 via-orange-500 to-rose-600 text-white p-6 sm:p-8 shadow-xl">
        <div className="absolute top-0 right-0 -mt-10 -mr-10 w-64 h-64 bg-white/10 rounded-full blur-3xl pointer-events-none" />
        <div className="absolute bottom-0 left-1/4 -mb-10 w-64 h-64 bg-black/10 rounded-full blur-3xl pointer-events-none" />

        <div className="relative z-10 flex flex-col md:flex-row items-start md:items-center justify-between gap-6">
          <div className="space-y-2 max-w-2xl">
            <div className="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-white/20 backdrop-blur-md text-white text-xs font-mono font-black uppercase tracking-wider border border-white/30">
              <Zap className="w-3.5 h-3.5 fill-white text-white animate-pulse" />
              <span>Sınav Sabahı Acil Durum Modu</span>
            </div>
            <h1 className="text-2xl sm:text-3xl lg:text-4xl font-black tracking-tight leading-tight text-white">
              Son 15 Dakika Hap Bilgi Kartları
            </h1>
            <p className="text-xs sm:text-sm text-white/90 leading-relaxed font-medium">
              Sınav salonu kapısına varmadan önce zihnini netleştir! En çok unutulan süreler, kilit oranlar, suç/cezalar ve sınav komisyonunun en sevdiği ölümcül çeldiriciler.
            </p>
          </div>

          {/* 15-Minute Focus Timer Widget */}
          <div className="bg-black/30 backdrop-blur-md border border-white/30 rounded-2xl p-4 flex flex-col items-center justify-center min-w-[200px] shrink-0 text-center shadow-inner">
            <span className="text-[11px] font-mono text-white/80 uppercase font-bold tracking-wider mb-1 flex items-center gap-1.5">
              <Clock className="w-3.5 h-3.5 text-amber-300" />
              Sınav Kapısına Kalan
            </span>
            <div className="text-3xl sm:text-4xl font-black font-mono tracking-wider text-amber-300 my-0.5">
              {formatTimer(timeLeftSeconds)}
            </div>
            <div className="flex items-center gap-2 mt-2">
              <button
                onClick={() => setIsTimerRunning(!isTimerRunning)}
                className="px-3 py-1 rounded-lg bg-white/20 hover:bg-white/30 active:scale-95 text-xs font-bold transition-all flex items-center gap-1 cursor-pointer"
                title={isTimerRunning ? 'Sayacı Duraklat' : 'Sayacı Başlat'}
              >
                {isTimerRunning ? <Pause className="w-3 h-3" /> : <Play className="w-3 h-3 fill-white" />}
                <span>{isTimerRunning ? 'Durdur' : 'Başlat'}</span>
              </button>
              <button
                onClick={() => {
                  setIsTimerRunning(false);
                  setTimeLeftSeconds(15 * 60);
                }}
                className="p-1.5 rounded-lg bg-white/10 hover:bg-white/20 active:scale-95 text-xs transition-all cursor-pointer"
                title="15 Dakikaya Sıfırla"
              >
                <RotateCcw className="w-3 h-3 text-white/80" />
              </button>
            </div>
          </div>
        </div>
      </div>

      {/* Control Bar: Mode Toggle & Audio Readout */}
      <div className="bg-white dark:bg-fintech-surface rounded-2xl border border-slate-200 dark:border-fintech-border p-4 shadow-sm flex flex-wrap items-center justify-between gap-4">
        {/* View Mode Buttons */}
        <div className="flex items-center gap-2 bg-slate-100 dark:bg-fintech-card p-1 rounded-xl border border-slate-200 dark:border-fintech-border">
          <button
            onClick={() => setViewMode('cards')}
            className={`flex items-center gap-2 px-3 py-1.5 rounded-lg text-xs font-bold transition-all cursor-pointer ${
              viewMode === 'cards'
                ? 'bg-white dark:bg-teal-600 text-slate-900 dark:text-white shadow-xs'
                : 'text-slate-600 dark:text-slate-400 hover:text-slate-900 dark:hover:text-white'
            }`}
          >
            <Layers className="w-4 h-4 text-amber-500" />
            <span>🎴 Seri Kart Akışı</span>
          </button>
          <button
            onClick={() => setViewMode('list')}
            className={`flex items-center gap-2 px-3 py-1.5 rounded-lg text-xs font-bold transition-all cursor-pointer ${
              viewMode === 'list'
                ? 'bg-white dark:bg-teal-600 text-slate-900 dark:text-white shadow-xs'
                : 'text-slate-600 dark:text-slate-400 hover:text-slate-900 dark:hover:text-white'
            }`}
          >
            <List className="w-4 h-4 text-teal-500" />
            <span>⚡ Tek Sayfa Hızlı Liste</span>
          </button>
        </div>

        {/* Audio Walk Button (Hands-free TTS) */}
        <div className="flex items-center gap-2">
          <button
            onClick={isPlaying ? stopAudio : handleStartAudioWalk}
            className={`flex items-center gap-2 px-4 py-2 rounded-xl text-xs font-bold transition-all shadow-sm cursor-pointer ${
              isPlaying
                ? 'bg-rose-500 text-white hover:bg-rose-600'
                : 'bg-gradient-to-r from-teal-600 to-emerald-600 text-white hover:opacity-95'
            }`}
            title="Kulaklıkla bekleyenler için kartları otomatik Türkçe seslendirir"
          >
            <Headphones className="w-4 h-4" />
            <span>{isPlaying ? '⏹️ Sesli Okumayı Durdur' : '🎧 Kulaklıkla Dinle (Hands-free)'}</span>
          </button>

          {/* Quick Review Filter */}
          <button
            onClick={() => setOnlyReviewFilter(!onlyReviewFilter)}
            className={`flex items-center gap-1.5 px-3 py-2 rounded-xl text-xs font-bold border transition-all cursor-pointer ${
              onlyReviewFilter
                ? 'bg-rose-50 border-rose-300 text-rose-700 dark:bg-rose-950/40 dark:border-rose-500/40 dark:text-rose-300'
                : 'bg-slate-50 border-slate-200 text-slate-700 dark:bg-fintech-card dark:border-fintech-border dark:text-slate-300 hover:bg-slate-100'
            }`}
          >
            <AlertCircle className="w-3.5 h-3.5 text-rose-500" />
            <span>Tekrar Edilecekler ({reviewIds.size})</span>
          </button>
        </div>
      </div>

      {/* Module Selector Tabs */}
      <div className="flex items-center gap-2 overflow-x-auto pb-1 scrollbar-none">
        {modulesList.map((m) => {
          const Icon = m.icon;
          const isSelected = selectedModule === m.id;
          return (
            <button
              key={m.id}
              onClick={() => setSelectedModule(m.id)}
              className={`flex items-center gap-2 px-3.5 py-2 rounded-xl text-xs font-bold whitespace-nowrap transition-all cursor-pointer border ${
                isSelected
                  ? 'bg-amber-500 text-slate-950 border-amber-600 shadow-sm font-black'
                  : 'bg-white dark:bg-fintech-surface text-slate-700 dark:text-slate-300 border-slate-200 dark:border-fintech-border hover:bg-slate-50 dark:hover:bg-fintech-card'
              }`}
            >
              <Icon className="w-3.5 h-3.5" />
              <span>{m.name}</span>
              <span className={`text-[10px] font-mono px-1.5 py-0.2 rounded-full ${
                isSelected ? 'bg-slate-950/20 text-slate-950' : 'bg-slate-100 dark:bg-fintech-card text-slate-500 dark:text-slate-400'
              }`}>
                {m.count}
              </span>
            </button>
          );
        })}
      </div>

      {/* Category Pills */}
      <div className="flex items-center gap-1.5 overflow-x-auto pb-1 scrollbar-none">
        {categoriesList.map((c) => {
          const isSelected = selectedCategory === c.id;
          return (
            <button
              key={c.id}
              onClick={() => setSelectedCategory(c.id)}
              className={`px-3 py-1 rounded-lg text-xs font-semibold whitespace-nowrap transition-all cursor-pointer ${
                isSelected
                  ? 'bg-slate-900 text-white dark:bg-teal-500 dark:text-slate-950 font-bold'
                  : 'bg-slate-100 dark:bg-fintech-card text-slate-600 dark:text-slate-400 hover:bg-slate-200 dark:hover:bg-slate-800'
              }`}
            >
              {c.label}
            </button>
          );
        })}
      </div>

      {/* Main Content Area */}
      {filteredCards.length === 0 ? (
        <div className="bg-white dark:bg-fintech-surface rounded-2xl border border-slate-200 dark:border-fintech-border p-12 text-center text-slate-500 dark:text-slate-400 space-y-3">
          <AlertCircle className="w-10 h-10 text-amber-500 mx-auto" />
          <h3 className="text-base font-bold text-slate-800 dark:text-slate-200">Seçilen Kriterde Kart Bulunamadı</h3>
          <p className="text-xs">Filtreleri temizleyerek tüm hap kartları inceleyebilirsiniz.</p>
          <button
            onClick={() => {
              setSelectedModule('all');
              setSelectedCategory('all');
              setOnlyReviewFilter(false);
            }}
            className="px-4 py-2 rounded-xl bg-teal-600 text-white text-xs font-bold cursor-pointer"
          >
            Filtreleri Sıfırla
          </button>
        </div>
      ) : viewMode === 'cards' ? (
        /* ========================================================= */
        /* MODE 1: TACTILE 3D FLIP FLASHCARD VIEW                    */
        /* ========================================================= */
        <div className="space-y-4">
          {/* Card Counter & Progress */}
          <div className="flex items-center justify-between text-xs text-slate-500 dark:text-slate-400 font-mono">
            <div className="flex items-center gap-2">
              <span className="font-bold text-slate-800 dark:text-slate-200">
                Kart {currentIndex + 1} / {filteredCards.length}
              </span>
              <span className="text-[10px] text-teal-600 dark:text-teal-400">
                ({rememberedIds.size} Aklımda • {reviewIds.size} Tekrar)
              </span>
            </div>
            <div className="hidden sm:flex items-center gap-3 text-[11px]">
              <span>[Space]: Çevir</span>
              <span>[←/→]: İlerle</span>
              <span>[1]: Aklımda</span>
              <span>[2]: Tekrar</span>
            </div>
          </div>

          {/* Card Container with Perspective */}
          {currentCard && (
            <div 
              onClick={() => setIsFlipped(!isFlipped)}
              className="relative min-h-[380px] sm:min-h-[420px] rounded-3xl cursor-pointer select-none transition-all duration-300 perspective-1000 group"
            >
              <div className={`w-full min-h-[380px] sm:min-h-[420px] rounded-3xl border transition-all duration-500 flex flex-col justify-between p-6 sm:p-8 shadow-lg ${
                isFlipped
                  ? 'bg-slate-900 border-amber-500/50 text-white ring-2 ring-amber-500/20'
                  : 'bg-white dark:bg-fintech-surface border-slate-200 dark:border-teal-500/30 text-slate-900 dark:text-white hover:border-teal-500/50'
              }`}>
                {/* Card Top Metadata Bar */}
                <div className="flex items-center justify-between">
                  <div className="flex items-center gap-2">
                    <span className="px-2.5 py-1 rounded-full text-xs font-mono font-bold bg-amber-50 dark:bg-amber-500/10 text-amber-700 dark:text-amber-400 border border-amber-200 dark:border-amber-500/30">
                      {currentCard.categoryLabel}
                    </span>
                    <span className="px-2.5 py-1 rounded-full text-xs font-mono font-bold bg-slate-100 dark:bg-fintech-card text-slate-600 dark:text-slate-300 border border-slate-200 dark:border-fintech-border">
                      Modül {currentCard.moduleId} • {currentCard.moduleName}
                    </span>
                  </div>

                  <div className="flex items-center gap-1.5">
                    {rememberedIds.has(currentCard.id) && (
                      <span className="px-2 py-0.5 rounded-md bg-emerald-50 dark:bg-emerald-500/20 text-emerald-700 dark:text-emerald-300 text-[10px] font-mono font-bold">
                        ✓ Aklımda
                      </span>
                    )}
                    {reviewIds.has(currentCard.id) && (
                      <span className="px-2 py-0.5 rounded-md bg-rose-50 dark:bg-rose-500/20 text-rose-700 dark:text-rose-300 text-[10px] font-mono font-bold">
                        ⚠️ Tekrar
                      </span>
                    )}
                    <span className="text-xs text-slate-400 dark:text-slate-500 flex items-center gap-1">
                      <RotateCw className="w-3.5 h-3.5 group-hover:rotate-180 transition-transform duration-500" />
                      {isFlipped ? 'Ön Yüz' : 'Cevap'}
                    </span>
                  </div>
                </div>

                {/* Card Center Content */}
                {!isFlipped ? (
                  /* FRONT FACE */
                  <div className="my-auto py-6 space-y-4 text-center">
                    <h2 className="text-xl sm:text-2xl font-black text-slate-900 dark:text-white tracking-tight leading-snug">
                      {currentCard.frontTitle}
                    </h2>
                    <p className="text-base sm:text-lg text-slate-600 dark:text-slate-300 font-medium max-w-xl mx-auto leading-relaxed">
                      "{currentCard.frontQuestion}"
                    </p>
                    <div className="pt-4">
                      <span className="inline-flex items-center gap-2 px-4 py-2 rounded-2xl bg-slate-100 dark:bg-fintech-card border border-slate-200 dark:border-fintech-border text-xs text-slate-500 dark:text-slate-400 font-bold group-hover:bg-amber-400 group-hover:text-slate-950 transition-colors">
                        <RotateCw className="w-3.5 h-3.5" />
                        Cevabı ve Kuralı Görmek İçin Dokun
                      </span>
                    </div>
                  </div>
                ) : (
                  /* BACK FACE (GOLDEN ANSWER & TRAP) */
                  <div className="my-auto py-4 space-y-4 animate-fade-in">
                    {/* Golden Highlighted Metric / Answer */}
                    <div className="p-4 rounded-2xl bg-amber-500/20 border-2 border-amber-400 text-center shadow-inner">
                      <span className="text-[11px] font-mono text-amber-300 uppercase tracking-widest block font-bold mb-1">
                        Kilit Sayı / Hüküm
                      </span>
                      <span className="text-2xl sm:text-3xl font-black text-amber-300 tracking-wide font-mono">
                        {currentCard.keyHighlight}
                      </span>
                    </div>

                    {/* Legal Rule Explanation */}
                    <div className="p-4 rounded-2xl bg-slate-800/80 border border-slate-700 text-slate-200 text-sm sm:text-base leading-relaxed">
                      <span className="font-bold text-teal-400 block text-xs uppercase font-mono mb-1">Kanuni Kural:</span>
                      {currentCard.backRule}
                    </div>

                    {/* Dedicated Exam Trap Warning */}
                    {currentCard.trapNote && (
                      <div className="p-3.5 rounded-2xl bg-rose-950/40 border border-rose-500/40 text-rose-200 text-xs sm:text-sm leading-relaxed flex items-start gap-2.5">
                        <AlertCircle className="w-4 h-4 text-rose-400 shrink-0 mt-0.5" />
                        <div>
                          <strong className="text-rose-400 font-black block mb-0.5">Sınav Çeldirici Tuzağı:</strong>
                          {currentCard.trapNote}
                        </div>
                      </div>
                    )}
                  </div>
                )}

                {/* Card Bottom Controls */}
                <div className="pt-4 border-t border-slate-100 dark:border-fintech-border/50 flex items-center justify-between gap-4">
                  <div className="flex items-center gap-2">
                    <button
                      onClick={(e) => {
                        e.stopPropagation();
                        handleMarkRemembered(currentCard.id);
                      }}
                      className="flex items-center gap-1.5 px-3 py-1.5 rounded-xl bg-emerald-50 hover:bg-emerald-100 text-emerald-700 dark:bg-emerald-500/20 dark:hover:bg-emerald-500/30 dark:text-emerald-300 text-xs font-bold transition-all cursor-pointer"
                    >
                      <CheckCircle2 className="w-3.5 h-3.5" />
                      <span>Aklımda</span>
                    </button>
                    <button
                      onClick={(e) => {
                        e.stopPropagation();
                        handleMarkReview(currentCard.id);
                      }}
                      className="flex items-center gap-1.5 px-3 py-1.5 rounded-xl bg-rose-50 hover:bg-rose-100 text-rose-700 dark:bg-rose-500/20 dark:hover:bg-rose-500/30 dark:text-rose-300 text-xs font-bold transition-all cursor-pointer"
                    >
                      <AlertCircle className="w-3.5 h-3.5" />
                      <span>Tekrar Göster</span>
                    </button>
                  </div>

                  <div className="flex items-center gap-2">
                    <button
                      onClick={(e) => {
                        e.stopPropagation();
                        handlePrev();
                      }}
                      className="p-2 rounded-xl bg-slate-100 hover:bg-slate-200 dark:bg-fintech-card dark:hover:bg-slate-800 text-slate-700 dark:text-slate-300 transition-all cursor-pointer"
                      title="Önceki Kart (Sol Ok)"
                    >
                      <ArrowLeft className="w-4 h-4" />
                    </button>
                    <button
                      onClick={(e) => {
                        e.stopPropagation();
                        handleNext();
                      }}
                      className="p-2 rounded-xl bg-slate-100 hover:bg-slate-200 dark:bg-fintech-card dark:hover:bg-slate-800 text-slate-700 dark:text-slate-300 transition-all cursor-pointer"
                      title="Sonraki Kart (Sağ Ok)"
                    >
                      <ArrowRight className="w-4 h-4" />
                    </button>
                  </div>
                </div>
              </div>
            </div>
          )}
        </div>
      ) : (
        /* ========================================================= */
        /* MODE 2: RAPID LIST MATRIX VIEW                            */
        /* ========================================================= */
        <div className="space-y-4">
          <div className="flex items-center justify-between pb-2 border-b border-slate-200 dark:border-fintech-border">
            <span className="text-xs font-mono font-bold text-slate-500 dark:text-slate-400 uppercase">
              Toplam {filteredCards.length} Hap Kural Listeleniyor
            </span>
            <span className="text-xs text-slate-400">Hızlı göz gezdirme modu</span>
          </div>

          <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
            {filteredCards.map((card, idx) => (
              <div
                key={card.id}
                className="bg-white dark:bg-fintech-surface rounded-2xl border border-slate-200 dark:border-fintech-border p-5 space-y-3 shadow-xs hover:border-amber-500/40 transition-all"
              >
                <div className="flex items-start justify-between gap-2">
                  <div className="flex items-center gap-2">
                    <span className="text-xs font-mono font-black text-amber-600 dark:text-amber-400">
                      #{idx + 1}
                    </span>
                    <span className="text-[11px] font-mono px-2 py-0.5 rounded-full bg-slate-100 dark:bg-fintech-card text-slate-600 dark:text-slate-400 font-bold">
                      Modül {card.moduleId}
                    </span>
                    <span className="text-[11px] font-mono text-slate-500 dark:text-slate-400">
                      {card.categoryLabel}
                    </span>
                  </div>
                  <span className="px-2 py-0.5 rounded-md bg-amber-50 dark:bg-amber-500/15 text-amber-800 dark:text-amber-300 font-mono text-xs font-black border border-amber-200 dark:border-amber-500/30">
                    {card.keyHighlight}
                  </span>
                </div>

                <div>
                  <h3 className="text-sm font-black text-slate-900 dark:text-white leading-snug">
                    {card.frontTitle}
                  </h3>
                  <p className="text-xs text-slate-600 dark:text-slate-300 mt-1 leading-relaxed">
                    {card.backRule}
                  </p>
                </div>

                {card.trapNote && (
                  <div className="p-2.5 rounded-xl bg-rose-50 dark:bg-rose-950/30 border border-rose-200 dark:border-rose-500/30 text-[11px] text-rose-900 dark:text-rose-200 leading-relaxed">
                    <span className="font-bold text-rose-700 dark:text-rose-400 block mb-0.5">⚠️ Sınav Notu:</span>
                    {card.trapNote}
                  </div>
                )}
              </div>
            ))}
          </div>
        </div>
      )}

      {/* Bottom Cross-Navigation Card */}
      <div className="rounded-2xl bg-slate-50 dark:bg-fintech-surface border border-slate-200 dark:border-fintech-border p-6 flex flex-col sm:flex-row items-center justify-between gap-4 shadow-sm">
        <div>
          <h4 className="text-sm font-black text-slate-900 dark:text-white">Daha Kapsamlı Notlara mı İhtiyacın Var?</h4>
          <p className="text-xs text-slate-600 dark:text-slate-400">115 maddelik detaylı CheatSheet tablosunu inceleyebilir veya 935 soruluk soru havuzunda test çözebilirsin.</p>
        </div>

        <div className="flex flex-wrap items-center gap-3 w-full sm:w-auto">
          <button
            onClick={() => onNavigate('cheat-sheet')}
            className="flex-1 sm:flex-initial flex items-center justify-center gap-2 px-4 py-2.5 rounded-xl bg-white dark:bg-fintech-card border border-slate-300 dark:border-fintech-border text-slate-800 dark:text-slate-100 text-xs font-bold hover:bg-slate-100 transition-all cursor-pointer"
          >
            <Zap className="w-3.5 h-3.5 text-amber-500" />
            <span>115 Maddelik CheatSheet</span>
          </button>
          <button
            onClick={() => onNavigate('practice', { moduleId: selectedModule === 'all' ? undefined : selectedModule })}
            className="flex-1 sm:flex-initial flex items-center justify-center gap-2 px-5 py-2.5 rounded-xl bg-teal-600 hover:bg-teal-700 active:bg-teal-800 text-white text-xs font-bold transition-all shadow-md shadow-teal-700/20 cursor-pointer"
          >
            <Play className="w-3.5 h-3.5 fill-white text-white" />
            <span>Test Çözmeye Başla</span>
          </button>
        </div>
      </div>
    </div>
  );
};

export default ExamMorningPage;
