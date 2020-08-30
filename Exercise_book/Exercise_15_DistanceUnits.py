#!~/anaconda3/bin/python

feet= float(input("Your measurement in feet, monsoir...\n>"))

miles=feet//5280
remaining=feet-feet%5280

yards=remaining//3
remaining-=remaining%3

inches=remaining*12

print(f"Your distance in retarded units: {int(miles)} miles, {int(yards)} yards and {int(inches)} inches")
#FUCK YOU USE METRIC UNITS LIKE A NORMAL PERSON!!! IN WHAT BACKWARDS COUNTRY DO YOU NEED TO TORTURE YOURSELF WITH SUCH AN UNINTUITIVE UNIT?
#OH WAIT, FUCKING AMERICA. DOES USING BASE 10 METRICS NOT SEEM EASIER?
#WHAT KIND OF MASOCHIST WOULD PUT THEMSELVES THROUGH THIS SHIT SERIOUSLY!!!