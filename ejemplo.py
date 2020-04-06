#from random import randint, uniform,random
import random
"""
ar1 = []
n = 4
m = 4


for i in range (n):
    ar1.append([])
    for j in range (m):
        ar1[i].append(random.randint(0, 100))

for i in range(n):
    for j in range (len(ar1[i])):
        print (ar1[i][j], end= " ")
    print ('')
"""       

ar2= []
f = int(input("Ingrese la cantidad de Filas: "))
c = int(input("Ingrese la cantidad de Columnas: "))

#Agregar Numeros en matriz (fxc)
for i in range(f): 
    ar2.append([])
    for j in range(c):
        ar2[i].append(i)
    
#Mostrar (fxc)

for i in range (f):
    for j in range (c):
        print(ar2[i][j], end = " ")
    print(' ')
    
    
