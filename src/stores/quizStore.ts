import { create } from 'zustand';
import { ModuleId, Question, QuizMode, QuizSession, UserAnswer } from '../types/exam';
import { calculateQuizResults } from '../utils/spkScoring';
import { useProgressStore } from './progressStore';
import { selectSmartQuestions, shuffleArray, shuffleQuestionOptions } from '../utils/questionSelector';
import allQuestionsData from '../data/all_questions.json';

interface StartQuizOptions {
  mode: QuizMode;
  moduleId?: ModuleId | 'all';
  questionCount?: number;
  sourceFilter?: 'all' | 'master' | 'cikmis' | 'ogretici' | 'konu' | 'genel';
  filterMode?: 'unseen' | 'all' | 'mistakes' | 'bookmarks';
  customQuestions?: Question[];
  title?: string;
  timeLimitMinutes?: number;
}

interface QuizState {
  currentSession: QuizSession | null;
  activeQuestion: Question | null;
  activeAnswer: UserAnswer | null;
  isAnswerLocked: boolean; // In practice mode, lock answer once selected
  explanationRead: boolean; // In practice mode, next button requires explanation view
  
  // Actions
  startQuiz: (options: StartQuizOptions) => void;
  selectOption: (optionKey: 'A' | 'B' | 'C' | 'D' | 'E') => void;
  unlockOrChangeAnswer: () => void;
  setExplanationRead: (read: boolean) => void;
  toggleReviewFlag: (questionId: string) => void;
  goToQuestion: (index: number) => void;
  nextQuestion: () => boolean;
  prevQuestion: () => boolean;
  finishQuiz: () => QuizSession | null;
  resetSession: () => void;
  updateTimer: (elapsedSeconds: number) => void;
}

const allQuestions = allQuestionsData as Question[];

