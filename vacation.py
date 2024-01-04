#!/usr/bin/env python3

 print("How many years have you been an employee: ")
 emyears = int(input() ) # emyears is integer input input from user

if emyears >= 30:
    vacadays = emyears * 3
elif emyears >= 20:
    vacadays = emyears * 2
elif emyears >= 10:
    vacadays = emyears * 1.5
else: # this could be read, "in all other cases"
    vacadays = emyears * 1
print('You have ', vacadays, ' vacation days.')
