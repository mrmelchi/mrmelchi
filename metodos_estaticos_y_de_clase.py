class Programadores():
    cantidad = 0

    def __init__(self, nombre):
        self.nombre = nombre
        self.habilidad = []
        Programadores.cantidad += 1


    def nueva_habilidad(self, habilidad):
        self.habilidad.append(habilidad)

    def metodo_estatico():
        print('Cantidad de programadores: ', Programadores.cantidad)

    metodo_estatico = staticmethod(metodo_estatico) # Para poder llamar el metodo estático desde la instancia
                                                    # si se comenta esta líne la linea 28 da error

    def metodo_de_clase(cls):
        cls.metodo_estatico()

    metodo_de_clase = classmethod(metodo_de_clase)  # Para poder llamar el metodo de clase desde la clase
    # si se comenta esta líne la linea 33 da error

if __name__ == '__main__':
    mario = Programadores('mario')
    mario.nueva_habilidad('Python')
    mario.nueva_habilidad('HTML')
    pablo = Programadores('pablo')
    pablo.nueva_habilidad('Java')
    print(mario.habilidad)
    print(pablo.habilidad)
    Programadores.metodo_estatico()
    mario.metodo_estatico()  # no da error solo si existe la linea 16
    Programadores.metodo_de_clase()
    mario.metodo_de_clase()
    pablo.metodo_de_clase()
