#===========================================================
# Cristian Torres Rioja
#===========================================================
#   Paradigmas de programación
#   Matemática Algoritmica
#   ESFM-IPN    Dic_2023
#===========================================================

#===========================================================
#   Broadcast con MPI
#   distribución de datos
#===========================================================

from mpi4py import MPI
import numpy

#   objeto comunicador

comm = MPI.COMM_WORLD

#   quien soy

rank = comm.Get_rank()

#===========================================================
#   El proceso 0 tiene datos y los otros no
#===========================================================

if rank == 0:
    data = {'key1' : [7, 2.72, 2+3],
            'key2' : ( 'abc', 'xyz')}

else:
    data = None

#===========================================================
#   Enviar diccionario a todos los procesos desde root
#===========================================================

data = comm.bcast(data, root=0)
print(data)

#===========================================================
#   Ahora más rápido usando numpy
#===========================================================
#   tamaño del arreglo
n = 10
if rank == 0:
    #   Arreglo de enteros de 0 al n-1
    data = numpy.arange(n, dtype='i')

else:
    data = numpy.empty(n, dtype='i')

#===========================================================
#   Broadcast pro que pide el tupo de dato
#   Optimizado para comunicación rápida
#===========================================================

comm.Bcast([data,MPI.INT], root=0)

#===========================================================
#   Asegurarse que todo salió bien
#===========================================================

for i in range(n):
    assert data[i] == i

print(data)

