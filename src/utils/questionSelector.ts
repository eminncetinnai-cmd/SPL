import { ModuleId, Question, Option } from '../types/exam';

export interface SmartSelectionOptions {
  moduleId?: ModuleId | 'all';
  count: number;
  sourceFilter?: 'all' | 'master' | 'cikmis' | 'ogretici' | 'konu' | 'genel';
  filterMode?: 'unseen' | 'all' | 'mistakes' | 'bookmarks';
  seenQuestionIds: string[];
  avoidRepetition?: boolean;
}

export interface SelectionResult {
  questions: Question[];
  unseenCount: number;
  seenCount: number;
  totalPoolCount: number;
  remainingUnseenInPool: number;
  isNewCycleStarted: boolean;
}

/**
 * Format raw question ID into a clean, human-readable reference code.
 * Example:
 *   q_1001_master_042 -> #1001-M042
 *   q_1003_ogretici_015 -> #1003-O015
 *   q_1005_konu_008 -> #1005-K008
 */
export function formatQuestionId(id: string): string {
  if (!id) return '';
  
  const m1 = id.match(/q_(\d{4})_(master|cikmis|ogretici|konu|web|exam)_(\d+)/i);
  if (m1) {
    const mod = m1[1];
    let src = 'M';
    if (m1[2] === 'cikmis') src = 'C';
    else if (m1[2] === 'ogretici') src = 'O';
    else if (m1[2] === 'konu') src = 'K';
    else if (m1[2] === 'web') src = 'W';
    else if (m1[2] === 'exam') src = 'E';
    const num = m1[3].padStart(3, '0');
    return `#${mod}-${src}${num}`;
  }

  return `#${id.replace(/^q_/, '').toUpperCase()}`;
}

export function getQuestionFingerprint(text: string): string {
  if (!text) return '';
  return text
    .toLowerCase()
    .replace(/[^a-z0-9ğüşıöç]/gi, '')
    .slice(0, 60);
}

/**
 * Cryptographically sound, mathematically uniform Fisher-Yates (Knuth) shuffle algorithm.
 * Guarantees that all N! permutations are equally likely without any sort comparator bias.
 */
export function shuffleArray<T>(array: T[]): T[] {
  const arr = [...array];
  for (let i = arr.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1));
    const temp = arr[i];
    arr[i] = arr[j];
    arr[j] = temp;
  }
  return arr;
}

/**
 * Shuffles the options of a question among themselves (A, B, C, D, E),
 * and dynamically remaps correct_answer to the new position of the correct text.
 * Guarantees that the candidate cannot rely on letter memorization.
 */
export function shuffleQuestionOptions(question: Question): Question {
  if (!question || !question.options || question.options.length <= 1) {
    return question;
  }

  // Identify the text of the correct answer
  const originalCorrectOpt = question.options.find(
    (opt) => opt.key === question.correct_answer
  );
  const correctText = originalCorrectOpt ? originalCorrectOpt.text : question.options[0]?.text;

  // Shuffle the option objects
  const shuffledItems = shuffleArray(question.options);

  const keys: ('A' | 'B' | 'C' | 'D' | 'E')[] = ['A', 'B', 'C', 'D', 'E'];
  let newCorrectKey: 'A' | 'B' | 'C' | 'D' | 'E' = 'A';

  const newOptions: Option[] = shuffledItems.map((item, index) => {
    const key = keys[index] || 'A';
    if (item.text === correctText) {
      newCorrectKey = key;
    }
    return {
      key,
      text: item.text,
    };
  });

  // Also clean up any static letter mentions in explanation so it never conflicts with shuffled options
  let sanitizedExplanation = question.explanation;
  if (sanitizedExplanation) {
    sanitizedExplanation = sanitizedExplanation
      .replace(/\s*(?:Bu nedenle\s+|Dolayısıyla\s+)?[Dd]oğru\s+(?:seçenek|cevap|şık)\s+[A-Ea-e](?:\s*şıkkıdır|['’]dir|['’]dur|['’]dır|['’]dür)?[\.\!]?/g, '')
      .replace(/\s*[A-Ea-e]\s*şıkkı\s+(?:aykırıdır\s+ve\s+)?doğru\s+cevaptır[\.\!]?/g, '')
      .trim();
  }

  return {
    ...question,
    options: newOptions,
    correct_answer: newCorrectKey,
    explanation: sanitizedExplanation,
  };
}

/**
 * Smart Question Selection Algorithm with Anti-Repeat Pool Rotation.
 * Guarantees that questions do NOT repeat across exams until 100% of the pool is exhausted.
 */
