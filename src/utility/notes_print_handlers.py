from utility.colorize import colorize_message

def notes_print(notes):
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
    if len(tags_with_notes)!=0:
        print('--------------------------------------------------------------------------------')
        for tag in tags_with_notes:
            print(tag)
            notes_print(tags_with_notes[tag])
    else: 
        print(colorize_message(f"No tags with notes", "YELLOW"))


if __name__ == "__main__":
    pass