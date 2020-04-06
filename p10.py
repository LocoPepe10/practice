import random 

anch_matriz = 4
alto_matriz= 4

ancho_sub = 2
alto_sub = 2

matriz = []
sub_matriz = []

acumulador = []
suma = 0

for i in range(anch_matriz):
    matriz.append([])
    for j in range(alto_matriz):
        matriz[i].append(random.randint(1,5))

for i in range(anch_matriz):
    
    for j in range(alto_matriz):
        print(matriz[i][j], end = ' ')

    print(' ')
print('')


if (anch_matriz % ancho_sub == 0 and alto_matriz % alto_sub == 0):
    
    for x in range(anch_matriz-alto_sub):
        for y in range(alto_matriz-ancho_sub):
            for i in range(ancho_sub):
                for j in range(alto_sub):
                    
                    a = x*ancho_sub + i
                    b = y*alto_sub + j
                    #print(matriz[a][b], end = ' ')
                    suma = suma + matriz[a][b]                           
                    print(a,b)
                print(' ')
            print(' ')
            acumulador.append(suma)
            
            suma = 0
else: 
    print("Error")

"""
print(acumulador)

for x in range(anch_matriz-alto_sub):
        for y in range(alto_matriz-ancho_sub):
            for i in range(ancho_sub):
                for j in range(alto_sub):
                    
                    a = x*ancho_sub + i
                    b = y*alto_sub + j
                    print(matriz[a][b], end = ' ')
                    suma = suma + matriz[a][b]                           
                    print(a,b)
                print(' ')
            
            print(' ')
                







