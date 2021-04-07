class SlottedClass:
    __slots__ = ['attr_x', 'attr_y']  # These are slots
    def __init__(self, x, y):
        self.attr_x = x
        self.attr_y = y

    def sum_content(self):
        return self.attr_x + self.attr_y

inst = SlottedClass(12345, 67890)
print(inst.attr_x)
    # 12345
print(inst.attr_y)  # We can access its attributes
    # 67890
inst.attr_x = 54321  # We ca modify its attributes
    # 54321
print(inst.sum_content())  # We can call its methods
    # 122211
#inst.attr_xyz = 54321
    # Traceback (most recent call last):
    #   File "C:/Users/Mario/PycharmProjects/pythonProject/slots_property.py", line 19, in <module>
    #     inst.attr_xyz = 54321
    # AttributeError: 'SlottedClass' object has no attribute 'attr_xyz'

#print(inst.__dict__)
    # Traceback (most recent call last):
    #   File "C:/Users/Mario/PycharmProjects/pythonProject/slots_property.py", line 25, in <module>
    #     print(inst.__dict__)
    # AttributeError: 'SlottedClass' object has no attribute '__dict__'

print(SlottedClass.__dict__)

    # {'__module__': '__main__', '__slots__': ['attr_x', 'attr_y'], '__init__': <function SlottedClass.__init__ at 0x01066808>, 'sum_content': <function SlottedClass.sum_content at 0x010667C0>, 'attr_x': <member 'attr_x' of 'SlottedClass' objects>, 'attr_y': <member 'attr_y' of 'SlottedClass' objects>, '__doc__': None}
print(SlottedClass.__dict__['attr_x'].__get__(inst, SlottedClass))
    # 54321
# The slots are desriptors!
SlottedClass.__dict__['attr_x'].__set__(inst, 100001)
print(SlottedClass.__dict__['attr_x'].__get__(inst, SlottedClass))
    # 100001
print(inst.attr_x)
    # 100001

# Let me introduce the properties
# Let's define some temperature conversion methods (Celsius, Kelvin, Fahrenheit)
def f_to_c(f):
    return (f - 32.0) * 5.0 / 9.0


def c_to_f(c):
    return c * 9.0 / 5.0 + 32.0


def k_to_c(k):
    return k - 273.15


def c_to_k(c):
    return c + 273.15

class TempClass(object):
    def __init__(self, temp_celsius=None, temp_fahrenheit=None, temp_kelvin=None):
        if temp_celsius is not None:
            self._temp = temp_celsius
        elif temp_fahrenheit is not None:
            self._temp = f_to_c(temp_fahrenheit)
        elif temp_kelvin is not None:
            self._temp = k_to_c(temp_kelvin)
        else:
            self._temp = 0

    def get_temp_celsius(self):
        return self._temp

    def set_temp_celsius(self, val):
        self._temp = val

    # This is a property declaration
    temp_celsius = property(get_temp_celsius, set_temp_celsius)

    def get_temp_fahrenheit(self):
        return c_to_f(self._temp)

    def set_temp_fahrenheit(self, val):
        self._temp = f_to_c(val)

    # This is another property
    temp_fahrenheit = property(get_temp_fahrenheit, set_temp_fahrenheit)

    def get_temp_kelvin(self):
        return c_to_k(self._temp)

    # And another property, WITHOUT setter!
    temp_kelvin = property(get_temp_kelvin)


# Let's try it
inst = TempClass(20)
print(inst.temp_fahrenheit)
print(inst.temp_kelvin)

inst.temp_fahrenheit = 32
print(inst.temp_celsius)

# inst.temp_kelvin = 200  # There is no setter --> modification fails

# Let's see how it works
print(inst.__dict__)

print(TempClass.__dict__)

print(TempClass.__dict__['temp_fahrenheit'])
print(TempClass.__dict__['temp_fahrenheit'].__get__(inst, TempClass))

TempClass.__dict__['temp_celsius'].__set__(inst, 100)
print(inst.__dict__)


# There are property decorators


class TempClass(object):
    def __init__(self, temp_celsius=None, temp_fahrenheit=None, temp_kelvin=None):
        if temp_celsius is not None:
            self._temp = temp_celsius
        elif temp_fahrenheit is not None:
            self._temp = f_to_c(temp_fahrenheit)
        elif temp_kelvin is not None:
            self._temp = k_to_c(temp_kelvin)
        else:
            self._temp = 0

    # tmp_celsius getter
    @property
    def temp_celsius(self):
        """Temp. in Celsius"""
        return self._temp

    # tmp_celsius setter
    @temp_celsius.setter
    def temp_celsius(self, val):
        self._temp = val

    @property
    def temp_fahrenheit(self):
        """Temp. in Fahrenheit"""
        return c_to_f(self._temp)

    @temp_fahrenheit.setter
    def temp_fahrenheit(self, val):
        self._temp = f_to_c(val)

    @property
    def temp_kelvin(self):
        """Temp. in Kelvin"""
        return c_to_k(self._temp)

    @temp_kelvin.setter
    def temp_kelvin(self, val):
        self._temp = k_to_c(val)
