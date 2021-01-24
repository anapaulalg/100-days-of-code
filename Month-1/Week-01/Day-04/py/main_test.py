from main import progressDay

def threeProgressDays():
    assert progressDay([10, 11, 12, 9, 10]) == 3

def oneProgressDays():
    assert progressDay([6, 5, 4, 3, 2, 9]) == 1

def zeroProgressDays():
    assert progressDay([9, 9]) == 0

if __name__ == "__main__":
    threeProgressDays()
    oneProgressDays()
    zeroProgressDays()
    print('All tests passed')