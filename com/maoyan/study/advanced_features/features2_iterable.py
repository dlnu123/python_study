from collections.abc import Iterable


d = {'a': 1, 'b': 2, 'c': 3}

for key in d.keys():
    print(key)

for value in d.values():
    print(value)

for item in d.items():
    print(item)

for key, value in d.items():
    print(key, value)


print(isinstance('abc', Iterable))


# 课后习题
def findMinAndMax(L):
    if len(L) == 0:
        return (None, None)
    else:
        min = L[0]
        max = L[0]
        for x in L:
            if x < min:
                min = x
            if x > max:
                max = x
        return min, max


# 测试
if findMinAndMax([]) != (None, None):
    print('测试失败!1')
elif findMinAndMax([7]) != (7, 7):
    print('测试失败!2')
elif findMinAndMax([7, 1]) != (1, 7):
    print('测试失败!3')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败!4')
else:
    print('测试成功!')