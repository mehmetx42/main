meme_dict = {
    "CRINGE": "Garip ya da utandırıcı bir şey",
    "LOL": "Komik bir şeye verilen cevap",
    "XD": "Komik bir şeye diğer bir şekilde verilen cevap",
    "GG": "İyi oyundu anlamında verilen cevap",
    "NT": "İyi denemeydi anlamında verilen cevap",
    "GANG": "Yardım anlamında verilen cevap",
    "ROFL" - "bir şakaya karşılık cevap",
    "SHEESH" - "onaylamamak",
    "CREEPY" - "korkunç",
    "AGGRO" - "agresifleşmek/sinirlenmek",
    "IF" - "eğer",
    "EZ" - "kolay/kolaydı",
    "U2" - "seninde/sende",
    "HERO" - "Karakter",
    "HP" - "Can",
    "HF" - "İyi eğlenceler",
    "HEAL" - "Can verme",
    "AUTOFİLL" - "Tercih dışı seçim",
    "ACE" - "Katliam",
    "Ability" - "Oyundaki şampiyonların yetenekleri",
    "AFK" - "Oyunu bırakıp farklı bir yere gitmek, oyun ortasında bilgisayardan kalkmak",
}

for dongu in range(5):
    
    word = input("Anlamadığınız bir kelime yazın (hepsini büyük harflerle yazın!): ")
    
    if word in meme_dict:
        print(meme_dict[word])
    else:
        print("Kelime sözlükte bulunamadı.")
