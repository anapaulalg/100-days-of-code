# Trapping Rain Water

height = [4,2,0,3,2,5]

def findWallIndexes(startIndex, data):
    walls = []
    previousValue = 0
    previousIndex = None
    for i in range(startIndex, len(data)):
        if i != 0:
            previousValue = data[previousIndex]
        difference = data[i] - previousValue
        previousIndex = i
        if difference > 0:
            if (len(walls) > 1 and walls[-1] == i - 1):
                walls[-1] = previousIndex
            else:
                walls.append(previousIndex)
        previousIndex = i
    return walls

def calculateTrappedWater(data, walls):
    sum = 0
    previousIndex = None
    for i in range(len(walls)):
        if (previousIndex != None and previousIndex != walls[i]):
            minValue = min([data[walls[i]], data[previousIndex]])
            for j in range(len(data)):
                if (j > previousIndex and j < walls[i]):
                    sum = sum + (minValue - data[j])    
        previousIndex = walls[i]
    return sum

walls = findWallIndexes(0, height)
print(walls)
result = calculateTrappedWater(height, walls)
print(result)