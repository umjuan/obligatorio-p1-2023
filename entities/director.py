from entities.employee import Employee

class Director(Employee):
    def __init__(self, id, name, age, nationality, born, salary):
        super().__init__(id, name, age, nationality, born, salary)
        self.type = 'director'
    def isemployee(self):
        pass

