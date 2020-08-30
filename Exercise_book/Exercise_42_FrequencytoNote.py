#!~/anaconda3/bin/python

frequency = int(float(input("Gimme that frequency in Hz: ")))
dev = 1 #deviation from true value, has to small to be accurate. Will mess up code if beyond around 45 as the for loop will pick first thing

note_octave4 = {
"C" : 261.63, 
"D" : 293.66,
"E" : 329.63,
"F" : 349.23,
"G" : 392.00,
"A" : 440.00,
"B" : 493.88
}

for note, freq in note_octave4.items():
    if frequency - dev < freq < frequency + dev :
        print(f"Your correspondng Octave 4 note to your frequency, {frequency} Hz, is {note}4. It's exact frequency is {freq} Hz.")
        quit()

print(f"Frequency you entered, {frequency} Hz does not correspond to any Octave 4 note.")
        
    
    
