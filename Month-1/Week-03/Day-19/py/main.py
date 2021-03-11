# Find the Difference

def difference(s, t):
    if s in t:
        result = t.replace(s,'')

        return result

if __name__ == "__main__":
    s = "ae"
    t = "aea"
    print(difference(s, t))