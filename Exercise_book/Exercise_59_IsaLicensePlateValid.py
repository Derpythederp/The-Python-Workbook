#!~/anaconda3/bin/python
import re
#Only testing, this problem is better solved with indexing e.g [:3]

user_input = input("Input a license plate: ").upper()

if re.search("[A-Z]{3}[0-9]{3}", user_input):
    print("This is ye ol' type of license plate, she is.")
    
elif re.search("[0-9]{4}[A-Z]{3}", user_input):
    print("This is some fresh license plate number, ma dude.")

else:
    print(" *knock* *knock*\nThis is the traffic police! You're under arrest!")
