from main import letterCombinations

def digitsTwoAndThree():
    assert letterCombinations(lists[0], lists[1]) == ['ad','ae','af','bd','be','bf','cd','ce','cf']

def digitsThreeandFour():
    assert letterCombinations(lists[1], lists[2]) == ['dg', 'dh', 'di', 'eg', 'eh', 'ei', 'fg', 'fh', 'fi']

if __name__ == "__main__":
    lists = [['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i'], ['j', 'k', 'l'], ['m', 'n', 'o'], ['p', 'q', 'r', 's'], ['t', 'u', 'v'],['w', 'x', 'y', 'z']]
    digitsTwoAndThree()
    digitsThreeandFour()
    print('All tests passed')