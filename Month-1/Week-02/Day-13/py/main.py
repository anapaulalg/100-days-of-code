# Need Help With Your Packing?

def CanFit(weighs, bags):
    if (sum(weighs) / bags) <= 10:
        result = True
    else:
        result = False
    return result

if __name__ == "__main__":
    weighs = [5, 4, 3]
    bags = 2
    print(CanFit(weighs, bags))