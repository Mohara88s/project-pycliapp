# edit_birthday.py

from utilities.colorize import colorize_message

def edit_birthday(current_birthday):
    print(colorize_message(f"Current Birthday: {current_birthday}", "YELLOW"))
    new_birthday = input("Enter new birthday (DD/MM/YYYY): ")
    # Here you can add a check for the date format
    print(colorize_message(f"Birthday updated to: {new_birthday}", "GREEN"))
    return new_birthday
