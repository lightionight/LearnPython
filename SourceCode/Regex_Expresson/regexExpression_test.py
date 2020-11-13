# -*- coding: utf-8 -*-
# test email formal
import re

# define a function
def is_valid_email(addr):
    re_email = re.compile(r"([0-9A-Za-z]*)@([0-9A-Za-z]*).[com|cn|com.cn]")
    match = re_email.match(addr)
    if match:
        print("True: " + match.group(1) + " + " + match.group(2))
    else:
        print("False")

is_valid_email("hello@qq.com")
is_valid_email("hello#qq.com")
