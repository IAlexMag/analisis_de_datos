import numpy as np

# un arreglo es una estructura de datos que nos permite almanecar varios valores del mismo tipo
'''
#crear array
a = np.array([1,2,3,4,5])
print(a)
print(type(a))

#saber cuantos elementos posee un arreglo
print(a.size)
print(a.ndim)
print(a.dtype)
print(a.shape)
#hacer operaciones con los arreglos
b = a+10 # a/10 a*10 a-10 etc
print(b)
#tipos de datos con numpy-----------------------------------------------

c = np.array([1,2,4,5,6], dtype= np.complex64)
print(c)

######## creación de arreglos###############3

d = np.arange(1,10,2)
print(d)

e = np.zeros(10, dtype=float)
print(e)

f = np.ones(10, dtype=int)
print(f)

g = np.empty(10, dtype=int)
print(g)

h =np.random.randint(0,100, 50)
print(h)

print(a[1:3])

a[1] = 10
print(a[1])'''

a = np.random.randint(0,20,20)
print(a)
# para poder generar un subarreglo se puede utilizar la siguiente sintaxis
#a[start:end:jumps]

b = a[0:5:2]
print(b)

# segunda opción definir mediante un listado de indices 
c = a[[0,1,3]]
print(c)

#####33vectorizar funciones#############################
def operacion(valor):
    return (valor**2)+2


vector = np.vectorize(operacion)

print(vector(a))

d= a.copy()

#vistas
e = a.view()

#paraconocer si un objeto es una vista se puede acceder con el método base
print(e.base)
print(id(a))
print(id(e.base))


A = np.array([[1,2,3,4,5],[6,7,8,9,0],[1,2,3,4,5]])
print(A)
print(A.ndim)
print(A.shape)
print(A[0][0])

#SUBARREGLO DE A
print(A[1,2:])

#Para obtener los valores de una clumna de una matriz se utiliza la siguiente sintaxis
# arreglo[:, 3] donde : hace referencia a todos los axis0 y 3 indica el número de columna del axis1
print(A[:,2])
print(A.std())
print(A[1].sum())

#Transposición 
print(A[:,4].sum())
print(A.T[4].sum())

#condiciones de los arreglos y filtros--------------------------------
B = A[A>3]
print(B)

#operadores lógicos se le agrega las condicones entre paréntesis dentro de un corchete
B = A[(A>3)&(A<8)]
print(B)

B= A[(A>3) | (A>8) | (A==5)]  # | = OR & = AND
print(B)

#funciones ON o ANY

C = np.random.randint(0,50,50)
print(C)

#si todos los números son mayores a 10

print(np.all(C>=0)) #Verififcar si todos los elementos dentro del areeglo cumple con la condiciones establecidas

#ANY permite conocer si al enos al.gunos elementos cumplen con las condiciones establecidos
print(np.any((C>=0)&(C<=100)))

#funciones WHERE y SELECT

#-------------------------------------

calificaciones = np.random.randint(1,11,20)
print(calificaciones)

#todas las calififciones >= 7 son aprobatorias.

# 2 tipos de mensajes

# Felicidades aporbaste la materia
# Lo sentimos no has aprobado la materia

mesnajes = np.where(
    calificaciones>=7,
    'Felicidades aporbaste la materia',
    'Lo sentimos no has aprobado la materia'
)

print(mesnajes)

# 4 tipos de mensajes

condiciones = [
    (calificaciones ==10),
    ((calificaciones==8) | (calificaciones==9)),
    (calificaciones==7),
    (calificaciones<7)
]

opciones= [
    'Felicidades, aprobaste la materia con 10',
    'Felicidades aprobaste la materia',
    'Aprobaste la materia',
    'Lo sentimos no aprobaste la materia'
]

B = np.select(condiciones, opciones)
print(B)

# con where seremos capaces de alamacenar con dos tipos de datos y conselect 
# se alamacenan multi¿piles tupos de valores 
#np.savetxt('arreglo.txt', A, fmt='%i')

#-----------------leer archivo de sistema------------
file = np.loadtxt('arreglo.txt')
print(file)

re = a.reshape((2,2))
print(re)