import React, { useState } from 'react';
import { 
  Play, 
  Pause, 
  SkipBack, 
  SkipForward, 
  X, 
  Gauge, 
  Headphones,
  ChevronDown,
  ChevronUp
} from 'lucide-react';
import { useAudioStore } from '../../stores/audioStore';

export const AudioPlayerBar: React.FC = () => {
  const {
    isPlaying,
    isPaused,
    title,
    moduleId,
    sentences,
    currentSentenceIndex,
    playbackRate,
    togglePlayPause,
    stop,
    nextSentence,
    prevSentence,
    jumpToSentence,
    setPlaybackRate,
  } = useAudioStore();

  const [isMinimized, setIsMinimized] = useState(false);

  if (!isPlaying && sentences.length === 0) {
    return null;
  }

  const currentSentence = sentences[currentSentenceIndex];
  const progressPercent = sentences.length > 0
    ? Math.round(((currentSentenceIndex + 1) / sentences.length) * 100)
    : 0;

  const speeds = [0.75, 1.0, 1.25, 1.5, 1.75, 2.0];

  // 1. MINIMIZED FLOATING PILL (KÜÇÜK MOD - EKRANI HİÇ KAPLAMAZ)
  if (isMinimized) {
    return (
      <div className="fixed bottom-16 md:bottom-4 right-4 sm:right-6 z-50 flex items-center gap-2 bg-slate-950/95 backdrop-blur-xl border border-teal-500/50 rounded-full px-3 py-1.5 shadow-2xl shadow-teal-950/60 animate-slide-up text-white max-w-[calc(100vw-32px)] select-none">
        {/* Play / Pause button */}
        <button
          onClick={togglePlayPause}
          className="w-7 h-7 rounded-full bg-gradient-to-r from-teal-500 to-emerald-500 text-slate-950 flex items-center justify-center font-bold shadow-md shrink-0 active:scale-95 transition-transform"
          title={isPlaying && !isPaused ? 'Duraklat' : 'Oynat'}
        >
          {isPlaying && !isPaused ? (
            <Pause className="w-3.5 h-3.5 fill-slate-950" />
          ) : (
            <Play className="w-3.5 h-3.5 fill-slate-950 translate-x-0.5" />
          )}
        </button>

        {/* Title */}
        <div className="min-w-0 max-w-[130px] sm:max-w-[200px]">
          <p className="text-xs font-bold text-slate-200 truncate">
            {title}
          </p>
        </div>

        {/* Speed Badge */}
        <span className="font-mono text-[10px] font-bold px-1.5 py-0.5 rounded bg-teal-500/20 text-teal-300 border border-teal-500/30 shrink-0">
          {playbackRate}x
        </span>

        {/* Expand button */}
        <button
          onClick={() => setIsMinimized(false)}
          className="p-1 rounded-full text-slate-400 hover:text-teal-300 hover:bg-slate-800 transition-colors shrink-0"
          title="Oynatıcıyı Genişlet"
        >
          <ChevronUp className="w-4 h-4" />
        </button>

        {/* Close */}
        <button
          onClick={stop}
          className="p-1 rounded-full text-slate-400 hover:text-rose-400 hover:bg-slate-800 transition-colors shrink-0"
          title="Kapat"
        >
          <X className="w-4 h-4" />
        </button>
      </div>
    );
  }

  // 2. EXPANDED COMPACT BAR (TAŞMAYI ÖNLEYEN SIKI VE DÜZENLİ TASARIM)
  return (
    <div className="fixed bottom-16 md:bottom-3 left-1/2 -translate-x-1/2 z-50 w-[calc(100vw-24px)] max-w-2xl bg-slate-950/95 backdrop-blur-2xl border border-teal-500/40 rounded-2xl p-3 shadow-2xl shadow-teal-950/60 animate-slide-up text-white overflow-hidden box-border select-none">
      {/* Clickable Thin Progress Line */}
      <div 
        onClick={(e) => {
          const rect = e.currentTarget.getBoundingClientRect();
          const clickX = e.clientX - rect.left;
          const ratio = clickX / rect.width;
          const targetIndex = Math.min(
            sentences.length - 1,
            Math.max(0, Math.floor(ratio * sentences.length))
          );
          jumpToSentence(targetIndex);
        }}
        className="w-full h-1.5 bg-slate-800/80 rounded-full mb-2 cursor-pointer overflow-hidden relative group"
        title="İlerlemek istediğiniz yere tıklayın"
      >
        <div
          className="h-full bg-gradient-to-r from-teal-500 via-cyan-400 to-emerald-400 transition-all duration-200"
          style={{ width: `${progressPercent}%` }}
        />
        <div className="absolute inset-0 bg-white/15 opacity-0 group-hover:opacity-100 transition-opacity" />
      </div>

      <div className="flex items-center justify-between gap-2 sm:gap-3 min-w-0">
        {/* Left: Animated Icon + Title & Sentence Preview */}
        <div className="flex items-center gap-2 min-w-0 flex-1">
          {/* Animated sound indicator */}
          <div className="w-8 h-8 rounded-xl bg-teal-500/15 border border-teal-500/30 flex items-center justify-center shrink-0">
            {isPlaying && !isPaused ? (
              <div className="flex items-end gap-0.5 h-3">
                <span className="w-0.5 bg-teal-400 rounded-full animate-bounce h-full" style={{ animationDelay: '0ms' }}></span>
                <span className="w-0.5 bg-teal-300 rounded-full animate-bounce h-2/3" style={{ animationDelay: '150ms' }}></span>
                <span className="w-0.5 bg-cyan-400 rounded-full animate-bounce h-5/6" style={{ animationDelay: '300ms' }}></span>
                <span className="w-0.5 bg-emerald-400 rounded-full animate-bounce h-1/2" style={{ animationDelay: '450ms' }}></span>
              </div>
            ) : (
              <Headphones className="w-4 h-4 text-teal-400" />
            )}
          </div>

          <div className="min-w-0 flex-1">
            <div className="flex items-center gap-1.5 min-w-0">
              {moduleId && (
                <span className="font-mono text-[9px] font-bold px-1 rounded bg-teal-500/20 text-teal-300 border border-teal-500/30 shrink-0">
                  {moduleId}
                </span>
              )}
              <h4 className="font-bold text-xs text-white truncate">
                {title}
              </h4>
            </div>
            {currentSentence && (
              <p className="text-[10px] text-slate-400 truncate italic mt-0.5 max-w-full">
                "{currentSentence.originalText}"
              </p>
            )}
          </div>
        </div>

        {/* Center: Playback Controls */}
        <div className="flex items-center gap-1 shrink-0">
          <button
            onClick={prevSentence}
            disabled={currentSentenceIndex === 0}
            className="p-1 rounded-lg text-slate-400 hover:text-white hover:bg-slate-800 transition-all disabled:opacity-25"
            title="Önceki Cümle"
          >
            <SkipBack className="w-3.5 h-3.5" />
          </button>

          {/* Main Play / Pause */}
          <button
            onClick={togglePlayPause}
            className="w-8 h-8 sm:w-9 sm:h-9 rounded-xl bg-gradient-to-r from-teal-500 to-emerald-500 hover:from-teal-400 hover:to-emerald-400 text-slate-950 flex items-center justify-center font-bold shadow-md shadow-teal-500/30 active:scale-95 transition-all shrink-0"
            title={isPlaying && !isPaused ? 'Duraklat' : 'Oynat'}
          >
            {isPlaying && !isPaused ? (
              <Pause className="w-4 h-4 fill-slate-950" />
            ) : (
              <Play className="w-4 h-4 fill-slate-950 translate-x-0.5" />
            )}
          </button>

          <button
            onClick={nextSentence}
            disabled={currentSentenceIndex >= sentences.length - 1}
            className="p-1 rounded-lg text-slate-400 hover:text-white hover:bg-slate-800 transition-all disabled:opacity-25"
            title="Sonraki Cümle"
          >
            <SkipForward className="w-3.5 h-3.5" />
          </button>
        </div>

        {/* Right: Speed, Sentence Counter, Minimize & Close */}
        <div className="flex items-center gap-1.5 shrink-0">
          {/* Speed Selector */}
          <div className="flex items-center gap-1 bg-slate-900/90 px-1.5 py-0.5 rounded-lg border border-slate-800 text-[11px] font-mono">
            <Gauge className="w-3 h-3 text-slate-400 hidden sm:inline" />
            <select
              value={playbackRate}
              onChange={(e) => setPlaybackRate(parseFloat(e.target.value))}
              className="bg-transparent text-teal-300 font-bold focus:outline-none cursor-pointer"
            >
              {speeds.map((s) => (
                <option key={s} value={s} className="bg-slate-900 text-white">
                  {s}x
                </option>
              ))}
            </select>
          </div>

          {/* Sentence Counter (hidden on very narrow screens) */}
          <span className="text-[10px] font-mono text-slate-400 hidden md:inline">
            {currentSentenceIndex + 1}/{sentences.length}
          </span>

          {/* Minimize / Pill Toggle */}
          <button
            onClick={() => setIsMinimized(true)}
            className="p-1.5 rounded-lg bg-slate-900 hover:bg-slate-800 text-slate-400 hover:text-teal-300 border border-slate-800 transition-colors"
            title="Simge Durumuna Küçült (Mini Mod)"
          >
            <ChevronDown className="w-3.5 h-3.5" />
          </button>

          {/* Stop & Close */}
          <button
            onClick={stop}
            className="p-1.5 rounded-lg bg-slate-900 hover:bg-rose-500/20 text-slate-400 hover:text-rose-300 border border-slate-800 transition-colors"
            title="Durdur & Kapat"
          >
            <X className="w-3.5 h-3.5" />
          </button>
        </div>
      </div>
    </div>
  );
};
