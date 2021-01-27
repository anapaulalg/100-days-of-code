from main import nextPrime

def thirteenNextPrime():
    assert nextPrime(13) == 13

def fourteenNextPrime():
    assert nextPrime(14) == 17

def thirtytwoNextPrime():
    assert nextPrime(32) == 37

if __name__ == "__main__":
    thirteenNextPrime()
    fourteenNextPrime()
    thirtytwoNextPrime()
    print('All tests passed')