class Student:

    @property
    def first_name(self):
        try:
            return self.__first_name
        except AttributeError:
            return ""

    @first_name.setter
    def first_name(self, new_first_name):
        if type(new_first_name) is str:
            self.__first_name = new_first_name
        else:
            raise TypeError("Please provide a string for the first name")

    @property
    def last_name(self):
        try:
            return self.__last_name
        except AttributeError:
            return ""

    @last_name.setter
    def last_name(self, new_last_name):
        if type(new_last_name) is str:
            self.__last_name = new_last_name
        else:
            raise TypeError("Please provide a string for the last name")

    @property
    def age(self):
        try:
            return self.__age
        except AttributeError:
            return 0

    @age.setter
    def age(self, new_age):
        if type(new_age) is int:
            self.__age = new_age
        else:
            raise TypeError("Please provide an integer value for the age")

    @property
    def cohort_number(self):
        try:
            return self.__cohort_number
        except AttributeError:
            return 0

    @cohort_number.setter
    def cohort_number(self, new_cohort_number):
        if type(new_cohort_number) is int:
            self.__cohort_number = new_cohort_number
        else:
            raise TypeError(
                "Please provide an integer value for the cohort number")

    @property
    def full_name(self):
        return f"{self.__first_name} {self.__last_name}"

    def __str__(self):
        return f"{self.full_name} is {self.age} years old and is in cohort {self.cohort_number}"


mike = Student()
mike.first_name = "Mike"
mike.last_name = "Ellis"
mike.age = 35
mike.cohort_number = 39

print(mike)
