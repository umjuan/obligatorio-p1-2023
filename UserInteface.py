#tkinter library is used to construct the GUI.
from entities.employee import Employee
from entities.car import Car
from entities.mechanic import Mechanic
from entities.driver import Driver
from entities.director import Director
from entities.exceptions import *
import tkinter as tk
from tkinter import ttk, messagebox
#datetime helps with datestamp
import datetime

class UserInterface:

    def __init__(self):
        pass
        # global window

        # window = tk.Tk() 
        # window.geometry('500x300')
        # window.title('FIA Formula 1')

        # #Buttons
        # create_employee_button = ttk.Button(window, width=50, text="Alta Empleado", command= create_employee(2,'Pedro',23,'Uruguay', '17/08/1998', 200, 'Mechanic',300))
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
    if INV_EM_ID(id) and NE_ID(id):
        pass
    else:
        raise Invalid_Employee_id(), Non_Existent_Id    #,Invalid_Employee_Parameter

    for employee in Employee.employee_lista():
        if employee !=name and name != None and name.isalpha():
            pass
        else: 
            raise Alphabet, Team_Name_Already_in_Use
    if int(age) != None and 120>age>14 :
        pass
    else:
        raise Age
    if nationality != None and nationality.isalpha() and NATIONALITY_LIST(nationality):
            pass
    else:
        raise Nationality
    if datetime.datetime(born) != None and DATE_VALIDATION(born):
        pass
    else:
        raise Dates
    if int(salary) != None and 0>salary>9999999999999:
        pass
    else:
        raise Salary
    if INV_SC(score):
        pass
    else:
        raise Invalid_score
    if INV_SC(total_score):
        pass
    else:
        raise Invalid_score
    if car_number == int and NC_OE_CAR_NMBR(car_number):
        pass
    else:
        raise 'Car number incorrect', Car_Nmbr_Already_in_Use 
    if type == 'Mechanic':
        INV_SC(score)
        M = Mechanic(id,name,age,nationality,born,salary,score)
        M.employee_add(M)
        print(f'Created {M._name}')
    if type == 'Driver':
        INV_SC(score)
        INV_SC(total_score)
        M = Driver(id,name,age,nationality,born,salary,score,total_score,car_number)
        M._score = score
        M.employee_add(M)
        print(f'Created driver {M._name, M._car_number, M._score, M._total_score}')
    if type == 'Director':
        M = Director(id, name, age, nationality, born, salary)
        M.employee_add(M)
        print(f'Created {M._name}')

def create_car(model,year,score,colour):
    if model == str and model not in CAR_MODEL_VALIDATION(model):
        pass
    else:
        raise Car_Model_In_Use
    if year != None and YEAR(year):
        pass
    else:
        raise Year
    if score == int and INV_SC(score):
        pass
    else:
        raise Score
    if colour == str and COLOR_LIST(colour):
        pass
    else:
        raise Colour
    car = Car(model,year,score,colour)
    car.add_car(car)
    print(f'{car._model} has been created successfully')
    
def create_team(team_name,nationality,foundation_date,car_model,drivers,team_leader,mechanics):
    if team_name == str and TEAM_NAME_AIU(team_name):
        pass
    else:
        raise Alphabet, Team_Name_Already_in_Use
    if nationality != None and nationality.isalpha() and NATIONALITY_LIST(nationality):
            pass
    else:
        raise Nationality
    if datetime.datetime(foundation_date) != None and DATE_VALIDATION_TEAM(foundation_date):
        pass
    else:
        Dates_Team
    if car_model != None and car_model== str and car_model in Car.cars:
        pass
    else:
        raise Car_No_Exist
    for driver in drivers:
        if driver == int and NE_ID(driver) and EM_HAS_TEAM(driver):
            pass
        else:
            raise Non_Existent_Id, Employee_Has_A_Team
    if INV_EM_ID(team_leader) and NE_ID(team_leader) and EM_HAS_TEAM(team_leader):
        pass
    else:
        raise Non_Existent_Id, Employee_Has_A_Team
    for mechanic in mechanics:
        if INV_EM_ID(mechanic) and NE_ID(mechanic) and EM_HAS_TEAM(mechanic):
            pass
        else:
            raise Non_Existent_Id, Employee_Has_A_Team
    team = Team(team_name,nationality,foundation_date,car_model,drivers,team_leader,mechanics)
    Team.add_team(team)
    print(f'{team.team_name} has been created successfully')

        


if __name__ == '__main__':
    Ux = UserInterface()
    create_employee(3, 'Juancho',33,'Uruguay', '10/08/2020',3400, 'Mechanic',90,300,100)
    Employee.employee_lista