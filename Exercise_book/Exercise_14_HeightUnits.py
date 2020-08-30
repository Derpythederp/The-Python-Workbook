#!~/anaconda3/bin/python

feet=int(input("Please enter your height, feet first, followed by inches:"))
inches=int(input())

centimeters= (feet*12+inches)*2.54
print(f"Your height is {centimeters}cm.")
print(f"Your height is {centimeters//100}m and {centimeters%100}cm")