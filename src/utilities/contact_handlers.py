from collections import namedtuple
from classes import AddressBook, Record
from utilities.colorize import colorize_message
"""
Contact Management System

Provides complete CRUD operations for contact records including:
- Personal information management
- Phone number handling
- Email/address management
- Birthday tracking
"""
def add_contact(args, book: AddressBook):
    """
    Creates or updates a contact with basic information
    """
    if len(args)<3:
        raise ValueError("Please give me the contact's first and last name and phone")
    first_name, last_name, phone, *_ = args
    name = first_name + ' ' + last_name
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
    """
    Updates an existing contact's phone number
    """
    if len(args)<4:
        raise ValueError("Please give me the contact's first and last name, old phone and new phone")
    first_name, last_name, phone, new_phone, *_ = args
    name = first_name + ' ' + last_name
    record = book.find(name)
    if record is None:
        raise Exception(f"The contact {name} is not found")
    record.edit_phone(phone, new_phone)
    message = "Contact updated"
    return colorize_message(message, "GREEN")


def delete_contact(args, book: AddressBook):
    """
    Removes a contact completely from the address book
    """
    if len(args)<2:
        raise ValueError("Please give me the contact's first and last name")
    first_name, last_name, *_ = args
    name = first_name + ' ' + last_name
    book.delete(name)
    message = "Contact deleted"
    return colorize_message(message, "GREEN")

def get_all_contacts(book: AddressBook):
    """
    Retrieves all contacts in a sorted, structured format
    """
    list_of_contacts = []
    Contact_tuple = namedtuple('Contact', ['name', 'phones','birthday', 'email', 'address'])
    for name, record in book.get_all_records.items():
        list_of_contacts.append(Contact_tuple(name, record.get_phones, record.get_birthday, record.get_email, record.get_address))
    return sorted(list_of_contacts)

def show_phone(args, book: AddressBook):
    """
    Displays a contact's phone numbers
    """
    if len(args)<2:
        raise ValueError("Please give me the contact's first and last name")
    first_name, last_name, *_ = args
    name = first_name + ' ' + last_name
    record = book.find(name)
    if record is None:
        raise Exception(f"The contact {name} is not found")
    message = f'{", ".join(record.get_phones)}'
    return colorize_message(message, "GREEN")

def add_email(args, book):
    """
    Adds an email address to a contact
    """
    if len(args)<3:
        raise ValueError("Please give me the contact's first and last name and email")
    first_name, last_name, email = args
    name = first_name + ' ' + last_name
    record = book.find(name)
    if not record:
        return f"No contact found with name: {name}"
    record.add_email(email)
    message = f"Email '{email}' added to contact '{name}'"
    return colorize_message(message, "GREEN")
    
def add_address(args, book):
    """
    Adds a physical address to a contact
    """
    if len(args)<3:
        raise ValueError("Please give me the contact's first and last name and address")
    first_name, last_name, *address = args
    name = first_name + ' ' + last_name
    address = " ".join(address)
    record = book.find(name)
    if not record:
        return f"No contact found with name: {name}"
    record.add_address(address)
    message = f"Address '{address}' added to contact '{name}'"
    return colorize_message(message, "GREEN")

def edit_email(args, book):
    """
    Updates a contact's email address
    """
    if len(args)<3:
        raise ValueError("Please give me the contact's first and last name and email")
    first_name, last_name, new_email = args
    name = first_name + ' ' + last_name
    record = book.find(name)
    if not record:
        return f"No contact found with name: {name}"
    record.edit_email(new_email)
    message = f"Email for '{name}' updated to '{new_email}'"
    return colorize_message(message, "GREEN")

def edit_address(args, book):
    """
    Updates a contact's physical address
    """
    if len(args)<3:
        raise ValueError("Please give me the contact's first and last name and address")
    first_name, last_name, *new_address = args
    name = first_name + ' ' + last_name
    record = book.find(name)
    new_address_str = " ".join(new_address)
    if not record:
        return f"No contact found with name: {name}"
    record.edit_address(new_address_str)
    message = f"Address for '{name}' updated to '{new_address_str}'"
    return colorize_message(message, "GREEN")

def delete_email(args, book: AddressBook):
    """
    Removes a contact's email address
    """
    if len(args)<1:
        raise ValueError("Please give me the contact's email")
    email, *_ = args
    book.delete(email)
    message = "email deleted"
    return colorize_message(message, "GREEN")

def delete_address(args, book: AddressBook):
    """
    Removes a contact's physical address
    """
    if len(args) !=2:
        raise ValueError("Please give me the contact's first and last name")

    first_name, last_name, *_= args
    name = first_name + ' ' + last_name
    record = book.find(name)
    if not isinstance(record, Record):
        return(f"No contact with the name '{name}' exists")
    if record.address:
        record.delete_address()
        message = "Address deleted"
        return colorize_message(message, "GREEN")
    else:
        return("Address not found for this contact")
    
def edit_name(args, book):
    """
    Changes a contact's name
    """
    if len(args)<4:
        raise ValueError("Please give me the contact's old first and last name and new first and last name")
    old_first_name, old_last_name, new_first_name, new_last_name, *_ = args
    old_name = old_first_name +' '+ old_last_name
    new_name = new_first_name +' '+ new_last_name
    book.edit_name(old_name, new_name)
    message = f"Name changed from '{old_name}' to '{new_name}'"
    return colorize_message(message, "GREEN")


def add_birthday(args, book: AddressBook):
    """
    Sets/updates a contact's birthday
    """
    if len(args)<3:
        raise ValueError(f"Please give me the contact's first and last name and birthday date")
    first_name, last_name, birthay, *_ = args
    name = first_name + ' ' + last_name
    record = book.find(name)
    if record is None:
        raise Exception(f"The contact {name} is not found")
    record.add_birthday(birthay)
    message = "Contact updated"
    return colorize_message(message, "GREEN")


def show_birthday(args, book: AddressBook):
    """
    Displays a contact's birthday
    """
    if len(args)<2:
        raise ValueError(f"Please give me the contact's first and last name")
    first_name, last_name, *_ = args
    name = first_name + ' ' + last_name
    record = book.find(name)
    if record is None:
        raise Exception(f"The contact {name} is not found")
    res = record.get_birthday
    if not res:
        raise Exception(f"The birthday is not found")
    return colorize_message(res, "GREEN")


def get_upcoming_birthdays(args, book: AddressBook):
    """
    Retrieves contacts with birthdays within specified days
    """
    days=365
    if len(args)>0:
        try:
            days = int(args[0])
        except:
            raise Exception("Days must be a positive integer")
    list_of_birthdays = []
    Birthday_tuple = namedtuple('Birthday_tuple', ['name', 'birthday'])
    for contact in book.get_upcoming_birthdays(days):
        list_of_birthdays.append(Birthday_tuple(contact.get('name'), contact.get('congratulation_date')))
    return list_of_birthdays

def edit_birthday(args, book):
    """
    Updates a contact's birthday date
    """
    if len(args)<3:
        raise ValueError("Please give me the contact's first and last name and birthday date")
    first_name, last_name, new_birthday, *_ = args
    name = first_name + ' ' + last_name
    record = book.find(name)
    if not record:
        return f"No contact found with name: {name}"
    record.edit_birthday(new_birthday)
    message = f"Birthday for '{name}' updated to '{new_birthday}'"
    return colorize_message(message, "GREEN")



if __name__ == "__main__":
    pass
