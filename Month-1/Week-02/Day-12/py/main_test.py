from main import landscapeType

def testOne():
    assert landscapeType([1, 4, 1]) == "montain"

def testTwo():
    assert landscapeType([9, 7, 9]) == "valley"

def testThree():
    assert landscapeType([2, 2, 2]) == "neither"

if __name__ == "__main__":
    testOne()
    testTwo()
    testThree()
    print("All tests passed")