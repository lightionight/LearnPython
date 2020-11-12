'''
面向过程的程序设计把计算机程序视为一系列的命令集合，
即一组函数的顺序执行。为了简化程序设计，面向过程把函
数继续切分为子函数，即把大块函数通过切割成小块函数来降低系统的复杂度。

而面向对象的程序设计把计算机程序视为一组对象的集合，
而每个对象都可以接收其他对象发过来的消息，并处理这些消
息，计算机程序的执行就是一系列消息在各个对象之间传递
'''

#define an class
class Student(object): #(Object) is inhert from object class
    def __init__(self,name, socre): # every class must define a fuction name  __init__ for instance
        self.name = name
        self.socre = socre
        self._grade = "None"
    #define some object operator function
    def print(self):
        print("%s : %s" %(self.name, self.socre))
    def grade(self):
        self._grade = "A"
        print(self._grade)
    def setname(self, name):
        self.name = name

#instance an class object
bob = Student("Tom", 78) 

# class equal than an class object template;
# using it to creat same object

