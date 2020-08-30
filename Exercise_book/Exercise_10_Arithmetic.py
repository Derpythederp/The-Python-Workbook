#!~/anaconda3/bin/python
import math 
a = int(input("Value of a: \n"))
b = int(input("Value of b: \n"))

sum_of_ab = a+b
difference = a-b
product = a*b
quotient = a//b
remainder = a%b
base_10 = math.log10(a)
a_power_b = a**b

print(f"Sum of a and b: {sum_of_ab}")
print(f"Difference when b is substracted from a: {difference}")
print(f"Product of a and b: {product}")
print(f"Quotient when a is divided by b: {quotient}")
print(f"Remainder when a is divided by b: {remainder}")
print(f"The result of log10a: {base_10}")
print(f"The result of a to power of b: {a_power_b}")

