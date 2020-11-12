'''
列表生成表达式
List Creat by range expression
for example:
    [1, 2, 3, 4, 5, 6, 7, 8, 9] can simply using
    list(range(1, 10)) ----- range(min, max)  from min and low max;
'''
l = list(range(1, 10))
#for i in l:
    #print(i)

# for complict case
l1 = [x * x for x in range(1, 11)]
#for i in l1:
    #print(i)

# 甚至还可以对x 的取值进行判断
l2 = [y * y for y in range(1, 11) if y % 3 == 0]

#也可以定义多个变量, 同时赋予不同的取值范围进行变量的合并
l3 = [x + y for x in "ABCDEFG" for y in "HJKLMN"]
for i in l3:
    print(i)

# of course we can define three variables in list expression , but not normal

