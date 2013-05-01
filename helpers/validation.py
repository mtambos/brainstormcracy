'''
Created on Aug 17, 2011

@author: Mario Tambos
'''
from google.appengine.ext import db

def PositiveIntegerValidator(value):
    if value < 0:
        raise db.ValidationError()