# Restore IP Addresses

s = "2600"

if len(s) < 4:
    print('This cannot be a valid IP')

ip = int(s[:3])
if ip <= 255:
    print(ip)
else:
    ipSmall = int(s[:2])
    print(ipSmall)