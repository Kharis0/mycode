#!/usr/bin/env python3
"""kharisZ Research | kharisz.INC Practice
        99 bottles of beer countdown script"""

def bottles_of_beer_countdown(starting_bottles):
    # Loop through the range starting from the user input down to 1 (inclusive), with a step of -1
    for i in range(starting_bottles, 0, -1):
        # Output the current number of bottles on the wall
        print(f"{i} bottles of beer on the wall!")
        
        # Output the current number of bottles, and the action of taking one down and passing it around
        print(f"{i} bottles of beer! You take one down, pass it around!")
        
        # Check if there are no more bottles, and output the appropriate message
        if i - 1 == 0:
            print("No more bottles of beer on the wall!")
        else:
            # Output the remaining bottles on the wall
            print(f"{i - 1} bottles of beer on the wall!")

def main():
    try:
        # Prompt the user to enter the number of bottles, and convert it to an integer
        starting_bottles = int(input("Enter the number of bottles of beer to start the countdown (1-100): "))
        
        # Validate that the input is within the specified range
        if not (1 <= starting_bottles <= 100):
            raise ValueError("Please enter a number between 1 and 100.")
        
        # Call the countdown function with the user's input
        bottles_of_beer_countdown(starting_bottles)
    except ValueError as e:
        # Handle a ValueError (e.g., if the user enters a non-integer or an out-of-range value)
        print(f"Error: {e}")

# Check if the script is run as the main program
if __name__ == "__main__":
    # Call the main function
    main()

