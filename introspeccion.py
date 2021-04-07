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
    def __init__(self, nombre, sueldo):
        Empleado.__init__(self, nombre, 'Gerente', sueldo)

    def aumento(self, pct, bonus):
        Empleado.aumento(self, pct+bonus)

    def __str__(self):
        return 'Gerente: {apellido}, Salario: {salario}'.format(apellido=self.apellido, salario=self.sueldo)



if __name__ == '__main__':
    federico = Gerente('Federico Eberhardt', 100000)
    print(federico.__dict__)
    federico.apellido()
    Gerente.aumento(federico, 0.10, 0.10)
    print(federico)
    print(federico.__class__)
    print(federico.__class__.__name__)
    print(federico.__class__.__bases__)
    print(federico.__class__.__dict__)
    print(federico.__dict__)

    for key in federico.__dict__:
        print(key , ' => ', getattr(federico, key))
        print(key, ' => ', federico.__dict__[key])

    print(federico.__class__.__bases__)





