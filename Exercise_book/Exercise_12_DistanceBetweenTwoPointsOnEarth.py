#!~/anaconda3/bin/python
from math import radians, acos, sin, cos

#radians break the pretty formatting below, but math module works off of radians
lat_1 = radians(float(input("Latitude of Point 1: ")))
long_1 = radians(float(input("Longitude of Point 1: ")))
lat_2 = radians(float(input("Latitude of Point 2: ")))
long_2 = radians(float(input("Longitude of Point 2: ")))

distance = 6371.01*acos(sin(lat_1)*sin(lat_2)+cos(lat_1)*cos(lat_2)*cos(long_1-long_2))
print(f"Distance between point ({lat_1}, {long_1}) and point ({lat_2}, {long_2}) is {distance}km.")