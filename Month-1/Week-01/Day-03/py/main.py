# Barbecue Skewers

# skewers = ["--xo--x--ox--", "--xx--x--xx--", "--oo--o--oo--", "--xx--x--ox--", "--xx--x--ox--"]
# --xo--x--ox-- --xx--x--xx-- --oo--o--oo-- --xx--x--ox-- --xx--x--ox--

def countNonVeg(skewers):
    numberOfNonVeg = 0
    for elem in skewers:
        if 'x' in elem:
            numberOfNonVeg = numberOfNonVeg + 1
    return numberOfNonVeg

def countVeg(skewers): 
    numberOfNonVeg = countNonVeg(skewers)       
    numberOfVeg = len(skewers) - numberOfNonVeg
    return numberOfVeg

if __name__ == "__main__": 
    skewers = input("What are the skewers? ").split()
    print("[" + str(countVeg(skewers)) + ", " + str(countNonVeg(skewers)) + "]")