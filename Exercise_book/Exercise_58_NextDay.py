#!~/anaconda3/bin/python

year = int(input("Year? yyyy \n> "))
month = int(input("Month? mm \n> "))
day = int(input("Day? dd\n> "))

special_months = [4, 6, 9, 11] #30 days, February has its own check

leap_year = False
if year % 400 == 0:
    leap_year = True
elif year % 100 == 0:
    pass
elif year % 4 == 0:
    leap_year = True

next_day = day
next_month = month
next_year = year
if month in special_months:
    if day >= 30:
        next_day = 1
        next_month = month + 1

elif month == 2:
    if leap_year:
        if day >= 28:
            next_day = 1
            next_month = month + 1
            
    elif not leap_year:
        if day >= 29:
            next_day = 1
            next_month = month + 1
elif month >= 12:
    if day >= 31:
        next_day = 1
        next_month = 1
        next_year = year + 1

else:
    if day >= 31:
        next_day = 1
        next_month = month + 1
    else:
        next_day = day + 1


#Code can be killed by inputs larger than what is valid, for example 32 for days in year, while still increment month

print(f"Tomorrow's date is {next_year}-{next_month}-{next_day}")