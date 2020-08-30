#!~/anaconda3/bin/python
from math import pi

radius = float(input("Radius of circle:\n>"))
area = pi*radius**2
volume = 4/3*pi*radius**3

print(f"Your circle area of {radius} units is : {area} units squared")
print(f"Your sphere volume of {radius} units is : {volume} units cubed")