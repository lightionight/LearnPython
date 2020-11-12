'''对List进行切片取值'''
L = ["Machael", "sarah", "tracy", "Tom", "Bob"]

r1 = []
n = 3
for i in range(n):
    r1.append(L[i])
    print(r1[i])

# python 提供非常方便的范围取值方法;
r2 = L[0:3]

# 也可以倒序取值
r3 = L[-1:-2]
