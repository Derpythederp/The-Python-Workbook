#!~/anaconda3/bin/python

#An alternative solution is to use NumPy (don't reinvent the wheel + faster due to c)
'''
import numpy as np
#assume uer has entered values for a b and c here
quadratic = np.poly1d ([a, b, c])


threshold = 1e-5 #to account for numpy algorithm error when calculating roots
real_num = quadratic.r[abs(r.imag < threshold)]
#take quadratic roots, take real elements by checking for imaginary value < threshold to account for algorithm
#Numpy can index by rule

num_real = real_num.shape[0] #can use len() here, gets no. of col
coeff_count = len(quadratic.c) #use of len() instead of shape, since 1d array. c attribute is coefficients
num_imag = coeff_count - num_real

print(f"{quadratic} equation has roots {quadratic.r[0]} and {quadratic.r[1]}") #r is a built in attribute of poly1d classes
print(f"Equation has {num_imag} imaginary roots and {num_real} real roots.")
'''



'''
#alternative 2 which is pretty smart, assuming you want to use the function
pm = np.array([+1,-1]) #only np arrays can do parallel calculations you see later
root1, root2 = (-b + pm * sqrt(b ** 2 - 4 * a * c)) / 2 / a 
discriminant = sqrt (b ** 2 - 4 * a * c)

#if part is almost the same as below
'''


from math import sqrt

a = float(input("Coefficient of x square: "))
b = float(input("Coefficient of x: "))
c = float(input("Coefficient of constant: "))

#lambda are anonymous functions, choice for this is readability and so I dun have to make redundant code.
root = lambda a, b, c, pm : (-b + pm * sqrt(b ** 2 - 4 * a * c)) / 2 / a #pm is plus minus
discriminant = lambda a, b, c: b ** 2 - 4 * a * c 

eqn_discrim = discriminant(a, b, c)
if eqn_discrim < 0:
    print("There are no real roots.")
elif eqn_discrim == 0:
    print(f"There is 1 root.\nThe root is {root(a, b, c, 1)}")
else:
    print(f"There are 2 roots.\nThe roots are {root(a, b, c, 1):.5f} and {root(a, b, c, -1):.5f}")

#I redesigned this code at some point because I was thinking too hard and wanted to calculate even the complex numbers. 
#This was not part of the objectives and sqrt kept giving me a ValueError (apparenly it can't output complex no.)
#tl;dr Keep your thinking simple.