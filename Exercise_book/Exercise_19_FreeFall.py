#!~/anaconda3/bin/python

from math import sqrt

height = float(input("Height object is dropped from in metres \n>"))
init_speed = 0
accel = 9.8

final_speed = sqrt(init_speed**2+2*9.8*height)
print(f"Final speed of object upon impact is: {final_speed} m/s")