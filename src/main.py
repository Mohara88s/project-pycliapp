from utilities import *
import os

def main():
    commands = {
        "hello": {
            "handler": lambda args: print(colorize_message("How can I help you?", "GREEN")),
            "description": "Greet the bot"
        },
        "add-contact": {
            "handler": lambda args: print(add_contact(args, book)),
            "description": "Add a new contact or a new phone to the contact in the format [add-contact [FIRST_NAME] [LAST_NAME] [PHONE]]"
        },
        "all-contacts": {
            "handler": lambda args: show_all_contacts(get_all_contacts(book)),
            "description": "Show all contacts in details"
        },
        "delete-contact": {
            "handler": lambda args: print(delete_contact(args, book)),
            "description": "Delete contact in the format [delete-contact [FIRST_NAME] [LAST_NAME]]"
        },
        "edit-name": {
            "handler": lambda args: print(edit_name(args, book)),
            "description": "Edit name of a contact in the format [edit-name [OLD_FIRST_NAME] [OLD_LAST_NAME] [NEW_FIRST_NAME] [NEW_LAST_NAME]]"
        },
        "search-contact": {
            "handler": lambda args: handle_search_contact(args, book),
            "description": "Search contacts by: name, phone, birthday, email interactively"
        },
        "phone": {
            "handler": lambda args: print(show_phone(args, book)),
            "description": "Show available phone numbers by name in the format [phone [FIRST_NAME] [LAST_NAME]]"
        },
        "edit-phone": {
            "handler": lambda args: print(change_contact(args, book)),
            "description": "Change contact phone number in the format [edit-phone [FIRST_NAME] [LAST_NAME] [OLD_PHONE] [NEW_PHONE]]"
        },
        "add-birthday": {
            "handler": lambda args: print(add_birthday(args, book)),
            "description": "Add date of birth to a contact in the format [add-birthday [FIRST_NAME] [LAST_NAME] [DD.MM.YYYY]]"
        },
         "edit-birthday": {
            "handler": lambda args: print(edit_birthday(args, book)),
            "description": "Edit birthday of a contact in the format [edit-birthday [FIRST_NAME] [LAST_NAME]] [DD.MM.YYYY]]"
        },
        "birthday": {
            "handler": lambda args: print(show_birthday(args, book)),
            "description": "Show contact's date of birth in the format [birthday [FIRST_NAME] [LAST_NAME]]"
        },
        "birthdays": {
            "handler": lambda args: show_birthdays(get_upcoming_birthdays(args, book)),
            "description": "Show upcoming birthdays in the format [birthdays [LIMIT_OF_DAYS_UNTIL_BIRTHDAY]]"
        },
        "add-email": {
            "handler": lambda args: print(add_email(args, book)),
            "description": "Add email to contact in the format [add-email [FIRST_NAME] [LAST_NAME] [EMAIL]]"
        },
        "edit-email": {
            "handler": lambda args: print(edit_email(args, book)),
            "description": "Edit email of a contact in the format [edit-email [FIRST_NAME] [LAST_NAME] [NEW_EMAIL]]"
        },
        "add-address": {
            "handler": lambda args: print(add_address(args, book)),
            "description": "Add address to contact in the format [add-address [FIRST_NAME] [LAST_NAME] [ADDRESS]]"
        },
        "edit-address": {
            "handler": lambda args: print(edit_address(args, book)),
            "description": "Edit address of a contact in the format [edit-address [FIRST_NAME] [LAST_NAME] [NEW_ADDRESS]]"
        },
        "delete-address": {
            "handler": lambda args: print(delete_address(args, book)),
            "description": "Delete address in the format [delete-address [FIRST_NAME] [LAST_NAME]]"
        },
        "add-note": {
            "handler": lambda args: print(add_note(args, notes_book)),
                "description": "Add note interactively"
        },
        "all-notes": {
            "handler": lambda args: print(show_all_notes(notes_book)),
            "description": "Show all notes"
        },
        "edit-note": {
            "handler": lambda args: edit_note(args, notes_book),
            "description": "Edit note interactively"
        },
        "delete-note": {
            "handler": lambda args: delete_note(args, notes_book),
            "description": "Delete note interactively"
        },
        "delete-all-notes": {
            "handler": lambda args: delete_all_notes(args, notes_book),
            "description": "Delete all notes with confirmation"
        },
        "search-notes": {
            "handler": lambda args: search_note(args, notes_book),
            "description": "Search notes by title, tag, tag grupped or content interactively"
        },
        "help": {
            "handler": lambda args: show_help(commands),
            "description": "Show list of available commands"
        },
        "close": {
            "handler": lambda args: print(colorize_message("Good bye!", "GREEN")),
            "description": "Сlose the application"
        },
        "exit": {
            "handler": lambda args: print(colorize_message("Good bye!", "GREEN")),
            "description": "Сlose the application"
        }
    }

    exit_commands = ["close", "exit"]

    if not os.getenv("ABOT_DEV_MODE") == '1':
        show_banner()

    book = load_addressbook()
    notes_book = load_notes()
    print(colorize_message("Welcome to the assistant bot! If this is your first time, type 'help'.", "GREEN"))

    while True:
        try:
            command, *args = parse_input(user_input_handler('Enter a command: '))
            command_data = commands.get(command)

            if command in exit_commands:
                command_data["handler"](args)
                save_addressbook(book)
                save_notes(notes_book)
                break

            if command_data:
                command_data["handler"](args)
            else:
                suggestion = suggest_command(command, commands)
                if suggestion:
                    print(colorize_message(f"Unknown command: '{command}'. Did you mean '{' or '.join(suggestion)}'?", "YELLOW"))
                else:
                    print(colorize_message(f"Invalid command: '{command}'. You can try the 'help' command.", "YELLOW"))
        
        # Catch all exceptions
        except Exception as e:
            error_handler(e)
        finally:
            save_addressbook(book)
            save_notes(notes_book)

# func to start abot in dev mode
def dev_main():
    os.environ["ABOT_DEV_MODE"] = '1'
    main() 
    
if __name__ == "__main__":
    main()