export const useQuizStore = create<QuizState>((set, get) => ({
  currentSession: null,
  activeQuestion: null,
  activeAnswer: null,
  isAnswerLocked: false,
  explanationRead: false,

  startQuiz: (options) => {
    let selectedQuestions: Question[] = [];

    if (options.customQuestions && options.customQuestions.length > 0) {
      // Group by module to preserve official exam section boundaries (1001 -> 1003 -> 1005 -> 1012),
      // and random-shuffle the questions strictly within each module!
      const moduleMap: Record<string, Question[]> = {};
      const moduleOrder: string[] = [];
      
      options.customQuestions.forEach((q) => {
        const mod = q.module_id || 'all';
        if (!moduleMap[mod]) {
          moduleMap[mod] = [];
          moduleOrder.push(mod);
        }
        moduleMap[mod].push(q);
      });

      let shuffledGrouped: Question[] = [];
      moduleOrder.forEach((mod) => {
        shuffledGrouped = [...shuffledGrouped, ...shuffleArray(moduleMap[mod])];
      });
      selectedQuestions = shuffledGrouped;
    } else if (options.filterMode === 'mistakes') {
      const { mistakes } = useProgressStore.getState();
      const unresolvedMistakeIds = new Set(
        Object.values(mistakes).filter((m) => !m.resolved).map((m) => m.question.id)
      );
      let mistakePool = allQuestions.filter((q) => unresolvedMistakeIds.has(q.id));
      if (options.moduleId && options.moduleId !== 'all') {
        mistakePool = mistakePool.filter((q) => q.module_id === options.moduleId);
      }
      selectedQuestions = shuffleArray(mistakePool).slice(0, options.questionCount || 25);
    } else if (options.filterMode === 'bookmarks') {
      const { bookmarks } = useProgressStore.getState();
      const bookmarkIds = new Set(bookmarks);
      let bookmarkPool = allQuestions.filter((q) => bookmarkIds.has(q.id));
      if (options.moduleId && options.moduleId !== 'all') {
        bookmarkPool = bookmarkPool.filter((q) => q.module_id === options.moduleId);
      }
      selectedQuestions = shuffleArray(bookmarkPool).slice(0, options.questionCount || 25);
    } else {
      const { seenQuestionIds, avoidQuestionRepetition } = useProgressStore.getState();
      const selection = selectSmartQuestions(allQuestions, {
        moduleId: options.moduleId,
        count: options.questionCount || 25,
        sourceFilter: options.sourceFilter || 'all',
        filterMode: options.filterMode || 'unseen',
        seenQuestionIds,
        avoidRepetition: options.filterMode === 'all' ? false : avoidQuestionRepetition,
      });
      selectedQuestions = shuffleArray(selection.questions);
    }

    if (selectedQuestions.length === 0) {
      alert('Seçilen kriterlere uygun soru bulunamadı.');
      return;
    }

    // Shuffles options (A, B, C, D, E) for every question and re-maps correct_answer dynamically
    selectedQuestions = selectedQuestions.map(shuffleQuestionOptions);

    // Mark questions as seen so they are not repeated in future tests
    useProgressStore.getState().markQuestionsSeen(selectedQuestions.map((q) => q.id));

    const sessionId = `session_${Date.now()}_${Math.random().toString(36).substring(2, 7)}`;
    const timeLimitSeconds = options.timeLimitMinutes
      ? options.timeLimitMinutes * 60
      : options.mode === 'simulation'
      ? selectedQuestions.length * 72 // ~1.2 mins per question (SPK standard: 100 questions = 120 mins)
      : undefined;

    let title = options.title || 'SPK Modül Testi';
    if (!options.title) {
      if (options.mode === 'simulation') {
        title = options.moduleId === 'all' || !options.moduleId
          ? 'SPK Düzey 1 Tam Sınav Simülasyonu (4 Modül)'
          : `Modül ${options.moduleId} Süreli Deneme Sınavı`;
      } else if (options.mode === 'mistakes') {
        title = 'Yanlış Sorular Tekrar Testi';
      } else if (options.mode === 'bookmarks') {
        title = 'Yıldızlı Sorular Çalışma Testi';
      } else {
        const sourceLabel = options.sourceFilter === 'cikmis'
          ? 'Çıkmış Sınav'
          : options.sourceFilter === 'genel'
          ? 'Genel Soru Havuzu'
          : options.sourceFilter === 'master' 
          ? 'Master Soru' 
          : options.sourceFilter === 'ogretici' 
          ? 'Öğretici & Tuzak' 
          : options.sourceFilter === 'konu'
          ? 'Konu Anlatımı'
          : 'Pratik Çalışma';
        title = options.moduleId && options.moduleId !== 'all'
          ? `Modül ${options.moduleId} ${sourceLabel} Testi`
          : `Genel SPK ${sourceLabel} Testi`;
      }
    }

    const initialAnswers: Record<string, UserAnswer> = {};
    selectedQuestions.forEach((q) => {
      initialAnswers[q.id] = {
        question_id: q.id,
        module_id: q.module_id,
        selected_option: null,
        correct_option: q.correct_answer,
        is_correct: false,
        time_spent_seconds: 0,
        marked_for_review: false,
      };
    });

    const newSession: QuizSession = {
      id: sessionId,
      mode: options.mode,
      module_id: options.moduleId || 'all',
      title,
      started_at: new Date().toISOString(),
      duration_seconds: 0,
      time_limit_seconds: timeLimitSeconds,
      questions: selectedQuestions,
      current_index: 0,
      user_answers: initialAnswers,
      is_completed: false,
    };

    set({
      currentSession: newSession,
      activeQuestion: selectedQuestions[0],
      activeAnswer: initialAnswers[selectedQuestions[0].id],
      isAnswerLocked: false,
      explanationRead: false,
    });
  },

  selectOption: (optionKey) => {
    const { currentSession, activeQuestion, isAnswerLocked } = get();
    if (!currentSession || !activeQuestion) return;

    // In practice mode, if already locked, do not allow changing
    if (currentSession.mode === 'practice' && isAnswerLocked) return;

    const isCorrect = activeQuestion.correct_answer === optionKey;
    const currentAnswer = currentSession.user_answers[activeQuestion.id] || {
      question_id: activeQuestion.id,
      module_id: activeQuestion.module_id,
      selected_option: null,
      correct_option: activeQuestion.correct_answer,
      is_correct: false,
      time_spent_seconds: 0,
      marked_for_review: false,
    };

    const updatedAnswer: UserAnswer = {
      ...currentAnswer,
      selected_option: optionKey,
      is_correct: isCorrect,
    };

    const updatedUserAnswers = {
      ...currentSession.user_answers,
      [activeQuestion.id]: updatedAnswer,
    };

    const updatedSession = {
      ...currentSession,
      user_answers: updatedUserAnswers,
    };

    set({
      currentSession: updatedSession,
      activeAnswer: updatedAnswer,
      isAnswerLocked: currentSession.mode === 'practice', // Practice mode locks immediately
      explanationRead: currentSession.mode !== 'practice',
    });

    // In practice mode, immediately persist question answer to progressStore
    if (currentSession.mode === 'practice') {
      useProgressStore.getState().recordAnswer(activeQuestion, optionKey, isCorrect);
    }
  },

  unlockOrChangeAnswer: () => {
    set({ isAnswerLocked: false });
  },

  setExplanationRead: (read) => {
    set({ explanationRead: read });
  },

  toggleReviewFlag: (questionId) => {
    const { currentSession } = get();
    if (!currentSession) return;

    const currentAnswer = currentSession.user_answers[questionId];
    if (!currentAnswer) return;

    const updatedAnswer = {
      ...currentAnswer,
      marked_for_review: !currentAnswer.marked_for_review,
    };

    set({
      currentSession: {
        ...currentSession,
        user_answers: {
          ...currentSession.user_answers,
          [questionId]: updatedAnswer,
        },
      },
      activeAnswer: get().activeQuestion?.id === questionId ? updatedAnswer : get().activeAnswer,
    });
  },

  goToQuestion: (index) => {
    const { currentSession } = get();
    if (!currentSession || index < 0 || index >= currentSession.questions.length) return;

    const nextQ = currentSession.questions[index];
    const nextAns = currentSession.user_answers[nextQ.id];
    const isLocked = currentSession.mode === 'practice' && nextAns?.selected_option !== null;

    set({
      currentSession: {
        ...currentSession,
        current_index: index,
      },
      activeQuestion: nextQ,
      activeAnswer: nextAns || null,
      isAnswerLocked: isLocked,
      explanationRead: currentSession.mode !== 'practice' || !isLocked,
    });
  },

  nextQuestion: () => {
    const { currentSession } = get();
    if (!currentSession) return false;

    const nextIdx = currentSession.current_index + 1;
    if (nextIdx < currentSession.questions.length) {
      get().goToQuestion(nextIdx);
      return true;
    }
    return false;
  },

  prevQuestion: () => {
    const { currentSession } = get();
    if (!currentSession) return false;

    const prevIdx = currentSession.current_index - 1;
    if (prevIdx >= 0) {
      get().goToQuestion(prevIdx);
      return true;
    }
    return false;
  },

  updateTimer: (elapsedSeconds) => {
    const { currentSession } = get();
    if (!currentSession || currentSession.is_completed) return;

    set({
      currentSession: {
        ...currentSession,
        duration_seconds: elapsedSeconds,
      },
    });
  },

  finishQuiz: () => {
    const { currentSession } = get();
    if (!currentSession) return null;

    const result = calculateQuizResults(currentSession.questions, currentSession.user_answers);

    const completedSession: QuizSession = {
      ...currentSession,
      is_completed: true,
      ended_at: new Date().toISOString(),
      score: result.score,
      accuracy_pct: result.accuracyPct,
      correct_count: result.correctCount,
      wrong_count: result.wrongCount,
      empty_count: result.emptyCount,
      module_breakdown: result.moduleResults as any,
      overall_passed: result.overallPassed,
    };

    // Save into persistent store
    useProgressStore.getState().recordQuizCompletion(completedSession);

    set({
      currentSession: completedSession,
    });

    return completedSession;
  },

  resetSession: () => {
    set({
      currentSession: null,
      activeQuestion: null,
      activeAnswer: null,
      isAnswerLocked: false,
      explanationRead: false,
    });
  },
}));
