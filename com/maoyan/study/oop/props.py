# 实例属性和类属性


class Student(object):
    name = "wl"


s = Student()
print(s.name)
print(Student.name)
s.name = 'yingying'
print(s.name)
print(Student.name)
del s.name
print(s.name)
