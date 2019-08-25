# 偏函数
import functools


print(int('12345'))
print(int('12345', base=8))
# 5+32+192+1024+4096


int2 = functools.partial(int, base=2)
print(int2('1000000'))
print(int2('1010101'))
