# 🎯 Devin / Antigravity - Hazır-Yapıştır Prompt

**Aşağıdakileri Antigravity'nin prompt alanına kopyala-yapıştır:**

---

## COPY-PASTE BAŞLA 👇

```
ROLE: SPK SPL1 Premium Exam Prep Application Architect

You are building a professional, premium desktop exam preparation platform for Turkish SPK SPL1 (Securities Market Law) certification.

CORE PRINCIPLES:
1. Data Integrity: Question/answer data is immutable (loaded from source, never mutated in UI)
2. Modular: Subjects 1001, 1003, 1005, 1012 are independent quiz modules
3. Premium UX: Dark Bloomberg-inspired theme, smooth animations, professional charts
4. SPK Grading: 50 questions max, 1 point each = 100 points max
5. Transparent Scoring: Show raw score + accuracy % + subject breakdown

TECH STACK: Tauri 2 + React 18 + TypeScript + Tailwind CSS + shadcn/ui + Recharts + Zustand

PROJECT STRUCTURE:
spk-spl1-app/
├── src-tauri/
│  ├── src/
│  │  ├── main.rs (IPC commands)
│  │  ├── db.rs (SQLite helpers)
│  │  └── scoring.rs (SPK scoring logic)
│  ├── Cargo.toml
│  └── tauri.conf.json
├── src/
│  ├── App.tsx
│  ├── pages/ (Home, QuizDetail, Results, Dashboard, Settings)
│  ├── components/ (QuestionCard, AnswerSelector, ExplanationPanel, Charts)
│  ├── stores/ (quizStore.ts, analyticsStore.ts - Zustand)
│  └── utils/
├── package.json
├── vite.config.ts
├── tsconfig.json
└── README.md

USER'S DOCUMENT FOLDER: ~/Desktop/SPK_SPL1_Docs/

EXPECTED JSON FORMAT:
{
  "subject": "1001",
  "subject_name": "Sermaye Piyasası Mevzuatı Temel",
  "questions": [
    {
      "id": "q_1001_001",
      "text": "Question text here",
      "options": [
        { "key": "A", "text": "Option A" },
        { "key": "B", "text": "Option B" },
        { "key": "C", "text": "Option C" },
        { "key": "D", "text": "Option D" },
        { "key": "E", "text": "Option E" }
      ],
      "correct_answer": "A",
      "explanation": "Detailed 2-3 paragraph explanation"
    }
  ]
}

---

## PHASE 1: FOUNDATION (Day 1-2)

Task: Initialize Tauri project, create SQLite schema, build document loader

Requirements:
1. Initialize Tauri project with React + TypeScript scaffold
2. Create SQLite schema (src-tauri/src/db.rs):
   - Tables: subjects, questions, quiz_sessions, quiz_answers, overall_results
   - Schema should support exam question storage and progress tracking
3. Implement IPC command: load_documents_from_folder(folder_path: String)
   - Read all JSON files from folder
   - Validate against expected schema
   - Insert into SQLite (check for duplicates)
   - Return: { success: bool, loaded_count: int, errors?: string[] }
4. Write unit tests for JSON parsing and SQLite operations
5. Ensure `cargo build` completes without errors

Deliverable:
- ✅ Tauri project structure created
- ✅ SQLite DB initialized
- ✅ Document loader functional
- ✅ Tests passing
- ✅ Ready for Phase 2

---

## PHASE 2: QUIZ ENGINE & BASIC UI (Day 2-3)

Task: Build quiz flow (subject selection → question → answer → feedback)

Backend Requirements (Tauri Commands in src-tauri/src/main.rs):
1. get_subject_list() 
   → Returns: [{ id: "1001", name: "...", question_count: int }]

2. start_quiz_session(subject_id: String) 
   → Returns: { session_id: String, questions: [{ id, text, options }] }

3. submit_answer(session_id: String, question_id: String, selected_option: String) 
   → Returns: {
       "question_id": "q_1001_001",
       "selected": "A",
       "correct": "A",
       "is_correct": true,
       "explanation": "...",
       "next_question_id": "q_1001_002" or null
     }

4. end_quiz_session(session_id: String) 
   → Returns: { session_id, subject_id, correct_count, raw_score, accuracy_pct, time_spent_seconds }

Write integration tests for each command.

Frontend Requirements (React pages + components):

1. pages/Home.tsx
   - Display 4 subject cards (1001, 1003, 1005, 1012) in responsive grid
   - Dark theme: bg-slate-900, text-white, accent: teal-500
   - Each card shows: subject name, question count, last quiz date (if exists), "Start Quiz" button
   - Card hover effect (shadow lift)

2. pages/QuizDetail.tsx
   - Display current question (large, centered text)
   - Show 5 radio buttons for options A-E
   - CRITICAL: Answer Lock Mechanism:
     * Before selection: all options clickable
     * After selection:
       - Show ✓ (green badge) or ✗ (red badge) immediately
       - Disable further option changes (lock radio)
       - Reveal explanation panel below
       - Show "Next Question" button (DISABLED until explanation scrolled to bottom)
   - Progress bar: "Question 3 of 25"
   - Component styling: card-based, clean typography

3. components/ExplanationPanel.tsx
   - Scrollable container (min-height: 200px)
   - Display explanation from database
   - Emit onScrolledToBottom event when user scrolls to end
   - Styling: light text on dark bg, readable font size

4. stores/quizStore.ts (Zustand state management)
   ```typescript
   interface QuizState {
     session_id: string | null;
     subject_id: string;
     current_question: Question | null;
     answers: AnswerRecord[];
     selectedAnswer: string | null;
     feedback: { is_correct: boolean; explanation: string } | null;
     explanationRead: boolean;
     
     setSelectedAnswer: (option: string) => void;
     submitAnswer: () => Promise<void>;
     nextQuestion: () => void;
     endQuiz: () => Promise<void>;
   }
   ```

5. Use Tailwind CSS + shadcn/ui for all components
6. Write component tests (React Testing Library)

Deliverable:
- ✅ Home page with 4 subject cards
- ✅ Quiz detail page with question + options
- ✅ Answer lock mechanism (lock after select, unlock after explanation read)
- ✅ Feedback display (correct/incorrect badge)
- ✅ Navigation (next question works)
- ✅ All tests passing
- ✅ Ready for Phase 3

---

## PHASE 3: RESULTS & ANALYTICS DASHBOARD (Day 3-4)

Task: Build results display and professional analytics dashboard

Backend Requirements (Tauri Commands):

1. get_quiz_results(session_id: String)
   → Returns: {
       "session_id": "...",
       "subject": "1001",
       "subject_name": "...",
       "total_questions": 25,
       "correct_count": 21,
       "raw_score": 21,
       "accuracy_pct": 84.0,
       "time_spent_minutes": 18,
       "answers": [
         {
           "question_id": "...",
           "selected": "A",
           "correct": "A",
           "is_correct": true,
           "time_sec": 45
         },
         ...
       ]
     }

2. get_overall_analytics()
   → Returns: {
       "subject_stats": {
         "1001": { "attempts": 3, "avg_accuracy": 82.5, "last_score": 84 },
         "1003": { "attempts": 2, "avg_accuracy": 76.0, "last_score": 80 },
         "1005": { "attempts": 1, "avg_accuracy": 88.0, "last_score": 88 },
         "1012": { "attempts": 0, "avg_accuracy": null, "last_score": null }
       },
       "all_quizzes": [
         { "date": "2025-01-15", "subject": "1001", "score": 84, "accuracy": 84.0, "time_minutes": 18 },
         ...
       ]
     }

Frontend Requirements:

1. pages/Results.tsx
   - Large score display: "21 / 25" (bold, teal color)
   - Accuracy badge: "84%" (color-coded: green >70%, yellow 50-70%, red <50%)
   - Time spent: "18 minutes 34 seconds"
   - "Reviewed X/25 explanations" or similar
   - Collapsible Q&A review: all 25 questions with:
     * Question text (shortened if needed)
     * Selected answer + correct answer
     * Green ✓ / red ✗ badge
     * Link to full explanation (modal or expand)
   - Action buttons: "Back to Home" + "Retake Quiz"

2. pages/Dashboard.tsx (Analytics Dashboard)
   - Professional fintech styling (Bloomberg-inspired dark theme)
   - Grid layout:
     * Top row: 4 subject status cards (1001, 1003, 1005, 1012)
       - Last score, avg accuracy %, mini sparkline trend
       - "Practice" button per subject
     * Chart section:
       - Chart 1: Bar chart - Subject Accuracy Comparison (4 bars, each subject)
       - Chart 2: Line chart - Time series (last 5-10 quizzes, trend over time)
       - Chart 3: Gauge/Circular Progress - Simulated Exam Score (if all 4 subjects attempted)
     * Stats table:
       Columns: Subject | Attempts | Avg Accuracy | Last Score | Trend (↗ ↙ ➡)
   
3. components/ResultsChart.tsx (Recharts Bar Chart)
   - X-axis: Subject (1001, 1003, 1005, 1012)
   - Y-axis: Accuracy % (0-100)
   - Use teal-500 color, dark background
   - Show values on top of bars

4. components/TrendChart.tsx (Recharts Line Chart)
   - X-axis: Quiz date/number
   - Y-axis: Score (0-25 or %)
   - Multiple lines if tracking multiple subjects
   - Smooth curve interpolation

5. Use Recharts for all charts (professional, responsive, dark theme compatible)
6. Write tests for chart rendering

Styling (Premium Dark Theme):
- Cards: bg-slate-800 border border-slate-700 rounded-lg
- Text: text-slate-100 (primary), text-slate-400 (secondary)
- Accent: text-teal-500, hover:bg-teal-900/20
- Backgrounds: gradient from-slate-950 to-slate-900
- Font: Inter (sans-serif) for body, monospace for scores

Deliverable:
- ✅ Results page shows score + accuracy + time
- ✅ Q&A review collapsible (all questions visible)
- ✅ Dashboard page renders without errors
- ✅ Bar chart (subject comparison) displays correctly
- ✅ Line chart (time series) displays correctly
- ✅ Gauge chart (exam score simulation) displays correctly
- ✅ Stats table updates after quiz
- ✅ All tests passing
- ✅ Ready for Phase 4

---

## PHASE 4: SETTINGS, POLISH & EXPORT (Day 4-5)

Task: Add settings page, quiz history, export functionality, and UX polish

Frontend Requirements:

1. pages/Settings.tsx
   - Document folder picker
     * Show current folder path
     * Button: "Change Folder" (file dialog)
     * Button: "Reload Documents" (re-import from folder)
     * Status: "25 questions loaded for 1001" etc.
   - Theme toggle: "Dark Mode" / "Light Mode" (currently only Dark supported)
   - Export results:
     * Button: "Export to CSV"
     * CSV format: quiz_date, subject, score, accuracy_pct, time_spent_minutes
     * Save to ~/Downloads/spk_results_export_[timestamp].csv
   - Clear history:
     * Button: "Clear All Quiz History"
     * Confirmation dialog: "Delete all X quizzes? This cannot be undone."
   - About section:
     * App name: "SPK SPL1 Exam Prep"
     * Version: "1.0.0"
     * Copyright, support info

2. Quiz History (sidebar or modal)
   - Show last 10 quizzes (sortable by date)
   - Columns: Date, Subject, Score, Accuracy, Time
   - Click row to view full quiz details
   - Delete individual quiz option

3. UX Polish & Error Handling
   - Loading states: Show spinner while backend processes
   - Toast notifications: Use sonner or react-hot-toast for success/error messages
   - Smooth page transitions: Fade-in/fade-out animations
   - Error scenarios:
     * Document folder not found: "Folder not found. Please select correct path."
     * DB corruption: Auto-recovery or user-friendly reset option
     * IPC timeout: "Taking longer than usual... retrying" + retry button
   - Responsive design: Test on 1366x768 and 1920x1080
   - Accessibility: alt text, ARIA labels, keyboard navigation
   - Keyboard shortcuts:
     * Enter = submit answer
     * Esc = back to home
     * R = retake quiz

4. IPC Error Handling
   - Wrap all Tauri command calls in try/catch
   - Implement retry mechanism for timeouts
   - Log errors to console (dev mode only) or file (production)

Deliverable:
- ✅ Settings page fully functional
- ✅ Document folder can be changed and reloaded
- ✅ Export to CSV works
- ✅ Clear history works (with confirmation)
- ✅ Quiz history visible in sidebar/modal
- ✅ Toast notifications working
- ✅ Smooth page transitions
- ✅ Error handling covers all edge cases
- ✅ Responsive on 1366x768 and 1920x1080
- ✅ Keyboard shortcuts functional
- ✅ All tests passing
- ✅ Ready for build

---

## PHASE 5: BUILD & RELEASE (Day 5)

Task: Build desktop app and verify standalone functionality

Requirements:
1. Run: cargo tauri build
   - Creates .exe (Windows) or .dmg (Mac)
   - File size should be <50MB
   - No build errors

2. Test standalone app:
   - Click .exe / open .dmg
   - App launches without external dependencies
   - Load documents from ~/Desktop/SPK_SPL1_Docs/
   - Take a full 25-question quiz
   - Submit answers, see feedback
   - View results
   - Check dashboard
   - Export results CSV
   - No console errors or crashes

3. Create installer (optional):
   - MSI installer for Windows (via WiX or NSIS)
   - DMG installer for Mac
   - Include version number, company info

Deliverable:
- ✅ Standalone .exe/.dmg created
- ✅ Installer working
- ✅ All features tested and working
- ✅ No runtime errors
- ✅ Release-ready

---

## TESTING STRATEGY

Unit Tests (per component):
- [ ] JSON parsing tests
- [ ] SQLite CRUD tests
- [ ] Score calculation tests
- [ ] Component render tests

Integration Tests:
- [ ] load_documents_from_folder with mock JSON
- [ ] Full quiz flow (start → answer → end)
- [ ] Results calculation and display

Visual Tests (manual):
- [ ] Responsive design (1366x768, 1920x1080)
- [ ] Dark theme consistency
- [ ] Chart rendering
- [ ] Error message display

Performance Tests:
- [ ] Quiz load time <1s
- [ ] Answer feedback <500ms
- [ ] Dashboard load <2s

---

## KNOWN CONSTRAINTS

- User folder path: ~/Desktop/SPK_SPL1_Docs/
- Subjects: 1001, 1003, 1005, 1012
- Max questions per subject: typically 25
- Max score: 50 (if simulating full exam across 4 subjects)
- Database: SQLite (local, encrypted by Tauri)
- No internet required (fully offline)
- Windows & Mac target platforms

---

## SUCCESS CRITERIA

✅ App launches and renders Home page with 4 subject cards
✅ User can load documents and see "X questions loaded"
✅ Full quiz flow works: select subject → answer all questions → see results
✅ Answer lock mechanism working (can't change answer after selecting)
✅ Feedback shows correct/incorrect badge + explanation
✅ Results page displays score, accuracy, time
✅ Dashboard shows professional charts and stats
✅ Settings page allows folder change and export
✅ Responsive design tested on 1366x768 and 1920x1080
✅ No console errors
✅ Standalone .exe/.dmg works without dependencies
✅ All tests passing with >70% coverage

---

## COMMIT MESSAGES (Git)

- "Phase 1: Tauri scaffold, SQLite schema, document loader"
- "Phase 2: Quiz engine, home page, quiz detail page"
- "Phase 3: Results page, dashboard, charts (Recharts)"
- "Phase 4: Settings, history, export, polish, error handling"
- "Phase 5: Build, release, final testing"

---

## NOTES

- If user doesn't have documents yet, I can generate mock questions (5-8 per subject) for testing. Just ask.
- Each subject should be independent (no cross-contamination of answers between 1001/1003/1005/1012)
- Premium UX means: smooth animations, professional fonts, clean spacing, dark theme throughout
- SPK scoring is straightforward: 1 point per correct answer, max 50 if full exam simulated
- Standart Puan (Z-score) can be added later if baseline statistics available

Ready to start Phase 1? Confirm folder path and proceed.

```

