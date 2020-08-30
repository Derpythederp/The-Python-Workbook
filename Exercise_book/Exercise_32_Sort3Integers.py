#!~/anaconda3/bin/python

#From this exercise onwards, code following PEP standards.
#Minimize whitespace, add whitespace at correct points for readility
#Better code involves santization of input
#Best code has comments for others

a, b, c = input("Enter three digits, delimited by space: ").split(sep=" ")
a, b, c = int(a), int(b), int(c)
mn = min(a, b, c)
mx = max(a, b, c)
mid = a + b + c - mn - mx
print(f""" 
Your sorted values in ascending order are 
1) {mn}
2) {mid}
30 {mx}
""")