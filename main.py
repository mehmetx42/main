meme_dict = {
    "CRINGE": "Garip ya da utandırıcı bir şey",
    "LOL": "Komik bir şeye verilen cevap",
    "XD": "Komik bir şeye diğer bir şekilde verilen cevap",
    "GG": "İyi oyundu anlamında verilen cevap",
    "NT": "İyi denemeydi anlamında verilen cevap",
    "GANG": "Yardım anlamında verilen cevap",
}
for dongu in range(5):
    
    word = input("Anlamadığınız bir kelime yazın (hepsini büyük harflerle yazın!): ")
    
    if word in meme_dict:
        print(meme_dict[word])
    else:
        print("Kelime sözlükte bulunamadı.")
