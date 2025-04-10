from classes.Field import Field

class Address(Field):
    def __init__(self, address):
        self.value = self.address_validation(address)

    @staticmethod
    def address_validation(address: str) -> str:
        # Перевірка, що адреса не пуста
        if not isinstance(address, str):
            raise ValueError("Address must be a string.")
        if not 5<= len(address) <=100:
            raise ValueError ("Address must be between 5 and 100 characters long.")
        return address

if __name__ == "__main__":
    pass