from utility.colorize import colorize_message

def add_note(args, notes_book):
    if len(args) < 3:
        raise ValueError("Please provide a title, content (in quotes), and a tag. Format: add-note TITLE \"CONTENT\" TAG")

    title = args[0]
    tag = args[-1]
    content = " ".join(args[1:-1])

    notes_book.add_note(title, content, [tag])
    return colorize_message("Note added successfully!", "GREEN")


def show_note(args, notes_book):
    if len(args) < 1:
        raise ValueError("Please provide the note title")

    title = args[0]
    for note in notes_book.all_notes():
        if note.title == title:
            return str(note)

    return colorize_message(f"Note with title '{title}' not found.", "YELLOW")

def show_notes(args, notes_book):
    notes = notes_book.all_notes()
    if not notes:
        return colorize_message("No notes available.", "YELLOW")
    result = ""
    for note in notes:
        result += str(note) + "\n" + "-"*30 + "\n"
    return result

def delete_note(args, notes_book):
    if len(args) < 1:
        return colorize_message("Please provide the note title", "RED")

    title = args[0]
    if notes_book.delete_note(title):
        return colorize_message(f"Note '{title}' deleted successfully.", "GREEN")
    else:
        return colorize_message(f"Note '{title}' not found.", "YELLOW")

def edit_note(args, notes_book):
    if len(args) < 4:
        return colorize_message("Format: edit-note OLD_TITLE NEW_TITLE \"NEW_CONTENT\" NEW_TAG", "RED")

    old_title = args[0]
    new_title = args[1]

    # Обробка лапок
    if args[2].startswith('"'):
        content_parts = []
        i = 2
        while i < len(args):
            content_parts.append(args[i])
            if args[i].endswith('"'):
                break
            i += 1
        new_content = " ".join(content_parts)[1:-1]  # remove outer quotes
        new_tag = args[i + 1] if i + 1 < len(args) else ""
    else:
        return colorize_message("Content must be in double quotes.", "RED")

    if not new_title.strip() or not new_content.strip() or not new_tag.strip():
        return colorize_message("Title, content, and tag cannot be empty.", "RED")

    notes_book.edit_note(old_title, new_title, new_content, new_tag)
    return colorize_message(f"Note '{old_title}' edited successfully.", "GREEN")

if __name__ == "__main__":
    pass