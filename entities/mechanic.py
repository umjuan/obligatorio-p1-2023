from entities.employee import Employee

class Mechanic(Employee):
    def __init__(self,id,name,age,nationality,born,salary,score):
        Employee.__init__(self,id,name,age,nationality,born,salary)
        self._score=score
        self.type='mechanic'
    @property
    def score(self):
        return self._score
    