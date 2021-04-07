def suma_lista(lista, suma=0):
    for item in lista:
        if isinstance(item, list):
            suma = suma_lista(item, suma=suma)
        else:
            suma += item
    return suma


print(suma_lista([[1, 2], [1, 2, 3], 10, [20]]))


def suma(lista):
    if not lista:
        return 0
    else:
        return lista[0] + suma(lista[1:])


print(suma([1, 2, 10]))

def remove_string(lista):
    sin_str = []
    if lista:
        for item in range(len(lista)):
            if not isinstance(lista[item], str):
                sin_str.append(lista[item])
                print(sin_str)
            else:
                remove_string(lista[item:-1])

    return sin_str


# Crea una funcion recursiva que recorra una lista y elimine los elementos que sean string. (de clase str)

def remove_string(lista):
    sin_str = []
    if lista:
        for item in lista:
            if not isinstance(item, str):
                sin_str.append(item)
                #print(sin_str)
            else:
                print(lista.index(item))
                #remove_string(lista.index(item):-1])

    return sin_str

#print([x for x in lista if not isinstance(x,str)])
#print(lista)
# lista = ['pp', 0, 1, 'aa','bb', 'cc', 5, 6, 'hola', 'pp', 7,'ñ']
# print(lista)
# print(remove_string(lista))

def remove_str(lista, copia=list()):
    if not lista:
        return copia
    else:
        if not isinstance(lista[0], str):
            copia.append(lista[0])
    remove_str(lista[1:])
    return copia

lista = [1, 'a', 'q', 'aa','bb', 'cc', 6, 6, 'hola', 'a', 7,'ñ']
import random

random.shuffle(lista)
print(lista)
print(remove(lista))
print(lista)

