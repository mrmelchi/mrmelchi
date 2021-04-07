class Generica:
    def set_data(self, data):
        self.data = data

    def mostrar(self):
        print(self.data)

x = Generica()
y = Generica()

x.set_data('hola')
y.set_data(123)

x.mostrar()
y.mostrar()

x.nuevo_attrib = 10
print(x.nuevo_attrib)

print(x.__dict__) # no considera los metodos, por ejemplo mostrar()
print(y.__dict__)

print(x.__class__)
print(y.__class__)

