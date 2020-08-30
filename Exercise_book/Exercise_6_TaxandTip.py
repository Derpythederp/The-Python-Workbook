#!~/anaconda3/bin/python
cost_meal=float(input("Price of meal\n>"))
#Man these are some santised inputs. Oh geez I wonder if I can't exploit this
tax = cost_meal*0.07
tip = cost_meal*0.18

grand_total= tax + tip + cost_meal

print("Your grand total is: ${:.2f}".format(grand_total))
