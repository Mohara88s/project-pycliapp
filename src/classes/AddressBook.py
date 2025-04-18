from collections import UserDict
from datetime import datetime
from classes.Record import Record
from classes.Name import Name
from classes.Phone import Phone

class AddressBook(UserDict):
    """
    Manages a collection of contact records with various search and manipulation capabilities.
    Extends UserDict to provide dictionary-like functionality with additional contact management features.
    """
    def __getitem__(self, key):
        return self.data.get(key, "Key not found")
    
    def add_record(self, record):
        self.data[record.name.value] = record
            
    def find(self, name):
        result = self.data.get(' '.join(word.capitalize() for word in name.strip().split()), None)
        return result

    def delete(self, name):
        if not ' '.join(word.capitalize() for word in name.strip().split()) in self.data:
            raise Exception(f"The contact with name:{' '.join(word.capitalize() for word in name.strip().split())} is not found")
        del self.data[' '.join(word.capitalize() for word in name.strip().split())]
    
    def edit_name(self, old_name, new_name):
        record = self.data.get(' '.join(word.capitalize() for word in old_name.strip().split()), None)
        if record == None:
            raise Exception(f"The contact with name:{' '.join(word.capitalize() for word in old_name.strip().split())} is not found")
        new_name_obj = Name(new_name)
        record.name = new_name_obj
        self.data[new_name_obj.value] = record
        old_key = ' '.join(word.capitalize() for word in old_name.strip().split())
        del self.data[old_key]
    
    @property
    def get_all_records(self):
        return self.data

    def get_upcoming_birthdays(self, days_to_bd:int)->list:
        """
        Finds contacts with birthdays within the specified number of days.
        Returns a sorted list of contacts with their upcoming celebration dates.
        """
        if not isinstance(days_to_bd, int) or days_to_bd <= 0:
            raise Exception("Days must be a positive integer")
        records_to_congr = []
        today = datetime.today().date()
        for name, record in self.data.items():
            if record.birthday:
                date_of_birth = datetime.strptime(f"{record.birthday}", "%Y-%m-%d").date()
                if today < date_of_birth: continue
                birthday_this_year = date_of_birth.replace(year=today.year)
                next_bd = date_of_birth.replace(year=today.year + 1) if birthday_this_year < today else birthday_this_year  
                if next_bd.toordinal() - today.toordinal() <= days_to_bd:    
                    congratulation_date = next_bd.strftime("%d.%m.%Y")
                    records_to_congr.append({"name":name, "congratulation_date":congratulation_date})
        return sorted(records_to_congr, key=lambda x: datetime.strptime(x["congratulation_date"], "%d.%m.%Y"), reverse=False)
    
    def search(self, search_term: str, search_type: str = 'name'):
        """
        Performs flexible search across contact records by different criteria.
        Supports searching by name, phone, birthday, and email with partial matching.
        """
        result_dict = {} 
        search_term = search_term.strip().lower()
        
        for record in self.data.values():
            # Search for name
            if search_type == 'name':
                name_to_check = record.name.value.lower()
                if search_term in name_to_check:
                    result_dict[record.name.value] = record
            
            # search for phone
            elif search_type == 'phone':
                for phone in record.phones:
                    if search_term in phone.value:
                        result_dict[record.name.value] = record
                        break
            
            # Search for birthday data
            elif search_type == 'birthday' and record.birthday:
                try:
                    bd_date = record.get_birthday
                    if search_term in bd_date:
                        result_dict[record.name.value] = record
                except (ValueError, AttributeError):
                    continue

            # Search for email
            elif search_type == 'email' and hasattr(record, 'email') and record.email:
                if search_term.lower() in str(record.email).lower():
                    result_dict[record.name.value] = record    
        
        return result_dict 
    
       

if __name__ == "__main__":
    try:
        # Створення нової адресної книги
        book = AddressBook()

        # Створення запису для John
        john_record = Record("John")
        john_record.add_phone("1234567890")
        john_record.add_phone("5555555555")

        # Додавання запису John до адресної книги
        book.add_record(john_record)

        # Створення та додавання нового запису для Jane
        jane_record = Record("Jane")
        jane_record.add_phone("9876543210")
        book.add_record(jane_record)

        # Виведення всіх записів у книзі
        for name, record in book.data.items():
            print(record)

        # Знаходження та редагування телефону для John
        john = book.find("John")
        john.edit_phone("1234567890", "1112223333")

        print(john)  # Виведення: Contact name: John, phones: 1112223333; 5555555555

        # Пошук конкретного телефону у записі John
        found_phone = john.find_phone("5555555555")
        print(f"{john.name}: {found_phone}")  # Виведення: John: 5555555555

        # Видалення запису Jane
        book.delete("Jane")


        # Мої додаткові перевірки
        # Додавання та видалення телефону для John
        john_record.add_phone("1231231231")
        # Додавання дня народження для John
        john_record.add_birthday("25.03.2000")
        print(john_record.get_birthday) # Виведення: 2000.03.25
        print(john) # Виведення: Contact name: John, contact birthday:2000-03-25, phones: 1112223333; 5555555555; 1231231231
        john_record.remove_phone("1231231231")
        print(john) # Виведення: Contact name: John, contact birthday:2000-03-25, phones: 1112223333; 5555555555
        # Дні народження що в межах 7 наступних днів
        print(book.get_upcoming_birthdays()) #Виведення: [{'name': 'John', 'congratulation_date': '2025.03.25'}]

            
    except Exception as e:
    # Обробка будь-якого винятку
        print(f"An error occurred: {e}")
