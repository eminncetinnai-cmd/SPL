# -*- coding: utf-8 -*-
import json, re

# Load files
with open("src/data/questions_master.json", "r", encoding="utf-8") as f:
    master_qs = json.load(f)

# Create a dictionary of fixes for Module 1012 questions
# We will target all 61 flawed questions and refine their options
fixes = {}

# 1. q_1012_cikmis_001
fixes["q_1012_cikmis_001"] = {
    "options": [
        {"key": "A", "text": "Brüt Takas Sistemi"},
        {"key": "B", "text": "Merkezi Karşı Taraf"},
        {"key": "C", "text": "Merkezi Kaydi Saklama"},
        {"key": "D", "text": "Ödünç Pay Piyasası"},
        {"key": "E", "text": "Şartlı Virman Sistemi"}
    ]
}

# 2. q_1012_cikmis_006
fixes["q_1012_cikmis_006"] = {
    "options": [
        {"key": "A", "text": "Brüt Takas Yöntemi"},
        {"key": "B", "text": "Merkezi Karşı Taraf"},
        {"key": "C", "text": "Doğrudan Kaydi Saklama"},
        {"key": "D", "text": "Ödünç Pay Piyasası"},
        {"key": "E", "text": "Serbest Virman Sistemi"}
    ]
}

# 3. q_1012_cikmis_007
fixes["q_1012_cikmis_007"] = {
    "options": [
        {"key": "A", "text": "Üye kurum iflas etse dahi takas emirleri geri alınamaz ve teminatlar iflas masasına dahil edilemez."},
        {"key": "B", "text": "İflas veya tasfiye kararı verilmesi halinde takas sisteminde bekleyen tüm işlemler derhal hükümsüz kalır."},
        {"key": "C", "text": "Üye kurum piyasada işlem hacmi daraldığında sisteme ilettiği takas emirlerini tek taraflı geri çekebilir."},
        {"key": "D", "text": "Takas kuruluşuna teslim edilen teminatlar üzerinde kamu alacakları için öncelikli ihtiyati haciz uygulanır."},
        {"key": "E", "text": "Takas kesinliği yalnızca organize para piyasalarında geçerli olup hisse senedi piyasalarında uygulanmaz."}
    ]
}

# 4. q_1012_cikmis_010
fixes["q_1012_cikmis_010"] = {
    "options": [
        {"key": "A", "text": "Aynı gün içinde alınan hisse aynı gün satılabilir ve gün içi çok taraflı netleştirme uygulanır."},
        {"key": "B", "text": "Netleştirme uygulanmaz; alım bedeli peşin nakit, satım hissesi hazır olmalıdır ve aynı gün satılamaz."},
        {"key": "C", "text": "Kredili alım, açığa satış ve ödünç verme işlemleri standart marjin oranları üzerinden serbestçe yapılabilir."},
        {"key": "D", "text": "Takas mutabakatı Borsa İstanbul tarafından iptal edilerek yatırımcı hesapları bir önceki seans gününe döndürülür."},
        {"key": "E", "text": "Yalnızca şirketin hakim veya imtiyazlı ortaklarının hisse senetlerinde alım satım yapılmasına izin verilir."}
    ]
}

# 5. q_1012_cikmis_017
fixes["q_1012_cikmis_017"] = {
    "options": [
        {"key": "A", "text": "Açığa Satış İlkesi"},
        {"key": "B", "text": "Teslim Karşılığı Ödeme İlkesi"},
        {"key": "C", "text": "Vadeli Netleştirme İlkesi"},
        {"key": "D", "text": "Temerrüt Faizi İlkesi"},
        {"key": "E", "text": "Çok Taraflı Takas İlkesi"}
    ]
}

# 6. q_1012_cikmis_018
fixes["q_1012_cikmis_018"] = {
    "options": [
        {"key": "A", "text": "İşlem gününde (T+0)"},
        {"key": "B", "text": "İki iş günü sonra (T+2)"},
        {"key": "C", "text": "Üç iş günü sonra (T+3)"},
        {"key": "D", "text": "Hafta sonu takas seansında"},
        {"key": "E", "text": "On beş iş günü sonra (T+15)"}
    ]
}

