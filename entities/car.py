class Car:
    def __init__(self,model,score,colour):
        self._model=model
        self._score=score
        self._colour=colour
    cars = []
    
    @property
    def model(self):
        return  self._model
    @property
    def score(self):
        return  self._score
    @property
    def colour(self):
        return  self._colour
    
    def cars_list(cls):
        cars = []
        for id in Car.cars:
            x = id
            cars.append(x)
        return cars


