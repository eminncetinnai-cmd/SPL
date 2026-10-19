import { jsPDF } from 'jspdf';

export interface DurationItem {
  id: string;
  moduleId: string;
  moduleName: string;
  duration: string;
  title: string;
  description: string;
  trap: string;
}

export interface RatioItem {
  id: string;
  moduleId: string;
  moduleName: string;
  value: string;
  title: string;
  description: string;
  trap: string;
}

export interface ComparisonItem {
  id: string;
  moduleId: string;
  moduleName: string;
  conceptA: { title: string; desc: string; keyPoint: string };
  conceptB: { title: string; desc: string; keyPoint: string };
  differenceRule: string;
}

export interface TrapItem {
  id: string;
  moduleId: string;
  moduleName: string;
  myth: string;
  reality: string;
  whyImportant: string;
}

export interface PdfExportOptions {
  durations: DurationItem[];
  ratios: RatioItem[];
  comparisons: ComparisonItem[];
  traps: TrapItem[];
  title?: string;
  filterTitle?: string;
}

const packagedPdfNames: Record<string, string> = {
  all: 'hap-bilgiler.pdf',
  '1001': 'hap-1001.pdf',
  '1003': 'hap-1003.pdf',
  '1005': 'hap-1005.pdf',
  '1012': 'hap-1012.pdf',
};

function packagedPdfUrl(scope: keyof typeof packagedPdfNames): string {
  return new URL(`kaynaklar/${packagedPdfNames[scope]}`, document.baseURI).toString();
}

export function downloadPackagedCheatSheetPdf(scope: keyof typeof packagedPdfNames): void {
  const link = document.createElement('a');
  link.href = packagedPdfUrl(scope);
  link.download = packagedPdfNames[scope];
  link.rel = 'noopener';
  document.body.appendChild(link);
  link.click();
  link.remove();
}

export function openPackagedCheatSheetPdf(scope: keyof typeof packagedPdfNames): void {
  const opened = window.open(packagedPdfUrl(scope), '_blank', 'noopener,noreferrer');
  if (!opened) {
    throw new Error('PDF önizlemesi açılamadı. Tarayıcı açılır pencere iznini kontrol edin.');
  }
}

/**
 * Downloads a direct PDF file without window.print or iframes
 */
export async function downloadCheatSheetPdf(options: PdfExportOptions): Promise<void> {
  const totalCount = options.durations.length + options.ratios.length + options.comparisons.length + options.traps.length;
  if (totalCount === 0) {
    throw new Error('PDF oluşturmak için aktarılacak hap bilgi bulunamadı.');
  }

  const fileName = `SPK_SPL_1_Altin_Hap_Bilgiler_${totalCount}_Madde_${Date.now()}.pdf`;
  const pdf = new jsPDF({ unit: 'mm', format: 'a4', orientation: 'portrait' });
  pdf.setTextColor(15, 23, 42);
  pdf.setDrawColor(15, 118, 110);
  pdf.setLineWidth(0.5);
  pdf.line(12, 8, 198, 8);
  const pageWidth = pdf.internal.pageSize.getWidth();
  const pageHeight = pdf.internal.pageSize.getHeight();
  const margin = 12;
  const lineHeight = 4.6;
  let y = margin;

  const addText = (text: string, size = 8, bold = false) => {
    pdf.setFont('helvetica', bold ? 'bold' : 'normal');
    pdf.setFontSize(size);
    const lines = pdf.splitTextToSize(text, pageWidth - margin * 2);
    lines.forEach((line: string) => {
      if (y + lineHeight > pageHeight - margin) {
        pdf.addPage();
        y = margin;
      }
      pdf.text(String(line), margin, y);
      y += lineHeight;
    });
    y += 1.5;
  };

  addText(options.title || 'SPK SERMAYE PIYASASI LİSANSLAMA DUZEY 1', 13, true);
  addText(options.filterTitle || 'Tum Konular ve 4 Temel Modul', 9);
  addText(`Toplam ${totalCount} madde`, 9, true);

  const addSection = <T extends { moduleName: string }>(
    title: string,
    items: T[],
    format: (item: T, index: number) => string
  ) => {
    if (items.length === 0) return;
    addText(title, 10, true);
    items.forEach((item, index) => addText(`${index + 1}. [${item.moduleName}] ${format(item, index)}`));
  };

  addSection('1. KANUNI SURELER, GUNLER VE VALORLER', options.durations, (item) =>
    `${item.duration} - ${item.title}. ${item.description} Tuzak: ${item.trap}`
  );
  addSection('2. KRITIK ESİK DEGERLERI, RAKAMLAR VE ORANLAR', options.ratios, (item) =>
    `${item.value} - ${item.title}. ${item.description} Tuzak: ${item.trap}`
  );
  addSection('3. KARISTIRILAN IKILI KAVRAMLAR', options.comparisons, (item) =>
    `${item.conceptA.title}: ${item.conceptA.desc} ${item.conceptB.title}: ${item.conceptB.desc} Fark: ${item.differenceRule}`
  );
  addSection('4. OLUMCUL SINAV TUZAKLARI', options.traps, (item) =>
    `Mit: ${item.myth} Gercek: ${item.reality} Onemi: ${item.whyImportant}`
  );

  const pdfBytes = pdf.output('arraybuffer');
  if (pdf.getNumberOfPages() === 0 || pdfBytes.byteLength === 0) {
    throw new Error('PDF oluşturuldu ancak geçerli içerik üretilemedi.');
  }
  pdf.save(fileName);
}

