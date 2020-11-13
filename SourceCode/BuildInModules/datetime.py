# datatime is python deal with time and date standard lib

# important datatime modules
# first datetime is modules name, second datetime is class name
from datetime import datetime 

# get current time from system
now = datetime.now()

print(now)

# using order time to create datetime object
dt = datetime(2020, 11, 13, 15, 31)
print(dt)
print(dt.timestamp())