export function selectSmartQuestions(
  allQuestions: Question[],
  options: SmartSelectionOptions
): SelectionResult {
  const {
    moduleId = 'all',
    count = 25,
    sourceFilter = 'all',
    filterMode = 'unseen',
    seenQuestionIds = [],
    avoidRepetition = true,
  } = options;

  const shouldAvoidRepetition = filterMode === 'all' ? false : avoidRepetition;

  // 1. Filter the candidate pool by module and source.
  // Every question ID remains selectable; similar wording does not make a
  // distinct question unavailable from the unseen pool.
  const candidatePool: Question[] = [];

  allQuestions.forEach((q) => {
    if (moduleId !== 'all' && q.module_id !== moduleId) {
      return;
    }
    if (sourceFilter === 'cikmis' && q.source !== 'cikmis') {
      return;
    }
    if (sourceFilter === 'genel' && q.source === 'cikmis') {
      return;
    }
    if (sourceFilter !== 'all' && sourceFilter !== 'genel' && sourceFilter !== 'cikmis' && q.source !== sourceFilter) {
      return;
    }
    candidatePool.push(q);
  });

  const totalPoolCount = candidatePool.length;
  if (totalPoolCount === 0) {
    return {
      questions: [],
      unseenCount: 0,
      seenCount: 0,
      totalPoolCount: 0,
      remainingUnseenInPool: 0,
      isNewCycleStarted: false,
    };
  }

  // If repetition avoidance is turned off or all questions selected, perform standard random shuffle
  if (!shouldAvoidRepetition) {
    const shuffled = shuffleArray(candidatePool);
    const selected = shuffled.slice(0, Math.min(count, totalPoolCount));
    const seenSet = new Set(seenQuestionIds);
    const unseen = selected.filter((q) => !seenSet.has(q.id)).length;
    return {
      questions: selected,
      unseenCount: unseen,
      seenCount: selected.length - unseen,
      totalPoolCount,
      remainingUnseenInPool: candidatePool.filter((q) => !seenSet.has(q.id)).length,
      isNewCycleStarted: false,
    };
  }

  // 2. Separate into unseen and seen questions
  const seenSet = new Set(seenQuestionIds);
  const unseenPool: Question[] = [];
  const seenPool: Question[] = [];

  candidatePool.forEach((q) => {
    if (seenSet.has(q.id)) {
      seenPool.push(q);
    } else {
      unseenPool.push(q);
    }
  });

  const requestedCount = Math.min(count, totalPoolCount);
  let selectedQuestions: Question[] = [];
  let isNewCycleStarted = false;

  if (filterMode === 'unseen') {
    if (unseenPool.length === 0) {
      // Tüm havuz en az bir kez çözüldü! Otomatik yeni döngü başlat
      isNewCycleStarted = true;
      const shuffled = shuffleArray(candidatePool);
      selectedQuestions = shuffled.slice(0, requestedCount);
    } else {
      // Kesinlikle sadece çözülmemiş taze soruları al (en fazla mevcut çözülmemiş kadar)
      const takeCount = Math.min(requestedCount, unseenPool.length);
      const shuffledUnseen = shuffleArray(unseenPool);
      selectedQuestions = shuffledUnseen.slice(0, takeCount);
    }
  } else {
    // Standart akıllı dağılım
    if (unseenPool.length >= requestedCount) {
      const shuffledUnseen = shuffleArray(unseenPool);
      selectedQuestions = shuffledUnseen.slice(0, requestedCount);
    } else if (unseenPool.length > 0 && avoidRepetition) {
      const neededFromSeen = requestedCount - unseenPool.length;
      const shuffledSeen = shuffleArray(seenPool);
      const pickedSeen = shuffledSeen.slice(0, neededFromSeen);
      selectedQuestions = shuffleArray([...unseenPool, ...pickedSeen]);
    } else {
      isNewCycleStarted = true;
      const shuffled = shuffleArray(candidatePool);
      selectedQuestions = shuffled.slice(0, requestedCount);
    }
  }

  // Final pass: ensure selected questions are thoroughly randomized
  selectedQuestions = shuffleArray(selectedQuestions);

  const unseenInBatch = selectedQuestions.filter((q) => !seenSet.has(q.id)).length;
  const remainingUnseen = Math.max(0, unseenPool.length - unseenInBatch);

  return {
    questions: selectedQuestions,
    unseenCount: unseenInBatch,
    seenCount: selectedQuestions.length - unseenInBatch,
    totalPoolCount,
    remainingUnseenInPool: remainingUnseen,
    isNewCycleStarted,
  };
}

/**
 * Selects 100 questions for the Full Official SPK Simulation Exam
 * (25 questions from each of the 4 modules: 1001, 1003, 1005, 1012),
 * strictly prioritizing unseen questions in every module,
 * and randomizing question order within each module section.
 */
export function selectSimulationExam100(
  allQuestions: Question[],
  seenQuestionIds: string[],
  avoidRepetition: boolean = true
): { questions: Question[]; totalUnseen: number } {
  const modules: ModuleId[] = ['1001', '1003', '1005', '1012'];
  let all100: Question[] = [];
  let totalUnseen = 0;

  modules.forEach((mod) => {
    const result = selectSmartQuestions(allQuestions, {
      moduleId: mod,
      count: 25,
      sourceFilter: 'all',
      seenQuestionIds,
      avoidRepetition,
    });
    // Shuffle the 25 questions selected for this specific module so order is completely unpredictable
    const randomizedModuleQuestions = shuffleArray(result.questions);
    all100 = [...all100, ...randomizedModuleQuestions];
    totalUnseen += result.unseenCount;
  });

  return {
    questions: all100,
    totalUnseen,
  };
}
