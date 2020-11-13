# _*_ coding: utf-8 _*_
'''
itertools
'''
import itertools
# using fro iterator Operator
# count()
# cycle()
# repeat()
# chain() group iterator object to more bigger iterator object
for i in itertools.chain("ABC", "XYZ")

# groupby() 挑出迭代器中重复的元素并放到一起,作为一个list ,因此 迭代对象有多少个类型的元素就有多少个list
