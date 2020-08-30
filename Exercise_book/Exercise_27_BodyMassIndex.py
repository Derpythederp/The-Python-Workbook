#!~/anaconda3/bin/python

#Down with the metrics system!

height = float(input("What is your height in metres?\n>"))
weight = float(input("What is your weight in kilograms?\n>"))

bmi = weight*height**-2
print(f"Your BMI is {bmi}.")