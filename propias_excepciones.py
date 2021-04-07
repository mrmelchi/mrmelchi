import traceback

class CustomError(Exception):
    def __init__(self, line, file):
        self.line = line
        self.file = file

    def logerror(self):
        with open('custom_error.txt', 'w') as error:
            error.write('Error ocurrido en la linea {} del archivo {}'.format(self.line, self.file))

    def __str__(self):
        return 'Error ocurrido en la linea {} del archivo {}'.format(self.line, self.file)

def funcion():
    raise CustomError(64, 'ejemplo.py')

try:
    funcion()
except CustomError as C:
    C.logerror()
    print(C)
    traceback.print_exc()

print('se sigue ejecutando el codigo'.upper())

# Ejercicio

# Crea tu propio error, que se arroje cuando un Usuario ingresa un password incorrecto.

import traceback

class InvalidPassword(Exception):
    def __init__(self, usuario):
        self.usuario = usuario

    def logerror(self):
        with open('password_error.txt', 'w') as error:
            error.write('La password ingresada por el usuario {} es invalida'.format(self.usuario))

    def __str__(self):
        return 'La password ingresada por el usuario {} es invalida'.format(self.usuario)

def password():
    usuario = input('Usuario: ')
    contraseña = input('Password: ')
    raise InvalidPassword(usuario)

try:
    password()
except InvalidPassword as I:
    I.logerror()
    print(I)
    traceback.print_exc()
