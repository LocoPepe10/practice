# -*- coding: utf-8 -*-
"""
Created on Tue Mar 31 22:48:48 2020

@author: locopepe
"""

resultados = {
   ('Honduras', 'Chile'):    (0, 1),
   ('Espana',   'Suiza'):    (0, 1),
   ('Suiza',    'Chile'):    (0, 1),
   ('Espana',   'Honduras'): (3, 0),
   ('Suiza',    'Honduras'): (0, 0),
   ('Espana',   'Chile'):    (2, 1),
}


q1 = []
q2 = []
ar = []




def mostrar_equipos(resultados):
    
    for i  in resultados:
        tupla = (i)
        q1.append(tupla[1])
        q2.append(tupla[0])
        
    ar = q1 + q2
    
    ar_final = []
    
    for i in ar:
        if (i not in ar_final):
            ar_final.append(i)
    
    print(ar_final)

mostrar_equipos(resultados)

