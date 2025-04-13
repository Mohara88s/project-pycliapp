from classes.Field import Field
import re

class Email(Field):
    def __init__(self, email):
        self.value = self.email_validation(email)

    def email_validation(self, email):
        # Email validation using regular expressions
        pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
        if not re.match(pattern, email):
            raise Exception("Invalid email format")
        return email.lower()
   
if __name__ == "__main__":
    pass