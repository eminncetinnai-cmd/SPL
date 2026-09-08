import React, { useState, useEffect } from 'react';
import { 
  BookOpen, 
  Search, 
  ChevronRight, 
  Play, 
  Lightbulb, 
  AlertTriangle, 
  CheckCircle,
  FileText,
  Table as TableIcon,
  Sparkles,
  Volume2,
  Pause,
  Headphones
} from 'lucide-react';
import topicNotesData from '../data/topic_notes.json';
import modulesData from '../data/modules.json';
import { ModuleId, TopicModuleNotes, TopicSection } from '../types/exam';
import { useAudioStore } from '../stores/audioStore';
import { cleanVisualText } from '../utils/speechEngine';

interface StudyNotesPageProps {
  initialModuleId?: ModuleId;
  onNavigate: (page: string, params?: any) => void;
}

export const StudyNotesPage: React.FC<StudyNotesPageProps> = ({
  initialModuleId = '1001',
  onNavigate,
}) => {
  const [activeModule, setActiveModule] = useState<ModuleId>(initialModuleId);
  const [activeSectionId, setActiveSectionId] = useState<string>('');
  const [searchQuery, setSearchQuery] = useState<string>('');

  const {
    isPlaying,
    isPaused,
    sectionId: playingSectionId,
    currentSentenceIndex,
    sentences,
    playSection,
    togglePlayPause,
    stop,
  } = useAudioStore();

  useEffect(() => {
    if (initialModuleId) {
      setActiveModule(initialModuleId);
      setActiveSectionId('');
    }
  }, [initialModuleId]);

  const currentNotes = (topicNotesData as Record<string, TopicModuleNotes>)[activeModule];
  const currentModuleInfo = modulesData.find((m) => m.id === activeModule);

  const sections = currentNotes?.sections || [];
  
  // Filter sections by search query if any
  const filteredSections = sections.filter((sec) => {
    if (!searchQuery.trim()) return true;
    const query = searchQuery.toLowerCase();
    return (
      sec.title.toLowerCase().includes(query) ||
      sec.content.some((c) => c.toLowerCase().includes(query)) ||
      sec.key_takeaways.some((k) => k.toLowerCase().includes(query)) ||
      sec.exam_traps.some((t) => t.toLowerCase().includes(query)) ||
      (sec.tables && sec.tables.some((tbl) => tbl.rows.some((r) => r.some((cell) => cell.toLowerCase().includes(query)))))
    );
  });

  const selectedSection = sections.find((s) => s.id === activeSectionId) || filteredSections[0];
  const currentSecIdx = sections.findIndex((s) => s.id === selectedSection?.id);

  // Audio listen handler
  const handleListenSection = () => {
    if (!selectedSection) return;

    if (playingSectionId === selectedSection.id && isPlaying) {
      togglePlayPause();
      return;
    }

    const allParagraphs: string[] = [
      selectedSection.title,
      ...selectedSection.content,
      ...selectedSection.exam_traps,
      ...selectedSection.key_takeaways,
    ];

    playSection({
      moduleId: activeModule,
      sectionId: selectedSection.id,
      title: selectedSection.title,
      paragraphs: allParagraphs,
      onComplete: () => {
        // Auto play next section if available
        if (currentSecIdx >= 0 && currentSecIdx + 1 < sections.length) {
          const nextSec = sections[currentSecIdx + 1];
          setActiveSectionId(nextSec.id);
          const nextPars = [
            nextSec.title,
            ...nextSec.content,
            ...nextSec.exam_traps,
            ...nextSec.key_takeaways,
          ];
          setTimeout(() => {
            playSection({
              moduleId: activeModule,
              sectionId: nextSec.id,
              title: nextSec.title,
              paragraphs: nextPars,
            });
          }, 600);
        }
      },
    });
  };

  const isCurrentSectionPlaying = playingSectionId === selectedSection?.id && isPlaying && !isPaused;

  return (
    <div className="max-w-7xl mx-auto space-y-6 animate-fade-in pb-24">
      {/* Header */}
      <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-4 border-b border-slate-200 dark:border-fintech-border/70 pb-5">
        <div>
          <span className="text-xs font-mono text-teal-600 dark:text-teal-400 font-bold uppercase tracking-wider block">
            Ders Notları & Akıcı Dinleme Rehberi
          </span>
          <h1 className="text-xl sm:text-2xl font-black text-slate-900 dark:text-white tracking-tight">
            SPK SPL Düzey 1 Konu Anlatımları
          </h1>
        </div>

        <div className="flex items-center gap-3 self-start sm:self-auto flex-wrap">
          <button
            onClick={() => onNavigate('module-quiz-prep', { moduleId: activeModule })}
            className="flex items-center gap-2 px-5 py-2.5 rounded-xl bg-teal-500 hover:bg-teal-400 text-slate-950 font-bold text-xs shadow-md shadow-teal-500/20 active:scale-95 transition-all"
          >
            <Play className="w-4 h-4 fill-slate-950" />
            <span>Bu Modülün Testini Çöz ({activeModule})</span>
          </button>
        </div>
      </div>

      {/* Module Selector Tabs */}
      <div className="grid grid-cols-2 lg:grid-cols-4 gap-3">
        {modulesData.map((m) => {
          const isActive = activeModule === m.id;
          return (
            <button
              key={m.id}
              onClick={() => {
                setActiveModule(m.id as ModuleId);
                setActiveSectionId('');
                setSearchQuery('');
              }}
              className={`p-3.5 rounded-2xl border text-left transition-all ${
                isActive
                  ? 'bg-teal-50 dark:bg-teal-500/15 border-teal-500 text-teal-950 dark:text-white shadow-sm ring-1 ring-teal-500/30'
                  : 'bg-white dark:bg-fintech-surface border-slate-200 dark:border-fintech-border text-slate-600 dark:text-slate-400 hover:text-slate-900 dark:hover:text-white hover:bg-slate-50 dark:hover:bg-fintech-card shadow-sm'
              }`}
            >
              <div className="flex items-center justify-between mb-1">
                <span className="font-mono text-xs font-bold text-teal-600 dark:text-teal-400">
                  Modül {m.code}
                </span>
                <span className="text-[10px] font-mono text-slate-500">
                  {m.category}
                </span>
              </div>
              <h4 className="text-xs sm:text-sm font-bold text-slate-900 dark:text-slate-200 truncate">
                {m.short_name}
              </h4>
            </button>
          );
        })}
      </div>

      {/* Search and Study Container */}
      <div className="grid grid-cols-1 lg:grid-cols-12 gap-6">
        {/* Left Column: Chapters / Sections Index & Search */}
        <div className="lg:col-span-4 space-y-4">
          {/* Search Box */}
          <div className="relative">
            <Search className="absolute left-3.5 top-3 w-4 h-4 text-slate-400" />
            <input
              type="text"
              value={searchQuery}
              onChange={(e) => setSearchQuery(e.target.value)}
              placeholder="Konu, süre veya kanun maddesi ara..."
              className="w-full bg-white dark:bg-fintech-surface border border-slate-200 dark:border-fintech-border rounded-xl pl-10 pr-4 py-2.5 text-xs text-slate-900 dark:text-slate-200 placeholder-slate-400 dark:placeholder-slate-500 focus:outline-none focus:border-teal-500 transition-colors shadow-sm"
            />
          </div>

          {/* Section Index List */}
          <div className="bg-white dark:bg-fintech-surface rounded-2xl border border-slate-200 dark:border-fintech-border p-3 space-y-1.5 max-h-[600px] overflow-y-auto shadow-sm">
            <p className="text-[11px] font-mono uppercase tracking-wider text-slate-500 dark:text-slate-400 font-bold px-2 py-1">
              İçindekiler ({filteredSections.length} Konu Başlığı)
            </p>
            {filteredSections.map((sec, idx) => {
              const isSelected = selectedSection?.id === sec.id;
              const isSecPlaying = playingSectionId === sec.id && isPlaying && !isPaused;
              const hasTables = sec.tables && sec.tables.length > 0;

              return (
                <button
                  key={sec.id}
                  onClick={() => setActiveSectionId(sec.id)}
                  className={`w-full flex items-start gap-2.5 p-3 rounded-xl text-left text-xs font-medium transition-all ${
                    isSelected
                      ? 'bg-teal-50 dark:bg-teal-500/15 border border-teal-300 dark:border-teal-500/40 text-teal-900 dark:text-teal-300 font-bold shadow-sm'
                      : 'text-slate-600 dark:text-slate-400 hover:text-slate-900 dark:hover:text-slate-200 hover:bg-slate-50 dark:hover:bg-fintech-card'
                  }`}
                >
                  <span className="font-mono text-teal-600 dark:text-teal-500/80 shrink-0">{idx + 1}.</span>
                  <div className="flex-1 leading-snug">
                    <span className="line-clamp-2">{cleanVisualText(sec.title)}</span>
                    <div className="flex items-center gap-2 mt-0.5">
                      {hasTables && (
                        <span className="text-[10px] text-teal-600 dark:text-teal-400/80 font-mono inline-flex items-center gap-1">
                          <TableIcon className="w-2.5 h-2.5" /> Tablolu
                        </span>
                      )}
                      {isSecPlaying && (
                        <span className="text-[10px] text-emerald-600 dark:text-emerald-400 font-mono inline-flex items-center gap-1 animate-pulse">
                          <Volume2 className="w-2.5 h-2.5" /> Çalıyor
                        </span>
                      )}
                    </div>
                  </div>
                </button>
              );
            })}
          </div>
        </div>

        {/* Right Column: Active Section Reader */}
        <div className="lg:col-span-8">
          {selectedSection ? (
            <div className="bg-white dark:bg-fintech-surface rounded-3xl border border-slate-200 dark:border-fintech-border p-6 sm:p-8 space-y-6 shadow-sm dark:shadow-xl leading-relaxed">
              {/* Section Header with Audio Play Button */}
              <div className="border-b border-slate-100 dark:border-fintech-border/70 pb-5 space-y-3">
                <div className="flex items-center justify-between gap-3">
                  <div className="flex items-center gap-2 text-xs font-mono text-teal-600 dark:text-teal-400">
                    <span>Modül {activeModule}</span>
                    <span>•</span>
                    <span>{currentModuleInfo?.short_name}</span>
                  </div>

                  {/* Audio Podcast Mode Button */}
                  <button
                    onClick={handleListenSection}
                    className={`flex items-center gap-2 px-4 py-2 rounded-xl text-xs font-bold transition-all shadow-md ${
                      isCurrentSectionPlaying
                        ? 'bg-emerald-500 text-slate-950 shadow-emerald-500/20 ring-2 ring-emerald-400 animate-pulse'
                        : 'bg-teal-50 dark:bg-teal-500/15 hover:bg-teal-100 dark:hover:bg-teal-500/25 text-teal-900 dark:text-teal-300 border border-teal-300 dark:border-teal-500/40 active:scale-95'
                    }`}
                    title="Bu konuyu yapay zeka ses tonlamasıyla dinleyin"
                  >
                    {isCurrentSectionPlaying ? (
                      <>
                        <Pause className="w-4 h-4 fill-slate-950" />
                        <span>Dinlemeyi Duraklat</span>
                      </>
                    ) : (
                      <>
                        <Headphones className="w-4 h-4 text-teal-600 dark:text-teal-400" />
                        <span>Sesli Dinle (Podcast Modu)</span>
                      </>
                    )}
                  </button>
                </div>

                <h2 className="text-xl sm:text-2xl font-black text-slate-900 dark:text-white tracking-tight">
                  {cleanVisualText(selectedSection.title)}
                </h2>
              </div>

              {/* Exam Traps & Special Tips Box (if any) */}
              {selectedSection.exam_traps && selectedSection.exam_traps.length > 0 && (
                <div className="bg-amber-50 dark:bg-amber-950/25 rounded-2xl border border-amber-200 dark:border-amber-500/40 p-5 space-y-3 shadow-sm">
                  <div className="flex items-center gap-2 text-amber-800 dark:text-amber-400 font-mono text-xs font-bold uppercase tracking-wider">
                    <AlertTriangle className="w-4 h-4 text-amber-600 dark:text-amber-400" />
                    <span>Sınavda Sıkça Çıkan Kritik Noktalar & Süreler</span>
                  </div>
                  <div className="space-y-2 text-xs sm:text-sm text-slate-800 dark:text-amber-200/90 leading-relaxed">
                    {selectedSection.exam_traps.map((trap, i) => (
                      <p key={i} className="whitespace-pre-line leading-relaxed">
                        {cleanVisualText(trap)}
                      </p>
                    ))}
                  </div>
                </div>
              )}

              {/* Concrete Market Examples / Case Studies */}
              {selectedSection.concrete_examples && selectedSection.concrete_examples.length > 0 && (
                <div className="bg-cyan-50/60 dark:bg-gradient-to-r dark:from-cyan-950/30 dark:via-fintech-card dark:to-slate-900/40 rounded-2xl border border-cyan-200 dark:border-cyan-500/40 p-5 space-y-3 shadow-sm">
                  <div className="flex items-center gap-2 text-cyan-800 dark:text-cyan-400 font-mono text-xs font-bold uppercase tracking-wider">
                    <Sparkles className="w-4 h-4 text-cyan-600 dark:text-cyan-400" />
                    <span>💼 Somut Piyasa Senaryosu & Olay İncelemesi</span>
                  </div>
                  <div className="space-y-2 text-xs sm:text-sm text-slate-800 dark:text-cyan-100/90 leading-relaxed font-sans">
                    {selectedSection.concrete_examples.map((ex, i) => (
                      <div key={i} className="p-3.5 rounded-xl bg-white dark:bg-cyan-950/30 border border-cyan-200 dark:border-cyan-500/20 text-slate-800 dark:text-slate-200 shadow-xs">
                        {cleanVisualText(ex)}
                      </div>
                    ))}
                  </div>
                </div>
              )}

              {/* Main Content Paragraphs (Clean Prose) */}
              <div className="space-y-4 text-slate-800 dark:text-slate-200 text-sm sm:text-base leading-relaxed">
                {selectedSection.content.map((para, i) => {
                  const cleanedPara = cleanVisualText(para);
                  if (!cleanedPara) return null;

                  return (
                    <p key={i} className="whitespace-pre-line text-slate-800 dark:text-slate-200 leading-relaxed">
                      {cleanedPara}
                    </p>
                  );
                })}
              </div>

              {/* Tables Section (if any) */}
              {selectedSection.tables && selectedSection.tables.length > 0 && (
                <div className="space-y-5 pt-2">
                  {selectedSection.tables.map((table, tIdx) => (
                    <div key={tIdx} className="overflow-x-auto rounded-2xl border border-slate-200 dark:border-fintech-border bg-slate-50/50 dark:bg-fintech-card/60 shadow-sm">
                      <table className="w-full text-left text-xs font-sans">
                        {table.headers && table.headers.length > 0 && (
                          <thead className="bg-slate-100 dark:bg-slate-900/90 border-b border-slate-200 dark:border-fintech-border text-slate-800 dark:text-teal-400 font-mono font-bold uppercase text-[11px]">
                            <tr>
                              {table.headers.map((h, hIdx) => (
                                <th key={hIdx} className="py-3 px-4 tracking-wider">
                                  {cleanVisualText(h)}
                                </th>
                              ))}
                            </tr>
                          </thead>
                        )}
                        <tbody className="divide-y divide-slate-200 dark:divide-fintech-border/60 text-slate-700 dark:text-slate-300">
                          {table.rows.map((row, rIdx) => (
                            <tr key={rIdx} className="hover:bg-slate-100/60 dark:hover:bg-slate-800/40 transition-colors">
                              {row.map((cell, cIdx) => (
                                <td key={cIdx} className="py-3 px-4 leading-relaxed">
                                  {cleanVisualText(cell)}
                                </td>
                              ))}
                            </tr>
                          ))}
                        </tbody>
                      </table>
                    </div>
                  ))}
                </div>
              )}

              {/* Key Takeaways Bullets (Clean format) */}
              {selectedSection.key_takeaways && selectedSection.key_takeaways.length > 0 && (
                <div className="bg-slate-50 dark:bg-fintech-card/80 rounded-2xl border border-slate-200 dark:border-fintech-border p-5 space-y-3 shadow-sm">
                  <div className="flex items-center gap-2 text-teal-700 dark:text-teal-400 font-mono text-xs font-bold uppercase tracking-wider">
                    <CheckCircle className="w-4 h-4 text-teal-600 dark:text-teal-400" />
                    <span>Önemli Maddeler ve Tanımlar</span>
                  </div>
                  <ul className="space-y-2.5 text-xs sm:text-sm text-slate-700 dark:text-slate-300">
                    {selectedSection.key_takeaways.map((point, i) => {
                      const cleanedPoint = cleanVisualText(point);
                      if (!cleanedPoint) return null;
                      return (
                        <li key={i} className="flex items-start gap-2.5">
                          <span className="w-1.5 h-1.5 rounded-full bg-teal-500 mt-2 shrink-0"></span>
                          <span className="leading-relaxed">{cleanedPoint}</span>
                        </li>
                      );
                    })}
                  </ul>
                </div>
              )}

              {/* Exam Tips / Öncüllü Soru Mantığı (if any) */}
              {selectedSection.exam_tips && selectedSection.exam_tips.length > 0 && (
                <div className="bg-purple-50 dark:bg-purple-950/20 rounded-2xl border border-purple-200 dark:border-purple-500/40 p-5 space-y-3 shadow-sm">
                  <div className="flex items-center gap-2 text-purple-800 dark:text-purple-400 font-mono text-xs font-bold uppercase tracking-wider">
                    <Lightbulb className="w-4 h-4 text-purple-600 dark:text-purple-400" />
                    <span>🎯 Sınavda Nasıl Sorulur? (Öncüllü Soru Mantığı)</span>
                  </div>
                  <div className="space-y-2 text-xs sm:text-sm text-slate-800 dark:text-purple-200/90 leading-relaxed">
                    {selectedSection.exam_tips.map((tip, i) => (
                      <p key={i} className="leading-relaxed">
                        {cleanVisualText(tip)}
                      </p>
                    ))}
                  </div>
                </div>
              )}

              {/* Action Bar at the Bottom: "Bu Konudan Hemen Test Çöz" */}
              <div className="pt-6 border-t border-slate-100 dark:border-fintech-border/70 flex flex-col sm:flex-row items-center justify-between gap-4">
                <div>
                  <span className="text-xs font-mono text-slate-500 dark:text-slate-400 block">Konuyu Pekiştir:</span>
                  <span className="text-xs text-slate-700 dark:text-slate-300 font-medium">Bu dersin tüm öncüllü ve eşik sorularıyla pratik yapın</span>
                </div>

                <button
                  onClick={() => onNavigate('practice', { initialModuleId: activeModule, initialSourceFilter: 'genel' })}
                  className="w-full sm:w-auto flex items-center justify-center gap-2 px-6 py-3.5 rounded-2xl bg-gradient-to-r from-teal-500 to-emerald-500 hover:from-teal-400 hover:to-emerald-400 text-slate-950 font-black text-xs shadow-md shadow-teal-500/25 active:scale-95 transition-all"
                >
                  <Play className="w-4 h-4 fill-slate-950" />
                  <span>🎯 Modül {activeModule} Testini Başlat</span>
                </button>
              </div>
            </div>
          ) : (
            <div className="bg-white dark:bg-fintech-surface rounded-2xl border border-slate-200 dark:border-fintech-border p-12 text-center text-slate-500 dark:text-slate-400 shadow-sm">
              Arama kriterinize uygun konu başlığı bulunamadı.
            </div>
          )}
        </div>
      </div>
    </div>
  );
};
