import { create } from 'zustand';
import { ModuleId, PastQuizSummary, MistakeEntry, Question, QuizSession } from '../types/exam';
import allQuestionsData from '../data/all_questions.json';

interface ModuleStats {
  attempts: number;
  totalQuestions: number;
  totalCorrect: number;
  totalWrong: number;
  averageAccuracy: number;
  bestScore: number;
  lastScore: number | null;
  lastDate: string | null;
}

interface ProgressState {
  history: PastQuizSummary[];
  mistakes: Record<string, MistakeEntry>;
  bookmarks: string[]; // question IDs
  learnedCards: string[]; // flashcard IDs
  starredCards: string[]; // flashcard IDs
  seenQuestionIds: string[]; // question IDs that have been solved in tests
  avoidQuestionRepetition: boolean; // toggle to avoid repeating seen questions
  moduleStats: Record<ModuleId, ModuleStats>;
  
  // Actions
  recordAnswer: (question: Question, selected: string, isCorrect: boolean) => void;
  recordMistakeCorrect: (questionId: string) => void;
  recordQuizCompletion: (session: QuizSession) => void;
  addMistake: (question: Question, selected: string) => void;
  removeMistake: (questionId: string) => void;
  toggleBookmark: (questionId: string) => boolean;
  isBookmarked: (questionId: string) => boolean;
  toggleLearnedCard: (cardId: string) => boolean;
  isCardLearned: (cardId: string) => boolean;
  toggleStarredCard: (cardId: string) => boolean;
  isCardStarred: (cardId: string) => boolean;
  markQuestionsSeen: (questionIds: string[]) => void;
  isQuestionSeen: (questionId: string) => boolean;
  resetSeenQuestions: (moduleId?: ModuleId | 'all') => void;
  setAvoidRepetition: (enabled: boolean) => void;
  getSeenCountByModule: (moduleId: ModuleId) => number;
  clearHistory: () => void;
  clearMistakes: () => void;
  resetSolvedQuestions: (options?: { includeHistory?: boolean }) => void;
  resetAll: () => void;
}

const STORAGE_KEY = 'spk_spl1_progress_v7';

const defaultModuleStats: Record<ModuleId, ModuleStats> = {
  '1001': { attempts: 0, totalQuestions: 0, totalCorrect: 0, totalWrong: 0, averageAccuracy: 0, bestScore: 0, lastScore: null, lastDate: null },
  '1003': { attempts: 0, totalQuestions: 0, totalCorrect: 0, totalWrong: 0, averageAccuracy: 0, bestScore: 0, lastScore: null, lastDate: null },
  '1005': { attempts: 0, totalQuestions: 0, totalCorrect: 0, totalWrong: 0, averageAccuracy: 0, bestScore: 0, lastScore: null, lastDate: null },
  '1012': { attempts: 0, totalQuestions: 0, totalCorrect: 0, totalWrong: 0, averageAccuracy: 0, bestScore: 0, lastScore: null, lastDate: null },
};

const canonicalQuestions = new Map(
  (allQuestionsData as Question[]).map((question) => [question.id, question])
);

function normalizeMistakeEntry(entry: MistakeEntry): MistakeEntry {
  const canonicalQuestion = canonicalQuestions.get(entry.question.id);
  if (!canonicalQuestion) return entry;

  const selectedOption = entry.question.options.find(
    (option) => option.key === entry.last_selected_option
  );
  const canonicalSelectedKey = selectedOption
    ? canonicalQuestion.options.find((option) => option.text === selectedOption.text)?.key
    : undefined;

  return {
    ...entry,
    question: canonicalQuestion,
    last_selected_option: canonicalSelectedKey || entry.last_selected_option,
  };
}

function normalizeMistakes(
  mistakes: Record<string, MistakeEntry>
): Record<string, MistakeEntry> {
  return Object.fromEntries(
    Object.entries(mistakes).map(([questionId, entry]) => [
      questionId,
      normalizeMistakeEntry(entry),
    ])
  );
}

