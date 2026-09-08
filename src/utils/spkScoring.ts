import { ModuleId, Question, UserAnswer, QuizSession } from '../types/exam';

export interface ModuleScoreResult {
  module_id: ModuleId;
  total_questions: number;
  answered_count: number;
  correct_count: number;
  wrong_count: number;
  empty_count: number;
  score: number; // 0 - 100
  accuracy_pct: number;
  passed_module_threshold: boolean; // >= 50
}

export interface ExamOverallResult {
  total_questions: number;
  total_correct: number;
  total_wrong: number;
  total_empty: number;
  average_score: number; // 0 - 100
  overall_accuracy: number;
  module_results: Record<ModuleId, ModuleScoreResult>;
  passed_all: boolean;
  status: 'PASSED' | 'FAILED_AVERAGE' | 'FAILED_MODULE_THRESHOLD';
  status_message: string;
  standart_puan_estimate: number;
}

export function calculateQuizResults(
  questions: Question[],
  userAnswers: Record<string, UserAnswer>
): {
  correctCount: number;
  wrongCount: number;
  emptyCount: number;
  score: number;
  accuracyPct: number;
  moduleResults: Record<ModuleId, ModuleScoreResult>;
  overallPassed: boolean;
  statusMessage: string;
} {
  const moduleMap: Record<ModuleId, { total: number; correct: number; wrong: number; empty: number }> = {
    '1001': { total: 0, correct: 0, wrong: 0, empty: 0 },
    '1003': { total: 0, correct: 0, wrong: 0, empty: 0 },
    '1005': { total: 0, correct: 0, wrong: 0, empty: 0 },
    '1012': { total: 0, correct: 0, wrong: 0, empty: 0 },
  };

  let correctCount = 0;
  let wrongCount = 0;
  let emptyCount = 0;

  questions.forEach((q) => {
    const ans = userAnswers[q.id];
    const mod = q.module_id;
    if (moduleMap[mod]) {
      moduleMap[mod].total += 1;
    }

    if (!ans || ans.selected_option === null) {
      emptyCount += 1;
      if (moduleMap[mod]) moduleMap[mod].empty += 1;
    } else if (ans.is_correct) {
      correctCount += 1;
      if (moduleMap[mod]) moduleMap[mod].correct += 1;
    } else {
      wrongCount += 1;
      if (moduleMap[mod]) moduleMap[mod].wrong += 1;
    }
  });

  const total = questions.length || 1;
  const score = Math.round((correctCount / total) * 100);
  const accuracyPct = Math.round((correctCount / total) * 1000) / 10;

  const moduleResults: Record<ModuleId, ModuleScoreResult> = {} as any;
  let hasFailedModuleThreshold = false;

  (Object.keys(moduleMap) as ModuleId[]).forEach((modId) => {
    const item = moduleMap[modId];
    if (item.total > 0) {
      const modScore = Math.round((item.correct / item.total) * 100);
      const modAccuracy = Math.round((item.correct / item.total) * 1000) / 10;
      const passedMod = modScore >= 50;
      if (!passedMod) {
        hasFailedModuleThreshold = true;
      }
      moduleResults[modId] = {
        module_id: modId,
        total_questions: item.total,
        answered_count: item.correct + item.wrong,
        correct_count: item.correct,
        wrong_count: item.wrong,
        empty_count: item.empty,
        score: modScore,
        accuracy_pct: modAccuracy,
        passed_module_threshold: passedMod,
      };
    }
  });

  const isMultipleModules = Object.keys(moduleResults).length > 1;
  let overallPassed = false;
  let statusMessage = '';

  if (isMultipleModules) {
    if (score >= 60 && !hasFailedModuleThreshold) {
      overallPassed = true;
      statusMessage = 'TEBRİKLER! SPK Düzey 1 Sınav Barajını Geçtiniz (Ortalama ≥ 60 & Her Modül ≥ 50)';
    } else if (score >= 60 && hasFailedModuleThreshold) {
      overallPassed = false;
      statusMessage = 'ŞARTLI: Genel ortalamanız 60 ve üzeri ancak 50 puan altı kalan modülünüz var.';
    } else {
      overallPassed = false;
      statusMessage = 'BARAJ ALTI: Genel ortalama 60 puanın altında kaldı (Hedef: Ortalama ≥ 60).';
    }
  } else {
    // Single module quiz
    overallPassed = score >= 50;
    statusMessage = overallPassed
      ? 'BAŞARILI: Modül Barajını Geçtiniz (Puan ≥ 50)'
      : 'YETERSİZ: Modül Barajı 50 Puandır. Tekrar çalışmanız önerilir.';
  }

  return {
    correctCount,
    wrongCount,
    emptyCount,
    score,
    accuracyPct,
    moduleResults,
    overallPassed,
    statusMessage,
  };
}

export function formatDuration(seconds: number): string {
  const mins = Math.floor(seconds / 60);
  const secs = seconds % 60;
  if (mins === 0) {
    return `${secs} sn`;
  }
  return `${mins} dk ${secs} sn`;
}
