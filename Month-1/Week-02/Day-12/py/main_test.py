from main import landscapeType

def testOne():
    assert landscapeType([1, 4, 1]) == "montain"

def testTwo():
    assert landscapeType([9, 7, 9]) == "valley"

def testThree():
    assert landscapeType([2, 2, 2]) == "neither"

def testFour():
    assert landscapeType([1, 1, 6]) == "Peak cannot be a boundary element"

if __name__ == "__main__":
    testOne()
    testTwo()
    testThree()
    testFour()
    print("All tests passed")