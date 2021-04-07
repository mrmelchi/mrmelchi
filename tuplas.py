# concatenación
print((1, 2, 3) + (1, 2, 3))

# repetición
print((1,2,3) * 4)

# index y slicing
a = 1, 2, 3
print(a[0], a[0:2], a[::-1])

# cast
lista = ['x', 'b', 'a', 'z']
tupla = tuple(lista)
print(tupla)

lista = sorted(tupla)
print(lista)

a = (1,2,3,1,2,3,1)
print(a.count(1))
start = a.index(1)
print(start)
start = a.index(1, start + 1)
print(start)
start = a.index(1, start + 1)
print(start)

a=(1,2,3,4,[4])
# print(a)
# a[4][0]=5
# print(a)
a[3]=5
print(a)

