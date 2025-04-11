from collections import namedtuple
from components import AddressBook, Record
from utility.colorize import colorize_message

def add_contact(args, book: AddressBook):
    if len(args)<2:
        raise ValueError("Please give me the contact's name and phone")
    name, phone, *_ = args
    record = book.find(name)
    message = "Contact updated"
    if record is None:
        record = Record(name)
        book.add_record(record)
        message = "Contact added"
    if phone:
        record.add_phone(phone)
    return colorize_message(message, "GREEN")


def change_contact(args, book: AddressBook):
    if len(args)<3:
        raise ValueError("Please give me the contact's name, old phone and new phone")
    name, phone, new_phone, *_ = args
    record = book.find(name)
    if record is None:
        raise Exception(f"The contact {name} is not found")
    record.edit_phone(phone, new_phone)
    message = "Contact updated"
    return colorize_message(message, "GREEN")


def delete_contact(args, book: AddressBook):
    if len(args)<1:
        raise ValueError("Please give me the contact's name")
    name, *_ = args
    book.delete(name)
    message = "Contact deleted"
    return colorize_message(message, "GREEN")

def get_all_contacts(book: AddressBook):
    list_of_contacts = []
    Contact_tuple = namedtuple('Contact', ['name', 'phones','birthday'])
    for name, record in book.get_all_records.items():
        list_of_contacts.append(Contact_tuple(name, record.get_phones, record.get_birthday)) #record.get_email, record.get_address
    return sorted(list_of_contacts)

def add_email(args, book):
    name, email = args
    record = book.get(name)
    if not record:
        return f"No contact found with name: {name}"
    record.add_email(email)
    return f"Email '{email}' added to contact '{name}'"

def add_address(args, book):

    if len(args) < 2:
        return("Invalid number of arguments. Usage: [name] [address]")
    name = args[0]
    address = " ".join(args[1:])
    record = book.find(name)
    if not isinstance(record, Record):
        return("Contact not found")
    try:
        record.add_address(address)
    except ValueError as e:
        return str(e)
    message = "Address added."
    return message
    

def edit_email(args, book):
    name, new_email = args
    record = book.get(name)
    if not record:
        return f"No contact found with name: {name}"
    record.edit_email(new_email)
    return f"Email for '{name}' updated to '{new_email}'"

def edit_address(args, book):
    name, new_address = args
    record = book.get(name)
    if not record:
        return f"No contact found with name: {name}"
    record.edit_address(new_address)
    return f"Address for '{name}' updated to '{new_address}'"

def edit_name(args, book):
    old_name, new_name = args
    record = book.pop(old_name, None)
    if not record:
        return f"No contact found with name: {old_name}"
    record.name.value = new_name
    book[new_name] = record
    return f"Name changed from '{old_name}' to '{new_name}'"

def edit_birthday(args, book):
    name, new_birthday = args
    record = book.get(name)
    if not record:
        return f"No contact found with name: {name}"
    record.edit_birthday(new_birthday)
    return f"Birthday for '{name}' updated to '{new_birthday}'"

def delete_email(args, book: AddressBook):
    if len(args)<1:
        raise ValueError("Please give me the contact's email")
    email, *_ = args
    book.delete(email)
    message = "email deleted"
    return colorize_message(message, "GREEN")

def delete_address(args, book: AddressBook):
    if len(args) !=1:
        raise ValueError("Please give me the contact's name")
    
    name = args[0]
    record = book.find(name)
    if not isinstance(record, Record):
        return(f"No contact with the name '{name}' exists")
    if record.address:
        record.delete_address()
        message = "Address deleted"
        return colorize_message(message, "GREEN")
    else:
        return("Address not found for this contact")
        
    

if __name__ == "__main__":
    pass
