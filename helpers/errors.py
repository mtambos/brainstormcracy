'''
Created on Aug 17, 2011

@author: Mario Tambos
'''

class ArgumentError(Exception):
    '''
    Raised when there's an unexpected argument value
    '''
    Name = None
    Value = None
    
    def __init__(self, message, name, value):
        Name = name
        Value = value
        __str__ = message + ". Name: " + Name + ", Value: " + Value

class DataInconsistencyError(Exception):
    '''
    Raised when there's an unexpected argument value
    '''
    Name = None
    Value = None
    
    def __init__(self, message, name, value):
        Name = name
        Value = value
        __str__ = message + ". Name: " + Name + ", Value: " + Value
        