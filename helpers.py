from entities.employee import Employee
from entities.team import Team
from entities.car import Car
from entities.driver import Driver
from entities.director import Director
from entities.mechanic import Mechanic
from exceptions.exceptions import *
from datetime import datetime

def NE_ID():                                       #Chequea si la id de un empleado existe, devuelve eror                                                      
    lista = Employee.employee_list       #si negativo, usado cuando se añade un empl. a un equipo
    return lista

def INV_EM_ID(ide):                                #chequea si la id dada es valida en cuanto a su sintaxis
    if len(ide) ==8:
        pass
    else:
        raise Invalid_Employee_id()
    # for x in list(ide):
    #     if x not in ['0','1','2','3','4','5','6','7','8','9']:
    #         raise Invalid_Employee_id()

def INV_SC():                                #chequea si un score dado es correcto
        scores = [x for x in range(0,100)]
        return scores

def EM_HAS_TEAM(ide):          #chequea si un empleado ya tiene un equipo antes de añadirlo a uno 
    lista=[]
    for i in Team.team_list:
        lista.extend(i.drivers)
        lista.extend(i.mechanics)
        lista.extend(i.team_leader)
        if ide in lista: raise Employee_Has_A_Team()
        else: pass

def TEAM_NAME_AIU(name):                  #chequea que no se este usando el mismo nombre para dos equipos
    lista= [i.team_name for i in Team.team_list]
    if name in lista:
        raise Team_Name_Already_in_Use()
    else:
        pass

def CAR_NMBR_AIU_(number):             #chequea que un piloto no repita su numero de auto
    for i in Employee.employee_list:     #usado cuando se crea un piloto
        if i.type=='driver':
            if number==i.car_number:
                raise Car_Nmbr_Already_in_Use()
            
def NC_OE_CAR_NMBR():         #chequea si el numero de auto dado es de un piloto que compite
    lista=[]                                  #usado durante la carrera
    for i in Team.team_list:
        for driver in i.drivers:
            x = driver.car_number
            lista.append(x)
    return lista
    #     lista.extend(i._drivers)
    # lista1=[x.car_number for x in Employee.employee_list if x.id in lista ]
    # if number not in lista1:
    #     raise Non_Competing_Or_Existing_Car_Nmbr()

def REP_PAR (lista):               #revisa que no se use un parametro repetido
    for i in lista:                #e.g.: pilotos que abandonaron (no se puesde repetir)
        if lista.count(i)>1:
            raise Repeating_Parameters()
        
def DATE_VALIDATION(date):
    date_obj  = datetime.strptime(date, '%d/%m/%Y').date()
    startDate = datetime.strptime('01/01/1888','%d/%m/%Y').date()
    endDate   = datetime.strptime('31/12/2008','%d/%m/%Y').date()
    # check if dateObj is between startDate and endDate
    if startDate <= date_obj <= endDate:
        return True
    
def CAR_MODEL_VALIDATION(model):
    if model == str:
        lista=[]                                  #usado durante la carrera
        for car in Car.cars_list:
            lista.append(car)
        return lista

