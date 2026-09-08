// Advanced Turkish Speech Synthesis & Prosody Engine

export interface SpeechSentence {
  text: string;
  originalText: string;
  index: number;
}

// Convert numbers into spoken Turkish words for natural legal reading
export function numberToTurkishWords(numStr: string): string {
  const num = parseInt(numStr, 10);
  if (isNaN(num)) return numStr;
  if (num === 0) return 'sıfır';

  const units = ['', 'bir', 'iki', 'üç', 'dört', 'beş', 'altı', 'yedi', 'sekiz', 'dokuz'];
  const tens = ['', 'on', 'yirmi', 'otuz', 'kırk', 'elli', 'altmış', 'yetmiş', 'seksen', 'doksan'];

  if (num < 10) return units[num];
  if (num < 100) {
    const t = Math.floor(num / 10);
    const u = num % 10;
    return `${tens[t]} ${units[u]}`.trim();
  }
  if (num < 1000) {
    const h = Math.floor(num / 100);
    const rest = num % 100;
    const hStr = h === 1 ? 'yüz' : `${units[h]} yüz`;
    return rest > 0 ? `${hStr} ${numberToTurkishWords(rest.toString())}` : hStr;
  }
  if (num < 1000000) {
    const th = Math.floor(num / 1000);
    const rest = num % 1000;
    const thStr = th === 1 ? 'bin' : `${numberToTurkishWords(th.toString())} bin`;
    return rest > 0 ? `${thStr} ${numberToTurkishWords(rest.toString())}` : thStr;
  }
  if (num < 1000000000) {
    const m = Math.floor(num / 1000000);
    const rest = num % 1000000;
    const mStr = `${numberToTurkishWords(m.toString())} milyon`;
    return rest > 0 ? `${mStr} ${numberToTurkishWords(rest.toString())}` : mStr;
  }
  return numStr;
}