# 7. q_1012_cikmis_023
fixes["q_1012_cikmis_023"] = {
    "options": [
        {"key": "A", "text": "Başlangıç Teminatı"},
        {"key": "B", "text": "Munzam Teminat"},
        {"key": "C", "text": "Garanti Fonu Katkısı"},
        {"key": "D", "text": "Üyelik Teminatı"},
        {"key": "E", "text": "Değişim Teminatı"}
    ]
}

# 8. q_1012_cikmis_024
fixes["q_1012_cikmis_024"] = {
    "options": [
        {"key": "A", "text": "Borsa İstanbul Anonim Şirketi"},
        {"key": "B", "text": "Merkezi Kayıt Kuruluşu Anonim Şirketi"},
        {"key": "C", "text": "İstanbul Takas ve Saklama Bankası A.Ş."},
        {"key": "D", "text": "Sermaye Piyasası Kurulu Başkanlığı"},
        {"key": "E", "text": "Türkiye Sermaye Piyasaları Birliği"}
    ]
}

# 9. q_1012_konu_006
fixes["q_1012_konu_006"] = {
    "options": [
        {"key": "A", "text": "Aynı gün başlangıç / En fazla 30 gün bitiş"},
        {"key": "B", "text": "En fazla 7 gün başlangıç / En fazla 1 yıl bitiş"},
        {"key": "C", "text": "En fazla 2 gün başlangıç / En fazla 180 gün bitiş"},
        {"key": "D", "text": "En fazla 15 gün başlangıç / En fazla 2 yıl bitiş"},
        {"key": "E", "text": "En fazla 30 gün başlangıç / En fazla 5 yıl bitiş"}
    ]
}

# 10. q_1012_konu_008
fixes["q_1012_konu_008"] = {
    "options": [
        {"key": "A", "text": "Borsa İstanbul Anonim Şirketi"},
        {"key": "B", "text": "Portföy Saklama Kuruluşu"},
        {"key": "C", "text": "Yatırımcı Tazmin Merkezi"},
        {"key": "D", "text": "Türkiye Sermaye Piyasaları Birliği"},
        {"key": "E", "text": "Merkezi Kayıt Kuruluşu"}
    ]
}

# 11. q_1012_master_004
fixes["q_1012_master_004"] = {
    "options": [
        {"key": "A", "text": "Doğrudan Hazine ve Maliye Bakanlığına bağlı, kamu sermayeli ve tüzel kişiliği haiz bir kalkınma bankasıdır."},
        {"key": "B", "text": "Yalnızca yabancı kurumsal yatırımcıların hesap açabildiği ve serbest döviz transferi yapan kıyı bankasıdır."},
        {"key": "C", "text": "Özel bir anonim şirket statüsünde, Bankacılık Kanunu'na tabi kalkınma ve yatırım bankası ile SPKn uyarınca Merkezi Takas Kuruluşudur."},
        {"key": "D", "text": "Borsa İstanbul bünyesinde işletilen, mevduat kabul etme yetkisine sahip ve şube ağıyla çalışan kamu mevduat bankasıdır."},
        {"key": "E", "text": "Türkiye Sermaye Piyasaları Birliği bünyesinde faaliyet yürüten, kâr amacı gütmeyen kamu yararına bir tüzel kişiliktir."}
    ]
}

# 12. q_1012_master_007
fixes["q_1012_master_007"] = {
    "options": [
        {"key": "A", "text": "Teslim Karşılığı Ödeme İlkesi"},
        {"key": "B", "text": "Açığa Satış ve Ödünç İlkesi"},
        {"key": "C", "text": "Tek Taraflı Takas İlkesi"},
        {"key": "D", "text": "Takas Kesinliği İlkesi"},
        {"key": "E", "text": "Kayıtsız Şartsız Devir İlkesi"}
    ]
}

