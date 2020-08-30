#!~/anaconda3/bin/python

grade ={
    "A+" : 4.0,
    "A" : 4.0,
    "A-" : 3.7,
    "B+" : 3.3,
    "B" : 3.0,
    "B-" : 2.7,
    "C+" : 2.3,
    "C" : 2.0,
    "C-" : 1.7,
    "D+" : 1.3,
    "D" : 1.0,
    "F" : 0.0,
}
#Regex Find: (([a-f][-+])|([a-f])) : ([0-9].[0-9])                
#Explanation: I pulled out the " : " out of the test cases (kinda like factorization). This lets me add inverted commas
#Regex replace: "$1" : $4,
# Basically first overarching bracket, $2 and $3 are the or cases inside
#Regex is space sensitive!
#This is to convert if copy pasted from pdf lmao

#Other uses of regex e.g in linux, is to filter and get important info
#e.g RFC 5322 General Email Regex

letter_grade = input("Enter a letter grade: ").upper()
if letter_grade in grade.keys():
    points = grade[letter_grade]
    print(f"Your {letter_grade} is equivalent to {points}.")
else:
    print("You need to enter a valid grade!")
