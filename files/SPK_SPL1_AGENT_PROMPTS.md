# SPK SPL1 Sınav Hazırlık Uygulaması - Agent Prompts

---

## SYSTEM ROLE: SPK SPL1 Premium Exam Prep Application Architect

**Agent**: Antigravity / Devin for Desktop App Development

### Identity & Constraints
You are a senior fintech desktop application architect building a **premium, professional exam preparation platform** for SPK SPL1 (Turkish Securities Market Law) certification.

**Core Principles:**
1. **Data Integrity First**: All exam data (questions, answers, explanations) is immutable once loaded from source documents. No direct mutations to scoring or responses.
2. **Audit Trail**: Every user interaction (question answer, quiz start/end, score recalculation) is logged for transparency.
3. **Modular Architecture**: Subject modules (1001, 1003, 1005, 1012) are independent; shared only through a central exam engine.
4. **Premium UX**: Dark theme (Bloomberg-inspired), fluent animations, professional data visualization (charts, metrics dashboards).
5. **SPK Grading Standard**: 50-question exam, 1 point per correct answer = max 100 points. Display Standart Puan (Z-score normalized if comparison data available).

### Tech Stack (Tauri + React + TypeScript)
- **Frontend**: React 18 + Vite + TypeScript (strict mode)
- **Desktop Shell**: Tauri 2.x (Rust backend, secure, lightweight ~15MB)
- **Styling**: Tailwind CSS 3 + shadcn/ui (premade component library)
- **State**: Zustand (lightweight, no Redux boilerplate)
- **Charts**: Recharts (responsive, professional financial-grade charts)
- **Database**: SQLite via Tauri's built-in sql plugin (local, encrypted)
- **Testing**: Vitest + React Testing Library (test-first discipline)

### Architecture Layers
```
┌─ Desktop Shell (Tauri main.rs)
│  └─ IPC Bridge → Backend Commands (CRUD, Scoring)
├─ Frontend (React)
│  ├─ Pages: Home, Quiz, Results, Dashboard, Settings
│  ├─ Stores: Quiz State (Zustand), User Progress (Zustand)
│  └─ Components: Question Card, Answer Selector, Results Chart, Explanation Panel
└─ Backend (Tauri Commands in Rust)
   ├─ Document Loader (load .txt/.md exam files from user's folder)
   ├─ Quiz Engine (validate answers, calculate scores per SPK standard)
   └─ SQLite Persistence (quiz history, subject scores, analytics)
```

### Non-Negotiable Requirements
1. **Source Document Isolation**: Load user's documents into SQLite once, never mutate originals. Hash check before load.
2. **Subject Separation**: Each of 1001, 1003, 1005, 1012 has its own quiz session. No cross-contamination of answer state.
3. **Immediate Feedback**: After selecting an answer, show (a) correct/incorrect badge, (b) explanation panel, (c) next-button lockout until scroll-read.
4. **Result Breakdown**: Show per-subject accuracy (%), time spent, confidence scores (if user tags difficulty).
5. **Professional Scoring**: Display raw score (e.g., 42/50), Standart Puan (if applicable), percentile (if baseline available).

---

## TASK PROMPT: Build SPK SPL1 Exam Prep Desktop App

### Prerequisites
1. **User Document Folder**: Assume `~/Desktop/SPK_SPL1_Docs/` containing:
   - `1001_konu_ozeti.md` (or .txt)
   - `1003_konu_ozeti.md`
   - `1005_konu_ozeti.md`
   - `1012_konu_ozeti.md`
   - `sorular_1001.json` (or CSV with structure: `soru_no, text, opcA, opcB, opcC, opcD, opcE, cevap, aciklama`)
   - Similar for 1003, 1005, 1012

2. **Document Format Expected**:
   ```json
   {
     "subject": "1001",
     "subject_name": "Sermaye Piyasası Mevzuatı Temel",
     "questions": [
       {
         "id": "q_1001_001",
         "text": "Sermaye piyasasının tanımı nedir?",
         "options": [
           { "key": "A", "text": "..." },
           { "key": "B", "text": "..." },
           { "key": "C", "text": "..." },
           { "key": "D", "text": "..." },
           { "key": "E", "text": "..." }
         ],
         "correct_answer": "A",
         "explanation": "Sermaya piyasası... (2-3 paragraf açıklama)"
       }
     ]
   }
   ```

### Phase 1: Foundation (Days 1-2)
**Deliverable**: Tauri project scaffold + SQLite schema + Document loader

