from collections import UserDict
from datetime import date, datetime, timedelta
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

    def get_upcoming_birthdays(self, days: int) -> list:
        today = date.today()
        end_date = today + timedelta(days=days)
        upcoming = []
        seen = set()

        for record in self.data.values():
            birthday = record.get_birthday_date()
            if birthday:
                this_year_birthday = birthday.replace(year=today.year)
                if today <= this_year_birthday <= end_date:
                    key = record.name.value
                    if key not in seen:
                        seen.add(key)
                        upcoming.append(record)

        return upcoming

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
