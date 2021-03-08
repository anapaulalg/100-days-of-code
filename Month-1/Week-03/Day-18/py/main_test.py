from main import uniquePaths

def testOne():
    assert uniquePaths(3, 7) == 28

def testTwo():
    assert uniquePaths(3, 2) == 3

def testThree():
    assert uniquePaths(3, 3) == 6

if __name__ == "__main__":
    testOne()
    testTwo()
    testThree()
    print("All tests passed")