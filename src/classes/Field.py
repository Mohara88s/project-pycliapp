class Field:
    """
   Base class for all contact field types in the address book.
   Provides common functionality for field value storage and string representation.
   """
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)
    
    def __format__(self, format_spec):
        return format(str(self), format_spec)
    
if __name__ == "__main__":
    pass