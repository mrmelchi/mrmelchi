from typing import List

palabra = 'cena'

letra = 0
while letra < len(palabra):
    if palabra[letra] == 'z':
        print('la palabra %s contiene al menos una z' %palabra)
        break
    letra += 1
else:
    print('la palabra %s NO contiene z' %palabra)


# Crea un bucle for que recorra una lista y elimine los elementos del tipo int

lista = ['hola', 1, 4.0, 8, 14.3, 9, 'suma', 45]
for elemento in lista:
    if isinstance(elemento, int):
        lista.remove(elemento)
print(lista)

lista = ['hola', 1, 4.0, 8, 14.3, 9, 'suma', 45]
for (posicion, valor) in enumerate(lista):
    print(posicion, valor)

print('-' * 15)

d = dict(nombre='Mario Melchiori', edad=61, ocupacion='contador', salario=125000)
for posicion, (clave, valor) in enumerate(d.items()):
    print(posicion, clave, '--->', '=>', valor)

b = [[1, 2], [3, 4]]
a = zip(*b)
print(list(a))

