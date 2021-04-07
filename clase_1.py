class Auto:
    def __init__(self, marca, modelo, velocidad):
        self.marca = marca
        self.modelo = modelo
        self.velocidad = velocidad

    def acelerar(self, km):
        self.velocidad += km
        return self.velocidad

auto = Auto('Fiat','Palio', 0)
print(auto.marca)
print(auto.modelo)
print(auto.velocidad)
print(auto.acelerar(10))

print(auto.__dict__)
print(auto.__class__)

# ejercicio

class Mesa:
    def __init__(self, material, patas, capacidad, largo, ancho, color, ubicacion=[0,0], estado=0):
        self.material = material
        self.patas = patas
        self.capacidad = capacidad
        self.ancho = ancho
        self.largo = largo
        self.color = color
        self.ubicacion = ubicacion
        self.estado = estado

    def mover(self, largo=0, ancho=0):
        self.ubicacion[0] += largo
        self.ubicacion[1] += ancho

    def pintar(self, color):
        self.color = color

    def ocupar(self, estado):
        self.estado = estado

mesa = Mesa(material='madera', patas=4, capacidad=6, largo=2.5, ancho=1.4, color='marrón')
print(mesa.material, mesa.patas, mesa.capacidad, mesa.largo, mesa.ancho, mesa.color, mesa.ubicacion, mesa.estado)

mesa.mover(largo=1, ancho=0.5)
mesa.pintar(color='blanco')
mesa.ocupar(estado=1)

print(mesa.material, mesa.patas, mesa.capacidad, mesa.largo, mesa.ancho, mesa.color, mesa.ubicacion, mesa.estado)


