from main import progressDay

def threeProgressDays():
    assert countNonVeg([10, 11, 12, 9, 10]) == 3

def oneProgressDays():
    assert countNonVeg([6, 5, 4, 3, 2, 9]) == 1

def zeroProgressDays():
    assert countNonVeg([9, 9]) == 0

if __name__ == "__main__":
    threeProgressDays
    oneProgressDays
    zeroProgressDays
    print('All tests passed')