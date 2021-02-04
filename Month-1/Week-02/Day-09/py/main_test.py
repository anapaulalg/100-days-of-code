from main import findWallIndexes, calculateTrappedWater

def testOne():
    assert findWallIndexes, calculateTrappedWater([0,3,0,2,0,4]) == 7

def testTwo():
    assert findWallIndexes, calculateTrappedWater([0,1,0,2,1,0,1,3,2,1,2,1]) == 6

def testThree():
    assert findWallIndexes, calculateTrappedWater([0,1,0,2,1,0,1,3]) == 5

def testFour():
    assert findWallIndexes, calculateTrappedWater([0,1,0,2]) == 1

def testFive():
    assert findWallIndexes, calculateTrappedWater([2,1,0,1,3,2,1,2,1]) == 5

if __name__ == "__main__":
    testOne()
    testTwo()
    testThree()
    testFour()
    testFive()
    print('All tests passed')