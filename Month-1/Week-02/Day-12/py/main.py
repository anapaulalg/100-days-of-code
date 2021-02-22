# Mountains or Valleys

def landscapeType(landscape):
    ma = max(landscape)
    maIndex = landscape.index(ma)
    mi = min(landscape)
    miIndex = landscape.index(mi)

    if (landscape[0] < landscape[maIndex] > landscape[2]):
        result = "montain"
    elif (landscape[0] > landscape[miIndex] < landscape[2]):
        result = "valley"     
    elif ((landscape[0]) > (landscape[1] and landscape[2])) or ((landscape[2]) > (landscape[0] and landscape[1])):
        result = "Peak cannot be a boundary element"
    else:
        result = "neither"
    return result

if __name__ == "__main__":
    landscape = [3, 5, 3]
    print(landscapeType(landscape))