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

    def __init__():
        global window

        window = tk.Tk() 
        window.geometry('500x300')
        window.title('FIA Formula 1')

        #Buttons
        create_employee_button = ttk.Button(window, width=50, text="Alta Empleado", command= create_employee(2,'Pedro',23,'Uruguay', '17/08/1998', 200, 'Mechanic',300))
        create_employee_button.pack()

        create_car_button = ttk.Button(window, width=50, text="Alta auto")
        create_car_button.pack()

        create_team_button = ttk.Button(window, width=50,text="Alta de equipo")
        create_team_button.pack()

        simulate_race_button = ttk.Button(window, width=50,text="Simular carrera")
        simulate_race_button.pack()

        queries_button = ttk.Button(window, width=50,text="Consultas")
        queries_button.pack()

        exit_button = ttk.Button(window, width=50,text="Exit", command=window.destroy)
        exit_button.pack()

        window.mainloop()


def create_employee(id,name,age,nationality,born,salary,type,score):
    self = Employee
    if id is int:
        pass
    else:
        raise Invalid_Employee_Parameter
    if name != None and name not in self._employees:
        pass
    else:
        raise Invalid_Employee_Parameter
    if age == int:
        pass
    else:
        raise Invalid_Employee_Parameter

    if type == 'Mechanic':
        M = Mechanic(id,name,age,nationality,born,salary,score)
    # if type == 'Driver':
    #     M = Driver(id,name,age,nationality,born,salary,score,total_score,car_number)
    #     M.total_score(total_score)
    #     M.__car_number = car_number

    if type == 'Director':
        M = Director(id, name, age, nationality, born, salary)

UI = UserInterface
UI.__init__()