from classes.Field import Field

class Phone(Field):    
    """  
    Provides phone number storage with validation for 10-digit format.  
    Includes full validation and digit format enforcement.  
    """  
    def __init__(self, phone):
        validated_phone = self.phone_validation(phone)
        super().__init__(validated_phone)

    @staticmethod  
    def phone_validation(phone):
        if len(phone) != 10 | (not phone.isdigit()):
            raise Exception("The phone number has to contain 10 digits")
        return phone
    
if __name__ == "__main__":
    pass