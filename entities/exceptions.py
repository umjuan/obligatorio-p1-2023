from employee import Employee
from mechanic import Mechanic
from driver import Driver
from team_leader import Team_leader
from team import Team

class Invalid_Employee_id(Exception):

    def __init__(self, message='id length has to be of eight characters, only digits accepted'):
        self.message=message
        super().__init__(self.message)

class Invalid_score(Exception):

    def __init__(self, message='score is a number between and including 1-99'):
        self.message=message
        super().__init__(self.message)

'''class Invalid_Car_Parameter(Exception):

    def __init__(self, message='one or many of the car\'s parameters given were incorrect'):
        self.message=message
        super().__init__(self.message)
        '''

class Employee_Has_A_Team(Exception):

    def __init__(self, message='self descriptive'):
        self.message=message
        super().__init__(self.message)

class Team_Name_Already_in_Use(Exception):

    def __init__(self, message='self descriptive'):
        self.message=message
        super().__init__(self.message)

class Car_Nmbr_Already_in_Use(Exception):

    def __init__(self, message='self descriptive'):
        self.message=message
        super().__init__(self.message)

class Non_Competing_Or_Existing_Car_Nmbr(Exception):

    def __init__(self, message='self descriptive'):
        self.message=message
        super().__init__(self.message)

class Non_Existent_Id(Exception):

    def __init__(self, message='self descriptive'):
        self.message=message
        super().__init__(self.message)


class Repeating_Parameters(Exception):

    def __init__(self, message='two or more parameters are the same'):
        self.message=message
        super().__init__(self.message)

class Void_Parameter(Exception):

    def __init__(self, message='one or many required paramethers weren\'t given'):
        self.message=message
        super().__init__(self.message)

def NE_ID (ide):                                       #Chequea si la id de un empleado existe, devuelve eror                                                      
    lista=[i.id for i in Employee.employee_list]       #si negativo, usado cuando se añade un empl. a un equipo
    if ide not in lista: raise Non_Existent_Id()

def INV_EM_ID(ide):                                #chequea si la id dada es valida en cuanto a su sintaxis
    if len(ide)!=8: raise Invalid_Employee_id()
    for i in list(ide):
        if i not in ['0','1','2','3','4','5','6','7','8','9']:
            raise Invalid_Employee_id()

def INV_SC(sco):                                #chequea si un score dado es correcto
    if len(sco)>2:raise Invalid_score()
    for i in list(sco):
        if i not in ['0','1','2','3','4','5','6','7','8','9']:
            raise Invalid_Employee_id()

def EM_HAS_TEAM (ide):          #chequea si un empleado ya tiene un equipo antes de añadirlo a uno 
    lista=[]
    for i in Team.team_list:
        lista.extend(i.drivers)
        lista.extend(i.mechanics)
        lista.extend(i.team_leader)
    lista=[x.id for x in lista]
    if ide in lista: raise Employee_Has_A_Team()

def TEAM_NAME_AIU(name):                  #chqequea que no se este usando el mismo nombre para dos equipos
    lista= [i.team_name for i in Team.team_list]
    if name in lista:
        raise Team_Name_Already_in_Use()

def CAR_NMBR_AIU_(number):             #chequea que un piloto no repita su numero de auto
    for i in Employee.employee_list:     #usado cuando se crea un piloto
        if i.type=='driver':
            if number==i.car_number:
                raise Car_Nmbr_Already_in_Use()
            
def NC_OE_CAR_NMBR (number):         #chequea si el numero de auto dado es de un piloto que compite
    lista=[]                         #usado durante la carrera
    for i in Team.team_list:
        lista.extend(i.drivers)
    lista=[x.id for x in lista]
    if number not in lista:
        raise Non_Competing_Or_Existing_Car_Nmbr()
    