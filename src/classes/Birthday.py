from datetime import datetime
from classes.Field import Field
import re

class Birthday(Field):
    """
   Handles storage and validation of contact birthday information.
   Ensures dates are properly formatted and converts string dates to datetime objects.
   """
    def __init__(self, value):
        validated_date = self.validate_birthday(value)
        super().__init__(validated_date)

    @staticmethod
    def validate_birthday(value):
        # Check if the string and date format are correct
        if isinstance(value, str) and re.fullmatch(r'(\d{1}|\d{2}).(\d{1}|\d{2}).\d{4}', value) is not None: 
            return datetime.strptime(value, "%d.%m.%Y").date()
        else: raise ValueError("Invalid date format. Use DD.MM.YYYY")

if __name__ == "__main__":
    pass