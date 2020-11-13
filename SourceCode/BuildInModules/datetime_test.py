# _*_ coding: utf-8 _*_ 

import re

from datetime import datetime, timezone, timedelta

def to_timestamp(dt_str, tz_str):
    re_datetime = re.compile(r"(\d{4})-(\d+)-(\d+) (\d+):(\d+):(\d+)")
    re_timezone = re.compile(r"^\w{3}+(\d):*")
    M_datetime = re_datetime.match(dt_str)
    M_timezone = re_timezone.match(tz_str)
    if M_datetime and M_timezone:
        tz = timezone(timedelta(hours = M_timezone.group(1)))
        result = datetime(M_datetime.group(1), 
            M_datetime.group(2), 
            M_datetime.group(3), 
            M_datetime.group(4), 
            M_datetime.group(5), 
            M_datetime.group(6),
            tzinfo= tz)
        print(result.timestamp())

to_timestamp("2015-1-21 9:01:30", "UTC+5:00")

