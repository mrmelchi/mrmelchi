def f(a,b):
    return a*b

print(f(5,5))

l = lambda a,b: a*b
print(l(5, 5))

l = lambda x, y: x if x < y  else y
print(l(3,10))
print(l('avispa', 'avion'))
print(l('avispa', 'avión'))

def asignar(x):
    return (lambda y: y**x)

cubo = asignar(3)
print(cubo(2))

