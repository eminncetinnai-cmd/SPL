import React from 'react';
import { 
  Sparkles, 
  Play, 
  BookOpen, 
  AlertTriangle, 
  Star, 
  Award, 
  CheckCircle, 
  BarChart3, 
  Search,
  ArrowRight,
  ShieldAlert,
  Flame,
  Info,
  Layers,
  Zap
} from 'lucide-react';
import { ModuleProgressCards } from '../components/dashboard/ModuleProgressCards';
import { SubjectAccuracyChart } from '../components/dashboard/SubjectAccuracyChart';
import { PerformanceTrendChart } from '../components/dashboard/PerformanceTrendChart';
import { ReadinessGauge } from '../components/dashboard/ReadinessGauge';
import { useProgressStore } from '../stores/progressStore';
import { ModuleId } from '../types/exam';
import allQuestionsData from '../data/all_questions.json';

interface HomePageProps {
  onNavigate: (page: string, params?: any) => void;
}

export const HomePage: React.FC<HomePageProps> = ({ onNavigate }) => {
  const { history, mistakes, bookmarks, learnedCards, moduleStats } = useProgressStore();

  const totalQuizzes = history.length;
  const mistakeCount = Object.values(mistakes).filter((m) => !m.resolved).length;
  const bookmarkCount = bookmarks.length;
  const learnedCardsCount = learnedCards.length;

  const totalAnsweredFromModules = Object.values(moduleStats).reduce((acc, m) => acc + m.totalQuestions, 0);
  const totalCorrectFromModules = Object.values(moduleStats).reduce((acc, m) => acc + m.totalCorrect, 0);

  const totalAnswered = Math.max(totalAnsweredFromModules, history.reduce((acc, h) => acc + h.total_questions, 0));
  const totalCorrect = Math.max(totalCorrectFromModules, history.reduce((acc, h) => acc + h.correct_count, 0));
  const overallAccuracy = totalAnswered > 0 ? Math.round((totalCorrect / totalAnswered) * 100) : null;

  return (
    <div className="space-y-8 animate-fade-in pb-12">
      {/* Hero Banner */}
      <div className="relative overflow-hidden rounded-3xl bg-white dark:bg-gradient-to-r dark:from-slate-900 dark:via-fintech-card dark:to-slate-900 border border-slate-200 dark:border-teal-500/30 p-6 sm:p-8 shadow-sm">
        <div className="absolute top-0 right-0 -mt-8 -mr-8 w-64 h-64 bg-teal-500/5 dark:bg-teal-500/10 rounded-full blur-3xl pointer-events-none"></div>
        <div className="absolute bottom-0 left-1/3 -mb-8 w-64 h-64 bg-emerald-500/5 dark:bg-emerald-500/10 rounded-full blur-3xl pointer-events-none"></div>

        <div className="relative z-10 flex flex-col lg:flex-row items-start lg:items-center justify-between gap-6">
          <div className="space-y-3 max-w-2xl">
            <div className="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-teal-50 dark:bg-teal-500/15 text-teal-800 dark:text-teal-300 border border-teal-200 dark:border-teal-500/30 text-xs font-mono font-bold">
              <Sparkles className="w-3.5 h-3.5 text-teal-600 dark:text-teal-400" />
              <span>SPK SPL DÜZEY 1 MASTER SINAV & TEKRAR PLATFORMU</span>
            </div>
            <h1 className="text-2xl sm:text-3xl lg:text-4xl font-black text-slate-900 dark:text-white tracking-tight leading-tight">
              Sermaye Piyasası Lisanslama Sınavına <span className="text-transparent bg-clip-text bg-gradient-to-r from-teal-600 to-emerald-600 dark:from-teal-400 dark:to-emerald-400">Eksiksiz Hazırlanın</span>
            </h1>
            <p className="text-sm sm:text-base text-slate-600 dark:text-slate-300 leading-relaxed">
              4 Temel Modül, <strong>{(allQuestionsData as any[]).length} detaylı çözümlü soru</strong>, <strong>400 akılda kalıcı öğrenme kartı (Flashcards)</strong> ve sadeleştirilmiş konu anlatımlarıyla SPK barajını ilk girişte aşın.
            </p>

            <div className="flex items-center gap-4 text-xs font-mono text-slate-600 dark:text-slate-400 pt-1">
              <span className="flex items-center gap-1.5 text-slate-700 dark:text-slate-300 font-medium">
                <CheckCircle className="w-4 h-4 text-emerald-600 dark:text-emerald-400" /> Modül Barajı: ≥ 50 Puan
              </span>
              <span className="flex items-center gap-1.5 text-slate-700 dark:text-slate-300 font-medium">
                <CheckCircle className="w-4 h-4 text-teal-600 dark:text-teal-400" /> Genel Ortalama: ≥ 60 Puan
              </span>
            </div>
          </div>

          {/* Quick Action CTA Box */}
          <div className="flex flex-col sm:flex-row lg:flex-col gap-2.5 w-full sm:w-auto shrink-0">
            <button
              onClick={() => onNavigate('past-exams')}
              className="flex items-center justify-center gap-2.5 px-6 py-3.5 rounded-2xl bg-gradient-to-r from-amber-500 to-orange-500 hover:from-amber-600 hover:to-orange-600 text-white font-bold text-sm shadow-sm hover:shadow active:scale-95 transition-all"
            >
              <Award className="w-4 h-4 text-white" />
              <span>🎯 Çıkmış Sınav Soruları (110 Soru)</span>
              <ArrowRight className="w-4 h-4" />
            </button>

            <button
              onClick={() => onNavigate('practice', { sourceFilter: 'genel' })}
              className="flex items-center justify-center gap-2.5 px-6 py-3.5 rounded-2xl bg-gradient-to-r from-teal-600 to-emerald-600 hover:from-teal-700 hover:to-emerald-700 text-white font-bold text-sm shadow-sm hover:shadow active:scale-95 transition-all"
            >
              <Sparkles className="w-4 h-4 fill-white" />
              <span>📚 Genel Soru Havuzu (550 Soru)</span>
              <ArrowRight className="w-4 h-4" />
            </button>

            <button
              onClick={() => onNavigate('simulation-prep')}
              className="flex items-center justify-center gap-2.5 px-6 py-2.5 rounded-2xl bg-slate-100 hover:bg-slate-200 dark:bg-teal-500/15 dark:hover:bg-teal-500/25 text-slate-800 dark:text-teal-300 border border-slate-200 dark:border-teal-500/40 text-xs font-bold transition-all"
            >
              <Sparkles className="w-3.5 h-3.5 text-teal-600 dark:text-teal-400" />
              <span>Sınav Simülasyonu (100 Soru / Süreli)</span>
            </button>

            <button
              onClick={() => onNavigate('cheat-sheet')}
              className="flex items-center justify-center gap-2.5 px-6 py-2.5 rounded-2xl bg-amber-50 hover:bg-amber-100 dark:bg-gradient-to-r dark:from-amber-500/20 dark:via-fintech-card dark:to-amber-500/10 border border-amber-200 dark:border-amber-500/40 text-amber-900 dark:text-amber-300 font-bold text-xs shadow-xs transition-all"
            >
              <Zap className="w-3.5 h-3.5 fill-amber-500 text-amber-500 dark:fill-amber-300" />
              <span>⚡ Sınav Öncesi 10 Dk Hap Bilgiler</span>
            </button>
          </div>
        </div>
      </div>

      {/* KPI Stats Strip */}
      <div className="grid grid-cols-2 sm:grid-cols-4 gap-4">
        <div className="bg-white dark:bg-fintech-surface p-4 rounded-2xl border border-slate-200 dark:border-fintech-border space-y-1 shadow-sm">
          <span className="text-xs text-slate-500 dark:text-slate-400 font-mono uppercase block font-semibold">Soru Bankası Havuzu</span>
          <span className="text-xl sm:text-2xl font-black font-mono text-slate-900 dark:text-white">{(allQuestionsData as any[]).length} Soru</span>
          <span className="text-[11px] text-teal-700 dark:text-teal-400 block font-sans font-medium">110 Çıkmış + 400 Master + 150 Diğer</span>
        </div>

        <div className="bg-white dark:bg-fintech-surface p-4 rounded-2xl border border-slate-200 dark:border-fintech-border space-y-1 shadow-sm">
          <span className="text-xs text-slate-500 dark:text-slate-400 font-mono uppercase block font-semibold">Öğrenme Kartları</span>
          <span className="text-xl sm:text-2xl font-black font-mono text-teal-700 dark:text-teal-300">400 Kart</span>
          <span className="text-[11px] text-slate-500 dark:text-slate-400 block font-sans font-medium">{learnedCardsCount} / 400 Öğrenildi</span>
        </div>

        <div className="bg-white dark:bg-fintech-surface p-4 rounded-2xl border border-slate-200 dark:border-fintech-border space-y-1 shadow-sm">
          <span className="text-xs text-slate-500 dark:text-slate-400 font-mono uppercase block font-semibold">Tamamlanan Sınav</span>
          <span className="text-xl sm:text-2xl font-black font-mono text-cyan-700 dark:text-cyan-400">{totalQuizzes} Adet</span>
          <span className="text-[11px] text-slate-500 dark:text-slate-400 block font-sans font-medium">{totalAnswered} Soru Çözüldü</span>
        </div>

        <div className="bg-white dark:bg-fintech-surface p-4 rounded-2xl border border-slate-200 dark:border-fintech-border space-y-1 shadow-sm">
          <span className="text-xs text-slate-500 dark:text-slate-400 font-mono uppercase block font-semibold">Genel Başarı Oranı</span>
          <span className={`text-xl sm:text-2xl font-black font-mono ${
            overallAccuracy !== null ? (overallAccuracy >= 60 ? 'text-emerald-600 dark:text-emerald-400' : 'text-amber-600 dark:text-amber-400') : 'text-slate-400'
          }`}>
            {overallAccuracy !== null ? `%${overallAccuracy}` : '-'}
          </span>
          <span className="text-[11px] text-slate-500 dark:text-slate-400 block font-sans font-medium">
            {overallAccuracy !== null ? `${totalCorrect} Doğru Cevap` : 'İlk testinizi çözün'}
          </span>
        </div>
      </div>

      {/* Çıkmış Sınav Soruları Özel Test Grubu Banner */}
      <div className="rounded-3xl bg-amber-50/70 dark:bg-gradient-to-r dark:from-amber-500/10 dark:via-fintech-surface dark:to-slate-900 border border-amber-200 dark:border-amber-500/30 p-6 shadow-sm space-y-4">
        <div className="flex flex-col md:flex-row md:items-center justify-between gap-4">
          <div className="space-y-1.5">
            <div className="inline-flex items-center gap-2 px-2.5 py-0.5 rounded-full bg-amber-100 text-amber-800 border border-amber-200 dark:bg-amber-500/20 dark:text-amber-300 dark:border-amber-500/40 text-[11px] font-mono font-bold">
              <Award className="w-3.5 h-3.5 text-amber-600 dark:text-amber-400" />
              <span>ÖZEL ÇIKMIŞ SINAV GRUBU • 110 SORU</span>
            </div>
            <h3 className="text-lg font-black text-slate-900 dark:text-white tracking-tight flex items-center gap-2">
              🎯 Çıkmış Sınav Soruları Grubu
            </h3>
            <p className="text-xs text-slate-700 dark:text-slate-300 max-w-2xl leading-relaxed">
              SPK Lisanslama sınavlarında birebir çıkan soru kalıpları, süreler, kanuni yaptırımlar ve operasyonel iş akışlarından derlenen 110 soruluk özel çıkmış sınav havuzu.
            </p>
          </div>

          <button
            onClick={() => onNavigate('past-exams')}
            className="flex items-center justify-center gap-2 px-5 py-3 rounded-xl bg-gradient-to-r from-amber-500 to-orange-500 hover:from-amber-600 hover:to-orange-600 text-white font-bold text-xs shadow-sm active:scale-95 transition-all shrink-0"
          >
            <Play className="w-4 h-4 fill-white" />
            <span>Çıkmış Sorulardan Test Başlat</span>
            <ArrowRight className="w-4 h-4" />
          </button>
        </div>

        {/* Quick Module Buttons */}
        <div className="grid grid-cols-2 sm:grid-cols-4 gap-2 pt-2 border-t border-amber-200 dark:border-amber-500/20 text-xs">
          {[
            { id: '1001', name: '1001: Mevzuat (35 Soru)' },
            { id: '1003', name: '1003: SP Araçları (25 Soru)' },
            { id: '1005', name: '1005: Yatırım Kur. (25 Soru)' },
            { id: '1012', name: '1012: Takas & Sakl. (25 Soru)' },
          ].map((m) => (
            <button
              key={m.id}
              onClick={() => onNavigate('past-exams', { moduleId: m.id })}
              className="py-2 px-3 rounded-lg bg-white dark:bg-slate-900/80 hover:bg-amber-100 dark:hover:bg-amber-500/15 border border-amber-200 dark:border-slate-800 hover:border-amber-300 dark:hover:border-amber-500/40 text-slate-800 dark:text-slate-300 hover:text-amber-900 dark:hover:text-amber-200 font-mono text-[11px] font-bold text-center transition-all shadow-xs"
            >
              {m.name} &rarr;
            </button>
          ))}
        </div>
      </div>

      {/* 4 SPL Module Cards Section */}
      <div className="space-y-4">
        <div className="flex items-center justify-between">
          <div className="space-y-1">
            <h2 className="text-xl font-black text-slate-900 dark:text-white tracking-tight">
              SPK SPL Düzey 1 Sınav Modülleri
            </h2>
            <p className="text-xs text-slate-500 dark:text-slate-400">
              Her ders için ortalama 165 soru, 100 flashcard ve tam mevzuat ders notları mevcuttur.
            </p>
          </div>
        </div>

        <ModuleProgressCards onNavigate={onNavigate} />
      </div>

      {/* Learning Tools Quick Grid */}
      <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
        {/* Flashcards Box */}
        <div 
          onClick={() => onNavigate('flashcards')}
          className="p-6 rounded-3xl bg-white dark:bg-fintech-surface hover:bg-slate-50 dark:hover:bg-fintech-card border border-slate-200 dark:border-fintech-border hover:border-teal-500/40 cursor-pointer transition-all space-y-3 group shadow-sm"
        >
          <div className="w-12 h-12 rounded-2xl bg-teal-50 text-teal-700 border border-teal-200 dark:bg-teal-500/10 dark:text-teal-400 dark:border-teal-500/20 flex items-center justify-center group-hover:scale-110 transition-transform">
            <Layers className="w-6 h-6" />
          </div>
          <h3 className="font-bold text-base text-slate-900 dark:text-white group-hover:text-teal-700 dark:group-hover:text-teal-300 transition-colors">
            400 Öğrenme Kartı (Flashcards)
          </h3>
          <p className="text-xs text-slate-600 dark:text-slate-400 leading-relaxed">
            Kavram çiftleri, pratik örnekler ve sınav tuzaklarıyla hızlı tekrar yapın.
          </p>
          <div className="flex items-center gap-1.5 text-xs text-teal-700 dark:text-teal-400 font-bold pt-1">
            <span>Kartları İncele</span>
            <ArrowRight className="w-4 h-4 group-hover:translate-x-1 transition-transform" />
          </div>
        </div>

        {/* Mistake Notebook Box */}
        <div 
          onClick={() => onNavigate('mistakes')}
          className="p-6 rounded-3xl bg-white dark:bg-fintech-surface hover:bg-slate-50 dark:hover:bg-fintech-card border border-slate-200 dark:border-fintech-border hover:border-rose-500/40 cursor-pointer transition-all space-y-3 group shadow-sm"
        >
          <div className="w-12 h-12 rounded-2xl bg-rose-50 text-rose-700 border border-rose-200 dark:bg-rose-500/10 dark:text-rose-400 dark:border-rose-500/20 flex items-center justify-center group-hover:scale-110 transition-transform">
            <AlertTriangle className="w-6 h-6" />
          </div>
          <h3 className="font-bold text-base text-slate-900 dark:text-white group-hover:text-rose-700 dark:group-hover:text-rose-300 transition-colors">
            Yanlışlarım & Tekrar Defteri
          </h3>
          <p className="text-xs text-slate-600 dark:text-slate-400 leading-relaxed">
            Hatalı yaptığınız {mistakeCount > 0 ? `${mistakeCount} soruyu` : 'soruları'} analiz edin ve tek tıkla zayıf noktalardan test oluşturun.
          </p>
          <div className="flex items-center gap-1.5 text-xs text-rose-400 font-bold pt-1">
            <span>Deftere Git ({mistakeCount})</span>
            <ArrowRight className="w-4 h-4 group-hover:translate-x-1 transition-transform" />
          </div>
        </div>

        {/* 800 Question Bank Search */}
        <div 
          onClick={() => onNavigate('explorer')}
          className="p-6 rounded-3xl bg-fintech-surface hover:bg-fintech-card border border-fintech-border hover:border-cyan-500/40 cursor-pointer transition-all space-y-3 group shadow-xl"
        >
          <div className="w-12 h-12 rounded-2xl bg-cyan-500/10 text-cyan-400 border border-cyan-500/20 flex items-center justify-center group-hover:scale-110 transition-transform">
            <Search className="w-6 h-6" />
          </div>
          <h3 className="font-bold text-base text-white group-hover:text-cyan-300 transition-colors">
            540 Soru Bankası & Arama
          </h3>
          <p className="text-xs text-slate-400 leading-relaxed">
            Tüm soru havuzunda kanun maddesi veya anahtar kelimeye göre arama ve filtreleme yapın.
          </p>
          <div className="flex items-center gap-1.5 text-xs text-cyan-400 font-bold pt-1">
            <span>Soru Havuzunu Keşfet</span>
            <ArrowRight className="w-4 h-4 group-hover:translate-x-1 transition-transform" />
          </div>
        </div>
      </div>

      {/* Analytics & Performance Overview */}
      <div className="space-y-4 pt-4">
        <div className="flex items-center justify-between">
          <div>
            <h2 className="text-xl font-bold text-white tracking-tight">
              Sınav Hazırlık & Performans Analitiği
            </h2>
            <p className="text-xs text-slate-400">
              Ders bazlı başarı dağılımı ve resmi SPK barajı (%50) simülasyonu.
            </p>
          </div>

          <button
            onClick={() => onNavigate('dashboard')}
            className="text-xs text-teal-400 hover:text-teal-300 font-mono font-semibold flex items-center gap-1 hover:underline"
          >
            <span>Detaylı Analitik Görünümü</span>
            <ArrowRight className="w-3.5 h-3.5" />
          </button>
        </div>

        <div className="grid grid-cols-1 lg:grid-cols-12 gap-6">
          <div className="lg:col-span-8">
            <SubjectAccuracyChart />
          </div>
          <div className="lg:col-span-4">
            <ReadinessGauge />
          </div>
        </div>
      </div>
    </div>
  );
};
