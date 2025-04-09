from utility import *
import difflib

def main():
    commands = {
        "hello": {
            "handler": lambda args: print("How can I help you?"),
            "description": "Say hello to the bot"
        },
        "add": {
            "handler": lambda args: print(add_contact(args, book)),
            "description": "Add a new contact or a new phone to the contact in the format [add NAME PHONE]"
        },
        "change-phone": {
            "handler": lambda args: print(change_contact(args, book)),
            "description": "Change contact phone number in the format [change NAME OLD_PHONE NEW_PHONE]"
        },
        "delete-contact": {
            "handler": lambda args: print(delete_contact(args, book)),
            "description": "Delete contact in the format [delete-contact NAME]"
        },
        "phone": {
            "handler": lambda args: print(', '.join(show_phone(args, book))),
            "description": "Show available phone numbers by name in the format [phone NAME]"
        },
        "all": {
            "handler": lambda args: show_all_contacts(get_all_contacts(book)),
            "description": "Show all contacts in detail in the format [all]"
        },
        "add-birthday": {
            "handler": lambda args: print(add_birthday(args, book)),
            "description": "Add date of birth to a contact in the format [add-birthday DD.MM.YYYY]"
        },
        "show-birthday": {
            "handler": lambda args: print(show_birthday(args, book)),
            "description": "Show contact's date of birth in the format [show-birthday NAME]"
        },
        "birthdays": {
            "handler": lambda args: show_birthdays(get_upcoming_birthdays(args, book)),
            "description": "Show upcoming birthdays in the format [birthdays LIMIT_OF_DAYS_UNTIL_BIRTHDAY]"
        },
        "help": {
            "handler": lambda args: show_help(),
            "description": "Show list of available commands in the format [help]"
        },
        "close": {
            "handler": lambda args: print("Good bye!"),
            "description": "Сlose the application in the format [close]"
        },
        "exit": {
            "handler": lambda args: print("Good bye!"),
            "description": "Сlose the application in the format [exit]"
        }
    }
    exit_commands = ["close", "exit"]

    def suggest_command(user_command):
        matches = difflib.get_close_matches(user_command, commands.keys(), n=3, cutoff=0.6)
        print(matches)
        return matches if matches else None
    
    def show_help():
        print("This is available commands:")
        for name, info in commands.items():
            print(f"  {name:<15} - {info['description']}")


    book = load_addressbook()
    print("Welcome to the assistant bot! If this is your first time, type 'help'.")
    while True:
        try:
            command, *args = parse_input(user_input_handler())
            command_data = commands.get(command)
                
            if command in exit_commands:
                command_data["handler"](args)
                save_addressbook(book)
                break

            if command_data:
                command_data["handler"](args)
            else:
                suggestion = suggest_command(command)
                if suggestion:
                    print(colorize_message(f"Unknown command: '{command}'. Did you mean '{' or '.join(suggestion)}'?", "YELLOW"))

                else:
                    print(colorize_message(f"Invalid command: '{command}'. You can try the 'help' command.", "YELLOW"))  
        except Exception as e:
        # Обробка будь-якого винятку
            error_handler(e)
        finally:
            save_addressbook(book)
            

if __name__ == "__main__":
    main()
