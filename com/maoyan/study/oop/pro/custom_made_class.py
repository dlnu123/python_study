# __slots__
# __len__()
# __str__()、__repr__()
# __iter__()、__next__()
# __getitem__()、__setitem__()、__delitem__()
# __getattr__()
# __call__()


# 1、__str__()、__repr__()-------打印对象内容
class Student1(object):
    def __init__(self, name):
        self.__name = name

    def __str__(self):
        return "Student name = %s" % self.__name
        # print("Student name = " + self.__name)

    __repr__ = __str__


s1 = Student1("wangliang")
print(s1)
s1.__str__()


# 2、__iter__()、__next__()------斐波那契数列打印
class Fib(object):

    def __init__(self) -> None:
        self.a, self.b = 0, 1

    def __iter__(self):
        return self

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        if self.a > 1000:
            raise StopIteration()
        return self.a


for f in Fib():
    print(f)
# print(Fib()[0])


# 3、__getitem__()、__setitem__()、__delitem__()-------斐波那契数列下标、切片（正负数、步长）实现
class Fib2(object):
    def __getitem__(self, item):
        if isinstance(item, int):
            a, b = 1, 1
            n = 0
            while n < item:
                a, b = b, a + b
                n += 1
            return a
        elif isinstance(item, slice):
            start = item.start
            stop = item.stop
            a, b = 0, 1
            result = []
            if start is None:
                start = 0
            n = 0
            while n < stop:
                a, b = b, a + b
                if n >= start:
                    result.append(a)
                n += 1
            return result


print(Fib2()[100])
print(Fib2()[0:5])
print(Fib2()[:10])


# 4、__getattr__()
class Student2(object):

    def __init__(self, name) -> None:
        self.name = name

    def __getattr__(self, item):
        if item == 'score':
            return 999


s2 = Student2("test")
print(s2.name)
print(s2.score)


# 5、__call__()、callable()-----使对象可以被调用
class Student3(object):

    def __init__(self, name) -> None:
        self.name = name

    def __call__(self, *args, **kwargs):
        print("Student3 name is %s" % self.name)


s3 = Student3("eee")
s3()
