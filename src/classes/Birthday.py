from datetime import datetime
from classes.Field import Field
import re

class Birthday(Field):
    def __init__(self, value):
        if isinstance(value, str) and re.fullmatch(r'(\d{1}|\d{2}).(\d{1}|\d{2}).\d{4}', value) is not None: 
            self.value = datetime.strptime(value, "%d.%m.%Y").date()
        else: raise ValueError("Invalid date format. Use DD.MM.YYYY")

if __name__ == "__main__":
    pass