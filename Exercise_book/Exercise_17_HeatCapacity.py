#!~/anaconda3/bin/python
from time import sleep
mass_water = float(input("How much water are you heating in ml?\n>"))
final_temp = float(input("What temperature do you want your water to be in Celsius?\n>"))
room_temp = 25.0
temp_change = final_temp-room_temp

total_energy = mass_water*4.186*temp_change

print("Getting room temperature...")
sleep(1)
print(f"Room temperature acquired! Temperature is {room_temp} degree celsius")

if total_energy<0:
    print(f"Energy to lose: {abs(total_energy)}J")
else:
    print(f"Energy to gain: {total_energy}J")

cost_per_kwh = 8.9
total_energy_kwh=total_energy/3600/10**3
print(f"To heat {mass_water}ml of water, it will cost you {cost_per_kwh*total_energy_kwh} cents.")
