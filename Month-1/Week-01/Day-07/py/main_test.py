from main import merge

def arrays1():
    assert merge([2, 9, 1, 0, 0, 0], [5, 6, 7]) == [1, 2, 5, 6, 7, 9]

def arrays2():
    assert merge([90, 50, 40, 0, 0, 0], [55, 60, 99]) == [40, 50, 55, 60, 90, 99]

if __name__ == "__main__":
    arrays1()
    arrays2()
    print('All tests passed')