# 13. q_1012_master_008
fixes["q_1012_master_008"] = {
    "options": [
        {"key": "A", "text": "Takasbank Para Piyasası"},
        {"key": "B", "text": "BIST Tahvil Kesin Alım Pazarı"},
        {"key": "C", "text": "Serbest Altın ve Döviz Piyasası"},
        {"key": "D", "text": "Bankalararası Tahvil Repo Pazarı"},
        {"key": "E", "text": "Vadeli İşlem ve Opsiyon Pazarı"}
    ]
}

# 14. q_1012_master_009
fixes["q_1012_master_009"] = {
    "options": [
        {"key": "A", "text": "Bireysel Takas Üyesi ve Kurumsal Takas Üyesi"},
        {"key": "B", "text": "Doğrudan Takas Üyesi ve Genel Takas Üyesi"},
        {"key": "C", "text": "Tam Yetkili Takas Üyesi ve Kısmi Takas Üyesi"},
        {"key": "D", "text": "Yerel Takas Üyesi ve Uluslararası Takas Üyesi"},
        {"key": "E", "text": "Birincil Takas Üyesi ve İkincil Takas Üyesi"}
    ]
}

# 15. q_1012_master_011
fixes["q_1012_master_011"] = {
    "options": [
        {"key": "A", "text": "Takasbank ve Bankalararası Takas Odaları Merkezi"},
        {"key": "B", "text": "Merkezi Kayıt Kuruluşu ve Borsa İstanbul"},
        {"key": "C", "text": "Sermaye Piyasası Kurulu ve Maliye Bakanlığı"},
        {"key": "D", "text": "Türkiye Sermaye Piyasaları Birliği ve TCMB"},
        {"key": "E", "text": "Bankacılık Düzenleme ve Denetleme Kurumu ve BİAŞ"}
    ]
}

# 16. q_1012_master_015
fixes["q_1012_master_015"] = {
    "options": [
        {"key": "A", "text": "Yatırımcı gün içinde aldığı hisse senedini aynı gün serbestçe satabilir ve net bakiye üzerinden takasa dahil olur."},
        {"key": "B", "text": "Alınan hisse gün içi satılamaz, netleştirme yapılmaz; takas T+2'de brüt nakit ve brüt hisse ile sonuçlandırılır."},
        {"key": "C", "text": "Aracı kurumlar takas alacaklarını Takasbank'tan peşin tahsil eder ancak borçlarını T+5 gününe kadar erteleyebilirler."},
        {"key": "D", "text": "Hisse senedi üzerindeki tüm temettü ve oy hakları brüt takas tedbiri kaldırılıncaya kadar kanunen dondurulur."},
        {"key": "E", "text": "Yatırımcılar işlemlerini sadece fiziki hisse senetlerini takas merkezine bizzat elden teslim ederek gerçekleştirebilirler."}
    ]
}

# 17. q_1012_master_018
fixes["q_1012_master_018"] = {
    "options": [
        {"key": "A", "text": "Başlangıç Teminatı"},
        {"key": "B", "text": "Sürdürme Teminatı"},
        {"key": "C", "text": "Olağanüstü Teminat"},
        {"key": "D", "text": "Fiziki Teslimat Teminatı"},
        {"key": "E", "text": "Değişim Teminatı"}
    ]
}

# 18. q_1012_master_023
fixes["q_1012_master_023"] = {
    "options": [
        {"key": "A", "text": "Gün İçi Likidite Kredisi"},
        {"key": "B", "text": "Uzun Vadeli Yatırım Kredisi"},
        {"key": "C", "text": "Müşteri Kredili İşlem Avansı"},
        {"key": "D", "text": "Gecelik Repo Kredisi"},
        {"key": "E", "text": "Döviz Swap Destek Kredisi"}
    ]
}

# 19. q_1012_master_025
fixes["q_1012_master_025"] = {
    "options": [
        {"key": "A", "text": "Merkezi Kayıt Kuruluşu A.Ş."},
        {"key": "B", "text": "Borsa İstanbul Anonim Şirketi"},
        {"key": "C", "text": "İstanbul Takas ve Saklama Bankası A.Ş."},
        {"key": "D", "text": "Türkiye Cumhuriyet Merkez Bankası"},
        {"key": "E", "text": "Sermaye Piyasası Kurulu"}
    ]
}

