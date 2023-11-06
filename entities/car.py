class Car:
    def __init__(self,model,score,colour):
        self.__model=model
        self.__score=score
        self.__colour=colour
    
    @property
    def model(self):
        return  self.__model
    @property
    def score(self):
        return  self.__score
    @property
    def colour(self):
        return  self.__colour
