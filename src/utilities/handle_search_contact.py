from utilities.show_search_contact import show_search_contact
from utilities.user_input_handler import user_input_handler
from classes.Phone import Phone
from classes.Email import Email
from classes.Birthday import Birthday
from utilities.colorize import colorize_message
    
def handle_search_contact(args, book):
    """
    Allows interactive searching for contacts by various criteria.
    Includes input validation for each search type and displays formatted results.
    """
    valid_search_types = ["name", "phone", "birthday", "email"]
    
    # Interactive mode
    while True:
        search_type = user_input_handler(colorize_message("Enter the search type (name, phone, birthday, email): ", "GREEN")).strip().lower()
        if search_type in valid_search_types:
            break
        else:
            print(colorize_message(f"Invalid search type. Valid types: {', '.join(valid_search_types)}", "YELLOW")) 
    
    # Customize the query for the selected search type
    if search_type == "name":
        search_term = user_input_handler(colorize_message("Enter name: ", "GREEN")).strip()
        print(search_term)

    elif search_type == "phone":
        while True:
            search_term = user_input_handler(colorize_message("Enter phone (10 digits): ", "GREEN")).strip()
            try:
                Phone(search_term)
                break
            except Exception as e:
                print(colorize_message(str(e), "YELLOW"))

    elif search_type == "birthday":
        while True:
            search_term = user_input_handler(colorize_message("Enter date of birth to search (format DD.MM.YYYY): ", "GREEN")).strip()
            if search_term.lower() == "exit":
                return None
            
            try:
                Birthday(search_term)
                break
            except Exception as e:
                print(colorize_message(str(e), "YELLOW"))
           
    elif search_type == "email":
        while True:
            search_term = user_input_handler(colorize_message("Enter email: ", "GREEN")).strip()
            try:
                Email(search_term)
                break
            except Exception as e:
                print(colorize_message(str(e), "YELLOW"))
    
    return show_search_contact(book.search(search_term, search_type))