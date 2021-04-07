from random import randint
class RandAttr:
    def __init__(self, n=10):
        self.n = n

    def __get__(self, inst, cls):
        print('Called __get__')
        return randint(0, self.n)

class RandAttrClass:
    rand_attr = RandAttr(20) # Descriptors are class attributes

inst = RandAttrClass() # Let's instantiate and access it
print(inst.rand_attr)
print(inst.rand_attr)

class VerboseGetDescriptor:
    def __get__(self, inst, cls):
        print('Called __get__ on', self.__class__)
        print('\tself:', self)
        print('\tinst:', inst)
        print('\tcls:', cls)

class VerboseGetClass:
    attr = VerboseGetDescriptor()

inst = VerboseGetClass()
inst.attr
VerboseGetClass.attr

class LazyAttr:
    def __init__(self, name, func):
        self.name = name
        self.func = func

    def __get__(self, inst, cls):
        print('Called __get__')
        # let's add the result to the INSTANCE
        inst.__dict__[self.name] = self.func(self)
        return inst.__dict__[self.name]

from time import sleep

class LazyAttrUser:
    def expensive_func(self):
        print('\tCalled expensive func')
        sleep(10)
        return 12345
    # We give the same name than descriptor
    attr = LazyAttr('attr', expensive_func)

# Let's instantiate the class
inst = LazyAttrUser()
print(inst.__dict__)
        # {}

# Let's retrive it
print(inst.attr)
        # Called __get__
        # 	Called expensive func
        # 12345

# Let's do it again
print(inst.attr)
    # 12345   --- with no sleep
print(inst.__dict__['attr'])
    # 12345

class VerboseSetDescriptor:
    def __set__(self, inst, val):
        print('Called __set__ on:', self.__class__)
        print('\tself:', self)
        print('\tinst:', inst)
        print('\tcls:', val) # New value instead of class

class VerboseSetClass:
    attr = VerboseSetDescriptor()

inst = VerboseSetClass()
print(inst.__dict__)
    # {}
inst.attr = 12345
    # Called __set__ on: <class '__main__.VerboseSetDescriptor'>
    # 	self: <__main__.VerboseSetDescriptor object at 0x016790E8>
    # 	inst: <__main__.VerboseSetClass object at 0x01679118>
    # 	cls: 12345
print(inst.__dict__) # NO modification done
    # {}
VerboseSetClass.attr = 12345
print(inst.__dict__) # NO modification done
    # {}
print(VerboseSetClass.__dict__['attr'])
    # 12345          #  We have "removed" (rebound to a new value) the descriptor!

# __set__ in the real world

class TypedAttrib:
    def __init__(self, name, typ):
        self.name = name
        self.typ = typ  # Avoid using 'type' as attribute name

    def __set__(self, inst, val):
        if isinstance(val, self.typ):
            inst.__dict__[self.name] = val
        else:
            raise TypeError("TypeError: Wrong data type '{0}'".format(val))


#===========================================================================
# Note that I wouldn't recommend this! Duck typing FTW!!
#===========================================================================


# Let's use it
class MyTypedClass(object):
    string = TypedAttrib('string', str)
    integer = TypedAttrib('integer', int)  # Despite using the same name the descriptor will ALWAYS intercept the call


inst = MyTypedClass()
inst.string = "123"
print(inst.__dict__)


# Let's make it fail
try:
    inst.string = 123
except TypeError as e:
    print(e)

print(inst.__dict__)  # Note that no modification has been done

MyTypedClass.string = "123"
print(type(MyTypedClass.__dict__['string']))


# Let's make it fail
try:
    MyTypedClass.string = 123
except TypeError as e:
    print(e)

print(type(MyTypedClass.__dict__['string']))  # # We have "removed" (rebound to a new value) the descriptor!
