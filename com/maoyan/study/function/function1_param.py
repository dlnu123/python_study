# 函数的参数

# 参数顺序：位置参数-->默认参数-->可变参数-->命名关键字参数-->关键字参数

#   1、位置参数
#   2、默认参数
#       定义默认参数要牢记一点：默认参数必须指向不变对象！
#   3、可变参数
#   4、关键字参数
#   5、命名关键字参数


# 1、位置参数
# 计算一个数的n次方值
def power(x, n):
    return x**n


print(power(225, 2))


# 2、默认参数
# 计算一个数的n次方值(默认计算平方值)
def power(x, n=2):
    return x**n


print(power(225, 2))
print(power(225))


# 默认参数不为可变对象
def add_end(L=[]):
    L.append("END")
    return L


print(add_end())
print(add_end())
print(add_end())


def add_end(l=None):
    if l is None:
        l = []
    l.append("END")
    return l


print(add_end([1, 2, 3]))
print(add_end())
print(add_end())
print(add_end())


# 3、可变参数
def calc(numbers):
    sum = 0
    for n in numbers:
        sum += n**2
    print(sum)


calc([1, 2, 3])
calc((1, 3, 5, 7))


def calc2(*numbers):
    sum = 0
    for n in numbers:
        sum += n**2
    print(sum)
    if isinstance(numbers, list):
        numbers[0] = 10


calc2(1, 2, 3)
calc2(1, 3, 5, 7)
calc2()
num = [1, 2, 3]
num2 = (1, 3, 5, 7)
calc2(*num)
calc2(*num2)
print(num)


# 4、关键字参数


# 5、命名关键字参数
# 如果命名关键字参数没有默认值，必须传递
def person(name, age, *, city='xinji', job):
    print(name, age, city, job)


person('wangliang', 30, city='biejing', job='java')
person('wangliang', 30, job='java')


# 课后题目
def product(x, *y):
    if len(y) == 0:
        return x
    else:
        result = x
        for y1 in y:
            result *= y1
        return result
