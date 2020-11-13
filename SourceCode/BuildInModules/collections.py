# _*_ coding: utf-8 _*_

# collection is python build-in models prvide so much powerful tools
'''
namedtuple
'''
# define a tuple type name 
# very simialy like C / C++ enum style
from collections import namedtuple

# define a Point tuple type and set how many element Point tuple should hold on
# below is the case , show Point tuple type carray three element X, Y, and Z;
Point = namedtuple("Point", ["X", "Y", "Z"]) 

p = Point(78, 21, 12)
for i in p:
    print(i)

# Or Define a Shape tuple type
Circle = namedtuple("Circle", ["X", "Y", "R"]) # x y is origin R is 

'''
deque
'''
# list store data and order seaching is fast 
# but insert and delete is slowly 
# list is linear data store when data is huge , productivity is low 
# when in this case we should using deque
# deque is build for efficiency insert and delete operator
from collections import deque

de = deque(["A", "B", "C"])
de.append("X")
deque.appendleft("Y")

'''
defaultdict
Ordereddict
'''
from collections import defaultdict, OrderedDict

'''
chainmap
'''
'''
count
'''