# 20. q_1012_master_026
fixes["q_1012_master_026"] = {
    "options": [
        {"key": "A", "text": "Borsada işlem gören sermaye piyasası araçlarının fiziki basımını, güvenli matbaalarda üretimini ve teslimini organize etmek."},
        {"key": "B", "text": "Sermaye piyasası araçlarının kaydileştirilmesini sağlamak, hak sahipliği sicilini tutmak ve merkezi saklamasını yürütmek."},
        {"key": "C", "text": "Yatırım kuruluşlarına kredi tahsis etmek ve organize para piyasalarında gecelik faiz oranlarını belirleyerek uygulamak."},
        {"key": "D", "text": "Halka açık ortaklıkların hisse senetlerinde manipülasyon ve içeriden öğrenenlerin ticaretini tespit edip idari para cezası kesmek."},
        {"key": "E", "text": "Tüm sermaye piyasası kurumlarının bağımsız denetim raporlarını hazırlamak ve vergi beyannamelerini doğrudan onaylamak."}
    ]
}

# 21. q_1012_master_027
fixes["q_1012_master_027"] = {
    "options": [
        {"key": "A", "text": "Halka Arz Süreci"},
        {"key": "B", "text": "Kaydileştirme"},
        {"key": "C", "text": "Kotasyon Alma"},
        {"key": "D", "text": "Konsolidasyon"},
        {"key": "E", "text": "Sermaye Azaltımı"}
    ]
}

# 22. q_1012_master_030
fixes["q_1012_master_030"] = {
    "options": [
        {"key": "A", "text": "Söz konusu hisse senetleri tamamen iptal edilir ve bedelleri hiçbir hak talep edilmeksizin Yatırımcı Tazmin Merkezi'ne irat kaydedilir."},
        {"key": "B", "text": "Pay sahiplerinin ortaklık sıfatı düşer ve şirket yönetimi bu hisseleri genel kurul yetkisiyle üçüncü şahıslara yeniden satabilir."},
        {"key": "C", "text": "Hisseler borsada işlem göremez, aracı kurumlarca aracılık edilemez; temettü dışı haklar donar, teslim edilince haklar canlanır."},
        {"key": "D", "text": "Şirket bu hisseleri otomatik olarak tahvile dönüştürerek yatırımcılara sabit faizli borçlanma senedi olarak teslim etmek zorundadır."},
        {"key": "E", "text": "Hisselerin mülkiyeti doğrudan Hazine ve Maliye Bakanlığı'na geçer ve şirket sermayesi azaltılarak paylar sicilden terkin edilir."}
    ]
}

# 23. q_1012_master_031
fixes["q_1012_master_031"] = {
    "options": [
        {"key": "A", "text": "Kayıtlar sadece bilgilendirme amaçlı olup resmi uyuşmazlıklarda aracı kurumun fiziki dekontları esas alınır."},
        {"key": "B", "text": "Merkezi Kayıt Kuruluşu nezdinde tutulan elektronik kayıtlar mülkiyetin ispatında kanunen kesin delil teşkil eder."},
        {"key": "C", "text": "Hak sahipliği ispatı yalnızca şirket merkezinde tutulan fiziki basılı pay defterinin ibraz edilmesiyle mümkündür."},
        {"key": "D", "text": "Elektronik kayıtlar adi karine sayılır ve noter tasdikli sözleşme ibraz edilmedikçe mahkemelerce delil kabul edilmez."},
        {"key": "E", "text": "MKK kayıtları sadece genel kurula katılım hakkı verir, hisse devirlerinde ve hacizlerde herhangi bir bağlayıcılığı yoktur."}
    ]
}

# 24. q_1012_master_036
fixes["q_1012_master_036"] = {
    "options": [
        {"key": "A", "text": "Borsa İstanbul Anonim Şirketi"},
        {"key": "B", "text": "Merkezi Kayıt Kuruluşu Anonim Şirketi"},
        {"key": "C", "text": "İstanbul Takas ve Saklama Bankası A.Ş."},
        {"key": "D", "text": "Sermaye Piyasası Kurulu Başkanlığı"},
        {"key": "E", "text": "Türkiye Sermaye Piyasaları Birliği"}
    ]
}

