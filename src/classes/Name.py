from classes.Field import Field

class Name(Field):
    def __init__(self, name:str):
        self.value = ' '.join(word.capitalize() for word in name.strip().split())

if __name__ == "__main__":
    pass