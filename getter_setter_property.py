# ejercicio

class Casa:
    def __init__(self, habitaciones, baños, direccion, valor):
        self.habitaciones = habitaciones
        self.baños = baños
        self._direccion = direccion
        self.valor = valor

    @property
    def direccion(self):
        return self._direccion

    @direccion.setter
    def direccion(self, valor):
        if len(valor) <= 2:
            print('La dirección es inválida')
        else:
            self._direccion = valor

house = Casa(habitaciones=4, baños=2, direccion='Mitre 2833', valor=100000)
print(house.direccion)
house.direccion ='--'
print(house.direccion)
house.direccion ='25 de Mayo 1780'
print(house.direccion)