# 25. q_1012_master_040
fixes["q_1012_master_040"] = {
    "options": [
        {"key": "A", "text": "Virman İşlemi"},
        {"key": "B", "text": "Blokaj İşlemi"},
        {"key": "C", "text": "Kotasyon İşlemi"},
        {"key": "D", "text": "Takas Kesinliği"},
        {"key": "E", "text": "Repo Sözleşmesi"}
    ]
}

# 26. q_1012_master_042
fixes["q_1012_master_042"] = {
    "options": [
        {"key": "A", "text": "Ortaklıklar fiziki pay defteri tutmaya devam etmek zorunda olup MKK kayıtları sadece yardımcı istatistiki bilgi sunar."},
        {"key": "B", "text": "MKK tarafından tutulan kaydi hesap kayıtları ortaklıklar açısından pay defteri hükmündedir ve fiziki defter aranmaz."},
        {"key": "C", "text": "Pay defteri kayıtları yalnızca Ticaret Sicil Müdürlüğü nezdinde tutulur ve MKK sistemine herhangi bir veri aktarılmaz."},
        {"key": "D", "text": "Kaydi hisse senetleri için her yıl sonunda noter onaylı basılı pay defteri hazırlanıp MKK'ya onaylatılmalıdır."},
        {"key": "E", "text": "Anonim şirketler pay defterini aracı kurumlar vasıtasıyla saklar ve MKK kayıtları pay defteri yerine geçmez."}
    ]
}

# 27. q_1012_master_044
fixes["q_1012_master_044"] = {
    "options": [
        {"key": "A", "text": "Borsa İstanbul Anonim Şirketi"},
        {"key": "B", "text": "Sermaye Piyasası Kurulu"},
        {"key": "C", "text": "Merkezi Kayıt Kuruluşu"},
        {"key": "D", "text": "Takasbank A.Ş."},
        {"key": "E", "text": "Ticaret Bakanlığı"}
    ]
}

# 28. q_1012_master_062
fixes["q_1012_master_062"] = {
    "options": [
        {"key": "A", "text": "O seans yapılan tüm alım satım işlemleri Borsa tarafından derhal iptal edilir ve takasa dahil edilmez."},
        {"key": "B", "text": "Devre kesici anına kadar gerçekleşmiş tüm işlemler geçerlidir ve standart takas süreci aynen yürütülür."},
        {"key": "C", "text": "İlgili hissede o günkü takas işlemleri iptal edilerek tüm nakit ve hisseler yatırımcılara iade edilir."},
        {"key": "D", "text": "Takas valörü otomatik olarak T+5 gününe uzatılır ve üyelerden ilave munzam teminat talep edilir."},
        {"key": "E", "text": "Yalnızca kurumsal yatırımcıların işlemleri geçerli sayılır, bireysel yatırımcıların takasları askıya alınır."}
    ]
}

# 29. q_1012_master_066
fixes["q_1012_master_066"] = {
    "options": [
        {"key": "A", "text": "Menkul kıymeti satıp karşılığında nakit alır; vade bitiminde nakdi faiziyle geri ödeyerek menkul kıymeti geri alır."},
        {"key": "B", "text": "Nakit verip karşılığında menkul kıymeti teminat alır; vade sonunda menkul kıymeti iade edip nakdi faiziyle alır."},
        {"key": "C", "text": "Müşterisinin hisse senetlerini açığa satarak piyasadaki fiyat düşüşlerinden risksiz arbitraj geliri elde eder."},
        {"key": "D", "text": "Takasbank Garanti Fonuna katkı payı yatırarak temerrüde düşen diğer üyelerin borçlarını tasfiye etmeyi üstlenir."},
        {"key": "E", "text": "VİOP pazarında vadeli sözleşme satın alarak dayanak varlığı vade sonunda fiziki teslimatla talep etme hakkı kazanır."}
    ]
}

