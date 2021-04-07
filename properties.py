class Prop:
    def __init__(self, fget=None, fset=None, fdel=None):
        self.fget = fget
        self.fset = fset
        self.fdel = fdel

    def __get__(self, instance, owner):
        if instance is None:
            return self
        elif self.fget is None:
            raise AttributeError("unreadable attribute")
        else:
            return self.fget(instance)

    def __set__(self, instance, value):
        if self.fset is None:
            raise AttributeError("can't set attribute")
        else:
            self.fset(instance, value)

    def __delete__(self, instance):
        if self.fdel is None:
            raise AttributeError("can't delete attribute")
        else:
            self.fdel(instance)

class Cliente:
    def __init__(self, usuario):
        self._usuario = usuario

    def getUsuario(self):
        print('Recupera el usuario...')
        return self._usuario

    def setUsuario(self, valor):
        print('Modifica el usuario...')
        self._usuario = valor

    def delUsuario(self):
        print('Remueve el usuario...')
        del self._usuario

    usuario = Prop(getUsuario, setUsuario, delUsuario)

cliente1 = Cliente('Juan')
print(cliente1.usuario)
cliente1.usuario = 'Pedro'
print(cliente1.usuario)
del cliente1.usuario
print(Cliente.usuario.__doc__)
