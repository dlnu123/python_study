# filter高阶函数


# 只保留奇数
def is_odd(s):
    return s % 2 == 1


print(list(filter(is_odd, [1, 2, 4, 5, 6, 9, 10, 15])))


# 去除空字符串（？？？？？？？？）
def not_empty(s):
    return s and s.strip()


print(list(filter(not_empty, [' A ', '', 'B', None, 'C', '  '])))


# 求素数（？？？？？？？？？）
def odd_iter():
    n = 1
    while True:
        n += 2
        yield n


for x in odd_iter():
    if x < 100:
        print(x)


# 课后习题（？？？？？？）
