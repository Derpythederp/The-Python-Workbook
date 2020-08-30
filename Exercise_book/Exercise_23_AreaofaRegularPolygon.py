#!~/anaconda3/bin/python
from math import tan, pi

length = float(input("Length of a side of polygon: "))
sides = int(input("Number of sides: "))
area = sides*length**2/4/tan(pi/sides)
print(f"Area of regular polygon is {area} units squared")

#How they derive the formula is via the fact that polygon area = Sum of triangles = sum(1/2*triangle_base*triangle_height)
# = 1/2*sum_triangle_base*triangle_height = 1/2*perimeter_polygon*apotheum(distance from middle to mid point of one side of polygon)
