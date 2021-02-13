# Mountains or Valleys

landscape = [3, 5, 3, 3, 2]

def landscapeType(landscape):
    ma = max(landscape)
    maIndex = landscape.index(ma)
    print(maIndex)

    if (landscape[:maIndex] < ma > landscape[maIndex:]):
        print("montain")
        
    elif (landscape[0] > landscape[1] < landscape[2]):
        print("valley")
    else:
        print("neither")

    return landscapeType

landscapeType(landscape)