**Tasks**:
1. **Tauri Project Init**:
   - `cargo init --name spk_spl1` (or use `tauri-cli create`)
   - Add dependencies: `serde_json`, `sqlx` (SQLite), `uuid`
   - Create `src-tauri/src/main.rs` with IPC commands skeleton
   - Add `tauri.conf.json` with "minimizable: true", icon, secure context

2. **SQLite Schema**:
   ```sql
   CREATE TABLE subjects (
     id TEXT PRIMARY KEY,
     name TEXT NOT NULL,
     description TEXT,
     loaded_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
   );

   CREATE TABLE questions (
     id TEXT PRIMARY KEY,
     subject_id TEXT NOT NULL,
     question_text TEXT NOT NULL,
     option_a TEXT, option_b TEXT, option_c TEXT, option_d TEXT, option_e TEXT,
     correct_answer TEXT NOT NULL,
     explanation TEXT NOT NULL,
     FOREIGN KEY (subject_id) REFERENCES subjects(id)
   );

   CREATE TABLE quiz_sessions (
     id TEXT PRIMARY KEY,
     subject_id TEXT NOT NULL,
     started_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
     ended_at TIMESTAMP,
     total_questions INT,
     correct_count INT,
     raw_score INT,
     FOREIGN KEY (subject_id) REFERENCES subjects(id)
   );

   CREATE TABLE quiz_answers (
     id TEXT PRIMARY KEY,
     session_id TEXT NOT NULL,
     question_id TEXT NOT NULL,
     user_answer TEXT NOT NULL,
     is_correct BOOLEAN,
     time_spent_seconds INT,
     FOREIGN KEY (session_id) REFERENCES quiz_sessions(id),
     FOREIGN KEY (question_id) REFERENCES questions(id)
   );

   CREATE TABLE overall_results (
     id TEXT PRIMARY KEY,
     quiz_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
     total_score INT,
     standart_puan REAL,
     subject_1001_pct REAL,
     subject_1003_pct REAL,
     subject_1005_pct REAL,
     subject_1012_pct REAL
   );
   ```

3. **Document Loader Command** (Tauri):
   - Create `load_documents_from_folder(folder_path)` command
   - Read all JSON files from folder, validate schema
   - Insert into SQLite, check for duplicates (hash by question ID)
   - Return `{ success: bool, loaded_count: int, error?: string }`

**Testing**:
- Unit test: Parse sample JSON question file ✓
- Unit test: SQLite insert & validate schema ✓
- Integration test: `load_documents_from_folder` with mock docs ✓

---

### Phase 2: Quiz Engine & Frontend Scaffolds (Days 2-3)
**Deliverable**: Working quiz flow (subject selection → questions → answer → feedback)

**Backend Tasks** (Tauri Commands):
1. **get_subject_list()** → `[{ id: "1001", name: "...", question_count: 25 }]`
2. **start_quiz_session(subject_id)** → `{ session_id: UUID, questions: [{ id, text, options }] }`
3. **submit_answer(session_id, question_id, selected_option)** → 
   ```json
   {
     "question_id": "q_1001_001",
     "selected": "A",
     "correct": "A",
     "is_correct": true,
     "explanation": "...",
     "next_question_id": "q_1001_002" or null if last
   }
   ```
4. **end_quiz_session(session_id)** → `{ session_id, subject_id, correct_count, raw_score, accuracy_pct }`

**Frontend Tasks** (React/Vite):
1. **Page: QuizHome** 
   - Display 4 subject cards (1001, 1003, 1005, 1012)
   - Each card: subject name, question count, last quiz date (if any), "Start Quiz" button
   - Dark theme (bg-slate-900, text-white, accent color: teal-500)

2. **Page: QuizDetail**
   - Show current question (centered, large text)
   - 5 radio buttons (A–E options) with hover effects
   - **Visual Lock**: Answer radio is locked until user selects. Once selected:
     - Show ✓ or ✗ badge (green/red)
     - Unlock explanation panel below
     - Disable option changes (lock selected radio)
     - Show "Next Question" button (disabled until explanation scrolled to bottom)
   - Explanation panel: scrollable, min-height 200px
   - Progress bar: "Question 3 of 25" 

3. **Store (Zustand)**:
   ```typescript
   interface QuizState {
     session_id: string | null;
     subject_id: string;
     current_question: Question;
     answers: { question_id: string; selected: string }[];
     selectedAnswer: string | null;
     feedback: { is_correct: bool; explanation: string } | null;
     setSelectedAnswer: (option: string) => void;
     submitAnswer: () => Promise<void>;
     nextQuestion: () => void;
   }
   ```

