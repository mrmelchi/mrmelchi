class MiResta():
    def __init__(self, valor=0):
        self.valor = valor

    def __str__(self):
        return str(self.valor)

    def __sub__(self, other):
        if isinstance(other, MiResta):
            return MiResta(self.valor - other.valor)
        else:
            return MiResta(self.valor - other)

x = MiResta(10)
y = MiResta(3)
print(x - y)
print(x - 4.77)

print('-' * 10 + 'Lista inmutable' + ('-' * 10))

class MiListaInmutable:
    def __init__(self, valor):
        self.valor = valor

    def __getitem__(self, item):
        if isinstance(item, int):
            print('Este es un índice: ', item)
            return self.valor[item]
        else:
            print('Este es un slice: ', item)
            return self.valor[item]

x = MiListaInmutable([0,2,12,3,4,5])
print(x[2])
try:
    x[2]=10
except:
    print('La clase MiListaInmutable es inmutable')

print('-' * 10 + 'Lista Mutable' + ('-' * 10))

class MiListaMutable(list):
    def __init__(self, valor):
        self.valor = valor

    def __getitem__(self, item):
        if isinstance(item, int):
            print('Este es un índice: ', item)
            return self.valor[item]
        else:
            print('Este es un slice: ', item)
            return self.valor[item]

    def __setitem__(self, item, value):
        if isinstance(item, int):
            print('Este es un índice: ', item, 'Nuevo Valor: ', value)
            self.valor[item] = value
        else:
            print('Este es un slice: ', item, 'Nuevo Valor: ', value)
            self.valor[item] = value




x = MiListaMutable([0,2,3,4,5,6])
print(x.valor)
x[2]= 120
print(x.valor)
x[3:]=[]
print(x.valor)
x.valor.append(5)
print(x.valor)

conjunto = set([2,4,2,5,6,7,4,10])
print(conjunto)
print(conjunto[3])