# 30. q_1012_master_077
fixes["q_1012_master_077"] = {
    "options": [
        {"key": "A", "text": "İşlem gününde seans kapanışından hemen önce saat 17:30'a kadar"},
        {"key": "B", "text": "İşlem gününü izleyen iş günü (T+1) en geç saat 15:00'e kadar"},
        {"key": "C", "text": "Standart takas günü olan T+2 günü saat 16:45'e kadar"},
        {"key": "D", "text": "Haftalık takas mutabakatının yapıldığı Cuma günü seans sonuna kadar"},
        {"key": "E", "text": "Sözleşme vadesinin dolduğu son işlem gününde saat 12:00'ye kadar"}
    ]
}

# 31. q_1012_master_090
fixes["q_1012_master_090"] = {
    "options": [
        {"key": "A", "text": "Saklama kuruluşu kurucu PYŞ'nin iştiraki olmak zorunda olup fon harcamalarının onayını kurucu yönetim kurulundan alır."},
        {"key": "B", "text": "Saklama kuruluşu PYŞ'den tamamen bağımsızdır ve fon malvarlığını korumak üzere mevzuata uygunluk gözetimi yapar."},
        {"key": "C", "text": "Saklama kuruluşu fon portföyündeki hisse senetlerinin alım ve satım kararlarını doğrudan kendi analistleriyle belirler."},
        {"key": "D", "text": "Saklama kuruluşu yalnızca fon katılma paylarının halka arz izahnamesini hazırlamak ve SPK'ya tescil ettirmekle görevlidir."},
        {"key": "E", "text": "Saklama kuruluşu fon yönetim ücretlerini tahsil ederek tamamını Yatırımcı Tazmin Merkezi'ne aktarmakla yükümlüdür."}
    ]
}

# 32. q_1012_master_091
fixes["q_1012_master_091"] = {
    "options": [
        {"key": "A", "text": "Hisseler aracı kurumun iflas masasına devredilir ve aracı kurumun diğer tüm ticari borçlularına oransal paylaştırılır."},
        {"key": "B", "text": "Hisseler iflas masasına DAHİL EDİLEMEZ; MKK nezdinde yatırımcı adına kayıtlı olduğundan korunur ve YTM devri yapılır."},
        {"key": "C", "text": "Yatırımcının hisse senetleri derhal Borsa İstanbul'da piyasa fiyatından satılarak elde edilen nakit Hazineye aktarılır."},
        {"key": "D", "text": "Yatırımcı hisselerinin mülkiyetini kaybeder ve yalnızca aracı kurumun sermayesi oranında sınırlı tazminat talep edebilir."},
        {"key": "E", "text": "Hisse senetleri Takasbank Garanti Fonu'na intikal eder ve Takasbank üyeleri arasında eşit olarak bölüştürülür."}
    ]
}

# 33. q_1012_master_095
fixes["q_1012_master_095"] = {
    "options": [
        {"key": "A", "text": "Teminat iadesi ancak ilgili şirketin yıllık olağan genel kurul toplantısında onaylanması üzerine yapılabilir."},
        {"key": "B", "text": "Borç ve temerrüt faizi kapatıldığı anda sistem tarafından otomatik olarak üyenin serbest hesabına iade edilir."},
        {"key": "C", "text": "Takasbank teminatı 1 yıl boyunca faizsiz blokede tutar ve üyenin yeni bir temerrüde düşmeyeceğini izler."},
        {"key": "D", "text": "Teminatın %50'si aracı kuruma iade edilirken kalan %50'lik kısım Takasbank gelir havuzuna irat kaydedilir."},
        {"key": "E", "text": "Teminatlar nakit olarak ödenmeyip yalnızca Borsa İstanbul A.Ş. pay senetleri şeklinde mislen iade edilebilir."}
    ]
}

