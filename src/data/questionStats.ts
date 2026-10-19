/**
 * Soru Havuzu Meta Verileri ve İstatistikleri (Hafif Sayaçlar)
 * 2.1 MB'lık all_questions.json dosyasını Dashboard ve Ana Sayfa ilk açılışında
 * belleğe yüklememek için optimize edilmiş hafif meta veri modülü.
 */

export const TOTAL_QUESTION_COUNT = 1135;

export const MODULE_TOTAL_COUNTS: Record<string, number> = {
  '1001': 283,
  '1003': 290,
  '1005': 288,
  '1012': 274,
};

export const MODULE_NAMES: Record<string, string> = {
  '1001': 'Dar Kapsamlı Sermaye Piyasası Mevzuatı',
  '1003': 'Sermaye Piyasası Araçları 1',
  '1005': 'Yatırım Kuruluşları',
  '1012': 'Takas, Saklama ve Operasyon İşlemleri',
};

/**
 * Soru ID'sinden modül kodunu O(1) anında tespit eder.
 * Örnek: 'q_1001_sert_001' -> '1001'
 */
export function getModuleIdFromQuestionId(questionId: string): string {
  if (!questionId) return '';
  const match = questionId.match(/q_(\d{4})_/);
  return match ? match[1] : '';
}
