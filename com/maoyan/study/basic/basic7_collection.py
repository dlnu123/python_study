d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
print(d["Michael"])
# print(d["111"]) 不存在会抛异常
print(d.get('111', '不存在'))

print(d.pop('111', '不存在'))
