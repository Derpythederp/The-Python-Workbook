#!~/anaconda3/bin/python

#Out of the goodness of their heart, all inputs are nicely assumed to be santized

pos = input("Enter a chess board position. \n> ")

if bool(int(pos[1]) % 2):
    #if odd
    if bool(ord(pos[0]) % 2) :
        #since ord("a") is 97 and increases from there... we can do modular arithemic too. If odd column, e.g a, c ,e ...
        color = "black"
else:
    color = "white"

print(f"Your square is {color}.")