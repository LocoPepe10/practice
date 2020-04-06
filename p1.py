
""" 1) Ejercicio 1.

l = []
for i in range(2000,3201):
    if (i%7 == 0) and (i%5 != 0):
        l.append(str(i))

print(','.join(l)) """

"""
# 2) Ejercicio 2.

def factorial(x): 
    fact = 1 
    
    if(x == 0):
        print("El factorial es 0")
    else: 
        for i in range(1,x + 1):
            fact *=  i
    print("El factorial de",x,"es",fact)

factorial(5)
"""
"""
# 3) Ejercicio 3. 

a = int(input("Ingrese numero a procesar: "))
d = dict()

for i in range(1, a+1):
    d[i] = i*i

print(d)
"""

# 4) Ejercicio 4.
"""
lista = [] 
for i in range(10):
    lista.append(str(i))

t = tuple(lista)
print(lista) 
print(t)
"""






n = 3
d  = 3
ar = []

for i in range(n):
    ar.append([])
    for j in range(d):
        ar[i].append(i)

print(ar)




















