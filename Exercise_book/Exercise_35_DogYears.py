#!~/anaconda3/bin/python

hooman = int(float(input("Hooman years: ")))
#Why da fack you see this weird practice of float then int?
#float() is to catch the float e.g 0.5, int() is to round down. 
#If int() alone, will have ValueError as it cannot read strings with point (.) in it

if hooman < 0:
    print("Your bitch is still an unfertilised egg...")
elif hooman <= 2:
    doggo = hooman * 10.5
    print(f"Doggo years: {doggo} years old")
else:
    doggo = 2 * 10.5 + (hooman - 2) * 4
    print(f"Doggo years: {doggo} years old")

