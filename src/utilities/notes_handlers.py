from utilities.colorize import colorize_message
from utilities.user_input_handler import user_input_handler
from collections import defaultdict


def add_note(args, notes_book):
    """
    Add a new note interactively with title, content, and validated tags.
    Prevents duplicate titles and enforces input validation.
    """
    print(colorize_message("=== Add a New Note ===", "CYAN"))

    while True:
        title = user_input_handler("Enter title: ").strip()
        if not title:
            print(colorize_message("Title cannot be empty.", "RED"))
            continue
        if any(note.title == title for note in notes_book.all_notes()):
            print(colorize_message(f"Note with title '{title}' already exists.", "RED"))
            continue
        break

    while True:
        content = user_input_handler("Enter content: ").strip()
        if not content:
            print(colorize_message("Content cannot be empty.", "RED"))
            continue
        break

    tags = get_validated_tags()
    if not tags:
        return

    notes_book.add_note(title, content, tags)
    return colorize_message("Note added successfully!", "GREEN")

def delete_note(args, notes_book):
    """
    Interactively delete a selected note by title.
    Asks for user confirmation before deletion.
    """
    notes = sorted(notes_book.all_notes(), key=lambda note: note.title.lower())
    if not notes:
        print(colorize_message("No notes to delete.", "YELLOW"))
        return

    while True:
        print("Which note do you want to delete?")
        for idx, note in enumerate(notes, 1):
            print(f"{idx}. {note.title}")
        print(f"{len(notes) + 1}. Cancel")

        try:
            choice = int(user_input_handler("Enter number: "))
            if choice == len(notes) + 1:
                print(colorize_message("Note deletion canceled.", "YELLOW"))
                return

            note_to_delete = notes[choice - 1]
            confirm = user_input_handler(
                f"Are you sure you want to delete '{note_to_delete.title}'? (y/n): ").strip().lower()

            if confirm == "y":
                notes_book.delete_note(note_to_delete.title)
                print(colorize_message(f"Note '{note_to_delete.title}' deleted successfully.", "GREEN"))
            else:
                print(colorize_message("Deletion aborted.", "YELLOW"))
            return

        except (ValueError, IndexError):
            print(colorize_message("Invalid choice. Please select a number from the list above.", "RED"))

def delete_all_notes(args, notes_book):
    """
    Deletes all notes after confirmation from the user.
    """
    notes = notes_book.all_notes()
    if not notes:
        print(colorize_message("There are no notes to delete.", "YELLOW"))
        return

    confirm = user_input_handler("Are you sure you want to delete ALL notes? (y/n): ").strip().lower()
    if confirm == "y":
        notes_book.notes.clear()
        print(colorize_message("All notes deleted successfully.", "GREEN"))
    else:
        print(colorize_message("Deletion of all notes canceled.", "YELLOW"))

def edit_note(args, notes_book):
    """
    Allows interactive editing of an existing note's title, content, or tags.
    Includes full validation and duplicate title prevention.
    """
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
            print(colorize_message("Please select a number from the list above.", "RED"))

    new_title = note_to_edit.title
    new_content = note_to_edit.content
    new_tags = note_to_edit.tags[:]

    while True:
        print("What do you want to edit?")
        print("1. Title")
        print("2. Content")
        print("3. Tags")
        print("4. Finish editing")

        action = user_input_handler("Enter number: ").strip()

        if action == "1":
            while True:
                print(f"Current title: {new_title}")
                temp = user_input_handler("Enter new title: ").strip()
                if not temp:
                    print(colorize_message("Title cannot be empty.", "RED"))
                elif temp.lower() != note_to_edit.title.lower() and any(
                        n.title.lower() == temp.lower() for n in notes_book.all_notes()):
                    print(colorize_message(f"Note with title '{temp}' already exists.", "RED"))
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
            validated_tags = get_validated_tags()
            if validated_tags:
                new_tags = validated_tags
                print(f"Your new tags are: {colorize_message(', '.join(new_tags), 'YELLOW')}")

        elif action == "4":
            break
        else:
            print(colorize_message("Invalid option. Please choose 1, 2, 3 or 4.", "YELLOW"))

    if not new_title.strip() or not new_content.strip() or not any(tag.strip() for tag in new_tags):
        print(colorize_message("Error: title, content and tags must not be empty.", "RED"))
        return

    notes_book.edit_note(note_to_edit.title, new_title, new_content, new_tags)
    print(colorize_message("Note updated successfully.", "GREEN"))

