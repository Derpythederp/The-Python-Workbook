#!~/anaconda3/bin/python
from random import randint

#sound_level = int(float(input("Enter decibel: ")))

running = True

while running:
    """Main loop"""
    sound_level = randint(0,170)

    #dictionary defining all items and corresponding volumes. Better than using a 2D list to store item followed by value
    noise_dict = {"Jackhammer" : 130, "Gas Lawnmower" : 106, "Alarm clock" : 70, "Quiet room" : 40}

    if sound_level in noise_dict.values():
        for key, value in noise_dict.items():
            if sound_level == value:
                print(f"Your sound level, {sound_level} dB, is as loud as a {key}.")
    elif sound_level < 40:
        print(f"You can't even hear this message. {sound_level} dB is too soft...")
    elif sound_level > 130:
        print(f"What? I can't hear you!!! {sound_level} dB is too loud!")

    else:
        if 40 < sound_level < 70:
            print(f"Sound level, {sound_level} dB, is between Quiet room and Alarm Clock")
        elif 70 < sound_level < 106:
            print(f"Sound level, {sound_level} dB, is between Alarm Clock and Gas Lawnmower")
        elif 106 < sound_level < 130:
            "Sound level, {sound_level} dB, is between Gas Lawnmower and Jackhammer"

    run = input("Do you want to continue? y/n\n>")

    if run.lower() == "n":
        running = False

quit()