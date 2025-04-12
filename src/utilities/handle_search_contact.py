from utilities.show_search import show_search
from utilities.user_input_handler import user_input_handler
from classes.Phone import Phone
from classes.Email import Email
from classes.Birthday import Birthday
from classes.Name import Name
from utilities.colorize import colorize_message
    
def handle_search_contact(args, book):

    valid_search_types = ["name", "phone", "birthday", "email"]
    comand = "exit"
    if not args:
        # Інтерактивний режим
        while True:
            search_type = user_input_handler("Enter the search type (name, phone, birthday, email): ").strip().lower()
            if search_type in valid_search_types:
                break
            else:
                print(colorize_message("Invalid search type. ", "YELLOW")) 
        
        # Налаштовуємо запит під обраний тип пошуку
        if search_type == "name":
            search_term =  user_input_handler("Enter name: ").strip()


        elif search_type == "phone":
            while True:
                search_term = user_input_handler("Enter phone (10 digits): ").strip()
                
                # Number validation
                if search_term.isdigit() and len(search_term) == 10:
                    break
                elif search_term == comand:
                    break
                else:
                    print(colorize_message("The phone number has to contain 10 digits.", "YELLOW"))


        elif search_type == "birthday":
            while True:
                search_term = user_input_handler("Enter date of birth to search (format DD.MM.YYYY): ").strip()
                try:

                    if search_term == comand:
                        break
                    else:
                            # Перевірка формату дати 
                        day, month, year = search_term.split(".")
                        if (len(day) == 2 and len(month) == 2 and len(year) == 4 and 
                            day.isdigit() and month.isdigit() and year.isdigit() and
                            1 <= int(day) <= 31 and 1 <= int(month) <= 12 and 1000 <= int(year) <= 9999):
                            break
                        
                        else:
                            print(colorize_message("Incorrect date format. Format DD.ММ.YYYY.", "YELLOW"))
                except ValueError:
                    print(colorize_message("Incorrect date format. Format DD.ММ.YYYY.", "YELLOW"))

            """"       
        elif search_type == "email":
            while True:
                search_term = user_input_handler("Enter email: ").strip()
                try:
                    Email(search_term)
                    break
                except Exception as e:
                    print(str(e))
                        """
        
        elif search_type == "email":
            while True:
                search_term = user_input_handler("Enter email: ").strip()
                if "@" in search_term and "." in search_term:
                    break
                elif search_term == comand:
                        break
                else:
                    print(colorize_message("Incorrect email format. Email must contain the @ and .", "YELLOW"))    
                     

    else:
        search_term = input("Enter the search type: ").strip()
            
    return show_search(book.search(search_term, search_type))
   