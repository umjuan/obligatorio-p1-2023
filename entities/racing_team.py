import datetime
import Race
class Racing_Team(Race):
    def __init__(self):
        self._team_name= ""
        self._nationality = ""
        self.team_fundation_date = datetime.datetime.now()
        self.team_car_model = []
        self.team_score = float
        self.members = []
        self._racers = []
        self._mechanics = []
        self._directors = []
        self._official_racers = []

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