'''
AUTHOR: F3NG
DATE: 2020.11.06
'''
'''
Using python build-in List and tuple.
list is order collection, add and delete element at any time.
tuple is order collection but once init never can't change.
'''
# List
classmate = ['Michael', 'bob', 'tom'];
print(len(classmate));
# use subscript for get index element ,like C style.
classmate[1];
classmate[2];
print(classmate[1]);
# but when it out of range, it will get error.
# And use -1 to simply get the list last element,Just like this
print(classmate[-1]);
# and accroding this ,we can use this feature ,get last second element, last third element;
print(classmate[-2]);
print(classmate[-3]);
# because list can add element any time ,so you can do this.
classmate.append('adam');
classmate.append("Jack");
# Or insert element to particular index
classmate.insert(3, "Trump");
# Or delete element in particular inde;
classmate.pop(1);
# Or replace element by another element;
classmate[1] = "fenglei";

#And In List every element data type can be difference, not like C or C++ array or vector
classteda = ['HAHA', 1.23, True];
# At Last List can as be an element for another List, for example:
s = ["python", "java", classteda, "C++"];
#if you want to get first element in classteda at List s on third element , you can think it as 
# 2D array write as s[3][1], it simialy like C style 2D array;
s[3][1];
# if have no any element in List ,The len() function will get return 0;
a = [];
len(a); #will return 0;

# Tuple
# Tuple is more like C/C++ Const Array, once init and can't change value
T1 = ("Bob","Tom","Jerry");
# when decaler a tuple 
T2 = (1, 2);
#empty tuple
T3 = ();
# define contain one element tuple;
T4 = (1); # THIS is NOT RIGHT WAY, it mean varable T4 = 1; not tuple T4 contain one element;
T5 = (1,) # THIS IS RIGHT WAY, You must add ',' at last;

# Intro spec case ,when tuple contain an element is List, List element and List length can change 
# you can simily understand it as C pointer that  is an const Pointer.
# it can't change the pointer ,but can change the pointer pointing element type and size.
T6 = ("a", "b", ["A","B"]);
T6[3][1] = "X";
T6[3][2] = "Y";

# Tuple can't change is mean it's element pointer element can not change.


# List and Tuple is build-in Array type, one is flexiby, another is const.






