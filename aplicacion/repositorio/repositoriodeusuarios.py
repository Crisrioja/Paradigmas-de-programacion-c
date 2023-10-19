#===========================================================
# Cristian Torres Rioja
#===========================================================
#   Paradigmas de programación
#   Matemática Algoritmica
#   ESFM-IPN    oct_2023
#===========================================================

from aplicacion.modelos.usuario import Usuario

#===========================================================
#   Este objeto es una interface
#===========================================================

class RepositorioDeUsuarios:
    def abrir(mi)->None:
        pass
    def guardar(mi,usuario:Usuario)->None:
        pass
    def cerrar(mi)->None:
        pass
