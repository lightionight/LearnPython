# _*_ coding: utf-8 _*_
# hashlib provide a series alogrithom about HASH
# normally like MD5, SHA1
# HASH Algorithm is a function can translate any length data for an constant length string
# AND keep string is unique.
# usually if file's HASH string is equal, we can say they are the same thing

import hashlib

md = hashlib.md5()

md.update("Hello World!".encode("utf-8"))

print(md.hexdigest())
# MD5 is fast and result is 128 bit, normally expression an 32 HEX string

# basely if you know the string you can calculate the string MD5
# and password is not safe
# but we can add some string before string going MD5 calculate
def calcPw_md5(password):
    return get_md5(password + "Salt")
# The string "Salt" is add for encription
# only when we know the Salt we could calculate the password