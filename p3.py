# -*- coding: utf-8 -*-
"""
Created on Tue Mar 31 02:01:10 2020

@author: locopepe
"""


""" Menu interactivo: 

Alumnos de un colegio: 
    Datos - > Nombre, Edad.
    
1)Leer datos.
2) Mostrar datos.
3) Promedio nota.
4) Buscar nota.
5) Salir
   

"""

#Definiendo las variables. 
nom = []
nota = []
conta_notas = 0
conta_alumnos = 0


while(True): 

    print("###### Bienvenidos al Sistema Curricular ###### ")
    print("-------------------------------------------------")
    print("1)Leer datos.")
    print("2) Mostrar datos.")
    print("3) Promedio nota.")
    print("4) Buscar nota.")
    print("5) Salir")
    op = int(input("Ingrese opcion segun se quiera proceder..."))
    
    
    if(op == 1): 
        #1 Leer datos
        z = int(input("Cuantos Alumnos se desea ingresar?: "))
        
        for i in range(z): 
           
            x = input("Ingrese Nombre del alumno: ")
            nom.append(x)
            y = float(input("Ingrese la nota del Alumn: ")) 
            nota.append(y)
            conta_notas += y
            conta_alumnos += 1       

    if(op == 2): 
    #2 Mostrar datos.
        for l in range (0, len(nom)): 
            print("Alumno: ",nom[l]," - ","Nota:",nota[l])
        
        if(op == 3): 
        #3 Promedio de notas.
            suma = 0
            for g in range (0,len(nota)):
                suma = suma + nota[g]
        
            promedio = suma/conta_notas
    
    if(op == 4): 
    #4 Buscar nota de Alumno.

        alumno_nota = input("Ingrese el nombre del alumno que quiere visualizar: ")
        for i in range(0, len(nom)):
            if(nom[i] == alumno_nota):
                print("El alumno",nom[i],"posee un promedio de",nota[i])
            else:
                print("Alumno no encontrado.")
        
    if(op == 5):
        
        print("Adios!")          
        break
        
       








        






