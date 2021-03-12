from main import difference

def testOne():
    assert difference("abcd", "abcde") == "e"

def testTwo():
    assert difference("", "y") == "y"

def testThree():
    assert difference("a", "ax") == "x"

if __name__ == "__main__":
    testOne()
    testTwo()
    testThree()
    print("All tests passed")