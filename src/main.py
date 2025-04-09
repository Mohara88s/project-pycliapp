from utility import *
from utility.search_contacts import search_contacts
from colorama import Fore, init
import difflib

init(autoreset=True)
commands = ["hello","add","change","delete","phone","all","add-birthday","show-birthday","birthdays","close", "exit","search"]

def suggest_command(user_command):
    matches = difflib.get_close_matches(user_command, commands, n=1, cutoff=0.6)
    return matches[0] if matches else None

def main():
    book = load_addressbook()
    print("Welcome to the assistant bot! This is available commands:")
    print(f'{', '.join(commands)}')
    while True:
        try:
            command, *args = parse_input(user_input_handler())
            if command in ["close", "exit"]:
                save_addressbook(book)
                print("Good bye!")
                break
            elif command == "hello":
                print("How can I help you?")
            elif command == "add":
                print(add_contact(args, book))
            elif command == "change":
                print(change_contact(args, book))
            elif command == "delete":
                print(delete_contact(args, book))
            elif command == "phone":
                print(', '.join(show_phone(args, book)))
            elif command == "all":
                show_all_contacts(get_all_contacts(book))
            elif command == "add-birthday":
                print(add_birthday(args, book))
            elif command == "show-birthday":
                print(show_birthday(args, book))
            elif command == "birthdays":
                show_birthdays(get_upcoming_birthdays((book)))
            elif command == "search":
                print(search_contacts(args, book))
            else:
                suggestion = suggest_command(command)
                if suggestion:
                    print(colorize_message(f"Unknown command: '{command}'. Did you mean '{suggestion}'?", "YELLOW"))

                else:
                    print(colorize_message(f"Invalid command: '{command}'.", "YELLOW"))  
        except Exception as e:
        # Обробка будь-якого винятку
            error_handler(e)
        finally:
            save_addressbook(book)
            

if __name__ == "__main__":
    main()
