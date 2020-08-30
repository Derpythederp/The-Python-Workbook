#!~/anaconda3/bin/python
length = float(input ("Length of field in feet\n>"))
width = float(input ("Width of field in feet\n>"))
area_in_feet_sqr = length * width
area_in_acres = area_in_feet_sqr / 43560
print(f"Area of field : {area_in_acres}")