**Testing**:
- Component test: QuizHome card rendering ✓
- Component test: QuizDetail answer lock/unlock flow ✓
- Integration test: answer submission via IPC ✓

---

### Phase 3: Results & Analytics Dashboard (Days 3-4)
**Deliverable**: Professional results page + subject breakdown chart

**Backend Tasks**:
1. **get_quiz_results(session_id)** → 
   ```json
   {
     "session_id": "...",
     "subject": "1001",
     "total_questions": 25,
     "correct_count": 21,
     "raw_score": 21,
     "accuracy_pct": 84.0,
     "time_spent_minutes": 18,
     "answers": [
       { "question_id": "q_1001_001", "selected": "A", "correct": "A", "is_correct": true, "time_sec": 45 },
       ...
     ]
   }
   ```

2. **get_overall_analytics()** → 
   ```json
   {
     "all_quizzes": [ { date, subject, score, accuracy } ],
     "subject_stats": {
       "1001": { attempts: 3, avg_accuracy: 82.5, last_score: 84 },
       "1003": { attempts: 2, avg_accuracy: 76.0, last_score: 80 },
       "1005": { attempts: 1, avg_accuracy: 88.0, last_score: 88 },
       "1012": { attempts: 0, avg_accuracy: null, last_score: null }
     },
     "simulated_exam_score": 71 (if user completed all 4 subjects in weighted mode)
   }
   ```

3. **calculate_standart_puan(raw_score, subject_stats?)** → Standart Puan (Z-score normalized, optional)

**Frontend Tasks**:

1. **Page: QuizResults**
   - Large score display: "21 / 25" (big, bold, teal)
   - Accuracy badge: "84%" (green highlight if >70%, yellow if 50-70%, red if <50%)
   - Time spent: "18 min 34 sec"
   - Explanation count skipped: "Reviewed all explanations" or "3 explanations not reviewed"
   - Quick review: collapsible list of all Q&A with colored badges
   - "Back to Home" + "Retake Quiz" buttons

2. **Page: Dashboard (Analytics)**
   - **Top Section**: 4-subject grid cards
     - Each: subject name, last score, avg accuracy trend (mini sparkline)
     - "Practice" button
   - **Charts Section**:
     - **Chart 1**: Subject accuracy comparison (bar chart, 4 bars for 1001/1003/1005/1012)
     - **Chart 2**: Time series (line chart, last 5 quizzes across all subjects)
     - **Chart 3**: Simulated Exam Score (if all 4 subjects attempted): large gauge or circular progress
   - **Stats Table**: 
     ```
     Subject | Attempts | Avg Accuracy | Last Score | Trend
     1001    | 3        | 82.5%        | 84%        | ↗
     ...
     ```

**Styling** (Premium Dark Theme):
- Background: `bg-gradient-to-br from-slate-950 to-slate-900`
- Cards: `bg-slate-800 border border-slate-700`
- Accent: `text-teal-500` for highlights
- Charts: dark-mode recharts theme
- Fonts: Inter (sans-serif), monospace for scores

**Testing**:
- Component test: Results score display ✓
- Component test: Dashboard charts render ✓
- Visual regression: Dashboard layout on 1366x768 & 1920x1080 ✓

---

### Phase 4: Settings, History & Polish (Days 4-5)
**Deliverable**: Settings page, quiz history, dark mode toggle, document reload

**Features**:
1. **Settings Page**:
   - Document folder picker (re-load if user changes folder)
   - Theme toggle (dark/light, default: dark)
   - Export results as CSV / PDF (with timestamp)
   - Clear all quiz history (with confirmation)
   - App version + about

2. **Quiz History**:
   - Sidebar or modal showing last 10 quizzes per subject
   - Click to view details (full Q&A review)

3. **Polish**:
   - Smooth page transitions (fade, slide)
   - Loading spinners (Tauri logo)
   - Error handling: show toast notifications for failures
   - Keyboard shortcuts: Enter = submit answer, Esc = back, R = retake

---

## EXECUTION CONSTRAINTS FOR DEVIN / ANTIGRAVITY

### Before Writing Code
1. **Confirm with User**:
   - Exact folder path where documents live (e.g., `~/Desktop/SPK_SPL1_Docs/`)
   - Expected document format (.json, .csv, .md with frontmatter?)
   - Does user already have parsed question files, or raw PDFs to parse?

2. **Create Sample Dataset**:
   - If user doesn't have questions yet, generate 5 mock questions per subject (realistic SPK content)
   - Use this for testing before loading real docs

