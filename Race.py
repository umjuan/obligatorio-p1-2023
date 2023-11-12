from entities.team import Team
from entities.racing_team import Racing_Team
from entities.car import Car

class Race(object):

    def __init__(self):
        self._racers = []
        self._teams = []
        self._results = []

    def regist_unexpected(self):
        self.param = list(input('Insert comma separated racers number which left the race. '))
        self.param2 = list(input('Insert racer numbers who reported errors in pits. '))
        self.param3 = list(input('Insert racer numbers being penalized for breaking racing rules. '))

    @property
    def get_param(self):
        return self.param
    
    @property
    def get_param2(self):
        return self.param2
    
    @property
    def get_param3(self):
        return self.param3
    
    def get_left_race(self):
        return self.get_param
    
    def get_pits_error(self):
        return self.get_param2
    
    def get_penalties(self):
        return self.get_param3
    
    @property
    def get_racers(self):
        return self._racers
    
    @property
    def get_teams(self):
        return self._teams

    @property
    def get_results(self):
        return self._results
    
    def simulate_race(self):
        for number in self.param:        
            if number not in self.param and not None:

#       query_mechanic_teams()
#       query_cars_score()
#       score_final = suma_score_mecanicos + score_auto + score_piloto –
#                        5*cantidad_errores_en_pits - 8*cantidad_penalidad_infringir_norma 
                pass
            else:
                self._results.append(0)

    def query_top10_chmp(self):
        #Perform query
        pass

    def query_top5_salary(self):
        #Query
        pass        

    def query_top3_racers(self):
        #Query
        pass

    def query_team_director(self):
        #Query
        pass

    def query_team_chmp_results(self):
        #Query
        pass

# R = Race()
# A = R.regist_unexpected()
# z = R.get_param

# print(z)
# print(R.__init__)