from main import tress

def testOne():
    assert tress(1) == 1

def testTwo():
    assert tress(3) == 5

def testThree():
    assert tress(5) == 42

if __name__ == "__main__":
    testOne()
    testTwo()
    testThree()
    print('All tests passed')