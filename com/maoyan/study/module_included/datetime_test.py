# datetime是Python处理日期和时间的标准库。
# 1、获取【当前】日期和时间
# 2、获取【指定】日期和时间
# 3、datetime转换为timestamp
# 4、timestamp转换为datetime
# 5、str转换为datetime
# 6、datetime转换为str
# 7、datetime加减
# 8、本地时间转换为UTC时间
# 9、时区转换

import datetime


now = datetime.datetime.now()
print(now)
print(type(now))


print("---------------------------------------------------------------------------------------")
assign = datetime.datetime(2019, 9, 4, 16, 8)
print(assign)
print(type(assign))


print("---------------------------------------------------------------------------------------")
ts1 = now.timestamp()
ts2 = assign.timestamp()
print(ts1)
print(ts2)


print("---------------------------------------------------------------------------------------")
print(datetime.datetime.fromtimestamp(ts1))  # 本地时间
print(datetime.datetime.fromtimestamp(ts2))  # 本地时间
print(datetime.datetime.utcfromtimestamp(ts1))  # UTC时间


print("---------------------------------------------------------------------------------------")
print(datetime.datetime.strptime("2019-9-4 12:12:12", "%Y-%m-%d %H:%M:%S"))


print("---------------------------------------------------------------------------------------")
print(datetime.datetime.now().strftime("%A, %b %d %H:%M"))


print("---------------------------------------------------------------------------------------")
print(now + datetime.timedelta(days=1))
print(now + datetime.timedelta(hours=12))
print(now - datetime.timedelta(days=1, hours=2))


print("---------------------------------------------------------------------------------------")
tz_utc_8 = datetime.timezone(datetime.timedelta(hours=8))
zone = datetime.datetime(2019, 9, 4, 12, 12, 21, tzinfo=tz_utc_8)
print(zone)


# 课后习题
import re
from datetime import datetime, timezone, timedelta


def to_timestamp(dt_str, tz_str):
    pass


# 测试:
t1 = to_timestamp('2015-6-1 08:10:30', 'UTC+7:00')
assert t1 == 1433121030.0, t1

t2 = to_timestamp('2015-5-31 16:10:30', 'UTC-09:00')
assert t2 == 1433121030.0, t2

print('ok')

