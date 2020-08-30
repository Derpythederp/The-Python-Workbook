#!~/anaconda3/bin/python
kilo_pascals = float(input("Pressure in kilopascals: "))
ppi = kilo_pascals/6.89475
atm = kilo_pascals/101.325
mm_hg = 760 * atm


print(f"Your pressure has an equivalent of {ppi} ppi, {mm_hg} mm hg and {atm} atm")