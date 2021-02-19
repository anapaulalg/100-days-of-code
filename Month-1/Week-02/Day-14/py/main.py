# The Karaca's Encryption Algorithm

word = "banana"[::-1]

def encrypt(word):
    newword = word.replace("a", "0").replace("e", "1").replace("i", "2").replace("o", "2").replace("u", "3")
    aca = "aca"
    print(newword + aca)
    return encrypt

encrypt(word)