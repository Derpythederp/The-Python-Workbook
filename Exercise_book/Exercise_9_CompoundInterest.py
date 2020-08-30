#!~/anaconda3/bin/python
principal= float(input("Stoinks?\n>"))
years= int(input("Years you saving? \n>"))
interest= 0.04

amount=principal
year=0
while year<= years:
    print(f"Projected amount in {year} year(s): ${amount:.2f}")
    amount += amount * interest
    year+=1
    

