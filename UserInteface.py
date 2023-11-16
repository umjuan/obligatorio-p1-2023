#tkinter library is used to construct the GUI.
from entities.employee import Employee
from entities.exceptions import *
from entities.mechanic import Mechanic
from entities.driver import Driver
from entities.director import Director
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
    # else:
    #     raise Invalid_Employee_Parameter
    if int(age) != None and 120>age>14 :
        pass
    else:
        raise Age
    if nationality != None and nationality.isalpha():
            pass
    else:
        raise nationality
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
    
    '''
    remaining car_number validation
    '''

    # if nationality != None and nationality == str:
    #     pass
    # else:
    #     raise Invalid_Employee_Parameter
    # if born != None and born == datetime:
    #     pass
    # else:
    #     raise Invalid_Employee_Parameter
    # if salary != None and salary == int:
    #     pass
    # else:
    #     raise Invalid_Employee_Parameter
    # if score != None and score == int and score >= 0 <=99:
    #     pass
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
        print(f'Created driver {M._name, M._car_number, M._score, M._total_score}<')
    if type == 'Director':
        M = Director(id, name, age, nationality, born, salary)
        M.employee_add(M)
        print(f'Created {M._name}')

if __name__ == '__main__':
    Ux = UserInterface()
    create_employee(3, 'Juancho',33,'Uruguay', '10/08/2020',3400, 'Mechanic',90,300,100)
    Employee.employee_lista