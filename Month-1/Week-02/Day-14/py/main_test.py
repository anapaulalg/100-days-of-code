from main import encrypt

def testOne():
    assert encrypt("karaca") == "0c0r0kaca"

def testTwo():
    assert encrypt("burak") == "k0r3baca"

def testThree():
    assert encrypt("alpaca") == "0c0pl0aca"

if __name__ == "__main__":
    testOne()
    testTwo()
    testThree()
    print("All tests passed")