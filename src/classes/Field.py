class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)
    
    def __format__(self, format_spec):
        return format(str(self), format_spec)
    
if __name__ == "__main__":
    pass