#===========================================================
# Cristian Torres Rioja
#===========================================================
#   Paradigmas de programación
#   Matemática Algoritmica
#   ESFM-IPN    Dic_2023
#===========================================================

#===========================================================
#   Uso de tuberias para comunicación
#===========================================================

from multiprocessing import Process, Pipe

#===========================================================
#   Manda vector
#===========================================================

def f(extremo):
    extremo.send([0,1,2,3,4])
    extremo.close()

#===========================================================
#   Recibe vector y le suma 100 a cada componente
#===========================================================

def g(extremo):
    a = extremo.recv()
    for i in a:
        a[i] += 100
    print(a)
    extremo.close()


#===========================================================
#   Programa principal
#===========================================================
if __name__ == "__main__":

    #=======================================================
    #   Tuberia con sus extremos
    #=======================================================
    extremo1, extremo2 = Pipe()

    #=======================================================
    #   Instanciar procesos (target es la funcion)
    #       (args son los argumentos de la función)
    #=======================================================
    proceso1 = Process(target=f, args=(extremo1,))
    proceso2 = Process(target=g, args=(extremo2,))

    #=======================================================
    #   Comenzar procesos
    #=======================================================
    proceso2.start()
    proceso1.start()
    #=======================================================
    #   Esperar a que terminen los procesos
    #=======================================================
    proceso1.join()
    proceso2.join()
