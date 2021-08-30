# favorite number: write a program that prompts the user for a favorite number. use json to store the number in a file
# write a separate program that reads in this value and prints the message "I know your favorite number! It's..."

import json


def get_favorite_number():
    """Function to get the user's favorite number"""

    filename = 'favorite_number.json'
    try:
        favorite_number = int(input("Type your favorite number -> "))
        with open(filename, 'w') as f:
            json.dump(favorite_number, f)
    except IOError:
        print("Error while writing file")
    except ValueError:
        print("Only integer numbers are accepted")
    else:
        print("Number stored successfully")
        return favorite_number


def return_favorite_number():
    """"Function to print the user's favorite number, if exists"""

    get_favorite_number()
    filename = 'favorite_number.json'
    try:
        with open(filename) as f:
            favorite_number = json.load(f)
    except IOError:
        print("Error while reading file")
    else:
        print(f"I know your favorite number! It's {favorite_number}!")


return_favorite_number()
