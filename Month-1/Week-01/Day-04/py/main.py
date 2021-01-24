# Is Johnny Making Progress?

def progressDay(milesperday):
    progressDays = 0
    for i in range(len(milesperday)):
        if len(milesperday) != i+1 and milesperday[i] < milesperday[(i+1)]:
            progressDays = progressDays+1       
    return progressDays        

if __name__ == "__main__":
    milesperday = [3, 4, 1, 2]
    print(progressDay(milesperday))