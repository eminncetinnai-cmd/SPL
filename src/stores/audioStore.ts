import { create } from 'zustand';
import { speechEngine, splitIntoSentences, SpeechSentence } from '../utils/speechEngine';

interface PlaySectionOptions {
  moduleId: string;
  sectionId: string;
  title: string;
  paragraphs: string[];
  onComplete?: () => void;
}

interface AudioState {
  isPlaying: boolean;
  isPaused: boolean;
  title: string;
  moduleId: string | null;
  sectionId: string | null;
  sentences: SpeechSentence[];
  currentSentenceIndex: number;
  playbackRate: number;
  autoAdvance: boolean;
  selectedVoiceName: string | null;
  availableVoices: SpeechSynthesisVoice[];
  onCompleteCallback?: () => void;

  // Actions
  playSection: (options: PlaySectionOptions) => void;
  togglePlayPause: () => void;
  pause: () => void;
  resume: () => void;
  stop: () => void;
  nextSentence: () => void;
  prevSentence: () => void;
  jumpToSentence: (index: number) => void;
  setPlaybackRate: (rate: number) => void;
  setAutoAdvance: (enabled: boolean) => void;
  setVoice: (voiceName: string) => void;
  loadVoices: () => void;
}

export const useAudioStore = create<AudioState>((set, get) => ({
  isPlaying: false,
  isPaused: false,
  title: '',
  moduleId: null,
  sectionId: null,
  sentences: [],
  currentSentenceIndex: 0,
  playbackRate: 0.95, // Default natural articulate pace
  autoAdvance: true,
  selectedVoiceName: null,
  availableVoices: [],
  onCompleteCallback: undefined,

  loadVoices: () => {
    const voices = speechEngine.getVoices();
    const currentVoice = speechEngine.getCurrentVoice();
    set({
      availableVoices: voices,
      selectedVoiceName: currentVoice ? currentVoice.name : voices[0]?.name || null,
    });
  },

  setVoice: (voiceName: string) => {
    speechEngine.setVoice(voiceName);
    set({ selectedVoiceName: voiceName });
    const { isPlaying, currentSentenceIndex } = get();
    if (isPlaying) {
      get().jumpToSentence(currentSentenceIndex);
    }
  },

  playSection: ({ moduleId, sectionId, title, paragraphs, onComplete }) => {
    speechEngine.stop();

    const sentences = splitIntoSentences(paragraphs);
    if (sentences.length === 0) return;

    // Refresh voices if empty
    if (get().availableVoices.length === 0) {
      get().loadVoices();
    }

    set({
      isPlaying: true,
      isPaused: false,
      title,
      moduleId,
      sectionId,
      sentences,
      currentSentenceIndex: 0,
      onCompleteCallback: onComplete,
    });

    const playIndex = (index: number) => {
      const state = get();
      if (!state.isPlaying || index >= state.sentences.length) {
        set({ isPlaying: false, isPaused: false });
        if (state.onCompleteCallback && state.autoAdvance) {
          state.onCompleteCallback();
        }
        return;
      }

      set({ currentSentenceIndex: index });
      const currentSentence = state.sentences[index];

      speechEngine.speakSentence(
        currentSentence.text,
        state.playbackRate,
        () => {
          playIndex(index + 1);
        },
        () => {
          set({ isPlaying: false, isPaused: false });
        }
      );
    };

    playIndex(0);
  },

  togglePlayPause: () => {
    const { isPlaying, isPaused, currentSentenceIndex, sentences, playbackRate } = get();
    if (!isPlaying && sentences.length > 0) {
      set({ isPlaying: true, isPaused: false });
      const playIndex = (index: number) => {
        const state = get();
        if (!state.isPlaying || index >= state.sentences.length) {
          set({ isPlaying: false, isPaused: false });
          if (state.onCompleteCallback && state.autoAdvance) {
            state.onCompleteCallback();
          }
          return;
        }

        set({ currentSentenceIndex: index });
        const currentSentence = state.sentences[index];

        speechEngine.speakSentence(
          currentSentence.text,
          state.playbackRate,
          () => playIndex(index + 1),
          () => set({ isPlaying: false, isPaused: false })
        );
      };
      playIndex(currentSentenceIndex);
    } else if (isPlaying && !isPaused) {
      speechEngine.pause();
      set({ isPaused: true });
    } else if (isPlaying && isPaused) {
      speechEngine.resume();
      set({ isPaused: false });
    }
  },

  pause: () => {
    speechEngine.pause();
    set({ isPaused: true });
  },

  resume: () => {
    speechEngine.resume();
    set({ isPaused: false });
  },

  stop: () => {
    speechEngine.stop();
    set({
      isPlaying: false,
      isPaused: false,
      title: '',
      moduleId: null,
      sectionId: null,
      sentences: [],
      currentSentenceIndex: 0,
    });
  },

  nextSentence: () => {
    const { currentSentenceIndex, sentences } = get();
    if (currentSentenceIndex + 1 < sentences.length) {
      get().jumpToSentence(currentSentenceIndex + 1);
    }
  },

  prevSentence: () => {
    const { currentSentenceIndex } = get();
    if (currentSentenceIndex > 0) {
      get().jumpToSentence(currentSentenceIndex - 1);
    }
  },

  jumpToSentence: (index: number) => {
    const { sentences } = get();
    if (index < 0 || index >= sentences.length) return;

    speechEngine.stop();
    set({ isPlaying: true, isPaused: false, currentSentenceIndex: index });

    const playIndex = (idx: number) => {
      const state = get();
      if (!state.isPlaying || idx >= state.sentences.length) {
        set({ isPlaying: false, isPaused: false });
        if (state.onCompleteCallback && state.autoAdvance) {
          state.onCompleteCallback();
        }
        return;
      }

      set({ currentSentenceIndex: idx });
      const currentSentence = state.sentences[idx];

      speechEngine.speakSentence(
        currentSentence.text,
        state.playbackRate,
        () => playIndex(idx + 1),
        () => set({ isPlaying: false, isPaused: false })
      );
    };

    playIndex(index);
  },

  setPlaybackRate: (rate: number) => {
    set({ playbackRate: rate });
    const { isPlaying, currentSentenceIndex } = get();
    if (isPlaying) {
      get().jumpToSentence(currentSentenceIndex);
    }
  },

  setAutoAdvance: (enabled: boolean) => {
    set({ autoAdvance: enabled });
  },
}));
