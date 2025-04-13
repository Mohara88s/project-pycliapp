from classes.Field import Field

class Address(Field):
    """
   Handles storage and validation of contact address information.
   Ensures addresses meet required format and length constraints.
    """
    def __init__(self, address):
        validated_address = self.address_validation(address)
        super().__init__(validated_address)

    @staticmethod
    def address_validation(address: str) -> str:
        # Address validation
        if not isinstance(address, str):
            raise ValueError("Address must be a string.")
        if not 5<= len(address) <=100:
            raise ValueError ("Address must be between 5 and 100 characters long.")
        return address

if __name__ == "__main__":
    pass