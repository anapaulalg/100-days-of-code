from main import ipAddresses

def testOne():
    assert ipAddresses("233") == "This cannot be a valid IP"

def testTwo():
    assert ipAddresses("1234") == "1.2.3.4"

def testThree():
    assert ipAddresses("25525511135") == "255.255.111.35"

def testFour():
    assert ipAddresses("255011135") == "255.0.111.35"

if __name__ == "__main__":
    testOne()
    testTwo()
    testThree()
    testFour()
    print("All tests passed")