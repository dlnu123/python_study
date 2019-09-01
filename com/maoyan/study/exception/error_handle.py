# 错误处理
# 1、try...except...finally
# 2、stack
# 3、logging
# 4、raise


import logging
from functools import reduce


# 1、try...except...finally
def try_func(a, b):
    try:
        print("try...")
        result = int(a) / int(b)
        print("try...result: %d" % result)
    except ValueError as e:
        print("except ValueError:", e)
    except ZeroDivisionError as e:
        print("except ZeroDivisionError:", e)
    # 此处的 else 部分，只有在不发生异常的时候才会执行，如果发生异常，则会进入 except 代码块，不会进入 else 代码块
    else:
        print("else")
    finally:
        print("finally")
    print("END")


try_func(10, 2)
try_func(10, 0)
try_func(10, 'a')
print("----------------------------------------- 完美的分割线 -----------------------------------------")


# 2、stack
def foo(s):
    return 10 / int(s)


def bar(s):
    return foo(s) * 2


def main():
    print(bar(2))
    # 下面两行代码可以查看错误信息的调用栈
    # print(bar(0))
    # print(bar('a'))


main()
print("----------------------------------------- 完美的分割线 -----------------------------------------")


# 3、logging
def try_func2(a, b):
    try:
        print("try...")
        result = int(a) / int(b)
        print("try...result: %d" % result)
    except ValueError as e:
        logging.exception("except ValueError:", e)
    except ZeroDivisionError as e:
        logging.exception("except ZeroDivisionError:", e)
    # 此处的 else 部分，只有在不发生异常的时候才会执行，如果发生异常，则会进入 except 代码块，不会进入 else 代码块
    else:
        print("else")
    finally:
        print("finally")
    print("END")


try_func2(10, 2)
# try_func2(10, 0)
# try_func2(10, 'a')
print("----------------------------------------- 完美的分割线 -----------------------------------------")


# 4、raise
# 课后练习
def str2num(s):
    try:
        return int(s)
    except ValueError as e:
        try:
            return float(s)
        except ValueError as e:
            raise


def calc(exp):
    ss = exp.split('+')
    ns = map(str2num, ss)
    return reduce(lambda acc, x: acc + x, ns)


def main():
    r = calc('100 + 200 + 345')
    print('100 + 200 + 345 =', r)
    r = calc('99 + 88 + 7.6')
    print('99 + 88 + 7.6 =', r)


main()

