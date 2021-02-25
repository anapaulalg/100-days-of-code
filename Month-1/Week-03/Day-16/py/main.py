# Nim Game

def nimGame(n):
    if n % 4 != 0:
        result = True
    else:
        result = False
    return result

if __name__ == "__main__":
    n = 4
    print(nimGame(n))