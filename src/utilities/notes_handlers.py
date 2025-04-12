from utilities.colorize import colorize_message
from utilities.user_input_handler import user_input_handler

def add_note(args, notes_book):
    print(colorize_message("=== Add a New Note ===", "CYAN"))

    # === Title ===
    while True:
        title = user_input_handler("Enter title: ").strip()
        if not title:
            print(colorize_message("Title cannot be empty.", "RED"))
            continue

        if any(note.title == title for note in notes_book.all_notes()):
            print(colorize_message(f"Note with title '{title}' already exists.", "RED"))
            continue

        break

    # === Content ===
    while True:
        content = user_input_handler("Enter content: ").strip()
        if not content:
            print(colorize_message("Content cannot be empty.", "RED"))
            continue
        break

    # === Tags ===
    tags = []
    while True:
        tag = user_input_handler("Enter a tag: ").strip()
        if not tag:
            print(colorize_message("Tag cannot be empty.", "YELLOW"))
            continue
        if tag in tags:
            print(colorize_message("This tag is already added.", "YELLOW"))
        else:
            tags.append(tag)

        more = user_input_handler("Add another tag? (y/n): ").strip().lower()
        if more != "y":
            break

    if not tags:
        print(colorize_message("You must add at least one tag.", "RED"))
        return

    notes_book.add_note(title, content, tags)
    return colorize_message("Note added successfully!", "GREEN")

def show_note(args, notes_book):
    if not args:
        return colorize_message("Please provide the note title", "RED")

    title = " ".join(args)  # ← зчитує повністю всю назву з args

    for note in notes_book.all_notes():
        if note.title == title:
            return str(note)

    return colorize_message(f"Note with title '{title}' not found.", "YELLOW")


def show_notes(args, notes_book):
    notes = notes_book.all_notes()
    if not notes:
        return colorize_message("No notes available.", "YELLOW")

    sorted_notes = sorted(notes, key=lambda note: note.title.lower())

    result = ""
    for note in sorted_notes:
        result += str(note) + "\n" + "-"*30 + "\n"
    return result

def delete_note(args, notes_book):
    if len(args) < 1:
        return colorize_message("Please provide the note title", "RED")

    title = " ".join(args)  # ← зчитує повністю всю назву з args

    if notes_book.delete_note(title):
        return colorize_message(f"Note '{title}' deleted successfully.", "GREEN")
    else:
        return colorize_message(f"Note '{title}' not found.", "YELLOW")


def edit_note(args, notes_book):
    notes = sorted(notes_book.all_notes(), key=lambda note: note.title.lower())
    if not notes:
        print(colorize_message("No notes to edit.", "YELLOW"))
        return

    while True:
        print("Which note do you want to edit?")
        for idx, note in enumerate(notes, 1):
            print(f"{idx}. {note.title}")
        print(f"{len(notes)+1}. Finish editing")

        try:
            choice = int(user_input_handler("Enter number: "))
            if choice == len(notes) + 1:
                print(colorize_message("You have exited from note editing. Nothing was changed.", "YELLOW"))
                return
            note_to_edit = notes[choice - 1]
            print(f"You have selected {colorize_message(note_to_edit.title, 'YELLOW')}")
            break
        except (ValueError, IndexError):
            print(colorize_message("Note does not exist. Please select a number from the list above.", "RED"))

    new_title = note_to_edit.title
    new_content = note_to_edit.content
    new_tags = note_to_edit.tags[:]

    while True:
        print("\nWhat do you want to edit?")
        print("1. Title")
        print("2. Content")
        print("3. Tags")
        print("4. Finish editing")

        action = user_input_handler("Enter number: ").strip()

        if action == "1":
            print(f"Current title: {new_title}")
            while True:
                temp = user_input_handler("Enter new title: ").strip()
                if not temp:
                    print(colorize_message("Title cannot be empty.", "RED"))
                else:
                    new_title = temp
                    print(f"Your new title is: {colorize_message(new_title, 'YELLOW')}")
                    break

        elif action == "2":
            print(f"Current content: {new_content}")
            while True:
                temp = user_input_handler("Enter new content: ").strip()
                if not temp:
                    print(colorize_message("Content cannot be empty.", "RED"))
                else:
                    new_content = temp
                    print(f"Your new content is: {colorize_message(new_content, 'YELLOW')}")
                    break

        elif action == "3":
            print(f"Current tags: {' '.join(new_tags)}")
            while True:
                temp = user_input_handler("Enter new tags (space separated): ").strip()
                if not temp:
                    print(colorize_message("Tags cannot be empty.", "RED"))
                else:
                    new_tags = list(set(temp.split()))
                    print(f"Your new tags are: {colorize_message(', '.join(new_tags), 'YELLOW')}")
                    break

        elif action == "4":
            break
        else:
            print(colorize_message("Invalid option. Please choose 1, 2, 3 or 4.", "YELLOW"))

    if not new_title.strip() or not new_content.strip() or not any(tag.strip() for tag in new_tags):
        print(colorize_message("Error: title, content and tags must not be empty.", "RED"))
        return

    if new_title != note_to_edit.title:
        if any(n.title == new_title for n in notes_book.all_notes()):
            print(colorize_message(f"Note with title '{new_title}' already exists.", "RED"))
            return

    notes_book.edit_note(note_to_edit.title, new_title, new_content, new_tags)
    print(colorize_message("Note updated successfully.", "GREEN"))


if __name__ == "__main__":
    pass