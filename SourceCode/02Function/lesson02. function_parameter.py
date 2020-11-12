# define function Parameter
def func1(name, phoneN, age, city = "Wuhan"):
    print("Name:", name);
    print("Phone number:", phoneN);
    print("Age:", age);
    print("City:", city);

#func1("fenglei", "15926463626", 27);
#func1("fenglei", "15926463626", 27, "beijing");

# define auto size Parameter;
# implement by transform a tuple as parameter;
# use * prefix the parameter.
def func2(*number):
    sum = 0;
    for num in number:
        sum = sum + num;
    print(sum);
func2(1, 2, 3, 4, 5, 6, 7, 8);

#关键字参数
# 将参数自动组装为dict
#using ** prefix
def person(name, age, **kw):
    
