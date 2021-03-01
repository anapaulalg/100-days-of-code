# Prison Break

prision = [1, 0, 0, 1]

def prisionBreak(prision):
    n = -1
    for i in prision:
        if prision[0] == 1:
            n = n + 1
    
    newPrision = [0 if i==1 else 1 for i in prision]
    print(newPrision)
    
    return n

print(prisionBreak(prision))