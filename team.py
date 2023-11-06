class Team:
    def __init__(self,team_name,car_model,driver_1,driver_2,driver_reserve,team_leader,mechanic_1,mechanic_2,mechanic_3,mechanic_4,mechanic_5,mechanic_6,mechanic_7,mechanic_8):
        self.__team_name=team_name
        self.__car_model=car_model
        self.__driver_1=driver_1
        self.__driver_2=driver_2
        self.__driver_reserve=driver_reserve
        self.__team_leader=team_leader
        self.__mechanic_1=mechanic_1
        self.__mechanic_2=mechanic_2
        self.__mechanic_3=mechanic_3
        self.__mechanic_4=mechanic_4
        self.__mechanic_5=mechanic_5
        self.__mechanic_6=mechanic_6
        self.__mechanic_7=mechanic_7
        self.__mechanic_8=mechanic_8
    
    @property
    def team_name(self):
        return self.__team_name
    @property
    def car_model(self):
        return self.__car_model
    @property
    def driver_1(self):
        return self.__driver_1
    @driver_1.setter
    def driver_1(self,other):
        self.__driver_1=other
    @property
    def driver_2(self):
        return self.__driver_2
    @property
    def driver_reserve(self):
        return self.__driver_reserve
    @property
    def team_leader(self):
        return self.__team_leader