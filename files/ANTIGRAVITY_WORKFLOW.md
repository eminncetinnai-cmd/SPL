# Antigravity'de SPK SPL1 Uygulaması Geliştirme Workflow

**Hedef**: Premium masaüstü sınav hazırlık uygulaması (Tauri + React + TypeScript)
**IDE**: Antigravity / Devin
**Süre**: ~5 gün (fazlama-fast modda)

---

## ADIM 1: Proje Başlatma (30 dakika)

### 1.1 Antigravity'ye Bagla
1. Antigravity uygulamasını aç
2. **New Project** → Desktop App (Tauri)
3. **Project Name**: `spk-spl1-exam-prep`
4. **Language**: TypeScript
5. **UI Framework**: React 18 + Vite

### 1.2 Başlangıç Prompt'u Gönder

Antigravity'deki prompt input'una **şunları** kopyala-yapıştır:

```
SYSTEM ROLE: [Yukarıdaki SYSTEM ROLE kısmını kopyala]

TASK: [Yukarıdaki TASK PROMPT'un tamamını kopyala]

USER'S DOCUMENT FOLDER: ~/Desktop/SPK_SPL1_Docs/
(Contains: 1001_questions.json, 1003_questions.json, 1005_questions.json, 1012_questions.json)

TECH STACK: Tauri 2 + React 18 + TypeScript + Tailwind CSS + shadcn/ui + Recharts
```

### 1.3 Devin'in Soracağı Sorulara Cevap Ver
Devin muhtemelen soracak:
- "Dökümanlarınız var mı, yoksa sıfırdan oluşturayım mı?"
  → **Cevap**: "Dökümanlarım var, yolunu belirtebiliyorum" ya da "Mock data ile başla, sonra gerçek verileri yüklerim"
- "Standart Puan hesaplaması istiyorsunuz mı?"
  → **Cevap**: "Şimdilik raw score + accuracy %, sonra Standart Puan ekleriz"
- "Farklı tema / renk şeması?"
  → **Cevap**: "Dark mode, premium fintech look (Bloomberg-inspired), accent: teal-500"

---

## ADIM 2: Döküman Hazırlığı (1-2 saat)

### 2.1 Dökümanlarını Dönüştür

Eğer dökümanlarınız `.md` veya `.txt` ise, Devin'den JSON'a çevirmesini iste:

**Beklenen JSON Format**:
```json
{
  "subject": "1001",
  "subject_name": "Sermaye Piyasası Mevzuatı Temel",
  "questions": [
    {
      "id": "q_1001_001",
      "text": "Sermaye piyasasının tanımı nedir?",
      "options": [
        { "key": "A", "text": "Uzun vadeli fonlar..." },
        { "key": "B", "text": "Kısa vadeli..." },
        { "key": "C", "text": "Depo hizmetleri..." },
        { "key": "D", "text": "Sigorta ürünleri..." },
        { "key": "E", "text": "Banka ürünleri..." }
      ],
      "correct_answer": "A",
      "explanation": "Sermaye piyasası, uzun vadeli fonların... (2-3 paragraf, detaylı açıklama)"
    }
  ]
}
```

### 2.2 Test Verisi Oluştur

Eğer gerçek veriler yoksa, Devin'den **mock dataset** oluşturmasını iste:
- Her konu (1001, 1003, 1005, 1012) için **5-10 örnek soru**
- Gerçekçi SPK içeriği
- `.json` dosya olarak (`~/Desktop/SPK_SPL1_Docs/` klasörüne koy)

**Prompt**:
```
Create realistic mock SPK SPL1 questions for subject 1001-1012 in JSON format.
Generate 8 questions per subject with:
- Realistic Turkish financial law questions
- 5 options (A-E)
- Detailed explanations (2-3 sentences)
- Save as: 1001_questions.json, 1003_questions.json, etc.
Place in ~/Desktop/SPK_SPL1_Docs/
```

---

## ADIM 3: Phase 1 - Temel Yapı (2-3 saat)

### 3.1 Tauri Project Scaffold

