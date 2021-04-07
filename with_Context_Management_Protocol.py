with open('data.txt', 'w') as data:
    data.write('Utilizando With!!')


with open('data.txt') as data, open('data_new.txt', 'w') as new:
    texto = data.read()
    print(texto)
    new.write(texto)

class Traceback():
    def mensaje(self, arg):
        print('Ejecutando: ' + arg)

    def __enter__(self):
        print('Entrando al bloque with')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is None:
            print('Saliendo del bloque with sin excepciones')
        else:
            print('Ocurrió un error: ' + str(exc_type) + '==' + str(exc_val) + '==' + str(exc_tb))
            return False

with Traceback() as tb:
    tb.mensaje('Nuestra instancias Traceback')
    print('Aquí no huvo excepciones')

with Traceback() as tb:
    tb.mensaje('Nuestra instancias Traceback')
    raise NameError

'''
import contextlib

@contextlib.contextmanager
def my_context():
    print('Welcome!')
    yield
    print('Bye!')

with my_context():
    print('I am always executed before the yield keyword\n')
print('I am always executed after the yield keyword')

import time

@contextlib.contextmanager
def timer():
    # Start the timer
    start = time.time()
    # context breakdown
    yield
    # End the timer
    end = time.time()
    # Tell the user how much time elapsed
    print(f'This code block executed in {end - start} seconds.')

with timer():
    for i in range(10):
        time.sleep(0.05)
print('Done!')

@contextlib.contextmanager
def read_only(path_to_file):
    # Open the file
    file = open(path_to_file, 'r')
    # Context breakdwon
    yield file
    # Close the file
    file.close()

with read_only('data.txt') as file:
    print('Printing the contents of the file\n')
    print(file.read())
'''
