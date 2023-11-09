#===========================================================
# Cristian Torres Rioja
#===========================================================
#   Paradigmas de programación
#   Matemática Algoritmica
#   ESFM-IPN    Nov_2023
#===========================================================

#===========================================================
#   Gráficos usando la tortuga que pinta al cambiar
#===========================================================

import turtle
tortuga = turtle.Turtle()
tortuga.left(90)    #Giro a la izquierda de 90 grados
tortuga.speed(500)  #Velocidad de la tortuga

tortuga1 = turtle.Turtle()
tortuga1.left(-90)
tortuga1.speed(500)

#===========================================================
#   Con ángulos de 90 es un árbol H
#===========================================================

angulo: float = 90
angulo1: float = -90
#===========================================================
#   El arbol se construye con recursividad
#===========================================================

def arbol(i:float, angulo:float):
    if i<10.0:
        return
    else:
        tortuga.forward(i)  #Camina i
        tortuga.left(angulo)    #Gira a la izquierda 90 grados
        arbol(3.0*i/4.25,angulo)    #pide otro arbol y cambia la longitud del paso

        tortuga.right(2*angulo) #gira a la derecha 180
        arbol(3.0*i/4.25,angulo)
        tortuga.left(angulo)
        tortuga.backward(i)


def arbol1(i:float, angulo1:float):
    if i<10.0:
        return
    else:
        tortuga1.forward(i)
        tortuga1.left(angulo1)
        arbol1(3.0*i/4.25,angulo1)

        tortuga1.right(2*angulo)
        arbol1(3.0*i/4.25,angulo1)
        tortuga1.left(angulo1)
        tortuga1.backward(i)



arbol(150,angulo)
arbol1(150,angulo1)
turtle.done()


