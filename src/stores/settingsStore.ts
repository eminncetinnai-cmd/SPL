import { create } from 'zustand';

interface SettingsState {
  theme: 'dark' | 'light';
  soundEnabled: boolean;
  autoScrollExplanation: boolean;
  defaultQuestionCount: 25;
  setTheme: (theme: 'dark' | 'light') => void;
  toggleTheme: () => void;
  setSoundEnabled: (enabled: boolean) => void;
  setAutoScrollExplanation: (enabled: boolean) => void;
}

const STORAGE_KEY = 'spk_spl1_settings_v2';

const initialSettings = (() => {
  try {
    // Clear old settings key if exists
    try { localStorage.removeItem('spk_spl1_settings'); } catch (e) {}

    const saved = localStorage.getItem(STORAGE_KEY);
    if (saved) return JSON.parse(saved);
  } catch (e) {}
  return {
    theme: 'light' as const,
    soundEnabled: true,
    autoScrollExplanation: true,
    defaultQuestionCount: 25 as const,
  };
})();

export const useSettingsStore = create<SettingsState>((set, get) => ({
  ...initialSettings,
  setTheme: (theme) => {
    set({ theme });
    try {
      localStorage.setItem(STORAGE_KEY, JSON.stringify({ ...get(), theme }));
      if (theme === 'dark') {
        document.documentElement.classList.add('dark');
      } else {
        document.documentElement.classList.remove('dark');
      }
    } catch (e) {}
  },
  toggleTheme: () => {
    const nextTheme = get().theme === 'dark' ? 'light' : 'dark';
    get().setTheme(nextTheme);
  },
  setSoundEnabled: (soundEnabled) => {
    set({ soundEnabled });
    try {
      localStorage.setItem(STORAGE_KEY, JSON.stringify({ ...get(), soundEnabled }));
    } catch (e) {}
  },
  setAutoScrollExplanation: (autoScrollExplanation) => {
    set({ autoScrollExplanation });
    try {
      localStorage.setItem(STORAGE_KEY, JSON.stringify({ ...get(), autoScrollExplanation }));
    } catch (e) {}
  },
}));
