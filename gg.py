class Circle:
    PI = 3.14
    def __init__(self, radio):
        self.radio = radio
        self.circunsferencia = 2 * self.PI * self.radio

inst = Circle(2)
print(inst.circunsferencia)
inst.radio = 3
print(inst.circunsferencia)

print(inst.__dict__)

class Circle:
    PI = 3.14
    def __init__(self, radio):
        self.radio = radio

    def circunsferencia(self):
        return 2 * self.PI * self.radio

inst = Circle(2)
print(inst.circunsferencia())
inst.radio = 3
print(inst.circunsferencia())

print(inst.__dict__)
class Circle:
    PI = 3.14
    def __init__(self, radio):
        self.radio = radio
    @property
    def circunsferencia(self):
        return 2 * self.PI * self.radio

inst = Circle(2)
print(inst.circunsferencia)
inst.radio = 3
print(inst.circunsferencia)

print(inst.__dict__)


class Descriptor:

    def __init__(self):
        self.name = 'attr'

    def __get__(self, inst, cls):
        return self.name

    def __set__(self, inst, value):
        self.name = value

class Clase:
    name = Descriptor()

x = Clase()
print(x.name)
x.name = 'attribute'
print(x.name)
Clase.name = 'att'
print(x.name)
print(type(x).name)
y = Clase()
y.name = 'a'
print(x.name)
print(type(x).name)
print(y.name)
print(type(y).name)

#Sigue en el ejercicio la función proporcionada
from functools import partial
def func(u,v,w,x):
    return u*4 + v*3 + w*2 + x
#Introduce tu código aquí para crear e imprimir con tu función parcial
p = partial(func, 5, 6 , 7)
print(p(8))

u=5; v=6; w=7; x=8
print(func(u, v, w, x))