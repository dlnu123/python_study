# itertools
# 1、count()
# 2、cycle()
# 3、repeat()
# 4、takewhile()
# 5、chain()
# 6、groupby()


import itertools
import time


# start  step
i1 = itertools.count(2, 2)
for n in i1:
    time.sleep(1)
    print(n)
    if n > 5:
        break


i2 = itertools.cycle("ABC")
i = 0
for n in i2:
    time.sleep(1)
    print(n)
    i += 1
    if i % 3 == 0:
        break


# 不传第二个值，则会无限循环下去
i3 = itertools.repeat(12, 4)
for n in i3:
    time.sleep(1)
    print(n)


i4 = itertools.count(2, 1)
i41 = itertools.takewhile(lambda x: x < 10, i4)
print(list(i41))


for n in itertools.chain("abc", "ABC", "zzz"):
    print(n)


for key, group in itertools.groupby("AAABBBCCAAA"):
    print(key, list(group))
print("-------------------------------------------")
for key, group in itertools.groupby("AAABBBCCAaa"):
    print(key, list(group))
print("-------------------------------------------")
for key, group in itertools.groupby("AAABBBCCAaa", key=lambda x: x.upper()):
    print(key, list(group))
print("-------------------------------------------")


# 课后习题
def pi(N):
    """ 计算pi的值 """
    # step 1: 创建一个奇数序列: 1, 3, 5, 7, 9, ...
    odd = itertools.count(1, 2)
    # step 2: 取该序列的前N项: 1, 3, 5, 7, 9, ..., 2*N-1.
    odd_n = itertools.takewhile(lambda x: x <= 2 * N - 1, odd)
    # step 3: 添加正负符号并用4除: 4/1, -4/3, 4/5, -4/7, 4/9, ...
    total = 0
    n = 0
    for x in odd_n:
        if n % 2 == 0:
            total += 4 / x
        else:
            total += -4 / x
        n += 1
    # step 4: 求和:
    return total


# 测试:
print(pi(10))
print(pi(100))
print(pi(1000))
print(pi(10000))
assert 3.04 < pi(10) < 3.05
assert 3.13 < pi(100) < 3.14
assert 3.140 < pi(1000) < 3.141
assert 3.1414 < pi(10000) < 3.1415
print('ok')
