# Prison Break

prision = [1, 1, 1]

def prisionBreak(prision):
    n = 0
    for i in prision:
        if prision[0] == 0:
            n = 0 
        elif prision[i] == prision[i+1]:
            n = 1
        else:
            n = n + 1

    newPrision = [0 if i==1 else 1 for i in prision]
    print(newPrision)
    
    return n

print(prisionBreak(prision))