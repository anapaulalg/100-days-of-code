# Restore IP Addresses

s = "192333222111"

def ipAddresses(s):
    finalIp = []
    if len(s) < 4:
        return "This cannot be a valid IP"
    else:
        if len(s) == 4:
            for i in s:
                finalIp.append(i)
        else:
            while len(finalIp) < 4:
                segmentSize = 3
                segmentsLeft = 4 - len(finalIp)
                segmentFactor = len(s) / segmentsLeft
                
                if (s[0] == "0"):
                        segmentSize = 1
                else:
                    while segmentSize > len(s) or (segmentFactor <= 1.0 and segmentsLeft > len(s)):
                        segmentSize = segmentSize - 1
                        segmentFactor = segmentsLeft / segmentSize

                ipSegment = int(s[:segmentSize])
                if ipSegment <= 255:
                    finalIp.append(str(ipSegment))
                    s = s[segmentSize:]
                else:
                    ipSegment = int(s[:2])
                    finalIp.append(str(s[:segmentSize - 1]))
                    s = s[segmentSize - 1:]
                
    return ".".join(finalIp)
            
print(ipAddresses(s))