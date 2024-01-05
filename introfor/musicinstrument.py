#!/usr/bin/env python3
"""KharisZ | KharisZ.INC Research
   nesting an if-statement inside of a for loop"""

# create a list of strings
instruments = ["Electric guitar", "Bass guitar", "Midi Keyboard", "Acoustic guitar", "Classical guitar", "Drum", "Guitar Amp", "Bass amp", "Maracase"]
# create a second list of strings
approved_instruments = ["Acoustic guitar", "Guitar Amp", "Bass guitar", "Classical guitar"]
# loop across the list instruments
for x in instruments:
    print("\nThe instruments is " + x, end="")   # newline, print current instruments, and end without newline
    if x not in approved_instruments:  # if x does not appear within the list approved_instruments
        print(" - NOT AN APPROVED INSTRUMENT!", end="")
    else:   #if x is in approved instruments
        print(" - APPROVED INSTRUMENT!", end="")

print("\nOur list ended.")  # print when the list has finished