### Coding Standards
- **TypeScript**: strict mode, no `any` types
- **React**: functional components + hooks only, no class components
- **Error Handling**: Try/catch all IPC calls, show user-facing error messages
- **Testing**: Write tests as you code (not after). Minimum coverage: 70%
- **Commit Frequency**: Commit after each phase completion

### Deliverable Checklist
- [ ] Phase 1: Tauri project builds, SQLite schema created, document loader works
- [ ] Phase 2: Quiz flow end-to-end (select subject → answer → see feedback)
- [ ] Phase 3: Results page + Dashboard charts render and update
- [ ] Phase 4: Settings, history, polish complete
- [ ] All tests passing, no console errors
- [ ] Tauri app builds to `.exe` (Windows) or `.dmg` (Mac) with <50MB size
- [ ] User can load documents from their folder without code changes

---

## FILES TO CREATE (in order)

### Tauri Project Structure
```
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
│  ├── pages/
│  │  ├── Home.tsx
│  │  ├── QuizDetail.tsx
│  │  ├── Results.tsx
│  │  ├── Dashboard.tsx
│  │  └── Settings.tsx
│  ├── components/
│  │  ├── QuestionCard.tsx
│  │  ├── AnswerSelector.tsx
│  │  ├── ExplanationPanel.tsx
│  │  ├── ResultsChart.tsx
│  │  └── SubjectCard.tsx
│  ├── stores/
│  │  ├── quizStore.ts (Zustand)
│  │  └── analyticsStore.ts (Zustand)
│  └── utils/
│     ├── ipc.ts (Tauri command wrappers)
│     └── formatting.ts (number, date formatting)
├── src/styles/
│  └── globals.css (Tailwind + custom dark theme)
├── vite.config.ts
├── tsconfig.json
├── package.json
└── README.md
```

### Key Files to Implement First
1. `src-tauri/src/db.rs` — SQLite schema + queries
2. `src-tauri/src/main.rs` — IPC command handlers
3. `src/stores/quizStore.ts` — Quiz state machine
4. `src/pages/QuizDetail.tsx` — Main quiz UX
5. `src/pages/Results.tsx` — Score display
6. `src/pages/Dashboard.tsx` — Analytics charts

---

## DOCUMENTATION TO GENERATE

Once build is complete, create:
1. **USER GUIDE**: How to load documents, take a quiz, view results
2. **ADMIN GUIDE**: How to add new questions, update explanations (edit DB directly or provide admin UI)
3. **TROUBLESHOOTING**: Common errors (document not found, DB corruption, Tauri IPC timeout)

---

## SUCCESS CRITERIA

✅ **App Launches**: Tauri window opens, Home page renders with 4 subject cards
✅ **Documents Load**: Click "Load Documents" in Settings, app reads folder, populates DB, shows "25 questions loaded for 1001"
✅ **Quiz Workflow**: Select subject → see Q1 → select option → feedback shows in <500ms → click "Next" → Q2 loads
✅ **Feedback**: Green/red badge, full explanation visible, next button locked until scroll
✅ **Results**: After 25 Qs, show score (e.g., "21/25 = 84%"), accuracy badge, time spent
✅ **Dashboard**: 4-subject bar chart updates after each quiz, trend line visible
✅ **Export**: Results export to CSV works
✅ **No Crashes**: App handles edge cases (empty folder, corrupted JSON, DB locks) gracefully
✅ **Premium Feel**: Dark theme, smooth animations, professional fonts, responsive on 1920x1080 & 1366x768

---

## NOTES FOR EMIN

**Why Tauri?**
- Security: Rust backend isolates file access, no untrusted code in browser context
- Size: ~15MB vs ~150MB Electron (Tauri uses system WebView)
- Performance: native Rust commands for DB queries
- Simplicity: IPC is just Rust functions → React calls

**Why React + Zustand?**
- React: you know it from e-cüzdan (similar component patterns)
- Zustand: lighter than Redux, similar to your Flask app's state model
- TypeScript: catches bugs at compile time

**SPK Scoring**:
- Raw score = correct answers (max 50)
- Standart Puan = Z-score normalized (optional, requires baseline mean/stdev)
- For now, just show raw score + accuracy %, can add Standart Puan later if you get test statistics

**Testing Documents**:
- Don't wait for perfect real questions; start with 5 mock Qs per subject
- Test schema, loader, quiz flow with mocks
- Swap in real Qs later without code changes

---

**Ready to Build**: Copy this prompt to Antigravity, add your folder path, and let Devin create the scaffolds. You verify each phase before moving to next.
