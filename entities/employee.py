from abc import ABC, abstractmethod

class Employee(ABC):
    def __init__(self,id,name,age,nationality,born,salary):
        self._id=id
        self._name=name
        self._age=age
        self._nationality=nationality
        self._born=born
        self._salary=salary
    employee_list=[]
    
    @property
    def id(self):
        return self._id
    @property
    def name(self):
        return self._name
    @property
    def age(self):
        return self._age
    @property
    def nationality(self):
        return self._nationality
    @property
    def born(self):
        return self._born
    @property
    def salary(self):
        return self._salary
    @classmethod
    def employee_add(cls, other):
        Employee.employee_list.append(other)
    
    @abstractmethod
    def isemployee(self):
        pass
    
    def employee_lista(cls):
        ids = []
        for id in Employee.employee_list:
            x = id
            ids.append(x)
        return ids