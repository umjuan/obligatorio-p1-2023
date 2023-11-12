import datetime
import Race
from entities.car import Car
from entities.employee import Employee
from entities.exceptions import *

class Racing_Team(Race):
    def __init__(self):
        self._teams = []
        self._nationality = ""
        self.team_car_models = []
        self._directors = []

    def create_team(self,team_name,nationality,car_model,driver_1,driver_2,driver_reserve,team_leader,mechanic_1,mechanic_2,mechanic_3,mechanic_4,mechanic_5,mechanic_6,mechanic_7,mechanic_8):
        if team_name not in self._teams and team_name != None:
            self._team_name= team_name
        else:
            raise Team_Name_Already_in_Use
        
        self._nationality = nationality
        self.team_fundation_date = datetime.datetime.now()
        self.team_car_model = [car_model]
        self.team_score = float
        self.members = [driver_1,driver_2,driver_reserve,team_leader,mechanic_1, mechanic_2, mechanic_3,mechanic_4,mechanic_5,mechanic_6,mechanic_7,mechanic_8]
        self._racers = [driver_1,driver_2,driver_reserve]
        self._mechanics = [mechanic_1, mechanic_2, mechanic_3,mechanic_4,mechanic_5,mechanic_6,mechanic_7,mechanic_8]
        self._directors = [team_leader]
        self._official_racers = [driver_1,driver_2]

    @property
    def get_teams(self):
        return self._teams
    
    @property
    def get_team_name(self):
        return self._team_name
    
    @property
    def get_team_car_model(self):
        return self.team_car_model
    
    @property
    def get_members(self):
        return self.members
    
    @property
    def get_racers(self):
        return self._racers
    
    @property
    def get_official_racers(self):
        return self._official_racers
    
    @property
    def get_directors(self):
        return self._directors
    
    @property
    def get_mechanics(self):
        return self._mechanics
    
    @_official_racers.setter
    def _official_racers(self,other):
        self._official_racers = self._official_racers.pop()
        self._official_racers.append(other)