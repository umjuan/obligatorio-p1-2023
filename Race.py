from entities.employee import Employee
from entities.team import Team
from entities.car import Car
from entities.driver import Driver
from entities.director import Director
from entities.mechanic import Mechanic
from exceptions.exceptions import *
from datetime import datetime

class Race(object):
    
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
                    listteam.append(x)
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
                    listteam.append(x)
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
        part=self.get_left_race()
        listrace=[]
        for i in part:
            listdriver=[]
            if len(i)!=1:
                for x in i[1:]:
                    lista=[]
                    suma1=0
                    for z in Team.team_list:
                        if x in z.drivers:
                            num=[n for n in z.mechanics]
                            num1=int(z.car_model.score)
                            num3=z.team_leader
                            break
                    for y in Employee.employee_list:
                        if x==y.id:
                            num2=int(y.score)
                        if num3==y.id:
                            num4=int(y.score)
                        for w in num:
                            if w==y.id:
                                suma1+=int(y.score)
                                break
                    sumafinal=num1+num2+num4+suma1
                    lista.append(x)
                    lista.append(i[0])
                    lista.append(sumafinal)
                    listdriver.append(lista)       
            listrace.append(listdriver)
        part1=self.get_pits_error()
        for i in part1:
            for x in range(len(listrace)):
                num8=part1.count(listrace[x][0])
                listrace[x][2]-=num8*5
        part2=self.get_penalties()
        for i in part1:
            for x in range(len(listrace)):
                num8=part1.count(listrace[x][0])
                listrace[x][2]-=num8*8
        for i in listrace:
            print(i)
                
                




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