print("Hello World ! ");

#print a string
print("this is string!")

#查询字符编码位置
print(ord("中"));
ord("A")
ord("z")
print('\u4e2d\u6587');
x = b'ABCC';
print(x);
b'ABC'.decode('ascii');

#占位符号
print('%2d - %02d' %(3, 1.2));
#format()
print('hello, {0}, 成绩提高了 {1:.1f}%'.format('小明',17.125));

#f-string
r = 2.5;
s = 3.14 * r ** 2;
print(f"The area of circle with radius {r} is {s:.2f}");  
# {r} replace by r variable, {s:.2f} replace by s variable.

#Question
s1 = 72;
s2 = 85;
r = (s2 - s1) % s1;
print('%.1f'%(r));