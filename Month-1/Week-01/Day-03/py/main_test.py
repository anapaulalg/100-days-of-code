from main import countNonVeg, countVeg

def test_NonVeg():
    assert countNonVeg(["--xo--x--ox--", "--xx--x--xx--", "--oo--o--oo--", "--xx--x--ox--", "--xx--x--ox--"]) == 4

def test_Veg():
    assert countVeg(["--xo--x--ox--", "--xx--x--xx--", "--oo--o--oo--", "--xx--x--ox--", "--xx--x--ox--"]) == 1

if __name__ == "__main__":
    test_NonVeg()
    test_Veg()
    print('All tests passed')