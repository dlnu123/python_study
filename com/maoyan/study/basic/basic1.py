# print("123")
#
# print(100 + 200)
#
# name = input("input your name:")
# print(name)
#
# # print absolute value of an integer:
# a = -1100
# if a > 0:
#     print(a)
# else:
#     print(-a)

from functools import reduce

sp = "123.456".split('.')
print(reduce(lambda x, y: x * 10 + y, map(int, sp[0])))
print(reduce(lambda x, y: x * 10 + y, map(int, sp[1])) / 10**len(sp[1]))

s = ''
print(s and s.strip())
