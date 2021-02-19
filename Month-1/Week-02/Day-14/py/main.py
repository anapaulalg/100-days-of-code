# The Karaca's Encryption Algorithm

def encrypt(word):
    word = word[::-1]
    newword = word.replace("a", "0").replace("e", "1").replace("i", "2").replace("o", "2").replace("u", "3")
    result = newword + "aca"
    print(result)
    return result

if __name__ == "__main__":
    word = "banana"
    encrypt(word)