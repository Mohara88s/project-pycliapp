# edit_address.py

from utilities.colorize import colorize_message

def edit_address(current_address):
    print(colorize_message(f"Current Address: {current_address}", "YELLOW"))
    new_address = input("Enter new address: ")
    print(colorize_message(f"Address updated to: {new_address}", "GREEN"))
    return new_address