## COPY-PASTE SONA ULAŞTI 👆

---

## Sonra Neler Yapacaksın?

1. **Devin'e Gönder**: Yukarıdaki metni Antigravity prompt alanına kopyala-yapıştır
2. **Dosya Yolunu Belirt**: Devin'e sor: "Belirttiğim klasör yolu ~/Desktop/SPK_SPL1_Docs/ doğru mu?"
3. **Test Verisi**: Eğer gerçek sorularınız yoksa, Devin "5 mock soru per subject oluştur" yapacak
4. **Phase 1 Başlasın**: Devin Tauri scaffold'ı oluşturacak, SQLite schema'sını yazacak

---

## Beklenen Yanıt (Devin'den)

Devin şu şekilde start edecek:

```
✅ Phase 1 Starting
- Creating Tauri project structure...
- Defining SQLite schema (subjects, questions, quiz_sessions, etc.)
- Implementing document loader IPC command
- Writing unit tests...

Will confirm once scaffold is complete. Ready to verify? (Y/N)
```

Then:
```
✅ Phase 1 Complete
- Files created: src-tauri/src/main.rs, src-tauri/src/db.rs
- Database schema: 5 tables created
- Document loader: Tested with 25 mock questions (1001 subject)
- Tests: 8/8 passing ✓

Proceed to Phase 2? (Y/N)
```

---

## Emin'in Checklist (Bugün)

- [ ] Dökümanlarınızı kontrol et (~/Desktop/SPK_SPL1_Docs/ klasöründe var mı?)
- [ ] Devin prompt'unu kopyala-yapıştır
- [ ] Phase 1 tamamlandığında tasdik et
- [ ] Hata varsa, rapor et
- [ ] Phase 2 başlatıl

---

**Başlamaya hazır? 🚀**
