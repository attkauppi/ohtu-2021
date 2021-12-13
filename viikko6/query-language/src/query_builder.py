from matchers import *

class QueryBuilder:
    def __init__(self):
        self.query_object = All()
    
    def build(self):
        return self.query_object
    
    def playsIn(self, team):
        return QueryBuilder(PlaysIn(team))