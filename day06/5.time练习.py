# 时间练习

import re
from datetime import datetime, timezone, timedelta

a = dict([('name','noble'),('age',18)])


print(a['name'])
now = datetime.now()
# 时间 ==》 字符串
str = datetime.strftime(now, "%Y-%m-%d %H:%M:%S")

# 字符串 ==》 时间
time = datetime.strptime(str, "%Y-%m-%d %H:%M:%S")

# 获取utc时间
utc_time = now.astimezone(timezone.utc)

# 获取时区时间
bj_time = now.astimezone(timezone(timedelta(hours=8)))

# 时间 ==》 时间戳

timestrap = datetime.timestamp(bj_time)

# 时间戳 ==》 时间

timedate = datetime.fromtimestamp(timestrap, tz=timezone(timedelta(hours=0)))

# 本地时间转换为UTC时间 ==> 强制转换

timeqiang = now.replace(tzinfo=timezone(timedelta(hours=7)))
print(timeqiang)

def to_timestamp(dt_str, tz_str):
    ctime = datetime.strptime(dt_str, "%Y-%m-%d %H:%M:%S")
    mat_group = re.match(r"(UTC)([+-]\d{1,2}):([\d]{2})", tz_str)
    hours = mat_group.group(2)
    mins = mat_group.group(3)
    tz = timezone(timedelta(hours=int(hours), minutes=int(mins)))
    ctime = ctime.replace(tzinfo=tz)
    return ctime.timestamp()


# 测试:

t1 = to_timestamp("2015-6-1 08:10:30", "UTC+7:00")
assert t1 == 1433121030.0, t1

t2 = to_timestamp("2015-5-31 16:10:30", "UTC-09:00")

assert t2 == 1433121030.0, t2

print("ok")
