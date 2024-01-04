#!/usr/bin/env python3

def main():
    
    marvelchars= {
    "Starlord":{
        "real name": "peter quill",
        "powers": "dance moves",
        "archenemy": "Thanos"
    },
    "Mystique":{
        "real name": "raven darkholme",
        "powers": "shape shifter",
        "archenemy": "Professor X"
        },
    "Hulk":{
        "real name": "bruce banner",
        "powers": "super strength",
        "archenemy": "adrenaline"
        }
 }

    def get_user_input(prompt):
        return input(prompt).lower()

    def print_character_info(char_name, char_stat, value):
        print(f"{char_name.title()}'s {char_stat} is: {value}")

    
    while True:
        char_name = input("which character do you want to know about? (Starlord, Mistique, Hulk): ")


        if char_name in marvelchars:
            char_stat = input("What statistic do you want to know about? (real name, powers, archenemy): ")


        if char_stat in marvelchars[char_name]:
            value = marvelchars[char_name][char_stat].title()
            print_character_info(char_name, char_stat, value)
        else:
            print("Invalid statistic. Please enter a valid one. ")


        Play_again = input("Do you want to try again? (yes/no): ")
        if play_again != 'yes':
            break