def COLOR_LIST(colour):
    simplify = colour.lower()
    colours =["red", "blue", "green", "yellow", "orange", "purple", "pink", "brown",
            "gray", "white", "black", "turquoise", "lavender", "magenta", "cyan", "indigo",
            "maroon", "gold", "silver", "olive", "teal", "peach", "coral", "violet",
            "charcoal", "beige", "mint", "ruby", "slate", "salmon", "aqua", "tan",
            "navy", "khaki", "crimson", "lime", "rose", "brick", "amber", "mustard",
            "periwinkle", "sapphire", "sienna", "plum", "aquamarine", "apricot", "chartreuse", "cerulean",
            "tangerine", "rust", "mulberry", "ivory", "emerald", "steel", "burgundy", "forest green",
            "cornflower blue", "sky blue", "melon", "pumpkin", "ochre", "denim", "cobalt", "mauve",
            "moccasin", "papaya whip", "wheat", "slate gray", "turmeric", "honeydew", "orchid", "electric blue",
            "fuchsia", "lemon", "misty rose", "salmon pink", "thistle", "powder blue", "hot pink", "midnight blue",
            "chocolate", "olive drab", "pine green", "tomato", "firebrick", "dodger blue", "linen", "navajo white",
            "alice blue", "azure", "bisque", "blanched almond", "burlywood", "cadet blue", "chocolate", "cornsilk",
            "dark goldenrod", "dark khaki", "dark olive green", "dark orange", "dark orchid", "dark salmon", "dark sea green", "dark slate blue",
            "dark slate gray", "dark turquoise", "deep pink", "deep sky blue", "dim gray", "dodger blue", "firebrick", "floral white", "forest green",
            "gainsboro", "ghost white", "gold", "goldenrod", "green yellow", "honeydew", "hot pink", "indian red", "ivory", "khaki", "lavender blush",
            "lemon chiffon", "light blue", "light coral", "light cyan", "light goldenrod", "light goldenrod yellow", "light gray", "light green",
            "light pink", "light salmon", "light sea green", "light sky blue", "light slate gray", "light steel blue", "light yellow", "linen", "magenta",
            "maroon", "medium aquamarine", "medium blue", "medium orchid", "medium purple", "medium sea green", "medium slate blue", "medium spring green",
            "medium turquoise", "medium violet red", "midnight blue", "mint cream", "misty rose", "moccasin", "navajo white", "navy", "old lace", "olive",
            "olive drab", "orange", "orange red", "orchid", "pale goldenrod", "pale green", "pale turquoise", "pale violet red", "papaya whip", "peach puff",
            "peru", "pink", "plum", "powder blue", "purple", "red", "rosy brown", "royal blue", "saddle brown", "salmon", "sandy brown", "sea green", "seashell",
            "sienna", "silver", "sky blue", "slate blue", "slate gray", "snow", "spring green", "steel blue", "tan", "teal", "thistle", "tomato", "turquoise", "violet",
            "wheat", "white", "white smoke", "yellow", "yellow green"]
    if simplify in colours:
        pass
    
def NATIONALITY_LIST():
    nationalies = ["Afghanistan", "Albania", "Algeria", "Andorra", "Angola", "Antigua and Barbuda", "Argentina", "Armenia", "Australia",
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
            "Uzbekistan", "Vanuatu", "Vatican City", "Venezuela", "Vietnam", "Yemen", "Zambia", "Zimbabwe"]
    return nationalies

def YEAR(year):
    simplify = int(year)
    years =[1888, 1889, 1890, 1891, 1892, 1893, 1894, 1895, 1896, 1897,
            1898, 1899, 1900, 1901, 1902, 1903, 1904, 1905, 1906, 1907,
            1908, 1909, 1910, 1911, 1912, 1913, 1914, 1915, 1916, 1917,
            1918, 1919, 1920, 1921, 1922, 1923, 1924, 1925, 1926, 1927,
            1928, 1929, 1930, 1931, 1932, 1933, 1934, 1935, 1936, 1937,
            1938, 1939, 1940, 1941, 1942, 1943, 1944, 1945, 1946, 1947,
            1948, 1949, 1950, 1951, 1952, 1953, 1954, 1955, 1956, 1957,
            1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966, 1967,
            1968, 1969, 1970, 1971, 1972, 1973, 1974, 1975, 1976, 1977,
            1978, 1979, 1980, 1981, 1982, 1983, 1984, 1985, 1986, 1987,
            1988, 1989, 1990, 1991, 1992, 1993, 1994, 1995, 1996, 1997,
            1998, 1999, 2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007,
            2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017,
            2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025, 2026, 2027]
    if simplify in years:
        pass

def DATE_VALIDATION_TEAM(date):
    # date_obj  = datetime.strptime(date, '%d/%m/%Y').date()
    startDate = datetime.strptime(1888, 1, 1, 00, 00, 00).date()
    endDate   = datetime.strptime(2026, 1, 1, 00, 00, 00).date()
    # check if dateObj is between startDate and endDate
    if startDate <= date <= endDate:
        pass