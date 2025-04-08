from components.Field import Field

class Name(Field):
    def __init__(self, name):
        self.value = name.capitalize()
