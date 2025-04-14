from utilities.colorize import colorize_message
from rich.console import Console
from rich.table import Table
"""
Displays all contacts in a formatted rich table or shows a warning if empty.
"""
def show_all_contacts(contacts):
    if len(contacts)!=0:
        console = Console()

        table = Table(title="Address Book", title_style="bold green", style="green", row_styles=["cyan", "blue"] )

        table.add_column("Name")
        table.add_column("Phones")
        table.add_column("Birthday")
        table.add_column("Email")
        table.add_column("Address")

        for contact in contacts:
            birthday = contact.birthday if contact.birthday!=None else ''
            email = str(contact.email) if contact.email !=None else ''
            address = str(contact.address) if contact.address !=None else ''
            table.add_row(contact.name, '\n'.join(contact.phones), birthday, email, address)

        console.print(table)
    else: 
        print(colorize_message(f"No contacts yet ", "YELLOW"))

if __name__ == "__main__":
    pass