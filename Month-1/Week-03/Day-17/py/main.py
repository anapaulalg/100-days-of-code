# Prison Break

def prisonBreak(prison):
    n = 0
    for i in range(0, len(prison)):
        if i == 0 and prison[i] == 0:
            n = 0
            break
        elif prison[i] == 1:            
            n = n + 1
            prison = [0 if i==1 else 1 for i in prison]
    return n

if __name__ == "__main__":
    prison = [1, 1, 0, 0, 0, 1, 0]
    print(prisonBreak(prison))