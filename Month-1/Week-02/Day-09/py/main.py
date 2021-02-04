# Trapping Rain Water

def findWallIndexes(startIndex, data):
    walls = []
    previousValue = 0
    previousIndex = None
    for i in range(startIndex, len(data)):
        if i != 0:
            previousValue = data[previousIndex]
        else:
            previousIndex = i
            if data[i] > 0 and data[i + 1] <= data[i]:
                walls.append(previousIndex)
                continue
        difference = data[i] - previousValue
        previousIndex = i
        if (len(walls) > 0 and  data[i] >= data[walls[-1]]) or difference > 0:
            if (len(walls) > 1 and (walls[-1] == i - 1 or walls[-1] < data[i])):
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

if __name__ == "__main__":
    height = [4,2,0,3,2,5]
    walls = findWallIndexes(0, height)
    result = calculateTrappedWater(height, walls)
    print(result)