const initialData = (() => {
  try {
    if (typeof localStorage !== 'undefined') {
      // Clear legacy storage versions if any exist to guarantee clean state
      ['spk_spl1_progress_v1', 'spk_spl1_progress_v2', 'spk_spl1_progress_v3', 'spk_spl1_progress_v4', 'spk_spl1_progress_v5', 'spk_spl1_progress_v6'].forEach((oldKey) => {
        try { localStorage.removeItem(oldKey); } catch (e) {}
      });

      const saved = localStorage.getItem(STORAGE_KEY);
      if (saved) {
        const parsed = JSON.parse(saved);
        return {
          history: parsed.history || [],
          mistakes: normalizeMistakes(parsed.mistakes || {}),
          bookmarks: parsed.bookmarks || [],
          learnedCards: parsed.learnedCards || [],
          starredCards: parsed.starredCards || [],
          seenQuestionIds: parsed.seenQuestionIds || [],
          avoidQuestionRepetition: parsed.avoidQuestionRepetition !== undefined ? parsed.avoidQuestionRepetition : true,
          moduleStats: { ...defaultModuleStats, ...(parsed.moduleStats || {}) },
        };
      }
    }
  } catch (e) {
    console.error('Error initializing progressStore:', e);
  }
  return {
    history: [],
    mistakes: {},
    bookmarks: [],
    learnedCards: [],
    starredCards: [],
    seenQuestionIds: [],
    avoidQuestionRepetition: true,
    moduleStats: defaultModuleStats,
  };
})();

const arraySetCache = new WeakMap<string[], Set<string>>();
function getCachedSet(arr: string[]): Set<string> {
  let set = arraySetCache.get(arr);
  if (!set) {
    set = new Set(arr);
    arraySetCache.set(arr, set);
  }
  return set;
}

let pendingStateToSave: Partial<ProgressState> | null = null;
let saveTimeoutId: ReturnType<typeof setTimeout> | null = null;

function flushToStorage(state: Partial<ProgressState>) {
  try {
    if (typeof localStorage === 'undefined') return;
    const dataToSave = {
      history: state.history || [],
      mistakes: state.mistakes || {},
      bookmarks: state.bookmarks || [],
      learnedCards: state.learnedCards || [],
      starredCards: state.starredCards || [],
      seenQuestionIds: state.seenQuestionIds || [],
      avoidQuestionRepetition:
        state.avoidQuestionRepetition !== undefined ? state.avoidQuestionRepetition : true,
      moduleStats: state.moduleStats || defaultModuleStats,
    };
    localStorage.setItem(STORAGE_KEY, JSON.stringify(dataToSave));
  } catch (e) {
    console.error('Failed to save progress to localStorage', e);
  }
}

if (typeof window !== 'undefined') {
  window.addEventListener('beforeunload', () => {
    if (pendingStateToSave) {
      flushToStorage(pendingStateToSave);
      pendingStateToSave = null;
    }
  });
}

function saveToStorage(state: Partial<ProgressState>) {
  pendingStateToSave = state;
  if (saveTimeoutId) {
    clearTimeout(saveTimeoutId);
  }
  saveTimeoutId = setTimeout(() => {
    if (pendingStateToSave) {
      flushToStorage(pendingStateToSave);
      pendingStateToSave = null;
    }
    saveTimeoutId = null;
  }, 120);
}

