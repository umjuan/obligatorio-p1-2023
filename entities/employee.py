from abc import ABC

class Employee(ABC):
    def __init__(self,id,name,age,nationality,born,salary):
        self.__id=id
        self.__name=name
        self.__age=age
        self.__nationality=nationality
        self.__born=born
        self.__salary=salary
    employee_list=[]
    @property
    def id(self):
        return self.__id
    @property
    def name(self):
        return self.__name
    @property
    def age(self):
        return self.__age
    @property
    def nationality(self):
        return self.__nationality
    @property
    def born(self):
        return self.__born
    @property
    def salary(self):
        return self.__salary
    @classmethod
    def id_list(other):
        Employee.append(other.id)

    