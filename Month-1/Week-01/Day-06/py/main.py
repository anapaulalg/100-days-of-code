# Next Prime

x = 6

allNumbers = []
y = 1
while y < x - 1:
    y = y + 1
    allNumbers.append(y)
print(allNumbers)

result = [x / elem for elem in allNumbers]
print(result)

floatCount = 0
for elem in result:
    if elem % 2 > 0:
        floatCount = floatCount + 1

isPrime = floatCount == len(result)
print(isPrime)