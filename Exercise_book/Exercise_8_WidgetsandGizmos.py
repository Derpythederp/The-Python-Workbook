#!~/anaconda3/bin/python
widgets = int(input("Enter the number of widgets \n>"))
#Imagine this, a customer comes in fuming because int rounded up the number of widgets due to an accidental click
#The customer now has to pay the weight of a phantom product. Can we get some santisation pls
gizmos = int(input("Enter the number of gizmos \n>"))

total_weight= widgets * 75 + gizmos * 112

print(f"Total weight of order: {total_weight}grams")
