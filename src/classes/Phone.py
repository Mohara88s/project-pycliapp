from classes.Field import Field

class Phone(Field):    
    def __init__(self, phone):
        validated_phone = self.phone_validation(phone)
        super().__init__(validated_phone)
        
    def phone_validation(self, phone):
        if len(phone) != 10 | (not phone.isdigit()):
            raise Exception("The phone number has to contain 10 digits")
        return phone
    
if __name__ == "__main__":
    pass