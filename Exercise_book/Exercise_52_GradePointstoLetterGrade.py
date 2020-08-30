#!~/anaconda3/bin/python

grade_point = [4.0, 4.0, 3.7, 3.3, 3.0, 2.7, 2.3, 2.0, 1.7, 1.3, 1.0, 0.0]
grade_letter = ["A+", "A", "A-", "B+", "B", "B-", "C+", "C", "C-", "D+", "D", "F"]
points = float(input("Enter grade points: "))

for i in range(len(grade_point)-1):
    if grade_point[i+1] <= points < grade_point[i]:
        grade = grade_letter[i+1]
    elif points < 0:
        grade = "Sm0ll Brian" #Terribly written code.
    elif points > 4.0:
        grade = grade_letter[0]

print(f"Your grade is {grade}.")
        
    