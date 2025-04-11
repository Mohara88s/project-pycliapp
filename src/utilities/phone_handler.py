from classes import AddressBook

def show_phone(args, book: AddressBook):
    if len(args)<1:
        raise ValueError("Please give me the contact's name")
    name, *_ = args
    record = book.find(name)
    if record is None:
        raise Exception(f"The contact {name} is not found")
    return record.get_phones


if __name__ == "__main__":
    pass
