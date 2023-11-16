from employee import Employee

class Team_leader(Employee):
    def __init__(self,id,name,age,nationality,born,salary):
        Employee.__init__(self,id,name,age,nationality,born,salary)
        self.type='team_leader'
    


