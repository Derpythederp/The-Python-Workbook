#!~/anaconda3/bin/python

month, day= input("Enter month and day (e.g February 6) to check if it's a holiday!\n>" ).split(" ")
month = month.title()
day = int(day)

result = "Yes!" #I dun wanna write the result statement 3 times in each check
if month == "January" and day == 1:
    holiday = "New year's day"
elif month == "July" and day == 1:
    holiday  = "Canada day"
elif month == "December" and day == 25:
    holiday = "Christmas day"
else:
    result = "Nah."

print(f"Is it a holiday today? {result}")

if result == "Yes!":
    print(f"Today is {holiday}.")
else:
    print("Back to work I guess... =(")