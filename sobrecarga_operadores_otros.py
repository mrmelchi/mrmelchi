class Iterable_Cuadrado():
    def __init__(self, start, stop):
        self.value = start - 1
        self.stop = stop

    def __iter__(self):
        return self

    def __next__(self):
        if self.value == self.stop:
            raise StopIteration
        else:
            self.value += 1
            return self.value ** 2


for item in Iterable_Cuadrado(0, 10):
    print(item)

# -----------__getattr__ __setattr__ -----------

class Operadores:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def __getattr__(self, item):
        return object.__getattribute__(self, item)

    def __setattr__(self, item, value):
        if item == 'edad':
            return object.__setattr__(self, item, 32)
        else:
            return object.__setattr__(self, item, value)

    def __eq__(self, other):
        if self == other:
            return True
        else:
            return False

x = Operadores('Javier', 55)
print(x.nombre)
print(x.edad)
x.nombre = 'Pedro'
x.edad = 45
print(x.nombre)
print(x.edad)

x = Operadores('Javier', 55)
y = Operadores('Pedro', 33)

print(x.nombre==y.nombre)
print(x.edad==y.edad)
print('---------------------------------------------------------------------')
class Persona:
    def __init__(self, nombre):
        self._nombre = nombre

    def __getattr__(self, atributo):
        print('get attr: ' + atributo + ' ' + self._nombre)
        if atributo == 'nombre':
            return self._nombre
        else:
            raise AttributeError(atributo)

    def __setattr__(self, atributo, valor):
        print('set attr: ' + atributo + ' ' + valor)
        if atributo == 'nombre':
            atributo = '_nombre'
        self.__dict__[atributo] = valor

    def __delattr__(self, atributo):
        print('del: ' + atributo)
        if atributo == 'nombre':
            atributo = '_nombre'

        del self.__dict__[atributo]


persona1 = Persona('Juan')
print(persona1.nombre)
persona1.nombre = 'Pedro'
del persona1.nombre