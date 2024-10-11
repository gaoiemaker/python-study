# 获取当前时间和日期

from datetime import datetime,timedelta,timezone

now = datetime.now()
# print(now.strftime('%a,%b,%Y-%m-%d %H:%M:%S'))


t = 1429417200.0


# str转换为datetime
st = '2024-10-20 12:00:00'

cday = datetime.strptime(st,'%Y-%m-%d %H:%M:%S')

# print(cday)

# datetime加减 需要导入timedelta


culc = now + timedelta(hours=10)

# 本地时间转换为UTC时间

tz_utc_8 = timezone(timedelta(hours=8))

dt = now.replace(tzinfo=tz_utc_8)

# 时区转换
# 时间戳
timestamp = datetime.now().timestamp()
print(timestamp)
# utc_time = datetime.fromtimestamp(timestamp, tz=timezone.utc)
utc_now = now.astimezone(timezone.utc)

china_now = utc_now.astimezone(timezone(timedelta(hours=8)))


print(china_now)






