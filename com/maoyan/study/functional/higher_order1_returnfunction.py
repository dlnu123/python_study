# 返回函数

# 实现一个可变参数的求和。


# 简单实现
def calc_sum(*args):
    result = 0
    for num in args:
        result += num
    return result


print(calc_sum(1, 3, 5, 7, 9))


# 返回函数实现
def lazy_sum(*args):
    def my_sum():
        result = 0
        for num in args:
            result += num
        return result
    return my_sum


f = lazy_sum(1, 3, 5, 7, 9)
print(f)
print(f())


# 闭包的陷阱
# 返回闭包时牢记一点：返回函数不要引用任何循环变量，或者后续会发生变化的变量。
def count():
    fs = []
    for i in range(1, 4):
        def xxx():
            return i * i
        fs.append(xxx)
    return fs


f1, f2, f3 = count()
print(f1())  # 9
print(f2())  # 9
print(f3())  # 9


# 使用循环变量
def count1():
    fs = []

    def sub(i):
        def g():
            return i * i
        return g

    for i in range(1, 4):
        fs.append(sub(i))

    return fs


f4, f5, f6 = count1()
print(f4())
print(f5())
print(f6())


# 课后习题
# 如果内层函数访问外层函数的变量需要加  nonlocal  才行，但是内层函数 却能直接访问集合
def createCounter():
    m = [0]

    def counter():
        m[0] += 1
        return m[0]

    return counter


# 测试:
counterA = createCounter()
print(counterA(), counterA(), counterA(), counterA(), counterA()) # 1 2 3 4 5
counterB = createCounter()
if [counterB(), counterB(), counterB(), counterB()] == [1, 2, 3, 4]:
    print('测试通过!')
else:
    print('测试失败!')
