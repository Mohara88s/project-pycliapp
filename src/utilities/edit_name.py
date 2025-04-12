# edit_name.py

from utilities.colorize import colorize_message

def edit_name(current_name):
    print(colorize_message(f"Current Name: {current_name}", "YELLOW"))
    new_name = input("Enter new name: ")
    print(colorize_message(f"Name updated to: {new_name}", "GREEN"))
    return new_name
