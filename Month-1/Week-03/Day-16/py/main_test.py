from main import nimGame

def testOne():
    assert nimGame(1) == True

def testTwo():
    assert nimGame(2) == True

def testThree():
    assert nimGame(5) == True

def testFour():
    assert nimGame(8) == False

if __name__ == "__main__":
    testOne()
    testTwo()
    testThree()
    testFour()
    print("All tests passed")