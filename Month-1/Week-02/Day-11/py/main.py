# Restore IP Addresses

s = "233222777111"

def ipAddresses(s):
    if len(s) < 4:
        print('This cannot be a valid IP')
    else:
        firstPartIP = int(s[:3])
        if firstPartIP <= 255:
            print(str(firstPartIP) + '.')
        else:
            firstPartIP = int(s[:2])
            print(str(firstPartIP) + '.')
        
ipAddresses(s)
firstPartIP = int(s[:3])
secondPartIP = int(s[3:6])
thridPartIP = int(s[6:9])
fourthPartIP = int(s[9:])
print(str(firstPartIP) + '.' + str(secondPartIP) + '.' + str(thridPartIP) + '.' + str(fourthPartIP))