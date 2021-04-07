class Empleado:
    def __init__(self, nombre, puesto=None, sueldo=20000):
        self.nombre = nombre
        self.puesto = puesto
        self.sueldo = sueldo

    def aumento(self, pct):
        self.sueldo = int(self.sueldo * (1 + pct))

    def apellido(self):
        self.apellido =  self.nombre.split(' ')[-1]

    def __str__(self):
        return 'Empleado: {apellido}, Salario: {salario}'.format(apellido=self.apellido, salario=self.sueldo)

class Gerente(Empleado):
    def aumento(self, pct, bonus):
        Empleado.aumento(self, pct+bonus)


if __name__ == '__main__':
    mario = Empleado('Mario Melchiori', 'Auxiliar', 30000)
    print(mario.__dict__)
    mario.apellido()
    Empleado.aumento(mario, 0.10)
    print(mario)
    mario.__mro__()
    del mario

    federico = Empleado('Federico Eberhardt', 'Gerente', 100000)
    print(federico.__dict__)
    federico.apellido()
    Gerente.aumento(federico, 0.10, 0.10)
    print(federico)
    del federico


# ejercicio
class Persona:
    def __init__(self, nombre, id):
        self.nombre = nombre
        self.id = id

    def mostrar(self):
        print('Nombre: {nombre}, ID: {id}'.format(nombre=self.nombre, id=self.id))

class Empleado(Persona):
    def __init__(self, nombre, id, salario, cargo):
        Persona.__init__(self, nombre, id)
        self.salario = salario
        self.cargo = cargo

raul = Empleado('Raul', 886012, 200000, "Interno")

print('------ tres maneras de invocar al método mostrar ------')
raul.mostrar()
Empleado.mostrar(raul)
Persona.mostrar(raul)


# ejercicio

class Casa:
    def __init__(self, habitaciones, baño):
        self.habitaciones = habitaciones
        self.baño = baño

    def detalles(self):
        print(f'Esta propiedad tiene {self.habitaciones} habitacion/es \
con {self.baño} baño/s')

class Departamento(Casa):
    def __init__(self, habitaciones, baño, piso):
        Casa.__init__(self, habitaciones, baño)
        self.piso = piso

    def detalles(self):
        print(f'Esta propiedad tiene {self.habitaciones} habitacion/es \
con {self.baño} baño/s y está en el piso {self.piso}.')

casa = Casa(2, 1)
casa.detalles()
depto = Departamento(3, 2, 8)
depto.detalles()
