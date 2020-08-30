#!~/anaconda3/bin/python
#you can scum the whole exercise with time module as well as the next. But this code isn't hard

days = int(input("Enter the number of days, followed by hours, minutes and seconds.\nDays: "))
hours = int(input("Hours: "))
minutes = int(input("Minutes: "))
seconds = int(input("Seconds: "))

total_seconds = days*60*60*24+hours*60*60+minutes*60+seconds
print(f"{total_seconds} seconds has passed...")