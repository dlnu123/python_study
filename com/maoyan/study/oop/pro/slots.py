from types import MethodType


class Student(object):
    pass


s1 = Student()
s1.name = 'wwww'
print(s1.name)


def set_age(self, age):
    self.age = age


s1.set_age = MethodType(set_age, s1)
s1.set_age(111)
print(s1.age)


class StudentSlots(object):
    __slots__ = ('name', 'age')


s2 = StudentSlots()
# s2.score = 90


class StudentSlotsE(StudentSlots):
    __slots__ = ()


s3 = StudentSlotsE()
# s3.score = 11
# print(s3.score)
s3.name = 'sdsds'
print(s3.name)
