planilla = '{0:10}, {1:10}, {2:10}'
print(planilla.format('Florencia', 'Pablo', 'Victoria'))

planilla = '{primero}, {segundo}, {tercero}'
print(planilla.format(primero='Florencia', segundo='Pablo', tercero='Victoria'))

planilla = '{2}, {1}, {0}'
print(planilla.format('Florencia', 'Pablo', 'Victoria'))

import sys

planilla = 'Mi {1[tipo]} corre sobre {0.platform} '.format(sys, {'tipo':'PC'})
print(planilla)

print('{0:10}, {1:10}'.format('primero', 12.324))
print('{0:e}   {1:.3e}   {2:g}'.format(0.000031214, 0.000031214, 0.000031214))
print('{0:o}   {1:x}   {2:b}'.format(255, 255, 255))