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
    Contact_tuple = namedtuple('Contact', ['name', 'phones','birthday', 'email', 'address'])
    for name, record in book.get_all_records.items():
        list_of_contacts.append(Contact_tuple(name, record.get_phones, record.get_birthday, record.get_email, record.get_address))
    return sorted(list_of_contacts)

def add_email(args, book):
    if len(args)<2:
        raise ValueError("Please give me the contact's name and email")
    name, email = args
    record = book.find(name)
    if not record:
        return f"No contact found with name: {name}"
    record.add_email(email)
    return f"Email '{email}' added to contact '{name}'"

def add_address(args, book):
    if len(args)<2:
        raise ValueError("Please give me the contact's name and address")
    name, address = args
    record = book.find(name)
    if not record:
        return f"No contact found with name: {name}"
    record.add_address(address)
    return f"Address '{address}' added to contact '{name}'"

def edit_email(args, book):
    if len(args)<2:
        raise ValueError("Please give me the contact's name and email")
    name, new_email = args
    record = book.find(name)
    if not record:
        return f"No contact found with name: {name}"
    record.edit_email(new_email)
    return f"Email for '{name}' updated to '{new_email}'"

def edit_address(args, book):
    if len(args)<2:
        raise ValueError("Please give me the contact's name and address")
    name, new_address = args
    record = book.find(name)
    if not record:
        return f"No contact found with name: {name}"
    record.edit_address(new_address)
    return f"Address for '{name}' updated to '{new_address}'"

def edit_name(args, book):
    if len(args)<2:
        raise ValueError("Please give me the contact's old name and new name")
    old_name, new_name = args
    record = book.pop(old_name, None)
    if not record:
        return f"No contact found with name: {old_name}"
    record.name.value = new_name
    book[new_name] = record
    return f"Name changed from '{old_name}' to '{new_name}'"

def add_birthday(args, book: AddressBook):
    if len(args)<2:
        raise ValueError(f"Please give me the contact's name and birthday date")
    name, birthay, *_ = args
    record = book.find(name)
    if record is None:
        raise Exception(f"The contact {name} is not found")
    record.add_birthday(birthay)
    message = "Contact updated"
    return colorize_message(message, "GREEN")


def show_birthday(args, book: AddressBook):
    if len(args)<1:
        raise ValueError(f"Please give me the contact's name")
    name, *_ = args
    record = book.find(name)
    if record is None:
        raise Exception(f"The contact {name} is not found")
    res = record.get_birthday
    if not res:
        raise Exception(f"The birthday is not found")
    return colorize_message(res, "GREEN")


def get_upcoming_birthdays(args, book: AddressBook):
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
    if len(args)<2:
        raise ValueError("Please give me the contact's name and birthday date")
    name, new_birthday = args
    record = book.find(name)
    if not record:
        return f"No contact found with name: {name}"
    record.edit_birthday(new_birthday)
    return f"Birthday for '{name}' updated to '{new_birthday}'"

if __name__ == "__main__":
    pass
