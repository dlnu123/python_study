# iterable（可迭代对象） 和 Iterator（迭代器） 的区别

# 可迭代对象和迭代器有一个很大的不同
#   list/truple/map/dict这些数据的大小是确定的
#   但是迭代器不是，迭代器不知道要执行多少次。每调用一次next()，就会往下走一步，是惰性的。

from collections.abc import Iterable
from collections.abc import Iterator

print(isinstance({}, Iterable))
print(isinstance((), Iterable))
print(isinstance('abc', Iterable))
print(isinstance((x for x in range(10)), Iterable))
print(isinstance(100, Iterable))


print(isinstance({}, Iterator))
print(isinstance((), Iterator))
print(isinstance('abc', Iterator))
print(isinstance((x for x in range(10)), Iterator))
print(isinstance(100, Iterator))
