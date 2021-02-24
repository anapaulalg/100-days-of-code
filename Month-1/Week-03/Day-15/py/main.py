# Valid Anagram

def anagram(s, t):
    if sorted(s) == sorted(t):
        result = True
    else:
        result = False
    return result

if __name__ == "__main__":
    s = "car"
    t = "rac"
    print(anagram(s, t))