Prompt:
```
Phase 1: Foundation Setup
- Initialize Tauri project with cargo, create src-tauri/src/main.rs
- Implement SQLite schema in src-tauri/src/db.rs:
  * Tables: subjects, questions, quiz_sessions, quiz_answers, overall_results
- Create IPC command: load_documents_from_folder(folder_path: String)
  * Read all JSON files from folder
  * Parse & validate
  * Insert into SQLite
  * Return: { success: bool, loaded_count: int, error?: string }
- Write unit tests for JSON parsing and SQLite insertion
- Deliverable: `cargo build` runs without errors, SQLite DB is created
```

### 3.2 Kontrol
Devin tamamladığında:
- [ ] Tauri penceresi açılır mı?
- [ ] SQLite DB oluşturuldu mu (`app.db` ya da `data.db`)?
- [ ] Test verileri yüklendikten sonra `sqlite3 app.db "SELECT COUNT(*) FROM questions;"` çalışır mı?

---

## ADIM 4: Phase 2 - Quiz Engine & UI (3-4 saat)

### 4.1 Backend Commands

Prompt:
```
Phase 2: Quiz Engine & Frontend Scaffolds
Backend (Tauri Commands):
1. get_subject_list() → returns list of 4 subjects with question counts
2. start_quiz_session(subject_id: String) → returns session_id + first 3 questions
3. submit_answer(session_id, question_id, selected_option) → returns:
   {
     "question_id": "...",
     "selected": "A",
     "correct": "A",
     "is_correct": true,
     "explanation": "...",
     "next_question_id": "..." or null
   }
4. end_quiz_session(session_id) → returns score, accuracy_pct, time_spent

Write integration tests for each command.
```

### 4.2 Frontend Components

Prompt:
```
Phase 2 Frontend: React pages + components
Create:
1. pages/Home.tsx
   - Display 4 subject cards (1001, 1003, 1005, 1012)
   - Dark theme (bg-slate-900, text-white)
   - "Start Quiz" button per subject
   
2. pages/QuizDetail.tsx
   - Display question (centered, large)
   - 5 radio buttons (A-E)
   - After selection:
     * Show ✓ or ✗ badge (green/red)
     * Reveal explanation panel
     * Lock answer (disable further changes)
     * Show "Next Question" button (only after scrolling explanation)
   - Progress bar: "Question 3 of 25"

3. stores/quizStore.ts (Zustand)
   - State: session_id, subject_id, current_question, answers[], selectedAnswer, feedback
   - Actions: setSelectedAnswer, submitAnswer, nextQuestion

4. components/ExplanationPanel.tsx
   - Scrollable, min-height 200px
   - Shows explanation from DB
   - Fires onScrolledToBottom callback

Use Tailwind CSS + shadcn/ui for styling.
Write component tests.
```

### 4.3 Kontrol
- [ ] Home sayfasında 4 subject kartı görünüyor mü?
- [ ] Bir subject seçtiğinde quiz başlıyor mı?
- [ ] Soru görünüyor mu, şıklar tıklanabiliyor mu?
- [ ] Cevap seçince: badge gösterilme + explanation açılıyor mı?
- [ ] Next butonu sadece explanation'ı scroll ettikten sonra aktif mi?

---

## ADIM 5: Phase 3 - Results & Dashboard (3-4 saat)

### 5.1 Backend for Analytics

Prompt:
```
Phase 3: Results & Analytics Backend
Add IPC commands:
1. get_quiz_results(session_id: String) → returns:
   {
     "session_id": "...",
     "subject": "1001",
     "total_questions": 25,
     "correct_count": 21,
     "accuracy_pct": 84.0,
     "time_spent_minutes": 18,
     "answers": [
       { "question_id": "...", "selected": "A", "correct": "A", "is_correct": true, "time_sec": 45 },
       ...
     ]
   }

2. get_overall_analytics() → returns:
   {
     "subject_stats": {
       "1001": { "attempts": 3, "avg_accuracy": 82.5, "last_score": 84 },
       "1003": { "attempts": 2, "avg_accuracy": 76.0, "last_score": 80 },
       ...
     },
     "all_quizzes": [ { "date": "2025-01-15", "subject": "1001", "score": 84, "accuracy": 84.0 }, ... ]
   }

3. calculate_raw_score(correct_count: int) → returns raw_score (0-50 for SPK)

Test these with sample data.
```

