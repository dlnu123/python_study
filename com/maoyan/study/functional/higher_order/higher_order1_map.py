# map高阶函数学习
l = [1, 2, 3, 4, 5, 6, 7, 8, 9]
s = map(lambda x: x**2, l)

# map高阶函数生成的是【迭代器】
print(s)
print(list(s))


# 课后习题
def normalize(name):
    return name[0].upper() + name[1:len(name)].lower()


# 测试:
L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)
