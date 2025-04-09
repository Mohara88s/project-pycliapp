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
        list_of_contacts.append(Contact_tuple(name, record.get_phones, record.get_birthday))
    return sorted(list_of_contacts)


if __name__ == "__main__":
    pass
