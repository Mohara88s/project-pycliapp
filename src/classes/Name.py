from classes.Field import Field

class Name(Field):

    """
   Specialized field class for storing contact names.
   Automatically capitalizes names to ensure consistent formatting.
   """
    def __init__(self, name:str):
        self.value = ' '.join(word.capitalize() for word in name.strip().split())

if __name__ == "__main__":
    pass