# 序列化
#   1、pickle
#   2、json
#   3、进阶的json
import pickle, json


d = dict(name='Bob', age=20, score=88)
print(pickle.dumps(d))
with open('/Users/wangliang/PycharmProjects/python_study/com/maoyan/study/io/serialize', 'wb') as f:
    pickle.dump(d, f)
with open('/Users/wangliang/PycharmProjects/python_study/com/maoyan/study/io/serialize', 'rb') as f:
    d = pickle.load(f)
    print(d)


print('------------------json------------------')
print(json.dumps(d))


class Student(object):
    # __slots__ = ('name', 'age', 'score')

    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score


s = Student('Bob', 20, 88)
# print(json.dumps(s))  # 报异常：Object of type Student is not JSON serializable


def student2dict(std):
    return {
        'name': std.name,
        'age': std.age,
        'score': std.score
    }


print('Student', json.dumps(s, default=student2dict))
# 通常class的实例都有一个__dict__属性，它就是一个dict，用来存储实例变量。
# 也有少数例外，比如定义了__slots__的class。
print('Student-dict', json.dumps(s, default=lambda obj: obj.__dict__))

