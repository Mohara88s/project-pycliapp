from utility.show_search import show_search
from components.Phone import Phone
from components.Email import Email
from components.Birthday import Birthday
from components.Name import Name
"""def handle_search_contact(args, book):
    if not args:
        
        search_type = input("Enter search type (name, phone, birthday, email): ").strip()

        search_term = input("Enter search query: ").strip()
        return show_search(book.search(search_term, search_type))
    elif len(args) >= 2:
        
        return show_search(book.search(args[1], args[0]))
    else:
        print("Incorrect number of arguments. Use: search-contact [TYPE] [VALUE]")
        return 
        """
    
def handle_search_contact(args, book):

    valid_search_types = ["name", "phone", "birthday", "email"]

    if not args:
        # Интерактивный режим
        while True:
            search_type = input("Enter the search type (name, phone, birthday, email): ").strip().lower()
            if search_type in valid_search_types:
                break
            else:
                print(f"Invalid search type. ") #Valid types: {', '.join(valid_search_types)}
        
        # Подстраиваем запрос под выбранный тип поиска
        if search_type == "name":
            search_term =  input("Enter name: ").strip()


        elif search_type == "phone":
            while True:
                search_term = input("Enter phone (10 digits): ").strip()
                try:
                    # Используем метод валидации из класса Phone
                    Phone(search_term)
                    break
                except Exception as e:
                    print(str(e))


        elif search_type == "birthday":
            while True:
                search_term = input("Enter date of birth to search (format DD.MM.YYYY): ").strip()
                try:
                    # Проверяем формат даты
                    day, month, year = search_term.split(".")
                    if (len(day) == 2 and len(month) == 2 and len(year) == 4 and 
                        day.isdigit() and month.isdigit() and year.isdigit() and
                        1 <= int(day) <= 31 and 1 <= int(month) <= 12 and 1000 <= int(year) <= 9999):
                        break
                    else:
                        print("Incorrect date format. Format DD.ММ.YYYY.")
                except ValueError:
                    print("Incorrect date format. Format DD.ММ.YYYY.")


        elif search_type == "email":
            while True:
                search_term = input("Enter email: ").strip()
                try:
                    Email(search_term)
                    break
                except Exception as e:
                    print(str(e))




    else:
        search_term = input("Enter the search type: ").strip()
            
    return show_search(book.search(search_term, search_type))
    """
    elif len(args) >= 2:
        # Режим с аргументами
        return show_search(book.search(args[1], args[0]))
    else:
        print("Неправильное количество аргументов. Используйте: search-contact TYPE VALUE")
        return None
"""