#!~/anaconda3/bin/python

from math import pi

radius = float(input("Radius of base of cylinder:\n>"))
height = float(input("Height of base of cylinder:\n>"))
volume = pi*radius**2*height

print(f"Your volume of cylinder is: {volume:.1f} units cubed")