from entities.employee import Employee
from entities.team import Team
from entities.car import Car
from entities.driver import Driver
from entities.director import Director
from entities.mechanic import Mechanic
from exceptions.exceptions import *
from datetime import datetime
from helpers import *

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
    def param(self):
        listparam=self.param.replace(' ','')
        listparam=listparam.split(',')
        for i in listparam:
            if listparam.count(i)>1: listparam.remove(i)
        return listparam
    
    @property
    def param2(self):
        listparam=self.param2.replace(' ','')
        listparam=listparam.split(',')
        return listparam
    
    @property
    def param3(self):
        listparam=self.param3.replace(' ','')
        listparam=listparam.split(',')
        return listparam
    
    def get_left_race(self):
        listcomp=[]
        listpivot1=[]
        listpivot=self.param
        for y in Employee.employee_list:
            for z in listpivot:
                if y.type=='driver' and z==y.car_number:
                    listpivot1.append(y.id)
                
        for i in Team.team_list:
            count=0
            listteam=[]
            listteam.append(i.team_name)
            for x in i.drivers:
                if not x in listpivot1 and count<2:
                    listteam.append(x)
                    count+=1
            listcomp.append(listteam)
        return listcomp


    
    def get_pits_error(self):
        listcomp=[]
        listpivot1=[]
        listpivot=self.param2
        for y in Employee.employee_list:
            for z in listpivot:
                if y.type=='driver' and z==y.car_number:
                    listpivot1.append(y.id)
        
        for i in Team.team_list:
            listteam=[]
            listteam.append(i.team_name)
            for x in listpivot1:
                if x in i.drivers:
                    x.append(listteam)
            listcomp.append(listteam)    
        return listcomp

    
    def get_penalties(self):
        listcomp=[]
        listpivot1=[]
        listpivot=self.param3
        for y in Employee.employee_list:
            for z in listpivot:
                if y.type=='driver' and z==y.car_number:
                    listpivot1.append(y.id)
        
        for i in Team.team_list:
            listteam=[]
            listteam.append(i.team_name)
            for x in listpivot1:
                if x in i.drivers:
                    x.append(listteam)
            listcomp.append(listteam)    
        return listcomp

    
    @property
    def racers(self):
        return self._racers
    
    @property
    def teams(self):
        return self._teams

    @property
    def  results(self):
        return self._results
    
    def simulate_race(self):
        self.regist_unexpected()
        cars = []
        mechanics = []
        drivers = []
        # for employee in Employee.employee_list:
        #     if employee.type == 'mechanic':
        #         employee.m_score = []
        #         x = employee.score
        #         employee.m_score.append(x)
        #         mechanics.append(employee.m_score) 
        #     if employee.type == 'driver' and employee.injury == False:
        #         cars.append(employee._car_number)
        for team in Team.team_list:
            
            racing_team = {team._name, team._car_model, team._drivers, team._mechanics, team._team_leader}
            self._teams.append(racing_team)
            driver_score = []
            mechanic_score = []
            

            for driver in team._drivers:
                if driver in NE_ID():
                    for employee in Driver.employee_list:
                        if employee.id == driver:
                            driver_score.append(employee._total_score)
            driver_score = sum(driver_score)
            drivers.append(driver_score)

            for mechanic in team._mechanics:
                if mechanic in NE_ID():
                    for employee in Mechanic.employee_list:
                        if employee.id == mechanic:
                            mechanic_score.append(employee._score)
            mechanic_score = sum(mechanic_score)
            mechanics.append(mechanic_score)
            
        if self.get_left_race in cars:
            cars.remove(self.get_left_race)
        else:
            raise Car_No_Exist
        if self.get_pits_error in cars:
            self.pit_error = 1
        else:
            raise Car_No_Exist
        if self.get_penalties in cars:
            self.penalities = 1  
        else:
            raise Car_No_Exist
        grid_mechanics = []
        for grid_score in mechanics:
            grid_mechanics.append(grid_score)
    
        grid_results = [team for team in grid_mechanics,score_auto + score_piloto –
5*cantidad_errores_en_pits - 8*cantidad_penalidad_infringir_norma

        for car in cars:


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