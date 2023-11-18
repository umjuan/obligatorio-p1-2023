class Car:
    def __init__(self,model,year,score,colour):
        self._model=model
        self._year =year
        self._score=score
        self._colour=colour
        self._pit_error=''
        self._penality=''

    cars = []
    
    @property
    def model(self):
        return  self._model
    @property
    def year(self):
        return self._year
    @property
    def score(self):
        return  self._score
    @property
    def colour(self):
        return  self._colour
    @classmethod
    def add_car(cls,other):
        Car.cars.append(other)
    
    def cars_list(cls):
        return cls.cars


