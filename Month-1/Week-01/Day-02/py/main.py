# Finding Nemo

sentence = "I am Nemo"
words = sentence.split() 
position = words.index("Nemo") + 1

if "Nemo" in words: 
    print("I found Nemo at " + str(position))    
        
else:
    print("I can't find Nemo :(")