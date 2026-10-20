import React, { useState, useEffect, Suspense, lazy } from 'react';
import { Navbar } from './components/layout/Navbar';
import { Sidebar } from './components/layout/Sidebar';
import { HomePage } from './pages/HomePage';
import { useSettingsStore } from './stores/settingsStore';
import { useQuizStore } from './stores/quizStore';
import { ModuleId } from './types/exam';

import { Footer } from './components/layout/Footer';
import { MobileBottomNav } from './components/layout/MobileBottomNav';

// Lazy-loaded essential study pages
const PracticeQuizPage = lazy(() =>
  import('./pages/PracticeQuizPage').then((m) => ({ default: m.PracticeQuizPage }))
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
const SettingsPage = lazy(() =>
  import('./pages/SettingsPage').then((m) => ({ default: m.SettingsPage }))
);
const CheatSheetPage = lazy(() =>
  import('./pages/CheatSheetPage').then((m) => ({ default: m.CheatSheetPage }))
);

export const App: React.FC = () => {
  const [currentPage, setCurrentPage] = useState<string>('home');
  const [pageParams, setPageParams] = useState<any>({});
  const { theme } = useSettingsStore();
  const { currentSession } = useQuizStore();

  const isQuizActive = Boolean(
    currentSession && !currentSession.is_completed && (currentPage === 'practice' || currentPage === 'simulation')
  );

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
      case 'simulation-prep':
      case 'simulation':
        return (
          <PracticeQuizPage
            initialModuleId={pageParams.moduleId as ModuleId}
            initialFilterMode={pageParams.filterMode}
            initialSourceFilter={pageParams.sourceFilter}
            onNavigate={handleNavigate}
          />
        );
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
      case 'cheat-sheet':
      case 'exam-morning':
        return <CheatSheetPage onNavigate={handleNavigate} />;
      case 'settings':
        return <SettingsPage />;
      default:
        return <HomePage onNavigate={handleNavigate} />;
    }
  };

  // 100% Distraction-Free Pure Exam Cockpit (No Navbar, No Bottom Tabs, No Audio Bar, No Sidebar)
  if (isQuizActive) {
    return (
      <div className="min-h-screen bg-slate-900 dark:bg-fintech-dark text-slate-100 flex flex-col font-sans selection:bg-teal-500/30 selection:text-teal-200 pt-[calc(0.5rem+env(safe-area-inset-top,0px))] pb-[env(safe-area-inset-bottom,0px)] pl-[env(safe-area-inset-left,0px)] pr-[env(safe-area-inset-right,0px)]">
        <main className="flex-1 p-2 sm:p-4 lg:p-6 max-w-5xl mx-auto w-full">
          <Suspense
            fallback={
              <div className="flex items-center justify-center py-20">
                <div className="w-8 h-8 rounded-full border-3 border-teal-500/30 border-t-teal-500 animate-spin" />
              </div>
            }
          >
            {renderPage()}
          </Suspense>
        </main>
      </div>
    );
  }

  return (
    <div className="min-h-screen bg-fintech-dark text-slate-900 dark:text-slate-100 flex flex-col font-sans selection:bg-teal-500/30 selection:text-teal-900 relative">
      <Navbar onNavigate={handleNavigate} currentPage={currentPage} />

      <div className="flex flex-1">
        <Sidebar currentPage={currentPage} onNavigate={handleNavigate} />

        <main className="flex-1 p-3 sm:p-5 lg:p-7 pb-28 md:pb-7 max-w-7xl mx-auto w-full overflow-x-hidden flex flex-col justify-between">
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
    </div>
  );
};

export default App;
