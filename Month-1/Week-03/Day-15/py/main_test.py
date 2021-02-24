from main import anagram

def testOne():
    assert anagram("anagram", "nagaram") == True

def testTwo():
    assert anagram("america", "iracema") == True

def testThree():
    assert anagram("rat", "car") == False

def testFour():
    assert anagram("top", "tip") == False

if __name__ == "__main__":
    testOne()
    testTwo()
    testThree()
    testFour()
    print("All tests passed")