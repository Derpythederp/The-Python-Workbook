#!~/anaconda3/bin/python

penny = 1
nickel = 5
dime = 10
quarter = 25
loony = 100
toony = 200

cents= int(input("How much change do you need in cents? \n>"))
#Don't think too hard, this isn't knapsack. This only has the value of the item, not the cost of carrying the item as well
print(f"Toonies : {cents//toony}")
remainder = cents%toony

print(f"Loonies : {remainder//loony}")
remainder = remainder%loony

print(f"Quarters : {remainder//quarter}")
remainder = remainder%quarter

print(f"Dimes : {remainder//dime}")
remainder = remainder%dime

print(f"Nickels : {remainder//nickel}")
remainder = remainder%nickel

print(f"Pennies : {remainder//penny}")
remainder = remainder%penny
