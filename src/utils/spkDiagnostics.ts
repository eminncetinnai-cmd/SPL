import { ModuleId, ModuleInfo } from '../types/exam';
import modulesData from '../data/modules.json';

export interface ModuleBarrierStatus {
  moduleId: ModuleId;
  code: string;
  shortName: string;
  totalPoolQuestions: number;
  solvedQuestions: number;
  score: number; // 0 - 100
  status: 'passed' | 'failed' | 'warning' | 'untested';
  requiredCorrectInExam: number; // Needed out of 25 (SPK barajı: 13 / 25)
  missingNetToPass: number; // How many more nets needed to reach 50%
}

export interface SpkOverallDiagnosis {
  overallScore: number;
  overallStatus: 'passed' | 'failed_module' | 'failed_average' | 'insufficient_data';
  passedModulesCount: number;
  totalTestedModules: number;
  weakestModule: ModuleBarrierStatus | null;
  moduleStatuses: Record<ModuleId, ModuleBarrierStatus>;
  diagnosisMessage: string;
  actionAdvice: string;
}

export function calculateSpkDiagnostics(
  moduleStats: Record<ModuleId, { totalQuestions: number; totalCorrect: number; averageAccuracy: number; lastScore: number | null }>
): SpkOverallDiagnosis {
  const modules = modulesData as ModuleInfo[];
  const moduleStatuses: Record<ModuleId, ModuleBarrierStatus> = {} as any;

  let totalScore = 0;
  let testedModulesCount = 0;
  let passedCount = 0;
  let hasFailedModule = false;
  let weakest: ModuleBarrierStatus | null = null;
  let lowestScore = 999;

  for (const mod of modules) {
    const mid = mod.id as ModuleId;
    const stats = moduleStats[mid] || { totalQuestions: 0, totalCorrect: 0, averageAccuracy: 0, lastScore: null };
    const solved = stats.totalQuestions;
    const accuracy = solved >= 5 ? stats.averageAccuracy : (stats.lastScore !== null ? stats.lastScore : 0);

    let status: 'passed' | 'failed' | 'warning' | 'untested' = 'untested';
    let missingNet = 0;

    if (solved >= 5 || stats.lastScore !== null) {
      testedModulesCount++;
      totalScore += accuracy;

      if (accuracy < 50) {
        status = 'failed';
        hasFailedModule = true;
        // 50 points = 12.5 questions, so at least 13 correct answers needed out of 25
        const currentExamCorrectEst = Math.round((accuracy / 100) * 25);
        missingNet = Math.max(1, 13 - currentExamCorrectEst);
      } else if (accuracy < 60) {
        status = 'warning';
        passedCount++;
      } else {
        status = 'passed';
        passedCount++;
      }

      if (accuracy < lowestScore) {
        lowestScore = accuracy;
        weakest = {
          moduleId: mid,
          code: mod.code,
          shortName: mod.short_name,
          totalPoolQuestions: 220,
          solvedQuestions: solved,
          score: accuracy,
          status,
          requiredCorrectInExam: 13,
          missingNetToPass: missingNet,
        };
      }
    }

    moduleStatuses[mid] = {
      moduleId: mid,
      code: mod.code,
      shortName: mod.short_name,
      totalPoolQuestions: 220,
      solvedQuestions: solved,
      score: accuracy,
      status,
      requiredCorrectInExam: 13,
      missingNetToPass: missingNet,
    };
  }

  const averageScore = testedModulesCount > 0 ? Math.round(totalScore / testedModulesCount) : 0;

  if (testedModulesCount < 2) {
    return {
      overallScore: averageScore,
      overallStatus: 'insufficient_data',
      passedModulesCount: passedCount,
      totalTestedModules: testedModulesCount,
      weakestModule: weakest,
      moduleStatuses,
      diagnosisMessage: 'Risk Teşhisi İçin Veri Toplanıyor',
      actionAdvice: 'Modüllerden en az birer test çözerek SPK baraj analizinizi anlık görün.',
    };
  }

  if (hasFailedModule) {
    return {
      overallScore: averageScore,
      overallStatus: 'failed_module',
      passedModulesCount: passedCount,
      totalTestedModules: testedModulesCount,
      weakestModule: weakest,
      moduleStatuses,
      diagnosisMessage: 'DİKKAT: Modül Barajı Altındasınız!',
      actionAdvice: weakest
        ? `${weakest.code} (${weakest.shortName}) modülünde 50 barajını aşmak için +${weakest.missingNetToPass} net doğruya ihtiyacınız var.`
        : 'Baraj altındaki dersinize odaklanın.',
    };
  }

  if (averageScore < 60) {
    const missingAveragePoints = 60 - averageScore;
    const neededNetTotal = Math.ceil((missingAveragePoints * 4) / 4); // roughly needed net
    return {
      overallScore: averageScore,
      overallStatus: 'failed_average',
      passedModulesCount: passedCount,
      totalTestedModules: testedModulesCount,
      weakestModule: weakest,
      moduleStatuses,
      diagnosisMessage: 'Ders Barajları Tamam, Ortalama Barajı (60) Eksik',
      actionAdvice: `Her dersten 50'yi geçtiniz ancak lisans için genel ortalamanızı %${averageScore}'den %60'a (+${neededNetTotal} net) çıkarmanız gerekiyor.`,
    };
  }

  return {
    overallScore: averageScore,
    overallStatus: 'passed',
    passedModulesCount: passedCount,
    totalTestedModules: testedModulesCount,
    weakestModule: weakest,
    moduleStatuses,
    diagnosisMessage: 'TEBRİKLER: SPK Lisans Barajlarını Geçiyorsunuz!',
    actionAdvice: 'Hem her ders için 50 barajını hem de 60 genel not ortalamasını aşıyorsunuz. Tempoyu koruyun!',
  };
}
