def valida_velocidad_maxima(kilometros):
    assert kilometros < 120, 'Ha sobrepasado la velocidad máxima'
    return kilometros

valida_velocidad_maxima(130)
