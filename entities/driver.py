from entities.employee import Employee

class Driver(Employee):
    def __init__(self,id,name,age,nationality,born,salary,score,total_score,car_number,injury=False):
        Employee.__init__(self,id,name,age,nationality,born,salary)
        self._score=score
        self._total_score=total_score
        self._car_number=car_number
        self._injury=injury
        self.type='driver'
    @property
    def score(self):
        return  self._score
    @property
    def car_number(self):
        return  self._car_number
    @property
    def total_score(self):
        return self._total_score
    @total_score.setter
    def total_score(self,other):
        self._total_score=other
    @property
    def injury(self):
        return self._injury
    @injury.setter
    def injury(self,other):
        self._injury=other
    def isemployee(self):
        pass