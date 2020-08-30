#!~/anaconda3/bin/python

#How int works is that it rounds down every single time (e.g 5.9 to 5)
magnitude_input = float(input("Magnitude of Earthquake to assess damage: "))
magnitude = int(magnitude_input)

#Bypass tedious and slow if-else with switch (switch codes are very non-pythonic)
descriptor = {
    1 : "Micro",
    2 : "Very Minor",
    3 : "Minor",
    4 : "Light",
    5 : "Moderate",
    6 : "Strong",
    7 : "Major",
    8 : "Great",
    9 : "Great",
    10 : "Meteoric"
}

if magnitude < 10:
    description = descriptor[magnitude]
elif magnitude < 0:
    description = "harmless, in fact I can't feel it"
else:
    description = descriptor[10]

print(f"A magnitude {magnitude_input} earthquake is considered to be a {description} earthquake.")