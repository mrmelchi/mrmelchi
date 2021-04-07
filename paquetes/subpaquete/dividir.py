from ..multiplicar import multiplica

def divide(dividendo, divisor):
    result = dividendo / divisor
    resto = dividendo % divisor
    return ('resultado: ', result, 'resto: ', resto)

def usa_multiplica():
    return multiplica