export const useProgressStore = create<ProgressState>((set, get) => ({
  history: initialData.history,
  mistakes: initialData.mistakes,
  bookmarks: initialData.bookmarks,
  learnedCards: initialData.learnedCards,
  starredCards: initialData.starredCards,
  seenQuestionIds: initialData.seenQuestionIds,
  avoidQuestionRepetition: initialData.avoidQuestionRepetition,
  moduleStats: initialData.moduleStats,

  recordAnswer: (question: Question, selected: string, isCorrect: boolean) => {
    const state = get();
    const mid = question.module_id as ModuleId;
    const current = state.moduleStats[mid] || { ...defaultModuleStats[mid] };

    const newTotalQ = current.totalQuestions + 1;
    const newTotalCorrect = current.totalCorrect + (isCorrect ? 1 : 0);
    const newTotalWrong = current.totalWrong + (isCorrect ? 0 : 1);
    const newAccuracy = Math.round((newTotalCorrect / newTotalQ) * 100);

    const updatedStats = {
      ...state.moduleStats,
      [mid]: {
        ...current,
        totalQuestions: newTotalQ,
        totalCorrect: newTotalCorrect,
        totalWrong: newTotalWrong,
        averageAccuracy: newAccuracy,
        lastDate: new Date().toISOString(),
      },
    };

    // Mark as seen only if not already in set
    const seenSet = getCachedSet(state.seenQuestionIds);
    const newSeenQuestionIds = seenSet.has(question.id)
      ? state.seenQuestionIds
      : [...state.seenQuestionIds, question.id];

    // Compute updated mistakes in the same pass (single Zustand set + single storage write)
    let newMistakes = state.mistakes;
    if (!isCorrect) {
      const existingMistake = state.mistakes[question.id];
      const newCount = existingMistake ? existingMistake.wrong_count + 1 : 1;
      const canonicalQuestion = canonicalQuestions.get(question.id) || question;
      const selectedOption = question.options.find((option) => option.key === selected);
      const canonicalSelected = selectedOption
        ? canonicalQuestion.options.find((option) => option.text === selectedOption.text)?.key
        : undefined;
      newMistakes = {
        ...state.mistakes,
        [question.id]: {
          question: canonicalQuestion,
          wrong_count: newCount,
          last_wrong_date: new Date().toISOString(),
          last_selected_option: canonicalSelected || selected,
          correct_streak: 0,
          resolved: false,
        },
      };
    } else {
      const existingMistake = state.mistakes[question.id];
      if (existingMistake && !existingMistake.resolved) {
        const correctStreak = (existingMistake.correct_streak || 0) + 1;
        newMistakes = {
          ...state.mistakes,
          [question.id]: {
            ...existingMistake,
            correct_streak: correctStreak,
            resolved: correctStreak >= 2,
          },
        };
      }
    }

    set({
      moduleStats: updatedStats,
      seenQuestionIds: newSeenQuestionIds,
      mistakes: newMistakes,
    });

    saveToStorage({
      ...get(),
      moduleStats: updatedStats,
      seenQuestionIds: newSeenQuestionIds,
      mistakes: newMistakes,
    });
  },

  recordMistakeCorrect: (questionId: string) => {
    const current = get().mistakes[questionId];
    if (!current || current.resolved) return;

    const correctStreak = (current.correct_streak || 0) + 1;
    const updatedEntry: MistakeEntry = {
      ...current,
      correct_streak: correctStreak,
      resolved: correctStreak >= 2,
    };
    const newMistakes = {
      ...get().mistakes,
      [questionId]: updatedEntry,
    };

    set({ mistakes: newMistakes });
    saveToStorage({ ...get(), mistakes: newMistakes });
  },

  recordQuizCompletion: (session: QuizSession) => {
    const summary: PastQuizSummary = {
      id: session.id,
      mode: session.mode,
      module_id: session.module_id || 'all',
      title: session.title,
      date: new Date().toISOString(),
      total_questions: session.questions.length,
      correct_count: session.correct_count || 0,
      wrong_count: session.wrong_count || 0,
      empty_count: session.empty_count || 0,
      score: session.score || 0,
      accuracy_pct: session.accuracy_pct || 0,
      duration_seconds: session.duration_seconds,
      overall_passed: session.overall_passed || false,
    };

    const newHistory = [summary, ...get().history];

    // Automatically mark all questions from this session as seen
    const existingSeen = new Set(get().seenQuestionIds);
    session.questions.forEach((q) => {
      const answer = session.user_answers[q.id];
      if (answer?.selected_option !== null && answer?.selected_option !== undefined) {
        existingSeen.add(q.id);
      }
    });
    const newSeenQuestionIds = Array.from(existingSeen);

    // Update module stats
    const updatedStats = { ...get().moduleStats };
    if (session.module_breakdown) {
      Object.entries(session.module_breakdown).forEach(([modId, stats]) => {
        const mid = modId as ModuleId;
        const current = updatedStats[mid] || { ...defaultModuleStats[mid] };
        
        const newAttempts = current.attempts + 1;
        const newBestScore = Math.max(current.bestScore, stats.score);

        // In simulation mode, individual answers weren't recorded during test.
        // Therefore, accumulate them cumulatively now. In practice mode, recordAnswer already counted them.
        let newTotalQ = current.totalQuestions;
        let newTotalCorrect = current.totalCorrect;
        let newTotalWrong = current.totalWrong;

        if (session.mode === 'simulation') {
          newTotalQ += stats.total;
          newTotalCorrect += stats.correct;
          newTotalWrong += stats.wrong;
        } else {
          newTotalQ = Math.max(newTotalQ, current.totalQuestions);
          newTotalCorrect = Math.max(newTotalCorrect, current.totalCorrect);
          newTotalWrong = Math.max(newTotalWrong, current.totalWrong);
        }

        const newAccuracy = newTotalQ > 0 ? Math.round((newTotalCorrect / newTotalQ) * 100) : current.averageAccuracy;

        updatedStats[mid] = {
          attempts: newAttempts,
          totalQuestions: newTotalQ,
          totalCorrect: newTotalCorrect,
          totalWrong: newTotalWrong,
          averageAccuracy: newAccuracy,
          bestScore: newBestScore,
          lastScore: stats.score,
          lastDate: new Date().toISOString(),
        };
      });
    }

    // Automatically record all mistakes
    if (session.user_answers && session.mode === 'simulation') {
      session.questions.forEach((q) => {
        const ans = session.user_answers[q.id];
        if (ans && ans.selected_option !== null) {
          if (!ans.is_correct) {
            get().addMistake(q, ans.selected_option);
          } else {
            get().recordMistakeCorrect(q.id);
          }
        }
      });
    }

    set({
      history: newHistory,
      seenQuestionIds: newSeenQuestionIds,
      moduleStats: updatedStats,
    });

    saveToStorage({
      ...get(),
      history: newHistory,
      seenQuestionIds: newSeenQuestionIds,
      moduleStats: updatedStats,
    });
  },

  markQuestionsSeen: (questionIds: string[]) => {
    const existingSeen = new Set(get().seenQuestionIds);
    let changed = false;
    questionIds.forEach((id) => {
      if (!existingSeen.has(id)) {
        existingSeen.add(id);
        changed = true;
      }
    });

    if (changed) {
      const newSeenQuestionIds = Array.from(existingSeen);
      set({ seenQuestionIds: newSeenQuestionIds });
      saveToStorage({ ...get(), seenQuestionIds: newSeenQuestionIds });
    }
  },

  isQuestionSeen: (questionId: string) => {
    return getCachedSet(get().seenQuestionIds).has(questionId);
  },

  resetSeenQuestions: (moduleId?: ModuleId | 'all') => {
    if (!moduleId || moduleId === 'all') {
      set({ seenQuestionIds: [] });
      saveToStorage({ ...get(), seenQuestionIds: [] });
    } else {
      // Keep seen questions from other modules, reset only for this module
      const filtered = get().seenQuestionIds.filter(
        (id) => canonicalQuestions.get(id)?.module_id !== moduleId
      );
      set({ seenQuestionIds: filtered });
      saveToStorage({ ...get(), seenQuestionIds: filtered });
    }
  },

  setAvoidRepetition: (enabled: boolean) => {
    set({ avoidQuestionRepetition: enabled });
    saveToStorage({ ...get(), avoidQuestionRepetition: enabled });
  },

  getSeenCountByModule: (moduleId: ModuleId) => {
    let count = 0;
    const seen = get().seenQuestionIds;
    for (let i = 0; i < seen.length; i++) {
      if (canonicalQuestions.get(seen[i])?.module_id === moduleId) {
        count++;
      }
    }
    return count;
  },

  addMistake: (question: Question, selected: string) => {
    const current = get().mistakes[question.id];
    const newCount = current ? current.wrong_count + 1 : 1;
    const canonicalQuestion = canonicalQuestions.get(question.id) || question;
    const selectedOption = question.options.find((option) => option.key === selected);
    const canonicalSelected = selectedOption
      ? canonicalQuestion.options.find((option) => option.text === selectedOption.text)?.key
      : undefined;
    const entry: MistakeEntry = {
      question: canonicalQuestion,
      wrong_count: newCount,
      last_wrong_date: new Date().toISOString(),
      last_selected_option: canonicalSelected || selected,
      correct_streak: 0,
      resolved: false,
    };

    const newMistakes = {
      ...get().mistakes,
      [question.id]: entry,
    };

    set({ mistakes: newMistakes });
    saveToStorage({ ...get(), mistakes: newMistakes });
  },

  removeMistake: (questionId: string) => {
    const current = get().mistakes[questionId];
    if (current) {
      const newMistakes = {
        ...get().mistakes,
        [questionId]: { ...current, resolved: true },
      };
      set({ mistakes: newMistakes });
      saveToStorage({ ...get(), mistakes: newMistakes });
    }
  },

  toggleBookmark: (questionId: string) => {
    let bookmarks = [...get().bookmarks];
    const index = bookmarks.indexOf(questionId);
    let isNowBookmarked = false;
    if (index >= 0) {
      bookmarks.splice(index, 1);
      isNowBookmarked = false;
    } else {
      bookmarks.push(questionId);
      isNowBookmarked = true;
    }
    set({ bookmarks });
    saveToStorage({ ...get(), bookmarks });
    return isNowBookmarked;
  },

  isBookmarked: (questionId: string) => {
    return getCachedSet(get().bookmarks).has(questionId);
  },

  toggleLearnedCard: (cardId) => {
    let learnedCards = [...get().learnedCards];
    const index = learnedCards.indexOf(cardId);
    let isNowLearned = false;
    if (index >= 0) {
      learnedCards.splice(index, 1);
      isNowLearned = false;
    } else {
      learnedCards.push(cardId);
      isNowLearned = true;
    }
    set({ learnedCards });
    saveToStorage({ ...get(), learnedCards });
    return isNowLearned;
  },

  isCardLearned: (cardId) => {
    return getCachedSet(get().learnedCards).has(cardId);
  },

  toggleStarredCard: (cardId) => {
    let starredCards = [...get().starredCards];
    const index = starredCards.indexOf(cardId);
    let isNowStarred = false;
    if (index >= 0) {
      starredCards.splice(index, 1);
      isNowStarred = false;
    } else {
      starredCards.push(cardId);
      isNowStarred = true;
    }
    set({ starredCards });
    saveToStorage({ ...get(), starredCards });
    return isNowStarred;
  },

  isCardStarred: (cardId) => {
    return getCachedSet(get().starredCards).has(cardId);
  },

  clearHistory: () => {
    set({ history: [], moduleStats: defaultModuleStats });
    saveToStorage({ ...get(), history: [], moduleStats: defaultModuleStats });
  },

  clearMistakes: () => {
    set({ mistakes: {} });
    saveToStorage({ ...get(), mistakes: {} });
  },

  resetSolvedQuestions: (options?: { includeHistory?: boolean }) => {
    if (options?.includeHistory) {
      set({
        seenQuestionIds: [],
        history: [],
        moduleStats: defaultModuleStats,
      });
      saveToStorage({
        ...get(),
        seenQuestionIds: [],
        history: [],
        moduleStats: defaultModuleStats,
      });
    } else {
      set({ seenQuestionIds: [] });
      saveToStorage({ ...get(), seenQuestionIds: [] });
    }
  },

  resetAll: () => {
    set({
      history: [],
      mistakes: {},
      bookmarks: [],
      learnedCards: [],
      starredCards: [],
      seenQuestionIds: [],
      avoidQuestionRepetition: true,
      moduleStats: defaultModuleStats,
    });
    saveToStorage({
      history: [],
      mistakes: {},
      bookmarks: [],
      learnedCards: [],
      starredCards: [],
      seenQuestionIds: [],
      avoidQuestionRepetition: true,
      moduleStats: defaultModuleStats,
    });
  },
}));
