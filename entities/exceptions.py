class Invalid_Employee_Parameter(Exception):

    def __init__(self, message='one or many of the employee\'s parameters given were incorrect, be it by type or length'):
        self.message=message
        super().__init__(self.message)


class Invalid_Car_Parameter(Exception):

    def __init__(self, message='one or many of the car\'s parameters given were incorrect'):
        self.message=message
        super().__init__(self.message)

class Employee_Has_A_Team(Exception):

    def __init__(self, message='self descriptive'):
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

class Non_Existent_Car_Nmbr(Exception):

    def __init__(self, message='self descriptive'):
        self.message=message
        super().__init__(self.message)

class Non_Existent_Id(Exception):

    def __init__(self, message='self descriptive'):
        self.message=message
        super().__init__(self.message)

class Non_Existent_Team(Exception):

    def __init__(self, message='self descriptive'):
        self.message=message
        super().__init__(self.message)

class Repeating_Parameters(Exception):

    def __init__(self, message='two or more parameters are the same'):
        self.message=message
        super().__init__(self.message)

class Void_Parameter(Exception):

    def __init__(self, message='one or many required paramethers weren\'t given'):
        self.message=message
        super().__init__(self.message)

    