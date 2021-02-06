from main import tress

def testOne():
    assert tress(1, 1) == 1

def testTwo():
    assert tress(1, 3) == [1, 1, 2, 5]

def testThree():
    assert tress(1, 5) == [1, 1, 2, 5, 14, 42]

if __name__ == "__main__":
    testOne()
    testTwo()
    testThree()
    print('All tests passed')