# 34. q_1012_ogretici_004
fixes["q_1012_ogretici_004"] = {
    "options": [
        {"key": "A", "text": "Halka açık şirketlerin mali tablolarını bağımsız denetim standartlarına göre denetlemek"},
        {"key": "B", "text": "İşlem tarafları arasındaki karşı taraf kredi riskini yönetmek ve takasın ifasını garanti etmek"},
        {"key": "C", "text": "Yatırımcıların portföylerini yöneterek borsa endeksinin üzerinde getiri performansı sağlamak"},
        {"key": "D", "text": "Aracı kurumlara sermaye piyasası faaliyet izni ve lisans belgesi tahsis etmek"},
        {"key": "E", "text": "Şirketlerin genel kurul toplantılarını bizzat yönetmek ve yönetim kurulu üyelerini seçmek"}
    ]
}

# 35. q_1012_ogretici_005
fixes["q_1012_ogretici_005"] = {
    "options": [
        {"key": "A", "text": "Üyenin Borsa İstanbul nezdinde rekor düzeyde işlem hacmine ulaşarak işlem limitlerini doldurmasıdır."},
        {"key": "B", "text": "Takas yükümlülüğünün süresinde yerine getirilmemesi sonucu üyenin mali taahhüdünü ifa edememesidir."},
        {"key": "C", "text": "Aracı kurumun müşterilerine sunduğu yatırım danışmanlığı tavsiyelerinde isabetsiz tahmin yapmasıdır."},
        {"key": "D", "text": "Halka açık şirketin genel kurulunda pay sahiplerine temettü dağıtılmaması yönünde karar alınmasıdır."},
        {"key": "E", "text": "Merkezi Kayıt Kuruluşu nezdinde açılan hesapların kimlik teyidi yapılmadan kullanıma sunulmasıdır."}
    ]
}

# 36. q_1012_ogretici_010
fixes["q_1012_ogretici_010"] = {
    "options": [
        {"key": "A", "text": "Piyasadaki hisse senetlerinin hedef fiyatlarını belirlemek amacıyla yapılan şirket analizleridir."},
        {"key": "B", "text": "Kayıtların ve takas verilerinin taraflar arasında tutarlılığını kontrol eden operasyonel teyit sürecidir."},
        {"key": "C", "text": "Aracı kurum personeline verilen periyodik sermaye piyasası mevzuat eğitim programıdır."},
        {"key": "D", "text": "Yatırımcıların borsa emirlerinin eşleşmesi amacıyla geliştirilen yüksek hızlı işlem altyapısıdır."},
        {"key": "E", "text": "Halka açık ortaklıkların Kamuyu Aydınlatma Platformu'na gönderdikleri özel durum açıklamalarıdır."}
    ]
}

# 37. q_1012_ogretici_012
fixes["q_1012_ogretici_012"] = {
    "options": [
        {"key": "A", "text": "Mütemerrit üyenin teminat ve katkısı -> Takasbank tahsisli sermayesi -> Diğer üyelerin Garanti Fonu katkıları"},
        {"key": "B", "text": "Diğer üyelerin Garanti Fonu katkıları -> Takasbank taahhütlü sermayesi -> Mütemerrit üyenin teminatları"},
        {"key": "C", "text": "Takasbank tahsisli sermayesi -> Mütemerrit üyenin teminatları -> Diğer üyelerin ilave katkı payları"},
        {"key": "D", "text": "Yatırımcı Tazmin Merkezi fonları -> Takasbank kalan sermayesi -> Borsa İstanbul Garanti Fonu rezervi"},
        {"key": "E", "text": "Türkiye Cumhuriyet Merkez Bankası avansı -> Takasbank munzam teminatı -> Mütemerrit üye portföyü"}
    ]
}

# 38. q_1012_ogretici_014
fixes["q_1012_ogretici_014"] = {
    "options": [
        {"key": "A", "text": "Yatırım kuruluşunun iflası veya tedrici tasfiyesi halinde yatırımcıların hisse senetleri korunur ve YTM tazmini devreye girer."},
        {"key": "B", "text": "Aracı kurum iflas ettiğinde yatırımcıların tüm hisse senetleri iflas masasına dahil edilir ve genel alacaklılara satılır."},
        {"key": "C", "text": "Yatırımcıların zararları doğrudan Borsa İstanbul Yönetim Kurulu üyelerinin şahsi malvarlıklarından nakden karşılanır."},
        {"key": "D", "text": "Merkezi Kayıt Kuruluşu iflas eden kurumun tüm yatırımcı hesaplarını resen kapatarak mülkiyet kayıtlarını tamamen siler."},
        {"key": "E", "text": "Yatırımcıların yalnızca döviz cinsinden varlıkları korunur, Türk Lirası ve hisse senedi varlıkları tamamen tazminatsız kalır."}
    ]
}

