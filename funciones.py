# Crea una funcion que tome dos argumentos y devuelva el cuadrado de la multiplicacion de ambos.

def cuadrado_del_producto(a, b):
    return (a * b) ** 2

print(cuadrado_del_producto(10, 10))

print('_' * 15)

# (L)ocal (E)nclosing (G)lobal (B)uilt-in  LEGB

x = 100

def ambito_1():
    x = 200
    print(x)

print(x) # global imprime 100
ambito_1() # local imprime 200
print('_' * 15)

def ambito_2():
    global x
    x = 200
    print(x)

print(x) # global imprime 100
ambito_2() # global imprime 200
print(x)  # global imprime 200
print('_' * 15)

def ambito_3():
    y = x + 200
    print(y)

print(x) # global imprime 200. x cambió en línea 24
ambito_3() # imprime y => 400
print('_' * 15)

# import builtins
# [print(x) for x in enumerate(dir(builtins))]

# open = 'Hola'
# print(open)
# file = open('archivo.txt', 'r') # file = open('archivo.txt') idem
# file.write('esto es una prueba')
# file.close()
w = 20

def funcion_1():
    y = 109
    def funcion_2():
        # y = y + 1 # no se permite asignación salvo definir la variable como nonlocal
        nonlocal y
        y *= 10
        global z  # puedo crear una variable global que no está creada
        z = 177
        # nonlocal w # No puedo crear una variable nonlocal que no está creada
        global w
        w += 50
        print(y, z, w)
    print(y)
    return funcion_2()

accion = funcion_1()

x = 100
def global_uso():
    print(x)  # puedo imprimir la variable global x  pero no asignar

global_uso()

x = 100
def global_uso():
     # x = x * 2 # no puedo asignar
    print(x)  # puedo imprimir la variable global x  pero no asignar

global_uso()

x = 100
def global_uso():
    global x
    x = x * 2 # puedo asignar si declaro usar la global
    print(x)

global_uso()

# las asignaciones a nombres de argumentos dentro de la función no afecta al caller
aGlobal = 10
def fun(bGlobal):
    bGlobal= 20
    return bGlobal

print(fun(aGlobal))
print(aGlobal)


# cambiar un objeto mutable en la función puede afectar al caller
aGlobal = []
def fun(bGlobal):
    aGlobal.append(20)
    return bGlobal

print(fun(aGlobal))
print(aGlobal)

aGlobal = []
def fun(bGlobal):
    aGlobal = bGlobal.copy() # o [:]
    aGlobal.append(20)
    return aGlobal

print(fun(aGlobal))
print(aGlobal)
