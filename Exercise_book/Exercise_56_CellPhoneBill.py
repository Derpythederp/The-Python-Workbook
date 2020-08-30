#!~/anaconda3/bin/python

call_time = int(float(input('What is your call air time in minutes in a month?\n> ')))
#round down so I lose money lol
text_msg = int(input("How many messages do you send in a month?\n> "))

call_cost = 0
text_cost = 0
if call_time > 50:
    call_cost = (call_time - 50) * 0.25
if text_msg > 50:
    text_cost = (text_msg - 50) * 0.15

base_charge = 15.00
nine_wan_wan = 0.44
tax = 0.05 * (base_charge + nine_wan_wan + call_cost + text_cost)
total_bill = 1.05 * (base_charge + nine_wan_wan + call_cost + text_cost)

print("Your Statistics:")
print(f"Base charge: ${base_charge:.2f}")
if call_time > 50: print("Additional minutes charge: ${0:.2f}".format(call_cost)) 
if text_msg > 50: print("Additional text message charge: ${0:.2f}".format(text_cost)) 
print(f"911 fee: ${nine_wan_wan:.2f}")
print(f"Tax: ${tax:.2f}")
print(f"Total Bill amount: ${total_bill:.2f}")
print("Thank you for your purchase, don't forget to pay up!")