print(list(range(1, 11)))


print([x * x for x in list(range(1, 11))])


print([x * x for x in list(range(2, 11)) if x % 2 == 0])


print([m + n for m in "XYZ" for n in "ABC"])


L1 = ['Hello', 'World', 18, 'Apple', None]
L2 = [s.lower() for s in L1 if isinstance(s, str)]
print(L2)


# 测试提交
