#!~/anaconda3/bin/python

a = input("Length of side 1: ")
b = input("Length of side 2: ")
c = input("Length of side 3: ")

if a == b == c:
    type = "Equilateral"
elif a == b or b == c or a == c: 
    type = "Isoceles"
else:
    type = "Scalene"

print(type, "triangle, it is.")
    