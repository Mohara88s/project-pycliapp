from utility.colorize import colorize_message

def show_all_contacts(contacts):
    if len(contacts)!=0:
        print(colorize_message(f"{"Name":<20}{"Phone":<15}{"Birthday":<15}{"Email":<20}{"Address":<20}", "MAGENTA"))
        for i, contact in enumerate(contacts):
            bithday = contact.birthday if contact.birthday!=None else 'None'
            print(contact.email)
            print(colorize_message(f"{contact.name:<20}{'\n                    '.join(contact.phones)}     {bithday:<15}{str(contact.email):<20}{str(contact.address):<20}", f"{"CYAN" if i%2==0 else "BLUE"}"))
    else: 
        print(colorize_message(f"No contacts yet ", "YELLOW"))

if __name__ == "__main__":
    pass