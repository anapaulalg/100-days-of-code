# Mountains or Valleys

landscape = [3, 5, 3]

def landscapeType(landscape):
    if (landscape[0] < landscape[1] > landscape[2]):
        print("montain")
    elif (landscape[0] > landscape[1] < landscape[2]):
        print("valley")
    else:
        print("neither")
    return landscapeType

landscapeType(landscape)