# 元类测试

# type()
# metaclass


# type()
def fn(self):
    print("Hello World!")


# 此处的第二个参数，必须是一个tuple，不能是一个list，而且当tuple只有一个元素的时候，不要忘记后面的逗号。
# 1、第一个参数是class的名字（str类型）
# 2、第二个参数是从哪些类继承（tuple类型）
# 3、第三个参数是绑定class的方法（dict类型）
Hello = type("Hello", (object,), dict(hello=fn))
h = Hello()
h.hello()
