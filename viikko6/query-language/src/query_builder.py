from matchers import *

class QueryBuilder:
    def __init__(self, query=And()):
        self.query_object = query
    
    def build(self):
        return self.query_object
    
    def hasAtLeast(self, value, attr):
        return QueryBuilder(And(HasAtLeast(value, attr), self.query_object))
    
    def hasFewerThan(self, value, attr):
        return QueryBuilder(And(HasFewerThan(value, attr), self.query_object))
    
    def playsIn(self, team):
        return QueryBuilder(And(PlaysIn(team), self.query_object))
    
    def oneOf(self, m1, m2):
        return QueryBuilder(Or(m1, m2))
    
    
