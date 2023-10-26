#===========================================================
# Cristian Torres Rioja
#===========================================================
#   Paradigmas de programación
#   Matemática Algoritmica
#   ESFM-IPN    oct_2023
#===========================================================

#===========================================================
#   yield transforma la funcion a iterador
#===========================================================

def migenerador():
    print("Primero")
    yield 10
    print("Segundo")
    yield "20"
    print("Tercero")
    yield "hola"


#===========================================================
#   Gen es un iterador
#===========================================================

gen = migenerador()
val1 = next(gen)
print(val1)
val2 = next(gen)
print(val2)
val3 = next(gen)
print(val3)
