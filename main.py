# This is a sample Python script.

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

print('En el jardín tengo {cantidad} flores de mi planta de {planta}'.format(planta="Jazmin", cantidad=10))
print('En el jardín tengo %(cantidad)d flores de mi planta de %(planta)s' % ({'planta':"Jazmin", 'cantidad':10}))
print("este es {1} de mi {0} con mi {2[horno]}".format("primer", "segundo", {"canillla": 2, 'horno': '5'}))
