from employee import Employee
from car import Car
from mechanic import Mechanic
from driver import Driver
from team_leader import Team_leader
from team import Team
from datetime import datetime

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

class Car_Model_In_Use(Exception):

    def __init__(self, message='This car model is represented by another team, check values'):
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

class Alphabet(Exception):

    def __init__(self, message='check syntax issues, only alphabet characters available'):
        self.message=message
        super().__init__(self.message)

class Age(Exception):

        def __init__(self, message='Check age range of years [15-120] dates between [1888/01/01 - 2008/01/01/]'):
            self.message=message
            super().__init__(self.message)

class Nacionality(Exception):
    def __init__(self, message='Check nationality sintax, remember must use alphabet characters'):
        self.message=message
        super().__init__(self.message)

class Dates(Exception):
    def __init__(self, message='Check nationality sintax, remember must use alphabet characters'):
        self.message=message
        super().__init__(self.message)

class Salary(Exception):
    def __init__(self, message='Salary must be int and 0 > salary >= 9999999999999'):
        self.message=message
        super().__init__(self.message)

class Score(Exception):
    def __init__(self, message='Score must be int and 0 > salary >= 99'):
        self.message=message
        super().__init__(self.message)

class Colour(Exception):
    def __init__(self, message='Colour not founded, colour must be str'):
        self.message=message
        super().__init__(self.message)

class Nationality(Exception):
    def __init__(self, message='Country not founded, country must be str'):
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
    if 0>len(sco)>2:
        for i in list(sco):  
            if i not in ['0','1','2','3','4','5','6','7','8','9']:
                raise Score()
        pass

def EM_HAS_TEAM (ide):          #chequea si un empleado ya tiene un equipo antes de añadirlo a uno 
    lista=[]
    for i in Team.team_list:
        lista.extend(i.drivers)
        lista.extend(i.mechanics)
        lista.extend(i.team_leader)
        if ide in lista: raise Employee_Has_A_Team()

def TEAM_NAME_AIU(name):                  #chequea que no se este usando el mismo nombre para dos equipos
    lista= [i.team_name for i in Team.team_list]
    if name in lista:
        raise Team_Name_Already_in_Use()

def CAR_NMBR_AIU_(number):             #chequea que un piloto no repita su numero de auto
    for i in Employee.employee_list:     #usado cuando se crea un piloto
        if i.type=='driver':
            if number==i.car_number:
                raise Car_Nmbr_Already_in_Use()
            
def NC_OE_CAR_NMBR(number):         #chequea si el numero de auto dado es de un piloto que compite
    lista=[]                                  #usado durante la carrera
    for i in Team.team_list:
        lista.extend(i.drivers)
    lista1=[x.car_number for x in Employee.employee_list if x.id in lista ]
    if number not in lista1:
        raise Non_Competing_Or_Existing_Car_Nmbr()

def REP_PAR (lista):               #revisa que no se use un parametro repetido
    for i in lista:                #e.g.: pilotos que abandonaron (no se puesde repetir)
        if lista.count(i)>1:
            raise Repeating_Parameters()
        
def DATE_VALIDATION (date):
    date_obj  = datetime.strptime(date, '%Y-%m-%d').date()
    startDate = datetime.datetime(1888, 1, 1, 00, 00, 00).date()
    endDate   = datetime.strptime(2008, 1, 1, 00, 00, 00).date()
    # check if dateObj is between startDate and endDate
    if startDate <= date_obj <= endDate:
        return True
    
def CAR_MODEL_VALIDATION(model):
    if model == str:
        pass
    lista=[]                                  #usado durante la carrera
    for car in Car.cars_list:
        lista.append(car)
    return lista

