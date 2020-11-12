# base class is root class, python all class's root class is object class.
# subclass is in inhert from base class and inhert all propertial and methon
class Animal(object):
    def run(self):
        print("Animal is running.")
    
class Cat(Animal):
    pass

class Dog(Animal):
    pass

dog = Dog()
cat = Cat()
dog.run()
cat.run()

'''
动态类型 OR 动态变量 类型语言
Python的“file-like object“就是一种鸭子类型。对真正的文件对象，
它有一个read()方法，返回其内容。但是，许多对象，只要有read()方法，
都被视为“file-like object“。许多函数接收的参数就是“file-like object“，
你不一定要传入真正的文件对象，完全可以传入任何实现了read()方法的对象。
'''