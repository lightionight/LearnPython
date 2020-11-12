# class Attribute access
# Instance Attribute Access
'''
class Student(object):
    count = 0
    statu = False
    def __init__(self, name):
        self.name = name
        Student.count += 1

#################################
A = Student("Tom")
print(Student.count)
B = Student("Jack")
print(Student.count) # Now is Access Class Attribute

## 限制Class Attribute Create
class Student(object):
    __slots__ = ("name", "Age")
# Not Effect for subClass
class Tom(Student):
    pass
'''
class Person(object):
    @property
    def birth(self):
        return self._birth
    
    @birth.setter
    def birth(self, value):
        self._birth = value
    
    @property
    def age(self):
        return 2015 - self._birth
    
A = Person()
A.birth = 1998
print(A.age)