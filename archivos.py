file = open('archivo.txt', 'w')
file.write('Primera linea\n')
file.write('Segunda linea\n')
file.close()

file = open('archivo.txt', 'r') # file = open('archivo.txt') idem
print(file.readline())
print(file.readline())
print(file.readline())

file.seek(0) # se posiciona en la primer fila
print(file.read())
file.close()

file2 = open('nuevo_archivo.txt', 'w')
a, b, c, d, f, g = (1, 2, 3, 'Hola', [23, 16, 28], {'clave': 156})
file2.write('{}, {}, {}\n'.format(str(a),str(b), str(c)) + d + '\n' + str(f) + '\n' + str(g) + '\n')
file2.close()

file2 = open('nuevo_archivo.txt')
file2.read()
print(file2.read())
file2.close()

file3 = open('nuevo_archivo.txt')
linea_1 = eval(file3.readline())
linea_2 = file3.readline()
linea_3 = eval(file3.readline())
linea_4 = eval(file3.readline())
print(linea_1, type(linea_1))
print(linea_2, type(linea_2))
print(linea_3, type(linea_3))
print(linea_4, type(linea_4))
file3.close()


# ejercicio
file = open('archivo.txt', 'w')
file.write('Primera línea\n')
file.write('Segunda línea\n')
file.write('Tercera línea\n')
file.close()

file = open('archivo.txt', 'r') # file = open('archivo.txt') idem
for pasada in range(3):
    file.seek(0) # se posiciona en la primer fila
    raya = '-' * 10
    print(raya , pasada + 1 , raya)
    print(file.readline(), end='')
    print(file.readline(), end='')
    print(file.readline(), end='')

file.close()

import pickle
d = dict(nombre='Mario Melchiori', edad=61, ocupacion='contador', salario=125000)
file = open('archivo,pkl', 'wb')
escribe = pickle.dump(d, file)
file.close()

file = open('archivo,pkl', 'rb')
lee = pickle.load(file)
print(lee, type(lee))
file.close()

import json
j = json.dumps(d)
print(j, type(j))
p = json.loads(j)
print(p, type(p))

# ejercicio
import pickle
d = dict(nombre='Juan Perez', edad=25, ocupacion='contador', salario=125000)
file = open('archivo,pkl', 'wb')
escribe = pickle.dump(d, file)
file.close()

file = open('archivo,pkl', 'rb')
lee = pickle.load(file)
print(lee, type(lee))
file.close()