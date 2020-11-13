# -*- coding: utf-8 -*-
from enum import Enum
class Gender(Enum):
    Male = 0
    Female = 1

class Student(object):
    def __init__(self, name, gender = Gender.Male):
        self.name = name
        self.gender = gender
    
tom = Student("TOM")
print(tom.gender)
