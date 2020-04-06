# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 01:29:32 2020

@author: locopepe
"""

# Lectura del Archivo. 
text = open('c:\\Users\\locopepe\\Desktop\\Entrada.txt','r',encoding="utf-8")
ar = []

lineas = text.readlines()

for linea in lineas:
    var = linea.strip()
    x = var
    ar.append(x)

palabra = ar[0]
n = ar[1]

key = int(n)

text.close()

abc= "abcdefghijklmnopqrstuvxwyz"

cifrado = "" 

#Cifrado.
for i in palabra:
    if (i in abc):
        indice = abc.index(i)
        nuevo_indice = (indice + key) % len(abc)
        cifrado+= abc[nuevo_indice]
    else: 
        cifrado+= 1
print("Mensaje cifrado: ", cifrado)


#Decifrar  
decifrado = ""
for i in cifrado:
        if (i in abc):
            indice2 = abc.index(i)
            nuevo_indice2 = (indice2 - key) % len(abc)
            decifrado+= abc[nuevo_indice2]
        else:
            decifrado+=1
print("Mensaje decifrado: ", decifrado)

text2 = open('c:\\Users\\locopepe\\Desktop\\salida.txt','w',encoding="utf-8")

text2.write(cifrado)

text2.close()











        
