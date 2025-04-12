# edit_email.py

from utilities.colorize import colorize_message

def edit_email(current_email):
    print(colorize_message(f"Current Email: {current_email}", "YELLOW"))
    new_email = input("Enter new email: ")
    # Тут можна додати перевірку на правильність email
    print(colorize_message(f"Email updated to: {new_email}", "GREEN"))
    return new_email
