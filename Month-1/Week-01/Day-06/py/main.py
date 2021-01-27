# Next Prime

def isPrime(number):
    allNumbers = []
    y = 1
    while y < number - 1:
        y = y + 1
        allNumbers.append(y)  

    floatCount = 0
    for elem in allNumbers:
        if number % elem > 0:
            floatCount = floatCount + 1
    isPrime = floatCount == len(allNumbers)
    return isPrime

def nextPrime(number):
    prime = False
    while prime == False:
        prime = isPrime(number)        
        if prime == False:
            number = number + 1
    return number

if __name__ == "__main__":
    x = 90
    print(nextPrime(x))