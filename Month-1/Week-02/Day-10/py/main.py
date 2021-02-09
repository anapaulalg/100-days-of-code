# Unique Binary Search Trees

def tress(n):
    if n < 2:
        return 1
    numbers = [0] * (n + 1)
    numbers[0], numbers[1] = 1, 1    
    for i in range(2, n + 1):
        for j in range(0, i):
            numbers[i] += numbers[j]*numbers[i - j - 1]
    return numbers[-1]

print(tress(4))