from main import prisionBreak

def testOne():
    assert prisionBreak([1, 1, 0, 0, 0, 1, 0]) == 4

def testTwo():
    assert prisionBreak([1, 1, 1]) == 1

def testThree():
    assert prisionBreak([0, 0, 0]) == 0

def testFour():
    assert prisionBreak([0, 1, 1, 1]) == 0

if __name__ == "__main__":
    testOne()
    testTwo()
    testThree()
    testFour()
    print("All tests passed")