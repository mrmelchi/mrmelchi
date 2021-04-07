# d = {'nombre': 'Mario Melchiori', 'edad': 61, 'ocupacion': 'contador', 'salario': 125000}
d = dict(nombre='Mario Melchiori', edad=61, ocupacion='contador', salario=125000)

print(d)
print(d['nombre'])
print(len(d))
print('apellido' in d)
print('edad' in d)
print(list(d.keys()))
print(list(d.values()))
print(list(d.items()) [0][1])
d['salario'] = 200000
d['trabajo'] = ['ecommerce', 'blog']
print(d)
del d['trabajo']
print(d)
print(d.get('nombre'))
print(d.get('apellido'))
d2 = {'domicilio':'Mitre 2833', 'antigüedad':41}
print(d2)
d.update(d2)
print(d)
d.pop('antigüedad')
print(d)
g = d.copy()
print(g is d)
print(g == d)
d = {"salario":12000, "area": "Desarrollo", "antiguedad": 7 }
d.update( {"antiguedad": 8} )
print(d)