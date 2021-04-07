def remove_str(lista, copia=list()):
    if not lista:
        return copia
    else:
        if not isinstance(lista[0], str):
            copia.append(lista[0])

        return remove_str(lista[1:], copia=copia)



lista = [1, 'a', 'q', 'aa','bb', 'cc', 6, 6, 'hola', 'a', 7,'ñ']
import random
lista = random.sample(lista, random.randint(0,len(lista)))
print(lista)
print(remove_str(lista))
print(lista)