def fun(a, b, c):
    print(a, b, c)

print('-' * 7, 'por posición', '-' * 7)
fun(1, 2, 3)

print('-' * 7, 'por palabra clave -keyword', '-' * 7)
fun(c=3, b=2, a=1)

print('-' * 7, 'por default', '-' * 7)
def fun(a, b=2, c=3):
    print(a, b, c)
fun(1)
fun(1, c=2)
fun(1, c=2)
# fun(c=1, b=2, 3) Posicional argumento no pueden seguir a default argumentos.
fun(3, c=1, b=2)

print('-' * 7, 'por cantidad arbitrario de argumentos', '-' * 7)
print('-' * 7, 'por posición', '-' * 7)

def fun(*args):
    print(args)

fun(1, 2, 3)

print('-' * 7, 'por palabra clave -keyword', '-' * 7)
def fun(**kwargs):
    print(kwargs)

fun(a=1, b=2, c=[1, 2, 3], d = 'string')

print('-' * 7, 'uniendo todo', '-' * 7)
def fun(a, b, *args, **kwargs):
    print(a, b, args, kwargs)

fun(1, 2, 4, 5, d='string', e=3.1416)

print('-' * 7, 'argumento solo clave', '-' * 7)
def fun(a, *b, c):
    print(a, b, c)

fun(1, 2, 4, 5, c='string')

def fun(a, *, c):
    print(a, c)

fun(1, c='string')

print('-' * 7, 'orden de los argumentos', '-' * 7)
def fun(a, b, *args, c, **kwargs):
    print(a, b, args, c, kwargs)

fun(1, 2, 4, 5, c='string', d=7)

# ejercicio

def minimo(*args):
    menor = args[0]
    for item in range(1, len(args)):
        if args[item] < menor:
            menor = args[item]
    return menor

print(minimo(0,4,2,5,67,100,50))

def minimo(*args):
    menor = args[0]
    for item in args:
        if item < menor:
            menor = item
    return menor

print(minimo(0,4,2,5,67,100,50))

def funcion(nombre, apellido, *, edad, genero):
    print('Nombre y Apellido: {} {}, {} años de edad, género {}.'.format(nombre, apellido, edad, genero))

funcion('Juan', 'Perez', edad=45, genero='masculino')