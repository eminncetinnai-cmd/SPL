export type ModuleId = '1001' | '1003' | '1005' | '1012';

export interface Option {
  key: 'A' | 'B' | 'C' | 'D' | 'E';
  text: string;
}

export type CognitiveSkill = 'KB1_Kavramsal' | 'KB2_Muhakeme' | 'KB3_Vaka';

export interface Question {
  id: string;
  module_id: ModuleId;
  number: number;
  source: 'master' | 'cikmis' | 'ogretici' | 'konu';
  topic: string;
  chapter: string;
  text: string;
  options: Option[];
  correct_answer: 'A' | 'B' | 'C' | 'D' | 'E';
  explanation: string;
  trap?: string;
  difficulty: 'easy' | 'medium' | 'hard';
  cognitive_skill?: CognitiveSkill;
  tags: string[];
}

export interface ModuleInfo {
  id: ModuleId;
  code: string;
  name: string;
  short_name: string;
  category: string;
  description: string;
  color: string;
  borderColor: string;
  accentColor: string;
  icon: string;
  total_exam_questions: number;
  passing_score: number;
  target_score: number;
}

export interface TopicSection {
  id: string;
  title: string;
  content: string[];
  concrete_examples?: string[];
  key_takeaways: string[];
  exam_traps: string[];
  exam_tips?: string[];
  tables?: Array<{
    headers: string[];
    rows: string[][];
  }>;
}

export interface TopicModuleNotes {
  module_id: ModuleId;
  title: string;
  total_sections: number;
  sections: TopicSection[];
}

export interface Flashcard {
  id: string;
  module_id: ModuleId;
  number: number;
  title: string;
  chapter: string;
  definition: string;
  example: string;
  trap: string;
}

export interface UserAnswer {
  question_id: string;
  module_id: ModuleId;
  selected_option: 'A' | 'B' | 'C' | 'D' | 'E' | null;
  correct_option: 'A' | 'B' | 'C' | 'D' | 'E';
  is_correct: boolean;
  time_spent_seconds: number;
  marked_for_review: boolean;
}

export type QuizMode = 'practice' | 'simulation' | 'mistakes' | 'bookmarks' | 'custom';

export interface QuizSession {
  id: string;
  mode: QuizMode;
  module_id?: ModuleId | 'all';
  title: string;
  started_at: string;
  ended_at?: string;
  duration_seconds: number;
  time_limit_seconds?: number;
  questions: Question[];
  current_index: number;
  user_answers: Record<string, UserAnswer>;
  is_completed: boolean;
  score?: number;
  accuracy_pct?: number;
  correct_count?: number;
  wrong_count?: number;
  empty_count?: number;
  module_breakdown?: Record<ModuleId, {
    total: number;
    correct: number;
    wrong: number;
    empty: number;
    score: number;
    passed: boolean;
  }>;
  overall_passed?: boolean;
}

export interface PastQuizSummary {
  id: string;
  mode: QuizMode;
  module_id: string;
  title: string;
  date: string;
  total_questions: number;
  correct_count: number;
  wrong_count: number;
  empty_count: number;
  score: number;
  accuracy_pct: number;
  duration_seconds: number;
  overall_passed: boolean;
}

export interface MistakeEntry {
  question: Question;
  wrong_count: number;
  last_wrong_date: string;
  last_selected_option: string;
  correct_streak?: number;
  resolved: boolean;
}
