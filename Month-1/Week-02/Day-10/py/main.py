# Unique Binary Search Trees

def tress(self, n):
    if n < 2:
        return 1
    numbers = [0] * (n + 1)
    numbers[0], numbers[1] = 1, 1    
    for i in range(2, n + 1):
        for j in range(0, i):
            numbers[i] += numbers[j]*numbers[i - j - 1]
    return numbers

print(tress(1, 4))