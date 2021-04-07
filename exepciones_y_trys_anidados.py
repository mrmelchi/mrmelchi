import sys

print(dir(Exception))

# Captura por Exception
print('-' * 25)
try:
    ['abc'] + 3
    # sys.exit()
except NameError as T:
    print('Capturado por TypeError')
    print(T)
except Exception as E:
    print('Capturado por Exception')
    print(E)
except:
    print('No hereda de Exception')

# Captura por TypeError
print('-' * 25)
try:
    ['abc'] + 3
    # sys.exit()
except TypeError as T:
    print('Capturado por TypeError')
    print(T)
except Exception as E:
    print('Capturado por Exception')
    print(E)
except:
    print('No hereda de Exception')

print('-' * 25)
# Para sys.exit() funcione no debe haber ningún except: porque sino lo gestionará y no podemos salir del programa

try:
    sys.exit()
except TypeError as T:
    print('Capturado por TypeError')
    print(T)
except Exception as E:
    print('Capturado por Exception')
    print(E)
except:
    print('sys.exit() no hereda de Exception')

print('Como lo gestiona tendría que llegar aquí')
print('No tendría que existir except:')

print('-' * 25 + ' Nada debajo de esta línea se debe imprimir')
try:
    print('se comenta para que siga el código de abajo') # sys.exit()
except TypeError as T:
    print('Capturado por TypeError')
    print(T)
except Exception as E:
    print('Capturado por Exception')
    print(E)

print('Como lo gestiona tendría que llegar aquí')
print('No tendría que existir except:')

print('-' * 25)
try:
    print('primer try')
    try:
        print('segundo try')
        # raise IndexError se comenta para que siga el código de abajo
    finally:
        print('segundo finally')
finally:
    print('primer finally')

print('-' * 25)
try:
    print('primer try')

    try:
        print('segundo try')
        raise IndexError

    except TypeError:
        print('segundo except')

    print('continua bloque 2')
except:
    print('primer except')

print('continua bloque 1')

print('-' * 25)
try:
    print('primer try')
    raise IndexError

    try:
        print('segundo try')
        raise IndexError
    except:
        print('segundo except')

    print('continua bloque 2')
except:
    print('primer except')

print('continua bloque 1')