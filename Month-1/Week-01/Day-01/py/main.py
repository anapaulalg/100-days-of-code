# Convert Age to Days

def calculateAge(age):
    calcAge = age * 365
    return calcAge

if __name__ == "__main__":    
    yourAge = int(input("What is your age (in years)? "))
    calcAge = calculateAge(yourAge)
    print("Your age in days is: " + str(calcAge))