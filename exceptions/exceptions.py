class Invalid_Employee_id(Exception):

    def __init__(self, message='id length has to be of eight characters, only digits accepted'):
        self.message=message
        super().__init__(self.message)

class Invalid_score(Exception):

    def __init__(self, message='score is a number between and including 1-99'):
        self.message=message
        super().__init__(self.message)

'''class Invalid_Car_Parameter(Exception):

    def __init__(self, message='one or many of the car\'s parameters given were incorrect'):
        self.message=message
        super().__init__(self.message)
        '''

class Employee_Has_A_Team(Exception):

    def __init__(self, message='Employee already has a team'):
        self.message=message
        super().__init__(self.message)

class Team_Name_Already_in_Use(Exception):

    def __init__(self, message='self descriptive'):
        self.message=message
        super().__init__(self.message)

class Car_Nmbr_Already_in_Use(Exception):

    def __init__(self, message='self descriptive'):
        self.message=message
        super().__init__(self.message)

class Non_Competing_Or_Existing_Car_Nmbr(Exception):

    def __init__(self, message='self descriptive'):
        self.message=message
        super().__init__(self.message)

class Car_Model_In_Use(Exception):

    def __init__(self, message='This car model is represented by another team, check values'):
        self.message=message
        super().__init__(self.message)

class Non_Existent_Id(Exception):

    def __init__(self, message='self descriptive'):
        self.message=message
        super().__init__(self.message)

class Repeating_Parameters(Exception):

    def __init__(self, message='two or more parameters are the same'):
        self.message=message
        super().__init__(self.message)

class Alphabet(Exception):

    def __init__(self, message='check syntax issues, only alphabet characters available'):
        self.message=message
        super().__init__(self.message)

class Age(Exception):

    def __init__(self, message='Check age range of years [15-120] dates between [1888/01/01 - 2008/01/01/]'):
        self.message=message
        super().__init__(self.message)

class Nacionality(Exception):
    def __init__(self, message='Check nationality sintax, remember must use alphabet characters'):
        self.message=message
        super().__init__(self.message)

class Dates(Exception):
    def __init__(self, message='Check  sintax, remember dates between [1888/01/01 - 2008/01/01/]'):
        self.message=message
        super().__init__(self.message)

class Dates_Team(Exception):
    def __init__(self, message='Check  sintax, remember dates between [1888/01/01 - 2026/01/01/]'):
        self.message=message
        super().__init__(self.message)

class Salary(Exception):
    def __init__(self, message='Salary must be int and 0 > salary >= 9999999999999'):
        self.message=message
        super().__init__(self.message)

class Score(Exception):
    def __init__(self, message='Score must be int and 0 > salary >= 99'):
        self.message=message
        super().__init__(self.message)

class Colour(Exception):
    def __init__(self, message='Colour not founded, colour must be str'):
        self.message=message
        super().__init__(self.message)

class Nationality(Exception):
    def __init__(self, message='Country not founded, country must be str'):
        self.message=message
        super().__init__(self.message)

class Year(Exception):
    def __init__(self, message='Year not founded or not int, year must be between [1888-2027]'):
        self.message=message
        super().__init__(self.message)

class Car_No_Exist(Exception):
    def __init__(self, message='Car not founded in our list, car must be created before beeing asigned'):
        self.message=message
        super().__init__(self.message)


