from classes.Field import Field

class Name(Field):
    """
   Specialized field class for storing contact names.
   Automatically capitalizes names to ensure consistent formatting.
   """
    def __init__(self, name):
        self.value = name.capitalize()

if __name__ == "__main__":
    pass