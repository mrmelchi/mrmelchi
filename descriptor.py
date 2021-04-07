from math import pi

class Circulo:
    def __init__(self, radio):
        self.radio = radio

    def area(self):
        print(pi * self.radio ** 2)

    def perimetro(self):
        print(2 * pi * self.radio)

    class Descriptor:
        def __init__(self):
            self._pi = pi

        def __get__(self, instance, owner):
            return self._pi

        def __set__(self, instance, value):
            return self.__dict__['_pi']

        def __delete__(self, instance):
            del self._pi

    pi = Descriptor()

circulo = Circulo(radio= 2.5)
circulo.area()
circulo.perimetro()
circulo.pi = 3.1416
print(circulo.pi)
circulo.area()
circulo.perimetro()
print(circulo.pi)
Circulo.pi = 3.1416
print(Circulo.pi)
circulo.area()
circulo.perimetro()



