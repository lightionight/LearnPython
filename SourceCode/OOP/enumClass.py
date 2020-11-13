JAR = 1
FEB = 2
MAR = 3     # USE Captital for constant variable
# But JAR FEB MAR still can change it's data type
# python give us a Enum class for using constant
from enum import Enum

Month = Enum("Month", ("JAR", "FEB", "MAR", "APR", "MAY"))
# just like C And C++ enum element value start 1
# but you can creat subclass from Enum
class Day(Enum):
    Sun = 0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6
    # just like This special case for set Sun to 0

