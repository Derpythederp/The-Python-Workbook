#!~/anaconda3/bin/python

#Normal number of days in a month - 31 days
normal = ["january", "march", "april", "may", "june", "july", "august", "september", "october", "november", "december"]
month = input("Enter a month in full name: ").lower()

if month == "february":
    print("February can have 28 or 29 days.")
elif month in normal:
    print(f"{month.title()} has 31 days.")
else:
    print(f"I don't think {month} is even a month, or you didn't type the FULL NAME of the month.")