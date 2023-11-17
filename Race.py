from entities.employee import Employee
from entities.team import Team
from entities.car import Car
from entities.driver import Driver
from entities.director import Director
from entities.mechanic import Mechanic
from exceptions.exceptions import *
from datetime import datetime

class Race(object):
    employees = Employee
    drivers = Driver
    directors = Director
    cars = Car
    

    def __init__(self):
        teams = Team
        employees = Employee
        drivers = Driver
        directors = Director
        self._racers = []
        self._teams = []
        self._results = []

    def regist_unexpected(self):
        self.param = list(input('Insert comma separated racers number which left the race. '))
        self.param2 = list(input('Insert racer numbers who reported errors in pits. '))
        self.param3 = list(input('Insert racer numbers being penalized for breaking racing rules. '))

    @property
    def get_param(self):
        return self.param
    
    @property
    def get_param2(self):
        return self.param2
    
    @property
    def get_param3(self):
        return self.param3
    
    def get_left_race(self):
        return self.get_param
    
    def get_pits_error(self):
        return self.get_param2
    
    def get_penalties(self):
        return self.get_param3
    
    @property
    def get_racers(self):
        return self._racers
    
    @property
    def get_teams(self):
        return self._teams

    @property
    def get_results(self):
        return self._results
    
    def simulate_race(self):
        self.regist_unexpected
        teams = Team
        employees = Employee
        drivers = Driver
        directors = Director
        cars = Car.cars
        if self.get_left_race in cars:
            self.cars = self.cars - self.get_param
        if self.get_pits_error in cars:
            self.cars = self.cars - self.get_pits_error
        if self.get_penalties in cars:
            self.cars = self.cars - self.get_penalties
        for faults in self.cars:
            cars.append(faults)

    def query_top10_chmp(self):
        #Perform query
        pass

    def query_top5_salary(self):
        #Query
        pass        

    def query_top3_racers(self):
        #Query
        pass

    def query_team_director(self):
        #Query
        pass

    def query_team_chmp_results(self):
        #Query
        pass