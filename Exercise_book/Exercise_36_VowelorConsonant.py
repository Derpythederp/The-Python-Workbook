#!~/anaconda3/bin/python
vowels = ["a", "e", "i", "o", "u"]
letter = input("Letter please. ")
#Overly sanitized
if len(letter) == 1 and not isinstance(int(letter), int):
    if letter in vowels:
        print(f"{letter} is a vowel.")
    elif letter not in vowels and letter == "y":
        print(f"{letter} is sometimes a vowel, and sometimes a consonant.")
    else:
        print(f"{letter} is a consonant")

else:
    print("Oi mate. Play by the rules.")