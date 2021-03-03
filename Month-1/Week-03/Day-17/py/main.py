# Prison Break

prison = [1, 1, 0, 0, 0, 1, 0]

def prisonBreak(prison):
    n = 0
    for i in range(0, len(prison)):
        print(i)
        if i == 0 and prison[i] == 0:
            n = 0
            break
        elif prison[i] == 1:            
            n = n + 1
            prison = [0 if i==1 else 1 for i in prison]
            print(prison)
    return n

print(prisonBreak(prison))