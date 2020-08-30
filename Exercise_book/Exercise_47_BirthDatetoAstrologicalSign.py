#!~/anaconda3/bin/python

#FUCKING HELL, this would have been worse with only if statements due to readbility

#dictionary format [[from], [to]]     where [from] and [to] are in [mm,dd]
#dictionary doesn't provide any more advantages in terms of speed than a tuple, I can't use a key-value system after all.
zodiac_dict = {
"Capricorn" : [[12, 22], [1, 19]],
"Aquarius" : [[1, 20], [2, 18]],
"Pisces" : [[2, 19], [3, 20]],
"Aries" : [[3, 21], [4, 19]],
"Taurus" : [[4, 20], [5, 20]],
"Gemini" : [[5, 21], [6, 20]],
"Cancer" : [[6, 21], [7, 22]],
"Leo" : [[7, 23], [8, 22]],
"Virgo" : [[8, 23], [9, 22]],
"Libra" : [[9, 23], [10, 22]],
"Scorpio" : [[10, 23], [11, 21]],
"Sagittarius" : [[10, 22], [12, 21]]
}

#This one actually reaps benefit of dictionary, as it's faster to get value from key ( O(1) ).
months = {
"January" : 1, 
"February" : 2, 
"March" : 3, 
"April" : 4, 
"May" : 5, 
"June" : 6, 
"July" : 7, 
"August" : 8, 
"September" : 9,
"October" : 10, 
"November" : 11, 
"December": 12}

month = months[input("Month of birth in FULL NAME (e.g January): ").title()]
day = int(input("Day of birth (e.g 31): "))

for zodiac_sign, date_range in zodiac_dict.items():
    if month == date_range[0][0]:
        #if month lies within this month, move on. This is the first month in the range and counts till end of month 
        if date_range[0][1] <= day <= 31:
            zodiac = zodiac_sign

    elif month == date_range[1][0]:
        #if month lies within this month, move on.  This is the second month in the range and counts from start of month
        if 1 <= day <= date_range[1][1]:
            zodiac = zodiac_sign
    

print(f"Your zodiac sign is {zodiac}.")

