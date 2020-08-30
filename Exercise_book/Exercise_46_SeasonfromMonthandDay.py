#!~/anaconda3/bin/python

month = input("Enter a month in FULL NAME: ").title()
day = int(input("Enter a day of the month: "))

months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

#this is almost as bad as yanderedev's coding, you can make a switch with dictionaries like I did previously

if month in months and day <= 31:
    if month == "January" or "February":
        #Technically Feb has only 28 days so this will be a test case one might account for.
        season = "Winter"

    elif month == "March":
        if day < 20:
            season = "Winter"
        else:
            season = "Spring"

    elif month == "April" or "May":
        season = "Spring"

    elif month == "June":
        if day < 21:
            season = "Spring"
        else:
            season = "Summer"

    elif month == "July" or "August":
        season = "Summer"

    elif month == "September":
        if day < 22:
            season = "Summer"
        else:
            season = "Fall"
    
    elif month == "October" or "November":
        season = "Fall"
    
    elif month == "December":
        if day < 21:
            season = "Fall"
        else:
            season = "Winter"
    print(f"The season on {day} {month} is {season}.")

else:
    print("Enter a valid date.")

