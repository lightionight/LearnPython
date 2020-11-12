'''
Learn how to using function in python
function 的本质就是抽象
通过写出抽象的规律 然后代替重复的写法;
借助抽象,我们才不用关心底层的具体计算过程,而直接再更高的层次上思考问题.
'''
# base using function
abs(100);
abs(-20);
abs(-100);
#abs("hello"); Error can't pass in string
max();
max(1,2);
max(1, 2, 3, 4, 5);

# data type transform for:
int("123");
float("12.34");

# define custom function
def my_abs(x):
    if x >= 0:
        return x;
    else:
        return -x;
my_abs(-100);

# define null function 
def nop():
    pass;

# add function parameter check
def my_abs2(x):
    if not isinstance(x, (int, float)):
        raise TypeError("Bad Operand type")
    if x >= 0:
        return x
    else:
        return -x
# can return multi_value, but just not True, it just return a tuple, as a many element combine into a tuple.
# So basely function still return a single return value.
import math
def move(x, y, step, angle = 0):
    nx = x + step * math.cos(angle);
    ny = y - step * math.cos(angle);
    return nx, ny;
# 