/**
 * Alias for backward compatibility
 */
export function generateCheatSheetPdf(options: PdfExportOptions): void {
  downloadCheatSheetPdf(options);
}

/**
 * Opens full standalone view in a clean new tab where user can read or print safely
 */
export function openCheatSheetInNewTab(options: PdfExportOptions): void {
  const html = generateFullStandaloneHtml(options);
  const previewWindow = window.open('', '_blank');
  if (!previewWindow) {
    throw new Error('Önizleme penceresi açılamadı. Tarayıcı açılır pencere iznini kontrol edin.');
  }

  previewWindow.document.open();
  previewWindow.document.write(html);
  previewWindow.document.close();
  previewWindow.focus();
}

/**
 * Downloads standalone offline HTML report
 */
export function downloadCheatSheetHtml(options: PdfExportOptions): void {
  const html = generateFullStandaloneHtml(options);
  const blob = new Blob([html], { type: 'text/html;charset=utf-8' });
  const url = URL.createObjectURL(blob);
  const totalCount = options.durations.length + options.ratios.length + options.comparisons.length + options.traps.length;
  const a = document.createElement('a');
  a.href = url;
  a.download = `SPK_SPL_1_Altin_Hap_Bilgiler_${totalCount}_Madde.html`;
  document.body.appendChild(a);
  a.click();
  document.body.removeChild(a);
  setTimeout(() => URL.revokeObjectURL(url), 10000);
}

