class Team:
    def __init__(self,team_name,car_model,drivers,team_leader,mechanics):
        self._team_name=team_name
        self._car_model=car_model
        self._drivers=drivers
        self._team_leader=team_leader
        self._mechanics=mechanics
    team_list=[]
    @property
    def team_name(self):
        return self._team_name
    @property
    def car_model(self):
        return self._car_model
    @property
    def drivers(self):
        return self._drivers
    @property
    def team_leader(self):
        return self._team_leader
    @property
    def mechanics(self):
        return self._mechanics
    @classmethod
    def add_team(cls,other):
        Team.team_list.append(other)