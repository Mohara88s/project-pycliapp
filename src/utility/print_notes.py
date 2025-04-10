from utility.colorize import colorize_message

def print_notes(notes):
    
    if len(notes)!=0:
        print('--------------------------------------------------------------------------------')
        for i, note in enumerate(notes):
            print(colorize_message(f"Title:{note.title}", "RED"))
            print(colorize_message(f"Tags:{' '.join(note.tags)}", 'GREEN'))
            print(colorize_message(f"Content:{note.content}", "BLUE"))
            print('--------------------------------------------------------------------------------')
    else: 
        print(colorize_message(f"No notes ", "YELLOW"))


if __name__ == "__main__":
    pass