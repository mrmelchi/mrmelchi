a = [1, 2, 3, 4, 5, 6]
por_diez = []

for elemento in a:
    por_diez.append(elemento * 10)

print(por_diez)

por_diez = [elemento * 10 for elemento in a]
print(por_diez)

print([x * y for x in [1, 2] for y in [1, 2]])
lista = ['jabon', 'agua', 'fuego', 'pc', 'kilometros', 'figura']

f = [elemento for elemento in lista if elemento[0] == 'f']
print(f)

t = [x + y for x in 'abc' for y in 'ABC']
print(t)

t = [x + y for x in 'abc' if x!='c' for y in 'ABC' if y!='C']
print(t)

# ejercicio

print([x * y for x in [1, 2] for y in [1, 2]])