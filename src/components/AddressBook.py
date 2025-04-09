from collections import UserDict
from datetime import datetime
from components.Record import Record
from components.Name import Name
from components.Phone import Phone

class AddressBook(UserDict):

    def __getitem__(self, key):
        return self.data.get(key, "Key not found")
    
    def add_record(self, record):
        self.data[record.name.value] = record
            
    def find(self, name):
        result = self.data.get(name.capitalize(), None)
        return result

    def delete(self, name):
        if not name.capitalize() in self.data:
            raise Exception(f"The contact with name:{name.capitalize()} is not found")
        del self.data[name.capitalize()]

    @property
    def get_all_records(self):
        return self.data

    def get_upcoming_birthdays(self, days_to_bd:int)->list:
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
