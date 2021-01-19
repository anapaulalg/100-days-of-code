from main import calculateAge

def test_integer_positive_input():
    assert calculateAge(10) == 3650

if __name__ == "__main__":
    test_integer_positive_input()
    print('Test passed')