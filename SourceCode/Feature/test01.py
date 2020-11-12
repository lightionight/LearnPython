'''
Ref: https://www.liaoxuefeng.com/wiki/1016959663602400/1017269965565856
Need Fix
'''
def trim(s):
    F = 0
    L = -1
    if s[F] != " " and s[L] != " ":
        return s[F:L]
    else:
        if s[F] == " ":
            F += 1
        if s[L] == " ":
            L += -1
        return trim(s[F:L])
print(trim("  Name      "))
    
    