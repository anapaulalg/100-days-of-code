from main import numberOfPairs

def onePair():
    assert numberOfPairs("AA") == 1

def fourPairs():
    assert numberOfPairs("CABBACCC") == 4

def zeroPair():
    assert numberOfPairs("AB") == 0

if __name__ == "__main__":
    onePair()
    fourPairs()
    zeroPair()
    print('All tests passed')