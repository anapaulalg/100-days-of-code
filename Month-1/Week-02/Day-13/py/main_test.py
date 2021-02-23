from main import CanFit

def testOne():
    assert CanFit([1, 4, 1], 1) == True

def testTwo():
    assert CanFit([9, 7, 20], 2) == False

def testThree():
    assert CanFit([2, 2, 12], 3) == True

if __name__ == "__main__":
    testOne()
    testTwo()
    testThree()
    print("All tests passed")