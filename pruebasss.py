# -*- coding: utf-8 -*-
"""
Created on Thu Apr  2 23:25:32 2020

@author: locopepe
"""
import random

ar1 = []

n = 2

for i in range(n):
    ar1.append([])
    for j in range(n):
        ar1[i].append(random.randint(1,5))
 
for i in range(n):
    
    for j in range(n):
        print(ar1[i][j], end= " ")
    print(" ")


for i in ar1[0:1]:
    for j in ar1[0:2]:
        print(ar1[i][j])


"""
pos_inicial = ar1[0][0]

print(' ')

print(pos_inicial)"""