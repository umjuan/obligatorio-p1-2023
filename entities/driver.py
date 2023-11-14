from entities.employee import Employee

class Driver(Employee):
    def __init__(self,id,name,age,nationality,born,salary,score,total_score,car_number,injury=False):
        super().__init__(self,id,name,age,nationality,born,salary)
        self.__score=score
        self.__total_score=total_score
        self.__car_number=car_number
        self.__injury=injury

    @property
    def score(self):
        return  self.__score
    @property
    def car_number(self):
        return  self.__car_number
    @property
    def total_score(self):
        return self.__total_score
    @total_score.setter
    def total_score(self,other):
        self.__total_score=other
    @property
    def injury(self):
        return self.__injury
    @injury.setter
    def injury(self,other):
        self.__injury=other