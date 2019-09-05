# 集合模块
# 1、namedtuple
# 2、deque
# 3、defaultdict
# 4、OrderedDict（Key会按照插入的顺序排列，不是Key本身排序）（FIFO）
# 5、ChainMap
# 6、Counter


from collections import namedtuple
from collections import deque
from collections import defaultdict
from collections import OrderedDict


Point = namedtuple("Point", ["x", "y"])
p = Point(1, 2)
print(p.x)
print(p.y)
# isinstance() arg 2 must be a type or tuple of types
# namedtuple是一个函数
# print(isinstance(p, namedtuple))
print(isinstance(p, Point))
print(isinstance(p, tuple))
# tuple不可以修改
# p.x = 1


q = deque(["a", "b", "c"])
q.append("x")
q.appendleft("y")
print(q)
print(q.count("a"))
q.extend(["o", "p", "q"])
print(q)
q.insert(0, "o")
print(q.count("o"))
print(q)
print(q.pop())
print(q)
print(q.popleft())
print(q)


d = dict({"1": "1-", "2": "2-"})
print(d.get("12"))

# 报异常
# dd = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
# print(dd['key2'])
default = defaultdict(lambda: "N/A")
default["key1"] = "key1"
print(default["key1"])
print(default["key2"])


d = dict([('a', 1), ('c1212', 2), ('b', 3)])
print(d)
od = OrderedDict([('a', 1), ('c', 2), ('b', 3)])
print(od)