# 39. q_1012_ogretici_017
fixes["q_1012_ogretici_017"] = {
    "options": [
        {"key": "A", "text": "Üyeler teminatsız olarak diledikleri tutarda sınırsız nakit borçlanma hakkına sahip olurlar."},
        {"key": "B", "text": "Üyeler nakit borçlanabilmek için Takasbank'a mevzuatta kabul edilen geçerli teminatları vermek zorundadır."},
        {"key": "C", "text": "Nakit borçlanma faiz oranları üyeler tarafından kendi aralarında ikili müzakereyle gizlice kararlaştırılır."},
        {"key": "D", "text": "Yalnızca yabancı bankaların işlem yapabildiği, yerli aracı kurumlara kapalı bir pazar yapısıdır."},
        {"key": "E", "text": "Borçlanılan nakit tutarlar sadece Borsa İstanbul A.Ş. hisse senetlerinin alımında kullanılabilir."}
    ]
}

# Clean giveaway parentheticals in other questions
giveaway_patterns = [
    (r"\s*\(MKT\)", ""),
    (r"\s*\(MKK\)", ""),
    (r"\s*\(TPP\)", ""),
    (r"\s*\(SPK\)", ""),
    (r"\s*\(DvP\s*/\s*Delivery versus Payment\)", ""),
    (r"\s*\(DvP\)", ""),
    (r"\s*\(DCM\)", ""),
    (r"\s*\(GCM\)", ""),
    (r"\s*\(BTOM\)", ""),
    (r"\s*\(Initial Margin\)", ""),
    (r"\s*\(Variation Margin\)", ""),
    (r"\s*\(Intraday Credit\)", ""),
    (r"\s*\(Dematerialization\)", ""),
    (r"\s*\(Menkul Kıymet Transferi\)", ""),
    (r"\s*\(Central Counterparty\)", ""),
    (r"\s*\(Direct Holding\)", ""),
    (r"\s*\(Omnibus\)", ""),
    (r"\s*\(Settlement\)", ""),
    (r"\s*\(Clearing\)", ""),
]

# Apply fixes to master_qs
updated_count = 0
for q in master_qs:
    if str(q.get("module_id")) != "1012":
        continue
    qid = q["id"]
    if qid in fixes:
        q["options"] = fixes[qid]["options"]
        updated_count += 1
    else:
        # Check if correct option has a unilateral parenthetical that can be cleaned
        opts = q["options"]
        c_key = q["correct_answer"]
        c_opt = next((o for o in opts if o["key"] == c_key), None)
        if c_opt:
            c_has_paren = bool(re.search(r'\(.*?\)', c_opt['text']))
            wrong_has_paren = any(re.search(r'\(.*?\)', o['text']) for o in opts if o['key'] != c_key)
            if c_has_paren and not wrong_has_paren:
                # Clean parenthetical from correct option
                orig_text = c_opt["text"]
                new_text = orig_text
                for pat, rep in giveaway_patterns:
                    new_text = re.sub(pat, rep, new_text)
                # If still has trailing paren, clean it
                new_text = re.sub(r"\s*\([^)]*\)$", "", new_text)
                if new_text != orig_text and len(new_text) > 5:
                    c_opt["text"] = new_text.strip()
                    updated_count += 1

print(f"Applied fixes to {updated_count} questions in Module 1012.")

# Save updated questions_master.json
with open("src/data/questions_master.json", "w", encoding="utf-8") as f:
    json.dump(master_qs, f, ensure_ascii=False, indent=2)

print("Saved to src/data/questions_master.json")
