'''
Python 内置 dict的支持，another computer language may call it map， use key-value store，
it's so fast to seaching
'''
name = ["Tom", "Jerry", "Rome"];
scores = [95, 80, 75];
# and Combine them, replace by single list
# dict using {}

students = {"Tom":95, "Jerry": 80, "Rome":75}
print(students["Tom"]);
# and dict can revalue element
students["Tom"] = 100;
print(students["Tom"]);
# if key not in dict ,it will be Key error;
#print(students["Jack"]);

# two way can handle this exception
# 1.using in jugement key is or not, if exist it will return True, otherwise return false;
print("Jack" in students);

# 2. using dict.function get() if not exist will return none, or you can choose return string ;
print(students.get("Jack"));
print(students.get("Jack","Not in dict"));

#if want delete element in dict can use pop(key) function.
students.pop("Tom");

# between dict and List
# relationship is trade-off
# time and space
# Reminder : dict key Can NOT change.
'''
set also is collection of key, but can't store value and can not repeat.
So there is no same key in set.
and set is not order
'''
# normally, set need list to init
s = set([1, 2, 3]);
# can add element by function add(key), repeat key will not effect.
s.add(5);
s.add(4);
# can remove element by function remove(key),
s.remove(1);
s.remove(2);
# usually it used as AND and OR operation.

# One tip, python variable more like a pointer
# can change particular string value
a = "abc";
a.replace("a", "A");
# it actully restore a new data "Abc" in a another place, a.replace() return a pointer point to new place,
# So you need an another variable to store this pointer;
b = a.replace("a", "A");
