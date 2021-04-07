# from paquetes.subpaquete.dividir import divide
# from paquetes.multiplicar import multiplica, pi, usa_divide
#
# m = multiplica(10, pi)
# print(m)
# divide(10, pi)
#
# g = usa_divide()
# g(10, pi)

from paquetes.subpaquete.dividir import usa_multiplica, divide
from paquetes.multiplicar import pi, multiplica

divide(10, pi)

m = multiplica(10, pi)
print(m)

g = usa_multiplica()
print(g(10, pi))

