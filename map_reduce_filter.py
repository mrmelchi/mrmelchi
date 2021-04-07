empleados = [dict(nombre='Mario', salario=1250, cargo='empleado'),
             dict(nombre='Pedro', salario=1250, cargo='administrativo'),
             dict(nombre='Luis', salario=5000, cargo='jefe'),
             dict(nombre='Flavia', salario=7000, cargo='gerente'),
             dict(nombre='Daniela', salario=1250, cargo='empleado')]

print(empleados)


def aumento(elemento):
    copia = elemento.copy()
    nuevo_salario = copia['salario'] + copia['salario'] * 0.10
    copia['salario'] = nuevo_salario
    return copia

nueva_lista = list(map(aumento, empleados))
print(nueva_lista)

print(list(filter(lambda elem: elem['cargo'] == 'administrativo', empleados)))
print(list(filter(lambda elem: elem['salario'] > 3000, empleados)))

from functools import reduce

salario = list(map(lambda elem: elem['salario'], empleados))
print(salario)
print(reduce((lambda x,y: x + y), salario))

print(sum(salario))

# ejercicio
empleados = [dict(nombre='Mario', salario=1250, cargo='empleado'),
             dict(nombre='Pedro', salario=1250, cargo='administrativo'),
             dict(nombre='Luis', salario=5000, cargo='jefe'),
             dict(nombre='Flavia', salario=7000, cargo='gerente'),
             dict(nombre='Daniela', salario=1250, cargo='empleado')]


def mayuscula(elemento):
    copia = elemento.copy()
    copia['nombre'] = copia['nombre'].upper()
    copia['cargo'] = copia['cargo'].upper()
    return copia

empleado = list(map(mayuscula, empleados))
print(empleado)




