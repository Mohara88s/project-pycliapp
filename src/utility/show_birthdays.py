from utility.colorize import colorize_message

def show_birthdays(birthdays):
    if len(birthdays)!=0:
        print(colorize_message(f"{"Name":<20}{"Birthday":<15}", "MAGENTA"))
        for i, contact in enumerate(birthdays):
            print(colorize_message(f"{contact.name:<20}{contact.birthday}", f"{"CYAN" if i%2==0 else "BLUE"}"))
    else: 
        print(colorize_message(f"There are no upcoming birthdays", "YELLOW"))

if __name__ == "__main__":
    pass