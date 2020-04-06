# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 16:04:17 2020

@author: locopepe
"""

### Lectura del archivo.

text = open('c:\\Users\\locopepe\\Desktop\\fichero.txt','r',encoding="utf-8")
ar = []

lineas = text.readlines()

for linea in lineas:
    var = linea.strip()
    x = var
    ar.append(x)

palabra = ar[0]
llave = ar[1]

print(palabra)
print(llave)

text.close()

### Escritura y Salida del Archivo.

text2 = open('c:\\Users\\locopepe\\Desktop\\salida.txt','w',encoding="utf-8")

text2.write(" ")

text2.close()

