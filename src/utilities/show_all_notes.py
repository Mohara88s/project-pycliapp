from utilities.colorize import colorize_message

def show_all_notes(notes_book):
    notes = notes_book.all_notes()
    if not notes:
        return colorize_message("No notes available.", "YELLOW")

    result = ""
    for note in notes:
        result += (
            colorize_message(f"\nTitle: {note.title}", "RED") + "\n" +
            colorize_message(f"Tags: {' '.join(note.tags)}", "GREEN") + "\n" +
            colorize_message(f"Content: {note.content}", "CYAN") + "\n" +
            "-" * 30 + "\n"
        )
    return result

if __name__ == "__main__":
    pass