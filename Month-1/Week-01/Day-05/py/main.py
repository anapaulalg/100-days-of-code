# Pair of Socks

def numberOfPairs(sockPairs):
    uniqueSocks = []
    for elem in sockPairs:
        if uniqueSocks.count(elem) == 0:
            uniqueSocks.append(elem)

    pairsSocks = 0
    for elem in uniqueSocks:
        socks = sockPairs.count(elem)
        pairsSocks = pairsSocks + int(socks / 2)
    return pairsSocks

if __name__ == "__main__":
    sockPairs = "ABABCA"
    print(numberOfPairs(sockPairs))