class Student(object):

    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def print_score(self):
        print("%s ： %s" % (self.__name, self.__score))


bart = Student('Bart Simpson', 59)
lisa = Student('Lisa Simpson', 87)
bart.print_score()
lisa.print_score()

# print(bart.__name)
print(bart._Student__name)  # 可以获取，但是强烈不建议这样做，因为不同版本的Python解释器可能会把__name改成不同的变量名。


# 课后习题
class Student(object):
    def __init__(self, name, gender):
        self.__name = name
        self.__gender = gender

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_gender(self):
        return self.__gender

    def set_gender(self, gender):
        self.__gender = gender


# 测试:
bart = Student('Bart', 'male')
if bart.get_gender() != 'male':
    print('测试失败!')
else:
    bart.set_gender('female')
    if bart.get_gender() != 'female':
        print('测试失败!')
    else:
        print('测试成功!')
