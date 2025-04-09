from collections import namedtuple
from components import AddressBook
from utility.colorize import colorize_message


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


def get_upcoming_birthdays(book: AddressBook):
    list_of_birthdays = []

    Birthday_tuple = namedtuple('Birthday_tuple', ['name', 'birthday'])
    result = []

    for record in book.get_upcoming_birthdays(days):
        result.append(Birthday_tuple(record.name.value, record.birthday.value))

    return result
    
if __name__ == "__main__":
    pass
