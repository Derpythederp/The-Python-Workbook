#!~/anaconda3/bin/python

note = input("What note from octaves 1 to 9 do you want?  (e.g C4): ")

note_octave4 = {
"C" : 261.63, 
"D" : 293.66,
"E" : 329.63,
"F" : 349.23,
"G" : 392.00,
"A" : 440.00,
"B" : 493.88
}

try:
    note_val, octave = note[0].upper(), int(note[1:])

    note = note_val + str(octave) #convert back to nicely formatted note. 

    if octave == 4:
        frequency = note_octave4[note_val]

    elif 0 < octave < 11:
    #A human can hear 10 octaves only
        frequency = note_octave4[note_val] / 2 ** (4-octave)

    elif octave == 0:
        print(f"Your note, {note}, cannot have an octave of 0")
        frequency = "Null"

    else:
    #if octave is more than 10
        frequency = note_octave4[note_val] / 2 ** (4-octave)
        print (f"Your note {note} is theoretical and cannot be heard by humans.")

    print(f"Your note, {note} has a frequency of {frequency} Hz")

except (ValueError, KeyError):
    #Except note is not an integer, or octave is not found in the dictionary
    print("Yamero! User-sama, note koto nai yo.")


    


    





