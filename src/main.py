from utilities import *

def main():
    commands = {
        "hello": {
            "handler": lambda args: print("How can I help you?"),
            "description": "Greet the bot"
        },
        "add-contact": {
            "handler": lambda args: print(add_contact(args, book)),
            "description": "Add a new contact or a new phone to the contact in the format [add-contact [NAME] [PHONE]]"
        },
        "all-contacts": {
            "handler": lambda args: show_all_contacts(get_all_contacts(book)),
            "description": "Show all contacts in detail in the format [all-contacts]"
        },
        "delete-contact": {
            "handler": lambda args: print(delete_contact(args, book)),
            "description": "Delete contact in the format [delete-contact [NAME]]"
        },
        "edit-name": {
            "handler": lambda args: print(edit_name(args, book)),
            "description": "Edit name of a contact in the format [edit-name [OLD_NAME] [NEW_NAME]]"
        },
        "search-contact": {
            "handler": lambda args: handle_search_contact(args, book),
            "description": "Search contacts by: name, phone, birthday, emailin the format [search-contact] for interactive mode"
        },
        "phone": {
            "handler": lambda args: print(', '.join(show_phone(args, book))),
            "description": "Show available phone numbers by name in the format [phone [NAME]]"
        },
        "edit-phone": {
            "handler": lambda args: print(change_contact(args, book)),
            "description": "Change contact phone number in the format [edit-phone [NAME] [OLD_PHONE] [NEW_PHONE]]"
        },
        "add-birthday": {
            "handler": lambda args: print(add_birthday(args, book)),
            "description": "Add date of birth to a contact in the format [add-birthday [NAME] [DD.MM.YYYY]]"
        },
         "edit-birthday": {
            "handler": lambda args: print(edit_birthday(args, book)),
            "description": "Edit birthday of a contact in the format [edit-birthday [NAME] [DD.MM.YYYY]]"
        },
        "birthday": {
            "handler": lambda args: print(show_birthday(args, book)),
            "description": "Show contact's date of birth in the format [birthday [NAME]]"
        },
        "birthdays": {
            "handler": lambda args: show_birthdays(get_upcoming_birthdays(args, book)),
            "description": "Show upcoming birthdays in the format [birthdays [LIMIT_OF_DAYS_UNTIL_BIRTHDAY]]"
        },
        "add-email": {
            "handler": lambda args: print(add_email(args, book)),
            "description": "Add email to contact in the format [add-email [NAME] [EMAIL]]"
        },
        "edit-email": {
            "handler": lambda args: print(edit_email(args, book)),
            "description": "Edit email of a contact in the format [edit-email [NAME] [NEW_EMAIL]]"
        },
        "add-address": {
            "handler": lambda args: print(add_address(args, book)),
            "description": "Add address to contact in the format [add-address [NAME] [ADDRESS]]"
        },
        "edit-address": {
            "handler": lambda args: print(edit_address(args, book)),
            "description": "Edit address of a contact in the format [edit-address [NAME] [NEW_ADDRESS]]"
        },
        "delete-address": {
            "handler": lambda args: print(delete_address(args, book)),
            "description": "Delete address in the format [delete-address [NAME]]"
        },
        "add-note": {
            "handler": lambda args: print(add_note(args, notes_book)),
                "description": "Add a note [add-note \"[TITLE]\" \"[CONTENT]\" [TAG1 TAG2 ...]]"
        },
        "note": {
            "handler": lambda args: print(show_note(args, notes_book)),
            "description": "Show note by title in the format [note [TITLE]]"
        },
        "all-notes": {
            "handler": lambda args: print(show_all_notes(notes_book)),
            "description": "Show all notes in the format [all-notes]"
        },
        "edit-note": {
            "handler": lambda args: print(edit_note(args, notes_book)),
            "description": "Edit note in the format [edit-note \"[OLD_TITLE]\" \"[NEW_TITLE]\" \"[NEW_CONTENT]\" [TAG1 TAG2 ...]]"
        },
        "delete-note": {
            "handler": lambda args: print(delete_note(args, notes_book)),
            "description": "Delete note by title in the format [delete-note [TITLE]]"
        },
        "search-note": {
            "handler": lambda args: notes_print(search_notes(args, notes_book)),
            "description": "Search notes by title, tags or query in the format [search-note title: TITLE] or [search-note tags: TAGS] or [search-note QUERY]"
        },
        "search-notes-by-tag": {
            "handler": lambda args: tags_with_notes_print(search_and_group_notes_by_tag(args, notes_book)),
            "description": "Search sorted tags which are similar to query and connectet to them notes in the format [search-notes-by-tag QUERY]"
        },
        "help": {
            "handler": lambda args: show_help(commands),
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

    book = load_addressbook()
    notes_book = load_notes()
    print("Welcome to the assistant bot! If this is your first time, type 'help'.")

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

if __name__ == "__main__":
    main()