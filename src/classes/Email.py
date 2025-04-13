from classes.Field import Field
import re

class Email(Field):
    """
   Handles storage and validation of contact email addresses.
   Ensures emails meet required format using regex pattern matching.
   """
    def __init__(self, email):
        validated_email = self.email_validation(email)
        super().__init__(validated_email)

    @staticmethod
    def email_validation(email):
        # Email validation using regular expressions
        pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
        if not re.match(pattern, email):
            raise Exception("Invalid email format")
        return email.lower()
   
if __name__ == "__main__":
    pass