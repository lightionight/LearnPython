# Using Loop
# In python 
'''
In python Loop 第一种为for loop
    for item in container
        do something...
'''
s = ["Tom", "Jack", "Harry", "Rick", "Morty"];
for item in s:
    print(item);

'''
如果我们需要产生序列，可以用到range（）函数
list（range（5））
range(5) mean  start from 0 and smaller than 5;
'''
s2 = list(range(5));
for item in s2:
    print(item);
'''
第二种循环为 while loop
'''
x = 0;
y = 99;
while y > 0:
    x = x + y;
    y = y - 1;
print(x);

'''
if you want end loop, you can using break 
And continue can end loop not consider condition jugement;
'''
n = 1;
while n <= 100:
    if n > 11:
        break;
    print(n);
    n = n + 1;
print("END");