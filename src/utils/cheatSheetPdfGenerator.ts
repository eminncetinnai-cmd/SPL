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

export function generateCheatSheetPdf(options: PdfExportOptions): void {
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

  const html = `<!DOCTYPE html>
<html lang="tr">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
  <title>SPK SPL Düzey 1 - Sınav Öncesi Kritik Hap Bilgiler Rehberi</title>
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
      .section-heading {
        page-break-after: avoid !important;
        break-after: avoid !important;
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
      background: #ffffff;
      padding: 10px;
    }
    .header-box {
      border: 2px solid #0f766e;
      border-radius: 8px;
      padding: 12px 16px;
      background: #f0fdfa;
      margin-bottom: 14px;
    }
    .header-top {
      display: flex;
      justify-content: space-between;
      align-items: center;
      border-bottom: 1.5px solid #ccfbf1;
      padding-bottom: 6px;
      margin-bottom: 6px;
    }
    .header-title-small {
      font-size: 8pt;
      font-weight: 800;
      letter-spacing: 1px;
      color: #0f766e;
      text-transform: uppercase;
    }
    .header-date {
      font-size: 8pt;
      font-family: monospace;
      color: #475569;
      font-weight: 600;
    }
    .header-main-title {
      font-size: 14pt;
      font-weight: 900;
      color: #042f2e;
      margin-bottom: 3px;
      letter-spacing: -0.3px;
    }
    .header-subtitle {
      font-size: 9pt;
      color: #334155;
      margin-bottom: 8px;
      font-weight: 500;
    }
    .stats-pills {
      display: flex;
      flex-wrap: wrap;
      gap: 6px;
    }
    .stat-pill {
      font-size: 7.5pt;
      font-weight: 700;
      padding: 2px 8px;
      border-radius: 4px;
      background: #ffffff;
      border: 1px solid #99f6e4;
      color: #0f766e;
    }
    .stat-pill.amber {
      border-color: #fde68a;
      background: #fef3c7;
      color: #92400e;
    }
    .stat-pill.emerald {
      border-color: #a7f3d0;
      background: #d1fae5;
      color: #065f46;
    }
    .stat-pill.purple {
      border-color: #ddd6fe;
      background: #ede9fe;
      color: #5b21b6;
    }
    .stat-pill.rose {
      border-color: #fecdd3;
      background: #ffe4e6;
      color: #9f1239;
    }

    .section-heading {
      font-size: 11pt;
      font-weight: 900;
      padding: 6px 10px;
      border-radius: 6px;
      margin-top: 14px;
      margin-bottom: 6px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      color: #ffffff;
    }
    .bg-durations { background: #b45309; }
    .bg-ratios { background: #047857; }
    .bg-comparisons { background: #6d28d9; }
    .bg-traps { background: #be123c; }

    table.data-table {
      width: 100%;
      border-collapse: collapse;
      margin-bottom: 12px;
      font-size: 8pt;
    }
    table.data-table th {
      background: #f1f5f9;
      color: #1e293b;
      font-weight: 800;
      text-align: left;
      padding: 5px 6px;
      border: 1px solid #cbd5e1;
      font-size: 7.5pt;
      text-transform: uppercase;
      letter-spacing: 0.5px;
    }
    table.data-table td {
      padding: 5px 6px;
      border: 1px solid #e2e8f0;
      vertical-align: top;
      color: #0f172a;
    }
    table.data-table tr:nth-child(even) {
      background-color: #f8fafc;
    }

    .badge-cell {
      font-weight: 800;
      font-family: monospace;
      font-size: 8pt;
      border-radius: 4px;
      padding: 2px 5px;
      display: inline-block;
      white-space: nowrap;
    }
    .badge-amber {
      background: #fef3c7;
      color: #78350f;
      border: 1px solid #fde68a;
    }
    .badge-emerald {
      background: #d1fae5;
      color: #064e3b;
      border: 1px solid #a7f3d0;
    }
    .badge-purple {
      background: #ede9fe;
      color: #4c1d95;
      border: 1px solid #ddd6fe;
    }
    .badge-rose {
      background: #ffe4e6;
      color: #881337;
      border: 1px solid #fecdd3;
    }

    .module-code {
      font-family: monospace;
      font-weight: 800;
      font-size: 7.5pt;
      color: #475569;
      background: #e2e8f0;
      padding: 1px 4px;
      border-radius: 3px;
      display: inline-block;
    }

    .item-title {
      font-weight: 800;
      color: #0f172a;
      display: block;
      margin-bottom: 2px;
    }
    .item-desc {
      color: #334155;
      line-height: 1.3;
    }
    .trap-box {
      background: #fffbeb;
      border: 1px solid #fef3c7;
      border-left: 3px solid #f59e0b;
      padding: 3px 5px;
      border-radius: 3px;
      font-size: 7.5pt;
      color: #78350f;
      line-height: 1.25;
    }
    .trap-myth {
      background: #fff1f2;
      border: 1px solid #ffe4e6;
      border-left: 3px solid #f43f5e;
      padding: 4px 6px;
      border-radius: 3px;
      color: #881337;
      font-size: 7.5pt;
      line-height: 1.25;
      margin-bottom: 3px;
    }
    .trap-reality {
      background: #f0fdf4;
      border: 1px solid #dcfce7;
      border-left: 3px solid #10b981;
      padding: 4px 6px;
      border-radius: 3px;
      color: #064e3b;
      font-size: 7.5pt;
      line-height: 1.25;
    }

    .comparison-box {
      background: #faf5ff;
      border: 1px solid #f3e8ff;
      padding: 4px 6px;
      border-radius: 4px;
      margin-bottom: 3px;
      font-size: 7.5pt;
    }
    .comparison-rule {
      background: #ede9fe;
      border-left: 3px solid #7c3aed;
      padding: 4px 6px;
      border-radius: 3px;
      color: #4c1d95;
      font-size: 7.5pt;
      font-weight: 600;
    }

    .footer {
      border-top: 1px solid #cbd5e1;
      padding-top: 6px;
      margin-top: 16px;
      display: flex;
      justify-content: space-between;
      font-size: 7pt;
      color: #64748b;
      font-family: monospace;
    }

    .print-button-bar {
      margin-bottom: 12px;
      text-align: right;
    }
    .btn-print {
      background: #0f766e;
      color: #ffffff;
      border: none;
      padding: 8px 16px;
      border-radius: 6px;
      font-weight: 800;
      font-size: 9pt;
      cursor: pointer;
    }
  </style>
</head>
<body>
  <div class="print-button-bar no-print">
    <button class="btn-print" onclick="window.print()">🖨️ PDF Olarak Kaydet / Yazdır</button>
  </div>

  <!-- Header -->
  <div class="header-box">
    <div class="header-top">
      <span class="header-title-small">T.C. SPK SERMAYE PİYASASI LİSANSLAMA SINAVLARI • PRO REHBER</span>
      <span class="header-date">Hazırlayan: Emin ÇETİN • ${printDate}</span>
    </div>
    <h1 class="header-main-title">${title}</h1>
    <p class="header-subtitle">
      <strong>Temmuz 2026 SPL Resmi Ders Çalışma Notları</strong> ve güncel mevzuat tebliğleri doğrultusunda sınav öncesi hızlı tekrar rehberi.
      Kapsam: <em>${filterTitle}</em>.
    </p>
    <div class="stats-pills">
      <span class="stat-pill amber">⏱️ ${durations.length} Kanuni Süre</span>
      <span class="stat-pill emerald">📊 ${ratios.length} Kritik Eşik & Oran</span>
      <span class="stat-pill purple">⚖️ ${comparisons.length} İkili Kavram</span>
      <span class="stat-pill rose">🚨 ${traps.length} Ölümcül Tuzak</span>
      <span class="stat-pill">Toplam ${totalCount} Hap Bilgi</span>
    </div>
  </div>

  ${
    durations.length > 0
      ? `
  <!-- SECTION 1: DURATIONS -->
  <div class="section-heading bg-durations">
    <span>⏱️ 1. KANUNİ SÜRELER, GÜNLER VE VALÖRLER</span>
    <span style="font-size: 8pt; font-weight: normal;">(${durations.length} Madde)</span>
  </div>
  <table class="data-table">
    <thead>
      <tr>
        <th style="width: 24px;">#</th>
        <th style="width: 44px;">Ders</th>
        <th style="width: 105px;">Süre / Valör</th>
        <th>Konu ve Kanuni Kural</th>
        <th style="width: 220px;">⚠️ Sınav Tuzağı & Çeldirici</th>
      </tr>
    </thead>
    <tbody>
      ${durations
        .map(
          (item, idx) => `
        <tr>
          <td style="text-align: center; font-weight: bold; color: #64748b;">${idx + 1}</td>
          <td style="text-align: center;"><span class="module-code">${item.moduleId}</span></td>
          <td><span class="badge-cell badge-amber">${escapeHtml(item.duration)}</span></td>
          <td>
            <span class="item-title">${escapeHtml(item.title)}</span>
            <div class="item-desc">${escapeHtml(item.description)}</div>
          </td>
          <td>
            <div class="trap-box">
              <strong>Tuzak:</strong> ${escapeHtml(item.trap)}
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
  <!-- SECTION 2: RATIOS -->
  <div class="section-heading bg-ratios">
    <span>📊 2. KRİTİK EŞİKLER, ORANLAR VE PARASAL LİMİTLER</span>
    <span style="font-size: 8pt; font-weight: normal;">(${ratios.length} Madde)</span>
  </div>
  <table class="data-table">
    <thead>
      <tr>
        <th style="width: 24px;">#</th>
        <th style="width: 44px;">Ders</th>
        <th style="width: 110px;">Eşik / Oran / Değer</th>
        <th>Konu ve Kanuni Hüküm</th>
        <th style="width: 220px;">⚠️ Sınav Tuzağı & Çeldirici</th>
      </tr>
    </thead>
    <tbody>
      ${ratios
        .map(
          (item, idx) => `
        <tr>
          <td style="text-align: center; font-weight: bold; color: #64748b;">${idx + 1}</td>
          <td style="text-align: center;"><span class="module-code">${item.moduleId}</span></td>
          <td><span class="badge-cell badge-emerald">${escapeHtml(item.value)}</span></td>
          <td>
            <span class="item-title">${escapeHtml(item.title)}</span>
            <div class="item-desc">${escapeHtml(item.description)}</div>
          </td>
          <td>
            <div class="trap-box">
              <strong>Tuzak:</strong> ${escapeHtml(item.trap)}
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
  <!-- SECTION 3: COMPARISONS -->
  <div class="section-heading bg-comparisons">
    <span>⚖️ 3. SIKÇA KARIŞTIRILAN İKİLİ KAVRAMLAR VE ALTIN AYRIM KURALLARI</span>
    <span style="font-size: 8pt; font-weight: normal;">(${comparisons.length} Madde)</span>
  </div>
  <table class="data-table">
    <thead>
      <tr>
        <th style="width: 24px;">#</th>
        <th style="width: 44px;">Ders</th>
        <th style="width: 210px;">Kavram A</th>
        <th style="width: 210px;">Kavram B</th>
        <th>🎯 Altın Ayrım Kuralı</th>
      </tr>
    </thead>
    <tbody>
      ${comparisons
        .map(
          (item, idx) => `
        <tr>
          <td style="text-align: center; font-weight: bold; color: #64748b;">${idx + 1}</td>
          <td style="text-align: center;"><span class="module-code">${item.moduleId}</span></td>
          <td>
            <div class="comparison-box">
              <span class="item-title">${escapeHtml(item.conceptA.title)}</span>
              <div class="item-desc">${escapeHtml(item.conceptA.desc)}</div>
              <div style="font-weight: 700; color: #6d28d9; margin-top: 2px;">🔑 ${escapeHtml(item.conceptA.keyPoint)}</div>
            </div>
          </td>
          <td>
            <div class="comparison-box">
              <span class="item-title">${escapeHtml(item.conceptB.title)}</span>
              <div class="item-desc">${escapeHtml(item.conceptB.desc)}</div>
              <div style="font-weight: 700; color: #6d28d9; margin-top: 2px;">🔑 ${escapeHtml(item.conceptB.keyPoint)}</div>
            </div>
          </td>
          <td>
            <div class="comparison-rule">
              ${escapeHtml(item.differenceRule)}
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
  <!-- SECTION 4: EXAM TRAPS -->
  <div class="section-heading bg-traps">
    <span>🚨 4. ÖLÜMCÜL SINAV TUZAKLARI (DOĞRU BİLİNEN YANLIŞLAR)</span>
    <span style="font-size: 8pt; font-weight: normal;">(${traps.length} Madde)</span>
  </div>
  <table class="data-table">
    <thead>
      <tr>
        <th style="width: 24px;">#</th>
        <th style="width: 44px;">Ders</th>
        <th style="width: 230px;">❌ Sınavda Çeldirici (YANLIŞ ALGI)</th>
        <th style="width: 250px;">✅ Kanuni Gerçek (DOĞRU BİLGİ)</th>
        <th>💡 Sınav Notu</th>
      </tr>
    </thead>
    <tbody>
      ${traps
        .map(
          (item, idx) => `
        <tr>
          <td style="text-align: center; font-weight: bold; color: #64748b;">${idx + 1}</td>
          <td style="text-align: center;"><span class="module-code">${item.moduleId}</span></td>
          <td>
            <div class="trap-myth">
              "${escapeHtml(item.myth)}"
            </div>
          </td>
          <td>
            <div class="trap-reality">
              ${escapeHtml(item.reality)}
            </div>
          </td>
          <td>
            <div class="item-desc" style="font-style: italic; color: #475569;">
              ${escapeHtml(item.whyImportant)}
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

  <div class="footer">
    <span>© 2026 Emin ÇETİN • Tüm Hakları Saklıdır</span>
    <span>İçerik Kürasyonu & Yazılım: <strong>Emin ÇETİN</strong></span>
    <span>SPK SPL Düzey 1 Lisanslama Hazırlık Platformu (Temmuz 2026 Müfredatı)</span>
  </div>

  <script>
    window.addEventListener('DOMContentLoaded', () => {
      setTimeout(() => {
        window.print();
      }, 400);
    });
  </script>
</body>
</html>`;

  const iframe = document.createElement('iframe');
  iframe.style.position = 'fixed';
  iframe.style.right = '0';
  iframe.style.bottom = '0';
  iframe.style.width = '0';
  iframe.style.height = '0';
  iframe.style.border = '0';
  document.body.appendChild(iframe);

  const doc = iframe.contentWindow?.document || iframe.contentDocument;
  if (!doc) {
    const printWindow = window.open('', '_blank');
    if (printWindow) {
      printWindow.document.open();
      printWindow.document.write(html);
      printWindow.document.close();
    }
    return;
  }

  doc.open();
  doc.write(html);
  doc.close();

  setTimeout(() => {
    if (iframe.parentNode) {
      iframe.parentNode.removeChild(iframe);
    }
  }, 120000);
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
