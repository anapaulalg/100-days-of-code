from main import prisonBreak

def testOne():
    assert prisonBreak([1, 1, 0, 0, 0, 1, 0]) == 4

def testTwo():
    assert prisonBreak([1, 1, 1]) == 1

def testThree():
    assert prisonBreak([0, 0, 0]) == 0

def testFour():
    assert prisonBreak([0, 1, 1, 1]) == 0

if __name__ == "__main__":
    testOne()
    testTwo()
    testThree()
    testFour()
    print("All tests passed")