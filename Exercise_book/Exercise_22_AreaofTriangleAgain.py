#!~/anaconda3/bin/python

from math import sqrt

side_1 = float(input("Length of side 1 of triangle: "))
side_2 = float(input("Length of side 2 of triangle: "))
side_3 = float(input("Length of side 3 of triangle: "))

s = 0.5*(side_1+side_2+side_3)
area = sqrt(s*(s-side_3)*(s-side_2)*(s-side_1))
print(f"Area of triangle is {area} units squared")
