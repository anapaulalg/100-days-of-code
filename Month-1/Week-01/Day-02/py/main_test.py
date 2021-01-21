from main import findNemo

def test_with_Nemo():
    assert findNemo('I am Nemo') == "I found Nemo at 3"

def test_without_Nemo():
    assert findNemo('I am Dory') == "I can't find Nemo :("

if __name__ == "__main__":
    test_with_Nemo()
    test_without_Nemo()
    print('All tests passed')