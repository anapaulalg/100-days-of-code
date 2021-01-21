# Finding Nemo

def findNemo(sentence):
    words = sentence.split() 
    if "Nemo" in words: 
        position = words.index("Nemo") + 1
        return "I found Nemo at " + str(position)   
            
    else:
        return "I can't find Nemo :("

if __name__ == "__main__": 
    sentence = input("What is the sentence? ")
    print(findNemo(sentence))