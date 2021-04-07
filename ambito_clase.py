class Ambitos():
    attr_clase = 55

    def instancia(self):
        variable_local = 22
        print('El método instancia imprime variable Local: %d' %variable_local)
        self.attr_instancia = 11


ejemplo = Ambitos()
print(Ambitos.attr_clase)
ejemplo.instancia()
Ambitos.instancia(ejemplo)
print(ejemplo.attr_instancia)
