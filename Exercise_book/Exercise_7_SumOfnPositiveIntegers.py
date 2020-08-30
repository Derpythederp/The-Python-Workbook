#!~/anaconda3/bin/python
n = abs(int(input("Positive integer pls\n>")))
#abs is just for santisation

sum = n * (n+1) // 2 #The divison is cos it's more satisfying

print(f"Sum of integers from 1 to n is {sum}")
