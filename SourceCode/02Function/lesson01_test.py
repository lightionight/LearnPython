'''
计算quadratic（a, b, c), and return ax2 + bx + c = 0 result;
'''
import math

def quadratic(a, b, c):
    if (b ** 2) - 4 * (a * c) < 0:
        print("There is no answer.")
    else:
        x1 = -b + (math.sqrt((b ** 2)- 4 * (a * c)));
        x2 = -b - (math.sqrt((b ** 2)- 4 * (a * c)));
        return (x1 / (2 * a)), (x2 / (2 * a));
    
print(quadratic(2, 3, 5));
print(quadratic(2, 3, 1));