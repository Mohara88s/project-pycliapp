from utilities.colorize import colorize_message

def notes_print(notes):
    """
    Prints a formatted list of notes with colored titles, tags, and content.
    Each note is separated by a horizontal line.
    """
    if len(notes)!=0:
        print('--------------------------------------------------------------------------------')
        for i, note in enumerate(notes):
            print(colorize_message(f"Title: {note.title}", "RED"))
            print(colorize_message(f"Tags: {' '.join(note.tags)}", 'GREEN'))
            print(colorize_message(f"Content: {note.content}", "BLUE"))
            print('--------------------------------------------------------------------------------')
    else: 
        print(colorize_message(f"No notes", "YELLOW"))

def tags_with_notes_print(tags_with_notes):
    """
    Prints notes grouped by tags. Each tag is listed with its corresponding notes.
    """
    if len(tags_with_notes)!=0:
        print('--------------------------------------------------------------------------------')
        for i, tag in enumerate(tags_with_notes):
            print(f"Tag {i+1} : '{tag}'")
            notes_print(tags_with_notes[tag])
    else: 
        print(colorize_message(f"No tags with notes", "YELLOW"))


if __name__ == "__main__":
    pass
