import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('src/data/all_questions.json', 'r', encoding='utf-8') as f:
    questions = json.load(f)

FINAL_7 = {
    "q_1005_master_025": {
        "text": "Müşteri emirlerinin sisteme kabulü ve borsaya iletiminde yatırım kuruluşunun uymak zorunda olduğu öncelik kuralı nedir?",
        "options": [
            {"key": "A", "text": "İşlem hacmi ve getirisi en yüksek olan kurumsal müşterilerin emirleri öncelikle iletilir"},
            {"key": "B", "text": "Aracı kurumun kendi portföyü için verdiği alım-satım emirleri müşteri emirlerinden önce girilir"},
            {"key": "C", "text": "Emirler sisteme geliş zamanı sırasına (zaman önceliğine) göre kaydedilir ve borsa sistemine iletilir"},
            {"key": "D", "text": "Gün içinde toplanan tüm müşteri emirleri seans sonunda tek bir blok emir halinde eşleştirilir"},
            {"key": "E", "text": "Yalnızca kredili hesap sözleşmesi bulunan genel müşterilerin emirlerine öncelik tanınır"}
        ],
        "correct_answer": "C",
        "explanation": "SPK mevzuatına göre aracı kurumlar, müşteri emirlerini geliş zamanı sırasına (zaman önceliği kuralı) göre sisteme kaydetmek ve borsa işlem sistemine iletmek zorundadır. Kurum kendi nam ve hesabına verdiği emirleri müşteri emirlerinin önüne geçiremez."
    },
    "q_1005_master_029": {
        "text": "Yatırım kuruluşlarının uygulayacakları komisyon oranları ve işlem masrafları ile ilgili hangisi DOĞRUDUR?",
        "options": [
            {"key": "A", "text": "Aracı kurumlar uyguladıkları komisyon oranlarını müşteriye önceden bildirmeksizin serbestçe artırabilir"},
            {"key": "B", "text": "Tüm borsa işlemleri için kanunda belirlenen tek bir maktu komisyon tutarının tahsili mecburidir"},
            {"key": "C", "text": "Komisyon oranları ve işlem masrafları aracı kurumların ticari sırrı olup kamuya açıklanması yasaktır"},
            {"key": "D", "text": "Komisyon ve masraf tarifeleri çerçeve sözleşmede açıkça belirtilmeli ve web sitesinde ilan edilmelidir"},
            {"key": "E", "text": "Bireysel genel müşterilerden hiçbir surette işlem komisyonu veya borsa payı kesilemez"}
        ],
        "correct_answer": "D",
        "explanation": "Yatırım kuruluşları uygulayacakları komisyon, ücret ve masraf tarifelerini çerçeve sözleşmede açık ve net olarak belirtmek ve güncel tarifelerini internet sitelerinde kamuya ilan etmek zorundadır. Sözleşmede yer almayan hiçbir gizli masraf tahsil edilemez."
    },
    "q_1005_master_043": {
        "text": "Yatırım danışmanlığı hizmeti sunulabilmesi için mevzuat gereğince aşağıdaki şartlardan hangisi ZORUNLUDUR?",
        "options": [
            {"key": "A", "text": "Müşterinin geçmiş borsa işlemlerinde en az %20 kârlılık elde etmiş olması"},
            {"key": "B", "text": "SPK'dan yetki belgesi alınması, yazılı danışmanlık sözleşmesi akdedilmesi ve Yerindelik Testi yapılması"},
            {"key": "C", "text": "Tavsiye edilecek sermaye piyasası araçları için müşteriye kesin anapara kâr garantisi taahhüt edilmesi"},
            {"key": "D", "text": "Danışmanlık hizmetinin yalnızca aracı kurumun merkez ofisinde yüz yüze verilmesi"},
            {"key": "E", "text": "Müşterinin portföyündeki hisselerin mülkiyetinin danışmana vekaleten devredilmesi"}
        ],
        "correct_answer": "B",
        "explanation": "Yatırım danışmanlığı; SPK'dan yetki belgesi alınmasını, müşteriyle yazılı yatırım danışmanlığı çerçeve sözleşmesi imzalanmasını ve müşterinin risk-getiri profilini ölçmek üzere Yerindelik Testi uygulanmasını emreder."
    },
    "q_1005_master_047": {
        "text": "Portföy yöneticisi veya yatırım danışmanının müşteriyle 'Kârdan pay alırım, zararı da kendi cebimden karşılarım' şeklinde sözleşme yapmasıyla ilgili hangisi DOĞRUDUR?",
        "options": [
            {"key": "A", "text": "Müşteri ile portföy yöneticisi arasında özel yazılı protokol düzenlenmesi şartıyla serbesttir"},
            {"key": "B", "text": "Yalnızca profesyonel müşteri statüsündeki kurumsal yatırımcılarla yapılan sözleşmelerde geçerlidir"},
            {"key": "C", "text": "SPK tarafından yatırımcı koruma aracı olarak kabul edilen ve tavsiye edilen standart bir uygulamadır"},
            {"key": "D", "text": "Yalnızca Borsa İstanbul pay piyasasında işlem gören BIST 30 hisseleri için geçerli bir yöntemdir"},
            {"key": "E", "text": "Zararın telafi edileceğine veya kâr garantisi verileceğine ilişkin taahhütte bulunulması KESİNLİKLE YASAKTIR"}
        ],
        "correct_answer": "E",
        "explanation": "SPK mevzuatı ve TSPB Meslek Kuralları uyarınca; sermaye piyasası çalışanlarının müşterilere kesin getiri taahhüdünde bulunması veya oluşacak zararın karşılanacağını garanti etmesi kesinlikle yasaktır."
    },
    "q_1005_master_050": {
        "text": "Bir yatırım kuruluşunda 'Bireysel Yatırım Danışmanı' olarak görev yapabilmek için aşağıdaki lisanslardan hangisine sahip olunması mevzuaten ZORUNLUDUR?",
        "options": [
            {"key": "A", "text": "Sermaye Piyasası Faaliyetleri Düzey 1 Lisansı"},
            {"key": "B", "text": "Sermaye Piyasası Faaliyetleri Düzey 2 Lisansı"},
            {"key": "C", "text": "Kurumsal Yönetim Derecelendirme Lisansı"},
            {"key": "D", "text": "Sermaye Piyasası Faaliyetleri Düzey 3 Lisansı"},
            {"key": "E", "text": "Gayrimenkul Değerleme Uzmanlığı Lisansı"}
        ],
        "correct_answer": "D",
        "explanation": "Yatırım Danışmanlığı hizmeti verecek personelin SPK Sermaye Piyasası Faaliyetleri Düzey 3 Lisansı ve ilgili yatırım danışmanlığı lisans belgesine sahip olması şarttır."
    },
    "q_1005_master_067": {
        "text": "Aşağıdaki kurumsal aktörlerden hangisi sermaye piyasası mevzuatına göre doğrudan 'Profesyonel Müşteri' sayılır?",
        "options": [
            {"key": "A", "text": "Yatırım fonları, emeklilik fonları ve sigorta şirketleri"},
            {"key": "B", "text": "Bankalar, aracı kurumlar ve portföy yönetim şirketleri"},
            {"key": "C", "text": "Merkezi Takas Kuruluşları, MKK ve Takasbank"},
            {"key": "D", "text": "Yetkili yabancı finansal kuruluşlar ve merkez bankaları"},
            {"key": "E", "text": "Yukarıda sayılan kurumsal aktörlerin tamamı doğrudan profesyonel müşteridir"}
        ],
        "correct_answer": "E",
        "explanation": "Yatırım Hizmetleri Tebliği m.31 uyarınca; bankalar, aracı kurumlar, portföy yönetim şirketleri, fonlar, sigorta şirketleri, Takasbank, MKK ve benzeri tüm kurumsal finansal kuruluşlar doğrudan Profesyonel Müşteri kabul edilir."
    },
    "q_1005_master_089": {
        "text": "Aşağıdakilerden hangisi Yatırımcı Tazmin Merkezi'nin (YTM) kanuni gelir kaynakları arasında yer alır?",
        "options": [
            {"key": "A", "text": "Yatırım kuruluşlarının ödediği giriş aidatları ve yıllık nispi katılma payları"},
            {"key": "B", "text": "10 yıllık zamanaşımına uğrayarak YTM'ye intikal eden emanet ve alacaklar"},
            {"key": "C", "text": "SPK tarafından tahsil edilen idari para cezalarının kanunda belirlenen payı"},
            {"key": "D", "text": "YTM malvarlığının nemalandırılmasından elde edilen faiz ve portföy gelirleri"},
            {"key": "E", "text": "Yukarıda sayılan kaynakların tamamı YTM'nin kanuni gelirlerindendir"}
        ],
        "correct_answer": "E",
        "explanation": "6362 sayılı Kanun m.85 uyarınca YTM'nin gelirleri; yatırım kuruluşlarının giriş ve yıllık katılma payları, zamanaşımına uğrayan varlıklar, idari para cezası payları ve fon malvarlığının getirisinden oluşur."
    }
}

for q in questions:
    qid = q['id']
    if qid in FINAL_7:
        rep = FINAL_7[qid]
        q['text'] = rep.get('text', q['text'])
        q['options'] = rep['options']
        q['correct_answer'] = rep['correct_answer']
        if 'explanation' in rep:
            q['explanation'] = rep['explanation']
        print(f"Polished final {qid}")

with open('src/data/all_questions.json', 'w', encoding='utf-8') as f:
    json.dump(questions, f, ensure_ascii=False, indent=2)

with open('src/data/questions_master.json', 'w', encoding='utf-8') as f:
    json.dump(questions, f, ensure_ascii=False, indent=2)

print("\nFinal 7 questions polished successfully!")
