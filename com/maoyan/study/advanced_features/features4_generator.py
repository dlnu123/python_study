# 列表生成器

g = (x * x for x in [1, 2, 3, 4, 5, 6, 7])
print(g)
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))


# 基本不会使用next方法获取列表生成器的值
# 使用迭代获取
for x in g:
    print(x, 'for')


# 如何将一个函数编程列表生成器
# 斐波那契数列实现
# 1
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        print(b)
        a, b = b, a + b
        n += 1
    print("DONE")


fib(5)


# 如何将上面的函数编程列表生成器
# yield关键字
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n += 1
    # return 为什么不输出，print 就输出呢？
    return "DONE"


print(fib(5))
for x in fib(5):
    print(x)
