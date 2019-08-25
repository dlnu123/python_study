# reduce高阶函数

# 1、序列求和
from functools import reduce


def add(x, y):
    return x + y


l = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(reduce(add, l))


# 2、序列转数字
def fn(x, y):
    return x * 10 + y


print(reduce(fn, l))


# 课后习题
def prod(L):
    return reduce(lambda x, y: x * y, L)


print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
if prod([3, 5, 7, 9]) == 945:
    print('测试成功!')
else:
    print('测试失败!')


# 课后习题2
def str2float(s):
    sp = s.split('.')
    x1 = reduce(lambda x, y: x * 10 + y, map(int, sp[0]))
    x2 = reduce(lambda x, y: x * 10 + y, map(int, sp[1])) / 10**len(sp[1])
    return x1 + x2


print('str2float(\'123.456\') =', str2float('123.456'))
if abs(str2float('123.456') - 123.456) < 0.00001:
    print('测试成功!')
else:
    print('测试失败!')
