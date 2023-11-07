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
tortuga.left(75)    #Giro a la izquierda de 90 grados
tortuga.speed(100)  #Velocidad de la tortuga

#===========================================================
#   Con ángulos de 90 es un árbol H
#===========================================================

angulo: float = 75

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


arbol(150,angulo)
turtle.done()


