import React, { useState, useEffect, Suspense, lazy } from 'react';
import { Navbar } from './components/layout/Navbar';
import { Sidebar } from './components/layout/Sidebar';
import { HomePage } from './pages/HomePage';
import { useSettingsStore } from './stores/settingsStore';
import { ModuleId } from './types/exam';

import { AudioPlayerBar } from './components/audio/AudioPlayerBar';
import { Footer } from './components/layout/Footer';
import { MobileBottomNav } from './components/layout/MobileBottomNav';

// Lazy-loaded pages to speed up initial startup and mobile JS parse time
const PracticeQuizPage = lazy(() =>
  import('./pages/PracticeQuizPage').then((m) => ({ default: m.PracticeQuizPage }))
);
const SimulationExamPage = lazy(() =>
  import('./pages/SimulationExamPage').then((m) => ({ default: m.SimulationExamPage }))
);
const ResultsPage = lazy(() =>
  import('./pages/ResultsPage').then((m) => ({ default: m.ResultsPage }))
);
const StudyNotesPage = lazy(() =>
  import('./pages/StudyNotesPage').then((m) => ({ default: m.StudyNotesPage }))
);
const FlashcardsPage = lazy(() =>
  import('./pages/FlashcardsPage').then((m) => ({ default: m.FlashcardsPage }))
);
const MistakeNotebookPage = lazy(() =>
  import('./pages/MistakeNotebookPage').then((m) => ({ default: m.MistakeNotebookPage }))
);
const BookmarksPage = lazy(() =>
  import('./pages/BookmarksPage').then((m) => ({ default: m.BookmarksPage }))
);
const QuestionExplorerPage = lazy(() =>
  import('./pages/QuestionExplorerPage').then((m) => ({ default: m.QuestionExplorerPage }))
);
const DashboardPage = lazy(() =>
  import('./pages/DashboardPage').then((m) => ({ default: m.DashboardPage }))
);
const SettingsPage = lazy(() =>
  import('./pages/SettingsPage').then((m) => ({ default: m.SettingsPage }))
);
const CheatSheetPage = lazy(() =>
  import('./pages/CheatSheetPage').then((m) => ({ default: m.CheatSheetPage }))
);
const ExamMorningPage = lazy(() =>
  import('./pages/ExamMorningPage').then((m) => ({ default: m.ExamMorningPage }))
);
const LicensesPage = lazy(() =>
  import('./pages/LicensesPage').then((m) => ({ default: m.LicensesPage }))
);

export const App: React.FC = () => {
  const [currentPage, setCurrentPage] = useState<string>('home');
  const [pageParams, setPageParams] = useState<any>({});
  const { theme } = useSettingsStore();

  useEffect(() => {
    if (theme === 'dark') {
      document.documentElement.classList.add('dark');
    } else {
      document.documentElement.classList.remove('dark');
    }
  }, [theme]);

  const handleNavigate = (page: string, params: any = {}) => {
    if (page === 'past-exams') {
      setCurrentPage('practice');
      setPageParams({ filterMode: 'unseen', ...params });
      window.scrollTo({ top: 0, behavior: 'smooth' });
      return;
    }
    setCurrentPage(page);
    setPageParams(params);
    window.scrollTo({ top: 0, behavior: 'smooth' });
  };

  const renderPage = () => {
    switch (currentPage) {
      case 'home':
        return <HomePage onNavigate={handleNavigate} />;
      case 'past-exams':
      case 'module-quiz-prep':
      case 'practice':
        return (
          <PracticeQuizPage
            initialModuleId={pageParams.moduleId as ModuleId}
            initialFilterMode={pageParams.filterMode}
            initialTestMode={pageParams.testMode}
            initialSourceFilter={pageParams.sourceFilter}
            onNavigate={handleNavigate}
          />
        );
      case 'simulation-prep':
      case 'simulation':
        return <SimulationExamPage onNavigate={handleNavigate} />;
      case 'results':
        return <ResultsPage onNavigate={handleNavigate} />;
      case 'study-notes':
        return (
          <StudyNotesPage
            initialModuleId={pageParams.moduleId as ModuleId}
            onNavigate={handleNavigate}
          />
        );
      case 'flashcards':
        return (
          <FlashcardsPage
            initialModuleId={pageParams.moduleId as ModuleId}
            onNavigate={handleNavigate}
          />
        );
      case 'mistakes':
        return <MistakeNotebookPage onNavigate={handleNavigate} />;
      case 'bookmarks':
        return <BookmarksPage onNavigate={handleNavigate} />;
      case 'explorer':
        return (
          <QuestionExplorerPage
            initialModuleId={pageParams.moduleId}
            initialStatus={pageParams.status}
            onNavigate={handleNavigate}
          />
        );
      case 'dashboard':
        return <DashboardPage onNavigate={handleNavigate} />;
      case 'cheat-sheet':
        return <CheatSheetPage onNavigate={handleNavigate} />;
      case 'exam-morning':
        return (
          <ExamMorningPage
            initialModuleId={pageParams.moduleId}
            onNavigate={handleNavigate}
          />
        );
      case 'licenses':
        return <LicensesPage onNavigate={handleNavigate} />;
      case 'settings':
        return <SettingsPage />;
      default:
        return <HomePage onNavigate={handleNavigate} />;
    }
  };

  return (
    <div className="min-h-screen bg-fintech-dark text-slate-900 dark:text-slate-100 flex flex-col font-sans selection:bg-teal-500/30 selection:text-teal-900 relative">
      <Navbar onNavigate={handleNavigate} currentPage={currentPage} />

      <div className="flex flex-1">
        <Sidebar currentPage={currentPage} onNavigate={handleNavigate} />

        <main className="flex-1 p-3 sm:p-5 lg:p-7 max-w-7xl mx-auto w-full overflow-x-hidden flex flex-col justify-between">
          <div className="flex-1">
            <Suspense
              fallback={
                <div className="flex items-center justify-center py-20">
                  <div className="w-8 h-8 rounded-full border-3 border-teal-500/30 border-t-teal-500 animate-spin" />
                </div>
              }
            >
              {renderPage()}
            </Suspense>
          </div>
          <Footer onNavigate={handleNavigate} />
        </main>
      </div>

      {/* Mobile Bottom Tab Bar */}
      <MobileBottomNav currentPage={currentPage} onNavigate={handleNavigate} />

      {/* Global Floating Audio Player Bar */}
      <AudioPlayerBar />
    </div>
  );
};

export default App;
