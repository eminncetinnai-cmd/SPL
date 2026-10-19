import { PastQuizSummary, MistakeEntry } from '../types/exam';

export function exportQuizHistoryToCSV(history: PastQuizSummary[]): void {
  if (!history || history.length === 0) {
    alert('Dışa aktarılacak sınav geçmişi bulunamadı.');
    return;
  }

  const headers = [
    'Sınav ID',
    'Tarih',
    'Modül / Tür',
    'Soru Sayısı',
    'Doğru',
    'Yanlış',
    'Boş',
    'Puan (100 Üzerinden)',
    'Başarı Oranı (%)',
    'Süre (Saniye)',
    'SPK Durum'
  ];

  const rows = history.map((item) => [
    `"${item.id}"`,
    `"${item.date}"`,
    `"${item.title.replace(/"/g, '""')}"`,
    item.total_questions,
    item.correct_count,
    item.wrong_count,
    item.empty_count,
    item.score,
    item.accuracy_pct,
    item.duration_seconds,
    item.overall_passed ? 'GEÇTİ' : 'KALDI'
  ]);

  const csvContent = '\uFEFF' + [headers.join(';'), ...rows.map(r => r.join(';'))].join('\r\n');
  const blob = new Blob([csvContent], { type: 'text/csv;charset=utf-8;' });
  const url = URL.createObjectURL(blob);
  const link = document.createElement('a');
  const timestamp = new Date().toISOString().slice(0, 10);
  link.setAttribute('href', url);
  link.setAttribute('download', `SPK_SPL_Sinav_Gecmisi_${timestamp}.csv`);
  document.body.appendChild(link);
  link.click();
  document.body.removeChild(link);
}

import allQuestionsData from '../data/all_questions.json';
import { Question } from '../types/exam';

const canonicalMap = new Map<string, Question>(
  (allQuestionsData as Question[]).map((q) => [q.id, q])
);

export function exportMistakesToCSV(mistakes: MistakeEntry[]): void {
  if (!mistakes || mistakes.length === 0) {
    alert('Dışa aktarılacak hatalı soru bulunamadı.');
    return;
  }

  const headers = [
    'Soru ID',
    'Modül',
    'Konu',
    'Soru Metni',
    'Doğru Cevap',
    'Açıklama & Sınav İpucu',
    'Sınav Tuzağı',
    'Hata Sayısı',
    'Son Hata Tarihi'
  ];

  const rows = mistakes.map((item) => {
    const q = canonicalMap.get(item.question.id) || item.question;
    return [
      `"${q.id}"`,
      `"${q.module_id}"`,
      `"${(q.topic || '').replace(/"/g, '""')}"`,
      `"${q.text.replace(/"/g, '""')}"`,
      `"${q.correct_answer}"`,
      `"${(q.explanation || '').replace(/"/g, '""')}"`,
      `"${(q.trap || '').replace(/"/g, '""')}"`,
      item.wrong_count,
      `"${item.last_wrong_date}"`
    ];
  });

  const csvContent = '\uFEFF' + [headers.join(';'), ...rows.map(r => r.join(';'))].join('\r\n');
  const blob = new Blob([csvContent], { type: 'text/csv;charset=utf-8;' });
  const url = URL.createObjectURL(blob);
  const link = document.createElement('a');
  const timestamp = new Date().toISOString().slice(0, 10);
  link.setAttribute('href', url);
  link.setAttribute('download', `SPK_SPL_Hatali_Sorular_${timestamp}.csv`);
  document.body.appendChild(link);
  link.click();
  document.body.removeChild(link);
}
