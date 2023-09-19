#====================================================
#   Cristian Torres Rioja
#====================================================
#   Paradigmas de programacion
#   Matemática algoritmica
#   ESFM_IPN    sept-2023
#====================================================







#====================================================
#   Mi primera función
#====================================================

def saludo():
    #===========================================
    #Documentación rápida de la funcion
    #===========================================
    """Esta función saluda"""
    print(' ¡Quiúboles!, ¿Cómo estás?')


#====================================================
#   LLamado de la función
#====================================================

saludo()

#====================================================
#   Se ejecuta pero no se asigna
#====================================================

salida = saludo()


#====================================================
#   Esto no funciona
#====================================================

print(salida)

#====================================================
#   Mostrar documentación
#====================================================

#help(saludo)

#====================================================
#   Función con argumento
#====================================================

def salu2(nombre):
    """"Esta función te saluda por tu nombre"""
    print("¡Qué onda ese", nombre, "¡")
salu2("Julián")
salu2("Ángel")

#====================================================
#   Ahorrar trabajo del intérprete
#   Nombre:str la variable nombre es un str
#====================================================

def saludos(nombre:str):
    """Esta función te saluda por tu nombre estrictamente"""
    print("¡Qué onda ese", nombre, "!")
saludos("Cristian")
a = 123

print(type(a))
saludos(a)

#====================================================
#   Función con muchos argumentos
#====================================================

def saludos_multiples(nombre1,nombre2,nombre3):
    """Esta función saluda a 3 personas al mismo tiempo"""
    print("Hola ", nombre1,",", nombre2,"y", nombre3)
saludos_multiples("Hugo","Paco","Luis")

#====================================================
#   Fucnión con cualquier numero de argumentos
#====================================================

def muchos_saludos(*nombres):
    """Esta función saluda a todos los que quieras"""
    i = 0

    #=========================================
    #   end= es para ponerlo de corrido
    #=========================================

    print("Hola", end="")
    while len(nombres) > i:
        #Ultimo nombre
        if (i==len(nombres)-1):
            print(nombres[i])
        else:
            #Cualquier otro nombre
            print(nombres[i], end=", ")
        i+=1

muchos_saludos("Bosco","Angel","David","Tamara","Mili","Edwin","Lev","Luis","Abigail")

def greet(firstname, lastname):
    print ('Hello', firstname, lastname)

#====================================================
#    Llamar a la función con argumentos en desorden
#====================================================

greet(lastname='Jobs', firstname='Steve')

#====================================================
#   Función con argumentos escondidos **
#====================================================

def greet(**person):
    #==========================================
    #   persona tiene características firstname y lastname
    #==========================================
    print('Hello', person['firstname'], person['lastname'])

greet(firstname='Steve', lastname='Jobs')
greet(lastname='Jobs', firstname='Steve')
greet(firstname='Bill', lastname='Gates', age=55)   #Se pueden pasar mas parametros de los necesarios

#====================================================
#   Función con valores poor defecto
#====================================================

def greet(name = 'Guest'):
    print('Hello', name)

greet()     #Utiliza el valor dado de antemano
greet('Steve')

#====================================================
#   Función con resultado
#====================================================

def suma(a,b):
    return a + b


#====================================================
#   Programación funcional
#   Se pueden usar funciones dentro de funciones
#====================================================

total=suma(5, suma(10,20))
print(total)

#====================================================
#   Cálculo lambda
#   Nombre de la función = lambda variable : función
#====================================================

x_al_cuadrado = lambda x : x * x
al = x_al_cuadrado(5)
print(al)

#====================================================
#   Lambda de varias variables
#====================================================

suma = lambda x1, x2, x3: x1+x2+x3
print(suma(97,98,99))

sumas = lambda *x: x[0]+x[1]+x[2]+x[3]

print(sumas(100,200,300,400))

#====================================================
#   Uso de una fucnión anónima
#   El argumento va fuera del paréntesis
#====================================================

print((lambda x: x*x)(6))   #   función anónima

#====================================================
#   Función con variable global
#   ESVITE EL EXCESO !!!!!
#====================================================

name = 'Steve'
def greet():
    global name #Para utilizar una variable global (que viene fuera del bloque)
    name = 'Bill'
    print('Hello', name)

greet()




