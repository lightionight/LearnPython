# Regex expression is usding for deal with string the most data type we always need.
# \d is match digital "\d" match any digital "0"
# \w is match digital or character "\w" match "A" or "0"
# . is match any character

# for pattern change length
# *      for any number character
# +      at least have one
# ?      Node or have one
# {n}    have n element
# {m, n} have n or m element
# \      translate character

# []     is range pattern
# [0-9]  express match a digital that in range 0-9
# |      is OR  A|a  A and a all matched
# ^      is start from line  ^A is match Apple apple
# $      is end from line   $S is match startS not start
# python using regex expression by re
import re
'''
由于Python的字符串本身也用\转义，所以要特别注意
'''
if re.match(r"[0-9]{0,5}\-[0-9]{5,9}", "010-5948293"):
    print("Ok")

## regex expression can spit string group from string using ()
test = re.match(r"(\d{0,5})\-(\d{5,9})$", "010-5948293")
if test:
    print(test.group(1) + test.group(2))
    print(test.group(0))  # group(0) is origin string 

# for effection considering  we always precomplier regex pattern
re_telephone  = re.compile(r"(\d{3})\-(\d{11})$")
match1 = re_telephone.match("086-15926463626")
if match1:
    print(match1.group(1))
    print(match1.group(2))
