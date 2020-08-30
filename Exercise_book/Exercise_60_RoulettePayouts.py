#!~/anaconda3/bin/python

from random import randint



red = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]
green = [0, 37]

while True:
    roulette_result = randint(0, 37) #inclusive, 0 is 0 and 37 is 00

    if roulette_result in red:
        rvb = "Red"
    elif roulette_result in green:
        rvb = False
    else:
        rvb = "Black"

    if roulette_result != 0 and roulette_result != 37:
        if bool(roulette_result % 2):
            #If odd
            ove = "Odd"
        else:
            ove = "Even"
    else:
        ove = False

    if 1 <= roulette_result <= 18:
        half = "1 to 18"
    elif 19 <= roulette_result <= 36:
        half = "19 to 36"
    else:
        half = False

    if roulette_result == 37: roulette_result = "00" #My python has an issue with ternary operators i.e roulette_result = "00" if roulette_result == 37


    print(f"The spin resulted in {roulette_result}...")
    if roulette_result != 37 : print(f"Pay {roulette_result}") 
    if rvb : print(f"Pay {rvb}") 
    if ove : print(f"Pay {ove}") 
    if half : print(f"Pay {half}") 

    input("Press Enter key to continue. Cmd or Ctrl + C to exit.\n")