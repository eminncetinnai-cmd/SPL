import React from 'react';
import { 
  Settings, 
  Moon, 
  Sun, 
  Volume2, 
  VolumeX, 
  Download, 
  Trash2, 
  Info, 
  ShieldCheck, 
  Database,
  Award,
  BookOpen,
  Smartphone,
  CheckCircle2,
  Share2
} from 'lucide-react';
import { useSettingsStore } from '../stores/settingsStore';
import { useProgressStore } from '../stores/progressStore';
import { exportQuizHistoryToCSV, exportMistakesToCSV } from '../utils/csvExport';

export const SettingsPage: React.FC = () => {
  const { 
    theme, 
    setTheme, 
    soundEnabled, 
    setSoundEnabled, 
    autoScrollExplanation, 
    setAutoScrollExplanation 
  } = useSettingsStore();

  const { 
    history, 
    mistakes, 
    resetAll,
    seenQuestionIds,
    avoidQuestionRepetition,
    setAvoidRepetition,
    resetSeenQuestions
  } = useProgressStore();
  const mistakeList = Object.values(mistakes);

  const handleExportJSON = () => {
    const data = {
      timestamp: new Date().toISOString(),
      history,
      mistakes,
    };
    const blob = new Blob([JSON.stringify(data, null, 2)], { type: 'application/json' });
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = `SPK_SPL_Backup_${new Date().toISOString().slice(0, 10)}.json`;
    a.click();
  };

  const handleReset = () => {
    if (confirm('Tüm sınav geçmişiniz, istatistikleriniz ve yanlışlar defteriniz sıfırlanacaktır. Emin misiniz?')) {
      resetAll();
      alert('Tüm veriler başarıyla sıfırlandı.');
    }
  };

  return (
    <div className="max-w-4xl mx-auto space-y-8 animate-fade-in pb-16">
      {/* Header */}
      <div className="border-b border-slate-200 dark:border-fintech-border/70 pb-5">
        <span className="text-xs font-mono text-teal-600 dark:text-teal-400 font-bold uppercase tracking-wider block">
          Tercihler & Veri Yönetimi
        </span>
        <h1 className="text-xl sm:text-2xl font-black text-slate-900 dark:text-white tracking-tight">
          Uygulama Ayarları & Veri Depolama
        </h1>
      </div>

      <div className="space-y-6">
        {/* Appearance Settings */}
        <div className="bg-white dark:bg-fintech-surface rounded-2xl border border-slate-200 dark:border-fintech-border p-6 space-y-4 shadow-sm">
          <h3 className="font-bold text-sm text-slate-900 dark:text-white tracking-wide flex items-center gap-2">
            <Sun className="w-4 h-4 text-amber-500 dark:text-amber-400" />
            <span>Görünüm & Tema</span>
          </h3>

          <div className="flex items-center justify-between py-2 border-t border-slate-200 dark:border-fintech-border/60">
            <div>
              <span className="font-medium text-xs sm:text-sm text-slate-900 dark:text-slate-200 block">Tema Seçimi</span>
              <span className="text-xs text-slate-500 dark:text-slate-400">Aydınlık ve ferah okuma modu veya Bloomberg / Fintech Dark UI</span>
            </div>
            <div className="flex items-center gap-2 bg-slate-100 dark:bg-fintech-card p-1 rounded-xl border border-slate-200 dark:border-fintech-border">
              <button
                onClick={() => setTheme('light')}
                className={`px-3 py-1.5 rounded-lg text-xs font-bold transition-all ${
                  theme === 'light' ? 'bg-amber-400 text-slate-950 shadow-sm' : 'text-slate-600 hover:text-slate-900 dark:text-slate-400 dark:hover:text-white'
                }`}
              >
                Aydınlık (Light)
              </button>
              <button
                onClick={() => setTheme('dark')}
                className={`px-3 py-1.5 rounded-lg text-xs font-bold transition-all ${
                  theme === 'dark' ? 'bg-teal-500 text-slate-950 shadow-sm' : 'text-slate-600 hover:text-slate-900 dark:text-slate-400 dark:hover:text-white'
                }`}
              >
                Koyu Tema (Dark)
              </button>
            </div>
          </div>
        </div>

        {/* Quiz Preferences */}
        <div className="bg-white dark:bg-fintech-surface rounded-2xl border border-slate-200 dark:border-fintech-border p-6 space-y-4 shadow-sm">
          <h3 className="font-bold text-sm text-slate-900 dark:text-white tracking-wide flex items-center gap-2">
            <Volume2 className="w-4 h-4 text-teal-600 dark:text-teal-400" />
            <span>Sınav & Ses Tercihleri</span>
          </h3>

          <div className="divide-y divide-slate-200 dark:divide-fintech-border/60">
            <div className="flex items-center justify-between py-3">
              <div>
                <span className="font-medium text-xs sm:text-sm text-slate-900 dark:text-slate-200 block">Ses Efektleri</span>
                <span className="text-xs text-slate-500 dark:text-slate-400">Doğru/yanlış cevaplarda ve sınav bitiminde ses çal</span>
              </div>
              <button
                onClick={() => setSoundEnabled(!soundEnabled)}
                className={`w-12 h-6 rounded-full transition-colors relative p-0.5 ${
                  soundEnabled ? 'bg-teal-500' : 'bg-slate-300 dark:bg-slate-700'
                }`}
              >
                <div
                  className={`w-5 h-5 rounded-full bg-white transition-transform ${
                    soundEnabled ? 'translate-x-6' : 'translate-x-0'
                  }`}
                />
              </button>
            </div>

            <div className="flex items-center justify-between py-3">
              <div>
                <span className="font-medium text-xs sm:text-sm text-slate-900 dark:text-slate-200 block">
                  Açıklama İnceleme Kontrolü
                </span>
                <span className="text-xs text-slate-500 dark:text-slate-400">
                  Pratik modda sonraki soruya geçmeden önce çözüm açıklamasının okunmasını teşvik et
                </span>
              </div>
              <button
                onClick={() => setAutoScrollExplanation(!autoScrollExplanation)}
                className={`w-12 h-6 rounded-full transition-colors relative p-0.5 ${
                  autoScrollExplanation ? 'bg-teal-500' : 'bg-slate-300 dark:bg-slate-700'
                }`}
              >
                <div
                  className={`w-5 h-5 rounded-full bg-white transition-transform ${
                    autoScrollExplanation ? 'translate-x-6' : 'translate-x-0'
                  }`}
                />
              </button>
            </div>

            {/* Anti-Repeat Smart Pool Setting */}
            <div className="flex items-center justify-between py-3">
              <div>
                <span className="font-medium text-xs sm:text-sm text-slate-900 dark:text-slate-200 block">
                  🛡️ Tekrarsız Soru Havuz Rotasyonu
                </span>
                <span className="text-xs text-slate-500 dark:text-slate-400">
                  Sınav ve denemelerde havuzdaki tüm sorular tükenene kadar daha önce çözdüğünüz sorular tekrar çıkmaz
                </span>
              </div>
              <button
                onClick={() => setAvoidRepetition(!avoidQuestionRepetition)}
                className={`w-12 h-6 rounded-full transition-colors relative p-0.5 ${
                  avoidQuestionRepetition ? 'bg-teal-500' : 'bg-slate-300 dark:bg-slate-700'
                }`}
              >
                <div
                  className={`w-5 h-5 rounded-full bg-white transition-transform ${
                    avoidQuestionRepetition ? 'translate-x-6' : 'translate-x-0'
                  }`}
                />
              </button>
            </div>
          </div>
        </div>

        {/* Data & Backup Management */}
        <div className="bg-white dark:bg-fintech-surface rounded-2xl border border-slate-200 dark:border-fintech-border p-6 space-y-4 shadow-sm">
          <h3 className="font-bold text-sm text-slate-900 dark:text-white tracking-wide flex items-center gap-2">
            <Database className="w-4 h-4 text-cyan-600 dark:text-cyan-400" />
            <span>Veri Dışa Aktarma & Yedekleme</span>
          </h3>

          <div className="grid grid-cols-1 sm:grid-cols-3 gap-3 pt-1">
            <button
              onClick={() => exportQuizHistoryToCSV(history)}
              className="p-4 rounded-xl bg-slate-50 hover:bg-slate-100 dark:bg-fintech-card dark:hover:bg-fintech-cardHover border border-slate-200 dark:border-fintech-border text-left space-y-1 transition-all shadow-sm"
            >
              <div className="flex items-center gap-2 text-teal-600 dark:text-teal-400 font-bold text-xs">
                <Download className="w-4 h-4" />
                <span>Sınav Karneleri (CSV)</span>
              </div>
              <p className="text-[11px] text-slate-500 dark:text-slate-400">
                Tüm sınav puanlarını ve süreleri Excel uyumlu CSV olarak indirin.
              </p>
            </button>

            <button
              onClick={() => exportMistakesToCSV(mistakeList)}
              className="p-4 rounded-xl bg-slate-50 hover:bg-slate-100 dark:bg-fintech-card dark:hover:bg-fintech-cardHover border border-slate-200 dark:border-fintech-border text-left space-y-1 transition-all shadow-sm"
            >
              <div className="flex items-center gap-2 text-rose-600 dark:text-rose-400 font-bold text-xs">
                <Download className="w-4 h-4" />
                <span>Yanlış Sorular (CSV)</span>
              </div>
              <p className="text-[11px] text-slate-500 dark:text-slate-400">
                Hatalı yapılan tüm soruları ve tuzak notlarını CSV olarak dışa aktarın.
              </p>
            </button>

            <button
              onClick={handleExportJSON}
              className="p-4 rounded-xl bg-slate-50 hover:bg-slate-100 dark:bg-fintech-card dark:hover:bg-fintech-cardHover border border-slate-200 dark:border-fintech-border text-left space-y-1 transition-all shadow-sm"
            >
              <div className="flex items-center gap-2 text-amber-600 dark:text-amber-400 font-bold text-xs">
                <Database className="w-4 h-4" />
                <span>Tam Veri Yedeği (JSON)</span>
              </div>
              <p className="text-[11px] text-slate-500 dark:text-slate-400">
                İlerlemenizi JSON formatında cihazınıza yedekleyin.
              </p>
            </button>
          </div>

          <div className="pt-3 border-t border-slate-200 dark:border-fintech-border/60 flex flex-col sm:flex-row sm:items-center justify-between gap-3">
            <div>
              <span className="text-xs font-bold text-teal-600 dark:text-teal-400 block">Soru Rotasyon Havuzunu Sıfırla</span>
              <span className="text-[11px] text-slate-500 dark:text-slate-400">
                Sınav geçmişinizi silmeden, sadece çözülmüş soru işaretlerini temizler ({seenQuestionIds.length} soru çözülmüş). Tüm 935 soru tekrar yeni soru olarak sınavlara girer.
              </span>
            </div>
            <button
              onClick={() => {
                if (confirm('Çözülmüş soru havuzu sıfırlanacak ve tüm sorular tekrar ilk kez çıkıyormuş gibi döngüye girecek. Sınav geçmişiniz silinmez. Onaylıyor musunuz?')) {
                  resetSeenQuestions('all');
                  alert('Soru rotasyon havuzu başarıyla sıfırlandı. 935 soru taze olarak havuza döndü.');
                }
              }}
              className="px-4 py-2 rounded-xl bg-teal-500/10 hover:bg-teal-500/20 text-teal-700 dark:text-teal-300 border border-teal-500/30 text-xs font-bold transition-all shrink-0 self-start sm:self-auto"
            >
              Havuz Döngüsünü Sıfırla
            </button>
          </div>

          <div className="pt-3 border-t border-slate-200 dark:border-fintech-border/60 flex flex-col sm:flex-row sm:items-center justify-between gap-3">
            <div>
              <span className="text-xs font-bold text-rose-500 dark:text-rose-400 block">Tüm Verileri Sıfırla</span>
              <span className="text-[11px] text-slate-500">
                Sınav geçmişinizi, çözülmüş soru istatistiklerini ve hatalı soru defterinizi tamamen siler.
              </span>
            </div>
            <button
              onClick={handleReset}
              className="px-4 py-2 rounded-xl bg-rose-500/10 hover:bg-rose-500/20 text-rose-600 dark:text-rose-400 border border-rose-500/30 text-xs font-bold transition-all shrink-0 self-start sm:self-auto"
            >
              Fabrika Ayarlarına Dön
            </button>
          </div>
        </div>

        {/* iPhone / iPad PWA Offline Guide Card */}
        <div className="bg-gradient-to-br from-teal-500/10 via-slate-50 to-white dark:from-teal-500/10 dark:via-fintech-surface dark:to-slate-900 rounded-2xl border border-teal-300 dark:border-teal-500/30 p-5 sm:p-6 space-y-4 shadow-sm">
          <div className="flex items-center justify-between border-b border-teal-200 dark:border-teal-500/20 pb-3">
            <div className="flex items-center gap-2.5">
              <div className="p-2 rounded-xl bg-teal-500/15 text-teal-700 dark:text-teal-400">
                <Smartphone className="w-5 h-5" />
              </div>
              <div>
                <h3 className="text-sm font-black text-slate-900 dark:text-white">
                  iPhone & iPad Çevrimdışı (Offline) Kurulum Rehberi
                </h3>
                <p className="text-[11px] text-slate-500 dark:text-slate-400">
                  İnternetsiz metroda, uçakta ve yolda test çözmek için ana ekrana ekleyin.
                </p>
              </div>
            </div>
            <span className="hidden sm:inline-flex items-center gap-1 px-2.5 py-1 rounded-full bg-emerald-50 dark:bg-emerald-500/15 text-emerald-800 dark:text-emerald-300 border border-emerald-200 dark:border-emerald-500/30 text-[10px] font-mono font-bold">
              <CheckCircle2 className="w-3.5 h-3.5" />
              <span>iOS Uyumlu</span>
            </span>
          </div>

          <div className="grid grid-cols-1 sm:grid-cols-3 gap-3 text-xs">
            <div className="p-3.5 rounded-xl bg-white dark:bg-fintech-card border border-slate-200 dark:border-fintech-border space-y-1.5 shadow-xs">
              <span className="w-5 h-5 rounded-full bg-teal-600 text-white font-mono font-bold text-[11px] flex items-center justify-center">1</span>
              <h4 className="font-bold text-slate-900 dark:text-white">Safari'de Açın</h4>
              <p className="text-[11px] text-slate-600 dark:text-slate-400 leading-relaxed">
                Platformu iPhone'unuzun yerleşik <strong>Safari</strong> tarayıcısında açın.
              </p>
            </div>

            <div className="p-3.5 rounded-xl bg-white dark:bg-fintech-card border border-slate-200 dark:border-fintech-border space-y-1.5 shadow-xs">
              <span className="w-5 h-5 rounded-full bg-teal-600 text-white font-mono font-bold text-[11px] flex items-center justify-center">2</span>
              <h4 className="font-bold text-slate-900 dark:text-white">Paylaş'a Dokunun</h4>
              <p className="text-[11px] text-slate-600 dark:text-slate-400 leading-relaxed">
                Alttaki <strong>Paylaş (kare ve yukarı ok ⎋)</strong> butonuna tıklayın.
              </p>
            </div>

            <div className="p-3.5 rounded-xl bg-white dark:bg-fintech-card border border-slate-200 dark:border-fintech-border space-y-1.5 shadow-xs">
              <span className="w-5 h-5 rounded-full bg-teal-600 text-white font-mono font-bold text-[11px] flex items-center justify-center">3</span>
              <h4 className="font-bold text-slate-900 dark:text-white">Ana Ekrana Ekle</h4>
              <p className="text-[11px] text-slate-600 dark:text-slate-400 leading-relaxed">
                Menüden <strong>"Ana Ekrana Ekle"</strong>yi seçin ve <strong>"Ekle"</strong>ye basın.
              </p>
            </div>
          </div>

          <div className="text-[11px] font-mono text-teal-800 dark:text-teal-300 bg-teal-50 dark:bg-teal-950/30 p-2.5 rounded-xl border border-teal-200 dark:border-teal-500/20 flex items-center gap-2">
            <span>💡 İpucu:</span>
            <span>Uygulama olarak eklendiğinde adres çubuğu kalkar, tam ekran ve tamamen internetsiz çalışır.</span>
          </div>
        </div>

        {/* About & Copyright */}
        <div className="bg-slate-50 dark:bg-slate-900/60 rounded-2xl border border-slate-200 dark:border-fintech-border p-6 space-y-4 text-xs text-slate-600 dark:text-slate-400 leading-relaxed shadow-sm">
          <div className="flex items-center justify-between border-b border-slate-200 dark:border-slate-800 pb-3">
            <div className="flex items-center gap-2 text-slate-900 dark:text-slate-100 font-black text-sm">
              <Info className="w-4 h-4 text-teal-600 dark:text-teal-400" />
              <span>SPK SPL Düzey 1 Sınav Platformu Hakkında</span>
            </div>
            <span className="px-2.5 py-0.5 rounded-full bg-teal-50 dark:bg-teal-500/10 text-teal-800 dark:text-teal-300 border border-teal-200 dark:border-teal-500/30 text-[10px] font-mono font-bold">
              v2.5.0 PRO
            </span>
          </div>

          <p>
            Bu platform, Sermaye Piyasası Kurulu (SPK) SPL Düzey 1 Lisanslama Sınavlarına hazırlanan adaylar için özel olarak geliştirilmiş yüksek performanslı, interaktif ve tam çevrimdışı (offline) bir masaüstü çalışma yazılımıdır.
          </p>

          <div className="p-4 rounded-xl bg-white dark:bg-fintech-card border border-slate-200 dark:border-fintech-border space-y-2">
            <div className="flex items-center justify-between">
              <span className="font-mono text-[11px] uppercase tracking-wider font-bold text-slate-500 dark:text-slate-400">
                Fikri Mülkiyet & Telif Sahibi
              </span>
              <span className="font-bold text-slate-900 dark:text-slate-100 text-xs">
                Emin ÇETİN
              </span>
            </div>
            <p className="text-[11px] text-slate-500 dark:text-slate-400 leading-relaxed">
              Programın tüm yazılım mimarisi, kullanıcı arayüzü tasarımı, sınav soru havuzu (935 soru), öğrenme kartları (400 kart) ve özet analiz tabloları <strong>Emin ÇETİN</strong> tarafından oluşturulmuştur. 5846 sayılı Fikir ve Sanat Eserleri Kanunu ile ilgili mevzuat hükümleri uyarınca <strong>tüm hakları saklıdır</strong>.
            </p>
          </div>

          <div className="flex flex-wrap items-center justify-between gap-2 pt-1 text-[11px] font-mono text-slate-500 dark:text-slate-400">
            <span>Müfredat: Temmuz 2026 SPL Standartları</span>
            <span>Veri Tabanı: 935 Soru • 400 Kart • 32 Bölüm</span>
          </div>
        </div>
      </div>
    </div>
  );
};
