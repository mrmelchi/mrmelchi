class Generica:
    def set_data(self, data):
        self.data = data

    def mostrar(self):
        print(self.data)

    def __add__(self, yourself):
        return self.data + ' ' + yourself.data

    def __str__(self):
        return 'este objeto es de ' + self.data

x = Generica()
y = Generica()

x.set_data('Margarita')
y.set_data('Juanita')
print(x + y)
print(x)

# ejercicio
from datetime import datetime
class Empleado:
    def __init__(self, nombre, apellido, nacimiento, ingreso, cargo, salario):
        self.nombre = nombre
        self.apellido = apellido
        self.nacimiento = nacimiento
        self.ingreso = ingreso
        self.cargo = cargo
        self.salario = salario
        self.edad = datetime.now().year - self.nacimiento
        self.antiguedad = datetime.now().year- self.ingreso
        self.nombre_completo = self.nombre + ' ' + self.apellido

    def __str__(self):
        return f'Nombre Completo: {self.nombre_completo}\nEdad al finalizar el año: {self.edad}\nAntigüedad al finalizar el año: {self.antiguedad}\nCargo: {self.cargo}\nSalario: {self.salario:,}'

    def __le__(self, other):
        if self.salario <= other.salario:
            return True
        else:
            return False

mario = Empleado('Mario', 'Melchiori', 1959, 1980, 'Auviliar', 30000)
print(mario)
flavia = Empleado('Flavia', 'Gomez', 1980, 2001, 'Gerente', 150000)
print(flavia)
print(mario.salario <= flavia.salario)
print(mario.salario >= flavia.salario)
