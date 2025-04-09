from datetime import datetime, date
from components.Name import Name
from components.Phone import Phone
from components.Birthday import Birthday
 
class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.birthday = None

    @property
    def get_phones(self):
        list_of_phones = []
        for phone in self.phones:
            list_of_phones.append(phone.value)
        return list_of_phones
    
    def add_phone(self, phone):
        if self.find_phone(phone):
            raise Exception(f"The phone number {phone} has already been added to contact {self.name}")
        self.phones.append(Phone(phone))

    def remove_phone(self, phone):
        if not self.find_phone(phone):
            raise Exception(f"The phone number:{phone} is not found")
        self.phones = [ph for ph in self.phones if ph.value != phone]   

    def edit_phone(self, phone, new_phone):
        if not self.find_phone(phone):
            raise Exception(f"The phone number:{phone} is not found")
        self.phones = [Phone(new_phone) if ph.value == phone else ph for ph in self.phones]
        
    def find_phone(self, phone):
        result = [ph for ph in self.phones if ph.value == phone]
        return result[0] if len(result) > 0 else None
    
    @property
    def get_birthday(self):
        if self.birthday:
            value = self.birthday.value
            if isinstance(value, date):
                return value.strftime("%d.%m.%Y")
            elif isinstance(value, str):
                try:
                    birthday_date = datetime.strptime(value, "%d.%m.%Y")
                    return birthday_date.strftime("%d.%m.%Y")
                except ValueError:
                    raise Exception("Invalid birthday format. Use DD.MM.YYYY")
        raise Exception("The birthday is not found")
    
    def add_birthday(self, birthday_str):
        self.birthday=Birthday(birthday_str)

    def get_birthday_date(self):
        if not self.birthday or not getattr(self.birthday, "value", None):
            return None

        value = self.birthday.value

        if isinstance(value, date):
            return value

        try:
            return datetime.strptime(value, "%d.%m.%Y").date()
        except ValueError:
            return None

    def __str__(self):
        return f"Contact name: {self.name.value}, contact birthday:{self.birthday}, phones: {'; '.join(p.value for p in self.phones)}"
    
if __name__ == "__main__":
    pass