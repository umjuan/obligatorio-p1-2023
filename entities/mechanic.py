from entities.employee import Employee

class Mechanic(Employee):
    def __init__(self,id,name,age,nationality,born,salary,score):
        super().__init__(self,id,name,age,nationality,born,salary)
        self.__score=score

    @property
    def score(self):
        return self.__score
    