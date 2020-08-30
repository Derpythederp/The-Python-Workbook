#!~/anaconda3/bin/python

bread = int(input("Bread.\n>"))
price = 3.49
discount = 0.6 #Defining variables helps readability too
discount_price = price * discount
total = bread * price * discount

print(f"""
Regular price per loaf:    ${price:10.2f}
Discounted price per loaf: ${discount_price:10.2f}
Total Price:               ${total:10.2f}
""")

#What this exercise wanted I misunderstood the first time round. What they wanted was to line up the decimal points
#What I thought they wanted was to just format min character count and the 2 decimal points
#Hence the solution needs to be either 1) Multiline like I did 2) 3 Print statements so you can properly line up your decimal points