def COLOR_LIST(colour):
    simplify = colour.lower()
    colours =[i.lower() for i in ["Red", "Blue", "Green", "Yellow", "Orange", "Purple", "Pink", "Brown", "Gray",
            "White",  "Black", "Turquoise", "Lavender", "Magenta", "Cyan", "Indigo", "Maroon",
            "Gold", "Silver",  "Olive", "Teal", "Peach", "Coral", "Violet", "Charcoal", "Beige",
            "Mint", "Ruby", "Slate",  "Salmon", "Aqua", "Tan", "Navy", "Khaki", "Crimson", "Lime",
            "Rose", "Brick", "Amber",  "Mustard", "Periwinkle", "Sapphire", "Sienna", "Plum", "Aquamarine",
            "Apricot", "Chartreuse",  "Cerulean", "Tangerine", "Rust", "Mulberry", "Ivory", "Emerald", "Steel", "Burgundy",
            "Forest Green", "Cornflower Blue", "Sky Blue", "Melon", "Pumpkin", "Ochre", "Denim",  "Cobalt", "Mauve", "Moccasin",
            "Papaya Whip", "Wheat", "Slate Gray", "Turmeric", "Honeydew",  "Orchid", "Electric Blue", "Fuchsia", "Lemon", "Misty Rose",
            "Salmon Pink", "Thistle",  "Powder Blue", "Hot Pink", "Midnight Blue", "Chocolate", "Olive Drab", "Pine Green",  "Tomato", "Firebrick",
            "Dodger Blue", "Linen", "Navajo White",  "Alice Blue", "Azure", "Bisque", "Blanched Almond", "Burlywood", "Cadet Blue", "Chocolate", 
            "Cornsilk", "Dark Goldenrod", "Dark Khaki", "Dark Olive Green", "Dark Orange", "Dark Orchid",  "Dark Salmon", "Dark Sea Green", "Dark Slate Blue",
            "Dark Slate Gray", "Dark Turquoise",  "Deep Pink", "Deep Sky Blue", "Dim Gray", "Dodger Blue", "Firebrick", "Floral White", "Forest Green",
            "Gainsboro", "Ghost White", "Gold", "Goldenrod", "Green Yellow", "Honeydew", "Hot Pink", "Indian Red",  "Ivory", "Khaki", "Lavender Blush",
            "Lemon Chiffon", "Light Blue", "Light Coral", "Light Cyan",  "Light Goldenrod", "Light Goldenrod Yellow", "Light Gray", "Light Green",
            "Light Pink", "Light Salmon",  "Light Sea Green", "Light Sky Blue", "Light Slate Gray", "Light Steel Blue", "Light Yellow", "Linen",  "Magenta",
            "Maroon", "Medium Aquamarine", "Medium Blue", "Medium Orchid", "Medium Purple", "Medium Sea Green",  "Medium Slate Blue", "Medium Spring Green", 
            "Medium Turquoise", "Medium Violet Red", "Midnight Blue",  "Mint Cream", "Misty Rose", "Moccasin", "Navajo White", "Navy", "Old Lace", "Olive",
            "Olive Drab",  "Orange", "Orange Red", "Orchid", "Pale Goldenrod", "Pale Green", "Pale Turquoise", "Pale Violet Red",  "Papaya Whip", "Peach Puff",
            "Peru", "Pink", "Plum", "Powder Blue", "Purple", "Red", "Rosy Brown",  "Royal Blue", "Saddle Brown", "Salmon", "Sandy Brown", "Sea Green", "Seashell",
            "Sienna", "Silver",  "Sky Blue", "Slate Blue", "Slate Gray", "Snow", "Spring Green", "Steel Blue", "Tan", "Teal", "Thistle",  "Tomato", "Turquoise", "Violet",
            "Wheat", "White", "White Smoke", "Yellow", "Yellow Green"]]
    if simplify in colours:
        pass
    
def NATIONALITY_LIST(nationality):
    simplify = nationality.lower()
    nationalies = [i.lower() for i in["Afghanistan", "Albania", "Algeria", "Andorra", "Angola", "Antigua and Barbuda", "Argentina", "Armenia", "Australia",
            "Austria", "Azerbaijan", "Bahamas", "Bahrain", "Bangladesh", "Barbados", "Belarus", "Belgium", "Belize", "Benin",
            "Bhutan", "Bolivia", "Bosnia and Herzegovina", "Botswana", "Brazil", "Brunei", "Bulgaria", "Burkina Faso", "Burundi",
            "Cabo Verde", "Cambodia", "Cameroon", "Canada", "Central African Republic", "Chad", "Chile", "China", "Colombia",
            "Comoros", "Congo (Congo-Brazzaville)", "Costa Rica", "Croatia", "Cuba", "Cyprus", "Czechia (Czech Republic)", "Denmark",
            "Djibouti", "Dominica", "Dominican Republic", "East Timor (Timor-Leste)", "Ecuador", "Egypt", "El Salvador", "Equatorial Guinea",
            "Eritrea", "Estonia", "Eswatini", "Ethiopia", "Fiji", "Finland", "France", "Gabon", "Gambia", "Georgia", "Germany", "Ghana",
            "Greece", "Grenada", "Guatemala", "Guinea", "Guinea-Bissau", "Guyana", "Haiti", "Honduras", "Hungary", "Iceland", "India",
            "Indonesia", "Iran", "Iraq", "Ireland", "Israel", "Italy", "Ivory Coast", "Jamaica", "Japan", "Jordan", "Kazakhstan", "Kenya",
            "Kiribati", "Korea, North", "Korea, South", "Kosovo", "Kuwait", "Kyrgyzstan", "Laos", "Latvia", "Lebanon", "Lesotho", "Liberia",
            "Libya", "Liechtenstein", "Lithuania", "Luxembourg", "Madagascar", "Malawi", "Malaysia", "Maldives", "Mali", "Malta", "Marshall Islands",
            "Mauritania", "Mauritius", "Mexico", "Micronesia", "Moldova", "Monaco", "Mongolia", "Montenegro", "Morocco", "Mozambique", "Myanmar",
            "Namibia", "Nauru", "Nepal", "Netherlands", "New Zealand", "Nicaragua", "Niger", "Nigeria", "North Macedonia", "Norway", "Oman",
            "Pakistan", "Palau", "Panama", "Papua New Guinea", "Paraguay", "Peru", "Philippines", "Poland", "Portugal", "Qatar", "Romania",
            "Russia", "Rwanda", "Saint Kitts and Nevis", "Saint Lucia", "Saint Vincent and the Grenadines", "Samoa", "San Marino",
            "Sao Tome and Principe", "Saudi Arabia", "Senegal", "Serbia", "Seychelles", "Sierra Leone", "Singapore", "Slovakia", "Slovenia",
            "Solomon Islands", "Somalia", "South Africa", "South Sudan", "Spain", "Sri Lanka", "Sudan", "Suriname", "Sweden", "Switzerland",
            "Syria", "Taiwan", "Tajikistan", "Tanzania", "Thailand", "Togo", "Tonga", "Trinidad and Tobago", "Tunisia", "Turkey",
            "Turkmenistan", "Tuvalu", "Uganda", "Ukraine", "United Arab Emirates", "United Kingdom", "United States", "Uruguay",
            "Uzbekistan", "Vanuatu", "Vatican City", "Venezuela", "Vietnam", "Yemen", "Zambia", "Zimbabwe"]]
    if simplify in nationalies:
        pass