from utilities.colorize import colorize_message

def show_search(result_dict):
    if not result_dict:
        print(colorize_message("Nothing found. ", "GREEN"))
        return

    for name, record in result_dict.items():
        print("―" * 40)

        print(f"👤 Name: {name}")
        
        # Show phone
        phones = ', '.join([phone.value for phone in record.phones]) if record.phones else ""
        print(f"📞 Phone: {phones}")
        
        # Show email
        email = str(record.email) if hasattr(record, 'email') and record.email else ""
        print(f"📧 Email: {email}")
        
        # Show date of birth
        birthday = str(record.birthday) if hasattr(record, 'birthday') and record.birthday else ""
        print(f"🎂 Birthday: {birthday}")

        # Show address
        address = str(record.address) if hasattr(record, 'address') and record.address else ""
        print(f"🏠 Address: {address}")

        print("―" * 40)



    

if __name__ == "__main__":
    pass