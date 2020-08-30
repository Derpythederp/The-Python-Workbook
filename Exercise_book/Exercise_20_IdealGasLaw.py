#!~/anaconda3/bin/python

pressure = float(input("Pressure in Pascals: "))
volume = float(input("Volume in liters: "))
temperature = float(input("Temperature in degree celsius: ")) + 273.15
ideal_gas_const = 8.314

moles = pressure*volume/ideal_gas_const/temperature/1000
print(f"Number of moles of gas is {moles} mole. ")