function escapeHtml(str: string): string {
  if (!str) return '';
  return str
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;')
    .replace(/'/g, '&#039;');
}

function generateCheatSheetInnerHtml(options: PdfExportOptions, forPdfExport = false): string {
  const {
    durations,
    ratios,
    comparisons,
    traps,
    title = 'SPK SERMAYE PİYASASI LİSANSLAMA DÜZEY 1',
    filterTitle = 'Tüm Konular ve 4 Temel Modül (1001, 1003, 1005, 1012)',
  } = options;

  const totalCount = durations.length + ratios.length + comparisons.length + traps.length;
  const printDate = new Date().toLocaleDateString('tr-TR', {
    day: 'numeric',
    month: 'long',
    year: 'numeric',
  });

  return `
  <!-- Header Box -->
  <div style="border: 2px solid #0f766e; border-radius: 8px; padding: 12px 16px; background: #f0fdfa; margin-bottom: 14px;">
    <div style="display: flex; justify-content: space-between; align-items: center; border-bottom: 1.5px solid #ccfbf1; padding-bottom: 6px; margin-bottom: 6px;">
      <span style="font-size: 8pt; font-weight: 800; letter-spacing: 1px; color: #0f766e; text-transform: uppercase;">
        T.C. SPK SERMAYE PİYASASI LİSANSLAMA SINAVLARI • PRO REHBER
      </span>
      <span style="font-size: 8pt; font-family: monospace; color: #475569; font-weight: 600;">
        Hazırlayan: Emin ÇETİN • ${printDate}
      </span>
    </div>
    <h1 style="font-size: 13pt; font-weight: 900; color: #042f2e; margin-bottom: 3px; letter-spacing: -0.3px;">
      ${escapeHtml(title)}
    </h1>
    <p style="font-size: 8.5pt; color: #334155; margin-bottom: 8px; font-weight: 500; line-height: 1.35;">
      <strong>Temmuz 2026 SPL Resmi Ders Çalışma Notları</strong> ve güncel mevzuat tebliğleri doğrultusunda sınav öncesi altın hap bilgiler.
      Kapsam: <em>${escapeHtml(filterTitle)}</em>.
    </p>
    <div style="display: flex; flex-wrap: wrap; gap: 6px;">
      <span style="font-size: 7.5pt; font-weight: 700; padding: 3px 8px; border-radius: 4px; background: #fef3c7; color: #92400e; border: 1px solid #fde68a;">
        ⏱️ ${durations.length} Kanuni Süre
      </span>
      <span style="font-size: 7.5pt; font-weight: 700; padding: 3px 8px; border-radius: 4px; background: #d1fae5; color: #065f46; border: 1px solid #a7f3d0;">
        📊 ${ratios.length} Kritik Eşik & Oran
      </span>
      <span style="font-size: 7.5pt; font-weight: 700; padding: 3px 8px; border-radius: 4px; background: #ede9fe; color: #5b21b6; border: 1px solid #ddd6fe;">
        ⚖️ ${comparisons.length} İkili Kavram
      </span>
      <span style="font-size: 7.5pt; font-weight: 700; padding: 3px 8px; border-radius: 4px; background: #ffe4e6; color: #9f1239; border: 1px solid #fecdd3;">
        🚨 ${traps.length} Ölümcül Tuzak
      </span>
      <span style="font-size: 7.5pt; font-weight: 700; padding: 3px 8px; border-radius: 4px; background: #f1f5f9; color: #334155; border: 1px solid #cbd5e1;">
        Toplam ${totalCount} Madde
      </span>
    </div>
  </div>

  ${
    durations.length > 0
      ? `
  <!-- Section 1 -->
  <div style="background: #b45309; color: #ffffff; padding: 5px 10px; font-weight: 800; font-size: 8.5pt; border-radius: 4px; margin-bottom: 6px; page-break-after: avoid;">
    ⏱️ 1. KANUNİ SÜRELER, GÜNLER VE VALÖRLER (${durations.length} Madde)
  </div>
  <table style="width: 100%; border-collapse: collapse; margin-bottom: 12px; font-size: 8pt;">
    <thead>
      <tr style="background: #f8fafc; color: #1e293b;">
        <th style="border: 1px solid #cbd5e1; padding: 5px; width: 28px; text-align: center;">#</th>
        <th style="border: 1px solid #cbd5e1; padding: 5px; width: 45px; text-align: center;">Ders</th>
        <th style="border: 1px solid #cbd5e1; padding: 5px; width: 75px; text-align: center;">Süre / Valör</th>
        <th style="border: 1px solid #cbd5e1; padding: 5px; width: 140px;">Konu & Düzenleme</th>
        <th style="border: 1px solid #cbd5e1; padding: 5px;">Açıklama & Sınavda Çıkış Şekli</th>
        <th style="border: 1px solid #cbd5e1; padding: 5px; width: 180px;">Ölümcül Sınav Tuzağı</th>
      </tr>
    </thead>
    <tbody>
      ${durations
        .map(
          (item, idx) => `
        <tr style="background: ${idx % 2 === 0 ? '#ffffff' : '#fcfdfe'}; page-break-inside: avoid;">
          <td style="border: 1px solid #e2e8f0; padding: 5px; text-align: center; font-weight: bold; color: #64748b;">${idx + 1}</td>
          <td style="border: 1px solid #e2e8f0; padding: 5px; text-align: center;">
            <span style="display: inline-block; padding: 2px 5px; border-radius: 4px; font-family: monospace; font-weight: 700; font-size: 7.5pt; background: #e2e8f0; color: #334155;">
              ${item.moduleId}
            </span>
          </td>
          <td style="border: 1px solid #e2e8f0; padding: 5px; text-align: center;">
            <span style="display: inline-block; padding: 2px 6px; border-radius: 4px; font-weight: 800; font-size: 8pt; background: #fef3c7; color: #92400e; border: 1px solid #fde68a;">
              ${escapeHtml(item.duration)}
            </span>
          </td>
          <td style="border: 1px solid #e2e8f0; padding: 5px; font-weight: 700; color: #0f172a;">
            ${escapeHtml(item.title)}
          </td>
          <td style="border: 1px solid #e2e8f0; padding: 5px; color: #334155; line-height: 1.3;">
            ${escapeHtml(item.description)}
          </td>
          <td style="border: 1px solid #e2e8f0; padding: 5px;">
            <div style="background: #fffbeb; border-left: 3px solid #f59e0b; padding: 4px 6px; border-radius: 3px; font-size: 7.5pt; color: #78350f; line-height: 1.25;">
              ⚠️ ${escapeHtml(item.trap)}
            </div>
          </td>
        </tr>
      `
        )
        .join('')}
    </tbody>
  </table>
  `
      : ''
  }

  ${
    ratios.length > 0
      ? `
  <!-- Section 2 -->
  <div style="background: #047857; color: #ffffff; padding: 5px 10px; font-weight: 800; font-size: 8.5pt; border-radius: 4px; margin-bottom: 6px; page-break-after: avoid;">
    📊 2. KRİTİK EŞİK DEĞERLERİ, RAKAMLAR VE ORANLAR (${ratios.length} Madde)
  </div>
  <table style="width: 100%; border-collapse: collapse; margin-bottom: 12px; font-size: 8pt;">
    <thead>
      <tr style="background: #f8fafc; color: #1e293b;">
        <th style="border: 1px solid #cbd5e1; padding: 5px; width: 28px; text-align: center;">#</th>
        <th style="border: 1px solid #cbd5e1; padding: 5px; width: 45px; text-align: center;">Ders</th>
        <th style="border: 1px solid #cbd5e1; padding: 5px; width: 75px; text-align: center;">Eşik / Oran</th>
        <th style="border: 1px solid #cbd5e1; padding: 5px; width: 140px;">Konu & Düzenleme</th>
        <th style="border: 1px solid #cbd5e1; padding: 5px;">Kanuni Esas & Detay</th>
        <th style="border: 1px solid #cbd5e1; padding: 5px; width: 180px;">Ölümcül Sınav Tuzağı</th>
      </tr>
    </thead>
    <tbody>
      ${ratios
        .map(
          (item, idx) => `
        <tr style="background: ${idx % 2 === 0 ? '#ffffff' : '#fcfdfe'}; page-break-inside: avoid;">
          <td style="border: 1px solid #e2e8f0; padding: 5px; text-align: center; font-weight: bold; color: #64748b;">${idx + 1}</td>
          <td style="border: 1px solid #e2e8f0; padding: 5px; text-align: center;">
            <span style="display: inline-block; padding: 2px 5px; border-radius: 4px; font-family: monospace; font-weight: 700; font-size: 7.5pt; background: #e2e8f0; color: #334155;">
              ${item.moduleId}
            </span>
          </td>
          <td style="border: 1px solid #e2e8f0; padding: 5px; text-align: center;">
            <span style="display: inline-block; padding: 2px 6px; border-radius: 4px; font-weight: 800; font-size: 8pt; background: #d1fae5; color: #065f46; border: 1px solid #a7f3d0;">
              ${escapeHtml(item.value)}
            </span>
          </td>
          <td style="border: 1px solid #e2e8f0; padding: 5px; font-weight: 700; color: #0f172a;">
            ${escapeHtml(item.title)}
          </td>
          <td style="border: 1px solid #e2e8f0; padding: 5px; color: #334155; line-height: 1.3;">
            ${escapeHtml(item.description)}
          </td>
          <td style="border: 1px solid #e2e8f0; padding: 5px;">
            <div style="background: #fffbeb; border-left: 3px solid #f59e0b; padding: 4px 6px; border-radius: 3px; font-size: 7.5pt; color: #78350f; line-height: 1.25;">
              ⚠️ ${escapeHtml(item.trap)}
            </div>
          </td>
        </tr>
      `
        )
        .join('')}
    </tbody>
  </table>
  `
      : ''
  }

  ${
    comparisons.length > 0
      ? `
  <!-- Section 3 -->
  <div style="background: #6d28d9; color: #ffffff; padding: 5px 10px; font-weight: 800; font-size: 8.5pt; border-radius: 4px; margin-bottom: 6px; page-break-after: avoid;">
    ⚖️ 3. KARIŞTIRILAN İKİLİ TANIM VE KAVRAM KARŞILAŞTIRMALARI (${comparisons.length} Madde)
  </div>
  <table style="width: 100%; border-collapse: collapse; margin-bottom: 12px; font-size: 8pt;">
    <thead>
      <tr style="background: #f8fafc; color: #1e293b;">
        <th style="border: 1px solid #cbd5e1; padding: 5px; width: 28px; text-align: center;">#</th>
        <th style="border: 1px solid #cbd5e1; padding: 5px; width: 45px; text-align: center;">Ders</th>
        <th style="border: 1px solid #cbd5e1; padding: 5px; width: 200px;">Kavram A</th>
        <th style="border: 1px solid #cbd5e1; padding: 5px; width: 200px;">Kavram B</th>
        <th style="border: 1px solid #cbd5e1; padding: 5px;">Sınavdaki Altın Ayrım Kuralı</th>
      </tr>
    </thead>
    <tbody>
      ${comparisons
        .map(
          (item, idx) => `
        <tr style="background: ${idx % 2 === 0 ? '#ffffff' : '#fcfdfe'}; page-break-inside: avoid;">
          <td style="border: 1px solid #e2e8f0; padding: 5px; text-align: center; font-weight: bold; color: #64748b;">${idx + 1}</td>
          <td style="border: 1px solid #e2e8f0; padding: 5px; text-align: center;">
            <span style="display: inline-block; padding: 2px 5px; border-radius: 4px; font-family: monospace; font-weight: 700; font-size: 7.5pt; background: #e2e8f0; color: #334155;">
              ${item.moduleId}
            </span>
          </td>
          <td style="border: 1px solid #e2e8f0; padding: 5px;">
            <div style="background: #faf5ff; border: 1px solid #f3e8ff; padding: 4px 6px; border-radius: 4px; font-size: 7.5pt;">
              <strong style="color: #6d28d9; display: block; margin-bottom: 2px;">${escapeHtml(item.conceptA.title)}</strong>
              <div style="color: #334155; margin-bottom: 2px;">${escapeHtml(item.conceptA.desc)}</div>
              <div style="font-weight: 700; color: #5b21b6;">💡 ${escapeHtml(item.conceptA.keyPoint)}</div>
            </div>
          </td>
          <td style="border: 1px solid #e2e8f0; padding: 5px;">
            <div style="background: #faf5ff; border: 1px solid #f3e8ff; padding: 4px 6px; border-radius: 4px; font-size: 7.5pt;">
              <strong style="color: #6d28d9; display: block; margin-bottom: 2px;">${escapeHtml(item.conceptB.title)}</strong>
              <div style="color: #334155; margin-bottom: 2px;">${escapeHtml(item.conceptB.desc)}</div>
              <div style="font-weight: 700; color: #5b21b6;">💡 ${escapeHtml(item.conceptB.keyPoint)}</div>
            </div>
          </td>
          <td style="border: 1px solid #e2e8f0; padding: 5px;">
            <div style="background: #ede9fe; border-left: 3px solid #7c3aed; padding: 4px 6px; border-radius: 3px; font-size: 7.5pt; color: #4c1d95; line-height: 1.3;">
              ⚡ <strong>ALTIN KURAL:</strong> ${escapeHtml(item.differenceRule)}
            </div>
          </td>
        </tr>
      `
        )
        .join('')}
    </tbody>
  </table>
  `
      : ''
  }

  ${
    traps.length > 0
      ? `
  <!-- Section 4 -->
  <div style="background: #be123c; color: #ffffff; padding: 5px 10px; font-weight: 800; font-size: 8.5pt; border-radius: 4px; margin-bottom: 6px; page-break-after: avoid;">
    🚨 4. ÖLÜMCÜL SINAV TUZAKLARI VE YANILGILAR (${traps.length} Madde)
  </div>
  <table style="width: 100%; border-collapse: collapse; margin-bottom: 12px; font-size: 8pt;">
    <thead>
      <tr style="background: #f8fafc; color: #1e293b;">
        <th style="border: 1px solid #cbd5e1; padding: 5px; width: 28px; text-align: center;">#</th>
        <th style="border: 1px solid #cbd5e1; padding: 5px; width: 45px; text-align: center;">Ders</th>
        <th style="border: 1px solid #cbd5e1; padding: 5px; width: 220px;">Yaygın Sınav Yanılgısı (YANLIŞ)</th>
        <th style="border: 1px solid #cbd5e1; padding: 5px;">Mevzuat ve Kanuni Gerçek (DOĞRU)</th>
        <th style="border: 1px solid #cbd5e1; padding: 5px; width: 170px;">Soru Geliş Nedeni</th>
      </tr>
    </thead>
    <tbody>
      ${traps
        .map(
          (item, idx) => `
        <tr style="background: ${idx % 2 === 0 ? '#ffffff' : '#fcfdfe'}; page-break-inside: avoid;">
          <td style="border: 1px solid #e2e8f0; padding: 5px; text-align: center; font-weight: bold; color: #64748b;">${idx + 1}</td>
          <td style="border: 1px solid #e2e8f0; padding: 5px; text-align: center;">
            <span style="display: inline-block; padding: 2px 5px; border-radius: 4px; font-family: monospace; font-weight: 700; font-size: 7.5pt; background: #e2e8f0; color: #334155;">
              ${item.moduleId}
            </span>
          </td>
          <td style="border: 1px solid #e2e8f0; padding: 5px;">
            <div style="background: #fff1f2; border-left: 3px solid #f43f5e; padding: 4px 6px; border-radius: 3px; color: #881337; font-size: 7.5pt; line-height: 1.25;">
              "${escapeHtml(item.myth)}"
            </div>
          </td>
          <td style="border: 1px solid #e2e8f0; padding: 5px;">
            <div style="background: #f0fdf4; border-left: 3px solid #10b981; padding: 4px 6px; border-radius: 3px; color: #064e3b; font-size: 7.5pt; line-height: 1.25;">
              ✅ ${escapeHtml(item.reality)}
            </div>
          </td>
          <td style="border: 1px solid #e2e8f0; padding: 5px;">
            <div style="font-style: italic; color: #475569; font-size: 7.5pt; line-height: 1.25;">
              💡 ${escapeHtml(item.whyImportant)}
            </div>
          </td>
        </tr>
      `
        )
        .join('')}
    </tbody>
  </table>
  `
      : ''
  }

  <!-- Footer -->
  <div style="margin-top: 16px; padding-top: 8px; border-top: 1px solid #cbd5e1; display: flex; justify-content: space-between; font-size: 7.5pt; color: #64748b; font-family: monospace;">
    <span>© 2026 Emin ÇETİN • Tüm Hakları Saklıdır</span>
    <span>İçerik Kürasyonu & Yazılım Mimarisi: <strong>Emin ÇETİN</strong></span>
    <span>SPK SPL Düzey 1 Lisanslama Hazırlık Platformu (Temmuz 2026 Standartları)</span>
  </div>
  `;
}

function generateFullStandaloneHtml(options: PdfExportOptions): string {
  const content = generateCheatSheetInnerHtml(options, false);

  return `<!DOCTYPE html>
<html lang="tr">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>SPK SPL Düzey 1 - Sınav Öncesi Kritik Hap Bilgiler | Emin ÇETİN</title>
  <style>
    @page {
      size: A4 portrait;
      margin: 10mm 8mm 12mm 8mm;
    }
    @media print {
      body {
        -webkit-print-color-adjust: exact !important;
        print-color-adjust: exact !important;
      }
      .no-print {
        display: none !important;
      }
      tr {
        page-break-inside: avoid !important;
        break-inside: avoid !important;
      }
    }
    * {
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }
    body {
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
      font-size: 8.5pt;
      line-height: 1.35;
      color: #0f172a;
      background: #f8fafc;
      padding: 16px;
    }
    .wrapper {
      max-width: 900px;
      margin: 0 auto;
      background: #ffffff;
      padding: 24px;
      border-radius: 12px;
      box-shadow: 0 4px 6px -1px rgb(0 0 0 / 0.1);
    }
    .top-bar {
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 16px;
      padding: 12px 16px;
      background: #0f766e;
      color: #ffffff;
      border-radius: 8px;
    }
    .btn {
      padding: 8px 16px;
      border-radius: 6px;
      font-weight: 700;
      font-size: 9pt;
      cursor: pointer;
      border: none;
      transition: all 0.2s;
    }
    .btn-print {
      background: #ffffff;
      color: #0f766e;
    }
    .btn-print:hover {
      background: #ccfbf1;
    }
    .btn-close {
      background: rgba(255, 255, 255, 0.15);
      color: #ffffff;
    }
    .btn-close:hover {
      background: rgba(255, 255, 255, 0.25);
    }
  </style>
</head>
<body>
  <div class="wrapper">
    <div class="top-bar no-print">
      <div style="font-weight: 800; font-size: 10pt;">
        📋 SPK SPL 1 Altın Hap Bilgiler Raporu
      </div>
      <div style="display: flex; gap: 8px;">
        <button type="button" class="btn btn-print" onclick="window.focus(); window.print();">🖨️ Yazdır / PDF Kaydet</button>
      </div>
    </div>

    ${content}
  </div>
</body>
</html>`;
}
