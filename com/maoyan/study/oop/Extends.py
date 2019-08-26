# 鸭子类型


class Animal(object):
    def run(self):
        print("Animal is running")


class Dog(Animal):
    def run(self):
        print("Dog is running")


class Cat(Animal):
    def run(self):
        print("Cat is running")


animal = Animal()
dog = Dog()
cat = Cat()
animal.run()
dog.run()
cat.run()


print(isinstance(animal, Animal))
print(isinstance(dog, Animal))
print(isinstance(dog, Dog))
print(isinstance(cat, Animal))
print(isinstance(cat, Cat))
print(isinstance(animal, Dog))


def run(animal):
    animal.run()


run(Animal())
run(Dog())
run(Cat())
