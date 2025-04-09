from components.AddressBook import AddressBook
from utility.user_input_handler import user_input_handler


def format_contact(record):
    """Форматує інформацію про контакт для відображення."""
    phones = ', '.join(p.value for p in record.phones)
    birthday = record.get_birthday if record.birthday else "не вказано"
    email = getattr(record, 'email', "не вказано")
    
    return (
        f"Ім'я: {record.name.value}\n"
        f"Телефони: {phones}\n"
        f"День народження: {birthday}\n"
        f"Email: {email}"  # Прибрали тире і перехід на новий рядок
    )

def show_search(args, book: AddressBook):
    """
    Функція для пошуку контактів за різними критеріями.
    
    Args:
        args: аргументи командного рядка
        book: екземпляр адресної книги
    
    Returns:
        str: відформатований результат пошуку або повідомлення про помилку
    """
    search_types = {
        '1': ('name', "ім'ям", "Введіть ім'я: "),
        '2': ('phone', "телефоном", "Введіть номер телефону: "),
        '3': ('birthday', "датою народження", "Введіть дату народження (DD.MM.YYYY): "),
        '4': ('email', "email", "Введіть email: ")
    }

    # Інтерактивний режим, якщо немає аргументів
    if not args:
        print("\nДоступні варіанти пошуку:")
        for num, (_, desc, _) in search_types.items():
            print(f"{num} - Пошук за {desc}")
        
        choice = input("\nВиберіть номер варіанту пошуку: ").strip()
        if choice not in search_types:
            return "Невірний вибір. Введіть число від 1 до 4"
        
        search_type, _, prompt = search_types[choice]
        search_term = input(prompt).strip()
    else:
        # Якщо передані аргументи
        if len(args) < 2:
            return "Введіть тип пошуку та значення"
        search_type, search_term = args[0], ' '.join(args[1:])
    
    # Отримуємо результати пошуку як словник
    result_dict = book.search(search_term, search_type)
    
    if not result_dict:
        return "Контакти не знайдені"
    
     # Форматуємо результат
    formatted_contacts = [format_contact(record) for record in result_dict.values()]
    
    # Створюємо текст результату з акуратним форматуванням
    result_text = f"\nЗнайдено контактів: {len(result_dict)}\n"
    
    # Додаємо контакти з роздільниками
    for contact in formatted_contacts:
        result_text += "\n" + contact
    
    return result_text