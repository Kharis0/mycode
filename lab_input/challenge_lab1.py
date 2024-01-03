#!/usr/bin/env python3
"""Kharis Research | KharisZ.Inc
   print() - concatenate vs print a series of items"""

def main():

    # collect string input from the user name
    user_name = input("What is your name? ")

    # Collect string input asking what day of the week it is.
    week_day = input("What day of the week is it? ")

    ## the line below creates a single string that is passed to print()
    print(f'Hello,{user_name}!   Happy  {week_day}!')


main()
