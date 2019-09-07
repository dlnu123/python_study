# 集合模块
# 1、namedtuple
# 2、deque
# 3、defaultdict
# 4、OrderedDict（Key会按照插入的顺序排列，不是Key本身排序）（FIFO）
# 5、ChainMap（指定优先级）
# 6、Counter


from collections import namedtuple
from collections import deque
from collections import defaultdict
from collections import OrderedDict
from collections import ChainMap
from collections import Counter
import os
import argparse


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


# OrderedDict -> FIFO
class LastUpdatedOrderedDict(OrderedDict):
    def __init__(self, capacity):
        super(LastUpdatedOrderedDict, self).__init__()
        self._capacity = capacity

    def __setitem__(self, key, value):
        if key in self:
            del self[key]
            print("Delete key", key)
        else:
            if len(self) + 1 > self._capacity:
                first = self.popitem(last=False)
                print("Remove First", first)
        OrderedDict.__setitem__(self, key, value)


# FIFO测试
last = LastUpdatedOrderedDict(3)
last.__setitem__("1", "1")
print(last)
last.__setitem__("2", "2")
print(last)
last.__setitem__("1", "1")
print(last)
last.__setitem__("3", "3")
print(last)
last.__setitem__("4", "4")
print(last)


# ChainMap -> 优先级之类
# 构造缺省参数:
defaults = {"color": "red", "user": "guest"}

# 构造命令行参数:
parser = argparse.ArgumentParser()
parser.add_argument("-u", "--user")
parser.add_argument("-c", "--color")
namespace = parser.parse_args()
command_line_args = {k: v for k, v in vars(namespace).items() if v}

# 组合成ChainMap:
combined = ChainMap(command_line_args, os.environ, defaults)

# 打印参数:
print("---------------------------------")
print('color=%s' % combined['color'])
print('user=%s' % combined['user'])
print("---------------------------------")


# Counter -> 计数器
counter = Counter()
for c in "programming":
    counter[c] += 1
print(counter)
print(counter.get("r"))
print(counter.get("o"))

