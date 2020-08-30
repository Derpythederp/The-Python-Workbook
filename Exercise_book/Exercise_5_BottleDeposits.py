#!~/anaconda3/bin/python
"""I assume they don't want the fancy implementation with len() and if statements.
Im dumbing down my response
"""


liter_less=int(input("Enter the number of bottles you have less than or equal to 1 liter\n>"))
liter_more=int(input("Enter the number of bottles you have more than 1 liter\n>"))
#The style of code above is susceptible to attacks so do use a try except.
refund = 0.10 * liter_less + liter_more * 0.25
print("Here's your fucking money : ${0:.2f}".format(refund))


"""In case you were wondering,

Syntax of .format :
"{}".format()
"{0}".format()


Syntax of special format options:
"{0:.2f}".format(item_1) - Put item_1 for string sub, but format such that 2 floating numbers. 
Colon is needed else item_1 is read as a class object

"{:12}".format(item_2) - Align the output 12 spaces to right by padding with space. 
E.g item_2 is 10
Output:
          10


"""