### 5.2 Frontend Pages

Prompt:
```
Phase 3 Frontend: Results & Dashboard
Create:
1. pages/Results.tsx
   - Large score display: "21 / 25"
   - Accuracy badge: "84%" (color-coded: green >70%, yellow 50-70%, red <50%)
   - Time spent: "18 min 34 sec"
   - Collapsible Q&A review (all 25 questions with correct/incorrect badges)
   - "Back to Home" + "Retake Quiz" buttons

2. pages/Dashboard.tsx
   - 4 subject cards in grid (1001, 1003, 1005, 1012)
     * Last score, avg accuracy, mini sparkline trend
   - Charts (using Recharts):
     * Bar chart: Subject accuracy comparison (4 bars)
     * Line chart: Time series (last 5 quizzes)
     * Gauge/circular: Simulated exam score (if all 4 subjects done)
   - Stats table: Subject | Attempts | Avg Accuracy | Last Score | Trend
   
3. components/ResultsChart.tsx (Recharts bar chart)
4. components/TrendChart.tsx (Recharts line chart)

Use dark theme (bg-slate-800 cards, teal-500 accents).
Premium fintech styling (Bloomberg-inspired).
```

### 5.3 Kontrol
- [ ] Quiz bittikten sonra Results sayfası yükleniyor mu?
- [ ] Skor, accuracy, zaman görünüyor mu?
- [ ] Dashboard'da 4 subject kartı görünüyor mu?
- [ ] Bar chart (subject comparison) çiziliyor mu?
- [ ] Line chart (trend) çiziliyor mu?

---

## ADIM 6: Phase 4 - Polish & Settings (2-3 saat)

### 6.1 Settings & History

Prompt:
```
Phase 4: Settings, History, Export
Create:
1. pages/Settings.tsx
   - Document folder picker (file dialog)
   - Theme toggle (dark/light)
   - Export results (CSV download)
   - Clear history (with confirmation dialog)
   - About + app version

2. Quiz History (sidebar modal)
   - Last 10 quizzes
   - Click to view details
   - Subject, date, score, accuracy

3. Export functionality
   - CSV: quiz_date, subject, score, accuracy, time_spent
   - Save to ~/Downloads/spk_results_export.csv

Add keyboard shortcuts:
   - Enter = submit answer
   - Esc = back to home
   - R = retake quiz
```

### 6.2 UX Polish

Prompt:
```
Polish & Error Handling:
1. Loading states: Show spinner when fetching from backend
2. Toast notifications: Success/error messages (use sonner or react-hot-toast)
3. Smooth transitions: Fade, slide animations for page changes
4. Error handling:
   - Document folder not found: Show friendly error, suggest correct path
   - DB corruption: Auto-recovery or reset option
   - IPC timeout: Retry mechanism
5. Responsive design: Test on 1366x768 and 1920x1080 (and mobile if needed)
6. Accessibility: alt text, ARIA labels, keyboard navigation

Write tests for error scenarios.
```

### 6.3 Kontrol
- [ ] Settings sayfası açılıyor mu?
- [ ] Document folder yeniden yüklenebiliyor mu?
- [ ] Export CSV çalışıyor mu?
- [ ] Hata durumlarında user-friendly mesaj mı var?
- [ ] Keyboard shortcuts çalışıyor mu?

---

## ADIM 7: Build & Release (1 saat)

### 7.1 Desktop Build

Prompt:
```
Build for Desktop:
1. Run: cargo tauri build
   - Creates .exe (Windows) or .dmg (Mac)
   - File size should be <50MB

2. Test standalone app:
   - Click .exe / open .dmg
   - App launches without dependencies
   - Load documents from ~/Desktop/SPK_SPL1_Docs/
   - Take a quiz
   - View results & dashboard
   - No errors in console

3. Create installer (MSI for Windows, DMG for Mac)
```

