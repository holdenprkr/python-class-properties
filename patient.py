class Patient:
    def __init__(self, social_security_number, date_of_birth, health_insurance_account_number, first_name, last_name, address):
        self.__social_security_number = social_security_number
        self.__date_of_birth = date_of_birth
        self.__health_insurance_account_number = health_insurance_account_number
        self.__first_name = first_name
        self.__last_name = last_name
        self.__address = address

    @property
    def social_security_number(self):
        return self.__social_security_number

    @property
    def date_of_birth(self):
        return self.__date_of_birth

    @property
    def health_insurance_account_number(self):
        return self.__health_insurance_account_number

    @property
    def full_name(self):
        return f"{self.__first_name} {self.__last_name}"

    @property
    def address(self):
        try:
            return self.__address
        except AttributeError:
            return ""

    @address.setter
    def address(self, new_address):
        if type(new_address) is str:
            self.__address = new_address
        else:
            raise TypeError("Please provide a string for the address")


cashew = Patient(
    "097-23-1003", "08/13/92", "7001294103",
    "Daniela", "Agnoletti", "500 Infinity Way"
)

print(cashew.social_security_number)
print(cashew.date_of_birth)

print(cashew.full_name)

cashew.address = "400 Billion Dr"
print(cashew.address)
