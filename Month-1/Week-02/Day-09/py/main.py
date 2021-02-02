# Trapping Rain Water

height = [4,2,0,3,2,5]

def rainWater(height):
    for i in height:
        if (i - 1) and (i + 1) > i:
            rainWater = (max(height[0:2])**2) - sum(height[i-1:i+2]) - len(height[0:i+2]) - 1
    print(rainWater)
    return rainWater

rainWater(height)