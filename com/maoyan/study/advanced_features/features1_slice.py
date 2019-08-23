# 切片

L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']

# 取前3个元素
# print(L[0:3])
# print(L[:3])
#
# # 从后面取元素
# print(L[-1:])
# print(L[-2:])
#
#
# L = list(range(100))
# print(L)
# # 前10个数：
# print(L[:10])
# # 后10个数：
# print(L[-10:])
# # 前11-20个数：
# print(L[10:20])
# # 前10个数，每两个取一个：
# print(L[:10:2])
# # 所有数，每5个取一个：
# print(L[::5])
#
#
# print((0, 1, 2, 3, 4, 5)[:3])


# 课后习题
def trim(s):
    start = 0
    end = len(s)
    if end == start:
        return ''
    else:
        while start < end and s[start] == ' ':
            start += 1
        end -= 1
        while end > 0 and s[end] == ' ':
            end -= 1
    return s[start:end + 1]


# 测试:
if trim('hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello') != 'hello':
    print('测试失败!')
elif trim('  hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello  world  ') != 'hello  world':
    print('测试失败!')
elif trim('') != '':
    print('测试失败!')
elif trim('    ') != '':
    print('测试失败!')
else:
    print('测试成功!')
