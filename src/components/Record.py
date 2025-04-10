from datetime import datetime, date
from components.Name import Name
from components.Phone import Phone
from components.Birthday import Birthday
from components.Email import Email
from components.Address import Address
 
class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = [] 
        self.birthday = None
        self.email = None
        self.address = None


    @property
    def get_phones(self):
        list_of_phones = []
        for phone in self.phones:
            list_of_phones.append(phone.value)
        return list_of_phones
    
    def add_email(self, email):
        self.email = email
    
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
        birthday_date = datetime.strptime(str(self.birthday), "%Y-%m-%d").strftime("%d.%m.%Y") if self.birthday else None
        return birthday_date
    
    def add_birthday(self, birthday_str):
        self.birthday=Birthday(birthday_str)

    def add_email(self, email_str):
        self.email = Email(email_str)

    def add_address(self, address_str):
        self.address = Address(address_str)    


    def __str__(self):
        return f"Contact name: {self.name.value}, contact birthday:{self.birthday}, phones: {'; '.join(p.value for p in self.phones)}, email: {self.email}, address: {self.address}"
    
if __name__ == "__main__":
    pass