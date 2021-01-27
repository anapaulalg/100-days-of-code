from main import nextPrime

def thirteen():
    assert nextPrime(13) == 13

def fourteen():
    assert nextPrime(14) == 17

def thirtytwo():
    assert nextPrime(32) == 37


if __name__ == "__main__":
    thirteen()
    fourteen()
    thirtytwo()
    print('All tests passed')