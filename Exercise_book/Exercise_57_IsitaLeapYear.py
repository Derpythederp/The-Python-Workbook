#!~/anaconda3/bin/python

year = int(input("Year? \n> "))

leap_year = "not a leap year"
if year % 400 == 0:
    leap_year = "a leap year"
elif year % 100 == 0:
    pass
elif year % 4 == 0:
    leap_year = "a leap year"

print(f"Year {year} is {leap_year}.")