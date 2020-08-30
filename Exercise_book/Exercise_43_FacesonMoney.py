#!~/anaconda3/bin/python

denom = int(float(input("What is your denomination of money: ")))

#Boring ass implementation, without for loop

if denom == 1:
    face = "George Washington"

elif denom == 2:
    face = "Thomas Jefferson"

elif denom == 5:
    face = "Abraham Lincoln"

elif denom == 10:
    face = "Alexander Hamiliton"

elif denom == 20:
    face = "Andrew Jackson"

elif denom == 50:
    face = "Ulysses S. Grant"

elif denom == 69:
    face = "Ahegao face, noice."

elif denom == 100:
    face = "Benjamin Franklin"

else: 
    print("Your input denomination", str(denom), "is not a note.")
    quit()

print("Your face of freedom for $" + str(denom) + " is", face) #inferior way to format strings, as you have to convert int to str


