lista = [1, 2, 3, 4, 5]
diccionario = {'primero': 1, 'segundo': 2}
tupla = (1, 2, 'a')

for item in lista:
    print(item)

for item in diccionario:
    print(item)

for item in tupla:
    print(item)

iter_lista = iter(lista)
iter_dicci = iter(diccionario)
iter_tupla = iter(tupla)

print(iter_lista, iter_dicci, iter_tupla)

print(iter_tupla.__next__())
print(iter_tupla.__next__())
print(iter_tupla.__next__())
try:
    print(iter_tupla.__next__())
except StopIteration:
    print('StopIteration')
# ---- or ----
print(next(iter_lista))
print(next(iter_lista))
print(next(iter_lista))
print(next(iter_lista))
print(next(iter_lista))
try:
    print(next(iter_lista))
except StopIteration:
    print('StopIteration')

# --------------- generadores --------------

def cuadrado(n):
    for i in range(n):
        yield i ** 2

for i in cuadrado(5):
    print(i, end=':')

x = cuadrado(5)
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(x.__next__())
# print(x.__next__())

print(type(cuadrado))

# expresion generadora

g = (x**2 for x in range(10))
print(type(g))
print(g.__next__())
print(g.__next__())
print(g.__next__())
print(g.__next__())
print(g.__next__())
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
try:
    print(next(g))
except StopIteration:
    print('StopIteration')

print(dir(g))