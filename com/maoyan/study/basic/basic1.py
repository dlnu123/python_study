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

# from functools import reduce
#
# sp = "123.456".split('.')
# print(reduce(lambda x, y: x * 10 + y, map(int, sp[0])))
# print(reduce(lambda x, y: x * 10 + y, map(int, sp[1])) / 10**len(sp[1]))
#
# s = ''
# print(s and s.strip())


# 函数的默认参数，在使用的时候，可以不考虑顺序问题
def test(a, b=1, c=2):
    print(a, b, c)


test(1)
test(1, c=100)
test(1, b=200, c=100)
test(12, c=34, b=56)


containsKey = 1 if 1 > 1 else 0
print(containsKey)
