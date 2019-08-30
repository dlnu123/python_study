# 元类测试

# type()
# metaclass


# type()
def fn(self):
    print("Hello World!")


Hello = type("Hello", (object,), dict(hello=fn))
h = Hello()
h.hello()
