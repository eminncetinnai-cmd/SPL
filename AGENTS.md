# SPK SPL DÜZEY 1 - GELİŞTİRME VE İÇERİK KURALLARI (AGENTS.md)

Bu dosya, bu çalışma alanında (workspace) çalışacak tüm yapay zekâ asistanları ve geliştiriciler için **bağlayıcı kalıcı kuralları** belirler.

---

## 1. Temel İlke: Türkiye Maarif Modeli & Gerçek Sınav Seviyesi

SPL sınavları ezberci değil; **beceri temelli, bağlamsal, muhakeme ve durum odaklı (senaryo)** ölçme yapar.
Havuzdaki tüm sorular, açıklamalar ve öğrenme araçları bu felsefeye tam uyumlu olmak zorundadır.

### Bilişsel Düzey Dağılımı (Maarif Bilişsel Modeli)
Havuzda yer alan veya yeni eklenecek/güncellenecek sorular aşağıdaki 3 bilişsel basamak dengesine uymalıdır:
1. **`KB1_Kavramsal` (~%30 - %35)**: Temel kavram, kanun hükmü, yetki ve görev tanımları.
2. **`KB2_Muhakeme` (~%35 - %40)**: **I, II, III Öncüllü Sorular**, iki kavramı karşılaştırma, istisnanın istisnasını ayırt etme, hukuki çelişki yakalama.
3. **`KB3_Vaka` (~%30 - %35)**: Gerçek piyasa aktörleri içeren olay kurguları ("A Portföy Yönetim Şirketi...", "Yatırımcı Bay X...") ve **Çok Adımlı Sayısal/Matematiksel Hesaplamalar**.

---

## 2. Psikometrik Kalite Kapıları (Tavizsiz Kurallar)

1. **Lazy Giveaways (Kusurlu İpuçları) Sıfır Tolerans:**
   - Şıklarda "Yukarıdakilerin hepsi/tamamı", "Hiçbiri", "A ve B", "C ve D" gibi konumsal veya ezberci seçenekler **KESİNLİKLE KULLANILAMAZ**.
   - Tüm şıklar bağımsız, teknik ve ikna edici çeldiriciler olmak zorundadır.
2. **Şık Uzunluk Dengesi (Length Outlier Bias):**
   - Doğru şık, yanlış şıkların ortalama uzunluğundan **en fazla 1.8 kat** uzun olabilir.
   - Aday sadece şıkkın uzunluğuna bakarak doğru cevabı tahmin edememelidir.
3. **5 Aşamalı Açıklama Standardı:**
   Her sorunun `explanation` alanı şu şablonu içermelidir:
   - `1. MEVZUAT DAYANAĞI`: İlgili Kanun/Tebliğ madde referansı.
   - `2. HUKUKİ / TEKNİK ÇERÇEVE`: Kavramın kuralı ve ilkeleri.
   - `3. ADIM ADIM İNCELEME / HESAPLAMA`: Öncül analizi veya matematiksel formül adımları.
   - `4. DOĞRU CEVAP VE SONUÇ`: Hükmün net tespiti.
   - `5. ÇELDİRİCİ TUZAĞI`: Adayın en çok düşebileceği sınav tuzağı (`trap`).

---

## 3. Sayısal ve Formül Standartları

Sayısal sorularda gerçek SPL sınavında sorulan formüller tam olarak işlenmelidir:
- **Bedelli Sermaye Artırımı & Rüçhan Değeri**: $P_{yeni} = \frac{P_{eski} + (B \times R_{fiyat})}{1 + B}$, $R = P_{eski} - P_{yeni}$.
- **Bedelsiz + Bedelli Birlikte**: $P_{yeni} = \frac{P_{eski} + (B \times R_{fiyat})}{1 + B + BD}$.
- **Temettü Referans Fiyatı**: $P_{ref} = P_{kapanis} - \text{Brüt Temettü}$ (Stopaj düşülmez).
- **Tahvil Kirli Fiyat**: $\text{Kirli Fiyat} = \text{Temiz Fiyat} + \text{Birikmiş Faiz}$.
- **VİOP Margin Call**: Teminatın Sürdürme Teminatı altına düşmesi durumunda Başlangıç Teminatı'na tamamlanması kuralı.
- **Kredili İşlem Özkaynak Tamamlama**:
  - Özkaynak oranı %35'in altına düştüğünde başlangıç seviyesi olan %50'ye tamamlanır.
  - **Nakit Tamamlama**: Eksik özkaynak tutarı kadar nakit yatırılır.
  - **Hisse Senedi Tamamlama**: Getirilen hisse senetleri özkaynak hesabında %50 katsayı ile kabul edildiğinden, gereken hisse piyasa değeri = $\text{Eksik Tutar} \times 2$.
- **High-Water Mark (Zirve Değer)**: Portföy yönetiminde başarı primi sadece geçmişteki en yüksek değer (zirve) ve eşik değer aşıldığında tahakkuk ettirilir.
- **2026 Asgari Özsermaye Tutarları**: Dar Yetkili: 45M TL, Kısmi Yetkili: 190M TL, Geniş Yetkili: 380M TL, PYŞ / Yeni Kuruluş: 440M TL.

---

## 4. Veri Bütünlüğü ve Senkronizasyon Protokolü

1. **Çift Dosya Eşzamanlılığı:**
   - Sorularda yapılan herhangi bir değişiklik hem `src/data/all_questions.json` hem de `src/data/questions_master.json` dosyasına birebir aynı anda uygulanmalıdır.
2. **Toplam Soru Sayısı Assertion'ı:**
   - Havuz toplamı **tam 935 soru** olarak korunmalıdır (1001: 233, 1003: 240, 1005: 238, 1012: 224).
3. **Doğrulama ve Derleme Zorunluluğu:**
   Her güncelleme sonrası şu testler çalıştırılmalıdır:
   - `python scripts/verify_all.py` -> %100 Başarı (PASS)
   - `npm run build` (`tsc && vite build`) -> 0 Hata