def search_note(args, notes_book):
    """
    Searches for notes based on title, tag, or content.
    Presents interactive options to the user and displays matching results.
    """
    while True:
        print("How would you like to search?")
        print("1. By title")
        print("2. By tag")
        print("3. By tag grupped")
        print("4. By content")
        print("5. Cancel")

        choice = user_input_handler("Enter number: ").strip()

        if choice == "1":
            keyword = user_input_handler("Enter title or part of it: ").strip().lower()
            results = [note for note in notes_book.all_notes() if keyword in note.title.lower()]
        elif choice == "2":
            keyword = user_input_handler("Enter tag or part of it: ").strip().lower()
            results = [
                note for note in notes_book.all_notes()
                if any(keyword in tag.lower() for tag in note.tags)
            ]
        elif choice == "3":
            keyword = user_input_handler("Enter tag or part of it: ").strip().lower()
            tags_with_notes_print(search_and_group_notes_by_tag(keyword, notes_book))
            break
        elif choice == "4":
            keyword = user_input_handler("Enter keyword from content: ").strip().lower()
            results = [note for note in notes_book.all_notes() if keyword in note.content.lower()]
        elif choice == "5":
            print(colorize_message("Search canceled.", "YELLOW"))
            return
        else:
            print(colorize_message("Invalid choice. Please try again.", "RED"))
            continue
        if not results:
            print(colorize_message("No matching notes found.", "YELLOW"))
        else:
            print(colorize_message("Search Results:", "GREEN"))
            print(generate_boxed_notes(results))
        return

def search_and_group_notes_by_tag(q_tag, notes_book):
    tag_to_notes = defaultdict(list)

    for note in notes_book.all_notes():
        for tag in note.tags:
            tag_lower = tag.lower()
            if q_tag in tag_lower:
                tag_to_notes[tag].append(note)

    result = {
        key: sorted(tag_to_notes[key], key=lambda note: note.title.lower())
        for key in sorted(tag_to_notes.keys(), key=str.lower)
    }
    return result

def tags_with_notes_print(tags_with_notes):
    if len(tags_with_notes)!=0:
        print(colorize_message("Search Results:", "GREEN"))
        for i, tag in enumerate(tags_with_notes):
            print(f"     Tag {i+1} : '{tag}' set:")
            print(generate_boxed_notes(tags_with_notes[tag]))
    else: 
        print(colorize_message(f"No tags with notes", "YELLOW"))

def generate_boxed_notes(notes):
    """
    Returns a visually framed and colorized string representation of a list of notes.
    Used for pretty-printing note lists in the terminal.
    """
    if not notes:
        return colorize_message("No notes available.", "YELLOW")

    framed_notes = []
    formatted_notes = []

    for note in notes:
        note_lines = [
            f"Title: {note.title}",
            f"Tags: {' '.join(note.tags)}",
            f"Content: {note.content}"
        ]
        formatted_notes.append(note_lines)

    max_len = max(len(line) for note in formatted_notes for line in note)
    padding = 2
    content_width = max_len + padding * 2

    border = colorize_message("┌" + "─" * content_width + "┐", "WHITE")
    separator = colorize_message("├" + "─" * content_width + "┤", "WHITE")
    bottom = colorize_message("└" + "─" * content_width + "┘", "WHITE")

    framed_notes.append(border)

    for i, note_lines in enumerate(formatted_notes):
        for line in note_lines:
            padded_line = f"{' ' * padding}{line}{' ' * (content_width - len(line) - padding)}"
            colored = colorize_message(padded_line,
                                       "RED" if line.startswith("Title") else
                                       "GREEN" if line.startswith("Tags") else
                                       "CYAN")
            framed_notes.append(f"│{colored}│")
        if i != len(formatted_notes) - 1:
            framed_notes.append(separator)

    framed_notes.append(bottom)

    return "\n".join(framed_notes)

def show_all_notes(notes_book):
    """
    Retrieves and displays all saved notes using a boxed visual format.
    """
    notes = notes_book.all_notes()
    return generate_boxed_notes(notes)

def get_validated_tags():
    """
    Handles interactive input and validation of tags:
    - ensures no duplicates
    - enforces lowercase uniqueness
    - disallows spaces in tag names
    """
    tags = set()
    while True:
        tag = user_input_handler("Enter a tag: ").strip()

        if not tag:
            print(colorize_message("Tag cannot be empty.", "YELLOW"))
        elif " " in tag:
            print(colorize_message("Please add tag without spaces.", "RED"))
        elif tag.lower() in (t.lower() for t in tags):
            print(colorize_message("This tag is already added.", "YELLOW"))
        else:
            tags.add(tag)

        while True:
            more = user_input_handler("Add another tag? (y/n): ").strip().lower()
            if more == "y":
                break
            elif more == "n":
                if not tags:
                    print(colorize_message("You must add at least one tag.", "RED"))
                    continue
                return list(tags)
            else:
                print(colorize_message("Please enter 'y' or 'n'.", "YELLOW"))


if __name__ == "__main__":
    pass
