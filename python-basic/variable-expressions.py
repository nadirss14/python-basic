# DECLARACION DE VARIABLES
# -*- coding: utf-8 -*-
print('hola ' + 'hola!!')
print('hola, '*3 +'hola!!!')

PI= 3.1416

try:
    pass
    ratio=float(input('¿Cual es el radioñ?\n'))
    areaCircle= PI * (float(ratio)**2)
    print("El area del circulo con radio ", PI, " es: ",areaCircle)
except:
    pass
    print('El valor del radio debe ser numerico')