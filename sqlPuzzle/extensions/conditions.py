# -*- coding: utf-8 -*-
#
# SqlPuzzle
# Michal Horejsek <horejsekmichal@gmail.com>
# https://github.com/horejsek/sqlPuzzle
#

import sqlPuzzle.argsParser
import sqlPuzzle.sqlValue
import sqlPuzzle.relations


class Condition:
    def __init__(self):
        """
        Initialization of Condition.
        """
        self.__column = None
        self.__value = None
        self.__relation = None
    
    def __str__(self):
        """
        Print condition (part of WHERE).
        """
        return '`%s` %s %s' % (
            self.__column,
            sqlPuzzle.relations.RELATIONS[self.__relation],
            sqlPuzzle.sqlValue.SqlValue(self.__value),
        )
    
    def __eq__(self, other):
        return (
            self.getColumn() == other.getColumn() and
            self.getValue() == other.getValue() and
            self.getRelation() == other.getRelation()
        )
    
    def __ne__(self, other):
        return not self.__eq__(other)
    
    def set(self, column, value, relation=None):
        """
        Set column, value and relation.
        """
        self.setColumn(column)
        self.setValue(value)
        self.setRelation(relation or sqlPuzzle.relations.EQ)
    
    def setColumn(self, column):
        """
        Set column.
        """
        self.__column = column
    
    def setValue(self, value):
        """
        Set value.
        """
        self.__value = value
    
    def setRelation(self, relation):
        """
        Set relation.
        """
        self.__relation = relation
    
    def getColumn(self):
        """
        Get column.
        """
        return self.__column
    
    def getValue(self):
        """
        Get value.
        """
        return self.__value
    
    def getRelation(self):
        """
        Get relation.
        """
        return self.__relation


class Conditions:
    _conditionObject = Condition
    
    def __init__(self):
        """
        Initialization of Conditions.
        """
        self.__conditions = []
    
    def __str__(self):
        """
        Print limit (part of query).
        """
        if self.isSet():
            return "WHERE %s" % " AND ".join(str(condition) for condition in self.__conditions)
        return ""
    
    def _getConditions(self):
        return self.__conditions
    
    def isSet(self):
        """
        Is where set?
        """
        return self.__conditions != []
    
    def where(self, *args, **kwds):
        """
        Set condition(s).
        """
        for arg in sqlPuzzle.argsParser.parseArgsToListOfTuples(
            {'minItems': 2, 'maxItems': 3, 'allowDict': True, 'allowList': True},
            *args,
            **kwds
        ):
            condition = self._conditionObject()
            condition.set(*arg)
            self.__conditions.append(condition)
        
        return self
    
    def remove(self, *keys):
        """
        Remove condition(s).
        """
        if len(keys) == 0:
            self.__conditions = []
        
        if not isinstance(keys, (list, tuple)):
            keys = (keys,)
        
        conditions = []
        for condition in self.__conditions:
            if condition.getColumn() not in keys:
                conditions.append(condition)
        self.__conditions = conditions


