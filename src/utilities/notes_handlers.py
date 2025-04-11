from utilities.colorize import colorize_message

def add_note(args, notes_book):
    if len(args) < 3:
        raise ValueError("Please provide a title, content, and at least one tag. Format: add-note \"TITLE\" \"CONTENT\" TAG1 TAG2 ...")

    # === Витягуємо TITLE у подвійних лапках ===
    if args[0].startswith('"'):
        title_parts = []
        i = 0
        while i < len(args):
            title_parts.append(args[i])
            if args[i].endswith('"') and len(args[i]) > 1:
                break
            i += 1
        title = " ".join(title_parts).strip('"').strip("'")
        args = args[i + 1:]
    else:
        raise ValueError("Title must be in double quotes.")

    # === Витягуємо CONTENT у подвійних лапках ===
    if not args or not args[0].startswith('"'):
        raise ValueError("Content must be in double quotes.")

    content_parts = []
    i = 0
    while i < len(args):
        content_parts.append(args[i])
        if args[i].endswith('"') and len(args[i]) > 1:
            break
        i += 1
    content = " ".join(content_parts).strip('"').strip("'")
    remaining = args[i + 1:]

    # === Витягуємо TAG-и (унікальні, без дублікатів) ===
    tags = list(set(remaining)) if remaining else []

    if not title.strip() or not content.strip() or not tags:
        raise ValueError("Title, content, and tags cannot be empty.")

    # === Перевірка на унікальний тайтл ===
    for note in notes_book.all_notes():
        if note.title == title:
            raise ValueError(f"Note with title '{title}' already exists.")

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

from utilities.colorize import colorize_message

from utilities.colorize import colorize_message

def edit_note(args, notes_book):
    if len(args) < 4:
        return colorize_message("Format: edit-note \"OLD_TITLE\" \"NEW_TITLE\" \"NEW_CONTENT\" TAG1 TAG2 ...", "RED")

    def extract_quoted_value(arguments):
        parts = []
        i = 0
        while i < len(arguments):
            parts.append(arguments[i])
            if arguments[i].endswith('"') and len(arguments[i]) > 1:
                break
            i += 1
        value = " ".join(parts).strip('"').strip("'")
        remaining = arguments[i + 1:]
        return value, remaining

    # === OLD TITLE ===
    if not args[0].startswith('"'):
        return colorize_message("OLD_TITLE must be in double quotes.", "RED")
    old_title, args = extract_quoted_value(args)

    # === NEW TITLE ===
    if not args or not args[0].startswith('"'):
        return colorize_message("NEW_TITLE must be in double quotes.", "RED")
    new_title, args = extract_quoted_value(args)

    # === NEW CONTENT ===
    if not args or not args[0].startswith('"'):
        return colorize_message("NEW_CONTENT must be in double quotes.", "RED")
    new_content, args = extract_quoted_value(args)

    # === TAGS ===
    new_tags = list(set(args)) if args else []

    if not new_title.strip() or not new_content.strip() or not any(isinstance(tag, str) and tag.strip() for tag in new_tags):
        return colorize_message("Title, content, and tags cannot be empty.", "RED")

    try:
        notes_book.edit_note(old_title, new_title, new_content, new_tags)
        return colorize_message(f"Note '{old_title}' edited successfully.", "GREEN")
    except Exception as e:
        return colorize_message(str(e), "RED")

if __name__ == "__main__":
    pass