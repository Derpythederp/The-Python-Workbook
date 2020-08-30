#!~/anaconda3/bin/python
wavelength = int(input("Enter wavelength in nm: "))

color_nm = {
"Violet": [380, 450],
"Blue": [450, 495],
"Green": [495, 570],
"Yellow": [570, 590],
"Orange": [590, 620],
"Red": [620, 751]
}
if 380 <= wavelength <= 750:
    for color, rnge in color_nm.items():
        if rnge[0] <= wavelength < rnge[1]:
            colour = color
    print(f"At {wavelength:.1f} nm, color of light is {colour}.")
else:
    print("Wavelength is outside of visible spectrum")

