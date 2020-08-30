#!~/anaconda3/bin/python
width= float(input("Input width of room in metres"))
length= float(input("Input length of room in metres"))

try:
    area=width*length
    print(f"Room is {area} metres squared")

except TypeError:
    print("You dirty piece of shit, you have entered a string!!! You've doomed us all!")