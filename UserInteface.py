#tkinter library is used to construct the GUI.
import Race
from helpers import *
# from entities.employee import Employee
# from entities.car import Car as Car
# from entities.mechanic import Mechanic as Mechanic
# from entities.driver import Driver as Driver
# from entities.director import Director as Director
from exceptions.exceptions import *
import tkinter as tk
from tkinter import ttk, messagebox
#datetime helps with datestamp
from datetime import datetime

class UserInterface:

    def __init__(self):
        pass
        # r = Race
        # global window

        # window = tk.Tk() 
        # window.geometry('500x300')
        # window.title('FIA Formula 1')

        # #Buttons
        # create_employee_button = ttk.Button(window, width=50, text="Alta Empleado", command= print("Debug"))
        # create_employee_button.pack()

        # create_car_button = ttk.Button(window, width=50, text="Alta auto")
        # create_car_button.pack()

        # create_team_button = ttk.Button(window, width=50,text="Alta de equipo")
        # create_team_button.pack()

        # simulate_race_button = ttk.Button(window, width=50,text="Simular carrera")
        # simulate_race_button.pack()

        # queries_button = ttk.Button(window, width=50,text="Consultas")
        # queries_button.pack()

        # exit_button = ttk.Button(window, width=50,text="Exit", command=window.destroy)
        # exit_button.pack()

        # window.mainloop()


def create_employee(id,name,age,nationality,born,salary,type,score,total_score,car_number):
    if len(id) == 8 and id not in Employee.employee_list:
        pass
    else:
        raise Invalid_Employee_id or Non_Existent_Id    #,Invalid_Employee_Parameter

    for employee in Employee.employee_list:
        if name.isalpha() and name not in employee.name:
            pass
        else: 
            raise Alphabet or Team_Name_Already_in_Use
    if int(age) != None and 120>int(age)>14 :
        pass
    else:
        raise Age
    if nationality != None and nationality in NATIONALITY_LIST():
            pass
    else:
        raise Nationality
    if DATE_VALIDATION(born):
        pass
    else:
        raise Dates
    if int(salary) != None and int(salary)>0:
        pass
    else:
        raise Salary
    if int(score) in INV_SC():
        pass
    else:
        raise Invalid_score
    if int(total_score) in INV_SC():
        pass
    else:
        raise Invalid_score
    if int(car_number) not in NC_OE_CAR_NMBR():
        pass
    else:
        raise Car_Nmbr_Already_in_Use 
    if type == 'Mechanic':
        M = Mechanic(id,name,age,nationality,born,salary,score)
        M.isemployee()
        M.employee_add(M)
        print(f'Created {M._name, M.score, M.type}')
    if type == 'Driver':
        M = Driver(id,name,age,nationality,born,salary,score,total_score,car_number)
        M.isemployee()
        M._score = score
        M.employee_add(M)
        print(f'Created {M._name, M.type, M._car_number, M._score, M._total_score}')
    if type == 'Director':
        M = Director(id, name, age, nationality, born, salary)
        M.isemployee()
        M.employee_add(M)
        print(f'Created {M._name, M.type}')

def create_car(model,year,score,colour):
    if model not in CAR_MODEL_VALIDATION():
        pass
    else:
        raise Car_Model_In_Use
    if  int(year) in YEAR():
        pass
    else:
        raise Year
    if int(score) in INV_SC():
        pass
    else:
        raise Score
    if colour.lower() in COLOR_LIST():
        pass
    else:
        raise Colour
    car = Car(model,year,score,colour)
    car.add_car(car)
    print(f'{car._model} has been created successfully')

def create_team(team_name,nationality,foundation_date,car_model,drivers,team_leader,mechanics):
    if team_name not in TEAM_NAME_AIU():
        pass
    else:
        raise Alphabet or Team_Name_Already_in_Use
    if nationality != None and nationality in NATIONALITY_LIST():
            pass
    else:
        raise Nationality
    if DATE_VALIDATION_TEAM(foundation_date):
        pass
    else:
        Dates_Team
    if car_model in CAR_MODEL_VALIDATION():
        pass
    else:
        raise Car_No_Exist
    for driver in drivers:
        if str(driver) in NE_ID() and str(driver) not in EM_HAS_TEAM():
            pass
        else:
            raise Non_Existent_Id or Employee_Has_A_Team
    if team_leader in NE_ID() and team_leader not in EM_HAS_TEAM():
        pass
    else:
        raise Non_Existent_Id or Employee_Has_A_Team
    for mechanic in mechanics:
        if mechanic in NE_ID() and mechanic not in EM_HAS_TEAM():
            pass
        else:
            raise Non_Existent_Id or Employee_Has_A_Team
    team = Team(team_name,nationality,foundation_date,car_model,drivers,team_leader,mechanics)
    Team.add_team(team)
    print(f'{team.team_name} has been created successfully')

if __name__ == '__main__':
    Ux = UserInterface()
    # R = Race()
    #id,name,age,nationality,born,salary,type,score,total_score,car_number
    create_employee('49714935','Juancho','25',"Uruguay",'17/08/1998','3400','Mechanic','90','80','18')
    create_employee('49714936','Daniel','23',"Uruguay",'19/01/1999','3400','Mechanic','90','80','18')
    create_employee('49751535','Jorge','24',"Uruguay",'17/08/1998','3400','Mechanic','70','10','18')
    create_employee('49600135','Romina','25',"Uruguay",'17/08/1998','3400','Mechanic','67','60','18')
    create_employee('49302125','Lucia','27',"Uruguay",'17/08/1998','3400','Mechanic','78','80','18')
    create_employee('41111111','Andres','29',"Uruguay",'17/08/1998','3400','Mechanic','76','80','18')
    create_employee('43234935','Ramon','33',"Uruguay",'17/08/1998','3400','Mechanic','56','80','18')
    create_employee('46789135','Nataniel','55',"Uruguay",'17/08/1998','3400','Mechanic','61','80','18')
    create_employee('43589135','Marcusse','55',"Uruguay",'17/08/1968','3400','Mechanic','61','80','18')
    create_employee('43589135','Ronald','57',"United States",'17/08/1968','3400','Director','61','80','18')
    create_employee('46788911','Pedro','25',"Argentina",'17/08/1998','4400','Driver','90','80','77')
    create_employee('41308911','Joaquin','25',"Argentina",'01/01/1998','4400','Driver','90','80','11')
    create_employee('44988911','Rodrigo','25',"Argentina",'05/08/1995','4900','Driver','90','80','55')
    create_car('Alfa','2004','30','red')
    create_car('Lambo','2004','30','red')
    create_team('Scuderia', 'Uruguay', '14/12/2005','Lambo',['46788911','41308911','44988911'],'43589135',['43589135','46789135','43234935','41111111','49302125','49600135','49751535','49714936','49714935'])
    
    print(Employee.employee_list)
    print(Team.team_list)