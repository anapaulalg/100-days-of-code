# Letter Combinations of a Phone Number

def letterCombinations(firstList, secondList):
    i = 0
    while i < len(firstList):
        j = 0
        while j < len(secondList):     
            result = firstList[i] + secondList[j]
            j += 1 
            print(result)
        i += 1
    return result

if __name__ == "__main__":
    two = ['a', 'b', 'c']
    three = ['d', 'e', 'f']
    four = ['g', 'h', 'i']
    five = ['j', 'k', 'l']
    six = ['m', 'n', 'o']
    seven = ['p', 'q', 'r', 's']
    eight = ['t', 'u', 'v']
    nine = ['w', 'x', 'y', 'z']
    letterCombinations(two, three)