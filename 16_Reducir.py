#===========================================================
# Cristian Torres Rioja
#===========================================================
#   Paradigmas de programación
#   Matemática Algoritmica
#   ESFM-IPN    oct_2023
#===========================================================

#===========================================================
#   Uso de reducciones (colapsar resultados)
#===========================================================

#===========================================================
#   Mutiplicación de todos los números en la lista
#===========================================================

from functools import reduce

bigdata = [2,3,5,7,11,13,17,19,29]

#===========================================================
#   Fucnión x*y
#===========================================================

multiplicar = lambda x,y: x*y
suma = lambda x,y: x+y

print(reduce(multiplicar,bigdata))
print(reduce(suma,bigdata))

#===========================================================
#   Reduce le aplica la función por pares a los resultados y 
#   El siguiente elemento comenzando con los dos primeros
#   elementos
#===========================================================
