#!~/anaconda3/bin/python
air_temp = float(input("What is the air temperature in degree celsius: "))
wind_speed = float(input("What is the wind speed in km/h: "))
wci = 13.12+0.6215*air_temp-11.37*wind_speed**0.16+0.3965*air_temp*wind_speed**0.16
print(f"Wind Chill Index is {wci}.")