### 7.2 Kontrol Listesi (Final)
- [ ] `cargo build` başarılı
- [ ] Tauri app penceresi açılıyor
- [ ] Başlangıç sayfasında 4 subject kartı
- [ ] Quiz akışı (Q → cevap → feedback → next → results)
- [ ] Dashboard ve charts çalışıyor
- [ ] Settings ve export çalışıyor
- [ ] Hata durumları gracefully işleniyor
- [ ] Responsiveness: 1366x768 ve 1920x1080 test edildi
- [ ] Tests passing: `npm run test` %70+ coverage

---

## ADIM 8: Devin'e Verdiğin Prompt Şablonları

### Template 1: Phase Başlatma
```
[PHASE_NUMBER]. [PHASE_NAME]

Requirements:
- [req1]
- [req2]
- [req3]

Deliverable:
- Code in src/... and src-tauri/src/...
- Tests: unit + integration
- No console errors
- Ready for next phase

Tech Stack: Tauri + React + TypeScript + Tailwind + Recharts
```

### Template 2: Bug Fixing
```
Found bug: [describe issue]
Affected file: src/pages/QuizDetail.tsx (or wherever)
Expected behavior: [what should happen]
Actual behavior: [what happens now]

Fix this and write a test case so it doesn't regress.
```

### Template 3: Refactoring
```
Refactor [component/module] to:
- Separate concerns (X logic goes to store, Y goes to component)
- Improve performance (memo, useMemo for props/state)
- Better testing surface (pure functions, easier to mock)

Keep functionality same, just improve code quality.
```

---

## Pratik İpuçları

### 1. Test Verisi ile Başla
Gerçek dökümanlar yoksa, Devin mock data oluşturacak. Sonra swap-in edersin.

### 2. Phase by Phase
Her phase bittikten sonra **test et**. Hata varsa, hemen sor. Bir önceki phaseye gitmeden yeni phase'e geçme.

### 3. Commit Sıklığı
Devin'den isteki: "Her phase sonunda commit yap, mesaj yaz (ör: 'Phase 2: Quiz engine & UI')"

### 4. Version Control
Git init et:
```bash
cd spk-spl1-app
git init
git add .
git commit -m "Initial: Tauri + React scaffold"
```

### 5. Performance
- Quiz loading: <1s
- Answer feedback: <500ms
- Dashboard charts: <2s (even with 100 quiz history)

---

## Beklenen Output Formatı

Her Phase sonunda Devin şunu deliver etmeli:
```
✅ Phase [N] Complete
- Files: [list of new/modified files]
- Tests: [count passing tests]
- Status: Ready for Phase [N+1]
- Known issues: [any WIP or tech debt]
```

---

## Troubleshooting

### Tauri IPC timeout
→ Backend command çok uzun sürüyor. Devin'den async/await fix isteyebilirsin.

### SQLite lock error
→ Multiple connections conflict. Devin connection pool ekleyecek.

### Build fails: "not found: cargo"
→ Rust toolchain install et: `curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh`

### Charts not rendering
→ Recharts version mismatch. Devin dependency update etsin.

---

## Final Checklist Before Deploy

```
App Quality
- [ ] No console errors
- [ ] All tests passing (npm run test)
- [ ] Responsive design tested (1366x768, 1920x1080)
- [ ] Dark theme consistent across all pages
- [ ] 4 subjects + results + dashboard all functional

Performance
- [ ] Quiz load <1s
- [ ] Answer feedback <500ms
- [ ] Dashboard <2s
- [ ] Build size <50MB

Documentation
- [ ] README.md (how to load docs, take quiz, view results)
- [ ] ADMIN_GUIDE.md (how to add new questions to DB)
- [ ] TROUBLESHOOTING.md (common issues & fixes)

Deployment
- [ ] .exe (Windows) or .dmg (Mac) built
- [ ] Standalone app tested (no dependencies)
- [ ] Installer works
```

---

**Ready? Copy the full SYSTEM ROLE + TASK PROMPT to Antigravity, paste your folder path, and let Devin build! 🚀**
