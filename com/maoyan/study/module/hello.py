# 模块学习


""" hello module study """

__author__ = 'wangliang'


import sys


def test():
    args = sys.argv
    if len(args) == 1:
        print("Hello World")
    elif len(args) == 2:
        print("Hello", args[1])
    else:
        print("Too many arguments!")


# if __name__ == '__main__':
#     test()

a = '111'
