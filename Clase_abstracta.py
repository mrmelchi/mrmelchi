class BaseAuto():
    def delegar(self):
        self.acelerar()

    def acelerar(self):
        assert False, 'Tienes que escribir el método acelerar'

class Auto(BaseAuto):
    pass

auto= Auto() # Puede instanciar y no da error
#print(auto.delegar()) # da error porque no se escribió acelerar

from abc import ABCMeta, abstractmethod

class BaseAuto(metaclass=ABCMeta):
    @abstractmethod
    def acelerar(self):
        pass

class Auto(BaseAuto):
    def __init__(self):
        self.data = 'Estamos heredando de una clase abstracta'

    def acelerar(self):
        print(self.data)

auto = Auto() # pruebe sin crear acelerar metodo en clase Auto da: TypeError: NO PUEDO INSTANCIAR
           # Can't instantiate abstract class Auto with abstract methods acelerar
auto.acelerar()

