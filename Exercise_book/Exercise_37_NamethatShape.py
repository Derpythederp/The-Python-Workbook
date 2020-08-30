#!~/anaconda3/bin/python
shape = ["Triangle", "Square", "Pentagon", "Hexagon", "Heptagon", "Octagon", "Nonagon", "Decagon", "Iamgone"]
sides = int(input("Enter number of sides: "))
index = sides - 3
if 3 < sides <= 10:
    """Crucial to have lower limit, else it will still check the first condition and break"""
    print(f"Your shape is a {shape[index]}")
elif sides < 3:
    print("Your shape is a begone. What 2D shape has less than 3 sides? Also a circle is not counted.")
else:
    print(f"Your shape is a {shape[8]}. Ya beat the system, congratulations.")
