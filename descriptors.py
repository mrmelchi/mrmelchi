# descriptors.py
class Verbose_attribute():
    def __get__(self, obj, type=None) -> object:
        print("accessing the attribute to get the value")
        return 42

    def __set__(self, obj, value) -> None:
        print("accessing the attribute to set the value")
        raise AttributeError("Cannot change the value")

class Foo():
    attribute1 = Verbose_attribute()

my_foo_object = Foo()
x = my_foo_object.attribute1
print(x)
print('-' * 20)
class Foo():
    @property
    def attribute1(self) -> object:
        print("accessing the attribute to get the value")
        return 42

    @attribute1.setter
    def attribute1(self, value) -> None:
        print("accessing the attribute to set the value")
        raise AttributeError("Cannot change the value")

my_foo_object = Foo()
x = my_foo_object.attribute1
print(x)
print('-' * 20)
class Foo():
    def getter(self) -> object:
        print("accessing the attribute to get the value")
        return 42

    def setter(self, value) -> None:
        print("accessing the attribute to set the value")
        raise AttributeError("Cannot change the value")

    attribute1 = property(getter, setter)

my_foo_object = Foo()
x = my_foo_object.attribute1
print(x)
print('-' * 20)
class Vehicle():
    can_fly = False
    number_of_weels = 0

class Car(Vehicle):
    number_of_weels = 4

    def __init__(self, color):
        self.color = color

my_car = Car("red")
print(my_car.__dict__)
print(type(my_car).__dict__)
print(Car.__dict__)
print(type(my_car))
print('-' * 20)
# lookup.py
class Vehicle(object):
    can_fly = False
    number_of_weels = 0

class Car(Vehicle):
    number_of_weels = 4

    def __init__(self, color):
        self.color = color

my_car = Car("red")
print(my_car.color)
print(my_car.number_of_weels)
print(my_car.can_fly)
print(my_car.__dict__)
print(type(my_car).__dict__)
print(Vehicle.__dict__)
print('-' * 20)
# lookup2.py
class Vehicle():
    can_fly = False
    number_of_weels = 0

class Car(Vehicle):
    number_of_weels = 4

    def __init__(self, color):
        self.color = color

my_car = Car("red")

print(my_car.__dict__['color'])
print(type(my_car).__dict__['number_of_weels'])
print(type(my_car).__base__.__dict__['can_fly'])
print(type(my_car))
print(type(my_car).__base__)
print('-' * 20)
# descriptors2.py
class OneDigitNumericValue():
    def __init__(self):
        self.value = 0
    def __get__(self, obj, type=None) -> object:
        return self.value
    def __set__(self, obj, value) -> None:
        if value > 9 or value < 0 or int(value) != value:
            raise AttributeError("The value is invalid")
        self.value = value

class Foo():
    number = OneDigitNumericValue()

my_foo_object = Foo()
my_second_foo_object = Foo()
my_foo_object.__dict__.get('number')
Foo.__dict__['number'].__set__(my_foo_object , 9)
#my_foo_object.number = 5
my_foo_object.__dict__.get('number')
print(Foo.number)
print(my_foo_object.number)
print(my_second_foo_object.number)

my_third_foo_object = Foo()
print(my_third_foo_object.number)

print(Foo.__dict__['number'].value)
Foo.number = 1
print(type(Foo.number), '/////')
print(my_foo_object.__dict__)
# print(type(my_foo_object).__dict__['number'].__get__(my_foo_object, type(my_foo_object)), '-------')
print(type(my_foo_object).__dict__['number'].__get__(None, type(my_foo_object)), '-------')
print('-' * 20)
class OneDigitNumericValue():
    def __init__(self):
        self.value = {}

    def __get__(self, obj, type=None) -> object:
        try:
            return self.value[obj]
        except:
            return 0

    def __set__(self, obj, value) -> None:
        if value > 9 or value < 0 or int(value) != value:
            raise AttributeError("The value is invalid")
        self.value[obj] = value

class Foo():
    number = OneDigitNumericValue()

my_foo_object = Foo()
my_second_foo_object = Foo()

my_foo_object.number = 3
print(Foo.number)
print(my_foo_object.number)
print(Foo.number)
print(my_second_foo_object.number)

my_third_foo_object = Foo()
print(my_third_foo_object.number)

print(Foo.__dict__['number'])
print(my_foo_object.__dict__)
print('-' * 20)