export function cleanTextForSpeech(text: string): string {
  if (!text) return '';

  let cleaned = text;

  // 1. Remove visual emojis, bullet icons, brackets and markdown
  cleaned = cleaned.replace(/[✔📌💡⚠️▸•★■□✓✔✦🔹🔸▶️🔊⚡\(\)\[\]\{\}]/g, ' ');

  // 2. Pronounce Exam Traps & Key Headings with Strong Vocal Emphasis
  cleaned = cleaned.replace(/SINAVDA SIKÇA ÇIKAR/gi, 'Dikkat, sınavda sıkça çıkan kritik nokta.');
  cleaned = cleaned.replace(/Sınav İpucu & Tuzak/gi, 'Önemli sınav ipucu ve çeldirici uyarısı.');
  cleaned = cleaned.replace(/Sınav Tuzağı/gi, 'Dikkat, sınav tuzağı.');
  cleaned = cleaned.replace(/Kritik Süre/gi, 'Kritik yasal süre.');
  cleaned = cleaned.replace(/Önemli Maddeler/gi, 'Önemli maddeler ve esaslar.');
  cleaned = cleaned.replace(/Temel Mantık/gi, 'Temel mantık ve kural.');

  // 3. Convert formatted percentages (%20 -> yüzde yirmi)
  cleaned = cleaned.replace(/%\s*(\d+)/g, (_, n) => `yüzde ${numberToTurkishWords(n)}`);
  cleaned = cleaned.replace(/(\d+)\s*%/g, (_, n) => `yüzde ${numberToTurkishWords(n)}`);

  // 4. Convert monetary amounts (1.000.000 TL -> bir milyon Türk Lirası)
  cleaned = cleaned.replace(/(\d{1,3}(?:\.\d{3})+)\s*TL/gi, (_, amount) => {
    const rawNum = amount.replace(/\./g, '');
    return `${numberToTurkishWords(rawNum)} Türk Lirası`;
  });

  // 5. Expand legal and financial acronyms to fluent Turkish prose
  const abbreviations: [RegExp, string][] = [
    [/\b6362\s*sayılı\b/gi, 'Altı bin üç yüz altmış iki sayılı'],
    [/\b6102\s*sayılı\b/gi, 'Altı bin yüz iki sayılı'],
    [/\bSPKn\b/gi, 'Sermaye Piyasası Kanunu'],
    [/\bSPK'nın\b/gi, 'Sermaye Piyasası Kurulunun'],
    [/\bSPK'ya\b/gi, 'Sermaye Piyasası Kuruluna'],
    [/\bSPK'da\b/gi, 'Sermaye Piyasası Kurulunda'],
    [/\bSPK'dan\b/gi, 'Sermaye Piyasası Kurulundan'],
    [/\bSPK\b/gi, 'Sermaye Piyasası Kurulu'],
    [/\bMKK'nın\b/gi, 'Merkezi Kayıt Kuruluşunun'],
    [/\bMKK'ya\b/gi, 'Merkezi Kayıt Kuruluşuna'],
    [/\bMKK'da\b/gi, 'Merkezi Kayıt Kuruluşunda'],
    [/\bMKK\b/gi, 'Merkezi Kayıt Kuruluşu'],
    [/\bTSPB'nin\b/gi, 'Türkiye Sermaye Piyasaları Birliğinin'],
    [/\bTSPB'ye\b/gi, 'Türkiye Sermaye Piyasaları Birliğine'],
    [/\bTSPB\b/gi, 'Türkiye Sermaye Piyasaları Birliği'],
    [/\bTakasbank'ın\b/gi, 'Takasbankın'],
    [/\bTakasbank'a\b/gi, 'Takasbanka'],
    [/\bTakasbank\b/gi, 'Takasbank'],
    [/\bMKT\b/gi, 'Merkezi Karşı Taraf'],
    [/\bYTM'nin\b/gi, 'Yatırımcı Tazmin Merkezinin'],
    [/\bYTM'ye\b/gi, 'Yatırımcı Tazmin Merkezine'],
    [/\bYTM\b/gi, 'Yatırımcı Tazmin Merkezi'],
    [/\bBIST\b/gi, 'Borsa İstanbul'],
    [/\bBİST\b/gi, 'Borsa İstanbul'],
    [/\bVİOP\b/gi, 'Vadeli İşlem ve Opsiyon Piyasası'],
    [/\bKAP'a\b/gi, 'Kamuyu Aydınlatma Platformuna'],
    [/\bKAP'ta\b/gi, 'Kamuyu Aydınlatma Platformunda'],
    [/\bKAP\b/gi, 'Kamuyu Aydınlatma Platformu'],
    [/\bMASAK\b/gi, 'Mali Suçları Araştırma Kurulu'],
    [/\bT\+2\b/gi, 'Te artı iki gün'],
    [/\bT\+1\b/gi, 'Te artı bir gün'],
    [/\bT\+0\b/gi, 'Aynı gün Te sıfır'],
    [/\bDvP\b/gi, 'Ödeme Karşılığı Teslimat prensibi'],
    [/\bTL'dir\b/gi, 'Türk Lirasıdır'],
    [/\bTL'nin\b/gi, 'Türk Lirasının'],
    [/\bTL'ye\b/gi, 'Türk Lirasına'],
    [/\bTL\b/gi, 'Türk Lirası'],
    [/\bA\.Ş\.\b/gi, 'Anonim Şirketi'],
    [/\bAŞ\b/gi, 'Anonim Şirketi'],
    [/\bvb\.\b/gi, 've benzeri'],
    [/\bvd\.\b/gi, 've devamı maddeler'],
    [/\börn\.\b/gi, 'örneğin,'],
    [/\bvs\.\b/gi, 've saire'],
    [/≠/g, ', kesinlikle eşit değildir,'],
    [/↔/g, ' ile karşılaştırıldığında '],
    [/→/g, ' ardından '],
    [/1001/g, 'Bin bir'],
    [/1003/g, 'Bin üç'],
    [/1005/g, 'Bin beş'],
    [/1012/g, 'Bin on iki'],
  ];

  cleaned = cleaned.replace(/\b(?:md|m)\.\s*(\d+)/gi, (_, m: string) => `${numberToTurkishWords(m)}. madde`);
  cleaned = cleaned.replace(/\bf\.\s*(\d+)/gi, (_, f: string) => `${numberToTurkishWords(f)}. fıkra`);
  cleaned = cleaned.replace(/\bNo\.\s*(\d+)/gi, (_, n: string) => `numara ${numberToTurkishWords(n)}`);

  for (const [regex, replacement] of abbreviations) {
    cleaned = cleaned.replace(regex, replacement);
  }

  // 6. Natural Turkish Prosody & Breath Comma Injection (Tonlama ve Nefes Durakları)
  cleaned = cleaned.replace(/\b(Bu kapsamda|Bu doğrultuda|Dolayısıyla|Özetle|Buna göre|Sonuç olarak|Önemle belirtmek gerekir ki)\b/gi, '$1,');
  cleaned = cleaned.replace(/\b(ancak|fakat|oysa|oysaki|halbuki|lakin)\b/gi, ', $1');

  // 7. Normalize multiple spaces and punctuation
  cleaned = cleaned.replace(/,{2,}/g, ',');
  cleaned = cleaned.replace(/\s+/g, ' ').trim();

  // Ensure sentence ends with period for natural pitch drop
  if (!/[.!?]$/.test(cleaned)) {
    cleaned += '.';
  }

  return cleaned;
}

export function cleanVisualText(text: string): string {
  if (!text) return '';
  let cleaned = text;
  cleaned = cleaned.replace(/\[sec_\w+\]/g, '');
  cleaned = cleaned.replace(/^[•✔📌💡⚠️▸★■□✓✔✦🔹🔸▶️🔊⚡\s-]+/, '');
  cleaned = cleaned.replace(/\s+/g, ' ').trim();
  return cleaned;
}

export function splitIntoSentences(paragraphs: string[]): SpeechSentence[] {
  const sentences: SpeechSentence[] = [];

  paragraphs.forEach((p) => {
    const rawClean = cleanVisualText(p);
    if (!rawClean) return;

    // Split paragraph by sentence ending punctuation
    const rawSentences = rawClean.match(/[^.!?]+[.!?]+|\s*[^.!?]+$/g) || [rawClean];

    rawSentences.forEach((s) => {
      const trimmed = s.trim();
      if (trimmed.length > 3) {
        const speechVersion = cleanTextForSpeech(trimmed);
        sentences.push({
          text: speechVersion,
          originalText: trimmed,
          index: sentences.length,
        });
      }
    });
  });

  return sentences;
}

export class SpeechEngine {
  private synth: SpeechSynthesis | null = null;
  private currentUtterance: SpeechSynthesisUtterance | null = null;
  private selectedVoice: SpeechSynthesisVoice | null = null;
  private availableVoices: SpeechSynthesisVoice[] = [];

  constructor() {
    if (typeof window !== 'undefined' && 'speechSynthesis' in window) {
      this.synth = window.speechSynthesis;
      this.initVoices();
    }
  }

  public initVoices() {
    if (!this.synth) return;

    const loadVoices = () => {
      const allVoices = this.synth?.getVoices() || [];
      // Filter for Turkish voices or prioritize them
      const trVoices = allVoices.filter(
        (v) => v.lang.startsWith('tr') || v.lang.includes('TR') || v.name.toLowerCase().includes('turkish')
      );

      this.availableVoices = trVoices.length > 0 ? trVoices : allVoices;

      // Smart Voice Selection: Prioritize Neural / Natural / Google voices
      const premiumVoice = trVoices.find(
        (v) =>
          v.name.toLowerCase().includes('natural') ||
          v.name.toLowerCase().includes('online') ||
          v.name.toLowerCase().includes('neural') ||
          v.name.toLowerCase().includes('google') ||
          v.name.toLowerCase().includes('tolga') ||
          v.name.toLowerCase().includes('emel') ||
          v.name.toLowerCase().includes('yelda')
      );

      if (premiumVoice) {
        this.selectedVoice = premiumVoice;
      } else if (trVoices.length > 0) {
        this.selectedVoice = trVoices[0];
      }
    };

    loadVoices();
    if (this.synth.onvoiceschanged !== undefined) {
      this.synth.onvoiceschanged = loadVoices;
    }
  }

  getVoices(): SpeechSynthesisVoice[] {
    if (this.availableVoices.length === 0 && this.synth) {
      this.initVoices();
    }
    return this.availableVoices;
  }

  setVoice(voiceName: string) {
    const match = this.getVoices().find((v) => v.name === voiceName);
    if (match) {
      this.selectedVoice = match;
    }
  }

  getCurrentVoice(): SpeechSynthesisVoice | null {
    return this.selectedVoice;
  }

  speakSentence(
    text: string,
    rate: number = 0.95, // Default 0.95 for clear, articulate Turkish
    onEnd?: () => void,
    onError?: () => void
  ) {
    if (!this.synth) return;

    this.stop();

    const utterance = new SpeechSynthesisUtterance(text);
    utterance.lang = 'tr-TR';
    if (this.selectedVoice) {
      utterance.voice = this.selectedVoice;
    }
    
    // Natural prosody pitch and rate
    utterance.rate = Math.max(0.6, Math.min(1.8, rate));
    utterance.pitch = 1.02; // Slight natural pitch boost for clarity

    utterance.onend = () => {
      if (onEnd) onEnd();
    };

    utterance.onerror = (e) => {
      if (e.error !== 'canceled' && onError) {
        onError();
      }
    };

    this.currentUtterance = utterance;
    this.synth.speak(utterance);
  }

  pause() {
    if (this.synth && this.synth.speaking) {
      this.synth.pause();
    }
  }

  resume() {
    if (this.synth && this.synth.paused) {
      this.synth.resume();
    }
  }

  stop() {
    if (this.synth) {
      this.synth.cancel();
    }
    this.currentUtterance = null;
  }
}

export const speechEngine = new SpeechEngine();
