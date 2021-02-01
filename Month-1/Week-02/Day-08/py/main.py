# Letter Combinations of a Phone Number

def letterCombinations(firstList, secondList):
    i = 0
    result = []
    while i < len(firstList):
        j = 0
        while j < len(secondList):     
            result.append(firstList[i] + secondList[j]) 
            j += 1 
        i += 1
    print(result)
    return result

if __name__ == "__main__":
    lists = [['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i'], ['j', 'k', 'l'], ['m', 'n', 'o'], ['p', 'q', 'r', 's'], ['t', 'u', 'v'],['w', 'x', 'y', 'z']]
    digit2 = lists[0]
    digit3 = lists[1]
    digit4 = lists[2]
    digit5 = lists[3]
    digit6 = lists[4]
    digit7 = lists[5]
    digit8 = lists[6]
    digit9 = lists[7]
    letterCombinations(digit2, digit3)