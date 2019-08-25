# 装饰器
import functools, time


# 一层装饰器
def log(func):
    def wrapper(*args, **kwargs):
        print("一层装饰器")
        return func(*args, **kwargs)
    return wrapper


def log2(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            print(text, "二层装饰器")
            return func(*args, **kwargs)
        return wrapper
    return decorator


@log2("1111")
def now():
    print("2019-08-25")


now()
print(now.__name__)


# 课后习题
def metric(func):
    def wrapper(*args, **kwargs):
        print('%s executed in %s ms' % (func.__name__, 10.24))
        return func(*args, **kwargs)
    return wrapper


# 测试
@metric
def fast(x, y):
    time.sleep(0.0012)
    return x + y


@metric
def slow(x, y, z):
    time.sleep(0.1234)
    return x * y * z


f = fast(11, 22)
s = slow(11, 22, 33)
if f != 33:
    print('测试失败!')
elif s != 7986:
    print('测试失败!')
