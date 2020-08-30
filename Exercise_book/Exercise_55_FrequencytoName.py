#!~/anaconda3/bin/python

frequency = float((input("Frequency in Hz (e.g 2.1e+17): ")))

if 0 < frequency < (3 * 10 ** 9):
    name = "radio waves"
elif (3 * 10 ** 9) <= frequency < (3 * 10 ** 12):
    name = "microwaves"
elif (3 * 10 ** 12) <= frequency < (4.3 * 10 ** 14):
    name = "infrared light"
elif (4.3 * 10 ** 14) <= frequency < (7.5 * 10 ** 14):
    name = "visible light"
elif (7.5 * 10 ** 14) <= frequency < (3 * 10 ** 17):
    name = "ultraviolet light"
elif (3 * 10 ** 17) <= frequency < (3 * 10 ** 19):
    name = "x-rays"
elif frequency > (3 * 10 ** 19):
    name = "gamma rays"
else:
    print(f"You're stepping into the realm of antimatter, where no mortal made of matter has ever treaded...")

print (f"{frequency} Hz is a type of {name}")