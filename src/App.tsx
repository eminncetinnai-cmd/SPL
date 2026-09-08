import React, { useState, useEffect } from 'react';
import { Navbar } from './components/layout/Navbar';
import { Sidebar } from './components/layout/Sidebar';
import { HomePage } from './pages/HomePage';
import { PracticeQuizPage } from './pages/PracticeQuizPage';
import { SimulationExamPage } from './pages/SimulationExamPage';
import { ResultsPage } from './pages/ResultsPage';
import { StudyNotesPage } from './pages/StudyNotesPage';
import { FlashcardsPage } from './pages/FlashcardsPage';
import { MistakeNotebookPage } from './pages/MistakeNotebookPage';
import { BookmarksPage } from './pages/BookmarksPage';
import { QuestionExplorerPage } from './pages/QuestionExplorerPage';
import { DashboardPage } from './pages/DashboardPage';
import { SettingsPage } from './pages/SettingsPage';
import { CheatSheetPage } from './pages/CheatSheetPage';
import { useSettingsStore } from './stores/settingsStore';
import { ModuleId } from './types/exam';

import { AudioPlayerBar } from './components/audio/AudioPlayerBar';
import { Footer } from './components/layout/Footer';

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

        <main className="flex-1 p-4 sm:p-6 lg:p-8 max-w-7xl mx-auto w-full overflow-x-hidden flex flex-col justify-between">
          <div className="flex-1">
            {renderPage()}
          </div>
          <Footer onNavigate={handleNavigate} />
        </main>
      </div>

      {/* Global Floating Audio Player Bar */}
      <AudioPlayerBar />
    </div>
  );
};

export default App;
