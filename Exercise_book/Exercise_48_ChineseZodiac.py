#!~/anaconda3/bin/python

year = int(input("Enter a year: "))

remainder = (year - 2008)% 12
#Rat will have remainder of 0
#Ox of 1 and so on...
#Manual math to check: In year 1999, expected to get rabbit. 1999 - 2008 = -9 % 12 = -9
animals = ("Rat", "Ox", "Tiger", "Hare", "Dragon", "Snake", "Horse", "Sheep", "Monkey", "Rooster", "Dog", "Pig")

print(f"Zodiac sign of those born in {year} is {animals[remainder]}.")

#Not doing this shit lol, exploited