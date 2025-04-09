from components.AddressBook import AddressBook


def search_contacts(args, book: AddressBook):
    # Якщо аргументи не передані, показуємо меню
    if not args:
        print("\nДоступні варіанти пошуку:")
        print("1 - Пошук за ім'ям")
        print("2 - Пошук за телефоном")
        print("3 - Пошук за датою народження")
        print("4 - Пошук за email")
        
        try:
            choice = int(input("\nВиберіть номер варіанту пошуку: "))
        except ValueError:
            return "Будь ласка, введіть число від 1 до 4"
        
        search_term = input("Введіть значення для пошуку: ").strip()
        
        # Визначаємо тип пошуку на основі вибору користувача
        if choice == 1:
            search_type = 'name'
        elif choice == 2:
            search_type = 'phone'
        elif choice == 3:
            search_type = 'birthday'
        elif choice == 4:
            search_type = 'email'
        else:
            return "Невірний вибір. Введіть число від 1 до 4"
    else:
        # Старий формат для сумісності (якщо передані аргументи)
        if len(args) < 2:
            return "Введіть тип пошуку та значення"
        search_type, search_term = args[0], args[1]
    
    # Виконуємо пошук
    results = book.search(search_term, search_type)
    if not results:
        return "Контакти не знайдені"
    
    # Форматуємо результат
    output = []
    for record in results:
        phones = '\n'.join(f"Телефон {i+1}: {phone.value}" for i, phone in enumerate(record.phones))
        birthday = record.birthday.value if record.birthday else "не вказано"
        email = getattr(record, 'email', "не вказано")
        
        contact_info = [
            f"\nІм'я: {record.name.value}",
            phones,
            f"День народження: {birthday}",
            f"Email: {email}",
            "-" * 30  # Роздільник між контактами
        ]
        output.append('\n'.join(contact_info))
    
    return '\n'.join(output)