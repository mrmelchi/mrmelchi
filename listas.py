a = [1, 2, 3]
print(len(a))
b = [4, 5, 6]
print(a + b)
print(a * 4)
lista = ['huevos', 'Huevos', 'HUEVOS']
print(lista[2])
print(lista[1:])
print(lista[-2])
print(lista[::-1])

m = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(m[0])
print(m[0][2])

lista[1] = 'leche'
print(lista)
lista[0:2] = ['pan', 'cebolla', 'tomate']
print(lista)
lista[0:1] = []
print(lista)
lista = ['huevos', 'Huevos', 'HUEVOS']
lista.append('leche')
print(lista)
lista.sort()
print(lista)
lista.sort(reverse=True)
print(lista)