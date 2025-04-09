from components.Field import Field

class Address(Field):
    def __init__(self, address):
        self.value = self.address_validation(address)

    def address_validation(self, address):
        # Перевірка, що адреса не пуста
        if not address.strip():
            raise Exception("Address cannot be empty")
        return address

if __name__ == "__main__":
    pass