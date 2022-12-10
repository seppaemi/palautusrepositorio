from matchers import And
from matchers import  HasAtLeast
from matchers import  PlaysIn
from matchers import  Not
from matchers import  HasFewerThan
from matchers import  All
from matchers import  Or

class QueryBuilder:
    def __init__(self, query=All()):
        self._query = query
    
    def hasAtLeast(self, value, attr):
        return QueryBuilder(And(self._query, HasAtLeast(value, attr)))

    def playsIn(self, team):
        return QueryBuilder(And(self._query, PlaysIn(team)))

    def hasFewerThan(self, value, attr):
        return QueryBuilder(And(self._query, HasFewerThan(value, attr)))

    def Or(self, *queries):
        return QueryBuilder(Or(*queries))
    
    def build(self):
        return self._query
